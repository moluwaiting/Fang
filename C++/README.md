
## C++笔记

- ASCII码表：NULL为0,数字 48-57，大写字母65-90，小写字母97-122，'-'-NULL即可查到各种字符的ASCII码

## Code
```C++
//string 转 int 型 底层实现
int stringToint(string s)
{
    int ss=0,size_s=s.size();
    if(s[0]!='-')
    {
        for(auto num:s){
            if (num-'0'<=9 & num-'0'>=0) ss = ss+(num-'0')*pow(10,--size_s);
            else throw "ERROR";}
        return ss;}
    else if(s[0] == '-')
    {
        auto size_s2 = size_s-1;
        for(int i = 1;i<size_s;i++){
            if (s[i]-'0'<=9 & s[i]-'0'>=0) ss = ss+(s[i]-'0')*pow(10,--size_s2);
            else throw "ERROR";}
        return -1*ss;
    }
}
```
