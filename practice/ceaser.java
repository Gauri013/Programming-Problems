import java.util.Scanner;
public class Rto13 {
 public String Encode(String s, int k)
    {
        String s1 = "";
 for (int i = 0; i < s.length(); i++)
        {
 if ((s.charAt(i) >= 65 && s.charAt(i) <= 90) || (s.charAt(i) >= 97 && s.charAt(i) <= 122))
            {
 char ch = (char)(s.charAt(i) + k);
 if (s.charAt(i) >= 97 && s.charAt(i) <= 122 && ch > 122)
                    s1 += (char)(ch - 26);
 else if (s.charAt(i) >= 65 && s.charAt(i) <= 90 && ch > 90)
                    s1 += (char)(ch - 26);
 else
 s1 += (char)ch;
            }
 else
 s1 = s1 + s.charAt(i);
        }
 return s1;
    }
 public static void main(String arg[])
    {
        Scanner sa = new Scanner(System.in);
        Rto13 saa = new Rto13();
        System.out.println("Enter String to encode :");
        String s = sa.nextLine();
        System.out.println(saa.Encode(s,13));
    }
}