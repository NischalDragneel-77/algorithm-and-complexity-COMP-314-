#include<iostream>
#include<math.h>
#include "./Heap.h"

//public functions
Heap::Heap(){
    this->tail = 0;
    std::cout<<"Heap was created\n";
}

void Heap::addToHeap(int data, int priority){
    if(isFull()){
        std::cout<<"Heap is full\n";
        throw;
    };
    Node *node = new Node();
    node->data = data;
    node->priority = priority;

    //Adding the node to end of the tree
    tail+=1; //increment the tail pointer
    addToIndex(tail,node);
    //Traverse up the based on the priority of the node
    traverseUp(node,tail);
}

int Heap::removeFromHeap(){
    if(isEmpty()) throw "Heap Underflow";
    //save the head data to be returned
    int data = datas[1]->data;
    //get the last element of the heap
    Node* lastEl = datas[tail];
    //decrease the size of the heap
    tail-=1;
    //inrest the last element of heap to the root
    datas[1] = lastEl;
    //traveser down the heap to arrange the data
    traverseDown(lastEl,1);
    return data;
}

void Heap::changePriority(int data, int oldPriority, int newPriority){
    std::cout<<"Changing priority of "<<data<<" from "<<oldPriority<<" to "<<newPriority<<"\n";
    if(isEmpty()){
        std::cout<<"Heap is Empty\n";
        throw;
    };
    //find the index of the node
    int index = findIndex(data);
    std::cout<<index<<std::endl;
    //if the node is not found
    if(index == -1) {
        std::cout<<"Node not found\n";
        throw ;
    };

    //if the priority is same
    if(oldPriority == newPriority) return;
    //if the new priority is less than the old priority
    if(newPriority < oldPriority){
        //change the priority of the node
        datas[index]->priority = newPriority;
        //traverse up the node
        traverseUp(datas[index],index);
    }
    //if the new priority is greater than the old priority
    else{
        //change the priority of the node
        datas[index]->priority = newPriority;
        //traverse down the node
        traverseDown(datas[index],index);
    }
}

bool Heap::isEmpty(){
    return (tail == 0);
}

bool Heap::isFull(){
    return (tail >= MAX_SIZE);
}

void Heap::traverse(){
    if(isEmpty()) {
        std::cout<<"Heap is Empty\n";
        throw;
    };
    int index = 0;
    while (index < tail){
        index+=1;  
        std::cout<<"priority: "<<datas[index]->priority<<" Data: "<<datas[index]->data<<"\n"; 
    }
    std::cout<<std::endl;
}

//private functions
void Heap::addToIndex(int index,Node* node){
    datas[index] = node;
}

int Heap::findIndex(int data){
    int index = 1;
    while(index <= tail){
        if(datas[index]->data == data) return index;
        index+=1;
    }
    return -1;
}

//private functions
int Heap::getParentIndex(int currentIndex){
    return floor(currentIndex/2);
}

void Heap::traverseUp(Node* currentNode, int currentIndex){
    int newIndex = getParentIndex(currentIndex);
    if(newIndex >= 1){
        //parent node exists
        if(datas[newIndex]->priority > currentNode->priority){
            //low priority moveup
            //swap the infos
            Node* parentNode = datas[newIndex];
            datas[newIndex] = currentNode;
            datas[currentIndex] = parentNode; 
            //recursively travese up
            traverseUp(currentNode,newIndex);
        }
    }
}

void Heap::traverseDown(Node* currentNode, int currentIndex){
    //from the given index of the givem node find the index of its 
    //corresponding left and right child
    int leftIndex = 2*currentIndex;
    int rightIndex = 2*currentIndex+1;
    
    if(leftIndex <= tail && rightIndex <= tail){
        //node has both left and right subtree
        
        //compare the priority of the left and right child node and select with greatest priority
        int subTreeWithHighPriority = (datas[leftIndex]->priority <= datas[rightIndex]->priority) ? leftIndex : rightIndex;
        if(datas[subTreeWithHighPriority]->priority < currentNode->priority){
            //swap
            datas[currentIndex] = datas[subTreeWithHighPriority];
            datas[subTreeWithHighPriority] = currentNode;
            
            //recursively travese down
            traverseDown(
                datas[subTreeWithHighPriority],
                subTreeWithHighPriority
            );
            
        }
    }else if(leftIndex <= tail){
        //only left child present
        if(datas[leftIndex]->priority < currentNode->priority){
            //swap
            datas[currentIndex] = datas[leftIndex];
            datas[leftIndex] = currentNode;
            
            //recursively travese down
            traverseDown(
                datas[leftIndex],
                leftIndex
            );
            
        }

    }else if(rightIndex <= tail){
        //only right child present
        if(datas[rightIndex]->priority < currentNode->priority){
            //swap
            datas[currentIndex] = datas[rightIndex];
            datas[rightIndex] = currentNode;
            
            //recursively travese down
            traverseDown(
                datas[rightIndex],
                rightIndex
            );
            
        }
    }
}