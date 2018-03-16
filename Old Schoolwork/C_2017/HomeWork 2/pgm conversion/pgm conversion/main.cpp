#include <iostream>
using namespace std;

int main()
{
	int num, num_reverse = 0;
	int digit;
	cout << "Please enter a number: ";
	cin >> num;

	cout << "\n\nInput number is: " << num << endl;

	while(num)
	{
		digit = num - (num/10) * 10;
		num_reverse = digit + num_reverse * 10;  // We multiply num reverse here in order to ensure the digits appear in proper order

		num = num/10;
	}
	

	cout << "Reversed number is: " << num_reverse << endl;


	system("pause");
	return 0;

}