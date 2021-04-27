#include<iostream>
using namespace std;

bool uniqueChar(string str){
  for(int i = 0; i < str.length(); i++){
    for(int j = i + 1; j < str.length() - 1; j++){
      if(str[i] == str[j]) {
        return false;
      }
    }
  }
  return true;
}

int main(){
  string str = "noiygh";
  if(uniqueChar(str)){
    cout << "These characters are unique"<< endl;
  }
  else{
    cout << "These characters are not unique"<< endl;
  }
  return 0;
}
