#include "iostream"
#include "queue.h"

using namespace std;


int Queue::getSize()
{
	return size;
}

int Queue::isEmpty()
{
	if (size == 0) {
		cout << "QUEUE IS EMPTY !!!" << endl;
		return 1;
	}

	return 0;
}

int Queue::isFull()
{
	if (size == capacity) {
		cout << "QUEUE IS FULL !!!" << endl;
		return 1;
	}

	return 0;
}

int Queue::enque(int data)
{
	if (isFull()) {
		return -1;
	}

	rear = (rear + 1) % capacity;
	buffer[rear] = data;
	size ++;

	return 0;
}

int Queue::deque()
{
	int ret;

	if(isEmpty()) {
		return -1;
	}

	ret = buffer[front];
	front = (front + 1) % capacity;
	size --;
	return ret;
}
/************************************************************/




#if 0
int main()
{
	Queue q(5);

	for(int i = 1; i <=6; i++)
		q.enque(i);

	cout << q.deque() << endl;
	cout << q.deque() << endl;
	cout << q.deque() << endl;

	for(int i = 10; i <=16; i++)
		q.enque(i);

	cout << q.deque() << endl;
	cout << q.deque() << endl;
	cout << q.deque() << endl;

	return 0;
}
#endif
