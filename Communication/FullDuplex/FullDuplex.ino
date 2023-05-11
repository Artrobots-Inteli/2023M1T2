#define BUTTON 23
#define LED 4

// Os pinos de comunicação devem ser invertidos nos dois dispositivos
// o que é receiver em um é transmitter no outro e vice-versa
#define RECEIVER 18
#define TRANSMITTER 19

void setup()
{
    pinMode(BUTTON, INPUT_PULLUP);
    pinMode(LED, OUTPUT);
    pinMode(RECEIVER, INPUT);
    pinMode(TRANSMITTER, OUTPUT);
}

void loop()
{
    digitalWrite(TRANSMITTER, !digitalRead(BUTTON));
    digitalWrite(LED, digitalRead(RECEIVER));
}