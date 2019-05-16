////
//// Created by lionztt on 2019/5/10.
////
//
//#include <iostream>
//using namespace std;
//
//int main(){
//    printf(pow(100));
//    cout << "Hello, world!" << endl;
//}
//
double pow( double x, int n ){
    assert( n >= 0 );
    if( n == 0 ) return 1.0;
    double t = pow(x, n/2);
    if( n % 2) return x*t*t;
    return t*t;

}
//#include <iostream>
//using namespace std;
//int main()
//{
//    cout << "Hello, world!" << endl;
//    return 0;
//}
