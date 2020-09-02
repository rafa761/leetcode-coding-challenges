"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class MyQueue:

	def __init__(self):
		self.queue = []

	def push(self, x: int) -> None:
		self.queue.append(x)

	def pop(self) -> int:
		return self.queue.pop(0)

	def peek(self) -> int:
		return self.queue[0]

	def empty(self) -> bool:
		return len(self.queue) <= 0


if __name__ == '__main__':
	Q = MyQueue()

	print(Q.push(1))
	print(Q.push(2))
	print('peek -> 1: ', Q.peek())
	print('pop -> 1: ', Q.pop())
	print('empty -> false: ', Q.empty())
