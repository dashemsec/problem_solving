/*
 * https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
 *
 * Day 0: solve this problem with only queue implemention
 */


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include "queue.h"

#define MAX_QUEUE_ELEMENT 100

using namespace std;

void queue::display_front()
{
	if(isEmpty())
		return;
	cout << buffer[front] << endl;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int q, type, x, i;
    queue obj(MAX_QUEUE_ELEMENT);

    cin >> q;

    for(;q > 0; q--) {
    	cin >> type;
	switch(type) {
	    case 1:
		cin >> x;
		obj.enque(x);
		break;
	    case 2:
		obj.deque();
		break;
	    case 3:
		obj.display_front();
		break;
	}
	
    }
    return 0;
}
