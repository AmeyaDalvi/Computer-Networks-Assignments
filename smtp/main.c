#include <stdio.h>
#include <string.h>
<<<<<<< HEAD
#include <stdlib.h>
=======
>>>>>>> upstream/main

int connect_smtp(const char* host, int port);
void send_smtp(int sock, const char* msg, char* resp, size_t len);



/*
  Use the provided 'connect_smtp' and 'send_smtp' functions
  to connect to the "lunar.open.sice.indian.edu" smtp relay
  and send the commands to write emails as described in the
  assignment wiki.
 */
int main(int argc, char* argv[]) {
  if (argc != 3) {
    printf("Invalid arguments - %s <email-to> <email-filepath>", argv[0]);
    return -1;
  }

  char* rcpt = argv[1];
  char* filepath = argv[2];

  /* 
     STUDENT CODE HERE
   */
<<<<<<< HEAD

  int socket = connect_smtp("lunar.open.sice.indiana.edu", 25);
  FILE* file_ptr;
  char ch;
  file_ptr = fopen(filepath, "r");
  char email_body[4096];


  if (NULL == file_ptr) {
    printf("file can't be opened \n");
  }


// Refered from: https://www.geeksforgeeks.org/c-program-to-read-contents-of-whole-file/
// https://stackoverflow.com/questions/22621952/convert-char-to-string-in-c

  while (!feof(file_ptr)) {
      char cstr[2];
      cstr[1] = '\0';
      ch = fgetc(file_ptr);
      cstr[0] = ch;
      strcat(email_body, cstr);
  }

  int size = strlen(email_body);
  email_body[size-1] = '\0';

  printf("%d",size);

  strcat(email_body, "\r\n.\r\n"); //To append the period at the end of file
  printf("%s",email_body);
  fclose(file_ptr);

  // printf("%d",socket);
  
  char mail[100] = "MAIL FROM: ";
  char rcpt_to[100] = "RCPT TO: ";
  char response[4096];
  //HELO
  send_smtp(socket, "HELO iu.edu\n", response, 4096);
  printf("%s\n", response);

  //MAIL FROM
  strcat(mail, rcpt);
  strcat(mail, "\n");
  send_smtp(socket, mail, response, 4096);
  printf("%s\n", response);

  //RCPT TO
  strcat(rcpt_to, rcpt);
  strcat(rcpt_to, "\n");
  send_smtp(socket, rcpt_to, response, 4096);
  printf("%s\n", response);

  //DATA
  send_smtp(socket, "DATA\n", response, 4096);
  send_smtp(socket, email_body, response, 4096);
  printf("%s\n", response);
  
  return 0;

=======
  
  return 0;
>>>>>>> upstream/main
}
