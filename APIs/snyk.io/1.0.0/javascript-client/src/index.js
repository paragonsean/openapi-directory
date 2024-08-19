/**
 * Snyk API
 * The Snyk API is available to customers on [Business and Enterprise plans](https://snyk.io/plans) and allows you to programatically integrate with Snyk.  ## REST API  We are in the process of building a new, improved API (`https://api.snyk.io/rest`) built using the OpenAPI and JSON API standards. We welcome you to try it out as we shape and release endpoints until it, ultimately, becomes a full replacement for our current API.  Looking for our REST API docs? Please head over to [https://apidocs.snyk.io](https://apidocs.snyk.io)  ## API vs CLI vs Snyk integration  The API detailed below has the ability to test a package for issues, as they are defined by Snyk. It is important to note that for many package managers, using this API will be less accurate than running the [Snyk CLI](https://snyk.io/docs/using-snyk) as part of your build pipe, or just using it locally on your package. The reason for this is that more than one package version fit the requirements given in manifest files. Running the CLI locally tests the actual deployed code, and has an accurate snapshot of the dependency versions in use, while the API can only infer it, with inferior accuracy. It should be noted that the Snyk CLI has the ability to output machine-readable JSON output (with the `--json` flag to `snyk test`).  A third option, is to allow Snyk access to your development flow via the existing [Snyk integrations](https://snyk.io/docs/). The advantage to this approach is having Snyk monitor every new pull request, and suggest fixes by opening new pull requests. This can be achieved either by integrating Snyk directly to your source code management (SCM) tool, or via a broker to allow greater security and auditability.  If those are not viable options, this API is your best choice.  ## API url  The base URL for all API endpoints is https://api.snyk.io/v1/  ## Authorization  To use this API, you must get your token from Snyk. It can be seen on https://snyk.io/account/ after you register with Snyk and login.  The token should be supplied in an `Authorization` header with the token, preceded by `token`:  ```http Authorization: token API_KEY ```  Otherwise, a 401 \"Unauthorized\" response will be returned.  ```http HTTP/1.1 401 Unauthorized          {             \"code\": 401,             \"error\": \"Not authorised\",             \"message\": \"Not authorised\"         } ```  ## Overview and entities  The API is a REST API. It has the following entities:  ### Test result  The test result is the object returned from the API giving the results of testing a package for issues. It has the following fields:  | Property        | Type    | Description                                           | Example                                                         | |----------------:|---------|-------------------------------------------------------|-----------------------------------------------------------------| | ok              | boolean | Does this package have one or more issues?             | false                                                           | | issues          | object  | The issues found. See below for details.              | See below                                                       | | dependencyCount | number  | The number of dependencies the package has.           | 9                                                               | | org             | object  | The organization this test was carried out for.       | {\"name\": \"anOrg\", \"id\": \"5d7013d9-2a57-4c89-993c-0304d960193c\"} | | licensesPolicy  | object  | The organization's licenses policy used for this test | See in the examples                                             | | packageManager  | string  | The package manager for this package                  | \"maven\"                                                         | |                 |         |                                                       |                                                                 |  ### Issue  An issue is either a vulnerability or a license issue, according to the organization's policy. It has the following fields:  | Property       | Type          | Description                                                                                                                | Example                                | |---------------:|---------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------| | id             | string        | The issue ID                                                                                                               | \"SNYK-JS-BACKBONE-10054\"               | | url            | string        | A link to the issue details on snyk.io                                                                                     | \"https://snyk.io/vuln/SNYK-JS-BACKBONE-10054 | | title          | string        | The issue title                                                                                                            | \"Cross Site Scripting\"                 | | type           | string        | The issue type: \"license\" or \"vulnerability\".                                                                              | \"license\"                              | | paths          | array         | The paths to the dependencies which have an issue, and their corresponding upgrade path (if an upgrade is available). [More information about from and upgrade paths](#introduction/overview-and-entities/from-and-upgrade-paths) | [<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;\"from\": [\"a@1.0.0\", \"b@4.8.1\"],<br>&nbsp;&nbsp;&nbsp;&nbsp;\"upgrade\": [false, \"b@4.8.2\"]<br>&nbsp;&nbsp;}<br>] | | package        | string        | The package identifier according to its package manager                                                                    | \"backbone\", \"org.apache.flex.blazeds:blazeds\"| | version        | string        | The package version this issue is applicable to.                                                                           | \"0.4.0\"                                | | severity       | string        | The Snyk defined severity level: \"critical\", \"high\", \"medium\" or \"low\".                                                    | \"high\"                                 | | language       | string        | The package's programming language                                                                                         | \"js\"                                   | | packageManager | string        | The package manager                                                                                                        | \"npm\"                                  | | semver         | array[string] OR map[string]array[string] | One or more [semver](https://semver.org) ranges this issue is applicable to. The format varies according to package manager. | [\"<0.5.0, >=0.4.0\", \"<0.3.8, >=0.3.6\"] OR { \"vulnerable\": [\"[2.0.0, 3.0.0)\"], \"unaffected\": [\"[1, 2)\", \"[3, )\"] } |  ### Vulnerability  A vulnerability in a package. In addition to all the fields present in an issue, a vulnerability also has these fields:  Property        | Type    | Description                                                                                                                                                                                                                      | Example                                        | ----------------:|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|  publicationTime | Date    | The vulnerability publication time                                                                                                                                                                                               | \"2016-02-11T07:16:18.857Z\"                     |  disclosureTime  | Date    | The time this vulnerability was originally disclosed to the package maintainers                                                                                                                                                   | \"2016-02-11T07:16:18.857Z\"                     |  isUpgradable    | boolean | Is this vulnerability fixable by upgrading a dependency?                                                                                                                                                                         | true                                           |  description     | string  | The detailed description of the vulnerability, why and how it is exploitable. Provided in markdown format. | \"## Overview\\n[`org.apache.logging.log4j:log4j-core`](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22log4j-core%22)\\nIn Apache Log4j 2.x before 2.8.2, when using the TCP socket server or UDP socket server to receive serialized log events from another application, a specially crafted binary payload can be sent that, when deserialized, can execute arbitrary code.\\n\\n# Details\\nSerialization is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. The reverse process of creating object from sequence of bytes is called deserialization. Serialization is commonly used for communication (sharing objects between multiple hosts) and persistence (store the object state in a file or a database). It is an integral part of popular protocols like _Remote Method Invocation (RMI)_, _Java Management Extension (JMX)_, _Java Messaging System (JMS)_, _Action Message Format (AMF)_, _Java Server Faces (JSF) ViewState_, etc.\\n\\n_Deserialization of untrusted data_ ([CWE-502](https://cwe.mitre.org/data/definitions/502.html)), is when the application deserializes untrusted data without sufficiently verifying that the resulting data will be valid, letting the attacker to control the state or the flow of the execution. \\n\\nJava deserialization issues have been known for years. However, interest in the issue intensified greatly in 2015, when classes that could be abused to achieve remote code execution were found in a [popular library (Apache Commons Collection)](https://snyk.io/vuln/SNYK-JAVA-COMMONSCOLLECTIONS-30078). These classes were used in zero-days affecting IBM WebSphere, Oracle WebLogic and many other products.\\n\\nAn attacker just needs to identify a piece of software that has both a vulnerable class on its path, and performs deserialization on untrusted data. Then all they need to do is send the payload into the deserializer, getting the command executed.\\n\\n> Developers put too much trust in Java Object Serialization. Some even de-serialize objects pre-authentication. When deserializing an Object in Java you typically cast it to an expected type, and therefore Java's strict type system will ensure you only get valid object trees. Unfortunately, by the time the type checking happens, platform code has already created and executed significant logic. So, before the final type is checked a lot of code is executed from the readObject() methods of various objects, all of which is out of the developer's control. By combining the readObject() methods of various classes which are available on the classpath of the vulnerable application an attacker can execute functions (including calling Runtime.exec() to execute local OS commands).\\n- Apache Blog\\n\\n\\n## References\\n- [NVD](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5645)\\n- [jira issue](https://issues.apache.org/jira/browse/LOG4J2-1863)\\n\" |  isPatchable     | boolean | Is this vulnerability fixable by using a Snyk supplied patch?                                                                                                                                                                    | true                                           |  isPinnable      | boolean | Is this vulnerability fixable by pinning a transitive dependency                                                                                                                                                                 | true                                           |  identifiers     | object  | Additional vulnerability identifiers                                                                                                                                                                                             | {\"CWE\": [], \"CVE\": [\"CVE-2016-2402]}           |  credit          | string  | The reporter of the vulnerability                                                                                                                                                                                                | \"Snyk Security Team\"                           |  CVSSv3          | string  | Common Vulnerability Scoring System (CVSS) provides a way to capture the principal characteristics of a vulnerability, and produce a numerical score reflecting its severity, as well as a textual representation of that score. | \"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N\" |  cvssScore       | number  | CVSS Score                                                                                                                                                                                                                       | 5.3                                            |  patches         | array   | Patches to fix this issue, by snyk                                                                                                                                                                                               | see \"Patch\" below.                             |  upgradePath     | object  | The path to upgrade this issue, if applicable                                                                                                                                                                                    | see below                                      |  isPatched       | boolean | Is this vulnerability patched?                                                                                                                                                                                                   | false                                          |  exploitMaturity | string  | The snyk exploit maturity level  #### Patch  A patch is an object like this one:  ```json {   \"urls\": [     \"https://snyk-patches.s3.amazonaws.com/npm/backbone/20110701/backbone_20110701_0_0_0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"   ],   \"version\": \"<0.5.0 >=0.3.3\",   \"modificationTime\": \"2015-11-06T02:09:36.180Z\",   \"comments\": [     \"https://github.com/jashkenas/backbone/commit/0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"   ],   \"id\": \"patch:npm:backbone:20110701:0\" } ```  ### From and upgrade paths  Both from and upgrade paths are arrays, where each item within the array is a package `name@version`.  Take the following `from` path:  ``` [   \"my-project@1.0.0\",   \"actionpack@4.2.5\",   \"rack@1.6.4\" ] ```  Assuming this was returned as a result of a test, then we know:  - The package that was tested was `my-project@1.0.0`  - The dependency with an issue was included in the tested package via the direct dependency `actionpack@4.2.5`  - The dependency with an issue was [rack@1.6.4](https://snyk.io/vuln/rubygems:rack@1.6.4)  Take the following `upgrade` path:  ``` [   false,   \"actionpack@5.0.0\",   \"rack@2.0.1\" ] ```  Assuming this was returned as a result of a test, then we know:  - The package that was tested is not upgradable (`false`)  - The direct dependency `actionpack` should be upgraded to at least version `5.0.0` in order to fix the issue  - Upgrading `actionpack` to version `5.0.0` will cause `rack` to be installed at version `2.0.1`  If the `upgrade` path comes back as an empty array (`[]`) then this means that there is no upgrade path available which would fix the issue.  ### License issue  A license issue has no additional fields other than the ones in \"Issue\".  ### Snyk organization  The organization in Snyk this request is applicable to. The organization determines the access rights, licenses policy and is the unit of billing for private projects.  A Snyk organization has these fields:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | name        | string | The organization display name | \"deelmaker\"                            | id          | string | The ID of the organization    | \"3ab0f8d3-b17d-4953-ab6d-e1cbfe1df385\" |  ## Errors  This is a beta release of this API. Therefore, despite our efforts, errors might occur. In the unlikely event of such an error, it will have the following structure as JSON in the body:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | message     | string | Error message with reference  | Error calling Snyk api (reference: 39db46b1-ad57-47e6-a87d-e34f6968030b) | errorRef    | V4 uuid | An error ref to contact Snyk with | 39db46b1-ad57-47e6-a87d-e34f6968030b |  The error reference will also be supplied in the `x-error-reference` header in the server reply.  Example response:  ```http HTTP/1.1 500 Internal Server Error x-error-reference: a45ec9c1-065b-4f7b-baf8-dbd1552ffc9f Content-Type: application/json; charset=utf-8 Content-Length: 1848 Vary: Accept-Encoding Date: Sun, 10 Sep 2017 06:48:40 GMT ```  ## Rate Limiting  To ensure resilience against increasing request rates, we are starting to introduce rate-limiting. We are monitoring the rate-limiting system to ensure minimal impact on users while ensuring system stability. The limit is up to 2000 requests per minute, per user, subject to change. As such, we recommend calls to the API are throttled regardless of the current limit. All requests above the limit will get a response with status code `429` - `Too many requests` until requests stop for the duration of the rate-limiting interval (currently a minute).  ## Consuming Webhooks  Webhooks are delivered with a `Content-Type` of `application/json`, with the event payload as JSON in the request body. We also send the following headers:  - `X-Snyk-Event` - the name of the event  - `X-Snyk-Transport-ID` - a GUID to identify this delivery  - `X-Snyk-Timestamp` - an ISO 8601 timestamp for when the event occurred, for example: `2020-09-25T15:27:53Z`  - `X-Hub-Signature` - the HMAC hex digest of the request body, used to secure your webhooks and ensure the request did indeed come from Snyk  - `User-Agent` - identifies the origin of the request, for example: `Snyk-Webhooks/XXX`  ---  After your server is configured to receive payloads, it listens for any payload sent to the endpoint you configured. For security reasons, you should limit requests to those coming from Snyk.  ### Validating payloads  All transports sent to your webhooks have a `X-Hub-Signature` header, which contains the hash signature for the transport. The signature is a HMAC hexdigest of the request body, generated using sha256 and your `secret` as the HMAC key.  You could use a function in Node.JS such as the following to validate these signatures on incoming requests from Snyk:  ```javascript import * as crypto from 'crypto';  function verifySignature(request, secret) {   const hmac = crypto.createHmac('sha256', secret);   const buffer = JSON.stringify(request.body);   hmac.update(buffer, 'utf8');    const signature = `sha256=${hmac.digest('hex')}`;    return signature === request.headers['x-hub-signature']; } ```  ### Payload versioning  Payloads may evolve over time, and so are versioned. Payload versions are supplied as a suffix to the `X-Snyk-Event` header. For example, `project_snapshot/v0` indicates that the payload is `v0` of the `project_snapshot` event.  Version numbers only increment when a breaking change is made; for example, removing a field that used to exist, or changing the name of a field. Version numbers do not increment when making an additive change, such as adding a new field that never existed before.  **Note:** During the BETA phase, the structure of webhook payloads may change at any time, so we  recommend you check the payload version.  ### Event types  While consuming a webhook event, `X-Snyk-Event` header must be checked, as an end-point may receive multiple event types.  #### ping  The ping event happens after a new webhook is created, and can also be manually triggered using the ping webhook API. This is useful to test that your webhook receives data from Snyk correctly.  The `ping` event makes the following request:  ```jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: ping/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \"webhookId\": \"d3cf26b3-2d77-497b-bce2-23b33cc15362\" } ```  #### project_snapshot  This event is triggered every time an existing project is tested and a new snapshot is created. It is triggered on every test of a project, whether or not there are new issues. This event is not triggered when a new project is created or imported. Currently supported targets/scan types are Open Source and container.  ```jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: project_snapshot/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \"project\": { ... }, // project object matching API responses   \"org\": { ... }, // organization object matching API responses   \"group\": { ... }, // group object matching API responses   \"newIssues\": [], // array of issues object matching API responses   \"removedIssues\": [], // array of issues object matching API responses } ```  ####  Detailed example of a payload  ##### project  see: [https://snyk.docs.apiary.io/#reference/projects](https://snyk.docs.apiary.io/#reference/projects)  ```tsx \"project\": {   \"name\": \"snyk/goof\",   \"id\": \"af137b96-6966-46c1-826b-2e79ac49bbd9\",   \"created\": \"2018-10-29T09:50:54.014Z\",   \"origin\": \"github\",   \"type\": \"maven\",   \"readOnly\": false,   \"testFrequency\": \"daily\",   \"totalDependencies\": 42,   \"issueCountsBySeverity\": {     \"low\": 13,     \"medium\": 8,     \"high\": 4,     \"critical\": 5   },   \"imageId\": \"sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019\",   \"imageTag\": \"latest\",   \"imageBaseImage\": \"alpine:3\",   \"imagePlatform\": \"linux/arm64\",   \"imageCluster\": \"Production\",   \"hostname\": null,   \"remoteRepoUrl\": \"https://github.com/snyk/goof.git\",   \"lastTestedDate\": \"2019-02-05T08:54:07.704Z\",   \"browseUrl\": \"https://app.snyk.io/org/4a18d42f-0706-4ad0-b127-24078731fbed/project/af137b96-6966-46c1-826b-2e79ac49bbd9\",   \"importingUser\": {     \"id\": \"e713cf94-bb02-4ea0-89d9-613cce0caed2\",     \"name\": \"example-user@snyk.io\",     \"username\": \"exampleUser\",     \"email\": \"example-user@snyk.io\"   },   \"isMonitored\": false,   \"branch\": null,   \"targetReference\": null,   \"tags\": [     {       \"key\": \"example-tag-key\",       \"value\": \"example-tag-value\"     }   ],   \"attributes\": {     \"criticality\": [       \"high\"     ],     \"environment\": [       \"backend\"     ],     \"lifecycle\": [       \"development\"     ]   },   \"remediation\": {     \"upgrade\": {},     \"patch\": {},     \"pin\": {}   } } ```  ##### org  see: [https://snyk.docs.apiary.io/#reference/organizations](https://snyk.docs.apiary.io/#reference/organizations)  ```tsx \"org\": {   \"name\": \"My Org\",   \"id\": \"a04d9cbd-ae6e-44af-b573-0556b0ad4bd2\",   \"slug\": \"my-org\",   \"url\": \"https://api.snyk.io/org/my-org\",   \"created\": \"2020-11-18T10:39:00.983Z\" } ```  ##### group  see: [https://snyk.docs.apiary.io/#reference/groups](https://snyk.docs.apiary.io/#reference/groups)  ```tsx \"group\": {   \"name\": \"ACME Inc.\",    \"id\": \"a060a49f-636e-480f-9e14-38e773b2a97f\" } ```  ##### issue  see: https://snyk.docs.apiary.io/#reference/users/user-organization-notification-settings/list-all-aggregated-issues  ```tsx {   \"id\": \"npm:ms:20170412\",   \"issueType\": \"vuln\",   \"pkgName\": \"ms\",   \"pkgVersions\": [     \"1.0.0\"   ],   \"issueData\": {     \"id\": \"npm:ms:20170412\",     \"title\": \"Regular Expression Denial of Service (ReDoS)\",     \"severity\": \"low\",     \"url\": \"https://snyk.io/vuln/npm:ms:20170412\",     \"description\": \"Lorem ipsum\",     \"identifiers\": {       \"CVE\": [],       \"CWE\": [         \"CWE-400\"       ],       \"ALTERNATIVE\": [         \"SNYK-JS-MS-10509\"       ]     },     \"credit\": [       \"Snyk Security Research Team\"     ],     \"exploitMaturity\": \"no-known-exploit\",     \"semver\": {       \"vulnerable\": [         \">=0.7.1 <2.0.0\"       ]     },     \"publicationTime\": \"2017-05-15T06:02:45Z\",     \"disclosureTime\": \"2017-04-11T21:00:00Z\",     \"CVSSv3\": \"CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L\",     \"cvssScore\": 3.7,     \"language\": \"js\",     \"patches\": [       {         \"id\": \"patch:npm:ms:20170412:2\",         \"urls\": [           \"https://snyk-patches.s3.amazonaws.com/npm/ms/20170412/ms_071.patch\"         ],         \"version\": \"=0.7.1\",         \"comments\": [],         \"modificationTime\": \"2019-12-03T11:40:45.866206Z\"       }     ],     \"nearestFixedInVersion\": \"2.0.0\"   },   \"isPatched\": false,   \"isIgnored\": false,   \"fixInfo\": {     \"isUpgradable\": false,     \"isPinnable\": false,     \"isPatchable\": true,     \"nearestFixedInVersion\": \"2.0.0\"   },   \"priority\": {     \"score\": 399,     \"factors\": [       {         \"name\": \"isFixable\",         \"description\": \"Has a fix available\"       },       {         \"name\": \"cvssScore\",         \"description\": \"CVSS 3.7\"       }     ]   } } ```
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AddAMemberToAnOrganizationWithinAGroupRequest from './model/AddAMemberToAnOrganizationWithinAGroupRequest';
import AddATagToAProject200Response from './model/AddATagToAProject200Response';
import AddATagToAProjectRequest from './model/AddATagToAProjectRequest';
import AddIgnoreRequest from './model/AddIgnoreRequest';
import AddMemberBody from './model/AddMemberBody';
import AddNewIntegrationRequest from './model/AddNewIntegrationRequest';
import AddNewIntegrationRequestAnyOf from './model/AddNewIntegrationRequestAnyOf';
import AddNewIntegrationRequestAnyOf1 from './model/AddNewIntegrationRequestAnyOf1';
import AddNewIntegrationRequestAnyOf1Broker from './model/AddNewIntegrationRequestAnyOf1Broker';
import AddNewIntegrationRequestAnyOfCredentials from './model/AddNewIntegrationRequestAnyOfCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf';
import AddNewIntegrationRequestAnyOfCredentialsOneOf1 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf1';
import AddNewIntegrationRequestAnyOfCredentialsOneOf10 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf10';
import AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf11 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf11';
import AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf12 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf12';
import AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf13 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf13';
import AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf14 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf14';
import AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf15 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf15';
import AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf16 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf16';
import AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf17 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf17';
import AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf2 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf2';
import AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf3 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf3';
import AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf4 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf4';
import AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf5 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf5';
import AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf6 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf6';
import AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf7 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf7';
import AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf8 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf8';
import AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOf9 from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf9';
import AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials';
import AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials from './model/AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials';
import AggregatedProjectIssues from './model/AggregatedProjectIssues';
import AggregatedProjectIssuesFilters from './model/AggregatedProjectIssuesFilters';
import AggregatedProjectIssuesIssuesInner from './model/AggregatedProjectIssuesIssuesInner';
import AggregatedProjectIssuesIssuesInnerIssueData from './model/AggregatedProjectIssuesIssuesInnerIssueData';
import AllIgnores from './model/AllIgnores';
import AllJiraIssues from './model/AllJiraIssues';
import ApplyingAttributes200Response from './model/ApplyingAttributes200Response';
import ApplyingAttributes200ResponseAttributes from './model/ApplyingAttributes200ResponseAttributes';
import ApplyingAttributesRequest from './model/ApplyingAttributesRequest';
import AssignmentType from './model/AssignmentType';
import AutoRemediationPrs from './model/AutoRemediationPrs';
import BrokerSettings from './model/BrokerSettings';
import CloneAnIntegrationWithSettingsAndCredentialsRequest from './model/CloneAnIntegrationWithSettingsAndCredentialsRequest';
import ComposerLock from './model/ComposerLock';
import ComposerRequestPayload from './model/ComposerRequestPayload';
import CreateANewOrganization400Response from './model/CreateANewOrganization400Response';
import CreateANewOrganizationRequest from './model/CreateANewOrganizationRequest';
import CreateAWebhookRequest from './model/CreateAWebhookRequest';
import CreateJiraIssue200Response from './model/CreateJiraIssue200Response';
import CreateJiraIssue200ResponseJiraIssue from './model/CreateJiraIssue200ResponseJiraIssue';
import CreateJiraIssueRequest from './model/CreateJiraIssueRequest';
import CreateJiraIssueRequestFields from './model/CreateJiraIssueRequestFields';
import CreateOrganizationsBody from './model/CreateOrganizationsBody';
import DeletePendingUserProvision200Response from './model/DeletePendingUserProvision200Response';
import DeleteTagBody from './model/DeleteTagBody';
import DeleteTagFromGroup200Response from './model/DeleteTagFromGroup200Response';
import DeleteTagFromGroupRequest from './model/DeleteTagFromGroupRequest';
import DepGraphData from './model/DepGraphData';
import Dependencies from './model/Dependencies';
import DependenciesFilters from './model/DependenciesFilters';
import DependenciesFiltersFilters from './model/DependenciesFiltersFilters';
import ErrorResponse from './model/ErrorResponse';
import Function from './model/Function';
import FunctionId from './model/FunctionId';
import GetExistingIntegrationByType200Response from './model/GetExistingIntegrationByType200Response';
import GetGroupLevelAuditLogsRequest from './model/GetGroupLevelAuditLogsRequest';
import GetGroupLevelAuditLogsRequestFilters from './model/GetGroupLevelAuditLogsRequestFilters';
import GetImportJobDetails200Response from './model/GetImportJobDetails200Response';
import GetIssueCounts200Response from './model/GetIssueCounts200Response';
import GetIssueCounts200ResponseResultsInner from './model/GetIssueCounts200ResponseResultsInner';
import GetIssueCounts200ResponseResultsInnerFixable from './model/GetIssueCounts200ResponseResultsInnerFixable';
import GetIssueCounts200ResponseResultsInnerSeverity from './model/GetIssueCounts200ResponseResultsInnerSeverity';
import GetIssueCounts400Response from './model/GetIssueCounts400Response';
import GetIssueCounts400ResponseError from './model/GetIssueCounts400ResponseError';
import GetIssueCountsRequest from './model/GetIssueCountsRequest';
import GetIssueCountsRequestFilters from './model/GetIssueCountsRequestFilters';
import GetIssueCountsRequestFiltersPriorityScore from './model/GetIssueCountsRequestFiltersPriorityScore';
import GetListOfIssues200Response from './model/GetListOfIssues200Response';
import GetListOfIssues200ResponseResultsInner from './model/GetListOfIssues200ResponseResultsInner';
import GetListOfIssues200ResponseResultsInnerIssue from './model/GetListOfIssues200ResponseResultsInnerIssue';
import GetListOfIssues200ResponseResultsInnerIssueIdentifiers from './model/GetListOfIssues200ResponseResultsInnerIssueIdentifiers';
import GetListOfIssues200ResponseResultsInnerIssueSemver from './model/GetListOfIssues200ResponseResultsInnerIssueSemver';
import GetListOfIssues200ResponseResultsInnerOneOf from './model/GetListOfIssues200ResponseResultsInnerOneOf';
import GetListOfIssues200ResponseResultsInnerOneOf1 from './model/GetListOfIssues200ResponseResultsInnerOneOf1';
import GetListOfIssues200ResponseResultsInnerOneOf1Project from './model/GetListOfIssues200ResponseResultsInnerOneOf1Project';
import GetListOfIssuesRequest from './model/GetListOfIssuesRequest';
import GetListOfIssuesRequestFilters from './model/GetListOfIssuesRequestFilters';
import GetMyDetails200Response from './model/GetMyDetails200Response';
import GetOrganizationLevelAuditLogsRequest from './model/GetOrganizationLevelAuditLogsRequest';
import GetOrganizationLevelAuditLogsRequestFilters from './model/GetOrganizationLevelAuditLogsRequestFilters';
import GetProjectCounts200Response from './model/GetProjectCounts200Response';
import GetProjectCounts200ResponseResultsInner from './model/GetProjectCounts200ResponseResultsInner';
import GetProjectCountsRequest from './model/GetProjectCountsRequest';
import GetProjectCountsRequestFilters from './model/GetProjectCountsRequestFilters';
import GetProjectDependencyGraph200Response from './model/GetProjectDependencyGraph200Response';
import GetProjectDependencyGraph200ResponseDepGraph from './model/GetProjectDependencyGraph200ResponseDepGraph';
import GetProjectDependencyGraph200ResponseDepGraphGraph from './model/GetProjectDependencyGraph200ResponseDepGraphGraph';
import GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner from './model/GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner';
import GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner from './model/GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner';
import GetProjectDependencyGraph200ResponseDepGraphPkgManager from './model/GetProjectDependencyGraph200ResponseDepGraphPkgManager';
import GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner from './model/GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner';
import GetProjectDependencyGraph200ResponseDepGraphPkgsInner from './model/GetProjectDependencyGraph200ResponseDepGraphPkgsInner';
import GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo from './model/GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo';
import GetTestCounts200Response from './model/GetTestCounts200Response';
import GetTestCounts200ResponseResultsInner from './model/GetTestCounts200ResponseResultsInner';
import GetTestCounts200ResponseResultsInnerIsPrivate from './model/GetTestCounts200ResponseResultsInnerIsPrivate';
import GetTestCounts200ResponseResultsInnerIssuesPrevented from './model/GetTestCounts200ResponseResultsInnerIssuesPrevented';
import GetTestCountsRequest from './model/GetTestCountsRequest';
import GetTestCountsRequestFilters from './model/GetTestCountsRequestFilters';
import GetUserDetails200Response from './model/GetUserDetails200Response';
import GoPkgLock from './model/GoPkgLock';
import GolangdepRequestPayload from './model/GolangdepRequestPayload';
import GovendorRequestPayload from './model/GovendorRequestPayload';
import GradleFile from './model/GradleFile';
import GradleRequestPayload from './model/GradleRequestPayload';
import GradleRequestPayloadFiles from './model/GradleRequestPayloadFiles';
import Graph from './model/Graph';
import GraphDependency from './model/GraphDependency';
import GraphRequestPayload from './model/GraphRequestPayload';
import GroupSettings from './model/GroupSettings';
import GroupsAuditLogsFilters from './model/GroupsAuditLogsFilters';
import Ignore from './model/Ignore';
import IgnoreIgnorePath from './model/IgnoreIgnorePath';
import IgnoreIgnorePathIgnoredBy from './model/IgnoreIgnorePathIgnoredBy';
import IgnoreRule from './model/IgnoreRule';
import ImportTargetsRequest from './model/ImportTargetsRequest';
import ImportTargetsRequestAnyOf from './model/ImportTargetsRequestAnyOf';
import ImportTargetsRequestAnyOf1 from './model/ImportTargetsRequestAnyOf1';
import ImportTargetsRequestAnyOf1Target from './model/ImportTargetsRequestAnyOf1Target';
import ImportTargetsRequestAnyOf2 from './model/ImportTargetsRequestAnyOf2';
import ImportTargetsRequestAnyOf2Target from './model/ImportTargetsRequestAnyOf2Target';
import ImportTargetsRequestAnyOf3 from './model/ImportTargetsRequestAnyOf3';
import ImportTargetsRequestAnyOf3Target from './model/ImportTargetsRequestAnyOf3Target';
import ImportTargetsRequestAnyOf4 from './model/ImportTargetsRequestAnyOf4';
import ImportTargetsRequestAnyOf4Target from './model/ImportTargetsRequestAnyOf4Target';
import ImportTargetsRequestAnyOf5 from './model/ImportTargetsRequestAnyOf5';
import ImportTargetsRequestAnyOf5Target from './model/ImportTargetsRequestAnyOf5Target';
import ImportTargetsRequestAnyOf6 from './model/ImportTargetsRequestAnyOf6';
import ImportTargetsRequestAnyOf6Target from './model/ImportTargetsRequestAnyOf6Target';
import ImportTargetsRequestAnyOf7 from './model/ImportTargetsRequestAnyOf7';
import ImportTargetsRequestAnyOf7Target from './model/ImportTargetsRequestAnyOf7Target';
import ImportTargetsRequestAnyOf8 from './model/ImportTargetsRequestAnyOf8';
import ImportTargetsRequestAnyOf8Target from './model/ImportTargetsRequestAnyOf8Target';
import ImportTargetsRequestAnyOf9 from './model/ImportTargetsRequestAnyOf9';
import ImportTargetsRequestAnyOf9Target from './model/ImportTargetsRequestAnyOf9Target';
import ImportTargetsRequestAnyOfTarget from './model/ImportTargetsRequestAnyOfTarget';
import IntegrationSettings from './model/IntegrationSettings';
import IntegrationType from './model/IntegrationType';
import Integrations from './model/Integrations';
import InviteUsersRequest from './model/InviteUsersRequest';
import IssueCounts from './model/IssueCounts';
import IssueCountsFilters from './model/IssueCountsFilters';
import IssueCountsFiltersFilters from './model/IssueCountsFiltersFilters';
import IssuePaths from './model/IssuePaths';
import Issues from './model/Issues';
import IssuesFilters from './model/IssuesFilters';
import IssuesFiltersFilters from './model/IssuesFiltersFilters';
import IssuesResultsInner from './model/IssuesResultsInner';
import JiraIssue from './model/JiraIssue';
import JiraIssueRequest from './model/JiraIssueRequest';
import Licenses from './model/Licenses';
import LicensesFilters from './model/LicensesFilters';
import LicensesFiltersFilters from './model/LicensesFiltersFilters';
import ListAllAggregatedIssues200Response from './model/ListAllAggregatedIssues200Response';
import ListAllAggregatedIssues200ResponseIssuesInner from './model/ListAllAggregatedIssues200ResponseIssuesInner';
import ListAllAggregatedIssues200ResponseIssuesInnerFixInfo from './model/ListAllAggregatedIssues200ResponseIssuesInnerFixInfo';
import ListAllAggregatedIssues200ResponseIssuesInnerIssueData from './model/ListAllAggregatedIssues200ResponseIssuesInnerIssueData';
import ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers from './model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers';
import ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver from './model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver';
import ListAllAggregatedIssues200ResponseIssuesInnerLinks from './model/ListAllAggregatedIssues200ResponseIssuesInnerLinks';
import ListAllAggregatedIssues200ResponseIssuesInnerPriority from './model/ListAllAggregatedIssues200ResponseIssuesInnerPriority';
import ListAllAggregatedIssuesRequest from './model/ListAllAggregatedIssuesRequest';
import ListAllAggregatedIssuesRequestFilters from './model/ListAllAggregatedIssuesRequestFilters';
import ListAllAggregatedIssuesRequestFiltersPriority from './model/ListAllAggregatedIssuesRequestFiltersPriority';
import ListAllAggregatedIssuesRequestFiltersPriorityScore from './model/ListAllAggregatedIssuesRequestFiltersPriorityScore';
import ListAllDependencies200Response from './model/ListAllDependencies200Response';
import ListAllDependencies200ResponseResultsInner from './model/ListAllDependencies200ResponseResultsInner';
import ListAllDependencies200ResponseResultsInnerLicensesInner from './model/ListAllDependencies200ResponseResultsInnerLicensesInner';
import ListAllDependencies200ResponseResultsInnerProjectsInner from './model/ListAllDependencies200ResponseResultsInnerProjectsInner';
import ListAllDependenciesRequest from './model/ListAllDependenciesRequest';
import ListAllDependenciesRequestFilters from './model/ListAllDependenciesRequestFilters';
import ListAllLicenses200Response from './model/ListAllLicenses200Response';
import ListAllLicenses200ResponseResultsInner from './model/ListAllLicenses200ResponseResultsInner';
import ListAllLicenses200ResponseResultsInnerDependenciesInner from './model/ListAllLicenses200ResponseResultsInnerDependenciesInner';
import ListAllLicensesRequest from './model/ListAllLicensesRequest';
import ListAllLicensesRequestFilters from './model/ListAllLicensesRequestFilters';
import ListAllProjectSnapshotIssuePaths200Response from './model/ListAllProjectSnapshotIssuePaths200Response';
import ListAllProjectSnapshotIssuePaths200ResponseLinks from './model/ListAllProjectSnapshotIssuePaths200ResponseLinks';
import ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner from './model/ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner';
import ListAllProjectSnapshots200Response from './model/ListAllProjectSnapshots200Response';
import ListAllProjectSnapshots200ResponseSnapshotsInner from './model/ListAllProjectSnapshots200ResponseSnapshotsInner';
import ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts from './model/ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts';
import ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense from './model/ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense';
import ListAllProjectSnapshotsRequest from './model/ListAllProjectSnapshotsRequest';
import ListAllProjectSnapshotsRequestFilters from './model/ListAllProjectSnapshotsRequestFilters';
import ListAllProjects from './model/ListAllProjects';
import ListAllProjects200Response from './model/ListAllProjects200Response';
import ListAllProjects200ResponseOrg from './model/ListAllProjects200ResponseOrg';
import ListAllProjects200ResponseProjectsInner from './model/ListAllProjects200ResponseProjectsInner';
import ListAllProjectsRequest from './model/ListAllProjectsRequest';
import ListAllProjectsRequestFilters from './model/ListAllProjectsRequestFilters';
import ListAllProjectsRequestFiltersAttributes from './model/ListAllProjectsRequestFiltersAttributes';
import ListAllProjectsRequestFiltersTags from './model/ListAllProjectsRequestFiltersTags';
import ListAllTagsInAGroup200Response from './model/ListAllTagsInAGroup200Response';
import ListProjectSettings200Response from './model/ListProjectSettings200Response';
import ListProjectSettings200ResponseAutoRemediationPrs from './model/ListProjectSettings200ResponseAutoRemediationPrs';
import MavenAdditionalFile from './model/MavenAdditionalFile';
import MavenFile from './model/MavenFile';
import MavenRequestPayload from './model/MavenRequestPayload';
import MavenRequestPayloadFiles from './model/MavenRequestPayloadFiles';
import ModifyProjectNotificationSettingsRequest from './model/ModifyProjectNotificationSettingsRequest';
import MonitorDepGraphData from './model/MonitorDepGraphData';
import MonitorDepGraphRequest from './model/MonitorDepGraphRequest';
import MonitorDepGraphRequestDepGraph from './model/MonitorDepGraphRequestDepGraph';
import MonitorDepGraphRequestDepGraphGraph from './model/MonitorDepGraphRequestDepGraphGraph';
import MonitorDepGraphRequestDepGraphPkgManager from './model/MonitorDepGraphRequestDepGraphPkgManager';
import MonitorDepGraphRequestMeta from './model/MonitorDepGraphRequestMeta';
import MonitorGraph from './model/MonitorGraph';
import MonitorGraphDependency from './model/MonitorGraphDependency';
import MonitorGraphPayload from './model/MonitorGraphPayload';
import MonitorMetaData from './model/MonitorMetaData';
import MonitorNode from './model/MonitorNode';
import MonitorPackage from './model/MonitorPackage';
import MonitorPackageInfo from './model/MonitorPackageInfo';
import MonitorPkgManager from './model/MonitorPkgManager';
import MonitorRepository from './model/MonitorRepository';
import MoveProjectToADifferentOrganizationRequest from './model/MoveProjectToADifferentOrganizationRequest';
import NewIssuesNotificationSettingRequest from './model/NewIssuesNotificationSettingRequest';
import Node from './model/Node';
import NotificationSettingResponse from './model/NotificationSettingResponse';
import NotificationSettingsRequest from './model/NotificationSettingsRequest';
import NotificationSettingsResponse from './model/NotificationSettingsResponse';
import NpmRequestPayload from './model/NpmRequestPayload';
import OrgAuditLogsFilters from './model/OrgAuditLogsFilters';
import OrgOrgIdNotificationSettingsGet200Response from './model/OrgOrgIdNotificationSettingsGet200Response';
import OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations from './model/OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations';
import OrgOrgIdNotificationSettingsGet200ResponseProjectImported from './model/OrgOrgIdNotificationSettingsGet200ResponseProjectImported';
import OrgSettingsRequest from './model/OrgSettingsRequest';
import OrgSettingsResponse from './model/OrgSettingsResponse';
import Package from './model/Package';
import PackageInfo from './model/PackageInfo';
import PackageLockJsonFile from './model/PackageLockJsonFile';
import Patch from './model/Patch';
import PipRequestPayload from './model/PipRequestPayload';
import PkgManager from './model/PkgManager';
import PriorityScore from './model/PriorityScore';
import Project from './model/Project';
import ProjectAttributes from './model/ProjectAttributes';
import ProjectCounts from './model/ProjectCounts';
import ProjectCountsFilters from './model/ProjectCountsFilters';
import ProjectCountsFiltersFilters from './model/ProjectCountsFiltersFilters';
import ProjectDependencyGraph from './model/ProjectDependencyGraph';
import ProjectIssuesFilters from './model/ProjectIssuesFilters';
import ProjectIssuesFiltersFilters from './model/ProjectIssuesFiltersFilters';
import ProjectIssuesFiltersFiltersPriorityScore from './model/ProjectIssuesFiltersFiltersPriorityScore';
import ProjectMove from './model/ProjectMove';
import ProjectSettings from './model/ProjectSettings';
import ProjectSnapshots from './model/ProjectSnapshots';
import ProjectSnapshotsFilters from './model/ProjectSnapshotsFilters';
import ProjectWithoutRemediation from './model/ProjectWithoutRemediation';
import ProjectsFilters from './model/ProjectsFilters';
import ProjectsFiltersFilters from './model/ProjectsFiltersFilters';
import ProvisionAUserToTheOrganization200Response from './model/ProvisionAUserToTheOrganization200Response';
import ProvisionAUserToTheOrganizationRequest from './model/ProvisionAUserToTheOrganizationRequest';
import PullRequestAssignment from './model/PullRequestAssignment';
import Repository from './model/Repository';
import Retrieve200Response from './model/Retrieve200Response';
import Retrieve200ResponseAutoRemediationPrs from './model/Retrieve200ResponseAutoRemediationPrs';
import Retrieve200ResponseManualRemediationPrs from './model/Retrieve200ResponseManualRemediationPrs';
import Retrieve200ResponsePullRequestAssignment from './model/Retrieve200ResponsePullRequestAssignment';
import RetrieveASingleProject200Response from './model/RetrieveASingleProject200Response';
import RetrieveASingleProject200ResponseAttributes from './model/RetrieveASingleProject200ResponseAttributes';
import RetrieveASingleProject200ResponseImportingUser from './model/RetrieveASingleProject200ResponseImportingUser';
import RetrieveASingleProject200ResponseIssueCountsBySeverity from './model/RetrieveASingleProject200ResponseIssueCountsBySeverity';
import RetrieveASingleProject200ResponseRemediation from './model/RetrieveASingleProject200ResponseRemediation';
import RubygemsRequestPayload from './model/RubygemsRequestPayload';
import SBTFile from './model/SBTFile';
import SbtRequestPayload from './model/SbtRequestPayload';
import SbtRequestPayloadFiles from './model/SbtRequestPayloadFiles';
import SemverObject from './model/SemverObject';
import SetNotificationSettingsRequest from './model/SetNotificationSettingsRequest';
import SetNotificationSettingsRequestNewIssuesRemediations from './model/SetNotificationSettingsRequestNewIssuesRemediations';
import SetNotificationSettingsRequestProjectImported from './model/SetNotificationSettingsRequestProjectImported';
import SimpleNotificationSettingRequest from './model/SimpleNotificationSettingRequest';
import SimpleNotificationSettingResponse from './model/SimpleNotificationSettingResponse';
import Tag from './model/Tag';
import TagBody from './model/TagBody';
import TestComposerJsonComposerLockFileRequest from './model/TestComposerJsonComposerLockFileRequest';
import TestComposerJsonComposerLockFileRequestFiles from './model/TestComposerJsonComposerLockFileRequestFiles';
import TestComposerJsonComposerLockFileRequestFilesTarget from './model/TestComposerJsonComposerLockFileRequestFilesTarget';
import TestDepGraphRequest from './model/TestDepGraphRequest';
import TestDepGraphRequestDepGraph from './model/TestDepGraphRequestDepGraph';
import TestDepGraphRequestDepGraphGraph from './model/TestDepGraphRequestDepGraphGraph';
import TestGemfileLockFileRequest from './model/TestGemfileLockFileRequest';
import TestGemfileLockFileRequestFiles from './model/TestGemfileLockFileRequestFiles';
import TestGemfileLockFileRequestFilesTarget from './model/TestGemfileLockFileRequestFilesTarget';
import TestGopkgTomlGopkgLockFileRequest from './model/TestGopkgTomlGopkgLockFileRequest';
import TestGopkgTomlGopkgLockFileRequestFiles from './model/TestGopkgTomlGopkgLockFileRequestFiles';
import TestGopkgTomlGopkgLockFileRequestFilesTarget from './model/TestGopkgTomlGopkgLockFileRequestFilesTarget';
import TestGradleFileRequest from './model/TestGradleFileRequest';
import TestGradleFileRequestFiles from './model/TestGradleFileRequestFiles';
import TestGradleFileRequestFilesTarget from './model/TestGradleFileRequestFilesTarget';
import TestMavenFileRequest from './model/TestMavenFileRequest';
import TestMavenFileRequestFiles from './model/TestMavenFileRequestFiles';
import TestMavenFileRequestFilesTarget from './model/TestMavenFileRequestFilesTarget';
import TestPackageJsonPackageLockJsonFileRequest from './model/TestPackageJsonPackageLockJsonFileRequest';
import TestPackageJsonPackageLockJsonFileRequestFiles from './model/TestPackageJsonPackageLockJsonFileRequestFiles';
import TestPackageJsonPackageLockJsonFileRequestFilesTarget from './model/TestPackageJsonPackageLockJsonFileRequestFilesTarget';
import TestPackageJsonYarnLockFileRequest from './model/TestPackageJsonYarnLockFileRequest';
import TestRequirementsTxtFileRequest from './model/TestRequirementsTxtFileRequest';
import TestRequirementsTxtFileRequestFiles from './model/TestRequirementsTxtFileRequestFiles';
import TestRequirementsTxtFileRequestFilesTarget from './model/TestRequirementsTxtFileRequestFilesTarget';
import TestSbtFileRequest from './model/TestSbtFileRequest';
import TestVendorJsonFileRequest from './model/TestVendorJsonFileRequest';
import TestVendorJsonFileRequestFiles from './model/TestVendorJsonFileRequestFiles';
import TestVendorJsonFileRequestFilesTarget from './model/TestVendorJsonFileRequestFilesTarget';
import TestsFilters from './model/TestsFilters';
import TestsFiltersFilters from './model/TestsFiltersFilters';
import UpdateAMemberInTheOrganizationRequest from './model/UpdateAMemberInTheOrganizationRequest';
import UpdateAMemberSRoleInTheOrganizationRequest from './model/UpdateAMemberSRoleInTheOrganizationRequest';
import UpdateAProjectRequest from './model/UpdateAProjectRequest';
import UpdateAProjectRequestOwner from './model/UpdateAProjectRequestOwner';
import UpdateExistingIntegrationRequest from './model/UpdateExistingIntegrationRequest';
import UpdateExistingIntegrationRequestAnyOf from './model/UpdateExistingIntegrationRequestAnyOf';
import UpdateExistingIntegrationRequestAnyOf1 from './model/UpdateExistingIntegrationRequestAnyOf1';
import UpdateExistingIntegrationRequestAnyOf2 from './model/UpdateExistingIntegrationRequestAnyOf2';
import UpdateOrganizationSettingsRequest from './model/UpdateOrganizationSettingsRequest';
import UpdateOrganizationSettingsRequestRequestAccess from './model/UpdateOrganizationSettingsRequestRequestAccess';
import UpdateProjectSettingsRequest from './model/UpdateProjectSettingsRequest';
import UpdateRequest from './model/UpdateRequest';
import ViewGroupSettings200Response from './model/ViewGroupSettings200Response';
import ViewGroupSettings200ResponseRequestAccess from './model/ViewGroupSettings200ResponseRequestAccess';
import ViewOrganizationSettings200Response from './model/ViewOrganizationSettings200Response';
import ViewOrganizationSettings200ResponseRequestAccess from './model/ViewOrganizationSettings200ResponseRequestAccess';
import Vulnerability from './model/Vulnerability';
import YarnLockFile from './model/YarnLockFile';
import YarnRequestPayload from './model/YarnRequestPayload';
import AuditLogsApi from './api/AuditLogsApi';
import DependenciesApi from './api/DependenciesApi';
import EntitlementsApi from './api/EntitlementsApi';
import GroupsApi from './api/GroupsApi';
import ImportProjectsApi from './api/ImportProjectsApi';
import IntegrationsApi from './api/IntegrationsApi';
import LicensesApi from './api/LicensesApi';
import MonitorApi from './api/MonitorApi';
import OrganizationsApi from './api/OrganizationsApi';
import ProjectsApi from './api/ProjectsApi';
import ReportingAPIApi from './api/ReportingAPIApi';
import TestApi from './api/TestApi';
import UsersApi from './api/UsersApi';
import WebhooksApi from './api/WebhooksApi';


/**
* The Snyk API is available to customers on [Business and Enterprise plans](https://snyk.io/plans) and allows you to programatically integrate with Snyk.  ## REST API  We are in the process of building a new, improved API (&#x60;https://api.snyk.io/rest&#x60;) built using the OpenAPI and JSON API standards. We welcome you to try it out as we shape and release endpoints until it, ultimately, becomes a full replacement for our current API.  Looking for our REST API docs? Please head over to [https://apidocs.snyk.io](https://apidocs.snyk.io)  ## API vs CLI vs Snyk integration  The API detailed below has the ability to test a package for issues, as they are defined by Snyk. It is important to note that for many package managers, using this API will be less accurate than running the [Snyk CLI](https://snyk.io/docs/using-snyk) as part of your build pipe, or just using it locally on your package. The reason for this is that more than one package version fit the requirements given in manifest files. Running the CLI locally tests the actual deployed code, and has an accurate snapshot of the dependency versions in use, while the API can only infer it, with inferior accuracy. It should be noted that the Snyk CLI has the ability to output machine-readable JSON output (with the &#x60;--json&#x60; flag to &#x60;snyk test&#x60;).  A third option, is to allow Snyk access to your development flow via the existing [Snyk integrations](https://snyk.io/docs/). The advantage to this approach is having Snyk monitor every new pull request, and suggest fixes by opening new pull requests. This can be achieved either by integrating Snyk directly to your source code management (SCM) tool, or via a broker to allow greater security and auditability.  If those are not viable options, this API is your best choice.  ## API url  The base URL for all API endpoints is https://api.snyk.io/v1/  ## Authorization  To use this API, you must get your token from Snyk. It can be seen on https://snyk.io/account/ after you register with Snyk and login.  The token should be supplied in an &#x60;Authorization&#x60; header with the token, preceded by &#x60;token&#x60;:  &#x60;&#x60;&#x60;http Authorization: token API_KEY &#x60;&#x60;&#x60;  Otherwise, a 401 \&quot;Unauthorized\&quot; response will be returned.  &#x60;&#x60;&#x60;http HTTP/1.1 401 Unauthorized          {             \&quot;code\&quot;: 401,             \&quot;error\&quot;: \&quot;Not authorised\&quot;,             \&quot;message\&quot;: \&quot;Not authorised\&quot;         } &#x60;&#x60;&#x60;  ## Overview and entities  The API is a REST API. It has the following entities:  ### Test result  The test result is the object returned from the API giving the results of testing a package for issues. It has the following fields:  | Property        | Type    | Description                                           | Example                                                         | |----------------:|---------|-------------------------------------------------------|-----------------------------------------------------------------| | ok              | boolean | Does this package have one or more issues?             | false                                                           | | issues          | object  | The issues found. See below for details.              | See below                                                       | | dependencyCount | number  | The number of dependencies the package has.           | 9                                                               | | org             | object  | The organization this test was carried out for.       | {\&quot;name\&quot;: \&quot;anOrg\&quot;, \&quot;id\&quot;: \&quot;5d7013d9-2a57-4c89-993c-0304d960193c\&quot;} | | licensesPolicy  | object  | The organization&#39;s licenses policy used for this test | See in the examples                                             | | packageManager  | string  | The package manager for this package                  | \&quot;maven\&quot;                                                         | |                 |         |                                                       |                                                                 |  ### Issue  An issue is either a vulnerability or a license issue, according to the organization&#39;s policy. It has the following fields:  | Property       | Type          | Description                                                                                                                | Example                                | |---------------:|---------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------| | id             | string        | The issue ID                                                                                                               | \&quot;SNYK-JS-BACKBONE-10054\&quot;               | | url            | string        | A link to the issue details on snyk.io                                                                                     | \&quot;https://snyk.io/vuln/SNYK-JS-BACKBONE-10054 | | title          | string        | The issue title                                                                                                            | \&quot;Cross Site Scripting\&quot;                 | | type           | string        | The issue type: \&quot;license\&quot; or \&quot;vulnerability\&quot;.                                                                              | \&quot;license\&quot;                              | | paths          | array         | The paths to the dependencies which have an issue, and their corresponding upgrade path (if an upgrade is available). [More information about from and upgrade paths](#introduction/overview-and-entities/from-and-upgrade-paths) | [&lt;br&gt;&amp;nbsp;&amp;nbsp;{&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;from\&quot;: [\&quot;a@1.0.0\&quot;, \&quot;b@4.8.1\&quot;],&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;upgrade\&quot;: [false, \&quot;b@4.8.2\&quot;]&lt;br&gt;&amp;nbsp;&amp;nbsp;}&lt;br&gt;] | | package        | string        | The package identifier according to its package manager                                                                    | \&quot;backbone\&quot;, \&quot;org.apache.flex.blazeds:blazeds\&quot;| | version        | string        | The package version this issue is applicable to.                                                                           | \&quot;0.4.0\&quot;                                | | severity       | string        | The Snyk defined severity level: \&quot;critical\&quot;, \&quot;high\&quot;, \&quot;medium\&quot; or \&quot;low\&quot;.                                                    | \&quot;high\&quot;                                 | | language       | string        | The package&#39;s programming language                                                                                         | \&quot;js\&quot;                                   | | packageManager | string        | The package manager                                                                                                        | \&quot;npm\&quot;                                  | | semver         | array[string] OR map[string]array[string] | One or more [semver](https://semver.org) ranges this issue is applicable to. The format varies according to package manager. | [\&quot;&lt;0.5.0, &gt;&#x3D;0.4.0\&quot;, \&quot;&lt;0.3.8, &gt;&#x3D;0.3.6\&quot;] OR { \&quot;vulnerable\&quot;: [\&quot;[2.0.0, 3.0.0)\&quot;], \&quot;unaffected\&quot;: [\&quot;[1, 2)\&quot;, \&quot;[3, )\&quot;] } |  ### Vulnerability  A vulnerability in a package. In addition to all the fields present in an issue, a vulnerability also has these fields:  Property        | Type    | Description                                                                                                                                                                                                                      | Example                                        | ----------------:|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|  publicationTime | Date    | The vulnerability publication time                                                                                                                                                                                               | \&quot;2016-02-11T07:16:18.857Z\&quot;                     |  disclosureTime  | Date    | The time this vulnerability was originally disclosed to the package maintainers                                                                                                                                                   | \&quot;2016-02-11T07:16:18.857Z\&quot;                     |  isUpgradable    | boolean | Is this vulnerability fixable by upgrading a dependency?                                                                                                                                                                         | true                                           |  description     | string  | The detailed description of the vulnerability, why and how it is exploitable. Provided in markdown format. | \&quot;## Overview\\n[&#x60;org.apache.logging.log4j:log4j-core&#x60;](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22log4j-core%22)\\nIn Apache Log4j 2.x before 2.8.2, when using the TCP socket server or UDP socket server to receive serialized log events from another application, a specially crafted binary payload can be sent that, when deserialized, can execute arbitrary code.\\n\\n# Details\\nSerialization is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. The reverse process of creating object from sequence of bytes is called deserialization. Serialization is commonly used for communication (sharing objects between multiple hosts) and persistence (store the object state in a file or a database). It is an integral part of popular protocols like _Remote Method Invocation (RMI)_, _Java Management Extension (JMX)_, _Java Messaging System (JMS)_, _Action Message Format (AMF)_, _Java Server Faces (JSF) ViewState_, etc.\\n\\n_Deserialization of untrusted data_ ([CWE-502](https://cwe.mitre.org/data/definitions/502.html)), is when the application deserializes untrusted data without sufficiently verifying that the resulting data will be valid, letting the attacker to control the state or the flow of the execution. \\n\\nJava deserialization issues have been known for years. However, interest in the issue intensified greatly in 2015, when classes that could be abused to achieve remote code execution were found in a [popular library (Apache Commons Collection)](https://snyk.io/vuln/SNYK-JAVA-COMMONSCOLLECTIONS-30078). These classes were used in zero-days affecting IBM WebSphere, Oracle WebLogic and many other products.\\n\\nAn attacker just needs to identify a piece of software that has both a vulnerable class on its path, and performs deserialization on untrusted data. Then all they need to do is send the payload into the deserializer, getting the command executed.\\n\\n&gt; Developers put too much trust in Java Object Serialization. Some even de-serialize objects pre-authentication. When deserializing an Object in Java you typically cast it to an expected type, and therefore Java&#39;s strict type system will ensure you only get valid object trees. Unfortunately, by the time the type checking happens, platform code has already created and executed significant logic. So, before the final type is checked a lot of code is executed from the readObject() methods of various objects, all of which is out of the developer&#39;s control. By combining the readObject() methods of various classes which are available on the classpath of the vulnerable application an attacker can execute functions (including calling Runtime.exec() to execute local OS commands).\\n- Apache Blog\\n\\n\\n## References\\n- [NVD](https://web.nvd.nist.gov/view/vuln/detail?vulnId&#x3D;CVE-2017-5645)\\n- [jira issue](https://issues.apache.org/jira/browse/LOG4J2-1863)\\n\&quot; |  isPatchable     | boolean | Is this vulnerability fixable by using a Snyk supplied patch?                                                                                                                                                                    | true                                           |  isPinnable      | boolean | Is this vulnerability fixable by pinning a transitive dependency                                                                                                                                                                 | true                                           |  identifiers     | object  | Additional vulnerability identifiers                                                                                                                                                                                             | {\&quot;CWE\&quot;: [], \&quot;CVE\&quot;: [\&quot;CVE-2016-2402]}           |  credit          | string  | The reporter of the vulnerability                                                                                                                                                                                                | \&quot;Snyk Security Team\&quot;                           |  CVSSv3          | string  | Common Vulnerability Scoring System (CVSS) provides a way to capture the principal characteristics of a vulnerability, and produce a numerical score reflecting its severity, as well as a textual representation of that score. | \&quot;CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N\&quot; |  cvssScore       | number  | CVSS Score                                                                                                                                                                                                                       | 5.3                                            |  patches         | array   | Patches to fix this issue, by snyk                                                                                                                                                                                               | see \&quot;Patch\&quot; below.                             |  upgradePath     | object  | The path to upgrade this issue, if applicable                                                                                                                                                                                    | see below                                      |  isPatched       | boolean | Is this vulnerability patched?                                                                                                                                                                                                   | false                                          |  exploitMaturity | string  | The snyk exploit maturity level  #### Patch  A patch is an object like this one:  &#x60;&#x60;&#x60;json {   \&quot;urls\&quot;: [     \&quot;https://snyk-patches.s3.amazonaws.com/npm/backbone/20110701/backbone_20110701_0_0_0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\&quot;   ],   \&quot;version\&quot;: \&quot;&lt;0.5.0 &gt;&#x3D;0.3.3\&quot;,   \&quot;modificationTime\&quot;: \&quot;2015-11-06T02:09:36.180Z\&quot;,   \&quot;comments\&quot;: [     \&quot;https://github.com/jashkenas/backbone/commit/0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\&quot;   ],   \&quot;id\&quot;: \&quot;patch:npm:backbone:20110701:0\&quot; } &#x60;&#x60;&#x60;  ### From and upgrade paths  Both from and upgrade paths are arrays, where each item within the array is a package &#x60;name@version&#x60;.  Take the following &#x60;from&#x60; path:  &#x60;&#x60;&#x60; [   \&quot;my-project@1.0.0\&quot;,   \&quot;actionpack@4.2.5\&quot;,   \&quot;rack@1.6.4\&quot; ] &#x60;&#x60;&#x60;  Assuming this was returned as a result of a test, then we know:  - The package that was tested was &#x60;my-project@1.0.0&#x60;  - The dependency with an issue was included in the tested package via the direct dependency &#x60;actionpack@4.2.5&#x60;  - The dependency with an issue was [rack@1.6.4](https://snyk.io/vuln/rubygems:rack@1.6.4)  Take the following &#x60;upgrade&#x60; path:  &#x60;&#x60;&#x60; [   false,   \&quot;actionpack@5.0.0\&quot;,   \&quot;rack@2.0.1\&quot; ] &#x60;&#x60;&#x60;  Assuming this was returned as a result of a test, then we know:  - The package that was tested is not upgradable (&#x60;false&#x60;)  - The direct dependency &#x60;actionpack&#x60; should be upgraded to at least version &#x60;5.0.0&#x60; in order to fix the issue  - Upgrading &#x60;actionpack&#x60; to version &#x60;5.0.0&#x60; will cause &#x60;rack&#x60; to be installed at version &#x60;2.0.1&#x60;  If the &#x60;upgrade&#x60; path comes back as an empty array (&#x60;[]&#x60;) then this means that there is no upgrade path available which would fix the issue.  ### License issue  A license issue has no additional fields other than the ones in \&quot;Issue\&quot;.  ### Snyk organization  The organization in Snyk this request is applicable to. The organization determines the access rights, licenses policy and is the unit of billing for private projects.  A Snyk organization has these fields:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | name        | string | The organization display name | \&quot;deelmaker\&quot;                            | id          | string | The ID of the organization    | \&quot;3ab0f8d3-b17d-4953-ab6d-e1cbfe1df385\&quot; |  ## Errors  This is a beta release of this API. Therefore, despite our efforts, errors might occur. In the unlikely event of such an error, it will have the following structure as JSON in the body:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | message     | string | Error message with reference  | Error calling Snyk api (reference: 39db46b1-ad57-47e6-a87d-e34f6968030b) | errorRef    | V4 uuid | An error ref to contact Snyk with | 39db46b1-ad57-47e6-a87d-e34f6968030b |  The error reference will also be supplied in the &#x60;x-error-reference&#x60; header in the server reply.  Example response:  &#x60;&#x60;&#x60;http HTTP/1.1 500 Internal Server Error x-error-reference: a45ec9c1-065b-4f7b-baf8-dbd1552ffc9f Content-Type: application/json; charset&#x3D;utf-8 Content-Length: 1848 Vary: Accept-Encoding Date: Sun, 10 Sep 2017 06:48:40 GMT &#x60;&#x60;&#x60;  ## Rate Limiting  To ensure resilience against increasing request rates, we are starting to introduce rate-limiting. We are monitoring the rate-limiting system to ensure minimal impact on users while ensuring system stability. The limit is up to 2000 requests per minute, per user, subject to change. As such, we recommend calls to the API are throttled regardless of the current limit. All requests above the limit will get a response with status code &#x60;429&#x60; - &#x60;Too many requests&#x60; until requests stop for the duration of the rate-limiting interval (currently a minute).  ## Consuming Webhooks  Webhooks are delivered with a &#x60;Content-Type&#x60; of &#x60;application/json&#x60;, with the event payload as JSON in the request body. We also send the following headers:  - &#x60;X-Snyk-Event&#x60; - the name of the event  - &#x60;X-Snyk-Transport-ID&#x60; - a GUID to identify this delivery  - &#x60;X-Snyk-Timestamp&#x60; - an ISO 8601 timestamp for when the event occurred, for example: &#x60;2020-09-25T15:27:53Z&#x60;  - &#x60;X-Hub-Signature&#x60; - the HMAC hex digest of the request body, used to secure your webhooks and ensure the request did indeed come from Snyk  - &#x60;User-Agent&#x60; - identifies the origin of the request, for example: &#x60;Snyk-Webhooks/XXX&#x60;  ---  After your server is configured to receive payloads, it listens for any payload sent to the endpoint you configured. For security reasons, you should limit requests to those coming from Snyk.  ### Validating payloads  All transports sent to your webhooks have a &#x60;X-Hub-Signature&#x60; header, which contains the hash signature for the transport. The signature is a HMAC hexdigest of the request body, generated using sha256 and your &#x60;secret&#x60; as the HMAC key.  You could use a function in Node.JS such as the following to validate these signatures on incoming requests from Snyk:  &#x60;&#x60;&#x60;javascript import * as crypto from &#39;crypto&#39;;  function verifySignature(request, secret) {   const hmac &#x3D; crypto.createHmac(&#39;sha256&#39;, secret);   const buffer &#x3D; JSON.stringify(request.body);   hmac.update(buffer, &#39;utf8&#39;);    const signature &#x3D; &#x60;sha256&#x3D;${hmac.digest(&#39;hex&#39;)}&#x60;;    return signature &#x3D;&#x3D;&#x3D; request.headers[&#39;x-hub-signature&#39;]; } &#x60;&#x60;&#x60;  ### Payload versioning  Payloads may evolve over time, and so are versioned. Payload versions are supplied as a suffix to the &#x60;X-Snyk-Event&#x60; header. For example, &#x60;project_snapshot/v0&#x60; indicates that the payload is &#x60;v0&#x60; of the &#x60;project_snapshot&#x60; event.  Version numbers only increment when a breaking change is made; for example, removing a field that used to exist, or changing the name of a field. Version numbers do not increment when making an additive change, such as adding a new field that never existed before.  **Note:** During the BETA phase, the structure of webhook payloads may change at any time, so we  recommend you check the payload version.  ### Event types  While consuming a webhook event, &#x60;X-Snyk-Event&#x60; header must be checked, as an end-point may receive multiple event types.  #### ping  The ping event happens after a new webhook is created, and can also be manually triggered using the ping webhook API. This is useful to test that your webhook receives data from Snyk correctly.  The &#x60;ping&#x60; event makes the following request:  &#x60;&#x60;&#x60;jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: ping/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256&#x3D;7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \&quot;webhookId\&quot;: \&quot;d3cf26b3-2d77-497b-bce2-23b33cc15362\&quot; } &#x60;&#x60;&#x60;  #### project_snapshot  This event is triggered every time an existing project is tested and a new snapshot is created. It is triggered on every test of a project, whether or not there are new issues. This event is not triggered when a new project is created or imported. Currently supported targets/scan types are Open Source and container.  &#x60;&#x60;&#x60;jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: project_snapshot/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256&#x3D;7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \&quot;project\&quot;: { ... }, // project object matching API responses   \&quot;org\&quot;: { ... }, // organization object matching API responses   \&quot;group\&quot;: { ... }, // group object matching API responses   \&quot;newIssues\&quot;: [], // array of issues object matching API responses   \&quot;removedIssues\&quot;: [], // array of issues object matching API responses } &#x60;&#x60;&#x60;  ####  Detailed example of a payload  ##### project  see: [https://snyk.docs.apiary.io/#reference/projects](https://snyk.docs.apiary.io/#reference/projects)  &#x60;&#x60;&#x60;tsx \&quot;project\&quot;: {   \&quot;name\&quot;: \&quot;snyk/goof\&quot;,   \&quot;id\&quot;: \&quot;af137b96-6966-46c1-826b-2e79ac49bbd9\&quot;,   \&quot;created\&quot;: \&quot;2018-10-29T09:50:54.014Z\&quot;,   \&quot;origin\&quot;: \&quot;github\&quot;,   \&quot;type\&quot;: \&quot;maven\&quot;,   \&quot;readOnly\&quot;: false,   \&quot;testFrequency\&quot;: \&quot;daily\&quot;,   \&quot;totalDependencies\&quot;: 42,   \&quot;issueCountsBySeverity\&quot;: {     \&quot;low\&quot;: 13,     \&quot;medium\&quot;: 8,     \&quot;high\&quot;: 4,     \&quot;critical\&quot;: 5   },   \&quot;imageId\&quot;: \&quot;sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019\&quot;,   \&quot;imageTag\&quot;: \&quot;latest\&quot;,   \&quot;imageBaseImage\&quot;: \&quot;alpine:3\&quot;,   \&quot;imagePlatform\&quot;: \&quot;linux/arm64\&quot;,   \&quot;imageCluster\&quot;: \&quot;Production\&quot;,   \&quot;hostname\&quot;: null,   \&quot;remoteRepoUrl\&quot;: \&quot;https://github.com/snyk/goof.git\&quot;,   \&quot;lastTestedDate\&quot;: \&quot;2019-02-05T08:54:07.704Z\&quot;,   \&quot;browseUrl\&quot;: \&quot;https://app.snyk.io/org/4a18d42f-0706-4ad0-b127-24078731fbed/project/af137b96-6966-46c1-826b-2e79ac49bbd9\&quot;,   \&quot;importingUser\&quot;: {     \&quot;id\&quot;: \&quot;e713cf94-bb02-4ea0-89d9-613cce0caed2\&quot;,     \&quot;name\&quot;: \&quot;example-user@snyk.io\&quot;,     \&quot;username\&quot;: \&quot;exampleUser\&quot;,     \&quot;email\&quot;: \&quot;example-user@snyk.io\&quot;   },   \&quot;isMonitored\&quot;: false,   \&quot;branch\&quot;: null,   \&quot;targetReference\&quot;: null,   \&quot;tags\&quot;: [     {       \&quot;key\&quot;: \&quot;example-tag-key\&quot;,       \&quot;value\&quot;: \&quot;example-tag-value\&quot;     }   ],   \&quot;attributes\&quot;: {     \&quot;criticality\&quot;: [       \&quot;high\&quot;     ],     \&quot;environment\&quot;: [       \&quot;backend\&quot;     ],     \&quot;lifecycle\&quot;: [       \&quot;development\&quot;     ]   },   \&quot;remediation\&quot;: {     \&quot;upgrade\&quot;: {},     \&quot;patch\&quot;: {},     \&quot;pin\&quot;: {}   } } &#x60;&#x60;&#x60;  ##### org  see: [https://snyk.docs.apiary.io/#reference/organizations](https://snyk.docs.apiary.io/#reference/organizations)  &#x60;&#x60;&#x60;tsx \&quot;org\&quot;: {   \&quot;name\&quot;: \&quot;My Org\&quot;,   \&quot;id\&quot;: \&quot;a04d9cbd-ae6e-44af-b573-0556b0ad4bd2\&quot;,   \&quot;slug\&quot;: \&quot;my-org\&quot;,   \&quot;url\&quot;: \&quot;https://api.snyk.io/org/my-org\&quot;,   \&quot;created\&quot;: \&quot;2020-11-18T10:39:00.983Z\&quot; } &#x60;&#x60;&#x60;  ##### group  see: [https://snyk.docs.apiary.io/#reference/groups](https://snyk.docs.apiary.io/#reference/groups)  &#x60;&#x60;&#x60;tsx \&quot;group\&quot;: {   \&quot;name\&quot;: \&quot;ACME Inc.\&quot;,    \&quot;id\&quot;: \&quot;a060a49f-636e-480f-9e14-38e773b2a97f\&quot; } &#x60;&#x60;&#x60;  ##### issue  see: https://snyk.docs.apiary.io/#reference/users/user-organization-notification-settings/list-all-aggregated-issues  &#x60;&#x60;&#x60;tsx {   \&quot;id\&quot;: \&quot;npm:ms:20170412\&quot;,   \&quot;issueType\&quot;: \&quot;vuln\&quot;,   \&quot;pkgName\&quot;: \&quot;ms\&quot;,   \&quot;pkgVersions\&quot;: [     \&quot;1.0.0\&quot;   ],   \&quot;issueData\&quot;: {     \&quot;id\&quot;: \&quot;npm:ms:20170412\&quot;,     \&quot;title\&quot;: \&quot;Regular Expression Denial of Service (ReDoS)\&quot;,     \&quot;severity\&quot;: \&quot;low\&quot;,     \&quot;url\&quot;: \&quot;https://snyk.io/vuln/npm:ms:20170412\&quot;,     \&quot;description\&quot;: \&quot;Lorem ipsum\&quot;,     \&quot;identifiers\&quot;: {       \&quot;CVE\&quot;: [],       \&quot;CWE\&quot;: [         \&quot;CWE-400\&quot;       ],       \&quot;ALTERNATIVE\&quot;: [         \&quot;SNYK-JS-MS-10509\&quot;       ]     },     \&quot;credit\&quot;: [       \&quot;Snyk Security Research Team\&quot;     ],     \&quot;exploitMaturity\&quot;: \&quot;no-known-exploit\&quot;,     \&quot;semver\&quot;: {       \&quot;vulnerable\&quot;: [         \&quot;&gt;&#x3D;0.7.1 &lt;2.0.0\&quot;       ]     },     \&quot;publicationTime\&quot;: \&quot;2017-05-15T06:02:45Z\&quot;,     \&quot;disclosureTime\&quot;: \&quot;2017-04-11T21:00:00Z\&quot;,     \&quot;CVSSv3\&quot;: \&quot;CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L\&quot;,     \&quot;cvssScore\&quot;: 3.7,     \&quot;language\&quot;: \&quot;js\&quot;,     \&quot;patches\&quot;: [       {         \&quot;id\&quot;: \&quot;patch:npm:ms:20170412:2\&quot;,         \&quot;urls\&quot;: [           \&quot;https://snyk-patches.s3.amazonaws.com/npm/ms/20170412/ms_071.patch\&quot;         ],         \&quot;version\&quot;: \&quot;&#x3D;0.7.1\&quot;,         \&quot;comments\&quot;: [],         \&quot;modificationTime\&quot;: \&quot;2019-12-03T11:40:45.866206Z\&quot;       }     ],     \&quot;nearestFixedInVersion\&quot;: \&quot;2.0.0\&quot;   },   \&quot;isPatched\&quot;: false,   \&quot;isIgnored\&quot;: false,   \&quot;fixInfo\&quot;: {     \&quot;isUpgradable\&quot;: false,     \&quot;isPinnable\&quot;: false,     \&quot;isPatchable\&quot;: true,     \&quot;nearestFixedInVersion\&quot;: \&quot;2.0.0\&quot;   },   \&quot;priority\&quot;: {     \&quot;score\&quot;: 399,     \&quot;factors\&quot;: [       {         \&quot;name\&quot;: \&quot;isFixable\&quot;,         \&quot;description\&quot;: \&quot;Has a fix available\&quot;       },       {         \&quot;name\&quot;: \&quot;cvssScore\&quot;,         \&quot;description\&quot;: \&quot;CVSS 3.7\&quot;       }     ]   } } &#x60;&#x60;&#x60;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var SnykApi = require('index'); // See note below*.
* var xxxSvc = new SnykApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new SnykApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new SnykApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new SnykApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddAMemberToAnOrganizationWithinAGroupRequest model constructor.
     * @property {module:model/AddAMemberToAnOrganizationWithinAGroupRequest}
     */
    AddAMemberToAnOrganizationWithinAGroupRequest,

    /**
     * The AddATagToAProject200Response model constructor.
     * @property {module:model/AddATagToAProject200Response}
     */
    AddATagToAProject200Response,

    /**
     * The AddATagToAProjectRequest model constructor.
     * @property {module:model/AddATagToAProjectRequest}
     */
    AddATagToAProjectRequest,

    /**
     * The AddIgnoreRequest model constructor.
     * @property {module:model/AddIgnoreRequest}
     */
    AddIgnoreRequest,

    /**
     * The AddMemberBody model constructor.
     * @property {module:model/AddMemberBody}
     */
    AddMemberBody,

    /**
     * The AddNewIntegrationRequest model constructor.
     * @property {module:model/AddNewIntegrationRequest}
     */
    AddNewIntegrationRequest,

    /**
     * The AddNewIntegrationRequestAnyOf model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOf}
     */
    AddNewIntegrationRequestAnyOf,

    /**
     * The AddNewIntegrationRequestAnyOf1 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOf1}
     */
    AddNewIntegrationRequestAnyOf1,

    /**
     * The AddNewIntegrationRequestAnyOf1Broker model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOf1Broker}
     */
    AddNewIntegrationRequestAnyOf1Broker,

    /**
     * The AddNewIntegrationRequestAnyOfCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf1 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf1}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf1,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf10 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf10}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf10,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf11 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf11}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf11,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf12 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf12}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf12,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf13 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf13}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf13,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf14 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf14}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf14,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf15 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf15}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf15,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf16 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf16}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf16,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf17 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf17}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf17,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf2 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf2}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf2,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf3 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf3}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf3,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf4 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf4}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf4,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf5 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf5}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf5,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf6 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf6}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf6,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf7 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf7}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf7,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf8 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf8}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf8,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf9 model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf9}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf9,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials,

    /**
     * The AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials model constructor.
     * @property {module:model/AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials}
     */
    AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials,

    /**
     * The AggregatedProjectIssues model constructor.
     * @property {module:model/AggregatedProjectIssues}
     */
    AggregatedProjectIssues,

    /**
     * The AggregatedProjectIssuesFilters model constructor.
     * @property {module:model/AggregatedProjectIssuesFilters}
     */
    AggregatedProjectIssuesFilters,

    /**
     * The AggregatedProjectIssuesIssuesInner model constructor.
     * @property {module:model/AggregatedProjectIssuesIssuesInner}
     */
    AggregatedProjectIssuesIssuesInner,

    /**
     * The AggregatedProjectIssuesIssuesInnerIssueData model constructor.
     * @property {module:model/AggregatedProjectIssuesIssuesInnerIssueData}
     */
    AggregatedProjectIssuesIssuesInnerIssueData,

    /**
     * The AllIgnores model constructor.
     * @property {module:model/AllIgnores}
     */
    AllIgnores,

    /**
     * The AllJiraIssues model constructor.
     * @property {module:model/AllJiraIssues}
     */
    AllJiraIssues,

    /**
     * The ApplyingAttributes200Response model constructor.
     * @property {module:model/ApplyingAttributes200Response}
     */
    ApplyingAttributes200Response,

    /**
     * The ApplyingAttributes200ResponseAttributes model constructor.
     * @property {module:model/ApplyingAttributes200ResponseAttributes}
     */
    ApplyingAttributes200ResponseAttributes,

    /**
     * The ApplyingAttributesRequest model constructor.
     * @property {module:model/ApplyingAttributesRequest}
     */
    ApplyingAttributesRequest,

    /**
     * The AssignmentType model constructor.
     * @property {module:model/AssignmentType}
     */
    AssignmentType,

    /**
     * The AutoRemediationPrs model constructor.
     * @property {module:model/AutoRemediationPrs}
     */
    AutoRemediationPrs,

    /**
     * The BrokerSettings model constructor.
     * @property {module:model/BrokerSettings}
     */
    BrokerSettings,

    /**
     * The CloneAnIntegrationWithSettingsAndCredentialsRequest model constructor.
     * @property {module:model/CloneAnIntegrationWithSettingsAndCredentialsRequest}
     */
    CloneAnIntegrationWithSettingsAndCredentialsRequest,

    /**
     * The ComposerLock model constructor.
     * @property {module:model/ComposerLock}
     */
    ComposerLock,

    /**
     * The ComposerRequestPayload model constructor.
     * @property {module:model/ComposerRequestPayload}
     */
    ComposerRequestPayload,

    /**
     * The CreateANewOrganization400Response model constructor.
     * @property {module:model/CreateANewOrganization400Response}
     */
    CreateANewOrganization400Response,

    /**
     * The CreateANewOrganizationRequest model constructor.
     * @property {module:model/CreateANewOrganizationRequest}
     */
    CreateANewOrganizationRequest,

    /**
     * The CreateAWebhookRequest model constructor.
     * @property {module:model/CreateAWebhookRequest}
     */
    CreateAWebhookRequest,

    /**
     * The CreateJiraIssue200Response model constructor.
     * @property {module:model/CreateJiraIssue200Response}
     */
    CreateJiraIssue200Response,

    /**
     * The CreateJiraIssue200ResponseJiraIssue model constructor.
     * @property {module:model/CreateJiraIssue200ResponseJiraIssue}
     */
    CreateJiraIssue200ResponseJiraIssue,

    /**
     * The CreateJiraIssueRequest model constructor.
     * @property {module:model/CreateJiraIssueRequest}
     */
    CreateJiraIssueRequest,

    /**
     * The CreateJiraIssueRequestFields model constructor.
     * @property {module:model/CreateJiraIssueRequestFields}
     */
    CreateJiraIssueRequestFields,

    /**
     * The CreateOrganizationsBody model constructor.
     * @property {module:model/CreateOrganizationsBody}
     */
    CreateOrganizationsBody,

    /**
     * The DeletePendingUserProvision200Response model constructor.
     * @property {module:model/DeletePendingUserProvision200Response}
     */
    DeletePendingUserProvision200Response,

    /**
     * The DeleteTagBody model constructor.
     * @property {module:model/DeleteTagBody}
     */
    DeleteTagBody,

    /**
     * The DeleteTagFromGroup200Response model constructor.
     * @property {module:model/DeleteTagFromGroup200Response}
     */
    DeleteTagFromGroup200Response,

    /**
     * The DeleteTagFromGroupRequest model constructor.
     * @property {module:model/DeleteTagFromGroupRequest}
     */
    DeleteTagFromGroupRequest,

    /**
     * The DepGraphData model constructor.
     * @property {module:model/DepGraphData}
     */
    DepGraphData,

    /**
     * The Dependencies model constructor.
     * @property {module:model/Dependencies}
     */
    Dependencies,

    /**
     * The DependenciesFilters model constructor.
     * @property {module:model/DependenciesFilters}
     */
    DependenciesFilters,

    /**
     * The DependenciesFiltersFilters model constructor.
     * @property {module:model/DependenciesFiltersFilters}
     */
    DependenciesFiltersFilters,

    /**
     * The ErrorResponse model constructor.
     * @property {module:model/ErrorResponse}
     */
    ErrorResponse,

    /**
     * The Function model constructor.
     * @property {module:model/Function}
     */
    Function,

    /**
     * The FunctionId model constructor.
     * @property {module:model/FunctionId}
     */
    FunctionId,

    /**
     * The GetExistingIntegrationByType200Response model constructor.
     * @property {module:model/GetExistingIntegrationByType200Response}
     */
    GetExistingIntegrationByType200Response,

    /**
     * The GetGroupLevelAuditLogsRequest model constructor.
     * @property {module:model/GetGroupLevelAuditLogsRequest}
     */
    GetGroupLevelAuditLogsRequest,

    /**
     * The GetGroupLevelAuditLogsRequestFilters model constructor.
     * @property {module:model/GetGroupLevelAuditLogsRequestFilters}
     */
    GetGroupLevelAuditLogsRequestFilters,

    /**
     * The GetImportJobDetails200Response model constructor.
     * @property {module:model/GetImportJobDetails200Response}
     */
    GetImportJobDetails200Response,

    /**
     * The GetIssueCounts200Response model constructor.
     * @property {module:model/GetIssueCounts200Response}
     */
    GetIssueCounts200Response,

    /**
     * The GetIssueCounts200ResponseResultsInner model constructor.
     * @property {module:model/GetIssueCounts200ResponseResultsInner}
     */
    GetIssueCounts200ResponseResultsInner,

    /**
     * The GetIssueCounts200ResponseResultsInnerFixable model constructor.
     * @property {module:model/GetIssueCounts200ResponseResultsInnerFixable}
     */
    GetIssueCounts200ResponseResultsInnerFixable,

    /**
     * The GetIssueCounts200ResponseResultsInnerSeverity model constructor.
     * @property {module:model/GetIssueCounts200ResponseResultsInnerSeverity}
     */
    GetIssueCounts200ResponseResultsInnerSeverity,

    /**
     * The GetIssueCounts400Response model constructor.
     * @property {module:model/GetIssueCounts400Response}
     */
    GetIssueCounts400Response,

    /**
     * The GetIssueCounts400ResponseError model constructor.
     * @property {module:model/GetIssueCounts400ResponseError}
     */
    GetIssueCounts400ResponseError,

    /**
     * The GetIssueCountsRequest model constructor.
     * @property {module:model/GetIssueCountsRequest}
     */
    GetIssueCountsRequest,

    /**
     * The GetIssueCountsRequestFilters model constructor.
     * @property {module:model/GetIssueCountsRequestFilters}
     */
    GetIssueCountsRequestFilters,

    /**
     * The GetIssueCountsRequestFiltersPriorityScore model constructor.
     * @property {module:model/GetIssueCountsRequestFiltersPriorityScore}
     */
    GetIssueCountsRequestFiltersPriorityScore,

    /**
     * The GetListOfIssues200Response model constructor.
     * @property {module:model/GetListOfIssues200Response}
     */
    GetListOfIssues200Response,

    /**
     * The GetListOfIssues200ResponseResultsInner model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInner}
     */
    GetListOfIssues200ResponseResultsInner,

    /**
     * The GetListOfIssues200ResponseResultsInnerIssue model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInnerIssue}
     */
    GetListOfIssues200ResponseResultsInnerIssue,

    /**
     * The GetListOfIssues200ResponseResultsInnerIssueIdentifiers model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInnerIssueIdentifiers}
     */
    GetListOfIssues200ResponseResultsInnerIssueIdentifiers,

    /**
     * The GetListOfIssues200ResponseResultsInnerIssueSemver model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInnerIssueSemver}
     */
    GetListOfIssues200ResponseResultsInnerIssueSemver,

    /**
     * The GetListOfIssues200ResponseResultsInnerOneOf model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInnerOneOf}
     */
    GetListOfIssues200ResponseResultsInnerOneOf,

    /**
     * The GetListOfIssues200ResponseResultsInnerOneOf1 model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInnerOneOf1}
     */
    GetListOfIssues200ResponseResultsInnerOneOf1,

    /**
     * The GetListOfIssues200ResponseResultsInnerOneOf1Project model constructor.
     * @property {module:model/GetListOfIssues200ResponseResultsInnerOneOf1Project}
     */
    GetListOfIssues200ResponseResultsInnerOneOf1Project,

    /**
     * The GetListOfIssuesRequest model constructor.
     * @property {module:model/GetListOfIssuesRequest}
     */
    GetListOfIssuesRequest,

    /**
     * The GetListOfIssuesRequestFilters model constructor.
     * @property {module:model/GetListOfIssuesRequestFilters}
     */
    GetListOfIssuesRequestFilters,

    /**
     * The GetMyDetails200Response model constructor.
     * @property {module:model/GetMyDetails200Response}
     */
    GetMyDetails200Response,

    /**
     * The GetOrganizationLevelAuditLogsRequest model constructor.
     * @property {module:model/GetOrganizationLevelAuditLogsRequest}
     */
    GetOrganizationLevelAuditLogsRequest,

    /**
     * The GetOrganizationLevelAuditLogsRequestFilters model constructor.
     * @property {module:model/GetOrganizationLevelAuditLogsRequestFilters}
     */
    GetOrganizationLevelAuditLogsRequestFilters,

    /**
     * The GetProjectCounts200Response model constructor.
     * @property {module:model/GetProjectCounts200Response}
     */
    GetProjectCounts200Response,

    /**
     * The GetProjectCounts200ResponseResultsInner model constructor.
     * @property {module:model/GetProjectCounts200ResponseResultsInner}
     */
    GetProjectCounts200ResponseResultsInner,

    /**
     * The GetProjectCountsRequest model constructor.
     * @property {module:model/GetProjectCountsRequest}
     */
    GetProjectCountsRequest,

    /**
     * The GetProjectCountsRequestFilters model constructor.
     * @property {module:model/GetProjectCountsRequestFilters}
     */
    GetProjectCountsRequestFilters,

    /**
     * The GetProjectDependencyGraph200Response model constructor.
     * @property {module:model/GetProjectDependencyGraph200Response}
     */
    GetProjectDependencyGraph200Response,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraph model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraph}
     */
    GetProjectDependencyGraph200ResponseDepGraph,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphGraph model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphGraph}
     */
    GetProjectDependencyGraph200ResponseDepGraphGraph,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner}
     */
    GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner}
     */
    GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphPkgManager model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphPkgManager}
     */
    GetProjectDependencyGraph200ResponseDepGraphPkgManager,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner}
     */
    GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphPkgsInner model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphPkgsInner}
     */
    GetProjectDependencyGraph200ResponseDepGraphPkgsInner,

    /**
     * The GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo model constructor.
     * @property {module:model/GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo}
     */
    GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo,

    /**
     * The GetTestCounts200Response model constructor.
     * @property {module:model/GetTestCounts200Response}
     */
    GetTestCounts200Response,

    /**
     * The GetTestCounts200ResponseResultsInner model constructor.
     * @property {module:model/GetTestCounts200ResponseResultsInner}
     */
    GetTestCounts200ResponseResultsInner,

    /**
     * The GetTestCounts200ResponseResultsInnerIsPrivate model constructor.
     * @property {module:model/GetTestCounts200ResponseResultsInnerIsPrivate}
     */
    GetTestCounts200ResponseResultsInnerIsPrivate,

    /**
     * The GetTestCounts200ResponseResultsInnerIssuesPrevented model constructor.
     * @property {module:model/GetTestCounts200ResponseResultsInnerIssuesPrevented}
     */
    GetTestCounts200ResponseResultsInnerIssuesPrevented,

    /**
     * The GetTestCountsRequest model constructor.
     * @property {module:model/GetTestCountsRequest}
     */
    GetTestCountsRequest,

    /**
     * The GetTestCountsRequestFilters model constructor.
     * @property {module:model/GetTestCountsRequestFilters}
     */
    GetTestCountsRequestFilters,

    /**
     * The GetUserDetails200Response model constructor.
     * @property {module:model/GetUserDetails200Response}
     */
    GetUserDetails200Response,

    /**
     * The GoPkgLock model constructor.
     * @property {module:model/GoPkgLock}
     */
    GoPkgLock,

    /**
     * The GolangdepRequestPayload model constructor.
     * @property {module:model/GolangdepRequestPayload}
     */
    GolangdepRequestPayload,

    /**
     * The GovendorRequestPayload model constructor.
     * @property {module:model/GovendorRequestPayload}
     */
    GovendorRequestPayload,

    /**
     * The GradleFile model constructor.
     * @property {module:model/GradleFile}
     */
    GradleFile,

    /**
     * The GradleRequestPayload model constructor.
     * @property {module:model/GradleRequestPayload}
     */
    GradleRequestPayload,

    /**
     * The GradleRequestPayloadFiles model constructor.
     * @property {module:model/GradleRequestPayloadFiles}
     */
    GradleRequestPayloadFiles,

    /**
     * The Graph model constructor.
     * @property {module:model/Graph}
     */
    Graph,

    /**
     * The GraphDependency model constructor.
     * @property {module:model/GraphDependency}
     */
    GraphDependency,

    /**
     * The GraphRequestPayload model constructor.
     * @property {module:model/GraphRequestPayload}
     */
    GraphRequestPayload,

    /**
     * The GroupSettings model constructor.
     * @property {module:model/GroupSettings}
     */
    GroupSettings,

    /**
     * The GroupsAuditLogsFilters model constructor.
     * @property {module:model/GroupsAuditLogsFilters}
     */
    GroupsAuditLogsFilters,

    /**
     * The Ignore model constructor.
     * @property {module:model/Ignore}
     */
    Ignore,

    /**
     * The IgnoreIgnorePath model constructor.
     * @property {module:model/IgnoreIgnorePath}
     */
    IgnoreIgnorePath,

    /**
     * The IgnoreIgnorePathIgnoredBy model constructor.
     * @property {module:model/IgnoreIgnorePathIgnoredBy}
     */
    IgnoreIgnorePathIgnoredBy,

    /**
     * The IgnoreRule model constructor.
     * @property {module:model/IgnoreRule}
     */
    IgnoreRule,

    /**
     * The ImportTargetsRequest model constructor.
     * @property {module:model/ImportTargetsRequest}
     */
    ImportTargetsRequest,

    /**
     * The ImportTargetsRequestAnyOf model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf}
     */
    ImportTargetsRequestAnyOf,

    /**
     * The ImportTargetsRequestAnyOf1 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf1}
     */
    ImportTargetsRequestAnyOf1,

    /**
     * The ImportTargetsRequestAnyOf1Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf1Target}
     */
    ImportTargetsRequestAnyOf1Target,

    /**
     * The ImportTargetsRequestAnyOf2 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf2}
     */
    ImportTargetsRequestAnyOf2,

    /**
     * The ImportTargetsRequestAnyOf2Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf2Target}
     */
    ImportTargetsRequestAnyOf2Target,

    /**
     * The ImportTargetsRequestAnyOf3 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf3}
     */
    ImportTargetsRequestAnyOf3,

    /**
     * The ImportTargetsRequestAnyOf3Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf3Target}
     */
    ImportTargetsRequestAnyOf3Target,

    /**
     * The ImportTargetsRequestAnyOf4 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf4}
     */
    ImportTargetsRequestAnyOf4,

    /**
     * The ImportTargetsRequestAnyOf4Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf4Target}
     */
    ImportTargetsRequestAnyOf4Target,

    /**
     * The ImportTargetsRequestAnyOf5 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf5}
     */
    ImportTargetsRequestAnyOf5,

    /**
     * The ImportTargetsRequestAnyOf5Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf5Target}
     */
    ImportTargetsRequestAnyOf5Target,

    /**
     * The ImportTargetsRequestAnyOf6 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf6}
     */
    ImportTargetsRequestAnyOf6,

    /**
     * The ImportTargetsRequestAnyOf6Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf6Target}
     */
    ImportTargetsRequestAnyOf6Target,

    /**
     * The ImportTargetsRequestAnyOf7 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf7}
     */
    ImportTargetsRequestAnyOf7,

    /**
     * The ImportTargetsRequestAnyOf7Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf7Target}
     */
    ImportTargetsRequestAnyOf7Target,

    /**
     * The ImportTargetsRequestAnyOf8 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf8}
     */
    ImportTargetsRequestAnyOf8,

    /**
     * The ImportTargetsRequestAnyOf8Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf8Target}
     */
    ImportTargetsRequestAnyOf8Target,

    /**
     * The ImportTargetsRequestAnyOf9 model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf9}
     */
    ImportTargetsRequestAnyOf9,

    /**
     * The ImportTargetsRequestAnyOf9Target model constructor.
     * @property {module:model/ImportTargetsRequestAnyOf9Target}
     */
    ImportTargetsRequestAnyOf9Target,

    /**
     * The ImportTargetsRequestAnyOfTarget model constructor.
     * @property {module:model/ImportTargetsRequestAnyOfTarget}
     */
    ImportTargetsRequestAnyOfTarget,

    /**
     * The IntegrationSettings model constructor.
     * @property {module:model/IntegrationSettings}
     */
    IntegrationSettings,

    /**
     * The IntegrationType model constructor.
     * @property {module:model/IntegrationType}
     */
    IntegrationType,

    /**
     * The Integrations model constructor.
     * @property {module:model/Integrations}
     */
    Integrations,

    /**
     * The InviteUsersRequest model constructor.
     * @property {module:model/InviteUsersRequest}
     */
    InviteUsersRequest,

    /**
     * The IssueCounts model constructor.
     * @property {module:model/IssueCounts}
     */
    IssueCounts,

    /**
     * The IssueCountsFilters model constructor.
     * @property {module:model/IssueCountsFilters}
     */
    IssueCountsFilters,

    /**
     * The IssueCountsFiltersFilters model constructor.
     * @property {module:model/IssueCountsFiltersFilters}
     */
    IssueCountsFiltersFilters,

    /**
     * The IssuePaths model constructor.
     * @property {module:model/IssuePaths}
     */
    IssuePaths,

    /**
     * The Issues model constructor.
     * @property {module:model/Issues}
     */
    Issues,

    /**
     * The IssuesFilters model constructor.
     * @property {module:model/IssuesFilters}
     */
    IssuesFilters,

    /**
     * The IssuesFiltersFilters model constructor.
     * @property {module:model/IssuesFiltersFilters}
     */
    IssuesFiltersFilters,

    /**
     * The IssuesResultsInner model constructor.
     * @property {module:model/IssuesResultsInner}
     */
    IssuesResultsInner,

    /**
     * The JiraIssue model constructor.
     * @property {module:model/JiraIssue}
     */
    JiraIssue,

    /**
     * The JiraIssueRequest model constructor.
     * @property {module:model/JiraIssueRequest}
     */
    JiraIssueRequest,

    /**
     * The Licenses model constructor.
     * @property {module:model/Licenses}
     */
    Licenses,

    /**
     * The LicensesFilters model constructor.
     * @property {module:model/LicensesFilters}
     */
    LicensesFilters,

    /**
     * The LicensesFiltersFilters model constructor.
     * @property {module:model/LicensesFiltersFilters}
     */
    LicensesFiltersFilters,

    /**
     * The ListAllAggregatedIssues200Response model constructor.
     * @property {module:model/ListAllAggregatedIssues200Response}
     */
    ListAllAggregatedIssues200Response,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInner model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInner}
     */
    ListAllAggregatedIssues200ResponseIssuesInner,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInnerFixInfo model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInnerFixInfo}
     */
    ListAllAggregatedIssues200ResponseIssuesInnerFixInfo,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInnerIssueData model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueData}
     */
    ListAllAggregatedIssues200ResponseIssuesInnerIssueData,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers}
     */
    ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver}
     */
    ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInnerLinks model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInnerLinks}
     */
    ListAllAggregatedIssues200ResponseIssuesInnerLinks,

    /**
     * The ListAllAggregatedIssues200ResponseIssuesInnerPriority model constructor.
     * @property {module:model/ListAllAggregatedIssues200ResponseIssuesInnerPriority}
     */
    ListAllAggregatedIssues200ResponseIssuesInnerPriority,

    /**
     * The ListAllAggregatedIssuesRequest model constructor.
     * @property {module:model/ListAllAggregatedIssuesRequest}
     */
    ListAllAggregatedIssuesRequest,

    /**
     * The ListAllAggregatedIssuesRequestFilters model constructor.
     * @property {module:model/ListAllAggregatedIssuesRequestFilters}
     */
    ListAllAggregatedIssuesRequestFilters,

    /**
     * The ListAllAggregatedIssuesRequestFiltersPriority model constructor.
     * @property {module:model/ListAllAggregatedIssuesRequestFiltersPriority}
     */
    ListAllAggregatedIssuesRequestFiltersPriority,

    /**
     * The ListAllAggregatedIssuesRequestFiltersPriorityScore model constructor.
     * @property {module:model/ListAllAggregatedIssuesRequestFiltersPriorityScore}
     */
    ListAllAggregatedIssuesRequestFiltersPriorityScore,

    /**
     * The ListAllDependencies200Response model constructor.
     * @property {module:model/ListAllDependencies200Response}
     */
    ListAllDependencies200Response,

    /**
     * The ListAllDependencies200ResponseResultsInner model constructor.
     * @property {module:model/ListAllDependencies200ResponseResultsInner}
     */
    ListAllDependencies200ResponseResultsInner,

    /**
     * The ListAllDependencies200ResponseResultsInnerLicensesInner model constructor.
     * @property {module:model/ListAllDependencies200ResponseResultsInnerLicensesInner}
     */
    ListAllDependencies200ResponseResultsInnerLicensesInner,

    /**
     * The ListAllDependencies200ResponseResultsInnerProjectsInner model constructor.
     * @property {module:model/ListAllDependencies200ResponseResultsInnerProjectsInner}
     */
    ListAllDependencies200ResponseResultsInnerProjectsInner,

    /**
     * The ListAllDependenciesRequest model constructor.
     * @property {module:model/ListAllDependenciesRequest}
     */
    ListAllDependenciesRequest,

    /**
     * The ListAllDependenciesRequestFilters model constructor.
     * @property {module:model/ListAllDependenciesRequestFilters}
     */
    ListAllDependenciesRequestFilters,

    /**
     * The ListAllLicenses200Response model constructor.
     * @property {module:model/ListAllLicenses200Response}
     */
    ListAllLicenses200Response,

    /**
     * The ListAllLicenses200ResponseResultsInner model constructor.
     * @property {module:model/ListAllLicenses200ResponseResultsInner}
     */
    ListAllLicenses200ResponseResultsInner,

    /**
     * The ListAllLicenses200ResponseResultsInnerDependenciesInner model constructor.
     * @property {module:model/ListAllLicenses200ResponseResultsInnerDependenciesInner}
     */
    ListAllLicenses200ResponseResultsInnerDependenciesInner,

    /**
     * The ListAllLicensesRequest model constructor.
     * @property {module:model/ListAllLicensesRequest}
     */
    ListAllLicensesRequest,

    /**
     * The ListAllLicensesRequestFilters model constructor.
     * @property {module:model/ListAllLicensesRequestFilters}
     */
    ListAllLicensesRequestFilters,

    /**
     * The ListAllProjectSnapshotIssuePaths200Response model constructor.
     * @property {module:model/ListAllProjectSnapshotIssuePaths200Response}
     */
    ListAllProjectSnapshotIssuePaths200Response,

    /**
     * The ListAllProjectSnapshotIssuePaths200ResponseLinks model constructor.
     * @property {module:model/ListAllProjectSnapshotIssuePaths200ResponseLinks}
     */
    ListAllProjectSnapshotIssuePaths200ResponseLinks,

    /**
     * The ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner model constructor.
     * @property {module:model/ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner}
     */
    ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner,

    /**
     * The ListAllProjectSnapshots200Response model constructor.
     * @property {module:model/ListAllProjectSnapshots200Response}
     */
    ListAllProjectSnapshots200Response,

    /**
     * The ListAllProjectSnapshots200ResponseSnapshotsInner model constructor.
     * @property {module:model/ListAllProjectSnapshots200ResponseSnapshotsInner}
     */
    ListAllProjectSnapshots200ResponseSnapshotsInner,

    /**
     * The ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts model constructor.
     * @property {module:model/ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts}
     */
    ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts,

    /**
     * The ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense model constructor.
     * @property {module:model/ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense}
     */
    ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense,

    /**
     * The ListAllProjectSnapshotsRequest model constructor.
     * @property {module:model/ListAllProjectSnapshotsRequest}
     */
    ListAllProjectSnapshotsRequest,

    /**
     * The ListAllProjectSnapshotsRequestFilters model constructor.
     * @property {module:model/ListAllProjectSnapshotsRequestFilters}
     */
    ListAllProjectSnapshotsRequestFilters,

    /**
     * The ListAllProjects model constructor.
     * @property {module:model/ListAllProjects}
     */
    ListAllProjects,

    /**
     * The ListAllProjects200Response model constructor.
     * @property {module:model/ListAllProjects200Response}
     */
    ListAllProjects200Response,

    /**
     * The ListAllProjects200ResponseOrg model constructor.
     * @property {module:model/ListAllProjects200ResponseOrg}
     */
    ListAllProjects200ResponseOrg,

    /**
     * The ListAllProjects200ResponseProjectsInner model constructor.
     * @property {module:model/ListAllProjects200ResponseProjectsInner}
     */
    ListAllProjects200ResponseProjectsInner,

    /**
     * The ListAllProjectsRequest model constructor.
     * @property {module:model/ListAllProjectsRequest}
     */
    ListAllProjectsRequest,

    /**
     * The ListAllProjectsRequestFilters model constructor.
     * @property {module:model/ListAllProjectsRequestFilters}
     */
    ListAllProjectsRequestFilters,

    /**
     * The ListAllProjectsRequestFiltersAttributes model constructor.
     * @property {module:model/ListAllProjectsRequestFiltersAttributes}
     */
    ListAllProjectsRequestFiltersAttributes,

    /**
     * The ListAllProjectsRequestFiltersTags model constructor.
     * @property {module:model/ListAllProjectsRequestFiltersTags}
     */
    ListAllProjectsRequestFiltersTags,

    /**
     * The ListAllTagsInAGroup200Response model constructor.
     * @property {module:model/ListAllTagsInAGroup200Response}
     */
    ListAllTagsInAGroup200Response,

    /**
     * The ListProjectSettings200Response model constructor.
     * @property {module:model/ListProjectSettings200Response}
     */
    ListProjectSettings200Response,

    /**
     * The ListProjectSettings200ResponseAutoRemediationPrs model constructor.
     * @property {module:model/ListProjectSettings200ResponseAutoRemediationPrs}
     */
    ListProjectSettings200ResponseAutoRemediationPrs,

    /**
     * The MavenAdditionalFile model constructor.
     * @property {module:model/MavenAdditionalFile}
     */
    MavenAdditionalFile,

    /**
     * The MavenFile model constructor.
     * @property {module:model/MavenFile}
     */
    MavenFile,

    /**
     * The MavenRequestPayload model constructor.
     * @property {module:model/MavenRequestPayload}
     */
    MavenRequestPayload,

    /**
     * The MavenRequestPayloadFiles model constructor.
     * @property {module:model/MavenRequestPayloadFiles}
     */
    MavenRequestPayloadFiles,

    /**
     * The ModifyProjectNotificationSettingsRequest model constructor.
     * @property {module:model/ModifyProjectNotificationSettingsRequest}
     */
    ModifyProjectNotificationSettingsRequest,

    /**
     * The MonitorDepGraphData model constructor.
     * @property {module:model/MonitorDepGraphData}
     */
    MonitorDepGraphData,

    /**
     * The MonitorDepGraphRequest model constructor.
     * @property {module:model/MonitorDepGraphRequest}
     */
    MonitorDepGraphRequest,

    /**
     * The MonitorDepGraphRequestDepGraph model constructor.
     * @property {module:model/MonitorDepGraphRequestDepGraph}
     */
    MonitorDepGraphRequestDepGraph,

    /**
     * The MonitorDepGraphRequestDepGraphGraph model constructor.
     * @property {module:model/MonitorDepGraphRequestDepGraphGraph}
     */
    MonitorDepGraphRequestDepGraphGraph,

    /**
     * The MonitorDepGraphRequestDepGraphPkgManager model constructor.
     * @property {module:model/MonitorDepGraphRequestDepGraphPkgManager}
     */
    MonitorDepGraphRequestDepGraphPkgManager,

    /**
     * The MonitorDepGraphRequestMeta model constructor.
     * @property {module:model/MonitorDepGraphRequestMeta}
     */
    MonitorDepGraphRequestMeta,

    /**
     * The MonitorGraph model constructor.
     * @property {module:model/MonitorGraph}
     */
    MonitorGraph,

    /**
     * The MonitorGraphDependency model constructor.
     * @property {module:model/MonitorGraphDependency}
     */
    MonitorGraphDependency,

    /**
     * The MonitorGraphPayload model constructor.
     * @property {module:model/MonitorGraphPayload}
     */
    MonitorGraphPayload,

    /**
     * The MonitorMetaData model constructor.
     * @property {module:model/MonitorMetaData}
     */
    MonitorMetaData,

    /**
     * The MonitorNode model constructor.
     * @property {module:model/MonitorNode}
     */
    MonitorNode,

    /**
     * The MonitorPackage model constructor.
     * @property {module:model/MonitorPackage}
     */
    MonitorPackage,

    /**
     * The MonitorPackageInfo model constructor.
     * @property {module:model/MonitorPackageInfo}
     */
    MonitorPackageInfo,

    /**
     * The MonitorPkgManager model constructor.
     * @property {module:model/MonitorPkgManager}
     */
    MonitorPkgManager,

    /**
     * The MonitorRepository model constructor.
     * @property {module:model/MonitorRepository}
     */
    MonitorRepository,

    /**
     * The MoveProjectToADifferentOrganizationRequest model constructor.
     * @property {module:model/MoveProjectToADifferentOrganizationRequest}
     */
    MoveProjectToADifferentOrganizationRequest,

    /**
     * The NewIssuesNotificationSettingRequest model constructor.
     * @property {module:model/NewIssuesNotificationSettingRequest}
     */
    NewIssuesNotificationSettingRequest,

    /**
     * The Node model constructor.
     * @property {module:model/Node}
     */
    Node,

    /**
     * The NotificationSettingResponse model constructor.
     * @property {module:model/NotificationSettingResponse}
     */
    NotificationSettingResponse,

    /**
     * The NotificationSettingsRequest model constructor.
     * @property {module:model/NotificationSettingsRequest}
     */
    NotificationSettingsRequest,

    /**
     * The NotificationSettingsResponse model constructor.
     * @property {module:model/NotificationSettingsResponse}
     */
    NotificationSettingsResponse,

    /**
     * The NpmRequestPayload model constructor.
     * @property {module:model/NpmRequestPayload}
     */
    NpmRequestPayload,

    /**
     * The OrgAuditLogsFilters model constructor.
     * @property {module:model/OrgAuditLogsFilters}
     */
    OrgAuditLogsFilters,

    /**
     * The OrgOrgIdNotificationSettingsGet200Response model constructor.
     * @property {module:model/OrgOrgIdNotificationSettingsGet200Response}
     */
    OrgOrgIdNotificationSettingsGet200Response,

    /**
     * The OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations model constructor.
     * @property {module:model/OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations}
     */
    OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations,

    /**
     * The OrgOrgIdNotificationSettingsGet200ResponseProjectImported model constructor.
     * @property {module:model/OrgOrgIdNotificationSettingsGet200ResponseProjectImported}
     */
    OrgOrgIdNotificationSettingsGet200ResponseProjectImported,

    /**
     * The OrgSettingsRequest model constructor.
     * @property {module:model/OrgSettingsRequest}
     */
    OrgSettingsRequest,

    /**
     * The OrgSettingsResponse model constructor.
     * @property {module:model/OrgSettingsResponse}
     */
    OrgSettingsResponse,

    /**
     * The Package model constructor.
     * @property {module:model/Package}
     */
    Package,

    /**
     * The PackageInfo model constructor.
     * @property {module:model/PackageInfo}
     */
    PackageInfo,

    /**
     * The PackageLockJsonFile model constructor.
     * @property {module:model/PackageLockJsonFile}
     */
    PackageLockJsonFile,

    /**
     * The Patch model constructor.
     * @property {module:model/Patch}
     */
    Patch,

    /**
     * The PipRequestPayload model constructor.
     * @property {module:model/PipRequestPayload}
     */
    PipRequestPayload,

    /**
     * The PkgManager model constructor.
     * @property {module:model/PkgManager}
     */
    PkgManager,

    /**
     * The PriorityScore model constructor.
     * @property {module:model/PriorityScore}
     */
    PriorityScore,

    /**
     * The Project model constructor.
     * @property {module:model/Project}
     */
    Project,

    /**
     * The ProjectAttributes model constructor.
     * @property {module:model/ProjectAttributes}
     */
    ProjectAttributes,

    /**
     * The ProjectCounts model constructor.
     * @property {module:model/ProjectCounts}
     */
    ProjectCounts,

    /**
     * The ProjectCountsFilters model constructor.
     * @property {module:model/ProjectCountsFilters}
     */
    ProjectCountsFilters,

    /**
     * The ProjectCountsFiltersFilters model constructor.
     * @property {module:model/ProjectCountsFiltersFilters}
     */
    ProjectCountsFiltersFilters,

    /**
     * The ProjectDependencyGraph model constructor.
     * @property {module:model/ProjectDependencyGraph}
     */
    ProjectDependencyGraph,

    /**
     * The ProjectIssuesFilters model constructor.
     * @property {module:model/ProjectIssuesFilters}
     */
    ProjectIssuesFilters,

    /**
     * The ProjectIssuesFiltersFilters model constructor.
     * @property {module:model/ProjectIssuesFiltersFilters}
     */
    ProjectIssuesFiltersFilters,

    /**
     * The ProjectIssuesFiltersFiltersPriorityScore model constructor.
     * @property {module:model/ProjectIssuesFiltersFiltersPriorityScore}
     */
    ProjectIssuesFiltersFiltersPriorityScore,

    /**
     * The ProjectMove model constructor.
     * @property {module:model/ProjectMove}
     */
    ProjectMove,

    /**
     * The ProjectSettings model constructor.
     * @property {module:model/ProjectSettings}
     */
    ProjectSettings,

    /**
     * The ProjectSnapshots model constructor.
     * @property {module:model/ProjectSnapshots}
     */
    ProjectSnapshots,

    /**
     * The ProjectSnapshotsFilters model constructor.
     * @property {module:model/ProjectSnapshotsFilters}
     */
    ProjectSnapshotsFilters,

    /**
     * The ProjectWithoutRemediation model constructor.
     * @property {module:model/ProjectWithoutRemediation}
     */
    ProjectWithoutRemediation,

    /**
     * The ProjectsFilters model constructor.
     * @property {module:model/ProjectsFilters}
     */
    ProjectsFilters,

    /**
     * The ProjectsFiltersFilters model constructor.
     * @property {module:model/ProjectsFiltersFilters}
     */
    ProjectsFiltersFilters,

    /**
     * The ProvisionAUserToTheOrganization200Response model constructor.
     * @property {module:model/ProvisionAUserToTheOrganization200Response}
     */
    ProvisionAUserToTheOrganization200Response,

    /**
     * The ProvisionAUserToTheOrganizationRequest model constructor.
     * @property {module:model/ProvisionAUserToTheOrganizationRequest}
     */
    ProvisionAUserToTheOrganizationRequest,

    /**
     * The PullRequestAssignment model constructor.
     * @property {module:model/PullRequestAssignment}
     */
    PullRequestAssignment,

    /**
     * The Repository model constructor.
     * @property {module:model/Repository}
     */
    Repository,

    /**
     * The Retrieve200Response model constructor.
     * @property {module:model/Retrieve200Response}
     */
    Retrieve200Response,

    /**
     * The Retrieve200ResponseAutoRemediationPrs model constructor.
     * @property {module:model/Retrieve200ResponseAutoRemediationPrs}
     */
    Retrieve200ResponseAutoRemediationPrs,

    /**
     * The Retrieve200ResponseManualRemediationPrs model constructor.
     * @property {module:model/Retrieve200ResponseManualRemediationPrs}
     */
    Retrieve200ResponseManualRemediationPrs,

    /**
     * The Retrieve200ResponsePullRequestAssignment model constructor.
     * @property {module:model/Retrieve200ResponsePullRequestAssignment}
     */
    Retrieve200ResponsePullRequestAssignment,

    /**
     * The RetrieveASingleProject200Response model constructor.
     * @property {module:model/RetrieveASingleProject200Response}
     */
    RetrieveASingleProject200Response,

    /**
     * The RetrieveASingleProject200ResponseAttributes model constructor.
     * @property {module:model/RetrieveASingleProject200ResponseAttributes}
     */
    RetrieveASingleProject200ResponseAttributes,

    /**
     * The RetrieveASingleProject200ResponseImportingUser model constructor.
     * @property {module:model/RetrieveASingleProject200ResponseImportingUser}
     */
    RetrieveASingleProject200ResponseImportingUser,

    /**
     * The RetrieveASingleProject200ResponseIssueCountsBySeverity model constructor.
     * @property {module:model/RetrieveASingleProject200ResponseIssueCountsBySeverity}
     */
    RetrieveASingleProject200ResponseIssueCountsBySeverity,

    /**
     * The RetrieveASingleProject200ResponseRemediation model constructor.
     * @property {module:model/RetrieveASingleProject200ResponseRemediation}
     */
    RetrieveASingleProject200ResponseRemediation,

    /**
     * The RubygemsRequestPayload model constructor.
     * @property {module:model/RubygemsRequestPayload}
     */
    RubygemsRequestPayload,

    /**
     * The SBTFile model constructor.
     * @property {module:model/SBTFile}
     */
    SBTFile,

    /**
     * The SbtRequestPayload model constructor.
     * @property {module:model/SbtRequestPayload}
     */
    SbtRequestPayload,

    /**
     * The SbtRequestPayloadFiles model constructor.
     * @property {module:model/SbtRequestPayloadFiles}
     */
    SbtRequestPayloadFiles,

    /**
     * The SemverObject model constructor.
     * @property {module:model/SemverObject}
     */
    SemverObject,

    /**
     * The SetNotificationSettingsRequest model constructor.
     * @property {module:model/SetNotificationSettingsRequest}
     */
    SetNotificationSettingsRequest,

    /**
     * The SetNotificationSettingsRequestNewIssuesRemediations model constructor.
     * @property {module:model/SetNotificationSettingsRequestNewIssuesRemediations}
     */
    SetNotificationSettingsRequestNewIssuesRemediations,

    /**
     * The SetNotificationSettingsRequestProjectImported model constructor.
     * @property {module:model/SetNotificationSettingsRequestProjectImported}
     */
    SetNotificationSettingsRequestProjectImported,

    /**
     * The SimpleNotificationSettingRequest model constructor.
     * @property {module:model/SimpleNotificationSettingRequest}
     */
    SimpleNotificationSettingRequest,

    /**
     * The SimpleNotificationSettingResponse model constructor.
     * @property {module:model/SimpleNotificationSettingResponse}
     */
    SimpleNotificationSettingResponse,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TagBody model constructor.
     * @property {module:model/TagBody}
     */
    TagBody,

    /**
     * The TestComposerJsonComposerLockFileRequest model constructor.
     * @property {module:model/TestComposerJsonComposerLockFileRequest}
     */
    TestComposerJsonComposerLockFileRequest,

    /**
     * The TestComposerJsonComposerLockFileRequestFiles model constructor.
     * @property {module:model/TestComposerJsonComposerLockFileRequestFiles}
     */
    TestComposerJsonComposerLockFileRequestFiles,

    /**
     * The TestComposerJsonComposerLockFileRequestFilesTarget model constructor.
     * @property {module:model/TestComposerJsonComposerLockFileRequestFilesTarget}
     */
    TestComposerJsonComposerLockFileRequestFilesTarget,

    /**
     * The TestDepGraphRequest model constructor.
     * @property {module:model/TestDepGraphRequest}
     */
    TestDepGraphRequest,

    /**
     * The TestDepGraphRequestDepGraph model constructor.
     * @property {module:model/TestDepGraphRequestDepGraph}
     */
    TestDepGraphRequestDepGraph,

    /**
     * The TestDepGraphRequestDepGraphGraph model constructor.
     * @property {module:model/TestDepGraphRequestDepGraphGraph}
     */
    TestDepGraphRequestDepGraphGraph,

    /**
     * The TestGemfileLockFileRequest model constructor.
     * @property {module:model/TestGemfileLockFileRequest}
     */
    TestGemfileLockFileRequest,

    /**
     * The TestGemfileLockFileRequestFiles model constructor.
     * @property {module:model/TestGemfileLockFileRequestFiles}
     */
    TestGemfileLockFileRequestFiles,

    /**
     * The TestGemfileLockFileRequestFilesTarget model constructor.
     * @property {module:model/TestGemfileLockFileRequestFilesTarget}
     */
    TestGemfileLockFileRequestFilesTarget,

    /**
     * The TestGopkgTomlGopkgLockFileRequest model constructor.
     * @property {module:model/TestGopkgTomlGopkgLockFileRequest}
     */
    TestGopkgTomlGopkgLockFileRequest,

    /**
     * The TestGopkgTomlGopkgLockFileRequestFiles model constructor.
     * @property {module:model/TestGopkgTomlGopkgLockFileRequestFiles}
     */
    TestGopkgTomlGopkgLockFileRequestFiles,

    /**
     * The TestGopkgTomlGopkgLockFileRequestFilesTarget model constructor.
     * @property {module:model/TestGopkgTomlGopkgLockFileRequestFilesTarget}
     */
    TestGopkgTomlGopkgLockFileRequestFilesTarget,

    /**
     * The TestGradleFileRequest model constructor.
     * @property {module:model/TestGradleFileRequest}
     */
    TestGradleFileRequest,

    /**
     * The TestGradleFileRequestFiles model constructor.
     * @property {module:model/TestGradleFileRequestFiles}
     */
    TestGradleFileRequestFiles,

    /**
     * The TestGradleFileRequestFilesTarget model constructor.
     * @property {module:model/TestGradleFileRequestFilesTarget}
     */
    TestGradleFileRequestFilesTarget,

    /**
     * The TestMavenFileRequest model constructor.
     * @property {module:model/TestMavenFileRequest}
     */
    TestMavenFileRequest,

    /**
     * The TestMavenFileRequestFiles model constructor.
     * @property {module:model/TestMavenFileRequestFiles}
     */
    TestMavenFileRequestFiles,

    /**
     * The TestMavenFileRequestFilesTarget model constructor.
     * @property {module:model/TestMavenFileRequestFilesTarget}
     */
    TestMavenFileRequestFilesTarget,

    /**
     * The TestPackageJsonPackageLockJsonFileRequest model constructor.
     * @property {module:model/TestPackageJsonPackageLockJsonFileRequest}
     */
    TestPackageJsonPackageLockJsonFileRequest,

    /**
     * The TestPackageJsonPackageLockJsonFileRequestFiles model constructor.
     * @property {module:model/TestPackageJsonPackageLockJsonFileRequestFiles}
     */
    TestPackageJsonPackageLockJsonFileRequestFiles,

    /**
     * The TestPackageJsonPackageLockJsonFileRequestFilesTarget model constructor.
     * @property {module:model/TestPackageJsonPackageLockJsonFileRequestFilesTarget}
     */
    TestPackageJsonPackageLockJsonFileRequestFilesTarget,

    /**
     * The TestPackageJsonYarnLockFileRequest model constructor.
     * @property {module:model/TestPackageJsonYarnLockFileRequest}
     */
    TestPackageJsonYarnLockFileRequest,

    /**
     * The TestRequirementsTxtFileRequest model constructor.
     * @property {module:model/TestRequirementsTxtFileRequest}
     */
    TestRequirementsTxtFileRequest,

    /**
     * The TestRequirementsTxtFileRequestFiles model constructor.
     * @property {module:model/TestRequirementsTxtFileRequestFiles}
     */
    TestRequirementsTxtFileRequestFiles,

    /**
     * The TestRequirementsTxtFileRequestFilesTarget model constructor.
     * @property {module:model/TestRequirementsTxtFileRequestFilesTarget}
     */
    TestRequirementsTxtFileRequestFilesTarget,

    /**
     * The TestSbtFileRequest model constructor.
     * @property {module:model/TestSbtFileRequest}
     */
    TestSbtFileRequest,

    /**
     * The TestVendorJsonFileRequest model constructor.
     * @property {module:model/TestVendorJsonFileRequest}
     */
    TestVendorJsonFileRequest,

    /**
     * The TestVendorJsonFileRequestFiles model constructor.
     * @property {module:model/TestVendorJsonFileRequestFiles}
     */
    TestVendorJsonFileRequestFiles,

    /**
     * The TestVendorJsonFileRequestFilesTarget model constructor.
     * @property {module:model/TestVendorJsonFileRequestFilesTarget}
     */
    TestVendorJsonFileRequestFilesTarget,

    /**
     * The TestsFilters model constructor.
     * @property {module:model/TestsFilters}
     */
    TestsFilters,

    /**
     * The TestsFiltersFilters model constructor.
     * @property {module:model/TestsFiltersFilters}
     */
    TestsFiltersFilters,

    /**
     * The UpdateAMemberInTheOrganizationRequest model constructor.
     * @property {module:model/UpdateAMemberInTheOrganizationRequest}
     */
    UpdateAMemberInTheOrganizationRequest,

    /**
     * The UpdateAMemberSRoleInTheOrganizationRequest model constructor.
     * @property {module:model/UpdateAMemberSRoleInTheOrganizationRequest}
     */
    UpdateAMemberSRoleInTheOrganizationRequest,

    /**
     * The UpdateAProjectRequest model constructor.
     * @property {module:model/UpdateAProjectRequest}
     */
    UpdateAProjectRequest,

    /**
     * The UpdateAProjectRequestOwner model constructor.
     * @property {module:model/UpdateAProjectRequestOwner}
     */
    UpdateAProjectRequestOwner,

    /**
     * The UpdateExistingIntegrationRequest model constructor.
     * @property {module:model/UpdateExistingIntegrationRequest}
     */
    UpdateExistingIntegrationRequest,

    /**
     * The UpdateExistingIntegrationRequestAnyOf model constructor.
     * @property {module:model/UpdateExistingIntegrationRequestAnyOf}
     */
    UpdateExistingIntegrationRequestAnyOf,

    /**
     * The UpdateExistingIntegrationRequestAnyOf1 model constructor.
     * @property {module:model/UpdateExistingIntegrationRequestAnyOf1}
     */
    UpdateExistingIntegrationRequestAnyOf1,

    /**
     * The UpdateExistingIntegrationRequestAnyOf2 model constructor.
     * @property {module:model/UpdateExistingIntegrationRequestAnyOf2}
     */
    UpdateExistingIntegrationRequestAnyOf2,

    /**
     * The UpdateOrganizationSettingsRequest model constructor.
     * @property {module:model/UpdateOrganizationSettingsRequest}
     */
    UpdateOrganizationSettingsRequest,

    /**
     * The UpdateOrganizationSettingsRequestRequestAccess model constructor.
     * @property {module:model/UpdateOrganizationSettingsRequestRequestAccess}
     */
    UpdateOrganizationSettingsRequestRequestAccess,

    /**
     * The UpdateProjectSettingsRequest model constructor.
     * @property {module:model/UpdateProjectSettingsRequest}
     */
    UpdateProjectSettingsRequest,

    /**
     * The UpdateRequest model constructor.
     * @property {module:model/UpdateRequest}
     */
    UpdateRequest,

    /**
     * The ViewGroupSettings200Response model constructor.
     * @property {module:model/ViewGroupSettings200Response}
     */
    ViewGroupSettings200Response,

    /**
     * The ViewGroupSettings200ResponseRequestAccess model constructor.
     * @property {module:model/ViewGroupSettings200ResponseRequestAccess}
     */
    ViewGroupSettings200ResponseRequestAccess,

    /**
     * The ViewOrganizationSettings200Response model constructor.
     * @property {module:model/ViewOrganizationSettings200Response}
     */
    ViewOrganizationSettings200Response,

    /**
     * The ViewOrganizationSettings200ResponseRequestAccess model constructor.
     * @property {module:model/ViewOrganizationSettings200ResponseRequestAccess}
     */
    ViewOrganizationSettings200ResponseRequestAccess,

    /**
     * The Vulnerability model constructor.
     * @property {module:model/Vulnerability}
     */
    Vulnerability,

    /**
     * The YarnLockFile model constructor.
     * @property {module:model/YarnLockFile}
     */
    YarnLockFile,

    /**
     * The YarnRequestPayload model constructor.
     * @property {module:model/YarnRequestPayload}
     */
    YarnRequestPayload,

    /**
    * The AuditLogsApi service constructor.
    * @property {module:api/AuditLogsApi}
    */
    AuditLogsApi,

    /**
    * The DependenciesApi service constructor.
    * @property {module:api/DependenciesApi}
    */
    DependenciesApi,

    /**
    * The EntitlementsApi service constructor.
    * @property {module:api/EntitlementsApi}
    */
    EntitlementsApi,

    /**
    * The GroupsApi service constructor.
    * @property {module:api/GroupsApi}
    */
    GroupsApi,

    /**
    * The ImportProjectsApi service constructor.
    * @property {module:api/ImportProjectsApi}
    */
    ImportProjectsApi,

    /**
    * The IntegrationsApi service constructor.
    * @property {module:api/IntegrationsApi}
    */
    IntegrationsApi,

    /**
    * The LicensesApi service constructor.
    * @property {module:api/LicensesApi}
    */
    LicensesApi,

    /**
    * The MonitorApi service constructor.
    * @property {module:api/MonitorApi}
    */
    MonitorApi,

    /**
    * The OrganizationsApi service constructor.
    * @property {module:api/OrganizationsApi}
    */
    OrganizationsApi,

    /**
    * The ProjectsApi service constructor.
    * @property {module:api/ProjectsApi}
    */
    ProjectsApi,

    /**
    * The ReportingAPIApi service constructor.
    * @property {module:api/ReportingAPIApi}
    */
    ReportingAPIApi,

    /**
    * The TestApi service constructor.
    * @property {module:api/TestApi}
    */
    TestApi,

    /**
    * The UsersApi service constructor.
    * @property {module:api/UsersApi}
    */
    UsersApi,

    /**
    * The WebhooksApi service constructor.
    * @property {module:api/WebhooksApi}
    */
    WebhooksApi
};
