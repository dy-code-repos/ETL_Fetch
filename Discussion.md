# Discussion on Question
### How would you deploy this application in production?

**Option 1: AWS Lambda**
- **Integration with SQS:** AWS Lambda integrates seamlessly with SQS, providing automatic scaling and event-driven execution.
- **Transition:** Replace configuration files with environment variables and package the application for deployment.
- **Benefits and Limitations:** Lambda automatically scales with incoming messages but has a 15-minute execution limit and concurrency constraints.

**Option 2: Docker Containers**
- **Extended Execution Times:** Running code in Docker containers allows for longer execution times and greater control over the environment.
- **Horizontal Scaling:** Deploy containers on AWS EKS, EMR, or Fargate for scalable processing of SQS messages.
- **Configuration Management:** Use AWS Secrets Manager to securely store and manage configuration data.

**Conclusion:**
- **Lambda:** Ideal for event-driven tasks requiring automatic scaling.
- **Docker Containers:** Suitable for tasks needing extended execution times and more control over the environment.

### What other components would you want to add to make this production-ready?

To make the application production-ready, consider adding:

1. **Error Handling:**
   - Robust mechanisms to handle network issues, invalid messages, and database failures.
   
2. **Logging:**
   - Detailed logging to track execution and troubleshoot issues.

3. **Testing:**
   - Comprehensive unit and integration tests to ensure reliability and correctness, also test the custom algo for maskin throughly 

4. **Monitoring:**
   - Monitoring for SQS queues, Lambda functions, and database performance using AWS CloudWatch or similar tools.

5. **Security:**
   - Proper credential management using AWS IAM roles and policies.
   - Encryption of sensitive data in transit and at rest.

### How can this application scale with a growing dataset?

To handle larger datasets:

1. **Horizontal Scaling:**
   - Distribute the workload across multiple Lambda functions or Fargate instances.
   
2. **Batch Processing:**
   - Process messages in batches to reduce the number of read operations and improve efficiency.
   
3. **Database Optimization:**
   - Optimize database queries and use indexing to enhance performance.
   
4. **Auto Scaling:**
   - Use AWS Auto Scaling for Lambda functions or Kubernetes (EKS) to scale containerized applications.

### How can PII be recovered later on?

To recover PII:

1. **Custom Masking Logic:**
   - Mask IP addresses and device IDs using a custom logic that swaps digits and adds a random number.
   
2. **Unmasking Functions:**
   - Implement unmasking functions for both IP addresses and device IDs to reconstruct the original strings.
   
3. **Table Display:**
   - Used the unmasking functions when displaying tables to show unmasked data while keeping it masked in the database.

### What are the assumptions you made?

1. **Deployment:**
   - The code will be deployed on AWS services with the necessary permissions.
   
2. **Version Format:**
   - The `app_version` follows the format `<major>.<minor>.<patch>` (e.g., 2.3.4) with no component exceeding 99. Versions like 0.4 and 4 are considered equivalent.
   
3. **Configuration Management:**
   - The `config.ini` file will be replaced by AWS Secrets Manager or another secret vault for secure credential storage.
   
4. **Database and Queue Structure:**
   - The PostgreSQL table structure and the SQS queue message format will remain consistent as specified.
   
5. **Masking Requirements:**
   - Masking needs to be simple text-based to facilitate easy identification of duplicate values.
