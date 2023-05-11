#define LED 4
#define RECEIVER 18

void setup()
{
    pinMode(LED, OUTPUT);
    pinMode(RECEIVER, INPUT);
    Serial.begin(115200);
}

void loop()
{
    Serial.println(digitalRead(RECEIVER));
    digitalWrite(LED, digitalRead(RECEIVER));
}