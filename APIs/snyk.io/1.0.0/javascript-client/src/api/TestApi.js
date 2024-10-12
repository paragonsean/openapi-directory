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


import ApiClient from "../ApiClient";
import TestComposerJsonComposerLockFileRequest from '../model/TestComposerJsonComposerLockFileRequest';
import TestDepGraphRequest from '../model/TestDepGraphRequest';
import TestGemfileLockFileRequest from '../model/TestGemfileLockFileRequest';
import TestGopkgTomlGopkgLockFileRequest from '../model/TestGopkgTomlGopkgLockFileRequest';
import TestGradleFileRequest from '../model/TestGradleFileRequest';
import TestMavenFileRequest from '../model/TestMavenFileRequest';
import TestPackageJsonPackageLockJsonFileRequest from '../model/TestPackageJsonPackageLockJsonFileRequest';
import TestPackageJsonYarnLockFileRequest from '../model/TestPackageJsonYarnLockFileRequest';
import TestRequirementsTxtFileRequest from '../model/TestRequirementsTxtFileRequest';
import TestSbtFileRequest from '../model/TestSbtFileRequest';
import TestVendorJsonFileRequest from '../model/TestVendorJsonFileRequest';

/**
* Test service.
* @module api/TestApi
* @version 1.0.0
*/
export default class TestApi {

    /**
    * Constructs a new TestApi. 
    * @alias module:api/TestApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the testComposerJsonComposerLockFile operation.
     * @callback module:api/TestApi~testComposerJsonComposerLockFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test composer.json & composer.lock file
     * You can test your Composer packages for issues according to their manifest file & lockfile using this action. It takes a JSON object containing a \"target\" `composer.json` and a `composer.lock`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestComposerJsonComposerLockFileRequest} [testComposerJsonComposerLockFileRequest] 
     * @param {module:api/TestApi~testComposerJsonComposerLockFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testComposerJsonComposerLockFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testComposerJsonComposerLockFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/composer', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testDepGraph operation.
     * @callback module:api/TestApi~testDepGraphCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test Dep Graph
     * Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {module:model/TestDepGraphRequest} [testDepGraphRequest] 
     * @param {module:api/TestApi~testDepGraphCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testDepGraph(opts, callback) {
      opts = opts || {};
      let postBody = opts['testDepGraphRequest'];

      let pathParams = {
      };
      let queryParams = {
        'org': opts['org']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/dep-graph', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testForIssuesInAPublicGemByNameAndVersion operation.
     * @callback module:api/TestApi~testForIssuesInAPublicGemByNameAndVersionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test for issues in a public gem by name and version
     * You can test `rubygems` packages for issues according to their name and version.
     * @param {String} gemName The gem name.
     * @param {String} version The gem version to test.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {module:api/TestApi~testForIssuesInAPublicGemByNameAndVersionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testForIssuesInAPublicGemByNameAndVersion(gemName, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'gemName' is set
      if (gemName === undefined || gemName === null) {
        throw new Error("Missing the required parameter 'gemName' when calling testForIssuesInAPublicGemByNameAndVersion");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling testForIssuesInAPublicGemByNameAndVersion");
      }

      let pathParams = {
        'gemName': gemName,
        'version': version
      };
      let queryParams = {
        'org': opts['org']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/rubygems/{gemName}/{version}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion operation.
     * @callback module:api/TestApi~testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test for issues in a public package by group id, artifact id and version
     * You can test `maven` packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the `repository` query parameter).
     * @param {String} groupId The package's group ID.
     * @param {String} artifactId The package's artifact ID.
     * @param {String} version The package version to test.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {String} [repository] The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
     * @param {module:api/TestApi~testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(groupId, artifactId, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion");
      }
      // verify the required parameter 'artifactId' is set
      if (artifactId === undefined || artifactId === null) {
        throw new Error("Missing the required parameter 'artifactId' when calling testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion");
      }

      let pathParams = {
        'groupId': groupId,
        'artifactId': artifactId,
        'version': version
      };
      let queryParams = {
        'org': opts['org'],
        'repository': opts['repository']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/maven/{groupId}/{artifactId}/{version}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testForIssuesInAPublicPackageByGroupNameAndVersion operation.
     * @callback module:api/TestApi~testForIssuesInAPublicPackageByGroupNameAndVersionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test for issues in a public package by group, name and version
     * You can test `gradle` packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \"Maven\" above for details.
     * @param {String} group The package's group ID.
     * @param {String} name The package's artifact ID.
     * @param {String} version The package version to test.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {String} [repository] The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
     * @param {module:api/TestApi~testForIssuesInAPublicPackageByGroupNameAndVersionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testForIssuesInAPublicPackageByGroupNameAndVersion(group, name, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'group' is set
      if (group === undefined || group === null) {
        throw new Error("Missing the required parameter 'group' when calling testForIssuesInAPublicPackageByGroupNameAndVersion");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling testForIssuesInAPublicPackageByGroupNameAndVersion");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling testForIssuesInAPublicPackageByGroupNameAndVersion");
      }

      let pathParams = {
        'group': group,
        'name': name,
        'version': version
      };
      let queryParams = {
        'org': opts['org'],
        'repository': opts['repository']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/gradle/{group}/{name}/{version}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testForIssuesInAPublicPackageByNameAndVersion operation.
     * @callback module:api/TestApi~testForIssuesInAPublicPackageByNameAndVersionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test for issues in a public package by name and version
     * You can test `npm` packages for issues according to their name and version.
     * @param {String} packageName The package name. For scoped packages, **must** be url-encoded, so to test \"@angular/core\" version 4.3.2, one should `GET /test/npm/%40angular%2Fcore/4.3.2`.
     * @param {String} version The Package version to test.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {module:api/TestApi~testForIssuesInAPublicPackageByNameAndVersionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testForIssuesInAPublicPackageByNameAndVersion(packageName, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'packageName' is set
      if (packageName === undefined || packageName === null) {
        throw new Error("Missing the required parameter 'packageName' when calling testForIssuesInAPublicPackageByNameAndVersion");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling testForIssuesInAPublicPackageByNameAndVersion");
      }

      let pathParams = {
        'packageName': packageName,
        'version': version
      };
      let queryParams = {
        'org': opts['org']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/npm/{packageName}/{version}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testGemfileLockFile operation.
     * @callback module:api/TestApi~testGemfileLockFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test gemfile.lock file
     * You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \"target\" `Gemfile.lock`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestGemfileLockFileRequest} [testGemfileLockFileRequest] 
     * @param {module:api/TestApi~testGemfileLockFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testGemfileLockFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testGemfileLockFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/rubygems', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testGopkgTomlGopkgLockFile operation.
     * @callback module:api/TestApi~testGopkgTomlGopkgLockFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test Gopkg.toml & Gopkg.lock File
     * You can test your Go dep packages for issues according to their manifest file & lockfile using this action. It takes a JSON object containing a \"target\" `Gopkg.toml` and a `Gopkg.lock`.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {module:model/TestGopkgTomlGopkgLockFileRequest} [testGopkgTomlGopkgLockFileRequest] 
     * @param {module:api/TestApi~testGopkgTomlGopkgLockFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testGopkgTomlGopkgLockFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testGopkgTomlGopkgLockFileRequest'];

      let pathParams = {
      };
      let queryParams = {
        'org': opts['org']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/golangdep', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testGradleFile operation.
     * @callback module:api/TestApi~testGradleFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test gradle file
     * You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \"target\" `build.gradle`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestGradleFileRequest} [testGradleFileRequest] 
     * @param {module:api/TestApi~testGradleFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testGradleFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testGradleFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/gradle', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testMavenFile operation.
     * @callback module:api/TestApi~testMavenFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test maven file
     * You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \"target\" `pom.xml`.  Additional manifest files, if they are needed, like parent `pom.xml` files, child poms, etc., according the the definitions in the target `pom.xml` file, should be supplied in the `additional` body parameter.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {String} [repository] The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
     * @param {module:model/TestMavenFileRequest} [testMavenFileRequest] 
     * @param {module:api/TestApi~testMavenFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testMavenFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testMavenFileRequest'];

      let pathParams = {
      };
      let queryParams = {
        'org': opts['org'],
        'repository': opts['repository']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/maven', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testPackageJsonPackageLockJsonFile operation.
     * @callback module:api/TestApi~testPackageJsonPackageLockJsonFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test package.json & package-lock.json File
     * You can test your npm packages for issues according to their manifest file & optional lockfile using this action. It takes a JSON object containing a \"target\" `package.json` and optionally a `package-lock.json`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestPackageJsonPackageLockJsonFileRequest} [testPackageJsonPackageLockJsonFileRequest] 
     * @param {module:api/TestApi~testPackageJsonPackageLockJsonFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testPackageJsonPackageLockJsonFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testPackageJsonPackageLockJsonFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/npm', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testPackageJsonYarnLockFile operation.
     * @callback module:api/TestApi~testPackageJsonYarnLockFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test package.json & yarn.lock File
     * You can test your yarn packages for issues according to their manifest file & lockfile using this action. It takes a JSON object containing a \"target\" `package.json` and a `yarn.lock`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestPackageJsonYarnLockFileRequest} [testPackageJsonYarnLockFileRequest] 
     * @param {module:api/TestApi~testPackageJsonYarnLockFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testPackageJsonYarnLockFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testPackageJsonYarnLockFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/yarn', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testPipPackageNameVersionGet operation.
     * @callback module:api/TestApi~testPipPackageNameVersionGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test for issues in a public package by name and version
     * You can test `pip` packages for issues according to their name and version.
     * @param {String} packageName The package name.
     * @param {String} version The Package version to test.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {module:api/TestApi~testPipPackageNameVersionGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testPipPackageNameVersionGet(packageName, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'packageName' is set
      if (packageName === undefined || packageName === null) {
        throw new Error("Missing the required parameter 'packageName' when calling testPipPackageNameVersionGet");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling testPipPackageNameVersionGet");
      }

      let pathParams = {
        'packageName': packageName,
        'version': version
      };
      let queryParams = {
        'org': opts['org']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/pip/{packageName}/{version}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testRequirementsTxtFile operation.
     * @callback module:api/TestApi~testRequirementsTxtFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test requirements.txt file
     * You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \"target\" `requirements.txt`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestRequirementsTxtFileRequest} [testRequirementsTxtFileRequest] 
     * @param {module:api/TestApi~testRequirementsTxtFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testRequirementsTxtFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testRequirementsTxtFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/pip', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testSbtFile operation.
     * @callback module:api/TestApi~testSbtFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test sbt file
     * You can test your `sbt` packages for issues according to their manifest file using this action. It takes a JSON object containing a the \"target\" `build.sbt`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestSbtFileRequest} [testSbtFileRequest] 
     * @param {module:api/TestApi~testSbtFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testSbtFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testSbtFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/sbt', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testSbtGroupIdArtifactIdVersionGet operation.
     * @callback module:api/TestApi~testSbtGroupIdArtifactIdVersionGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test for issues in a public package by group id, artifact id and version
     * You can test `sbt` packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \"Maven\" above for details.
     * @param {String} groupId The package's group ID.
     * @param {String} artifactId The package's artifact ID.
     * @param {String} version The package version to test.
     * @param {Object} opts Optional parameters
     * @param {String} [org] The organization to test the package with. See \"The Snyk organization for a request\" above.
     * @param {String} [repository] The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
     * @param {module:api/TestApi~testSbtGroupIdArtifactIdVersionGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testSbtGroupIdArtifactIdVersionGet(groupId, artifactId, version, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'groupId' is set
      if (groupId === undefined || groupId === null) {
        throw new Error("Missing the required parameter 'groupId' when calling testSbtGroupIdArtifactIdVersionGet");
      }
      // verify the required parameter 'artifactId' is set
      if (artifactId === undefined || artifactId === null) {
        throw new Error("Missing the required parameter 'artifactId' when calling testSbtGroupIdArtifactIdVersionGet");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling testSbtGroupIdArtifactIdVersionGet");
      }

      let pathParams = {
        'groupId': groupId,
        'artifactId': artifactId,
        'version': version
      };
      let queryParams = {
        'org': opts['org'],
        'repository': opts['repository']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/sbt/{groupId}/{artifactId}/{version}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testVendorJsonFile operation.
     * @callback module:api/TestApi~testVendorJsonFileCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test vendor.json File
     * You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \"target\" `vendor.json`.
     * @param {Object} opts Optional parameters
     * @param {module:model/TestVendorJsonFileRequest} [testVendorJsonFileRequest] 
     * @param {module:api/TestApi~testVendorJsonFileCallback} callback The callback function, accepting three arguments: error, data, response
     */
    testVendorJsonFile(opts, callback) {
      opts = opts || {};
      let postBody = opts['testVendorJsonFileRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/test/govendor', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
