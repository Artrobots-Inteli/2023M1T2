#define POT_PIN 4
#define LED_PIN 23
#define LED_PWM_CHANNEL 0

#define PWM_FREQUENCY 5000
#define PWM_RESOLUTION 8

void setup()
{
    pinMode(LED_PIN, OUTPUT);
    pinMode(POT_PIN, INPUT);

    ledcSetup(LED_PWM_CHANNEL, PWM_FREQUENCY, PWM_RESOLUTION);
    ledcAttachPin(LED_PIN, LED_PWM_CHANNEL);

    Serial.begin(115200);
}

void loop()
{
    int potValue = analogRead(POT_PIN);
    int pwmValue = map(potValue, 0, 4095, 0, 255);
    ledcWrite(LED_PWM_CHANNEL, pwmValue);
    Serial.println(pwmValue);
}