 #define XSTEP A0
#define XDIR A1
#define XEN 38
#define YSTEP A6
#define YDIR A7
#define YEN A2
#define ZSTEP 46
#define ZDIR 48
#define ZEN A8
int stepTime = 1;



void setup() {
  pinMode(XSTEP, OUTPUT);
  pinMode(XDIR, OUTPUT);
  pinMode(XEN, OUTPUT);
  pinMode(YSTEP, OUTPUT);
  pinMode(YDIR, OUTPUT);
  pinMode(YEN, OUTPUT);
  pinMode(ZSTEP, OUTPUT);
  pinMode(ZDIR, OUTPUT);
  pinMode(ZEN, OUTPUT);
  digitalWrite(XEN, LOW);
  digitalWrite(YEN, LOW);
  digitalWrite(ZEN, LOW);
}


void loop() {
  digitalWrite(XDIR, HIGH);
  digitalWrite(XSTEP, HIGH);
  digitalWrite(YDIR, HIGH);
  digitalWrite(YSTEP, HIGH);
  digitalWrite(ZDIR, HIGH);
  digitalWrite(ZSTEP, HIGH);
  delay(stepTime);                      
  digitalWrite(XSTEP , LOW);
  digitalWrite(YSTEP , LOW);
  digitalWrite(ZSTEP , LOW);
  delay(stepTime);                       
}
