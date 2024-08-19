/**
 * Snyk API
 * The Snyk API is available to customers on [Business and Enterprise plans](https://snyk.io/plans) and allows you to programatically integrate with Snyk.  ## REST API  We are in the process of building a new, improved API (`https://api.snyk.io/rest`) built using the OpenAPI and JSON API standards. We welcome you to try it out as we shape and release endpoints until it, ultimately, becomes a full replacement for our current API.  Looking for our REST API docs? Please head over to [https://apidocs.snyk.io](https://apidocs.snyk.io)  ## API vs CLI vs Snyk integration  The API detailed below has the ability to test a package for issues, as they are defined by Snyk. It is important to note that for many package managers, using this API will be less accurate than running the [Snyk CLI](https://snyk.io/docs/using-snyk) as part of your build pipe, or just using it locally on your package. The reason for this is that more than one package version fit the requirements given in manifest files. Running the CLI locally tests the actual deployed code, and has an accurate snapshot of the dependency versions in use, while the API can only infer it, with inferior accuracy. It should be noted that the Snyk CLI has the ability to output machine-readable JSON output (with the `--json` flag to `snyk test`).  A third option, is to allow Snyk access to your development flow via the existing [Snyk integrations](https://snyk.io/docs/). The advantage to this approach is having Snyk monitor every new pull request, and suggest fixes by opening new pull requests. This can be achieved either by integrating Snyk directly to your source code management (SCM) tool, or via a broker to allow greater security and auditability.  If those are not viable options, this API is your best choice.  ## API url  The base URL for all API endpoints is https://api.snyk.io/v1/  ## Authorization  To use this API, you must get your token from Snyk. It can be seen on https://snyk.io/account/ after you register with Snyk and login.  The token should be supplied in an `Authorization` header with the token, preceded by `token`:  ```http Authorization: token API_KEY ```  Otherwise, a 401 \"Unauthorized\" response will be returned.  ```http HTTP/1.1 401 Unauthorized          {             \"code\": 401,             \"error\": \"Not authorised\",             \"message\": \"Not authorised\"         } ```  ## Overview and entities  The API is a REST API. It has the following entities:  ### Test result  The test result is the object returned from the API giving the results of testing a package for issues. It has the following fields:  | Property        | Type    | Description                                           | Example                                                         | |----------------:|---------|-------------------------------------------------------|-----------------------------------------------------------------| | ok              | boolean | Does this package have one or more issues?             | false                                                           | | issues          | object  | The issues found. See below for details.              | See below                                                       | | dependencyCount | number  | The number of dependencies the package has.           | 9                                                               | | org             | object  | The organization this test was carried out for.       | {\"name\": \"anOrg\", \"id\": \"5d7013d9-2a57-4c89-993c-0304d960193c\"} | | licensesPolicy  | object  | The organization's licenses policy used for this test | See in the examples                                             | | packageManager  | string  | The package manager for this package                  | \"maven\"                                                         | |                 |         |                                                       |                                                                 |  ### Issue  An issue is either a vulnerability or a license issue, according to the organization's policy. It has the following fields:  | Property       | Type          | Description                                                                                                                | Example                                | |---------------:|---------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------| | id             | string        | The issue ID                                                                                                               | \"SNYK-JS-BACKBONE-10054\"               | | url            | string        | A link to the issue details on snyk.io                                                                                     | \"https://snyk.io/vuln/SNYK-JS-BACKBONE-10054 | | title          | string        | The issue title                                                                                                            | \"Cross Site Scripting\"                 | | type           | string        | The issue type: \"license\" or \"vulnerability\".                                                                              | \"license\"                              | | paths          | array         | The paths to the dependencies which have an issue, and their corresponding upgrade path (if an upgrade is available). [More information about from and upgrade paths](#introduction/overview-and-entities/from-and-upgrade-paths) | [<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;\"from\": [\"a@1.0.0\", \"b@4.8.1\"],<br>&nbsp;&nbsp;&nbsp;&nbsp;\"upgrade\": [false, \"b@4.8.2\"]<br>&nbsp;&nbsp;}<br>] | | package        | string        | The package identifier according to its package manager                                                                    | \"backbone\", \"org.apache.flex.blazeds:blazeds\"| | version        | string        | The package version this issue is applicable to.                                                                           | \"0.4.0\"                                | | severity       | string        | The Snyk defined severity level: \"critical\", \"high\", \"medium\" or \"low\".                                                    | \"high\"                                 | | language       | string        | The package's programming language                                                                                         | \"js\"                                   | | packageManager | string        | The package manager                                                                                                        | \"npm\"                                  | | semver         | array[string] OR map[string]array[string] | One or more [semver](https://semver.org) ranges this issue is applicable to. The format varies according to package manager. | [\"<0.5.0, >=0.4.0\", \"<0.3.8, >=0.3.6\"] OR { \"vulnerable\": [\"[2.0.0, 3.0.0)\"], \"unaffected\": [\"[1, 2)\", \"[3, )\"] } |  ### Vulnerability  A vulnerability in a package. In addition to all the fields present in an issue, a vulnerability also has these fields:  Property        | Type    | Description                                                                                                                                                                                                                      | Example                                        | ----------------:|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|  publicationTime | Date    | The vulnerability publication time                                                                                                                                                                                               | \"2016-02-11T07:16:18.857Z\"                     |  disclosureTime  | Date    | The time this vulnerability was originally disclosed to the package maintainers                                                                                                                                                   | \"2016-02-11T07:16:18.857Z\"                     |  isUpgradable    | boolean | Is this vulnerability fixable by upgrading a dependency?                                                                                                                                                                         | true                                           |  description     | string  | The detailed description of the vulnerability, why and how it is exploitable. Provided in markdown format. | \"## Overview\\n[`org.apache.logging.log4j:log4j-core`](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22log4j-core%22)\\nIn Apache Log4j 2.x before 2.8.2, when using the TCP socket server or UDP socket server to receive serialized log events from another application, a specially crafted binary payload can be sent that, when deserialized, can execute arbitrary code.\\n\\n# Details\\nSerialization is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. The reverse process of creating object from sequence of bytes is called deserialization. Serialization is commonly used for communication (sharing objects between multiple hosts) and persistence (store the object state in a file or a database). It is an integral part of popular protocols like _Remote Method Invocation (RMI)_, _Java Management Extension (JMX)_, _Java Messaging System (JMS)_, _Action Message Format (AMF)_, _Java Server Faces (JSF) ViewState_, etc.\\n\\n_Deserialization of untrusted data_ ([CWE-502](https://cwe.mitre.org/data/definitions/502.html)), is when the application deserializes untrusted data without sufficiently verifying that the resulting data will be valid, letting the attacker to control the state or the flow of the execution. \\n\\nJava deserialization issues have been known for years. However, interest in the issue intensified greatly in 2015, when classes that could be abused to achieve remote code execution were found in a [popular library (Apache Commons Collection)](https://snyk.io/vuln/SNYK-JAVA-COMMONSCOLLECTIONS-30078). These classes were used in zero-days affecting IBM WebSphere, Oracle WebLogic and many other products.\\n\\nAn attacker just needs to identify a piece of software that has both a vulnerable class on its path, and performs deserialization on untrusted data. Then all they need to do is send the payload into the deserializer, getting the command executed.\\n\\n> Developers put too much trust in Java Object Serialization. Some even de-serialize objects pre-authentication. When deserializing an Object in Java you typically cast it to an expected type, and therefore Java's strict type system will ensure you only get valid object trees. Unfortunately, by the time the type checking happens, platform code has already created and executed significant logic. So, before the final type is checked a lot of code is executed from the readObject() methods of various objects, all of which is out of the developer's control. By combining the readObject() methods of various classes which are available on the classpath of the vulnerable application an attacker can execute functions (including calling Runtime.exec() to execute local OS commands).\\n- Apache Blog\\n\\n\\n## References\\n- [NVD](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5645)\\n- [jira issue](https://issues.apache.org/jira/browse/LOG4J2-1863)\\n\" |  isPatchable     | boolean | Is this vulnerability fixable by using a Snyk supplied patch?                                                                                                                                                                    | true                                           |  isPinnable      | boolean | Is this vulnerability fixable by pinning a transitive dependency                                                                                                                                                                 | true                                           |  identifiers     | object  | Additional vulnerability identifiers                                                                                                                                                                                             | {\"CWE\": [], \"CVE\": [\"CVE-2016-2402]}           |  credit          | string  | The reporter of the vulnerability                                                                                                                                                                                                | \"Snyk Security Team\"                           |  CVSSv3          | string  | Common Vulnerability Scoring System (CVSS) provides a way to capture the principal characteristics of a vulnerability, and produce a numerical score reflecting its severity, as well as a textual representation of that score. | \"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N\" |  cvssScore       | number  | CVSS Score                                                                                                                                                                                                                       | 5.3                                            |  patches         | array   | Patches to fix this issue, by snyk                                                                                                                                                                                               | see \"Patch\" below.                             |  upgradePath     | object  | The path to upgrade this issue, if applicable                                                                                                                                                                                    | see below                                      |  isPatched       | boolean | Is this vulnerability patched?                                                                                                                                                                                                   | false                                          |  exploitMaturity | string  | The snyk exploit maturity level  #### Patch  A patch is an object like this one:  ```json {   \"urls\": [     \"https://snyk-patches.s3.amazonaws.com/npm/backbone/20110701/backbone_20110701_0_0_0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"   ],   \"version\": \"<0.5.0 >=0.3.3\",   \"modificationTime\": \"2015-11-06T02:09:36.180Z\",   \"comments\": [     \"https://github.com/jashkenas/backbone/commit/0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"   ],   \"id\": \"patch:npm:backbone:20110701:0\" } ```  ### From and upgrade paths  Both from and upgrade paths are arrays, where each item within the array is a package `name@version`.  Take the following `from` path:  ``` [   \"my-project@1.0.0\",   \"actionpack@4.2.5\",   \"rack@1.6.4\" ] ```  Assuming this was returned as a result of a test, then we know:  - The package that was tested was `my-project@1.0.0`  - The dependency with an issue was included in the tested package via the direct dependency `actionpack@4.2.5`  - The dependency with an issue was [rack@1.6.4](https://snyk.io/vuln/rubygems:rack@1.6.4)  Take the following `upgrade` path:  ``` [   false,   \"actionpack@5.0.0\",   \"rack@2.0.1\" ] ```  Assuming this was returned as a result of a test, then we know:  - The package that was tested is not upgradable (`false`)  - The direct dependency `actionpack` should be upgraded to at least version `5.0.0` in order to fix the issue  - Upgrading `actionpack` to version `5.0.0` will cause `rack` to be installed at version `2.0.1`  If the `upgrade` path comes back as an empty array (`[]`) then this means that there is no upgrade path available which would fix the issue.  ### License issue  A license issue has no additional fields other than the ones in \"Issue\".  ### Snyk organization  The organization in Snyk this request is applicable to. The organization determines the access rights, licenses policy and is the unit of billing for private projects.  A Snyk organization has these fields:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | name        | string | The organization display name | \"deelmaker\"                            | id          | string | The ID of the organization    | \"3ab0f8d3-b17d-4953-ab6d-e1cbfe1df385\" |  ## Errors  This is a beta release of this API. Therefore, despite our efforts, errors might occur. In the unlikely event of such an error, it will have the following structure as JSON in the body:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | message     | string | Error message with reference  | Error calling Snyk api (reference: 39db46b1-ad57-47e6-a87d-e34f6968030b) | errorRef    | V4 uuid | An error ref to contact Snyk with | 39db46b1-ad57-47e6-a87d-e34f6968030b |  The error reference will also be supplied in the `x-error-reference` header in the server reply.  Example response:  ```http HTTP/1.1 500 Internal Server Error x-error-reference: a45ec9c1-065b-4f7b-baf8-dbd1552ffc9f Content-Type: application/json; charset=utf-8 Content-Length: 1848 Vary: Accept-Encoding Date: Sun, 10 Sep 2017 06:48:40 GMT ```  ## Rate Limiting  To ensure resilience against increasing request rates, we are starting to introduce rate-limiting. We are monitoring the rate-limiting system to ensure minimal impact on users while ensuring system stability. The limit is up to 2000 requests per minute, per user, subject to change. As such, we recommend calls to the API are throttled regardless of the current limit. All requests above the limit will get a response with status code `429` - `Too many requests` until requests stop for the duration of the rate-limiting interval (currently a minute).  ## Consuming Webhooks  Webhooks are delivered with a `Content-Type` of `application/json`, with the event payload as JSON in the request body. We also send the following headers:  - `X-Snyk-Event` - the name of the event  - `X-Snyk-Transport-ID` - a GUID to identify this delivery  - `X-Snyk-Timestamp` - an ISO 8601 timestamp for when the event occurred, for example: `2020-09-25T15:27:53Z`  - `X-Hub-Signature` - the HMAC hex digest of the request body, used to secure your webhooks and ensure the request did indeed come from Snyk  - `User-Agent` - identifies the origin of the request, for example: `Snyk-Webhooks/XXX`  ---  After your server is configured to receive payloads, it listens for any payload sent to the endpoint you configured. For security reasons, you should limit requests to those coming from Snyk.  ### Validating payloads  All transports sent to your webhooks have a `X-Hub-Signature` header, which contains the hash signature for the transport. The signature is a HMAC hexdigest of the request body, generated using sha256 and your `secret` as the HMAC key.  You could use a function in Node.JS such as the following to validate these signatures on incoming requests from Snyk:  ```javascript import * as crypto from 'crypto';  function verifySignature(request, secret) {   const hmac = crypto.createHmac('sha256', secret);   const buffer = JSON.stringify(request.body);   hmac.update(buffer, 'utf8');    const signature = `sha256=${hmac.digest('hex')}`;    return signature === request.headers['x-hub-signature']; } ```  ### Payload versioning  Payloads may evolve over time, and so are versioned. Payload versions are supplied as a suffix to the `X-Snyk-Event` header. For example, `project_snapshot/v0` indicates that the payload is `v0` of the `project_snapshot` event.  Version numbers only increment when a breaking change is made; for example, removing a field that used to exist, or changing the name of a field. Version numbers do not increment when making an additive change, such as adding a new field that never existed before.  **Note:** During the BETA phase, the structure of webhook payloads may change at any time, so we  recommend you check the payload version.  ### Event types  While consuming a webhook event, `X-Snyk-Event` header must be checked, as an end-point may receive multiple event types.  #### ping  The ping event happens after a new webhook is created, and can also be manually triggered using the ping webhook API. This is useful to test that your webhook receives data from Snyk correctly.  The `ping` event makes the following request:  ```jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: ping/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \"webhookId\": \"d3cf26b3-2d77-497b-bce2-23b33cc15362\" } ```  #### project_snapshot  This event is triggered every time an existing project is tested and a new snapshot is created. It is triggered on every test of a project, whether or not there are new issues. This event is not triggered when a new project is created or imported. Currently supported targets/scan types are Open Source and container.  ```jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: project_snapshot/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \"project\": { ... }, // project object matching API responses   \"org\": { ... }, // organization object matching API responses   \"group\": { ... }, // group object matching API responses   \"newIssues\": [], // array of issues object matching API responses   \"removedIssues\": [], // array of issues object matching API responses } ```  ####  Detailed example of a payload  ##### project  see: [https://snyk.docs.apiary.io/#reference/projects](https://snyk.docs.apiary.io/#reference/projects)  ```tsx \"project\": {   \"name\": \"snyk/goof\",   \"id\": \"af137b96-6966-46c1-826b-2e79ac49bbd9\",   \"created\": \"2018-10-29T09:50:54.014Z\",   \"origin\": \"github\",   \"type\": \"maven\",   \"readOnly\": false,   \"testFrequency\": \"daily\",   \"totalDependencies\": 42,   \"issueCountsBySeverity\": {     \"low\": 13,     \"medium\": 8,     \"high\": 4,     \"critical\": 5   },   \"imageId\": \"sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019\",   \"imageTag\": \"latest\",   \"imageBaseImage\": \"alpine:3\",   \"imagePlatform\": \"linux/arm64\",   \"imageCluster\": \"Production\",   \"hostname\": null,   \"remoteRepoUrl\": \"https://github.com/snyk/goof.git\",   \"lastTestedDate\": \"2019-02-05T08:54:07.704Z\",   \"browseUrl\": \"https://app.snyk.io/org/4a18d42f-0706-4ad0-b127-24078731fbed/project/af137b96-6966-46c1-826b-2e79ac49bbd9\",   \"importingUser\": {     \"id\": \"e713cf94-bb02-4ea0-89d9-613cce0caed2\",     \"name\": \"example-user@snyk.io\",     \"username\": \"exampleUser\",     \"email\": \"example-user@snyk.io\"   },   \"isMonitored\": false,   \"branch\": null,   \"targetReference\": null,   \"tags\": [     {       \"key\": \"example-tag-key\",       \"value\": \"example-tag-value\"     }   ],   \"attributes\": {     \"criticality\": [       \"high\"     ],     \"environment\": [       \"backend\"     ],     \"lifecycle\": [       \"development\"     ]   },   \"remediation\": {     \"upgrade\": {},     \"patch\": {},     \"pin\": {}   } } ```  ##### org  see: [https://snyk.docs.apiary.io/#reference/organizations](https://snyk.docs.apiary.io/#reference/organizations)  ```tsx \"org\": {   \"name\": \"My Org\",   \"id\": \"a04d9cbd-ae6e-44af-b573-0556b0ad4bd2\",   \"slug\": \"my-org\",   \"url\": \"https://api.snyk.io/org/my-org\",   \"created\": \"2020-11-18T10:39:00.983Z\" } ```  ##### group  see: [https://snyk.docs.apiary.io/#reference/groups](https://snyk.docs.apiary.io/#reference/groups)  ```tsx \"group\": {   \"name\": \"ACME Inc.\",    \"id\": \"a060a49f-636e-480f-9e14-38e773b2a97f\" } ```  ##### issue  see: https://snyk.docs.apiary.io/#reference/users/user-organization-notification-settings/list-all-aggregated-issues  ```tsx {   \"id\": \"npm:ms:20170412\",   \"issueType\": \"vuln\",   \"pkgName\": \"ms\",   \"pkgVersions\": [     \"1.0.0\"   ],   \"issueData\": {     \"id\": \"npm:ms:20170412\",     \"title\": \"Regular Expression Denial of Service (ReDoS)\",     \"severity\": \"low\",     \"url\": \"https://snyk.io/vuln/npm:ms:20170412\",     \"description\": \"Lorem ipsum\",     \"identifiers\": {       \"CVE\": [],       \"CWE\": [         \"CWE-400\"       ],       \"ALTERNATIVE\": [         \"SNYK-JS-MS-10509\"       ]     },     \"credit\": [       \"Snyk Security Research Team\"     ],     \"exploitMaturity\": \"no-known-exploit\",     \"semver\": {       \"vulnerable\": [         \">=0.7.1 <2.0.0\"       ]     },     \"publicationTime\": \"2017-05-15T06:02:45Z\",     \"disclosureTime\": \"2017-04-11T21:00:00Z\",     \"CVSSv3\": \"CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L\",     \"cvssScore\": 3.7,     \"language\": \"js\",     \"patches\": [       {         \"id\": \"patch:npm:ms:20170412:2\",         \"urls\": [           \"https://snyk-patches.s3.amazonaws.com/npm/ms/20170412/ms_071.patch\"         ],         \"version\": \"=0.7.1\",         \"comments\": [],         \"modificationTime\": \"2019-12-03T11:40:45.866206Z\"       }     ],     \"nearestFixedInVersion\": \"2.0.0\"   },   \"isPatched\": false,   \"isIgnored\": false,   \"fixInfo\": {     \"isUpgradable\": false,     \"isPinnable\": false,     \"isPatchable\": true,     \"nearestFixedInVersion\": \"2.0.0\"   },   \"priority\": {     \"score\": 399,     \"factors\": [       {         \"name\": \"isFixable\",         \"description\": \"Has a fix available\"       },       {         \"name\": \"cvssScore\",         \"description\": \"CVSS 3.7\"       }     ]   } } ```
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProjectsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIProjectsApi::OAIProjectsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIProjectsApi::~OAIProjectsApi() {
}

void OAIProjectsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.snyk.io/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("activate", defaultConf);
    _serverIndices.insert("activate", 0);
    _serverConfigs.insert("add_a_tag_to_a_project", defaultConf);
    _serverIndices.insert("add_a_tag_to_a_project", 0);
    _serverConfigs.insert("add_ignore", defaultConf);
    _serverIndices.insert("add_ignore", 0);
    _serverConfigs.insert("applying_attributes", defaultConf);
    _serverIndices.insert("applying_attributes", 0);
    _serverConfigs.insert("create_jira_issue", defaultConf);
    _serverIndices.insert("create_jira_issue", 0);
    _serverConfigs.insert("deactivate", defaultConf);
    _serverIndices.insert("deactivate", 0);
    _serverConfigs.insert("delete_a_project", defaultConf);
    _serverIndices.insert("delete_a_project", 0);
    _serverConfigs.insert("delete_ignores", defaultConf);
    _serverIndices.insert("delete_ignores", 0);
    _serverConfigs.insert("delete_project_settings", defaultConf);
    _serverIndices.insert("delete_project_settings", 0);
    _serverConfigs.insert("get_Project_dependency_graph", defaultConf);
    _serverIndices.insert("get_Project_dependency_graph", 0);
    _serverConfigs.insert("list_all_Aggregated_issues", defaultConf);
    _serverIndices.insert("list_all_Aggregated_issues", 0);
    _serverConfigs.insert("list_all_ignores", defaultConf);
    _serverIndices.insert("list_all_ignores", 0);
    _serverConfigs.insert("list_all_jira_issues", defaultConf);
    _serverIndices.insert("list_all_jira_issues", 0);
    _serverConfigs.insert("list_all_project_issue_paths", defaultConf);
    _serverIndices.insert("list_all_project_issue_paths", 0);
    _serverConfigs.insert("list_all_project_snapshot_aggregated_issues", defaultConf);
    _serverIndices.insert("list_all_project_snapshot_aggregated_issues", 0);
    _serverConfigs.insert("list_all_project_snapshot_issue_paths", defaultConf);
    _serverIndices.insert("list_all_project_snapshot_issue_paths", 0);
    _serverConfigs.insert("list_all_project_snapshots", defaultConf);
    _serverIndices.insert("list_all_project_snapshots", 0);
    _serverConfigs.insert("list_all_projects", defaultConf);
    _serverIndices.insert("list_all_projects", 0);
    _serverConfigs.insert("list_project_settings", defaultConf);
    _serverIndices.insert("list_project_settings", 0);
    _serverConfigs.insert("move_project_to_a_different_organization", defaultConf);
    _serverIndices.insert("move_project_to_a_different_organization", 0);
    _serverConfigs.insert("remove_a_tag_from_a_project", defaultConf);
    _serverIndices.insert("remove_a_tag_from_a_project", 0);
    _serverConfigs.insert("replace_ignores", defaultConf);
    _serverIndices.insert("replace_ignores", 0);
    _serverConfigs.insert("retrieve_a_single_project", defaultConf);
    _serverIndices.insert("retrieve_a_single_project", 0);
    _serverConfigs.insert("retrieve_ignore", defaultConf);
    _serverIndices.insert("retrieve_ignore", 0);
    _serverConfigs.insert("update_a_project", defaultConf);
    _serverIndices.insert("update_a_project", 0);
    _serverConfigs.insert("update_project_settings", defaultConf);
    _serverIndices.insert("update_project_settings", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIProjectsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIProjectsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIProjectsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIProjectsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIProjectsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIProjectsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIProjectsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIProjectsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIProjectsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAIProjectsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIProjectsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIProjectsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIProjectsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIProjectsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIProjectsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIProjectsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIProjectsApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAIProjectsApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAIProjectsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAIProjectsApi::activate(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["activate"][_serverIndices.value("activate")].URL()+"/org/{orgId}/project/{projectId}/activate");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::activateCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::activateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT activateSignal();
        Q_EMIT activateSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT activateSignalE(error_type, error_str);
        Q_EMIT activateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT activateSignalError(error_type, error_str);
        Q_EMIT activateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::add_a_tag_to_a_project(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIAdd_a_tag_to_a_project_request> &oai_add_a_tag_to_a_project_request) {
    QString fullPath = QString(_serverConfigs["add_a_tag_to_a_project"][_serverIndices.value("add_a_tag_to_a_project")].URL()+"/org/{orgId}/project/{projectId}/tags");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_add_a_tag_to_a_project_request.hasValue()){

        
        QByteArray output = oai_add_a_tag_to_a_project_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::add_a_tag_to_a_projectCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::add_a_tag_to_a_projectCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAdd_a_tag_to_a_project_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT add_a_tag_to_a_projectSignal(output);
        Q_EMIT add_a_tag_to_a_projectSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT add_a_tag_to_a_projectSignalE(output, error_type, error_str);
        Q_EMIT add_a_tag_to_a_projectSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT add_a_tag_to_a_projectSignalError(output, error_type, error_str);
        Q_EMIT add_a_tag_to_a_projectSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::add_ignore(const QString &org_id, const QString &project_id, const QString &issue_id, const ::OpenAPI::OptionalParam<OAIAdd_ignore_request> &oai_add_ignore_request) {
    QString fullPath = QString(_serverConfigs["add_ignore"][_serverIndices.value("add_ignore")].URL()+"/org/{orgId}/project/{projectId}/ignore/{issueId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_add_ignore_request.hasValue()){

        
        QByteArray output = oai_add_ignore_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::add_ignoreCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::add_ignoreCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT add_ignoreSignal(output);
        Q_EMIT add_ignoreSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT add_ignoreSignalE(output, error_type, error_str);
        Q_EMIT add_ignoreSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT add_ignoreSignalError(output, error_type, error_str);
        Q_EMIT add_ignoreSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::applying_attributes(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIApplying_attributes_request> &oai_applying_attributes_request) {
    QString fullPath = QString(_serverConfigs["applying_attributes"][_serverIndices.value("applying_attributes")].URL()+"/org/{orgId}/project/{projectId}/attributes");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_applying_attributes_request.hasValue()){

        
        QByteArray output = oai_applying_attributes_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::applying_attributesCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::applying_attributesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIApplying_attributes_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT applying_attributesSignal(output);
        Q_EMIT applying_attributesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT applying_attributesSignalE(output, error_type, error_str);
        Q_EMIT applying_attributesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT applying_attributesSignalError(output, error_type, error_str);
        Q_EMIT applying_attributesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::create_jira_issue(const QString &issue_id, const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAICreate_jira_issue_request> &oai_create_jira_issue_request) {
    QString fullPath = QString(_serverConfigs["create_jira_issue"][_serverIndices.value("create_jira_issue")].URL()+"/org/{orgId}/project/{projectId}/issue/{issueId}/jira-issue");
    
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_create_jira_issue_request.hasValue()){

        
        QByteArray output = oai_create_jira_issue_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::create_jira_issueCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::create_jira_issueCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreate_jira_issue_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT create_jira_issueSignal(output);
        Q_EMIT create_jira_issueSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT create_jira_issueSignalE(output, error_type, error_str);
        Q_EMIT create_jira_issueSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT create_jira_issueSignalError(output, error_type, error_str);
        Q_EMIT create_jira_issueSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::deactivate(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["deactivate"][_serverIndices.value("deactivate")].URL()+"/org/{orgId}/project/{projectId}/deactivate");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::deactivateCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::deactivateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deactivateSignal();
        Q_EMIT deactivateSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deactivateSignalE(error_type, error_str);
        Q_EMIT deactivateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deactivateSignalError(error_type, error_str);
        Q_EMIT deactivateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::delete_a_project(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["delete_a_project"][_serverIndices.value("delete_a_project")].URL()+"/org/{orgId}/project/{projectId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::delete_a_projectCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::delete_a_projectCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT delete_a_projectSignal();
        Q_EMIT delete_a_projectSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT delete_a_projectSignalE(error_type, error_str);
        Q_EMIT delete_a_projectSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT delete_a_projectSignalError(error_type, error_str);
        Q_EMIT delete_a_projectSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::delete_ignores(const QString &org_id, const QString &project_id, const QString &issue_id) {
    QString fullPath = QString(_serverConfigs["delete_ignores"][_serverIndices.value("delete_ignores")].URL()+"/org/{orgId}/project/{projectId}/ignore/{issueId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::delete_ignoresCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::delete_ignoresCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT delete_ignoresSignal();
        Q_EMIT delete_ignoresSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT delete_ignoresSignalE(error_type, error_str);
        Q_EMIT delete_ignoresSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT delete_ignoresSignalError(error_type, error_str);
        Q_EMIT delete_ignoresSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::delete_project_settings(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["delete_project_settings"][_serverIndices.value("delete_project_settings")].URL()+"/org/{orgId}/project/{projectId}/settings");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::delete_project_settingsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::delete_project_settingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT delete_project_settingsSignal();
        Q_EMIT delete_project_settingsSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT delete_project_settingsSignalE(error_type, error_str);
        Q_EMIT delete_project_settingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT delete_project_settingsSignalError(error_type, error_str);
        Q_EMIT delete_project_settingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::get_Project_dependency_graph(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["get_Project_dependency_graph"][_serverIndices.value("get_Project_dependency_graph")].URL()+"/org/{orgId}/project/{projectId}/dep-graph");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::get_Project_dependency_graphCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::get_Project_dependency_graphCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGet_Project_dependency_graph_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT get_Project_dependency_graphSignal(output);
        Q_EMIT get_Project_dependency_graphSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT get_Project_dependency_graphSignalE(output, error_type, error_str);
        Q_EMIT get_Project_dependency_graphSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT get_Project_dependency_graphSignalError(output, error_type, error_str);
        Q_EMIT get_Project_dependency_graphSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_Aggregated_issues(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIList_all_Aggregated_issues_request> &oai_list_all_aggregated_issues_request) {
    QString fullPath = QString(_serverConfigs["list_all_Aggregated_issues"][_serverIndices.value("list_all_Aggregated_issues")].URL()+"/org/{orgId}/project/{projectId}/aggregated-issues");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_list_all_aggregated_issues_request.hasValue()){

        
        QByteArray output = oai_list_all_aggregated_issues_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_Aggregated_issuesCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_Aggregated_issuesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_all_Aggregated_issues_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_Aggregated_issuesSignal(output);
        Q_EMIT list_all_Aggregated_issuesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_Aggregated_issuesSignalE(output, error_type, error_str);
        Q_EMIT list_all_Aggregated_issuesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_Aggregated_issuesSignalError(output, error_type, error_str);
        Q_EMIT list_all_Aggregated_issuesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_ignores(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["list_all_ignores"][_serverIndices.value("list_all_ignores")].URL()+"/org/{orgId}/project/{projectId}/ignores");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_ignoresCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_ignoresCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_ignoresSignal(output);
        Q_EMIT list_all_ignoresSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_ignoresSignalE(output, error_type, error_str);
        Q_EMIT list_all_ignoresSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_ignoresSignalError(output, error_type, error_str);
        Q_EMIT list_all_ignoresSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_jira_issues(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["list_all_jira_issues"][_serverIndices.value("list_all_jira_issues")].URL()+"/org/{orgId}/project/{projectId}/jira-issues");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_jira_issuesCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_jira_issuesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_jira_issuesSignal(output);
        Q_EMIT list_all_jira_issuesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_jira_issuesSignalE(output, error_type, error_str);
        Q_EMIT list_all_jira_issuesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_jira_issuesSignalError(output, error_type, error_str);
        Q_EMIT list_all_jira_issuesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_project_issue_paths(const QString &org_id, const QString &project_id, const QString &issue_id, const ::OpenAPI::OptionalParam<QString> &snapshot_id, const ::OpenAPI::OptionalParam<double> &per_page, const ::OpenAPI::OptionalParam<double> &page) {
    QString fullPath = QString(_serverConfigs["list_all_project_issue_paths"][_serverIndices.value("list_all_project_issue_paths")].URL()+"/org/{orgId}/project/{projectId}/issue/{issueId}/paths");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (snapshot_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "snapshotId", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("snapshotId")).append(querySuffix).append(QUrl::toPercentEncoding(snapshot_id.stringValue()));
    }
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "perPage", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("perPage")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_project_issue_pathsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_project_issue_pathsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_all_project_snapshot_issue_paths_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_project_issue_pathsSignal(output);
        Q_EMIT list_all_project_issue_pathsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_project_issue_pathsSignalE(output, error_type, error_str);
        Q_EMIT list_all_project_issue_pathsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_project_issue_pathsSignalError(output, error_type, error_str);
        Q_EMIT list_all_project_issue_pathsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_project_snapshot_aggregated_issues(const QString &org_id, const QString &project_id, const QString &snapshot_id, const ::OpenAPI::OptionalParam<OAIList_all_Aggregated_issues_request> &oai_list_all_aggregated_issues_request) {
    QString fullPath = QString(_serverConfigs["list_all_project_snapshot_aggregated_issues"][_serverIndices.value("list_all_project_snapshot_aggregated_issues")].URL()+"/org/{orgId}/project/{projectId}/history/{snapshotId}/aggregated-issues");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString snapshot_idPathParam("{");
        snapshot_idPathParam.append("snapshotId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "snapshotId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"snapshotId"+pathSuffix : pathPrefix;
        fullPath.replace(snapshot_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(snapshot_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_list_all_aggregated_issues_request.hasValue()){

        
        QByteArray output = oai_list_all_aggregated_issues_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_project_snapshot_aggregated_issuesCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_project_snapshot_aggregated_issuesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_all_Aggregated_issues_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_project_snapshot_aggregated_issuesSignal(output);
        Q_EMIT list_all_project_snapshot_aggregated_issuesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_project_snapshot_aggregated_issuesSignalE(output, error_type, error_str);
        Q_EMIT list_all_project_snapshot_aggregated_issuesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_project_snapshot_aggregated_issuesSignalError(output, error_type, error_str);
        Q_EMIT list_all_project_snapshot_aggregated_issuesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_project_snapshot_issue_paths(const QString &org_id, const QString &project_id, const QString &snapshot_id, const QString &issue_id, const ::OpenAPI::OptionalParam<double> &per_page, const ::OpenAPI::OptionalParam<double> &page) {
    QString fullPath = QString(_serverConfigs["list_all_project_snapshot_issue_paths"][_serverIndices.value("list_all_project_snapshot_issue_paths")].URL()+"/org/{orgId}/project/{projectId}/history/{snapshotId}/issue/{issueId}/paths");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString snapshot_idPathParam("{");
        snapshot_idPathParam.append("snapshotId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "snapshotId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"snapshotId"+pathSuffix : pathPrefix;
        fullPath.replace(snapshot_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(snapshot_id)));
    }
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "perPage", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("perPage")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_project_snapshot_issue_pathsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_project_snapshot_issue_pathsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_all_project_snapshot_issue_paths_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_project_snapshot_issue_pathsSignal(output);
        Q_EMIT list_all_project_snapshot_issue_pathsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_project_snapshot_issue_pathsSignalE(output, error_type, error_str);
        Q_EMIT list_all_project_snapshot_issue_pathsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_project_snapshot_issue_pathsSignalError(output, error_type, error_str);
        Q_EMIT list_all_project_snapshot_issue_pathsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_project_snapshots(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<double> &per_page, const ::OpenAPI::OptionalParam<double> &page, const ::OpenAPI::OptionalParam<OAIList_all_project_snapshots_request> &oai_list_all_project_snapshots_request) {
    QString fullPath = QString(_serverConfigs["list_all_project_snapshots"][_serverIndices.value("list_all_project_snapshots")].URL()+"/org/{orgId}/project/{projectId}/history");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (per_page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "perPage", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("perPage")).append(querySuffix).append(QUrl::toPercentEncoding(per_page.stringValue()));
    }
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_list_all_project_snapshots_request.hasValue()){

        
        QByteArray output = oai_list_all_project_snapshots_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_project_snapshotsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_project_snapshotsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_all_project_snapshots_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_project_snapshotsSignal(output);
        Q_EMIT list_all_project_snapshotsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_project_snapshotsSignalE(output, error_type, error_str);
        Q_EMIT list_all_project_snapshotsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_project_snapshotsSignalError(output, error_type, error_str);
        Q_EMIT list_all_project_snapshotsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_all_projects(const QString &org_id, const ::OpenAPI::OptionalParam<OAIList_all_projects_request> &oai_list_all_projects_request) {
    QString fullPath = QString(_serverConfigs["list_all_projects"][_serverIndices.value("list_all_projects")].URL()+"/org/{orgId}/projects");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_list_all_projects_request.hasValue()){

        
        QByteArray output = oai_list_all_projects_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_all_projectsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_all_projectsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_all_projects_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_all_projectsSignal(output);
        Q_EMIT list_all_projectsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_all_projectsSignalE(output, error_type, error_str);
        Q_EMIT list_all_projectsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_all_projectsSignalError(output, error_type, error_str);
        Q_EMIT list_all_projectsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::list_project_settings(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["list_project_settings"][_serverIndices.value("list_project_settings")].URL()+"/org/{orgId}/project/{projectId}/settings");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::list_project_settingsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::list_project_settingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_project_settings_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT list_project_settingsSignal(output);
        Q_EMIT list_project_settingsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT list_project_settingsSignalE(output, error_type, error_str);
        Q_EMIT list_project_settingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT list_project_settingsSignalError(output, error_type, error_str);
        Q_EMIT list_project_settingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::move_project_to_a_different_organization(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIMove_project_to_a_different_organization_request> &oai_move_project_to_a_different_organization_request) {
    QString fullPath = QString(_serverConfigs["move_project_to_a_different_organization"][_serverIndices.value("move_project_to_a_different_organization")].URL()+"/org/{orgId}/project/{projectId}/move");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_move_project_to_a_different_organization_request.hasValue()){

        
        QByteArray output = oai_move_project_to_a_different_organization_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::move_project_to_a_different_organizationCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::move_project_to_a_different_organizationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT move_project_to_a_different_organizationSignal();
        Q_EMIT move_project_to_a_different_organizationSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT move_project_to_a_different_organizationSignalE(error_type, error_str);
        Q_EMIT move_project_to_a_different_organizationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT move_project_to_a_different_organizationSignalError(error_type, error_str);
        Q_EMIT move_project_to_a_different_organizationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::remove_a_tag_from_a_project(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIAdd_a_tag_to_a_project_request> &oai_add_a_tag_to_a_project_request) {
    QString fullPath = QString(_serverConfigs["remove_a_tag_from_a_project"][_serverIndices.value("remove_a_tag_from_a_project")].URL()+"/org/{orgId}/project/{projectId}/tags/remove");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_add_a_tag_to_a_project_request.hasValue()){

        
        QByteArray output = oai_add_a_tag_to_a_project_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::remove_a_tag_from_a_projectCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::remove_a_tag_from_a_projectCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAdd_a_tag_to_a_project_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT remove_a_tag_from_a_projectSignal(output);
        Q_EMIT remove_a_tag_from_a_projectSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT remove_a_tag_from_a_projectSignalE(output, error_type, error_str);
        Q_EMIT remove_a_tag_from_a_projectSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT remove_a_tag_from_a_projectSignalError(output, error_type, error_str);
        Q_EMIT remove_a_tag_from_a_projectSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::replace_ignores(const QString &org_id, const QString &project_id, const QString &issue_id) {
    QString fullPath = QString(_serverConfigs["replace_ignores"][_serverIndices.value("replace_ignores")].URL()+"/org/{orgId}/project/{projectId}/ignore/{issueId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::replace_ignoresCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::replace_ignoresCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<QJsonValue> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        QJsonValue val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT replace_ignoresSignal(output);
        Q_EMIT replace_ignoresSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT replace_ignoresSignalE(output, error_type, error_str);
        Q_EMIT replace_ignoresSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT replace_ignoresSignalError(output, error_type, error_str);
        Q_EMIT replace_ignoresSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::retrieve_a_single_project(const QString &org_id, const QString &project_id) {
    QString fullPath = QString(_serverConfigs["retrieve_a_single_project"][_serverIndices.value("retrieve_a_single_project")].URL()+"/org/{orgId}/project/{projectId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::retrieve_a_single_projectCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::retrieve_a_single_projectCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIRetrieve_a_single_project_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT retrieve_a_single_projectSignal(output);
        Q_EMIT retrieve_a_single_projectSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT retrieve_a_single_projectSignalE(output, error_type, error_str);
        Q_EMIT retrieve_a_single_projectSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT retrieve_a_single_projectSignalError(output, error_type, error_str);
        Q_EMIT retrieve_a_single_projectSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::retrieve_ignore(const QString &org_id, const QString &project_id, const QString &issue_id) {
    QString fullPath = QString(_serverConfigs["retrieve_ignore"][_serverIndices.value("retrieve_ignore")].URL()+"/org/{orgId}/project/{projectId}/ignore/{issueId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    
    {
        QString issue_idPathParam("{");
        issue_idPathParam.append("issueId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "issueId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"issueId"+pathSuffix : pathPrefix;
        fullPath.replace(issue_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(issue_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::retrieve_ignoreCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::retrieve_ignoreCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT retrieve_ignoreSignal(output);
        Q_EMIT retrieve_ignoreSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT retrieve_ignoreSignalE(output, error_type, error_str);
        Q_EMIT retrieve_ignoreSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT retrieve_ignoreSignalError(output, error_type, error_str);
        Q_EMIT retrieve_ignoreSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::update_a_project(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIUpdate_a_project_request> &oai_update_a_project_request) {
    QString fullPath = QString(_serverConfigs["update_a_project"][_serverIndices.value("update_a_project")].URL()+"/org/{orgId}/project/{projectId}");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_update_a_project_request.hasValue()){

        
        QByteArray output = oai_update_a_project_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::update_a_projectCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::update_a_projectCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIRetrieve_a_single_project_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT update_a_projectSignal(output);
        Q_EMIT update_a_projectSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT update_a_projectSignalE(output, error_type, error_str);
        Q_EMIT update_a_projectSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT update_a_projectSignalError(output, error_type, error_str);
        Q_EMIT update_a_projectSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::update_project_settings(const QString &org_id, const QString &project_id, const ::OpenAPI::OptionalParam<OAIUpdate_project_settings_request> &oai_update_project_settings_request) {
    QString fullPath = QString(_serverConfigs["update_project_settings"][_serverIndices.value("update_project_settings")].URL()+"/org/{orgId}/project/{projectId}/settings");
    
    
    {
        QString org_idPathParam("{");
        org_idPathParam.append("orgId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orgId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orgId"+pathSuffix : pathPrefix;
        fullPath.replace(org_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(org_id)));
    }
    
    {
        QString project_idPathParam("{");
        project_idPathParam.append("projectId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "projectId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"projectId"+pathSuffix : pathPrefix;
        fullPath.replace(project_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(project_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_update_project_settings_request.hasValue()){

        
        QByteArray output = oai_update_project_settings_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProjectsApi::update_project_settingsCallback);
    connect(this, &OAIProjectsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProjectsApi::update_project_settingsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIList_project_settings_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT update_project_settingsSignal(output);
        Q_EMIT update_project_settingsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT update_project_settingsSignalE(output, error_type, error_str);
        Q_EMIT update_project_settingsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT update_project_settingsSignalError(output, error_type, error_str);
        Q_EMIT update_project_settingsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProjectsApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
