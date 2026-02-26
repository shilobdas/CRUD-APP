from pydantic import BaseModel
from typing import Optional

class ProductDataCreate(BaseModel):
    uniq_id: str
    product_name: Optional[str] = None
    brand_name: Optional[str] = None
    asin: Optional[str] = None
    category: Optional[str] = None
    upc_ean_code: Optional[str] = None
    list_price: Optional[str] = None
    selling_price: Optional[str] = None
    quantity: Optional[str] = None
    model_number: Optional[str] = None
    about_product: Optional[str] = None
    product_specification: Optional[str] = None
    technical_details: Optional[str] = None
    shipping_weight: Optional[str] = None
    product_dimensions: Optional[str] = None
    image: Optional[str] = None
    variants: Optional[str] = None
    sku: Optional[str] = None
    product_url: Optional[str] = None
    stock: Optional[str] = None
    product_details: Optional[str] = None
    dimensions: Optional[str] = None
    color: Optional[str] = None
    ingredients: Optional[str] = None
    direction_to_use: Optional[str] = None
    is_amazon_seller: Optional[str] = None
    size_quantity_variant: Optional[str] = None
    product_description: Optional[str] = None

class ProductDataUpdate(BaseModel):
    product_name: Optional[str] = None
    brand_name: Optional[str] = None
    asin: Optional[str] = None
    category: Optional[str] = None
    upc_ean_code: Optional[str] = None
    list_price: Optional[str] = None
    selling_price: Optional[str] = None
    quantity: Optional[str] = None
    model_number: Optional[str] = None
    about_product: Optional[str] = None
    product_specification: Optional[str] = None
    technical_details: Optional[str] = None
    shipping_weight: Optional[str] = None
    product_dimensions: Optional[str] = None
    image: Optional[str] = None
    variants: Optional[str] = None
    sku: Optional[str] = None
    product_url: Optional[str] = None
    stock: Optional[str] = None
    product_details: Optional[str] = None
    dimensions: Optional[str] = None
    color: Optional[str] = None
    ingredients: Optional[str] = None
    direction_to_use: Optional[str] = None
    is_amazon_seller: Optional[str] = None
    size_quantity_variant: Optional[str] = None
    product_description: Optional[str] = None

    class Config:
        from_attributes = True

class ProductDataResponse(BaseModel):
    uniq_id: str
    product_name: Optional[str]
    brand_name: Optional[str]
    selling_price: Optional[str]
    category: Optional[str]
    stock: Optional[str]

    class Config:
        from_attributes = True