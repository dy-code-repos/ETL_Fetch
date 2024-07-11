## Discussion on the questions
### Below are the answers to the questions asked in the assignment
#### How would you deploy this application in production?
- AWS Lambda seamlessly integrates with SQS, leveraging its scalability. Transition involves using environment variables instead of config files and packaging files for deployment. Lambda benefits from automatic scaling but has a 15-minute execution limit and concurrency constraints.
- Running code on Docker containers can provide extended execution times and horizontal container scaling for processing SQS messages. Deploying on EKS, EMR, or Fargate involves Docker containerization, we can containerize our code and utilize AWS Secret Manager for configuration storage. In conclusion, Choose Lambda for event-driven tasks needing scalability or Opt for Docker containers for longer executions and control, depending on scalability and data volume.

#### What other components would you want to add to make this production-ready?
I will consider adding
- Error Handling: Robust handling for network issues, invalid messages, and database failures.
- Logging: Detailed logging for tracking execution.
- Testing: Unit tests for reliability.
- Monitoring: Monitoring for SQS, Lambda, database performance, etc.
- Security: Proper credential management.

#### How can this application scale with a growing dataset?
To handle larger datasets:
Horizontal Scaling: Distribute workload across multiple Lambda/Fargate instances.
Batch Processing: Process messages in batches.
Database Optimization: Optimize database queries.
Auto Scaling: Multiple lambda instances can be used or AWS EMR can be used with EKS to scale containers to the next level.

### How can PII be recovered later on?
-


