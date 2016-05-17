
def change_to_win( b,n,p,nShifts,bet ):
    if nShifts < 0 :
        if b==0 :
            return 1;
        return 0;
    if b<0:
        return 0;
    count=0;
    count+=change_to_win(b-b/n,n,p,nShifts-1,b/n+bet)
    count+=change_to_win(b-bet,n,p,nShifts-1,bet)
    return count
    
    
b=100.0
n=10.0
p=0.1
nShifts=10*n 
bet=0;
totP=1;
for i in range(int(nShifts)):
    totP*=2;
totP=float(totP);
r=((change_to_win(b,n,p,nShifts,bet))/totP)*p;
print r;

