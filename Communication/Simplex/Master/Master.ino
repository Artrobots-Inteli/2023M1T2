#define BUTTON 23
#define TRANSMITTER 19

void setup()
{
    pinMode(BUTTON, INPUT_PULLUP);
    pinMode(TRANSMITTER, OUTPUT);
    Serial.begin(115200);
}

void loop()
{
    Serial.println(!digitalRead(BUTTON));
    digitalWrite(TRANSMITTER, !digitalRead(BUTTON));
}