public class Solution {
    public bool DetectCapitalUse(string word) {
        char[] ch = word.ToCharArray();
        int n = 0;
        foreach(char c in ch){
            if(Char.IsUpper(c)){
                n++;
            }
         }
        if(n==word.Length){
            return true;
        }
        if(n==1 && Char.IsUpper(word,0)){
            return true;
        }
        if(n==0){
            return true;
        }
        return false;
        
    }
}
