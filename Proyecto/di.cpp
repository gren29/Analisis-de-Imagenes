#include <iostream>

using namespace std;
int matriz[8][8] = {
        {0,0,0,0,0,0,0,0},
        {0,0,1,1,0,0,0,0},
        {0,1,1,1,1,0,1,0},
        {0,1,1,1,1,1,1,0},
        {0,0,1,1,1,1,1,0},
        {0,0,1,1,1,1,1,0},
        {0,0,0,0,1,0,1,0},
        {0,0,0,0,0,0,0,0}
    };

int matriz2[8][8] = {
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0}
    };

void Imprimir(){
    for(int x = 0; x < 8;x++){
        for(int y = 0; y < 8;y++){
            cout << matriz[x][y] << " ";
        }
        cout << endl;
    }
}

void Imprimir2(){
    for(int x = 0; x < 8;x++){
        for(int y = 0; y < 8;y++){
            cout << matriz2[x][y] << " ";
        }
        cout << endl;
    }
}
int main(){
    Imprimir();
    for(int x = 0; x < 8;x++){
        for(int y = 0; y < 8;y++){
            if(matriz[x][y] == 1){
                try{
                    matriz2[x][y] = 1;
                }
                catch(const std::exception& e){
                    matriz2[x][y] = 1;
                }

                try{
                    matriz2[x-1][y] = 1;
                }
                catch(const std::exception& e){
                    matriz2[x][y] = 1;
                }
                try{
                    matriz2[x+1][y] = 1;
                }
                catch(const std::exception& e){
                    matriz2[x][y] = 1;
                }
                try{
                    matriz2[x][y-1] = 1;
                }
                catch(const std::exception& e){
                    matriz2[x][y] = 1;
                }
                try{
                    matriz2[x][y+1] = 1;
                }
                catch(const std::exception& e){
                    matriz2[x][y] = 1;
                }
                
            }
        }
    }
    cout << endl;
    Imprimir2();
}