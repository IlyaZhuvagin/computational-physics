#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool IsPalindrom(string s) {
    for (int i = 0; i < s.size() / 2; ++i) {
        if (s[i] != s[s.size() - i - 1]) {
            return false;
        }
    }
    return true;
}

vector<string> PalindromFilter(vector<string> words, int minLength) {
    vector<string> res;
    for (int i = 0; i < words.size(); ++i) {
        if (words[i].size() >= minLength && IsPalindrom(words[i])) {
            res.push_back(words[i]);
        }
    }
    return res;
}


//int main(){
//    for(const auto& elem: PalindromFilter({"abacaba", "aba"}, 5))
//        cout << elem << endl;
//}