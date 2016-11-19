//knopje met lampje, afstand sensor, lichtsensor en warmte sensor

#define button1 2
#define button2 3
#define led1 8
#define led2 9
#define led3 10
#define echoPin 12
#define trigPin 13


// init knoppen
int a=0;
int b=0;
int i=0;	// bediening open of dicht
int j=0;	// bediening licht/warmte/handbediening

// init lichtsensor
int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the analog resistor divider
int bovengrens = 800;     // de bovengrens van de lichtsterkte, als de lichtsterkte hierboven komt rolt het scherm uit. 
int ondergrens = 600;     // de ondergrens van de lichtsterkte, als de lichtsterkte hieronder komt rolt het scherm in. 
int schermstatus = 0;     // Of het scherm in of uitgerold is. (0 = ingerold, 1 = uitgerold)
int afstand = 10;         // afstand voor de afstands sensor


// init warmtesensor
float voltage = 0;
float sensor = 0;
float celsius = 0;
int koud = 15;
int heet = 25;
int graden = 0;
int val = 0; // waarde van seriele verbinding

void setup()
{
  Serial.begin(9600);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop()
{
  if (i == 0){  
    digitalWrite(led1, HIGH);
    digitalWrite(led3, LOW);
      if (schermstatus == 1){
        knipper(1);
        schermstatus = 0;
        b = 0;
      }
  }
  if(i == 1){
    digitalWrite(led1, LOW);
    digitalWrite(led3, HIGH);
    if (schermstatus == 0){
      knipper(0);
      schermstatus = 1;
      a = 0;
      }
   }

  if (j == 0 && digitalRead(button2) == HIGH && b == 1){j = 1;}
  if (j == 1 && digitalRead(button2) == HIGH && b == 2){j = 2;}
  if (j == 2 && digitalRead(button2) == HIGH && b == 0){j = 0;}
  if (j == 0 && digitalRead(button2) == LOW){b = 1;}
  if (j == 1 && digitalRead(button2) == LOW){b = 2;}
  if (j == 2 && digitalRead(button2) == LOW){b = 0;}

if (j == 1){
  warmte_sensor();
  }
else if (j == 2){
  hand_bediening();
 }
 else{
  licht_sensor();
 }
delay(1000);
serials();
getInput();
}




void knipper(int nummer) {
  while (afstand_sensor()!= nummer){
    digitalWrite(led2, HIGH);
    delay(200);
    digitalWrite(led2, LOW);
    delay(500);
    }
}

void serials(){
//    Serial.print("afstand");
//    Serial.println(afstand_sensor());
    Serial.println("S");
    Serial.println(schermstatus);
}

void hand_bediening(){
  if (i == 0 && digitalRead(button1) == HIGH && a == 1){i = 1;} else{} // i word 1
  if (i == 1 && digitalRead(button1) == HIGH && a == 0){i = 0;} else{} // i word 0
  if (i == 0 && digitalRead(button1) == LOW){a = 1;} else{} // Test LED=uit en S4 is losgelaten
  if (i == 1 && digitalRead(button1) == LOW){a = 0;} else{} // Test LED=aan en S4 is losgelaten
  delay(4000);
}

int afstand_sensor() {
  long duration, distance;
  digitalWrite(trigPin, LOW);  // Added this line
  delayMicroseconds(2); // Added this line
  digitalWrite(trigPin, HIGH);
  
  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;

  if (distance >= afstand || distance <= 0){
    return 0;
  }
  else {
    return 1;
  }
}

void licht_sensor() {
  photocellReading = analogRead(photocellPin);  

  Serial.println("L");
  Serial.println(photocellReading);     // the raw analog reading

 //Hier checken we de lichtsterkte en voeren we de gewenste actie. 
  if (photocellReading < ondergrens) {
    //Serial.println("Het is donker -> zonnescherm gaat in");
    i = 0;
  } else if (photocellReading > bovengrens) {
    //Serial.println("Het is zonnig -> zonnescherm gaat uit");
    i = 1;
  } else {
    //Serial.println("Het is gewoon licht -> er veranderd niets. ");
  }
    delay(4000);
};

void warmte_sensor(){
  sensor = analogRead(5);
  voltage = (sensor*5000)/1024; // converteren van sensordata naar millivolts
  voltage = voltage-500;        // verwijderen van overige voltage
  celsius = voltage/10;         // converteren van millivolts naar celcius
  graden = (int)roundf(celsius);

  //Serial.print("Temperatuur: ");  // Het printen van de huidige temperatuur op het scherm
  Serial.println("T");
  Serial.println(graden);        // PC seriele monitor.
 //Serial.println(" graden Celcius");
 // Serial.println("_ _ _ _ _ _ _ _ _ _ _ _ _ _  ");

  if (celsius <= koud) {      // Als temp te koud is gaat het groene licht branden
    i=0;
    }
  else if (celsius >= heet){    // Als het te heet is gaat het rode licht branden
    i=1;
    }
    delay(4000);
}

/**
 * Neemt de input uit de terminal en zet deze om naar de onder of bovengrens. 
 */
void getInput(void){
  String readString;
  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill 
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c;
    }
  }
  //Als de seriele data "O" bevat wordt ondergrens de waarde uit de terminal.
  if(readString.indexOf("O") >=0){
        readString.replace("O","");
        int input = readString.toInt();
        if (input < bovengrens){ondergrens = input;}
  }
  // Als de seriele data "B" bevat wordt bovengrens de waarde uit de terminal.
  if(readString.indexOf("B") >=0){
        readString.replace("B","");
        int input = readString.toInt();
        if (input > ondergrens){bovengrens = input;}
  }
    // Als de seriele data "K" bevat wordt koud de waarde uit de terminal.
  if(readString.indexOf("K") >=0){
        readString.replace("K","");
        int input = readString.toInt();
        if (input < heet){koud = input;}
  }
    // Als de seriele data "H" bevat wordt heet de waarde uit de terminal.
  if(readString.indexOf("H") >=0){
        readString.replace("H","");
        int input = readString.toInt();
        if (input > koud){heet = input;}
  }
      // Als de seriele data "I" bevat wordt i de waarde uit de terminal.
  if(readString.indexOf("I") >=0){
        readString.replace("I","");
        int input = readString.toInt();
        j = 2; 
        if (input == 0 || 1){i = input;}
  }
    // Als de seriele data "J" bevat wordt j de waarde uit de terminal.
  if(readString.indexOf("J") >=0){
        readString.replace("J","");
        int input = readString.toInt();
        if (input == 0 || 1){j = input;}
  }
}
