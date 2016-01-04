import java.io.*;
import java.util.*;

public class PathSumFourWays{
    public static int N=0;
    public static long[][] aData=new long[101][101]; //NxN array of inputed numbers
    public static long[][] aMoves=new long[101][101]; //NxN array of calculated paths
    public static int[][] aStatus=new int[101][101]; //NxN array of calculated paths
    
    public static long ThreeMoves (int iColumn,int iRow){
        
        int iNEWS; 
        long result=1;
        for(iNEWS=aStatus[iColumn][iRow];iNEWS<4;iNEWS++){
            switch (iNEWS){
                case 0: //go Left
                    if(iColumn>0){
                        if(aMoves[iColumn][iRow]+aData[iColumn-1][iRow]<aMoves[iColumn-1][iRow] && aMoves[iColumn-1][iRow]!=0){
                            aMoves[iColumn-1][iRow]=aMoves[iColumn][iRow]+aData[iColumn-1][iRow];
                            FillArray();//empties direction array
                            result=ThreeMoves(iColumn-1,iRow);//checks surroundings for better solution   
                        }
                    } 
                    break;
                case 1://go Right
                    if(iColumn<N-1){
                        if(aMoves[iColumn][iRow]+aData[iColumn+1][iRow]<aMoves[iColumn+1][iRow] && aMoves[iColumn+1][iRow]!=0){
                            aMoves[iColumn+1][iRow]=aMoves[iColumn][iRow]+aData[iColumn+1][iRow];
                            FillArray();//empties direction array
                            result=ThreeMoves(iColumn+1,iRow);//checks surroundings for better solution   
                        }
                    } 
                    break;
                case 2://go Up
                    if(iRow>0){
                        if(aMoves[iColumn][iRow]+aData[iColumn][iRow-1]<aMoves[iColumn][iRow-1] && aMoves[iColumn][iRow-1]!=0){
                            aMoves[iColumn][iRow-1]=aMoves[iColumn][iRow]+aData[iColumn][iRow-1];
                            FillArray();//empties direction array
                            result=ThreeMoves(iColumn,iRow-1);//checks surroundings for better solution   
                        }
                    } 
                    break;
                case 3://go Down
                    if(iRow<N-1){
                        if(aMoves[iColumn][iRow]+aData[iColumn][iRow+1]<aMoves[iColumn][iRow+1] && aMoves[iColumn][iRow+1]!=0){
                            aMoves[iColumn][iRow+1]=aMoves[iColumn][iRow]+aData[iColumn][iRow+1];
                            FillArray();//empties direction array
                            result=ThreeMoves(iColumn,iRow+1);//checks surroundings for better solution   
                        }
                    } 
                    break;

            }
        }
         return result;
         
         
    }
    public static void FillArray (){
        for (int column=0;column<N;column++){
            for (int row=0;row<N;row++){
                aStatus[column][row]=0;
            }
        }           
    }
            
  public static long TheBestOfTwo (int iColumn,int iRow){
        
         long result=1;
                if(aMoves[iColumn][iRow-1]>aMoves[iColumn-1][iRow])
                {
                    aMoves[iColumn][iRow]=aMoves[iColumn-1][iRow]+aData[iColumn][iRow];
                    
                    if(aMoves[iColumn][iRow]+aData[iColumn][iRow-1]<aMoves[iColumn][iRow-1])
                    {
                        aMoves[iColumn][iRow-1]=aMoves[iColumn][iRow]+aData[iColumn][iRow-1];
                        FillArray();//empties direction array
                        result=ThreeMoves(iColumn,iRow-1);//checks surroundings for better solution
                    }
                }
                else
                {
                    aMoves[iColumn][iRow]=aMoves[iColumn][iRow-1]+aData[iColumn][iRow];
                    
                    if(aMoves[iColumn][iRow]+aData[iColumn-1][iRow]<aMoves[iColumn-1][iRow])
                    {
                        aMoves[iColumn-1][iRow]=aMoves[iColumn][iRow]+aData[iColumn-1][iRow];
                        FillArray();//empties direction array
                        result=ThreeMoves(iColumn-1,iRow);//checks surroundings for better solution
                    }
                }
         return result;
    }
     
    public static void main (String [] args) throws IOException {  
    String FileName="matrix.txt";    
    BufferedReader in2=new BufferedReader(new FileReader(FileName));
    String str="";  
    String str2="";
    
    while ((str2=in2.readLine()) != null) //keep counting rows untill the row is empty
    {
        N++; //finds the amount of rows/columns
    }
    in2.close();
    
    BufferedReader in=new BufferedReader(new FileReader(FileName));
    long sum;
    int i;
    int j;
    int iDown;
    int iAcross;
    long result;
    int column;
    String[][] start=new String[N][N]; //NxN array of inputed strings
    long oo=99999999999L;
    long minimum=oo; //minimum will start absuredly large to ensure that any number is less than it
    String vector[]=new String[N]; //a single column of numbers(as Strings) to be used as a storage unit
    for (int row=0;row<N;row++)
    {
        str=in.readLine(); //read a full line of numbers
        vector=str.split(","); //split each number seperated by a comma
        
        for (j=0;j<N;j++)
        {
            aData[j][row]=Integer.parseInt(vector[j]); //write the (String) numbers into an NxN array of longs
        }
    }
    aMoves[0][0]=aData[0][0];
    for (i=1;i<N;i++)
    {
        for (iDown=0;iDown<i;iDown++)
        {
            if (iDown==0)
            {
                aMoves[i][0]=aMoves[i-1][0]+aData[i][0];//goes down first time
            }
            else
            {
                result=TheBestOfTwo (i, iDown);//checks corner point of ixi matrix from (i-1,i) and (i,i-1)
            }
        }
        for (iAcross=0;iAcross<i;iAcross++)
        {
            if (iAcross==0)
            {
                aMoves[0][i]=aMoves[0][i-1]+aData[0][i];//goes across first time
            }
            else
            {
                
                result=TheBestOfTwo (iAcross,i);//checks corner point of ixi matrix from (i-1,i) and (i,i-1)
            }
        }
        
        result=TheBestOfTwo (i, i);//checks corner point of ixi matrix from (i-1,i) and (i,i-1)
    }
    long answer=aMoves[N-1][N-1];
    System.out.println("The answer is: " +answer);//prints answer
    long aFinalAnswer[]=new long[N*N];
    int iFinalAnswer=0;
    aFinalAnswer[iFinalAnswer++]=aData[N-1][N-1];
    int iRow=N-1;
    int iCol=N-1;
    while(!(iRow==0 && iCol==0))
        {
            if(iRow!=0 && answer-aData[iCol][iRow]==aMoves[iCol][iRow-1]){//go up
                aFinalAnswer[iFinalAnswer++]=aData[iCol][iRow-1];
                answer=aMoves[iCol][iRow-1];
                iRow--;
            }
            else if(iCol!=0 && answer-aData[iCol][iRow]==aMoves[iCol-1][iRow]){//go left
                aFinalAnswer[iFinalAnswer++]=aData[iCol-1][iRow];
                answer=aMoves[iCol-1][iRow];
                iCol--;
            }
            else if(iCol!=N-1 && answer-aData[iCol][iRow]==aMoves[iCol+1][iRow]){//go right
                aFinalAnswer[iFinalAnswer++]=aData[iCol+1][iRow];
                answer=aMoves[iCol+1][iRow];
                iCol++;
           }
            else if(iRow!=N-1 && answer-aData[iCol][iRow]==aMoves[iCol][iRow+1]){//go down
                aFinalAnswer[iFinalAnswer++]=aData[iCol][iRow+1];
                answer=aMoves[iCol][iRow+1];
                iRow++;
           }
            
        }

      System.out.print("The path is: ");
      for(i=iFinalAnswer-1;i>0;i--){
          System.out.print(aFinalAnswer[i]+", ");//prints path
      }
      System.out.println(aFinalAnswer[0]+". ");
    }
}
