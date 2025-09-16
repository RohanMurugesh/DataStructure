package dsa_course;

    // Node class (inner class)
    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
 class SingleLinkedList {
    // Head of the list
    Node head;

    // 1. Insert at the beginning
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);  // Create new node
        newNode.next = head;            // Point new node's next to current head
        head = newNode;                 // Move head to new node
    }

    // 2. Insert at the end
    public void insertAtEnd(int data) {
        Node newNode = new Node(data);  // Create new node

        // If list is empty, make newNode the head
        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;
        while (current.next != null) {
            current = current.next;     // Traverse to the end
        }
        current.next = newNode;         // Add new node at the end
    }

    // 3. Insert after a given node
    public void insertAfter(Node prevNode, int data) {
        if (prevNode == null) {
            System.out.println("The given previous node cannot be null.");
            return;
        }

        Node newNode = new Node(data);   // Create new node
        newNode.next = prevNode.next;    // Point newNode's next to prevNode's next
        prevNode.next = newNode;         // Link prevNode to newNode
    }

    // 4. Insert at a specific position (0-based index)
    public void insertAtPosition(int index, int data) {
        if (index < 0) {
            System.out.println("Invalid index.");
            return;
        }

        if (index == 0) {
            insertAtBeginning(data);
            return;
        }

        Node newNode = new Node(data);
        Node current = head;
        int count = 0;

        // Traverse to the node just before the desired position
        while (current != null && count < index - 1) {
            current = current.next;
            count++;
        }

        if (current == null) {
            System.out.println("Index is out of bounds.");
            return;
        }

        newNode.next = current.next;
        current.next = newNode;
    }

    // Helper method to print the list
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

    // Main method for testing
    public class Sll {
    public static void main(String[] args) {
        SingleLinkedList list = new SingleLinkedList();

        System.out.println("Insert at beginning:");
        list.insertAtBeginning(10);
        list.insertAtBeginning(20);
        list.printList();  // 20 -> 10 -> null

        System.out.println("Insert at end:");
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        list.printList();  // 20 -> 10 -> 30 -> 40 -> null

        System.out.println("Insert after a given node (10):");
        Node node10 = list.head.next; // Node with data = 10
        list.insertAfter(node10, 25);
        list.printList();  // 20 -> 10 -> 25 -> 30 -> 40 -> null

        System.out.println("Insert at specific position (index 2):");
        list.insertAtPosition(2, 15);
        list.printList();  // 20 -> 10 -> 15 -> 25 -> 30 -> 40 -> null
    }
}


