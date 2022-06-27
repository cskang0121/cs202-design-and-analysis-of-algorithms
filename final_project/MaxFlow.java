import java.util.ArrayList;
import java.util.LinkedList;
 
// DirectedGraph class explained above
class DirectedGraph {
    public static class Vertex {
 
        // number of the end vertex
        // weight or capacity
        // associated with the edge
 
        Integer i;
        Integer w;
 
        public Vertex(Integer i, Integer w)
        {
            this.i = i;
            this.w = w;
        }
    }
 
    final ArrayList<ArrayList<Vertex> > adjacencyList;
    int vertices;
 
    public DirectedGraph(int vertices)
    {
        this.vertices = vertices;
 
        adjacencyList = new ArrayList<>(vertices);
        for (int i = 0; i < vertices; i++)
            adjacencyList.add(new ArrayList<>());
    }
 
    public void addEdge(Integer u, Integer v,
                        Integer weight)
    {
        adjacencyList.get(u)
            .add(new Vertex(v, weight));
    }
 
    boolean hasEdge(int u, int v)
    {
        if (u >= vertices)
            return false;
 
        for (Vertex vertex : adjacencyList.get(u))
            if (vertex.i == v)
                return true;
        return false;
    }
 
    // Returns null if no edge
    // is found between u and v
    DirectedGraph.Vertex getEdge(int u, int v)
    {
        for (DirectedGraph.Vertex vertex :
             adjacencyList.get(u))
            if (vertex.i == v)
                return vertex;
 
        return null;
    }
}
 
public class MaxFlow {
    private final int source;
    private final int sink;
    private final DirectedGraph graph;
 
    private DirectedGraph residualGraph;
 
    public MaxFlow(DirectedGraph graph,
                   int source,
                   int sink)
    {
        this.graph = graph;
        this.source = source;
        this.sink = sink;
    }
 
    private void initResidualGraph()
    {
        residualGraph = new DirectedGraph(graph.vertices);
 
        // Construct residual graph
        for (int u = 0; u < graph.vertices; u++) {
 
            for (DirectedGraph.Vertex v : graph.adjacencyList.get(u)) {
 
                // If forward edge already
                // exists, update its weight
                if (residualGraph.hasEdge(u, v.i))
                    residualGraph.getEdge(u, v.i).w += v.w;
 
                // In case it does not
                // exist, create one
                else
                    residualGraph.addEdge(u, v.i, v.w);
 
                // If backward edge does
                // not already exist, add it
                if (!residualGraph.hasEdge(v.i, u))
                    residualGraph.addEdge(v.i, u, 0);
            }
        }
    }
 
    public int FIFOPushRelabel()
    {
        initResidualGraph();
 
        LinkedList<Integer> queue = new LinkedList<>();
 
        // Step 1: Initialize pre-flow
 
        // to store excess flow
        int[] e = new int[graph.vertices];
 
        // to store height of vertices
        int[] h = new int[graph.vertices];
 
        boolean[] inQueue = new boolean[graph.vertices];
 
        // set the height of source to V
        h[source] = graph.vertices;
 
        // send maximum flow possible
        // from source to all its adjacent vertices
        for (DirectedGraph.Vertex v :
            graph.adjacencyList.get(source)) {
            residualGraph.getEdge(source, v.i).w = 0;
            residualGraph.getEdge(v.i, source).w = v.w;
 
            // update excess flow
            e[v.i] = v.w;
 
            if (v.i != sink) {
                queue.add(v.i);
                inQueue[v.i] = true;
            }
        }
 
        // Step 2: Update the pre-flow
        // while there remains an applicable
        // push or relabel operation
        while (!queue.isEmpty()) {
 
            // vertex removed from
            // queue in constant time
            int u = queue.removeFirst();
            inQueue[u] = false;
 
            relabel(u, h);
            push(u, e, h, queue, inQueue);
        }
 
        return e[sink];
    }
 
    private void relabel(int u, int[] h)
    {
        int minHeight = Integer.MAX_VALUE;
 
        for (DirectedGraph.Vertex v :
             residualGraph.adjacencyList.get(u)) {
            if (v.w > 0)
                minHeight = Math.min(h[v.i],
                                     minHeight);
        }
 
        h[u] = minHeight + 1;
    }
 
    private void push(int u, int[] e, int[] h,
                      LinkedList<Integer> queue,
                      boolean[] inQueue)
    {
        for (DirectedGraph.Vertex v :
             residualGraph.adjacencyList.get(u)) {
            // after pushing flow if
            // there is no excess flow,
            // then break
            if (e[u] == 0)
                break;
 
            // push more flow to
            // the adjacent v if possible
            if (v.w > 0 && h[v.i] < h[u]) {
                // flow possible
                int f = Math.min(e[u], v.w);
 
                v.w -= f;
                residualGraph.getEdge(v.i, u).w += f;
 
                e[u] -= f;
                e[v.i] += f;
 
                // add the new overflowing
                // immediate vertex to queue
                if (!inQueue[v.i] && v.i != source
                    && v.i != sink) {
                    queue.add(v.i);
                    inQueue[v.i] = true;
                }
            }
        }
 
        // if after sending flow to all the
        // intermediate vertices, the
        // vertex is still overflowing.
        // add it to queue again
        if (e[u] != 0) {
            queue.add(u);
            inQueue[u] = true;
        }
    }
 
    public static void main(String[] args)
    {
        final int vertices = 6;
        final int source = 0;
        final int sink = 5;
 
        DirectedGraph dg
            = new DirectedGraph(vertices);
 
        dg.addEdge(0, 1, 16);
        dg.addEdge(0, 2, 13);
        dg.addEdge(1, 2, 10);
        dg.addEdge(2, 1, 4);
        dg.addEdge(1, 3, 12);
        dg.addEdge(3, 2, 9);
        dg.addEdge(2, 4, 14);
        dg.addEdge(4, 5, 4);
        dg.addEdge(4, 3, 7);
        dg.addEdge(3, 5, 20);
 
        MaxFlow maxFlow
            = new MaxFlow(
                dg, source, sink);
        System.out.println(
            "Max flow: "
            + maxFlow.FIFOPushRelabel());
    }
}