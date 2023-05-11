// https://wokwi.com/projects/364443339654461441

#define RED 19
#define GREEN 22
#define BLUE 23

#define RED_CHANNEL 0
#define GREEN_CHANNEL 1
#define BLUE_CHANNEL 2

int getColor()
{
    while (!Serial.available())
    {
    }
    return Serial.readStringUntil('\n').toInt();
}

void setup()
{
    pinMode(RED, OUTPUT);
    pinMode(GREEN, OUTPUT);
    pinMode(BLUE, OUTPUT);

    ledcSetup(RED_CHANNEL, 5000, 8);
    ledcSetup(GREEN_CHANNEL, 5000, 8);
    ledcSetup(BLUE_CHANNEL, 5000, 8);

    ledcAttachPin(RED, RED_CHANNEL);
    ledcAttachPin(GREEN, GREEN_CHANNEL);
    ledcAttachPin(BLUE, BLUE_CHANNEL);

    Serial.begin(115200);
}

int command = 0;
int r, g, b = 0;
void loop()
{
    Serial.println("Digite o r:");
    r = getColor();

    Serial.println("Digite o g:");
    g = getColor();

    Serial.println("Digite o b:");
    b = getColor();

    ledcWrite(RED_CHANNEL, r);
    ledcWrite(GREEN_CHANNEL, g);
    ledcWrite(BLUE_CHANNEL, b);
}
