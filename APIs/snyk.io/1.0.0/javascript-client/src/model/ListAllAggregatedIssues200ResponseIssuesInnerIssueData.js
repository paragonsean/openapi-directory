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

import ApiClient from '../ApiClient';
import ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers from './ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers';
import ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver from './ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver';

/**
 * The ListAllAggregatedIssues200ResponseIssuesInnerIssueData model module.
 * @module model/ListAllAggregatedIssues200ResponseIssuesInnerIssueData
 * @version 1.0.0
 */
class ListAllAggregatedIssues200ResponseIssuesInnerIssueData {
    /**
     * Constructs a new <code>ListAllAggregatedIssues200ResponseIssuesInnerIssueData</code>.
     * The details of the issue
     * @alias module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueData
     * @param cVSSv3 {String} The CVSS v3 string that signifies how the CVSS score was calculated (Non-IaC projects only)
     * @param credit {Array.<Object>} The list of people responsible for first uncovering or reporting the issue (Non-IaC projects only)
     * @param cvssScore {Number} The CVSS score that results from running the CVSSv3 string (Non-IaC projects only)
     * @param description {String} 
     * @param disclosureTime {String} The date that the vulnerability was first disclosed
     * @param exploitMaturity {String} The exploit maturity of the issue
     * @param id {String} The identifier of the issue
     * @param identifiers {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers} 
     * @param isMaliciousPackage {Boolean} Whether the issue is intentional, indicating a malicious package
     * @param language {String} The language of the issue (Non-IaC projects only)
     * @param nearestFixedInVersion {String} Nearest version which includes a fix for the issue. This is populated for container projects only. (Non-IaC projects only)
     * @param originalSeverity {String} The original severity status of the issue, as retrieved from Snyk Vulnerability database, before policies are applied
     * @param patches {Array.<Object>} A list of patches available for the given issue (Non-IaC projects only)
     * @param path {String} Path to the resource property violating the policy within the scanned project. (IaC projects only)
     * @param publicationTime {String} The date that the vulnerability was first published by Snyk (Non-IaC projects only)
     * @param semver {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver} 
     * @param severity {String} The severity status of the issue, after policies are applied
     * @param title {String} The issue title
     * @param url {String} URL to a page containing information about the issue
     * @param violatedPolicyPublicId {String} The ID of the violated policy in the issue (IaC projects only)
     */
    constructor(cVSSv3, credit, cvssScore, description, disclosureTime, exploitMaturity, id, identifiers, isMaliciousPackage, language, nearestFixedInVersion, originalSeverity, patches, path, publicationTime, semver, severity, title, url, violatedPolicyPublicId) { 
        
        ListAllAggregatedIssues200ResponseIssuesInnerIssueData.initialize(this, cVSSv3, credit, cvssScore, description, disclosureTime, exploitMaturity, id, identifiers, isMaliciousPackage, language, nearestFixedInVersion, originalSeverity, patches, path, publicationTime, semver, severity, title, url, violatedPolicyPublicId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, cVSSv3, credit, cvssScore, description, disclosureTime, exploitMaturity, id, identifiers, isMaliciousPackage, language, nearestFixedInVersion, originalSeverity, patches, path, publicationTime, semver, severity, title, url, violatedPolicyPublicId) { 
        obj['CVSSv3'] = cVSSv3;
        obj['credit'] = credit;
        obj['cvssScore'] = cvssScore;
        obj['description'] = description;
        obj['disclosureTime'] = disclosureTime;
        obj['exploitMaturity'] = exploitMaturity;
        obj['id'] = id;
        obj['identifiers'] = identifiers;
        obj['isMaliciousPackage'] = isMaliciousPackage;
        obj['language'] = language;
        obj['nearestFixedInVersion'] = nearestFixedInVersion;
        obj['originalSeverity'] = originalSeverity;
        obj['patches'] = patches;
        obj['path'] = path;
        obj['publicationTime'] = publicationTime;
        obj['semver'] = semver;
        obj['severity'] = severity;
        obj['title'] = title;
        obj['url'] = url;
        obj['violatedPolicyPublicId'] = violatedPolicyPublicId;
    }

    /**
     * Constructs a <code>ListAllAggregatedIssues200ResponseIssuesInnerIssueData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueData} obj Optional instance to populate.
     * @return {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueData} The populated <code>ListAllAggregatedIssues200ResponseIssuesInnerIssueData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListAllAggregatedIssues200ResponseIssuesInnerIssueData();

            if (data.hasOwnProperty('CVSSv3')) {
                obj['CVSSv3'] = ApiClient.convertToType(data['CVSSv3'], 'String');
            }
            if (data.hasOwnProperty('credit')) {
                obj['credit'] = ApiClient.convertToType(data['credit'], [Object]);
            }
            if (data.hasOwnProperty('cvssScore')) {
                obj['cvssScore'] = ApiClient.convertToType(data['cvssScore'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('disclosureTime')) {
                obj['disclosureTime'] = ApiClient.convertToType(data['disclosureTime'], 'String');
            }
            if (data.hasOwnProperty('exploitMaturity')) {
                obj['exploitMaturity'] = ApiClient.convertToType(data['exploitMaturity'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('identifiers')) {
                obj['identifiers'] = ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers.constructFromObject(data['identifiers']);
            }
            if (data.hasOwnProperty('isMaliciousPackage')) {
                obj['isMaliciousPackage'] = ApiClient.convertToType(data['isMaliciousPackage'], 'Boolean');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('nearestFixedInVersion')) {
                obj['nearestFixedInVersion'] = ApiClient.convertToType(data['nearestFixedInVersion'], 'String');
            }
            if (data.hasOwnProperty('originalSeverity')) {
                obj['originalSeverity'] = ApiClient.convertToType(data['originalSeverity'], 'String');
            }
            if (data.hasOwnProperty('patches')) {
                obj['patches'] = ApiClient.convertToType(data['patches'], [Object]);
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('publicationTime')) {
                obj['publicationTime'] = ApiClient.convertToType(data['publicationTime'], 'String');
            }
            if (data.hasOwnProperty('semver')) {
                obj['semver'] = ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver.constructFromObject(data['semver']);
            }
            if (data.hasOwnProperty('severity')) {
                obj['severity'] = ApiClient.convertToType(data['severity'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
            if (data.hasOwnProperty('violatedPolicyPublicId')) {
                obj['violatedPolicyPublicId'] = ApiClient.convertToType(data['violatedPolicyPublicId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListAllAggregatedIssues200ResponseIssuesInnerIssueData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListAllAggregatedIssues200ResponseIssuesInnerIssueData</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ListAllAggregatedIssues200ResponseIssuesInnerIssueData.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['CVSSv3'] && !(typeof data['CVSSv3'] === 'string' || data['CVSSv3'] instanceof String)) {
            throw new Error("Expected the field `CVSSv3` to be a primitive type in the JSON string but got " + data['CVSSv3']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['credit'])) {
            throw new Error("Expected the field `credit` to be an array in the JSON data but got " + data['credit']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['disclosureTime'] && !(typeof data['disclosureTime'] === 'string' || data['disclosureTime'] instanceof String)) {
            throw new Error("Expected the field `disclosureTime` to be a primitive type in the JSON string but got " + data['disclosureTime']);
        }
        // ensure the json data is a string
        if (data['exploitMaturity'] && !(typeof data['exploitMaturity'] === 'string' || data['exploitMaturity'] instanceof String)) {
            throw new Error("Expected the field `exploitMaturity` to be a primitive type in the JSON string but got " + data['exploitMaturity']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `identifiers`
        if (data['identifiers']) { // data not null
          ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers.validateJSON(data['identifiers']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        // ensure the json data is a string
        if (data['nearestFixedInVersion'] && !(typeof data['nearestFixedInVersion'] === 'string' || data['nearestFixedInVersion'] instanceof String)) {
            throw new Error("Expected the field `nearestFixedInVersion` to be a primitive type in the JSON string but got " + data['nearestFixedInVersion']);
        }
        // ensure the json data is a string
        if (data['originalSeverity'] && !(typeof data['originalSeverity'] === 'string' || data['originalSeverity'] instanceof String)) {
            throw new Error("Expected the field `originalSeverity` to be a primitive type in the JSON string but got " + data['originalSeverity']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['patches'])) {
            throw new Error("Expected the field `patches` to be an array in the JSON data but got " + data['patches']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // ensure the json data is a string
        if (data['publicationTime'] && !(typeof data['publicationTime'] === 'string' || data['publicationTime'] instanceof String)) {
            throw new Error("Expected the field `publicationTime` to be a primitive type in the JSON string but got " + data['publicationTime']);
        }
        // validate the optional field `semver`
        if (data['semver']) { // data not null
          ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver.validateJSON(data['semver']);
        }
        // ensure the json data is a string
        if (data['severity'] && !(typeof data['severity'] === 'string' || data['severity'] instanceof String)) {
            throw new Error("Expected the field `severity` to be a primitive type in the JSON string but got " + data['severity']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }
        // ensure the json data is a string
        if (data['violatedPolicyPublicId'] && !(typeof data['violatedPolicyPublicId'] === 'string' || data['violatedPolicyPublicId'] instanceof String)) {
            throw new Error("Expected the field `violatedPolicyPublicId` to be a primitive type in the JSON string but got " + data['violatedPolicyPublicId']);
        }

        return true;
    }


}

ListAllAggregatedIssues200ResponseIssuesInnerIssueData.RequiredProperties = ["CVSSv3", "credit", "cvssScore", "description", "disclosureTime", "exploitMaturity", "id", "identifiers", "isMaliciousPackage", "language", "nearestFixedInVersion", "originalSeverity", "patches", "path", "publicationTime", "semver", "severity", "title", "url", "violatedPolicyPublicId"];

/**
 * The CVSS v3 string that signifies how the CVSS score was calculated (Non-IaC projects only)
 * @member {String} CVSSv3
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['CVSSv3'] = undefined;

/**
 * The list of people responsible for first uncovering or reporting the issue (Non-IaC projects only)
 * @member {Array.<Object>} credit
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['credit'] = undefined;

/**
 * The CVSS score that results from running the CVSSv3 string (Non-IaC projects only)
 * @member {Number} cvssScore
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['cvssScore'] = undefined;

/**
 * @member {String} description
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['description'] = undefined;

/**
 * The date that the vulnerability was first disclosed
 * @member {String} disclosureTime
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['disclosureTime'] = undefined;

/**
 * The exploit maturity of the issue
 * @member {String} exploitMaturity
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['exploitMaturity'] = undefined;

/**
 * The identifier of the issue
 * @member {String} id
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['id'] = undefined;

/**
 * @member {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers} identifiers
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['identifiers'] = undefined;

/**
 * Whether the issue is intentional, indicating a malicious package
 * @member {Boolean} isMaliciousPackage
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['isMaliciousPackage'] = undefined;

/**
 * The language of the issue (Non-IaC projects only)
 * @member {String} language
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['language'] = undefined;

/**
 * Nearest version which includes a fix for the issue. This is populated for container projects only. (Non-IaC projects only)
 * @member {String} nearestFixedInVersion
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['nearestFixedInVersion'] = undefined;

/**
 * The original severity status of the issue, as retrieved from Snyk Vulnerability database, before policies are applied
 * @member {String} originalSeverity
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['originalSeverity'] = undefined;

/**
 * A list of patches available for the given issue (Non-IaC projects only)
 * @member {Array.<Object>} patches
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['patches'] = undefined;

/**
 * Path to the resource property violating the policy within the scanned project. (IaC projects only)
 * @member {String} path
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['path'] = undefined;

/**
 * The date that the vulnerability was first published by Snyk (Non-IaC projects only)
 * @member {String} publicationTime
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['publicationTime'] = undefined;

/**
 * @member {module:model/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver} semver
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['semver'] = undefined;

/**
 * The severity status of the issue, after policies are applied
 * @member {String} severity
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['severity'] = undefined;

/**
 * The issue title
 * @member {String} title
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['title'] = undefined;

/**
 * URL to a page containing information about the issue
 * @member {String} url
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['url'] = undefined;

/**
 * The ID of the violated policy in the issue (IaC projects only)
 * @member {String} violatedPolicyPublicId
 */
ListAllAggregatedIssues200ResponseIssuesInnerIssueData.prototype['violatedPolicyPublicId'] = undefined;






export default ListAllAggregatedIssues200ResponseIssuesInnerIssueData;

