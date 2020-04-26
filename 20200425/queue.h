/*
 * while enque, rear is advanced first then the data is inserted.
 * while deque, the data is taken from front and then the front is advanced.
 */
typedef class queue {
protected:
	int front;
	int rear;
	int *buffer;
	int capacity;
	int size;
public:
	queue(int cap) {
		capacity = cap;
		buffer = new int(cap);
		front = 0;
		rear = -1;
		size = 0;
	}

	 ~queue() {
	 	delete[] buffer;
	 }
	int enque(int data);
	int deque();
	int isFull();
	int isEmpty();
	int getSize();
	void display_front();
} Queue;

