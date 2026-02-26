from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import ProductData
from schemas import ProductDataCreate, ProductDataUpdate, ProductDataResponse
from typing import List, Optional

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Data CRUD API")

# CREATE 
@app.post("/products", response_model=ProductDataResponse)
def create_product(product: ProductDataCreate, db: Session = Depends(get_db)):
    """Add a new product"""
    db_product = ProductData(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# READ ALL 
@app.get("/products", response_model=List[ProductDataResponse])
def get_all_products(
    skip: int = Query(0, description="Skip rows"),
    limit: int = Query(100, description="Limit rows"),
    db: Session = Depends(get_db)
):
    """Get all products with pagination"""
    products = db.query(ProductData).offset(skip).limit(limit).all()
    return products

# READ BY ID 
@app.get("/products/{uniq_id}", response_model=ProductDataResponse)
def get_product_by_id(uniq_id: str, db: Session = Depends(get_db)):
    """Get product by Uniq Id"""
    product = db.query(ProductData).filter(ProductData.uniq_id == uniq_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# UPDATE Product

@app.put("/products/{uniq_id}", response_model=ProductDataResponse)
def update_product(uniq_id: str, product: ProductDataUpdate, db: Session = Depends(get_db)):
    """Update product by Uniq Id"""
    db_product = db.query(ProductData).filter(ProductData.uniq_id == uniq_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

#  PATCH (Partial Update) 
# @app.patch("/products/{uniq_id}", response_model=ProductDataResponse)
# def patch_product(uniq_id: str, product: ProductDataUpdate, db: Session = Depends(get_db)):
#     """Partially update product by Uniq Id"""
#     db_product = db.query(ProductData).filter(ProductData.uniq_id == uniq_id).first()
#     if not db_product:
#         raise HTTPException(status_code=404, detail="Product not found")
    
#     update_data = product.dict(exclude_unset=True)
#     for key, value in update_data.items():
#         setattr(db_product, key, value)
    
#     db.commit()
#     db.refresh(db_product)
#     return db_product


@app.patch("/products/{uniq_id}", response_model=ProductDataResponse)
def patch_product(uniq_id: str, product: ProductDataUpdate, db: Session = Depends(get_db)):
    """Partially update product by Uniq Id"""
    db_product = db.query(ProductData).filter(ProductData.uniq_id == uniq_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

#  DELETE 
@app.delete("/products/{uniq_id}")
def delete_product(uniq_id: str, db: Session = Depends(get_db)):
    """Delete product by Uniq Id"""
    db_product = db.query(ProductData).filter(ProductData.uniq_id == uniq_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": f"Product {uniq_id} deleted successfully"}

# SEARCH 
@app.get("/products/search/by-name")
def search_by_name(name: str, db: Session = Depends(get_db)):
    """Search products by name"""
    products = db.query(ProductData).filter(ProductData.product_name.ilike(f"%{name}%")).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products

# ROOT 
@app.get("/")
def root():
    return {"message": "Welcome to Product Data CRUD API! Go to /docs for Swagger UI"}