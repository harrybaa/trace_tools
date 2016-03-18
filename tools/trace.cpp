#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <limits>
#include <cstdio>
#include <cstdlib>
//#include <stdlib.h>

using namespace std;

fstream& GotoLine(fstream& file, unsigned int num){ //method: get the line at line#X
    file.seekg(ios::beg);
    for(int i=0; i < num - 1; i++){
        file.ignore(numeric_limits<streamsize>::max(),'\n');
    }
    return file;
}

template<typename T>
string str(T begin, T end)
{
    stringstream ss;
    bool first = true;
    for (; begin != end; begin++)
    {
        if (!first)
            ss << ",";
        ss << *begin;
        first = false;
    }
    return ss.str();
}

int main () {
  //ofstream traceFile;
  int lineNum = 0;
  int regNum = 0;
  int nextLine =0;
  int errLine =0;
  int prevPhiLine=1;
  string inputFile;
  string outputFile;
  cin>> inputFile;
  outputFile= inputFile+ "_fix.txt";
  string z= "0";
  string line;
  fstream myfile (inputFile.c_str());
  fstream mySecondfile (inputFile.c_str());
  ofstream writeFile (outputFile.c_str());
  string s;
  string token;
  string token1;
  string token2;
  string str1 = "-1";
  string curr_line;
  string curr_nextLine;
  string ret = "r";
  string compareLine;
   
  vector <string> v1; 
  vector <string> v2;
  
  if (myfile.is_open())
  {
    while (getline (myfile,line)) {
	  //getline (myfile,line);
	  lineNum++; //get current lineNum 
	  istringstream ss(line);
		
		while(getline(ss, token, ',') ) { 		//seperate this line by comma
			//v.push_back(token);
			if (token.compare(str1)==0) {			//get all the lines which contain '-1' 
				//GotoLine(mySecondfile, lineNum);
				//mySecondfile>>curr_line; 	//get the line with -1		
				//cout<<"-1 Lines: "<<curr_line<<endl;
				
			for (int k =1; k<4;k++){ 
				
				nextLine = lineNum+k;
				GotoLine(mySecondfile, nextLine);
				mySecondfile>>curr_nextLine; //the line after -1
				
				istringstream ss(curr_nextLine); 
				while(getline(ss, token, ',')) { //token1?
					v1.push_back(token);	
				}
				
				if(v1.at(3).compare(z)!=0 && v1.at(0).compare(ret)!=0){
					//cout<<"it is a register needs check"<<endl;
					//cout<<prevPhiLine<<endl;
					for (int i =(lineNum-1); (i> lineNum- 50 )&& (i>1) ; i--){ //i>1
						GotoLine(mySecondfile, i); //i is the lineNum
						mySecondfile>>compareLine;
						//cout<<compareLine<<'\n';
						
						istringstream ss(compareLine); 
						while(getline(ss, token, ',')) { //token2?
							v2.push_back(token);	
						}
						
						
						if ((v1.at(1).compare(v2.at(1)) ==0) &&  (v1.at(3).compare(v2.at(3)) ==0)  &&  (v1.at(4).compare(v2.at(4)) ==0) && (v1.at(2).compare(z)==0) &&(v1.at(2).compare(v2.at(2)) !=0) )
						{
							errLine=nextLine;
							//cout<<errLine<< " this line needs to be fixed"<< endl; 	//this line needs to be changed
							v1.at(2) = v2.at(2);
							s= str(v1.begin(), v1.end());
							//cout<<s<<endl;

							//for (vector<string>::const_iterator i = v1.begin(); i != v1.end(); ++i)
									//cout << *i << " "; //print out the changed line
							//cout<<'\n';
								
							break;	
						}

						vector<string>().swap(v2); 
						//v2.erase(v2.begin(), v2.end());
						
						
					} //for	

						vector<string>().swap(v2); 
						//v2.erase(v2.begin(), v2.end());
						
				} //if

				prevPhiLine= lineNum;

				vector<string>().swap(v1); 
				//v1.erase(v1.begin(), v1.end());	
				
			}	//later for
				
			} //if
		}//while	
		
			if(lineNum==errLine && !s.empty())
				line=s;
			writeFile<<line<<"\n";	
	
    }
	
	myfile.close();
	writeFile.close();
	mySecondfile.close();
	
  }
	
	else cout << "Unable to open file"<<endl; 
	
	vector<string>().swap(v1); 
	vector<string>().swap(v2); 
	v1.erase(v1.begin(), v1.end());
	v2.erase(v2.begin(), v2.end());


	return 0;	
}
