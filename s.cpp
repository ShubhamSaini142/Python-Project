#include <iostream>

using namespace std;
int main()
{
    int n = 6;
    int a[n] = {5, 2, 3, 6, 4, 1};
    cout << " Before" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << endl;
    }
    for (int i = 1; i < n; i++)
    {
        int j = i - 1;
        int e = a[i];
        while (j > 0)
        {
            if (e < a[j])
            {
                a[j + 1] = a[j];
                a[j] = e;
            }
            else
            {
                break;
            }
            j--;
        }
        // a[j + 1] = e;
        // shubham saini
    }
    cout << "After" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << endl;
    }
}