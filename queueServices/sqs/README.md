

# SQS (Simple Queue Service)
Amazon SQS supports both standard and FIFO queues  
* Standard
  * Unlimited Throughput
  * At-Least-Once Delivery
    * occasionally more than one copy of a message is delivered
  * Best-Effort Ordering
    * the order might not be the same
  * When: Send data between applications when the throughput is important
* FIFO
  * Exactly-Once Processing
  * FIFO
  * When: Send data between applications when the order of events is important



