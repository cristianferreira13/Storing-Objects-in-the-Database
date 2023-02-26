from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///pizza_orders.db', echo = True)

Session = sessionmaker(bind = engine)

Base = declarative_base()

class OrderPizza(Base):
    __tablename__ = "order_pizza"
    
    id = Column(Integer, primary_key = True)
    size = Column(String)
    toppings= Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    
    def __init__(self, size, toppings, price, quantity):
        self.size = size
        self.toppings = toppings
        self.price = price
        self.quantity = quantity
        
class OrderPizza(Base):
    def saveIn(self):
        session = Session()
        session.add(self)
        session.commit()
        
        
class OrderPizza(Base):
    @staticmethod
    def all():
        session: Session()
        return session.query(OrderPizza).all()




order = OrderPizza('large', 'pepperoni', 15, 1)
order.save()
numberOfOrders = OrderPizza.all()
for order in numberOfOrders:
    print(order.id,order.size, order.toppings, order.price, order.quantity)