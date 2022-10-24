#include<stdio.h> 
main()
{
    int n,a,b,c;
    printf("1.ADD\t 2.SUB\t 3.MUL\t 4.DIV\t 5.MOD\t"); 
    printf("enter a valid option(1-5)"); 
    scanf("%d",&n);
    if(n<1||n>5) 
    {
        printf("invalid option");
    } 
    printf("enter the 2 nos of your choice : "); 
    scanf("%d%d",&a,&b);
    switch(n)
    {
        case 1:c=a+b;
        printf("%d+%d=%d",a,b,c);
        break;
        case 2: c=a-b;
        printf("%d-%d=%d",a,b,c);
        break;
        case 3:c=a*b;
        printf("%dx%d=%d",a,b,c);
        break;
        case 4:c=a%b;
        printf("%d mod %d=%d",a,b,c);
        break;
        case 5:if(b!=0)
        c=a/b;
        printf("%d/%d=%d",a,b,c);   
        break;
    }
}