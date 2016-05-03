#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <stdio.h>


using namespace std;

void linspace(vector<float> &v,float start,float stop,float num){
    v.assign(num,0.0); 
    double delta=((stop-start))/(num-1);
    v[0]=start;
    for(int i=1;i<v.size();i++){
        v[i]=v[i-1]+delta;
    }
} 

void ones(vector<vector<float> > &m,float height,float width){
    m.assign(height,vector<float>(width,1));
}

void print_matrix(vector<vector<float> > &m,float height,float width){
        for(int i=0;i<height;i++){
            for(int j=0;j<width;j++){
                cout<<"\t"<<m[i][j];
            }
            cout<<endl;
        }
    
}

void copy(vector<vector<float> > &a,vector<vector<float> > &b,float height,float width){
    for(int i=0;i<height;i++){
            for(int j=0;j<width;j++){
                b[i][j]=a[i][j];
            }
            
        }
    
}

int main()
{
    
    float nx = 8;//41;
    float ny = 8;//41;
    float nt = 120;
    float c = 1;
    float dx = 2/(nx-1);
    float dy = 2/(ny-1);
    float sigma = 0.0009;
    float nu = 0.01;
    float dt = sigma*dx*dy/(nu);
    vector<float> x;
    vector<float> y;
    linspace(x,0,2,nx);
    linspace(y,0,2,ny);
    vector<vector<float> > u;
    vector<vector<float> > v;
    vector<vector<float> > un;
    vector<vector<float> > vn;
    vector<vector<float> > comb;
    ones(u,ny,nx);
    ones(v,ny,nx);
    ones(un,ny,nx);
    ones(vn,ny,nx);
    ones(comb,ny,nx);
   
    for(int i=.5/dy;i<1/dy+1;i++){
        for(int j=.5/dx;j<1/dx+1;j++){
            u[i][j]=2;
        }
    }
    for(int i=.5/dy;i<1/dy+1;i++){
        for(int j=.5/dx;j<1/dx+1;j++){
            v[i][j]=2;
        }
    }

    ///-------------------Grafica 1------------------
    //print_matrix(v);
    
    for(int n=0;n<=nt;n++){
        copy(u,un,ny,nx);
        copy(v,vn,ny,nx);
        
        for(int i=1;i<ny-1;i++){
            for(int j=1;j<nx-1;j++){
                u[i][j] = un[i][j]-dt/dx*un[i][j]*(un[i][j]-un[i][j-1])-dt/dy*vn[i][j]*(un[i][j]-un[i-1][j])+nu*dt/dx*2*(un[i][j+1]-2*un[i][j]+un[i][j-1])+nu*dt/dy*2*(un[i+1][j]-2*un[i][j]+un[i-1][j]);
                v[i][j] = vn[i][j] - dt/dx*un[i][j]*(vn[i][j]-vn[i][j-1])-dt/dy*vn[i][j]*(vn[i][j]-vn[i-1][j])+nu*dt/dx*2*(vn[i][j+1]-2*vn[i][j]+vn[i][j-1])+nu*dt/dy*2*(vn[i+1][j]-2*vn[i][j]+vn[i-1][j]);
            }
        }
        
        for(int i=0;i<ny;i++){
            u[i][0]=1;
            u[i][nx-1]=1;
            v[i][0]=1;
            v[i][nx-1]=1;
            
        }
        for(int i=0;i<nx;i++){
            u[0][i]=1;
            u[ny-1][i]=1;
            v[0][i]=1;
            v[ny-1][i]=1;
        }
    }
    
    ///-------------------Grafica 2------------------
    print_matrix(v,ny,nx);
    return 0;
}
/*
                u[i][j] = un[i][j]-dt/dx*un[i][j]*(un[i][j]-un[i][j-1])-dt/dy*vn[i][j]* \
                   (un[i][j]-un[i-1][j])+nu*dt/dx*2*(un[i][j+1]-2*un[i][j]+un[i][j-1])+ \
                   nu*dt/dy*2*(un[i+1][j]-2*un[i][j]+un[i-1][j]);
                v[i][j] = vn[i][j] - dt/dx*un[i][j]*(vn[i][j]-vn[i][j-1])-dt/dy*vn[i][j]* \
                   (vn[i][j]-vn[i-1][j])+nu*dt/dx*2*(vn[i][j+1]-2*vn[i][j]+vn[i][j-1])+ \
                   nu*dt/dy*2*(vn[i+1][j]-2*vn[i][j]+vn[i-1][j]);


*/