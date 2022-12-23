def main():
    n=int(input())
    count(n)

def count(i):
    
    for n in range (i):
        i=n+1
        print(i ,end="")

main()
