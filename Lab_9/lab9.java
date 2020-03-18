package lab9;

import java.util.LinkedList;
import java.util.Random;
import java.lang.Exception;

public class Graph
{
	private int V;
	private LinkedList<Integer> adj[];
	private String color[];
	Graph(int v, int e) throws Exception
	{
		if(v < 0 || e < 0 || e > v * (v-1) / 2)
			throw new Exception("Size error!");
		V = v;
		adj = new LinkedList[v];
		color = new String[v];
		for(int i = 0; i < V; i++)
		{
			adj[i] = new LinkedList<>();
			color[i] = "Gray";
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
	public void Explore() throws Exception
	{
		for(int i = 0; i < V; i++)
			color[i] = "Gray";
		for(int i = 0; i < V; i++)
			if(color[i].equals("Gray"))
				Is_bipartite(i);
	}
	public void Is_bipartite(int w) throws Exception
	{
		LinkedList<Integer> Q = new LinkedList<>();
		Q.add(w);
		color[w] = "Blue";
		while(!Q.isEmpty())
		{
			int u = Q.pop();
			for(int v : adj[u])
			{
				if(color[v].equals("Gray"))
				{
					if(color[u].equals("Blue"))
						color[v] = "Red";
					else
						color[v] = "Blue";
					Q.push(v);
				}
				else
					if(color[v].equals(color[u]))
						throw new Exception("NOT bipartite");
			}
		}
		for(int i = 0; i < V; i++)
			System.out.println(i + ": " + color[i]);
	}
	private boolean addEdge(int u, int v)
	{
		if(u != v && !adj[u].contains(v))
		{
			adj[u].add(v);
			adj[v].add(u);
			return true;
		}
		return false;
	}
	public void printTree()
	{
		for(int i = 0; i < V; i++)
		{
			//str += Integer.toString(i) + ": ";
			System.out.print(i + ": ");
			for(int j = 0; j < adj[i].size(); j++)
				//str += Integer.toString(adj[i].get(j)) + " ";
				System.out.print(adj[i].get(j) + " ");
			//str += '\n';
			System.out.println();
		}
		//str += '\n';
		System.out.println();
		//return str;
	}
}