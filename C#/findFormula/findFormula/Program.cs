using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace findFormula
{
    public class Answer
    {
        public static string LocateUniverseFormula()
        {
            string formule = "C:/Users/Archie/AppData/Local/Temp";
            string universeformula = "universe-formula.*";
            string[] Getfiles = Directory.GetFiles(formule, universeformula, SearchOption.AllDirectories);
            return String.Concat(Getfiles);
            
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            string formulaPath = "C:/Users/Archie/AppData/Local/Temp/test/universe-formula.txt";

            Console.WriteLine("In this example, the formula path is");
            
            Console.WriteLine(formulaPath);
            Console.WriteLine("and you found it at :");
            Console.WriteLine(Answer.LocateUniverseFormula());
            Console.Read();

        }
    }
}
