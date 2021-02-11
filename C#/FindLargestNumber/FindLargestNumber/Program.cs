using System;

namespace FindLargestNumber
{
    public class Algorithme
    {
        public static int FindLargest(int[] numbers)
        {
            Array.Sort(numbers);
            return numbers[^1];
        }
        public static int FindLargest2(int[] numbers)
        {
            int? result = null;
            for (int i = 0; i < numbers.Length; i++)
            {
                int num = numbers[i];
                if (num > result.Value)
                {
                    result = num;
                }
            }
            return (int) result;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = { 1, -28, 88, 200, 7 };
            //int result = Algorithme.FindLargest(numbers);
            int result = Algorithme.FindLargest2(numbers);

            Console.WriteLine(result);
            Console.Read();
            
        }
    }
}
