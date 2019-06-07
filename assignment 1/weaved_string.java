import java.util.Scanner;
public class Main {
    public String Encode(String str1, String str2)
    {
        char s1[] = new char[str1.length()];
        char s2[] = new char[str1.length()];
        for (int i = 0; i <=str1.length() ; i++){
            s1[i] = str1.charAt(i);
        }
        for (int i = 0; i <=str2.length() ; i++){
            s2[i] = str2.charAt(i);
        }
        String weaved = "";
        if (s1.length == s2.length){
            for (int i = 0; i <=s1.length ; i++){
                weaved += s1[i] + s2[i];
            }
        }
        else if( s1.length > s2.length){
            for (int i = 0; i <s2.length; i++)
                weaved += s1[i] + s2[i];
            for (int j = s2.length; j < s1.length ; j++)
                weaved += s1[j];
        }
        else {
            for (int i = 0; i <s1.length ; i++)
                weaved += s1[i] + s2[i];
            for (int j = s1.length; j < s2.length ; j++)
                weaved += s2[j];
        }
        return weaved ;
    }
    public static void main(String arg[])
    {
        Scanner sa = new Scanner(System.in) ;
        Main saa = new Main();
        System.out.println("Enter String to encode :");
        String s1 = sa.nextLine();
        System.out.println("Enter String to encode :");
        String s2 = sa.nextLine();
        System.out.println(saa.Encode( s1, s2));
    }
}