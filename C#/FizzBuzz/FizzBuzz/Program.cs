using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading;

namespace FizzBuzz
{
    class Solution
    {
        public static String FizzBuzz(int number, Dictionary<int, String> map)
        {
            string str = "";
            if (number % 3 == 0)
            {
                str += map[3];
            }
            if (number % 4 == 0)
            {
                str += map[4];
            }
            if (str.Length == 0)
            {
                str = number.ToString();
            }
            return str;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, String> map = new Dictionary<int, string>();
            map[3] = "FIZZ";
            map[4] = "BUZZ";

            Console.WriteLine(Solution.FizzBuzz(5, map));
            Console.WriteLine(Solution.FizzBuzz(3, map));
            Console.WriteLine(Solution.FizzBuzz(8, map));
            Console.WriteLine(Solution.FizzBuzz(12, map));
        }
    }
}
