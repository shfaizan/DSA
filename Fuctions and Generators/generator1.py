from time import sleep


def all_even():
    n = 0
    while True:
        yield n
        n += 2


my_gen = all_even()

for i in range(10):
    print(next(my_gen))

print("\n NOW I WILL DO IT AGAIN \n")
sleep(2)

for i in range(100):
    print(next(my_gen))

if __name__ == '__main__':
    pass
