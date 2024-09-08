import java.util.PriorityQueue;

public class PriorityQueueExample {
    public static void main(String[] args) {
        // Priority Queue using Java's in-built PriorityQueue class
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // Adding elements
        pq.add(10);
        pq.add(1);
        pq.add(30);

        // Peek the top element (min element in this case)
        System.out.println("Top Element: " + pq.peek());

        // Remove the top element
        System.out.println("Popped Element: " + pq.poll());

        // Peek again
        System.out.println("Top Element after pop: " + pq.peek());
    }
}
