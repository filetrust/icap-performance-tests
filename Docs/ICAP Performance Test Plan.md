![](RackMultipart20200903-4-1b3pjlr_html_a6b41439ee29750f.jpg)

#


# ICAP Performance Test Plan

| **Status:** | Published |
|   ---      | --- |
| **Version:**| 1.0 |

**Project Overview**

This project consists of adding an ICAP component capable of handling traffic of up to 800k user base which the Glasswall Rebuild SDK can be used to regenerate documents.

**Performance Test Objectives**

This test plan covers the performance requirements, load model, performance test approach, assumptions, issues, risks, constraints, milestone/schedule etc. for Rebuild K8s performance testing.

**Analysis &amp; Requirements**

The requirement below defines the expected performance standard for the Application and Infrastructure that supports this project.

In the absence of a business requirement, it&#39;s expected that some assumptions will be made and used

**Performance Goals &amp; Success Criteria**

ICAP component is capable of handling traffic of 800k user base/2gb of data each (TBC)

Absence of traffic should result in the cluster scaling down to a minimal state

Allocated resources scale underload

Allocated resources scale down with reduced traffic

Each document is processed by the Glasswall SDK in an individual container

Service bus queues?

SLOs are met

Process the Peak number of files as expected

**Hardware &amp; Software Specifications**

**Configuration platform** : (tbc)

- Azure
- Resources to allocate to the cluster (tbc)

**Configuration characteristics**

New Container per Rebuild API process

- File Type Detection
- Analysis
- Rebuild

A container per file

Scale up or down based on the number of files being processed

**Api Endpoints:**

- **External**

- Icap server

- **Internal**

  - The transaction logs
  - The audit

**Configuration diagram that illustrate the full Icap solution:**

![Icap Architecture](/img/IcapArchitecture.png)

**Test Approach**

High level approach for performance-testing the Application and Infrastructure:

- Identify the Load test Acceptance Criteria
- Define performance test scenarios
- Create a performance benchmark with required metrics
- Use a traffic generator or test engine to generate traffic/users
- Automate the execution of the defined scenarios
- Produce Test reports using resources metrics recorded, retrieved and displayed through a portal tbc
- Integrate Performance tests in CI/CD pipeline

**Test Data Planning**

The procedure that will be used to prepare the test data for Performance Test are detailed below:

- Identify the data required
- Identify and acquire the tools needed to create, modify, and manipulate the test data.
- Test the data through the Glasswall engine to ensure that they are ready for use and align with test requirements.
- Define a strategy for obtaining and refreshing the test data when required

**Test Preparation &amp; Process**

Testing will be performed using a tier of users for which traffic will be generated using defined user profiles.

**Proposed Loading Pattern:**

A combination of the load tier and user profile will define the load pattern for every scenario

**User Load Tiers**

|**Tier Name**| **Load Tier 1** | **Load Tier 2** | **Load Tier3** | **Load Tier 4** | **Load Tier5** | **Load Tier 6** | **Peak +** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Number of Users | 10 users | 1000 users | 10000 users | 100000 users | 500000 users | 815000 users | 815000 users |
| Number of Concurrent Requests | 1 cr | 120 cr | 1200 cr | 12000 cr | 60000 cr | 100000 cr | 110000 cr |

Using the given user base of 815000 and the expected peak load of 100000 concurrent requests, we have calculated the concurrent request to be 12% of the user base executing requests simultaneously. The other load tiers have been calculated using the 12 % figure.

The peak + load tier is a reach goal and will not be included as part of the delivery.

The time for the 100000 requests still needs to be confirmed

**User Profiles**

| Id | File Type | File Content | Number of Files | File Size(mb) | Think Time (sec) |
| --- | --- | --- | --- | --- | --- |
| 1 | MS Office | Clean | 1 to 5 | 5 to 100 | 5 to 15 |
| 2 | MS Office | Structural issues | 1 to 10 | 5 to 100 | 5 to 15 |
| 3 | PDF | Clean | 1 to 5 | 5 to 100 | 5 to 15 |
| 4 | PDF | Structural issues | 1 to 10 | 5 to 100 | 5 to 15 |
| 5 | Media files | Clean | 1 to 5 | 100 to 500 | 5 to 15 |
| 6 | Media files | Structural issues | 1 to 5 | 100 to 500 | 5 to 15 |
| 7 | Media files | Structural issues | 1 to 5 | 500 to 1GB | 15 to 45 |

The number of files can be picked in the range specified for the file type. A custom script will be used to select the number of files based on the specified range.
The think time will also be picked using a custom script

**Test Execution**

Three levels of testing will be performed using defined scenarios

**Baseline Tests:** Testing with normal or average usage to verify that the available system resources are adequate for the normal daily users&#39; activities and will also be used as a base for comparison with higher load.

| Pattern | Profile | Load Duration(min) | Initial CR Count | Ramp Time up /down (sec) | Step Requests | Max CR Count |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | All | 30 | 1 | 5/5 | 10 | 120 |
| 2 | All | 60 | 1 | 20/20 | 100 | 1200 |

The baseline figures are set on the assumption that the MVP solution might be able to run them, failing this, new goals &amp; assumptions can be made. If successful, the load tests will be run.

**Load Tests:**

Testing with peak load to determine whether the system resources are enough for heaviest usage

| Pattern | Profile | Test Duration(min) | Initial CR Count | Ramp Time up /down (sec) | Step Requests | Max CR Count |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | All | 30 | 120 | 15/10 | 100 | 12000 |
| 4 | All | 60 | 12000 | 15/10 | 100 | 60000 |
| 5 | All | 30 | 60000 | 30/20 | 100 | 100000 |
| 6 | All | 60 | 60000 | 30/20 | 100 | 100000 |

The load tests will need to be successfully achieved before moving on to the Stress Test.

The peak+ may be run in this phase of testing if deemed appropriate.

**Stress Test:** Testing to find the break point of the system using increased load

| Pattern | Profile | Load Duration(min) | Initial CR Count | Ramp Time up &amp; down (sec) | Step Requests | Max CR Count |
| --- | --- | --- | --- | --- | --- | --- |
| 7 | All | 120 | 120 | 10/5 | 100 | 100000 |
| 8 | All | 120 | 120 | 5/1 | 100 | 100000 |

Three types of scenarios will be tested, and the metrics recorded for monitoring

- Users requests are sent directly to the test site
- Users requests are sent via the Squid proxy to the test site
- Users requests are sent via the Squid proxy and ICAP to the test site

The different type of user profiles will be used to execute each scenario using the load tiers

At the test start:

3 Nodes will start with the profiles to be used

1 Node for traffics directly to the test site

1 Node for traffics via the squid proxy

1 Node for traffics via the squid proxy with ICAP

For each Node:

Pods will represent the number of profiles

For ex: 1 pod will be created for profile A-\&gt;10 files per user or 1 file per user

For each Pod:

A container will represent a user and created based on the number of users

A container will perform the user actions (upload or download file) to &amp; from the test site &amp; record metrics

![Test Execution](/img/TestExecution.png)

**Test Scenarios**

1. Upload a clean file to the test site
2. Upload a sanitisation file to the configured test site
3. Download a clean file from the test site
4. Download a sanitisation file from the test site

**Metrics to monitor at each test level**

- Total Number of Requests
- Total Number of Upload Requests
- Upload Response Time / file
- Total Number of Download Requests
- Download Response Time / file
- Total Number of Files processed
- Number of rebuild failures
- Number of Successful Rebuilt
- Number of bytes processed
- Min Concurrent Requests per sec
- Max Concurrent Requests per sec
- Minimum number of files processed /sec
- Maximum number of files processed /sec
- Number of Unprocessable Requests
- Service Bus Queue Values
- Number of processing Errors
- Cluster Node resource utilization:
- Number of running nodes or pods
- Pod&#39;s Disk, CPU &amp; memory utilization

**Pass criteria:**

1. 100% of uploaded or downloaded file is successfully rebuilt
2. The response time for the ICAP server to process a file is within acceptable bounds based on the file type &amp; size
3. The minimum number of files processed per second is within acceptable bounds based on traffic
4. The minimum number of requests processed per second is within acceptable bounds based on traffic
5. The system&#39;s performance is as expected under normal load
6. The system&#39;s performance is as expected under expected high load
7. The Service Bus Queues values are acceptable

The Pass criteria will be based on the base load test

**Assumptions, Constraints, and Risks**

**Assumptions**

| **Id** | **Assumption** |
| --- | --- |
| 1 | Current JMeter test can be used to define perform initial load test with the current configuration until the caching functionality is in. |
| 2 | In the absence of load requirement, scenarios will be defined for upload and download requests using made up numbers |
| 3 | Performance Testing will be done on dedicated performance test environment |
| 4 | The test execution will be done on the same build released to prod |

**Constraints**

| **id** | **Constraint** | **Impact** |
| --- | --- | --- |
| 1 | Lack of performance tester resource | Additional resources will need to be recruited from Upwork to help |
| 2 | The number of test files required for testing is not currently available and will need to be created | Testing will not replicate real user behavior |

**Risks**

| **Id** | **Risk** | **Impact** | **Action/Mitigation** | **Assigned To** |
| --- | --- | --- | --- | --- |
| 1 | The test framework and reporting portal is still undecided, and we are assuming that it will be able to generate sufficient load | High | A POC will be done to evaluate the traffic generator&#39;s ability to generate enough load for the tests | PM |
| 2 | Performance testing can be delayed by or blocked by a functional bug discovered during testing | Low | All functional tests will be executed to an agreed level prior to performance testing start | QA |
| 3 | In the absence of a load test acceptance criteria, assumptions will be used for testing, this could result in the figures used not replicating real user traffic | High | Load requirement related questions have been asked to the customer.Accurate requirements will replace the assumptions made &amp; used prior to prod release | PO |

**Milestones**

The key milestones are listed in the table below and represents a group of tasks on which completion of Performance Testing is dependent on.

**Schedule of Task Milestones**

| **ID** | **% Done** | **At Risk** | **Task** | **Due Date** | **Responsible** |
| --- | --- | --- | --- | --- | --- |
| 1 | 90 | No | Complete Performance Test Plan | 04/09 | QA &amp; Project team |
| 2 | 50 | No | Define Performance Test Profiles &amp; Load Pattern | 04/09 | QA &amp; Project team |
| 3 | 90 | No | Develop Scenarios to execute | 04/09 | QA |
| 4 | 50 | No | Plan and Create Test Environment | 04/09 | QA &amp; SRE |
| 5 | 20 | No | Plan &amp; Create Test Execution Framework | 11/09 | QA &amp; Dev |
| 6 | 0 | No | Design Load Script | 11/09 | QA Performance Test Engineer |
| 7 | 0 | No | Plan &amp; Create Test Data | 11/09 | QA |
| 8 | 0 | No | Configure Performance Monitoring &amp; Reporting | 11/09 | Project team, SRE |
| 9 | 0 | No | Test Execution and Analysis | tbc | QA Performance Test Engineer |

**Test Environment &amp; Tools (tbc)**

The performance test will be done on a dedicated Performance test environment provisioned with the required components below:

**Environment Specifics**

| **Resource** | **Platform** | **Nbr of Nodes** | **CPU/node** | **OS** | **Memory** | **Storage** |
| --- | --- | --- | --- | --- | --- | --- |
| Azure Container Service K8 Cluster | Azure | 3 | 2 | Linux |7GiB|TBC|



**Testing and Monitoring Tools**

| **Tool** | **Purpose** |
| --- | --- |
| JMeter / Artillery | Use with distributed load for test execution |
| Reporting portal (tbc) | Retrieve &amp; report test results |
| Traffic generator | To generate load to run the tests |
| Elastic Kibana Search | To capture the logs |
| Minio | To store the objects within the cluster |
| Test file generator | To create files for testing (tbc) |

**Test Reporting**

The test results can be collected through a portal and processed automatically into a report view/file **(tbc)**

The Performance testing results will be made available to all with an overall analysis of the solution and Infrastructure.

