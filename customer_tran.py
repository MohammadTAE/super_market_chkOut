class Customer:
    def __init__(self, id, item_count):
        self.__id = id
        self.__item_count = item_count
        self.__total = 0
        self.__discount = 0
        self.items_dict= dict()

    def scan(self, price_list, rand_item):
        item = price_list[rand_item]
        if item.name in self.items_dict:
            self.items_dict[item.name] += 1
        else:
            self.items_dict[item.name] = 1
        if item.special_count > 0 and self.items_dict[item.name] % item.special_count == 0:
            self.__discount += (item.price * item.special_count) - item.special_price
            print('Customer ' + str(self.__id) + ': discount so far= ' + str(self.__discount))
        self.__total += item.price

    def get_total(self):
        print('Customer ' + str(self.__id) + ': total before discount= ' + str(self.__total))
        self.__total -= self.__discount
        return self.__total

class Item:
    def __init__(self, name, price, special_count= 0, special_price= 0):
        self.name = name
        self.price = price
        self.special_count = special_count
        self.special_price = special_price

import random
import multiprocessing

def customer_checkout(customer_id, price_list):
    print('customer ' + str(customer_id) + ':')
    item_count = random.randint(1, 40)
    customer = Customer(customer_id, item_count)
    print('Customer ' + str(customer_id) + ': Scanning', item_count, 'items:')
    for item in range(item_count):
        rand_item = random.randint(0, len(price_list) - 1)
        message = 'Customer ' + str(customer_id) + ', item ' + str(item + 1) + ': ' + str(price_list[rand_item].name) + ', price= $' + str(price_list[rand_item].price)
        if price_list[rand_item].special_count > 0:
            message +=', special offer: ' + str(price_list[rand_item].special_count) + ' for $' + str(price_list[rand_item].special_price)
        print(message)
        customer.scan(price_list, rand_item)
    print('Customer ' + str(customer_id) + ': Total=', customer.get_total())

def get_item(name, price_list):
    for item in price_list:
        if item.name == name:
            return item
    return None

def main():
    price_list = [Item("A", 40, 3, 70), Item("B", 10, 2, 15), Item("C", 30), Item("D", 25, 0, 0)]

    customer_count = random.randint(1, 2)
    print('customer_count=', customer_count)
    jobs = []
    for customer_id in range(customer_count):
        p = multiprocessing.Process(target=customer_checkout, args=(customer_id, price_list))
        jobs.append(p)
        p.start()


if __name__ == '__main__':
    main()