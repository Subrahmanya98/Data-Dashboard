import uvicorn
from products import Product;
from fastapi import FastAPI,Request;


application = FastAPI()


if __name__=='__main__':
    uvicorn.run("app:application",host='0.0.0.0',port=4500, reload=True)

 
Pro_data=[];
@application.get('/product')
async def get_product(request:Request):
    return Pro_data;

@application.post('/product')
async def post_product(request:Request, products:Product):
    products.name = products.name + " 33"
    products.description=products.description + "44"
    Pro_data.append(products)
    return products


