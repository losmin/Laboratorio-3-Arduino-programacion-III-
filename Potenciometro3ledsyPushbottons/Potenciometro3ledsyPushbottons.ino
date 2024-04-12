// Declaración de constantes
const int ledRojo = 10;
const int ledAmarillo = 11;
const int ledVerde = 12;
const int pb1 = 2;
const int pb2 = 3;
const int pb3 = 4;
const int potenciometro = A1;

// Declaración de variables
int valorPotenciometro;
int sequence = 0; // Variable to keep track of the sequence

void setup() {
  // Configuración de los pines
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(pb1, INPUT_PULLUP);
  pinMode(pb2, INPUT_PULLUP);
  pinMode(pb3, INPUT_PULLUP);
  Serial.begin(9600); // Inicia la comunicación serial
}

void loop() {
  // Lee el estado de los pushbuttons y enciende los leds correspondientes
  if (digitalRead(pb1) == LOW) {
    sequence = 1; // Set sequence to InOrden
  } else if (digitalRead(pb2) == LOW) {
    sequence = 2; // Set sequence to PostOrden
  } else if (digitalRead(pb3) == LOW) {
    sequence = 3; // Set sequence to PreOrden
  } else {
    sequence = 0; // Reset sequence
  }

  switch (sequence) {
    case 1:
      InOrden();
      break;
    case 2:
      PostOrden();
      break;
    case 3:
      PreOrden();
      break;
    default:
      // Turn off all LEDs
      digitalWrite(ledRojo, LOW);
      digitalWrite(ledAmarillo, LOW);
      digitalWrite(ledVerde, LOW);
      break;
  }

  // Lee el valor del potenciómetro y lo envía a Processing a través del puerto serie
  valorPotenciometro = analogRead(potenciometro);
  Serial.println(valorPotenciometro);
  delay(50); // Pequeña pausa para evitar una transmisión muy rápida de datos por el puerto serie
}

void InOrden() {
  // Encender LEDs en orden
  digitalWrite(ledRojo, HIGH);
  delay(500);
  digitalWrite(ledRojo, LOW);
  delay(100);
  digitalWrite(ledAmarillo, HIGH);
  delay(500);
  digitalWrite(ledAmarillo, LOW);
  delay(100);
  digitalWrite(ledVerde, HIGH);
  delay(500);
  digitalWrite(ledVerde, LOW);
  delay(100);
}

void PostOrden() {
  // Encender LEDs en orden inverso
  digitalWrite(ledVerde, HIGH);
  delay(500);
  digitalWrite(ledVerde, LOW);
  delay(100);
  digitalWrite(ledAmarillo, HIGH);
  delay(500);
  digitalWrite(ledAmarillo, LOW);
  delay(100);
  digitalWrite(ledRojo, HIGH);
  delay(500);
  digitalWrite(ledRojo, LOW);
  delay(100);
}

void PreOrden() {
  // Encender LEDs secuencialmente
  digitalWrite(ledRojo, HIGH);
  delay(300);
  digitalWrite(ledAmarillo, HIGH);
  delay(300);
  digitalWrite(ledVerde, HIGH);
  delay(300);

  // Apagar LEDs en orden inverso
  digitalWrite(ledVerde, LOW);
  delay(100);
  digitalWrite(ledAmarillo, LOW);
  delay(100);
  digitalWrite(ledRojo, LOW);
  delay(100);
}
