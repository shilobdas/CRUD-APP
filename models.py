from sqlalchemy import Column, String, Text
from database import Base

class ProductData(Base):
    __tablename__ = "product_data"

    uniq_id = Column("Uniq Id", String(255), primary_key=True)
    product_name = Column("Product Name", Text)
    brand_name = Column("Brand Name", String(255))
    asin = Column("Asin", String(255))
    category = Column("Category", Text)
    upc_ean_code = Column("Upc Ean Code", String(255))
    list_price = Column("List Price", Text)
    selling_price = Column("Selling Price", Text)
    quantity = Column("Quantity", Text)
    model_number = Column("Model Number", String(255))
    about_product = Column("About Product", Text)
    product_specification = Column("Product Specification", Text)
    technical_details = Column("Technical Details", Text)
    shipping_weight = Column("Shipping Weight", String(255))
    product_dimensions = Column("Product Dimensions", String(255))
    image = Column("Image", Text)
    variants = Column("Variants", Text)
    sku = Column("Sku", String(255))
    product_url = Column("Product Url", Text)
    stock = Column("Stock", Text)
    product_details = Column("Product Details", Text)
    dimensions = Column("Dimensions", String(255))
    color = Column("Color", String(255))
    ingredients = Column("Ingredients", Text)
    direction_to_use = Column("Direction To Use", Text)
    is_amazon_seller = Column("Is Amazon Seller", String(10))
    size_quantity_variant = Column("Size Quantity Variant", Text)
    product_description = Column("Product Description", Text)

    