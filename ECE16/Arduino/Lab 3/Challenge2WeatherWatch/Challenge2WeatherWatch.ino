void setup() {
  setupCommunication();
  setupDisplay();
}

void loop() {
  String message = receiveMessage();
  delay(50);
  String message1 = receiveMessage();
  delay(50);
  String message2 = receiveMessage();
  delay(50);
  if((message != "")&&(message1 != "")&&(message2 != "")) {
    writeDisplay(message.c_str(), 0, false);
    writeDisplay(message1.c_str(), 1, false);
    writeDisplay(message2.c_str(), 2, false);
    sendMessage(message);
    sendMessage(message1);
    sendMessage(message2); 
  }
}
