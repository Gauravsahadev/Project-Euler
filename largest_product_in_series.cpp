#include <iostream>
#include <string>
using namespace std;
string s;
int getMult(int left, int right)
{
	double ans=1;
	for(int i=left;i<=right;++i)
		ans=ans* ( s[i]-'0');
	return ans;
}
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;++k)
	{
		int ans=0,n,m;
		cin>>n>>m;
		cin>>s;
		for(int i=0;i<s.size()-m;++i)
			ans=max(ans, getMult(i,i+m-1));
		cout<<ans<<endl;
	}
	return 0;
}
