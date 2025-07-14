from flask import Flask

from flask_sqlalchemy import SQLAlchemy 

ops = Flask(__name__)

ops.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"

# optional
ops.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

dbms = SQLAlchemy(ops) 



  
# association table , tabel name - , coln's name , referencing customers.id , products.id
customer_product = dbms.Table( "customer_product" , 
        dbms.Column("customer_id" , dbms.Integer , dbms.ForeignKey('customers.id')) , 

        dbms.Column("product_id" , dbms.Integer , dbms.ForeignKey('products.id'))  )


class Cust(dbms.Model) :

    __tablename__ = "customers"

    id = dbms.Column(dbms.Integer , primary_key = True )
    name = dbms.Column(dbms.String(45) , nullable = False )

    email = dbms.Column(dbms.String(45) , nullable = False , unique=True )

# class name and ass'n table name                      # for the sqlalchemy to know 
    items = dbms.relationship("Prod" , backref="owners" , secondary = customer_product)


    def __repr__ (self):
        return f" Customers ( '{self.name}' , '{self.email}' ) "
 

class Prod(dbms.Model) :

    __tablename__ = "products"


    id = dbms.Column(dbms.Integer , primary_key = True )
    product = dbms.Column(dbms.String(45) , nullable = False )

    price = dbms.Column( dbms.Integer, nullable = False )

    def __repr__ (self):
        return f" Customers ( '{self.product}' , '{self.price}' ) "



if __name__ == "__main__" :

    ops.run(debug=True)



# foreign key - in Prod :- it should have customer_id , as 
# one customer can have many product , also product_id
# for in Cust as they can purchase many products