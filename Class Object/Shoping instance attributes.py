class Shop:
    shoping_mall = 'jamiuna'
    def __init__(self,buyer) -> None:
        self.buyer = buyer
        self.cart = [] #instance attributes
        
    def add_to_cart(self,item):
        self.cart.append(item)

Rahim = Shop('Rahim')
Rahim.add_to_cart('Phone')
Rahim.add_to_cart('Shoes')
print(Rahim.cart)

niso = Shop('Niso')
niso.add_to_cart('watch')
niso.add_to_cart('cap')
print(niso.cart)