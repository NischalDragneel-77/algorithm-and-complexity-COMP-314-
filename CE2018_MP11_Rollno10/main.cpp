#include<iostream>
#include "./Heap.cpp"

int main(){
    Heap h1;
    h1.addToHeap(1,1);
    h1.addToHeap(10,10);
    h1.addToHeap(22,22);
    h1.addToHeap(21,21);
    h1.addToHeap(5,5);

    h1.traverse();
    std::cout<<std::endl;
    int head = h1.removeFromHeap();
    std::cout<<std::endl;
    std::cout<<head;
    std::cout<<std::endl;

    // h1.traverse();
    h1.addToHeap(13,13);
    h1.traverse();

    h1.changePriority(13,13,11);
    // int head = h1.removeFromHeap();
    h1.traverse();
    std::cout<<"DOne :D";
}