class Shop:
    cart=[] #Class Attributes
    def __init__(self,buyer) -> None:
        self.buyer = buyer
    
    def add_to_cart(self,item):

        self.cart.append(item)

rana= Shop('Rana')
rana.add_to_cart('shoes')
rana.add_to_cart('phone')
print(rana.cart)

niso= Shop('niso')
niso.add_to_cart('cap')
niso.add_to_cart('watch')
print(niso.cart)