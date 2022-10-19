<<<<<<< HEAD
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
=======
#include <stdio.h>
#include <stdlib.h>
>>>>>>> upstream/main

/*
  Use the `getaddrinfo` and `inet_ntop` functions to convert a string host and
  integer port into a string dotted ip address and port.
 */
<<<<<<< HEAD

=======
>>>>>>> upstream/main
int main(int argc, char* argv[]) {
  if (argc != 3) {
    printf("Invalid arguments - %s <host> <port>", argv[0]);
    return -1;
  }
  char* host = argv[1];
  long port = atoi(argv[2]);

  /*
    STUDENT CODE HERE
   */

<<<<<<< HEAD
  // https://www.educative.io/answers/how-to-use-the-sprintf-method-in-c
  // Converting port (service) to char*

  char service[100];
  sprintf(service, "%ld", port);

  // Creating the "hints" 
  struct addrinfo hints;
  memset(&hints, 0, sizeof(hints));
  hints.ai_family = PF_UNSPEC;    /* Allow IPv4 or IPv6 */
  hints.ai_socktype = SOCK_STREAM; /* Datagram socket */
  hints.ai_flags = AI_PASSIVE;    /* For wildcard IP address */
  hints.ai_protocol = IPPROTO_TCP;


  struct addrinfo *response;

  int res = getaddrinfo(host, service, &hints, &response);

  if (res != 0) {
    printf("Some error");
  }

  for(struct addrinfo *i = response; i!=NULL; i= i->ai_next){
    void* raw_addr;

    if (i->ai_family == AF_INET) { // Address is IPv4
      int sszie_t = INET_ADDRSTRLEN;
      char dst[sszie_t];
      struct sockaddr_in* tmp = (struct sockaddr_in*)i->ai_addr; // Cast addr into AF_INET container
      raw_addr = &(tmp->sin_addr); // Extract the address from the container
      inet_ntop(i->ai_family, raw_addr, dst, sszie_t);
      printf("IPv4 %s\n",dst);
    }
    else { // Address is IPv6
      int sszie_t = INET6_ADDRSTRLEN;
      char dst[sszie_t];
      struct sockaddr_in6* tmp = (struct sockaddr_in6*)i->ai_addr; // Cast addr into AF_INET6 container
      raw_addr = &(tmp->sin6_addr); // Extract the address from the container
      inet_ntop(i->ai_family, raw_addr, dst, sszie_t);
      printf("IPv6 %s\n",dst);
    }
    /* Use raw_addr as a generic address for inet_ntop */
  }
=======
>>>>>>> upstream/main

  return 0;
}
