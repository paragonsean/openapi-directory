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

#include "OAIGet_list_of_issues_200_response_results_inner_issue.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGet_list_of_issues_200_response_results_inner_issue::OAIGet_list_of_issues_200_response_results_inner_issue(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGet_list_of_issues_200_response_results_inner_issue::OAIGet_list_of_issues_200_response_results_inner_issue() {
    this->initializeModel();
}

OAIGet_list_of_issues_200_response_results_inner_issue::~OAIGet_list_of_issues_200_response_results_inner_issue() {}

void OAIGet_list_of_issues_200_response_results_inner_issue::initializeModel() {

    m_cvssv3_isSet = false;
    m_cvssv3_isValid = false;

    m_credit_isSet = false;
    m_credit_isValid = false;

    m_cvss_score_isSet = false;
    m_cvss_score_isValid = false;

    m_disclosure_time_isSet = false;
    m_disclosure_time_isValid = false;

    m_exploit_maturity_isSet = false;
    m_exploit_maturity_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_identifiers_isSet = false;
    m_identifiers_isValid = false;

    m_ignored_isSet = false;
    m_ignored_isValid = false;

    m_is_ignored_isSet = false;
    m_is_ignored_isValid = false;

    m_is_patchable_isSet = false;
    m_is_patchable_isValid = false;

    m_is_patched_isSet = false;
    m_is_patched_isValid = false;

    m_is_pinnable_isSet = false;
    m_is_pinnable_isValid = false;

    m_is_upgradable_isSet = false;
    m_is_upgradable_isValid = false;

    m_jira_issue_url_isSet = false;
    m_jira_issue_url_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_original_severity_isSet = false;
    m_original_severity_isValid = false;

    m_package_isSet = false;
    m_package_isValid = false;

    m_package_manager_isSet = false;
    m_package_manager_isValid = false;

    m_patches_isSet = false;
    m_patches_isValid = false;

    m_priority_score_isSet = false;
    m_priority_score_isValid = false;

    m_publication_time_isSet = false;
    m_publication_time_isValid = false;

    m_semver_isSet = false;
    m_semver_isValid = false;

    m_severity_isSet = false;
    m_severity_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_unique_severities_list_isSet = false;
    m_unique_severities_list_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIGet_list_of_issues_200_response_results_inner_issue::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGet_list_of_issues_200_response_results_inner_issue::fromJsonObject(QJsonObject json) {

    m_cvssv3_isValid = ::OpenAPI::fromJsonValue(m_cvssv3, json[QString("CVSSv3")]);
    m_cvssv3_isSet = !json[QString("CVSSv3")].isNull() && m_cvssv3_isValid;

    m_credit_isValid = ::OpenAPI::fromJsonValue(m_credit, json[QString("credit")]);
    m_credit_isSet = !json[QString("credit")].isNull() && m_credit_isValid;

    m_cvss_score_isValid = ::OpenAPI::fromJsonValue(m_cvss_score, json[QString("cvssScore")]);
    m_cvss_score_isSet = !json[QString("cvssScore")].isNull() && m_cvss_score_isValid;

    m_disclosure_time_isValid = ::OpenAPI::fromJsonValue(m_disclosure_time, json[QString("disclosureTime")]);
    m_disclosure_time_isSet = !json[QString("disclosureTime")].isNull() && m_disclosure_time_isValid;

    m_exploit_maturity_isValid = ::OpenAPI::fromJsonValue(m_exploit_maturity, json[QString("exploitMaturity")]);
    m_exploit_maturity_isSet = !json[QString("exploitMaturity")].isNull() && m_exploit_maturity_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_identifiers_isValid = ::OpenAPI::fromJsonValue(m_identifiers, json[QString("identifiers")]);
    m_identifiers_isSet = !json[QString("identifiers")].isNull() && m_identifiers_isValid;

    m_ignored_isValid = ::OpenAPI::fromJsonValue(m_ignored, json[QString("ignored")]);
    m_ignored_isSet = !json[QString("ignored")].isNull() && m_ignored_isValid;

    m_is_ignored_isValid = ::OpenAPI::fromJsonValue(m_is_ignored, json[QString("isIgnored")]);
    m_is_ignored_isSet = !json[QString("isIgnored")].isNull() && m_is_ignored_isValid;

    m_is_patchable_isValid = ::OpenAPI::fromJsonValue(m_is_patchable, json[QString("isPatchable")]);
    m_is_patchable_isSet = !json[QString("isPatchable")].isNull() && m_is_patchable_isValid;

    m_is_patched_isValid = ::OpenAPI::fromJsonValue(m_is_patched, json[QString("isPatched")]);
    m_is_patched_isSet = !json[QString("isPatched")].isNull() && m_is_patched_isValid;

    m_is_pinnable_isValid = ::OpenAPI::fromJsonValue(m_is_pinnable, json[QString("isPinnable")]);
    m_is_pinnable_isSet = !json[QString("isPinnable")].isNull() && m_is_pinnable_isValid;

    m_is_upgradable_isValid = ::OpenAPI::fromJsonValue(m_is_upgradable, json[QString("isUpgradable")]);
    m_is_upgradable_isSet = !json[QString("isUpgradable")].isNull() && m_is_upgradable_isValid;

    m_jira_issue_url_isValid = ::OpenAPI::fromJsonValue(m_jira_issue_url, json[QString("jiraIssueUrl")]);
    m_jira_issue_url_isSet = !json[QString("jiraIssueUrl")].isNull() && m_jira_issue_url_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_original_severity_isValid = ::OpenAPI::fromJsonValue(m_original_severity, json[QString("originalSeverity")]);
    m_original_severity_isSet = !json[QString("originalSeverity")].isNull() && m_original_severity_isValid;

    m_package_isValid = ::OpenAPI::fromJsonValue(m_package, json[QString("package")]);
    m_package_isSet = !json[QString("package")].isNull() && m_package_isValid;

    m_package_manager_isValid = ::OpenAPI::fromJsonValue(m_package_manager, json[QString("packageManager")]);
    m_package_manager_isSet = !json[QString("packageManager")].isNull() && m_package_manager_isValid;

    m_patches_isValid = ::OpenAPI::fromJsonValue(m_patches, json[QString("patches")]);
    m_patches_isSet = !json[QString("patches")].isNull() && m_patches_isValid;

    m_priority_score_isValid = ::OpenAPI::fromJsonValue(m_priority_score, json[QString("priorityScore")]);
    m_priority_score_isSet = !json[QString("priorityScore")].isNull() && m_priority_score_isValid;

    m_publication_time_isValid = ::OpenAPI::fromJsonValue(m_publication_time, json[QString("publicationTime")]);
    m_publication_time_isSet = !json[QString("publicationTime")].isNull() && m_publication_time_isValid;

    m_semver_isValid = ::OpenAPI::fromJsonValue(m_semver, json[QString("semver")]);
    m_semver_isSet = !json[QString("semver")].isNull() && m_semver_isValid;

    m_severity_isValid = ::OpenAPI::fromJsonValue(m_severity, json[QString("severity")]);
    m_severity_isSet = !json[QString("severity")].isNull() && m_severity_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_unique_severities_list_isValid = ::OpenAPI::fromJsonValue(m_unique_severities_list, json[QString("uniqueSeveritiesList")]);
    m_unique_severities_list_isSet = !json[QString("uniqueSeveritiesList")].isNull() && m_unique_severities_list_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGet_list_of_issues_200_response_results_inner_issue::asJsonObject() const {
    QJsonObject obj;
    if (m_cvssv3_isSet) {
        obj.insert(QString("CVSSv3"), ::OpenAPI::toJsonValue(m_cvssv3));
    }
    if (m_credit.size() > 0) {
        obj.insert(QString("credit"), ::OpenAPI::toJsonValue(m_credit));
    }
    if (m_cvss_score_isSet) {
        obj.insert(QString("cvssScore"), ::OpenAPI::toJsonValue(m_cvss_score));
    }
    if (m_disclosure_time_isSet) {
        obj.insert(QString("disclosureTime"), ::OpenAPI::toJsonValue(m_disclosure_time));
    }
    if (m_exploit_maturity_isSet) {
        obj.insert(QString("exploitMaturity"), ::OpenAPI::toJsonValue(m_exploit_maturity));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_identifiers.isSet()) {
        obj.insert(QString("identifiers"), ::OpenAPI::toJsonValue(m_identifiers));
    }
    if (m_ignored.size() > 0) {
        obj.insert(QString("ignored"), ::OpenAPI::toJsonValue(m_ignored));
    }
    if (m_is_ignored_isSet) {
        obj.insert(QString("isIgnored"), ::OpenAPI::toJsonValue(m_is_ignored));
    }
    if (m_is_patchable_isSet) {
        obj.insert(QString("isPatchable"), ::OpenAPI::toJsonValue(m_is_patchable));
    }
    if (m_is_patched_isSet) {
        obj.insert(QString("isPatched"), ::OpenAPI::toJsonValue(m_is_patched));
    }
    if (m_is_pinnable_isSet) {
        obj.insert(QString("isPinnable"), ::OpenAPI::toJsonValue(m_is_pinnable));
    }
    if (m_is_upgradable_isSet) {
        obj.insert(QString("isUpgradable"), ::OpenAPI::toJsonValue(m_is_upgradable));
    }
    if (m_jira_issue_url_isSet) {
        obj.insert(QString("jiraIssueUrl"), ::OpenAPI::toJsonValue(m_jira_issue_url));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_original_severity_isSet) {
        obj.insert(QString("originalSeverity"), ::OpenAPI::toJsonValue(m_original_severity));
    }
    if (m_package_isSet) {
        obj.insert(QString("package"), ::OpenAPI::toJsonValue(m_package));
    }
    if (m_package_manager_isSet) {
        obj.insert(QString("packageManager"), ::OpenAPI::toJsonValue(m_package_manager));
    }
    if (m_patches.size() > 0) {
        obj.insert(QString("patches"), ::OpenAPI::toJsonValue(m_patches));
    }
    if (m_priority_score_isSet) {
        obj.insert(QString("priorityScore"), ::OpenAPI::toJsonValue(m_priority_score));
    }
    if (m_publication_time_isSet) {
        obj.insert(QString("publicationTime"), ::OpenAPI::toJsonValue(m_publication_time));
    }
    if (m_semver.isSet()) {
        obj.insert(QString("semver"), ::OpenAPI::toJsonValue(m_semver));
    }
    if (m_severity_isSet) {
        obj.insert(QString("severity"), ::OpenAPI::toJsonValue(m_severity));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_unique_severities_list.size() > 0) {
        obj.insert(QString("uniqueSeveritiesList"), ::OpenAPI::toJsonValue(m_unique_severities_list));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getCvssv3() const {
    return m_cvssv3;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setCvssv3(const QString &cvssv3) {
    m_cvssv3 = cvssv3;
    m_cvssv3_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_cvssv3_Set() const{
    return m_cvssv3_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_cvssv3_Valid() const{
    return m_cvssv3_isValid;
}

QList<QJsonValue> OAIGet_list_of_issues_200_response_results_inner_issue::getCredit() const {
    return m_credit;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setCredit(const QList<QJsonValue> &credit) {
    m_credit = credit;
    m_credit_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_credit_Set() const{
    return m_credit_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_credit_Valid() const{
    return m_credit_isValid;
}

double OAIGet_list_of_issues_200_response_results_inner_issue::getCvssScore() const {
    return m_cvss_score;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setCvssScore(const double &cvss_score) {
    m_cvss_score = cvss_score;
    m_cvss_score_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_cvss_score_Set() const{
    return m_cvss_score_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_cvss_score_Valid() const{
    return m_cvss_score_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getDisclosureTime() const {
    return m_disclosure_time;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setDisclosureTime(const QString &disclosure_time) {
    m_disclosure_time = disclosure_time;
    m_disclosure_time_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_disclosure_time_Set() const{
    return m_disclosure_time_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_disclosure_time_Valid() const{
    return m_disclosure_time_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getExploitMaturity() const {
    return m_exploit_maturity;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setExploitMaturity(const QString &exploit_maturity) {
    m_exploit_maturity = exploit_maturity;
    m_exploit_maturity_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_exploit_maturity_Set() const{
    return m_exploit_maturity_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_exploit_maturity_Valid() const{
    return m_exploit_maturity_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getId() const {
    return m_id;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_id_Valid() const{
    return m_id_isValid;
}

OAIGet_list_of_issues_200_response_results_inner_issue_identifiers OAIGet_list_of_issues_200_response_results_inner_issue::getIdentifiers() const {
    return m_identifiers;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIdentifiers(const OAIGet_list_of_issues_200_response_results_inner_issue_identifiers &identifiers) {
    m_identifiers = identifiers;
    m_identifiers_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_identifiers_Set() const{
    return m_identifiers_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_identifiers_Valid() const{
    return m_identifiers_isValid;
}

QList<QJsonValue> OAIGet_list_of_issues_200_response_results_inner_issue::getIgnored() const {
    return m_ignored;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIgnored(const QList<QJsonValue> &ignored) {
    m_ignored = ignored;
    m_ignored_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_ignored_Set() const{
    return m_ignored_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_ignored_Valid() const{
    return m_ignored_isValid;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isIsIgnored() const {
    return m_is_ignored;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIsIgnored(const bool &is_ignored) {
    m_is_ignored = is_ignored;
    m_is_ignored_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_ignored_Set() const{
    return m_is_ignored_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_ignored_Valid() const{
    return m_is_ignored_isValid;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isIsPatchable() const {
    return m_is_patchable;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIsPatchable(const bool &is_patchable) {
    m_is_patchable = is_patchable;
    m_is_patchable_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_patchable_Set() const{
    return m_is_patchable_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_patchable_Valid() const{
    return m_is_patchable_isValid;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isIsPatched() const {
    return m_is_patched;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIsPatched(const bool &is_patched) {
    m_is_patched = is_patched;
    m_is_patched_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_patched_Set() const{
    return m_is_patched_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_patched_Valid() const{
    return m_is_patched_isValid;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isIsPinnable() const {
    return m_is_pinnable;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIsPinnable(const bool &is_pinnable) {
    m_is_pinnable = is_pinnable;
    m_is_pinnable_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_pinnable_Set() const{
    return m_is_pinnable_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_pinnable_Valid() const{
    return m_is_pinnable_isValid;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isIsUpgradable() const {
    return m_is_upgradable;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setIsUpgradable(const bool &is_upgradable) {
    m_is_upgradable = is_upgradable;
    m_is_upgradable_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_upgradable_Set() const{
    return m_is_upgradable_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_is_upgradable_Valid() const{
    return m_is_upgradable_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getJiraIssueUrl() const {
    return m_jira_issue_url;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setJiraIssueUrl(const QString &jira_issue_url) {
    m_jira_issue_url = jira_issue_url;
    m_jira_issue_url_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_jira_issue_url_Set() const{
    return m_jira_issue_url_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_jira_issue_url_Valid() const{
    return m_jira_issue_url_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getLanguage() const {
    return m_language;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_language_Set() const{
    return m_language_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_language_Valid() const{
    return m_language_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getOriginalSeverity() const {
    return m_original_severity;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setOriginalSeverity(const QString &original_severity) {
    m_original_severity = original_severity;
    m_original_severity_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_original_severity_Set() const{
    return m_original_severity_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_original_severity_Valid() const{
    return m_original_severity_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getPackage() const {
    return m_package;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setPackage(const QString &package) {
    m_package = package;
    m_package_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_package_Set() const{
    return m_package_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_package_Valid() const{
    return m_package_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getPackageManager() const {
    return m_package_manager;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setPackageManager(const QString &package_manager) {
    m_package_manager = package_manager;
    m_package_manager_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_package_manager_Set() const{
    return m_package_manager_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_package_manager_Valid() const{
    return m_package_manager_isValid;
}

QList<QJsonValue> OAIGet_list_of_issues_200_response_results_inner_issue::getPatches() const {
    return m_patches;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setPatches(const QList<QJsonValue> &patches) {
    m_patches = patches;
    m_patches_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_patches_Set() const{
    return m_patches_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_patches_Valid() const{
    return m_patches_isValid;
}

double OAIGet_list_of_issues_200_response_results_inner_issue::getPriorityScore() const {
    return m_priority_score;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setPriorityScore(const double &priority_score) {
    m_priority_score = priority_score;
    m_priority_score_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_priority_score_Set() const{
    return m_priority_score_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_priority_score_Valid() const{
    return m_priority_score_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getPublicationTime() const {
    return m_publication_time;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setPublicationTime(const QString &publication_time) {
    m_publication_time = publication_time;
    m_publication_time_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_publication_time_Set() const{
    return m_publication_time_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_publication_time_Valid() const{
    return m_publication_time_isValid;
}

OAIGet_list_of_issues_200_response_results_inner_issue_semver OAIGet_list_of_issues_200_response_results_inner_issue::getSemver() const {
    return m_semver;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setSemver(const OAIGet_list_of_issues_200_response_results_inner_issue_semver &semver) {
    m_semver = semver;
    m_semver_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_semver_Set() const{
    return m_semver_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_semver_Valid() const{
    return m_semver_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getSeverity() const {
    return m_severity;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setSeverity(const QString &severity) {
    m_severity = severity;
    m_severity_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_severity_Set() const{
    return m_severity_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_severity_Valid() const{
    return m_severity_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getTitle() const {
    return m_title;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_title_Set() const{
    return m_title_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getType() const {
    return m_type;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_type_Valid() const{
    return m_type_isValid;
}

QList<QJsonValue> OAIGet_list_of_issues_200_response_results_inner_issue::getUniqueSeveritiesList() const {
    return m_unique_severities_list;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setUniqueSeveritiesList(const QList<QJsonValue> &unique_severities_list) {
    m_unique_severities_list = unique_severities_list;
    m_unique_severities_list_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_unique_severities_list_Set() const{
    return m_unique_severities_list_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_unique_severities_list_Valid() const{
    return m_unique_severities_list_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getUrl() const {
    return m_url;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_url_Set() const{
    return m_url_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIGet_list_of_issues_200_response_results_inner_issue::getVersion() const {
    return m_version;
}
void OAIGet_list_of_issues_200_response_results_inner_issue::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_version_Set() const{
    return m_version_isSet;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cvssv3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credit.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_cvss_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disclosure_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exploit_maturity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifiers.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ignored.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_ignored_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_patchable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_patched_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_pinnable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_upgradable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_jira_issue_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_severity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_manager_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patches.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publication_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_semver.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_severity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unique_severities_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGet_list_of_issues_200_response_results_inner_issue::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_exploit_maturity_isValid && m_id_isValid && m_original_severity_isValid && m_package_isValid && m_severity_isValid && m_title_isValid && m_type_isValid && m_url_isValid && m_version_isValid && true;
}

} // namespace OpenAPI
