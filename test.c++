#include <iostream>

using namespace std;
int main(int argc, char const *argv[])
{
    /* code */
    

    return 0;
}

bool isSubsequence(string s, string t) 
    {
        int seq = s.size();
        
        int q = 0; 
        for(int i = 0; i < t.size(); i++)
        {
            
            if(t.at(i) == s.at(q))
            {
                seq--;
                q++;
            }
        }

        if(seq == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }