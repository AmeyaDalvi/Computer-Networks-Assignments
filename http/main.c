#include <stdio.h>
#include <string.h>
<<<<<<< HEAD
#include <stdlib.h>
=======
>>>>>>> upstream/main

void send_http(char* host, char* msg, char* resp, size_t len);


/*
  Implement a program that takes a host, verb, and path and
  prints the contents of the response from the request
  represented by that request.
 */
int main(int argc, char* argv[]) {
  if (argc != 4) {
    printf("Invalid arguments - %s <host> <GET|POST> <path>\n", argv[0]);
    return -1;
  }
  char* host = argv[1];
  char* verb = argv[2];
  char* path = argv[3];

<<<<<<< HEAD

  /*
    STUDENT CODE HERE
   */

  // char* space = " ";
  char* http = "HTTP/1.0\r\nHost: ";
  char* message = malloc(200);
  char* endSync = "\r\n\r\n";
  //message = verb;
  strcat(message, verb);
  // printf("%s", path);
  // strncat(message, space, 1);
  strcat(message, " ");
  strcat(message, path);
  // printf("%s\n", message);
  // strncat(message, space, 1);
  strcat(message, " ");
  // printf("%s\n", message);
  strcat(message, http);
  // printf("%s%s\n", message, host);
  strcat(message, host);
  strcat(message, endSync);

  char response[4096];
  send_http(host, message, response, 4096);
  printf("%s\n", response);
  return 0;

=======
  /*
    STUDENT CODE HERE
   */
  
  return 0;
>>>>>>> upstream/main
}
