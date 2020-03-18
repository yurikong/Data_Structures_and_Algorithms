package lab9;

import java.util.Scanner;

public class Tester
{
	public static void main(String args[])
	{
		try {
			System.out.print("Number of vertices: ");
			Scanner in = new Scanner(System.in);
			int V = in.nextInt();
			System.out.print("Number of edges: ");
			int E = in.nextInt();
			Graph G = new Graph(V, E);
			G.printTree();
			G.Explore();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			System.out.println(e.getMessage());
		}
	}
}
