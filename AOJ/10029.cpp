#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

int main()
{
	int total_number,i,tmp;
	vector<int> broken_number;
	cin >> total_number;
	for(i=0;i<total_number;i++){
		cin>>tmp;
		broken_number.push_back(tmp);
	}
	sort(broken_number.begin(),broken_number.end());
	for (i=0;i<total_number;i++){
		cout << broken_number[i];
		if(i==total_number-1){
			cout << endl;
		} else {
			cout << " ";
		}
	}
}