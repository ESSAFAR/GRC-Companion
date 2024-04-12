<a name="br1"></a> 



<a name="br2"></a> 

SAP GRC

**About the Tutorial**

SAP GRC (Governance, Risk and Compliance) solution enables organizations to manage

regulations and compliance and remove any risk in managing organizations’ key

operations. As per changing market situation, organizations are growing and rapidly

changing, and inappropriate documents are not acceptable for external auditors and

regulators. SAP GRC helps organization to manage their regulations and compliance.

This tutorial will walk you through the different features of SAP GRC.

**Audience**

This tutorial is designed for all those readers who are willing to learn the basics of SAP

GRC. This is also useful for those readers who wish to refresh their knowledge of GRC. SAP

Security Consultants and SAP Auditors at all levels can also draw benefits from this tutorial.

**Prerequisites**

The course is designed for beginners with little or no knowledge of SAP GRC. But you need

to have a basic understanding of SAP Basics to make the most of this tutorial.

**Disclaimer & Copyright**

ã Copyright 2018 by Tutorials Point (I) Pvt. Ltd.

All the content and graphics published in this e-book are the property of Tutorials Point (I)

Pvt. Ltd. The user of this e-book is prohibited to reuse, retain, copy, distribute or republish

any contents or a part of contents of this e-book in any manner without written consent

of the publisher.

We strive to update the contents of our website and tutorials as timely and as precisely as

possible, however, the contents may contain inaccuracies or errors. Tutorials Point (I) Pvt.

Ltd. provides no guarantee regarding the accuracy, timeliness or completeness of our

website or its contents including this tutorial. If you discover any errors on our website or

in this tutorial, please notify [us](mailto:contact@tutorialspoint.com)[ ](mailto:contact@tutorialspoint.com)[at](mailto:contact@tutorialspoint.com)[ ](mailto:contact@tutorialspoint.com)<contact@tutorialspoint.com>[.](mailto:contact@tutorialspoint.com)

i



<a name="br3"></a> 

SAP GRC

**Table of Contents**

**About the Tutorial..................................................................................................................................i**

**Audience ................................................................................................................................................i**

**Prerequisites ..........................................................................................................................................i**

**Disclaimer & Copyright...........................................................................................................................i**

**Table of Contents ..................................................................................................................................ii**

**1. SAP GRC — OVERVIEW ........................................................................................................ 1**

**Modules in SAP GRC ..............................................................................................................................1**

**2. SAP GRC — NAVIGATION..................................................................................................... 5**

**SAP GRC Work Centers ..........................................................................................................................6**

**3. SAP GRC — ACCESS CONTROL ........................................................................................... 8**

**Key Features..........................................................................................................................................8**

**How to Explore Access Control Set Up Work Center? ............................................................................8**

**4. SAP GRC — ACCESS MANAGEMENT WORK CENTER ................................................12**

**5. SAP GRC — ACCESS & AUTHORIZATION MANAGEMENT .......................................15**

**Authorization in Portal Component and NWBC ...................................................................................15**

**6. SAP GRC — AUTHORIZATION..........................................................................................19**

**Authorization in UME ..........................................................................................................................19**

**7. SAP GRC — ACCESS CONTROL LAUNCHPAD...............................................................21**

**Creating a New Launchpad in NWBC ...................................................................................................22**

**8. SAP GRC — INTEGRATION WITH ACCESS CONTROL...............................................26**

**9. SAP GRC — INTEGRATION WITH IAM ..........................................................................28**

ii



<a name="br4"></a> 

SAP GRC

**10. SAP GRC — AUDIT UNIVERSE ..........................................................................................29**

**Create an Auditable Entity...................................................................................................................29**

**SAP Process Control — Audit Risk Rating.............................................................................................30**

**Create an Audit Risk Rating .................................................................................................................30**

**11. SAP GRC — PROCESS CONTROL WORK CENTERS.....................................................32**

**My Home.............................................................................................................................................32**

**Master Data ........................................................................................................................................33**

**Reports and Analytics..........................................................................................................................34**

**12. SAP GRC — SOD RISK MANAGEMENT ...........................................................................36**

**13. SAP GRC — RISK MANAGEMENT ....................................................................................38**

**Phases in Risk Management ................................................................................................................38**

**Risk Classification ................................................................................................................................41**

**14. SAP GRC — RISK REMEDIATION.....................................................................................42**

**SAP GRC — Report Type ......................................................................................................................43**

**15. SAP GRC — MITIGATION CONTROLS ............................................................................44**

**Mitigation Control Types .....................................................................................................................44**

**Setting up Migration Controls..............................................................................................................45**

**16. SAP GRC — SUPERUSER PRIVILEGE ..............................................................................49**

**Standard Roles under Superuser Privilege Management .....................................................................49**

**17. SAP GRC — IMPLEMENTING SUPERUSER....................................................................51**

**Superuser Log......................................................................................................................................53**

**18. SAP GRC — ENHANCED RISK ANALYSIS.......................................................................55**

**Benefits of Using Organization Rules...................................................................................................56**

**19. SAP GRC — ASSIGNING MITIGATION CONTROLS......................................................58**

iii



<a name="br5"></a> 

SAP GRC

**20. SAP GRC – WORKFLOW INTEGRATION ........................................................................59**

**SAP GRC — Global Trade Services........................................................................................................60**

**Integration between SAP ERP and SAP Global Trade Services..............................................................61**

**21. SAP GRC — INSTALLATION AND CONFIGURATION .................................................62**

**22. SAP GRC — DATA SOURCES AND BUSINESS RULES..................................................69**

**23. SAP GRC — CREATING BUSINESS RULES .....................................................................72**

iv



<a name="br6"></a> 

1\. SAP GRC —Overview

SAP Governance, Risk and Compliance solution enables organizations to manage

regulations and compliance and remove any risk in managing organizations’ key

operations. As per changing market situation, organizations are growing and rapidly

changing and inappropriate documents, spreadsheets are not acceptable for external

auditors and regulators.

SAP GRC helps organization to manage their regulations and compliance and perform the

following activities:

·

Easy integration of GRC activities into existing process and automating key GRC

activities.

·

·

·

·

·

Low complexity and managing risk efficiently.

Improve risk management activities.

Managing fraud in business processed and audit management effectively.

Organizations perform better and companies can protect their values.

SAP GRC solution consists of three main areas: Analyze, manage and monitor.

**Modules in SAP GRC**

Let us now understand the different modules in SAP GRC:

**SAP GRC Access Control**

To mitigate risk in an organization, it is required to perform risk control as part of

compliance and regulation practice. Responsibilities should be clearly defined, managing

role provisioning and managing access for super user is critical for managing risk in an

organization.

**SAP GRC Process Control and Fraud Management**

SAP GRC Process Control software solution is used for managing compliance and policy

management. The compliance management capabilities allow organizations to manage

and monitor their internal control environments. Organizations can proactively fix any

identified issues and certify and report on the overall state of the corresponding compliance

activities.

SAP Process control supports the complete life cycle of policy management, including the

distribution and adherence of policies by target groups. These policies help organizations

to reduce the cost of compliance and improve management transparency and enables

organization to develop compliance management processes and policies in business

environment.

1



<a name="br7"></a> 

SAP GRC

**SAP GRC Risk Management**

SAP GRC Risk Management allows you to manage risk management activities. You can do

advance planning to identify risk in business and implement measures to manage risk and

allow you to make better decision that improves the performance of business.

Risks come in many forms:

·

·

·

·

Operational Risk

Strategic Risk

Compliance Risk

Financial Risk

**SAP GRC Audit Management**

This is used to improve the audit management process in an organization by documenting

artifacts, organizing work papers, and creating audit reports. You can easily integrate with

other governance, risk and compliance solution and enable organizations to align audit

management policies with business goals.

SAP GRC audit management helps auditor in making things simple by providing the

following capabilities:

·

You can instantly capture the artifacts for audit management and other evidences

using mobile capabilities drag-drop feature.

2



<a name="br8"></a> 

SAP GRC

·

·

You can easily create, track, and manage audit issues with global monitoring and

follow up.

You can perform search using search capabilities that allows to get more

information from legacy and working papers.

·

·

You can engage auditors with a user-friendly interface and collaboration tools.

Easy integration of audit management with SAP Fraud Management, SAP Risk

Management, and SAP Process Control to align audit process with business goals.

·

·

Quick resolution of issues using automated tracking tool.

Enhance the staff utilization, and less travel costs resulted from internal audit

planning, resource management, and scheduling.

·

·

Easy integration with SAP Business Objects reporting and data visualization tool to

visualize audit reports using Lumira and other BI reporting.

Use of pre-established templates to standardize audit artifacts and reporting

process.

**SAP GRC Fraud Management**

SAP GRC fraud management tool helps organizations to detect and prevent frauds at early

stage and hence reducing minimizing the business loss. Scans can be performed on huge

amount of data in real time with more accuracy and fraudent activities can be easily

identified.

SAP fraud management software can help organizations with following capabilities:

·

·

Easy investigation and documentation of fraud cases.

Increase the system alert and responsiveness to prevent fraudent activities to

happen more frequently in future.

·

Easy scanning of high volumes of transactions and business data.

**SAP GRC Global Trade Services**

SAP GRC GTS software helps organizations to enhance cross border supply within limits of

international trade management. It helps in reducing the penalty of risks from

International Trade Regulation authorities.

It provides centralize global trade management process with a single repository for all

compliance master data and content irrespective of size of an organization.

**SAP GRC Capability Model**

SAP BusinessObjects GRC solution consists of three main capabilities: **Analyze, Manage**

**and Monitor**.

3



<a name="br9"></a> 

SAP GRC

In the following diagram, you can see the SAP GRC Capability Model that covers all the

key features of SAP GRC software. Using GRC, organizations can check for all potential

risks and compliance findings and can take correct decision to mitigate them.

4



<a name="br10"></a> 

2\. SAP GRC —Navigation

In older versions of SAP GRC, to use access control, process control and risk management,

there was a separate navigation for each component. This means that users, to perform

cross component duties, had to login to each module separately and login multiple times.

This resulted in a tough process to manage multiple windows and documents to search

was also tough.

SAP GRC 10.0 provides direct navigation to access control, process control and risk

management components for a single user as per authorization and removes the

management of multiple windows.

**Step 1:** To perform customizing activities and maintain configuration settings for GRC

solution, go to T-code: SPRO -> SAP Reference IMG

5



<a name="br11"></a> 

SAP GRC

**Step 2:** Expand Governance, Risk and Compliance node:

**Step 3:** Logon to NetWeaver Business Client:

Run the transaction for NWBC in SAP Easy access.

It will open NetWeaver Business Client screen and you will receive the following url:

[http://ep5crgrc.renterpserver.com:8070/nwbc/~launch/?sap-client=800&sap-](http://ep5crgrc.renterpserver.com:8070/nwbc/~launch/?sap-client=800&sap-language=EN)

[language=EN](http://ep5crgrc.renterpserver.com:8070/nwbc/~launch/?sap-client=800&sap-language=EN)

**SAP GRC Work Centers**

You can use Work Centers to provide a central access point for GRC 10.0. They can be

organized based on what the customer has been licensed to operate.

**Step 1:** To access Work Centers, open NetWeaver Business Client as mentioned above.

Go to **/nwbc** option at the top to open Work Centers.

6



<a name="br12"></a> 

SAP GRC

**Step 2:** Once you click, you will be directed to the home screen of SAP NetWeaver Business

client.

Depending on the products that you have licensed, different components of the GRC

solution are displayed: **Access Control, Process Control, or Risk Management**.

7



<a name="br13"></a> 

3\. SAP GRC —Access Control

SAP GRC access control helps organizations to automatically detect, manage and prevent

access risk violations and reduce unauthorized access to company data and information.

Users can use automatic self-service to access request submission, workflow driven access

request and approvals of access. Automatic reviews of user access, role authorization and

risk violations can be used using SAP GRC Access Control.

SAP GRC Access Control handles key challenges by allowing business to manage access

risk. It helps organizations to prevent unauthorized access by defining segregation of

duties SoD and critical access and minimizing the time and cost of access risk

management.

**Key Features**

The following are the key features of SAP GRC Access Control:

·

·

·

·

·

To perform audit and compliance as per legal requirements with different audit

standards like SOX, BSI and ISO standards.

To automatically detect access risk violations across SAP and non-SAP systems in

an organization.

As mentioned, it empowers users with self-service access submission, workflow-

driven access requests and approvals of the request.

To automate reviews of user access, role authorizations, risk violations, and control

assignments in a small and large scale organization.

To efficiently manage the super-user access and avoiding risk violations and

unauthorized access to data and application in SAP and non-SAP system.

**How to Explore Access Control Set Up Work Center?**

Run the transaction for NWBC in SAP Easy access.

It will open NetWeaver Business Client screen and you will receive the following url:

[http://ep5crgrc.renterpserver.com:8070/nwbc/~launch/?sap-client=800&sap-](http://ep5crgrc.renterpserver.com:8070/nwbc/~launch/?sap-client=800&sap-language=EN)

[language=EN](http://ep5crgrc.renterpserver.com:8070/nwbc/~launch/?sap-client=800&sap-language=EN)

**Step 1:** To access Work Centers, open NetWeaver Business Client as mentioned above.

Go to **/nwbc** option at the top to open Work Centers.

8



<a name="br14"></a> 

SAP GRC

**Step 2:** Once you click, you will be directed to the home screen of SAP NetWeaver Business

client.

**Step 3:** Go to setup work center and explore the work set. Click some of the links under

each one and explore the various screens.

9



<a name="br15"></a> 

SAP GRC

**Step 4:** The Setup work center is available in Access Control and provides links to the

following sections:

·

·

·

·

·

·

·

·

·

Access Rule Maintenance

Exception Access Rules

Critical Access Rules

Generated Rules

Organizations

Mitigating Controls

Superuser Assignment

Superuser Maintenance

Access Owners

**Step 5:** You can use the above listed functions in the following ways:

·

Using Access Rule Maintenance section, you can manage access rule sets,

functions, and the access risks used to identify access violations.

·

Using Exception Access Rules, you can manage rules that supplement access rules.

10



<a name="br16"></a> 

SAP GRC

·

Using critical access rules section, you can define additional rules that identify

access to critical roles and profiles.

·

·

Using generated rules section, you can find and view generated access rules.

Under Organizations, you can maintain the company's organization structure for

compliance and risk management with related assignments.

·

·

·

·

The Mitigating Controls section allows you to manage controls to mitigate

segregation of duty, critical action, and critical permission access violations.

Superuser Assignment is where you assign owners to firefighter IDs and assign

firefighter IDs to users.

Superuser Maintenance is where you maintain firefighter, controller, and reason

code assignments.

Under Access Owners, you manage owner privileges for access management

capabilities.

11



<a name="br17"></a> 

SAP GRC

End of ebook preview

If you liked what you saw…

Buy it from our store @ **https://store.tutorialspoint.com**

12

