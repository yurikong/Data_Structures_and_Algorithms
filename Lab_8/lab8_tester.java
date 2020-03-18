package lab8;

import java.util.Scanner;

public class Tester
{
	public static void main(String args[])
	{
		System.out.print("Number of vertices: ");
		Scanner in = new Scanner(System.in);
		int V = in.nextInt();
		System.out.print("Number of edges: ");
		int E = in.nextInt();
		DiGraph G = new DiGraph(V, E);
		G.printTree();
		System.out.print("Enter a vertex to start BFS: ");
		int v = in.nextInt();
		G.BFS(v);
		try
		{
			G.DFS();
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
}
