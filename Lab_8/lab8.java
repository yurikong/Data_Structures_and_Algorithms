package lab8;

import java.util.LinkedList;
import java.util.Random;
import java.lang.Exception;

public class DiGraph
{
	private int V;
	private int time;
	private LinkedList<Integer> adj[];
	private int dist[];
	private int parent[];
	private int start[];
	private int end[];
	private int reachable[];
	private LinkedList<Integer> topo;
	DiGraph(int v, int e)
	{
		if(v < 0 || e < 0 || e > v * (v-1))
			return;
		V = v;
		adj = new LinkedList[v];
		dist = new int[V];
		parent = new int[V];
		start = new int[V];
		end = new int[V];
		reachable = new int[V];
		time = 0;
		topo = new LinkedList<>();
		for(int i = 0; i < V; i++)
		{
			adj[i] = new LinkedList<>();
			dist[i] = -1;
			parent[i] = -1;
			start[i] = -1;
			end[i] = -1;
			reachable[i] = 0;
		}
		while(e > 0)
		{
			//Random random = new Random(System.currentTimeMillis());
			Random random = new Random();
			int parent = random.nextInt(V);
			int child = random.nextInt(V);
			boolean success = addEdge(parent, child);
			if(success == true)
				e--;
		}
	}
	public void BFS(int u)
	{
		if(u < 0 || u >= V)
			return;
		reset();
		dist[u] = 0;
		parent[u] = -1;
		LinkedList<Integer> Q = new LinkedList<>();
		Q.push(u);
		while(!Q.isEmpty())
		{
			int w = Q.pop();
			for(int v : adj[w])
				if(v != u && parent[v] == -1)
				{
					parent[v] = w;
					dist[v] = dist[w] + 1;
					Q.push(v);
				}
		}
		for(int i = 0; i < V; i++)
			if(parent[i] != -1)
				reachable[i] = 1;
		System.out.println("BFS");
		System.out.print("vertices:\t");
		for(int i = 0; i < V; i++)
			System.out.print(i + " ");
		System.out.print("\ndistance:\t");
		for(int i = 0; i < V; i++)
			System.out.print(dist[i] + " ");
		System.out.print("\nparent:\t\t");
		for(int i = 0; i < V; i++)
			System.out.print(parent[i] + " ");
		System.out.print("\nreachable:\t");
		for(int i = 0; i < V; i++)
			System.out.print(reachable[i] + " ");
		System.out.println("\nShortest paths:");
		for(int i = 0; i < V; i++)
			if(reachable[i] == 1)
			{
				System.out.print(i + ":(dist = " + dist[i] + ")\t");
				int j = i;
				while(parent[j] != -1)
				{
					System.out.print(j + " ");
					j = parent[j];
				}
				System.out.print(j);
				System.out.println();
			}
		System.out.println();
	}
	public void DFS() throws Exception
	{
		reset();
		for(int i = 0; i < V; i++)
			if(parent[i] == -1)
				DFS_visit(i);
		System.out.println("DFS");
		System.out.print("vertices:\t");
		for(int i = 0; i < V; i++)
			System.out.print(i + " ");
		System.out.print("\nparent:\t\t");
		for(int i = 0; i < V; i++)
			System.out.print(parent[i] + " ");
		System.out.print("\nstart time:\t");
		for(int i = 0; i < V; i++)
			System.out.print(start[i] + " ");
		System.out.print("\nend time:\t");
		for(int i = 0; i < V; i++)
			System.out.print(end[i] + " ");
		System.out.print("\nTopo order:\t");
		while(!topo.isEmpty())
			System.out.print(topo.pop() + " ");
		System.out.println();
	}
	private void DFS_visit(int v) throws Exception
	{
		start[v] = ++time;
		for(int u : adj[v])
			if(parent[u] == -1)
			{
				parent[u] = v;
				DFS_visit(u);
			}
			else if(end[u] == -1)
				//System.out.println("Cycle detected, topological sort is impossible.");
				throw new Exception("Cycle detected, topological sort is impossible.");
		end[v] = ++time;
		if(!topo.contains(v))
			topo.push(v);
	}
	private boolean addEdge(int u, int v)
	{
		if(u != v && !adj[u].contains(v))
		{
			adj[u].add(v);
			return true;
		}
		return false;
	}
	private void reset()
	{
		for(int i = 0; i < V; i++)
		{
			dist[i] = -1;
			parent[i] = -1;
			start[i] = -1;
			end[i] = -1;
			reachable[i] = 0;
		}
		time = 0;
		topo = new LinkedList<>();
	}
	public void printTree()
	{
		String str = "";
		for(int i = 0; i < V; i++)
		{
			str += Integer.toString(i) + ": ";
			for(int j = 0; j < adj[i].size(); j++)
				str += Integer.toString(adj[i].get(j)) + " ";
			str += '\n';
		}
		System.out.println(str);
	}
}