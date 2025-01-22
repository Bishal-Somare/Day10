class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top of the stack is {self.stack[-1]}.")
        return self.stack[-1]

    def size(self):
        print(f"Current stack size: {len(self.stack)}.")
        return len(self.stack)

    def display(self):
        print("Stack (top to bottom):", self.stack[::-1])

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    stack.peek()
    stack.pop()
    stack.display()
    stack.size()
    stack.pop()
    stack.pop()
    stack.pop()
