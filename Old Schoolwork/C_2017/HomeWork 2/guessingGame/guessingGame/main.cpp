#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int main()
{
	int guess, answer;

	srand (time(NULL));
	answer = rand() % 100; // randomizes the answer between 0 and 100
	
	cout << "Guess a number between 1 and 100: ";
	cin >> guess;

	while (guess != answer)
	{
		if (guess > answer)
		{
			cout << " Wrong! Try a lower number. " << endl;
			cin >> guess;
		}

		if (guess < answer)
		{
			cout << " Wrong! Try a higher number. " << endl;
			cin >> guess;
		}

	}

	if (guess == answer)
	{
		cout << "Correct! The answer is " << answer << endl;
	}
	
	system("pause");
	return 0;
}