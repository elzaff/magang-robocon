#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define PI 3.14159265359
#define rad PI / 180

class Omniwheel
{
private:
    float invkin[4][3];
    int speed[4];

public:
    Omniwheel()
    {
        invkin[0][0] = cos(45.0 * rad);
        invkin[0][1] = sin(45.0 * rad);
        invkin[0][2] = 1;
        invkin[1][0] = cos(135.0 * rad);
        invkin[1][1] = sin(135.0 * rad);
        invkin[1][2] = 1;
        invkin[2][0] = cos(225.0 * rad);
        invkin[2][1] = sin(225.0 * rad);
        invkin[2][2] = 1;
        invkin[3][0] = cos(315.0 * rad);
        invkin[3][1] = sin(315.0 * rad);
        invkin[3][2] = 1;
    }

    void ngitung(int translasi[3])
    {
        for (int i = 0; i < 4; i++)
        {
            speed[i] = 0;
            for (int j = 0; j < 3; j++)
            {
                speed[i] += invkin[i][j] * translasi[j];
            }
        }
    }

    void nampilin()
    {
        for (int i = 0; i < 4; i++)
        {
            cout << "Keceptan roda " << i + 1 << " : " << speed[i] << endl;
        }
    }

    void nyimpen(const string &filename)
    {
        ofstream file(filename);
        for (int i = 0; i < 4; i++)
        {
            file << "Kecepatan roda " << i + 1 << " : " << speed[i] << endl;
        }
        file.close();
    }
};

int main()
{
    Omniwheel omni;

    int input[3];
    cout << "Masukkan translasi x, y, dan rotasi z : ";
    cin >> input[0] >> input[1] >> input[2];

    omni.ngitung(input);
    omni.nampilin();
    omni.nyimpen("hasil.txt");

    return 0;
}