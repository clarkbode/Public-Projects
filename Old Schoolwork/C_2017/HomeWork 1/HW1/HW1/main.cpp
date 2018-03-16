#include <iostream>
using namespace std;

int main()
{
	float fn, cl;

	cout << "Please enter the degrees in Fahrenheit. ";
	cin >> fn;

	cl = (fn - 32) * 5/9;

	cout << "Conversion: " << fn << " Fahrenheit = " << cl << " celsius " << endl;

	cin.get();
	cin.get();

	return 0;
}