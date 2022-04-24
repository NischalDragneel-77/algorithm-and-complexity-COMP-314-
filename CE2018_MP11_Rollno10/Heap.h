#include<iostream>
#define MAX_SIZE 500

class Node{
    public:
    int priority;
    int data;
};

class Heap{
    public:
    Heap();

    /*
    * Creates new node and adds to the heap
    @param data: data to be added to the heap
    @param priority: priority of the data
    */
    void addToHeap(int data, int priority);

    /*
    * Removes the root node and assigns the suitable new root from the heap
    @returns the data of the root node
    */
    int removeFromHeap();
    
    /*
    * Changes priority of the node and adjusts the heap accordingly
    @param data: data of the node to be changed
    @param oldPriority: old priority of the node
    @param newPriority: new priority of the node
    */
    void changePriority(int data, int oldPriority, int newPriority);

    /*
    * @returns true if heap is empty
    */
    bool isEmpty();

    /*
    * @returns true if heap is full
    */
    bool isFull();

    /*
    * BFS through the elements in the array
    */
    void traverse();

    private:
    //Contains all data as array of nodes
    Node* datas[MAX_SIZE];

    //Index of last item
    int tail;

    //add node to the provided index
    void addToIndex(int index,Node* node);

    //insert to left or right
    void insert(Node* subtree, Node* newNode);

    //finds index of the node
    int findIndex(int data);

    //get the parents index
    int getParentIndex(int currentIndex);

    //traverse up
    void traverseUp(Node* currentNode, int currentIndex);

    //traverse down
    void traverseDown(Node* currentNode, int currentIndex);
};