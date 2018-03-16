#include <iostream>
using namespace std;

int main()
{
	float secin, secout, secrem, min, hour;
	
	cout << "Please enter the time in seconds. ";
	cin >> secin;

	hour = int( secin / (60 * 60)) ;
	secrem = int( secin - (60 * 60) * hour);

	min = int( secrem / 60);
	secout = int( secrem - 60 * min);

	cout << hour << "::" << min << "::" << secout;

	cin.get();
	cin.get();
	return 0;
}