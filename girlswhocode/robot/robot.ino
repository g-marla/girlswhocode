#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int PIEZOPIN = 5;                            // Declare pin that the piezo is connected to.
// DECLARE LED PINS HERE

// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

void setup()
{
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 5. 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);      
  pinMode(5, OUTPUT);
  // Calibrate right servo
  // Attach LED pins here
}  

void forward()
{
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(-1700);
  delay(500);
}
void back()
{
  servoLeft.writeMicroseconds(-1700);
  servoRight.writeMicroseconds(-1700);
  delay(500);
}
void Right()
{
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(500);
}

void Left()
{
  servoLeft.writeMicroseconds(1300);        
  servoRight.writeMicroseconds(1300);
  delay(500);
}

void flash(int duration)
{
  digitalWrite(12, HIGH);
  delay(duration);
  digitalWrite(12,LOW);
  delay(duration);
}

void HIPS()
{
  forward();
  delay(250);
  Right();
  delay(250);
  Left();
}

void salsa()
{
  forward();
  forward();
  forward();
  back();
  forward();
  back();
}

void circle()
{
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(1500);
}

void CLOCK()
{

  servoRight.attach(12);
  servoRight.write(360);
  delay(500);
  flash(250);
  flash(250);
  flash(250);
  delay(300);
  
} 

void PIEZO()
{
  tone(5, 523, 2000);
  delay(800);
  tone(5, 780, 500);
  delay(800);
  tone(5, 690, 500);
  delay(200);
  tone(5, 655, 2000);
  delay(200);
  tone(5, 587, 500);
  delay(200);
  tone(5, 1007, 500);
  delay(800);
  tone(5, 780, 2000);
   delay(800);
  tone(5, 690, 500);
  delay(200);
  tone(5, 655, 2000);
  delay(200);
  tone(5, 587, 500);
  delay(200);
  tone(5, 988, 500);
  delay(800);
  tone(5, 780, 2000);
}

void loop()
{
  // Code for testing servos. 
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4. 
  HIPS();
  HIPS();
  PIEZO();
  delay(500);
  salsa();
  salsa();
  PIEZO();
  delay(500);
  circle();
  PIEZO();
  delay(500);
  HIPS();
  CLOCK();
  PIEZO();
  delay(500);
  PIEZO();
  delay(250);
}
