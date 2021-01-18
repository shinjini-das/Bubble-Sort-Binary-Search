#Bubblesort and binary search

class sort:
    arr=[]
    item=0
    def inpdata(self):
        for i in range(5):
            k=int(input("Input a nonduplicate number"))
            self.arr.append(k)

    def bubsort(self):
        t=0
        print("\nThe sorted list is ")
        for i in range(5):
            for j in range(5-i-1):
                if(self.arr[j]>self.arr[j+1]):
                    t=self.arr[j]
                    self.arr[j]=self.arr[j+1]
                    self.arr[j+1]=t

        print(self.arr)

    def binsearch(self):
        self.item=int(input("Enter the no for binary search"))
        beg=f=0
        last=4
        while(beg<last):
            mid=(beg+last)//2
            if(self.arr[mid]==self.item):
                f=1
                break
            if(self.item>self.arr[mid]):
                beg=mid+1
            if(self.item<self.arr[mid]):
                last=mid-1
        if(f==1):
            print(self.item," is found in the array")
        else:
            print(self.item," is not found in the array")

def main():
    a=sort()
    a.inpdata()
    a.bubsort()
    a.binsearch()
    
main()
