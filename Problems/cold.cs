using System;
using System.Linq;

class Solution
{
    static void Main(String[] args)
    {
        var n = int.Parse(Console.ReadLine());
        var temps = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        Console.WriteLine(temps.Count(t => t < 0));

    }
}
