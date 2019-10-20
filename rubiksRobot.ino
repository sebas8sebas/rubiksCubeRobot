#include<Servo.h>              //Servo library

//Initial values
Servo servo1;        //initialize a servo object for the connected servo     
Servo servo2;        //initialize a servo object for the connected servo           
int angleStep1 = 5;
int rotateWait1 = 75; 
int angleStep2 = 5;




void setup() 
{ 
  Serial.begin(9600);
  servo1.attach(10);      // attach the signal pin of servo to pin10 of arduino
  servo2.attach(5);      // attach the signal pin of servo to pin5 of arduino

  //position robot
  rotate1(81);
  delay(1000);
  rotate1(71);
  delay(1000);
  pos2();
  delay(5000);

} 

  
void loop() 
{ 
 delay(1000);
 readData();
}







//flip cube
void flipCube(int pos){
  delay(500);
  if (pos==1){
    servo2.write(8);
    }
  if (pos==2){
    servo2.write(88);
    }
  if (pos==3){
    servo2.write(170);
    }
  delay(500);
  rotate1(21);
  delay(300);
  rotate1(30); 
  delay(300); 
  rotate1(88); 
  }


//Position 1
void pos1() {
   delay(700);
   servo2.write(3);
  }

//Position 2
void pos2() {
  delay(700);
  servo2.write(84);
  }


//Position 3
void pos3() {
  delay(700);
  servo2.write(179);
  }


void rotateRight(){
  delay(500);
  rotate1(88);
  pos2(); 
  
  delay(1000);
  rotate1(60); //64
  delay(500);
  rotate1(63);
  delay(500);
  pos3();
  
  delay(500);
  rotate1(88);
  pos2();
  }


void rotateLeft(){
  delay(500);
  rotate1(88);
  //pos2(); 
  servo2.write(88); //nuevo
  
  delay(1000);
  rotate1(60);//64
  delay(500);
  rotate1(63);
  delay(500);
  
  pos1();
  
  delay(500);
  rotate1(88);
  //pos2();
  servo2.write(88);//nuevo
  }

void D(){
  rotateRight();
  componerD();
  }

void Dp(){
  rotateLeft();
  componerI();
  }

void D2() {
  rotateRight(); rotateRight();
  componer2();
  }



void B(){
  flipCube(2);
  rotateRight();
  componerD();
  flipCube(2);flipCube(2);flipCube(2);
  }

void Bp(){
  flipCube(2);
  rotateLeft();
  componerI();
  flipCube(2);flipCube(2);flipCube(2);
  }

void B2(){
  flipCube(2);
  rotateRight(); rotateRight();
  componer2();
  flipCube(2);flipCube(2);flipCube(2);
  }


void U(){
  flipCube(2); flipCube(2);
  rotateRight();
  componerD();
  flipCube(2);flipCube(2);
  }

void Up(){
  flipCube(2); flipCube(2);
  rotateLeft();
  componerI();
  flipCube(2);flipCube(2);
  }
  
void U2(){
  flipCube(2); flipCube(2);
  rotateRight(); rotateRight(); 
  componer2();
  flipCube(2);flipCube(2);
  }


void Front(){
  flipCube(2); flipCube(2); flipCube(2);
  rotateRight();
  componerD();
  flipCube(2);
  }

void Frontp(){
  flipCube(2); flipCube(2); flipCube(2);
  rotateLeft();
  componerI();
  flipCube(2);
  }

void Front2(){
  flipCube(2); flipCube(2); flipCube(2);
  rotateRight(); rotateRight();
  componer2();
  flipCube(2);
  }

void R(){
  flipCube(3); 
  rotateRight();
  componerD();
  flipCube(1); 
  }

void Rp(){
  flipCube(3); 
  rotateLeft();
  componerI();
  flipCube(1); 
  }
  
void R2(){
  flipCube(3); 
  rotateRight(); rotateRight();
  componer2();
  flipCube(1); 
  }


void L(){
  flipCube(1); 
  rotateRight();
  componerD();
  flipCube(3); 
  }

void Lp(){
  flipCube(1); 
  rotateLeft();
  componerI();
  flipCube(3); 
  }

void L2(){
  flipCube(1); 
  rotateRight(); rotateRight();
  componer2();
  flipCube(3); 
  }

void componerD(){
  delay(500);
  flipCube(2);
  flipCube(3); 
  flipCube(2);
  flipCube(2);
  flipCube(2);
  }


void componerI(){
  delay(500);
  flipCube(2);
  flipCube(1); 
  flipCube(2);
  flipCube(2);
  flipCube(2);
  }


void componer2(){
  delay(500);
  flipCube(2);
  flipCube(3);
  flipCube(3); 
  flipCube(2);
  flipCube(2);
  flipCube(2);
  }






  //Rotate servo
  void rotate1(int finish) {
  int start = servo1.read();
  
  if ( finish < start){
    for(int angle = start; angle >= finish; angle -= angleStep1)    
    {                                  
    servo1.write(angle);                 
    delay(rotateWait1);                       
    }  
    
    }
  else {
  for(int angle = start; angle <= finish; angle += angleStep1)    
  {                                  
    servo1.write(angle);                 
    delay(rotateWait1);                       
  }   
  }
  servo1.write(finish); 
}


//Read data sent from python app
void readData(){
  char c1;
  char c2;
  while(Serial.available()){
    c1 = Serial.read();
    c2 = Serial.read();
    
    if (c1=='D'&&c2=='o'){
      D();
      }
    else if (c1=='D'&&c2=='p'){
      Dp();
      }
    else if (c1=='D'&&c2=='t'){
      D2();
      }
    
    else if (c1=='B'&&c2=='o'){
      B();
      }
    else if (c1=='B'&&c2=='p'){
      Bp();
      }
    else if (c1=='B'&&c2=='t'){
      B2();
      }

    else if (c1=='U'&&c2=='o'){
      U();
      }
    else if (c1=='U'&&c2=='p'){
      Up();
      }
    else if (c1=='U'&&c2=='t'){
      U2();
      }

    else if (c1=='F'&&c2=='o'){
      Front();
      }
    else if (c1=='F'&&c2=='p'){
      Frontp();
      }
    else if (c1=='F'&&c2=='t'){
      Front2();
      }


    else if (c1=='R'&&c2=='o'){
      R();
      }
    else if (c1=='R'&&c2=='p'){
      Rp();
      }
    else if (c1=='R'&&c2=='t'){
      R2();
      }


     else if (c1=='L'&&c2=='o'){
      L();
      }
    else if (c1=='L'&&c2=='p'){
      Lp();
      }
    else if (c1=='L'&&c2=='t'){
      L2();
      }
       
    }
}
