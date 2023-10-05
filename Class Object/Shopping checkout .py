class Shoping:
    def __init__(self,name) -> None:
       self.name = name
       self.cart =[]

    def add_to_card(self, item,price,quantity):
        product= {'item': item, 'price': price, 'quantity' : quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total =0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price',total)
        if amount < total:
            print(f'plese provide {total - amount} more')
        else:
            extra = amount -total
            print(f'Here is Your items and extra money {extra}')
            
    def remove(self,key):
        #  self.cart =[]
        for items in self.cart:
            if items['item'] ==key:
                self.cart.remove(items)

         


        
swapan = Shoping('Swapan Alam')
swapan.add_to_card('Alu',50,9 )
swapan.add_to_card('dim',12, 24)
swapan.add_to_card('rice',50, 5)
# print(*swapan.cart)
# swapan.checkout(600)
swapan.checkout(1600)
swapan.remove('dim')
swapan.checkout(1000)
print(swapan.cart)
