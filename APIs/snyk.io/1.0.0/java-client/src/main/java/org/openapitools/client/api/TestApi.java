/*
 * Snyk API
 * The Snyk API is available to customers on [Business and Enterprise plans](https://snyk.io/plans) and allows you to programatically integrate with Snyk.  ## REST API  We are in the process of building a new, improved API (`https://api.snyk.io/rest`) built using the OpenAPI and JSON API standards. We welcome you to try it out as we shape and release endpoints until it, ultimately, becomes a full replacement for our current API.  Looking for our REST API docs? Please head over to [https://apidocs.snyk.io](https://apidocs.snyk.io)  ## API vs CLI vs Snyk integration  The API detailed below has the ability to test a package for issues, as they are defined by Snyk. It is important to note that for many package managers, using this API will be less accurate than running the [Snyk CLI](https://snyk.io/docs/using-snyk) as part of your build pipe, or just using it locally on your package. The reason for this is that more than one package version fit the requirements given in manifest files. Running the CLI locally tests the actual deployed code, and has an accurate snapshot of the dependency versions in use, while the API can only infer it, with inferior accuracy. It should be noted that the Snyk CLI has the ability to output machine-readable JSON output (with the `--json` flag to `snyk test`).  A third option, is to allow Snyk access to your development flow via the existing [Snyk integrations](https://snyk.io/docs/). The advantage to this approach is having Snyk monitor every new pull request, and suggest fixes by opening new pull requests. This can be achieved either by integrating Snyk directly to your source code management (SCM) tool, or via a broker to allow greater security and auditability.  If those are not viable options, this API is your best choice.  ## API url  The base URL for all API endpoints is https://api.snyk.io/v1/  ## Authorization  To use this API, you must get your token from Snyk. It can be seen on https://snyk.io/account/ after you register with Snyk and login.  The token should be supplied in an `Authorization` header with the token, preceded by `token`:  ```http Authorization: token API_KEY ```  Otherwise, a 401 \"Unauthorized\" response will be returned.  ```http HTTP/1.1 401 Unauthorized          {             \"code\": 401,             \"error\": \"Not authorised\",             \"message\": \"Not authorised\"         } ```  ## Overview and entities  The API is a REST API. It has the following entities:  ### Test result  The test result is the object returned from the API giving the results of testing a package for issues. It has the following fields:  | Property        | Type    | Description                                           | Example                                                         | |----------------:|---------|-------------------------------------------------------|-----------------------------------------------------------------| | ok              | boolean | Does this package have one or more issues?             | false                                                           | | issues          | object  | The issues found. See below for details.              | See below                                                       | | dependencyCount | number  | The number of dependencies the package has.           | 9                                                               | | org             | object  | The organization this test was carried out for.       | {\"name\": \"anOrg\", \"id\": \"5d7013d9-2a57-4c89-993c-0304d960193c\"} | | licensesPolicy  | object  | The organization's licenses policy used for this test | See in the examples                                             | | packageManager  | string  | The package manager for this package                  | \"maven\"                                                         | |                 |         |                                                       |                                                                 |  ### Issue  An issue is either a vulnerability or a license issue, according to the organization's policy. It has the following fields:  | Property       | Type          | Description                                                                                                                | Example                                | |---------------:|---------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------| | id             | string        | The issue ID                                                                                                               | \"SNYK-JS-BACKBONE-10054\"               | | url            | string        | A link to the issue details on snyk.io                                                                                     | \"https://snyk.io/vuln/SNYK-JS-BACKBONE-10054 | | title          | string        | The issue title                                                                                                            | \"Cross Site Scripting\"                 | | type           | string        | The issue type: \"license\" or \"vulnerability\".                                                                              | \"license\"                              | | paths          | array         | The paths to the dependencies which have an issue, and their corresponding upgrade path (if an upgrade is available). [More information about from and upgrade paths](#introduction/overview-and-entities/from-and-upgrade-paths) | [<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;\"from\": [\"a@1.0.0\", \"b@4.8.1\"],<br>&nbsp;&nbsp;&nbsp;&nbsp;\"upgrade\": [false, \"b@4.8.2\"]<br>&nbsp;&nbsp;}<br>] | | package        | string        | The package identifier according to its package manager                                                                    | \"backbone\", \"org.apache.flex.blazeds:blazeds\"| | version        | string        | The package version this issue is applicable to.                                                                           | \"0.4.0\"                                | | severity       | string        | The Snyk defined severity level: \"critical\", \"high\", \"medium\" or \"low\".                                                    | \"high\"                                 | | language       | string        | The package's programming language                                                                                         | \"js\"                                   | | packageManager | string        | The package manager                                                                                                        | \"npm\"                                  | | semver         | array[string] OR map[string]array[string] | One or more [semver](https://semver.org) ranges this issue is applicable to. The format varies according to package manager. | [\"<0.5.0, >=0.4.0\", \"<0.3.8, >=0.3.6\"] OR { \"vulnerable\": [\"[2.0.0, 3.0.0)\"], \"unaffected\": [\"[1, 2)\", \"[3, )\"] } |  ### Vulnerability  A vulnerability in a package. In addition to all the fields present in an issue, a vulnerability also has these fields:  Property        | Type    | Description                                                                                                                                                                                                                      | Example                                        | ----------------:|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|  publicationTime | Date    | The vulnerability publication time                                                                                                                                                                                               | \"2016-02-11T07:16:18.857Z\"                     |  disclosureTime  | Date    | The time this vulnerability was originally disclosed to the package maintainers                                                                                                                                                   | \"2016-02-11T07:16:18.857Z\"                     |  isUpgradable    | boolean | Is this vulnerability fixable by upgrading a dependency?                                                                                                                                                                         | true                                           |  description     | string  | The detailed description of the vulnerability, why and how it is exploitable. Provided in markdown format. | \"## Overview\\n[`org.apache.logging.log4j:log4j-core`](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22log4j-core%22)\\nIn Apache Log4j 2.x before 2.8.2, when using the TCP socket server or UDP socket server to receive serialized log events from another application, a specially crafted binary payload can be sent that, when deserialized, can execute arbitrary code.\\n\\n# Details\\nSerialization is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. The reverse process of creating object from sequence of bytes is called deserialization. Serialization is commonly used for communication (sharing objects between multiple hosts) and persistence (store the object state in a file or a database). It is an integral part of popular protocols like _Remote Method Invocation (RMI)_, _Java Management Extension (JMX)_, _Java Messaging System (JMS)_, _Action Message Format (AMF)_, _Java Server Faces (JSF) ViewState_, etc.\\n\\n_Deserialization of untrusted data_ ([CWE-502](https://cwe.mitre.org/data/definitions/502.html)), is when the application deserializes untrusted data without sufficiently verifying that the resulting data will be valid, letting the attacker to control the state or the flow of the execution. \\n\\nJava deserialization issues have been known for years. However, interest in the issue intensified greatly in 2015, when classes that could be abused to achieve remote code execution were found in a [popular library (Apache Commons Collection)](https://snyk.io/vuln/SNYK-JAVA-COMMONSCOLLECTIONS-30078). These classes were used in zero-days affecting IBM WebSphere, Oracle WebLogic and many other products.\\n\\nAn attacker just needs to identify a piece of software that has both a vulnerable class on its path, and performs deserialization on untrusted data. Then all they need to do is send the payload into the deserializer, getting the command executed.\\n\\n> Developers put too much trust in Java Object Serialization. Some even de-serialize objects pre-authentication. When deserializing an Object in Java you typically cast it to an expected type, and therefore Java's strict type system will ensure you only get valid object trees. Unfortunately, by the time the type checking happens, platform code has already created and executed significant logic. So, before the final type is checked a lot of code is executed from the readObject() methods of various objects, all of which is out of the developer's control. By combining the readObject() methods of various classes which are available on the classpath of the vulnerable application an attacker can execute functions (including calling Runtime.exec() to execute local OS commands).\\n- Apache Blog\\n\\n\\n## References\\n- [NVD](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5645)\\n- [jira issue](https://issues.apache.org/jira/browse/LOG4J2-1863)\\n\" |  isPatchable     | boolean | Is this vulnerability fixable by using a Snyk supplied patch?                                                                                                                                                                    | true                                           |  isPinnable      | boolean | Is this vulnerability fixable by pinning a transitive dependency                                                                                                                                                                 | true                                           |  identifiers     | object  | Additional vulnerability identifiers                                                                                                                                                                                             | {\"CWE\": [], \"CVE\": [\"CVE-2016-2402]}           |  credit          | string  | The reporter of the vulnerability                                                                                                                                                                                                | \"Snyk Security Team\"                           |  CVSSv3          | string  | Common Vulnerability Scoring System (CVSS) provides a way to capture the principal characteristics of a vulnerability, and produce a numerical score reflecting its severity, as well as a textual representation of that score. | \"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N\" |  cvssScore       | number  | CVSS Score                                                                                                                                                                                                                       | 5.3                                            |  patches         | array   | Patches to fix this issue, by snyk                                                                                                                                                                                               | see \"Patch\" below.                             |  upgradePath     | object  | The path to upgrade this issue, if applicable                                                                                                                                                                                    | see below                                      |  isPatched       | boolean | Is this vulnerability patched?                                                                                                                                                                                                   | false                                          |  exploitMaturity | string  | The snyk exploit maturity level  #### Patch  A patch is an object like this one:  ```json {   \"urls\": [     \"https://snyk-patches.s3.amazonaws.com/npm/backbone/20110701/backbone_20110701_0_0_0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"   ],   \"version\": \"<0.5.0 >=0.3.3\",   \"modificationTime\": \"2015-11-06T02:09:36.180Z\",   \"comments\": [     \"https://github.com/jashkenas/backbone/commit/0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"   ],   \"id\": \"patch:npm:backbone:20110701:0\" } ```  ### From and upgrade paths  Both from and upgrade paths are arrays, where each item within the array is a package `name@version`.  Take the following `from` path:  ``` [   \"my-project@1.0.0\",   \"actionpack@4.2.5\",   \"rack@1.6.4\" ] ```  Assuming this was returned as a result of a test, then we know:  - The package that was tested was `my-project@1.0.0`  - The dependency with an issue was included in the tested package via the direct dependency `actionpack@4.2.5`  - The dependency with an issue was [rack@1.6.4](https://snyk.io/vuln/rubygems:rack@1.6.4)  Take the following `upgrade` path:  ``` [   false,   \"actionpack@5.0.0\",   \"rack@2.0.1\" ] ```  Assuming this was returned as a result of a test, then we know:  - The package that was tested is not upgradable (`false`)  - The direct dependency `actionpack` should be upgraded to at least version `5.0.0` in order to fix the issue  - Upgrading `actionpack` to version `5.0.0` will cause `rack` to be installed at version `2.0.1`  If the `upgrade` path comes back as an empty array (`[]`) then this means that there is no upgrade path available which would fix the issue.  ### License issue  A license issue has no additional fields other than the ones in \"Issue\".  ### Snyk organization  The organization in Snyk this request is applicable to. The organization determines the access rights, licenses policy and is the unit of billing for private projects.  A Snyk organization has these fields:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | name        | string | The organization display name | \"deelmaker\"                            | id          | string | The ID of the organization    | \"3ab0f8d3-b17d-4953-ab6d-e1cbfe1df385\" |  ## Errors  This is a beta release of this API. Therefore, despite our efforts, errors might occur. In the unlikely event of such an error, it will have the following structure as JSON in the body:  Property    | Type   | Description                   | Example                                | -----------:| ------ | ----------------------------- | -------------------------------------- | message     | string | Error message with reference  | Error calling Snyk api (reference: 39db46b1-ad57-47e6-a87d-e34f6968030b) | errorRef    | V4 uuid | An error ref to contact Snyk with | 39db46b1-ad57-47e6-a87d-e34f6968030b |  The error reference will also be supplied in the `x-error-reference` header in the server reply.  Example response:  ```http HTTP/1.1 500 Internal Server Error x-error-reference: a45ec9c1-065b-4f7b-baf8-dbd1552ffc9f Content-Type: application/json; charset=utf-8 Content-Length: 1848 Vary: Accept-Encoding Date: Sun, 10 Sep 2017 06:48:40 GMT ```  ## Rate Limiting  To ensure resilience against increasing request rates, we are starting to introduce rate-limiting. We are monitoring the rate-limiting system to ensure minimal impact on users while ensuring system stability. The limit is up to 2000 requests per minute, per user, subject to change. As such, we recommend calls to the API are throttled regardless of the current limit. All requests above the limit will get a response with status code `429` - `Too many requests` until requests stop for the duration of the rate-limiting interval (currently a minute).  ## Consuming Webhooks  Webhooks are delivered with a `Content-Type` of `application/json`, with the event payload as JSON in the request body. We also send the following headers:  - `X-Snyk-Event` - the name of the event  - `X-Snyk-Transport-ID` - a GUID to identify this delivery  - `X-Snyk-Timestamp` - an ISO 8601 timestamp for when the event occurred, for example: `2020-09-25T15:27:53Z`  - `X-Hub-Signature` - the HMAC hex digest of the request body, used to secure your webhooks and ensure the request did indeed come from Snyk  - `User-Agent` - identifies the origin of the request, for example: `Snyk-Webhooks/XXX`  ---  After your server is configured to receive payloads, it listens for any payload sent to the endpoint you configured. For security reasons, you should limit requests to those coming from Snyk.  ### Validating payloads  All transports sent to your webhooks have a `X-Hub-Signature` header, which contains the hash signature for the transport. The signature is a HMAC hexdigest of the request body, generated using sha256 and your `secret` as the HMAC key.  You could use a function in Node.JS such as the following to validate these signatures on incoming requests from Snyk:  ```javascript import * as crypto from 'crypto';  function verifySignature(request, secret) {   const hmac = crypto.createHmac('sha256', secret);   const buffer = JSON.stringify(request.body);   hmac.update(buffer, 'utf8');    const signature = `sha256=${hmac.digest('hex')}`;    return signature === request.headers['x-hub-signature']; } ```  ### Payload versioning  Payloads may evolve over time, and so are versioned. Payload versions are supplied as a suffix to the `X-Snyk-Event` header. For example, `project_snapshot/v0` indicates that the payload is `v0` of the `project_snapshot` event.  Version numbers only increment when a breaking change is made; for example, removing a field that used to exist, or changing the name of a field. Version numbers do not increment when making an additive change, such as adding a new field that never existed before.  **Note:** During the BETA phase, the structure of webhook payloads may change at any time, so we  recommend you check the payload version.  ### Event types  While consuming a webhook event, `X-Snyk-Event` header must be checked, as an end-point may receive multiple event types.  #### ping  The ping event happens after a new webhook is created, and can also be manually triggered using the ping webhook API. This is useful to test that your webhook receives data from Snyk correctly.  The `ping` event makes the following request:  ```jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: ping/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \"webhookId\": \"d3cf26b3-2d77-497b-bce2-23b33cc15362\" } ```  #### project_snapshot  This event is triggered every time an existing project is tested and a new snapshot is created. It is triggered on every test of a project, whether or not there are new issues. This event is not triggered when a new project is created or imported. Currently supported targets/scan types are Open Source and container.  ```jsx POST /webhook-handler/snyk123 HTTP/1.1 Host: my.app.com X-Snyk-Event: project_snapshot/v0 X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a X-Snyk-Timestamp: 2020-09-25T15:27:53Z X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6 User-Agent: Snyk-Webhooks/044aadd Content-Type: application/json {   \"project\": { ... }, // project object matching API responses   \"org\": { ... }, // organization object matching API responses   \"group\": { ... }, // group object matching API responses   \"newIssues\": [], // array of issues object matching API responses   \"removedIssues\": [], // array of issues object matching API responses } ```  ####  Detailed example of a payload  ##### project  see: [https://snyk.docs.apiary.io/#reference/projects](https://snyk.docs.apiary.io/#reference/projects)  ```tsx \"project\": {   \"name\": \"snyk/goof\",   \"id\": \"af137b96-6966-46c1-826b-2e79ac49bbd9\",   \"created\": \"2018-10-29T09:50:54.014Z\",   \"origin\": \"github\",   \"type\": \"maven\",   \"readOnly\": false,   \"testFrequency\": \"daily\",   \"totalDependencies\": 42,   \"issueCountsBySeverity\": {     \"low\": 13,     \"medium\": 8,     \"high\": 4,     \"critical\": 5   },   \"imageId\": \"sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019\",   \"imageTag\": \"latest\",   \"imageBaseImage\": \"alpine:3\",   \"imagePlatform\": \"linux/arm64\",   \"imageCluster\": \"Production\",   \"hostname\": null,   \"remoteRepoUrl\": \"https://github.com/snyk/goof.git\",   \"lastTestedDate\": \"2019-02-05T08:54:07.704Z\",   \"browseUrl\": \"https://app.snyk.io/org/4a18d42f-0706-4ad0-b127-24078731fbed/project/af137b96-6966-46c1-826b-2e79ac49bbd9\",   \"importingUser\": {     \"id\": \"e713cf94-bb02-4ea0-89d9-613cce0caed2\",     \"name\": \"example-user@snyk.io\",     \"username\": \"exampleUser\",     \"email\": \"example-user@snyk.io\"   },   \"isMonitored\": false,   \"branch\": null,   \"targetReference\": null,   \"tags\": [     {       \"key\": \"example-tag-key\",       \"value\": \"example-tag-value\"     }   ],   \"attributes\": {     \"criticality\": [       \"high\"     ],     \"environment\": [       \"backend\"     ],     \"lifecycle\": [       \"development\"     ]   },   \"remediation\": {     \"upgrade\": {},     \"patch\": {},     \"pin\": {}   } } ```  ##### org  see: [https://snyk.docs.apiary.io/#reference/organizations](https://snyk.docs.apiary.io/#reference/organizations)  ```tsx \"org\": {   \"name\": \"My Org\",   \"id\": \"a04d9cbd-ae6e-44af-b573-0556b0ad4bd2\",   \"slug\": \"my-org\",   \"url\": \"https://api.snyk.io/org/my-org\",   \"created\": \"2020-11-18T10:39:00.983Z\" } ```  ##### group  see: [https://snyk.docs.apiary.io/#reference/groups](https://snyk.docs.apiary.io/#reference/groups)  ```tsx \"group\": {   \"name\": \"ACME Inc.\",    \"id\": \"a060a49f-636e-480f-9e14-38e773b2a97f\" } ```  ##### issue  see: https://snyk.docs.apiary.io/#reference/users/user-organization-notification-settings/list-all-aggregated-issues  ```tsx {   \"id\": \"npm:ms:20170412\",   \"issueType\": \"vuln\",   \"pkgName\": \"ms\",   \"pkgVersions\": [     \"1.0.0\"   ],   \"issueData\": {     \"id\": \"npm:ms:20170412\",     \"title\": \"Regular Expression Denial of Service (ReDoS)\",     \"severity\": \"low\",     \"url\": \"https://snyk.io/vuln/npm:ms:20170412\",     \"description\": \"Lorem ipsum\",     \"identifiers\": {       \"CVE\": [],       \"CWE\": [         \"CWE-400\"       ],       \"ALTERNATIVE\": [         \"SNYK-JS-MS-10509\"       ]     },     \"credit\": [       \"Snyk Security Research Team\"     ],     \"exploitMaturity\": \"no-known-exploit\",     \"semver\": {       \"vulnerable\": [         \">=0.7.1 <2.0.0\"       ]     },     \"publicationTime\": \"2017-05-15T06:02:45Z\",     \"disclosureTime\": \"2017-04-11T21:00:00Z\",     \"CVSSv3\": \"CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L\",     \"cvssScore\": 3.7,     \"language\": \"js\",     \"patches\": [       {         \"id\": \"patch:npm:ms:20170412:2\",         \"urls\": [           \"https://snyk-patches.s3.amazonaws.com/npm/ms/20170412/ms_071.patch\"         ],         \"version\": \"=0.7.1\",         \"comments\": [],         \"modificationTime\": \"2019-12-03T11:40:45.866206Z\"       }     ],     \"nearestFixedInVersion\": \"2.0.0\"   },   \"isPatched\": false,   \"isIgnored\": false,   \"fixInfo\": {     \"isUpgradable\": false,     \"isPinnable\": false,     \"isPatchable\": true,     \"nearestFixedInVersion\": \"2.0.0\"   },   \"priority\": {     \"score\": 399,     \"factors\": [       {         \"name\": \"isFixable\",         \"description\": \"Has a fix available\"       },       {         \"name\": \"cvssScore\",         \"description\": \"CVSS 3.7\"       }     ]   } } ```
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.TestComposerJsonComposerLockFileRequest;
import org.openapitools.client.model.TestDepGraphRequest;
import org.openapitools.client.model.TestGemfileLockFileRequest;
import org.openapitools.client.model.TestGopkgTomlGopkgLockFileRequest;
import org.openapitools.client.model.TestGradleFileRequest;
import org.openapitools.client.model.TestMavenFileRequest;
import org.openapitools.client.model.TestPackageJsonPackageLockJsonFileRequest;
import org.openapitools.client.model.TestPackageJsonYarnLockFileRequest;
import org.openapitools.client.model.TestRequirementsTxtFileRequest;
import org.openapitools.client.model.TestSbtFileRequest;
import org.openapitools.client.model.TestVendorJsonFileRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TestApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TestApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TestApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for testComposerJsonComposerLockFile
     * @param testComposerJsonComposerLockFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testComposerJsonComposerLockFileCall(TestComposerJsonComposerLockFileRequest testComposerJsonComposerLockFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testComposerJsonComposerLockFileRequest;

        // create path and map variables
        String localVarPath = "/test/composer";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testComposerJsonComposerLockFileValidateBeforeCall(TestComposerJsonComposerLockFileRequest testComposerJsonComposerLockFileRequest, final ApiCallback _callback) throws ApiException {
        return testComposerJsonComposerLockFileCall(testComposerJsonComposerLockFileRequest, _callback);

    }

    /**
     * Test composer.json &amp; composer.lock file
     * You can test your Composer packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;composer.json&#x60; and a &#x60;composer.lock&#x60;.
     * @param testComposerJsonComposerLockFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testComposerJsonComposerLockFile(TestComposerJsonComposerLockFileRequest testComposerJsonComposerLockFileRequest) throws ApiException {
        testComposerJsonComposerLockFileWithHttpInfo(testComposerJsonComposerLockFileRequest);
    }

    /**
     * Test composer.json &amp; composer.lock file
     * You can test your Composer packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;composer.json&#x60; and a &#x60;composer.lock&#x60;.
     * @param testComposerJsonComposerLockFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testComposerJsonComposerLockFileWithHttpInfo(TestComposerJsonComposerLockFileRequest testComposerJsonComposerLockFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testComposerJsonComposerLockFileValidateBeforeCall(testComposerJsonComposerLockFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test composer.json &amp; composer.lock file (asynchronously)
     * You can test your Composer packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;composer.json&#x60; and a &#x60;composer.lock&#x60;.
     * @param testComposerJsonComposerLockFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testComposerJsonComposerLockFileAsync(TestComposerJsonComposerLockFileRequest testComposerJsonComposerLockFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testComposerJsonComposerLockFileValidateBeforeCall(testComposerJsonComposerLockFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testDepGraph
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testDepGraphRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testDepGraphCall(String org, TestDepGraphRequest testDepGraphRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testDepGraphRequest;

        // create path and map variables
        String localVarPath = "/test/dep-graph";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testDepGraphValidateBeforeCall(String org, TestDepGraphRequest testDepGraphRequest, final ApiCallback _callback) throws ApiException {
        return testDepGraphCall(org, testDepGraphRequest, _callback);

    }

    /**
     * Test Dep Graph
     * Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testDepGraphRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testDepGraph(String org, TestDepGraphRequest testDepGraphRequest) throws ApiException {
        testDepGraphWithHttpInfo(org, testDepGraphRequest);
    }

    /**
     * Test Dep Graph
     * Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testDepGraphRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testDepGraphWithHttpInfo(String org, TestDepGraphRequest testDepGraphRequest) throws ApiException {
        okhttp3.Call localVarCall = testDepGraphValidateBeforeCall(org, testDepGraphRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test Dep Graph (asynchronously)
     * Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testDepGraphRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testDepGraphAsync(String org, TestDepGraphRequest testDepGraphRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testDepGraphValidateBeforeCall(org, testDepGraphRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testForIssuesInAPublicGemByNameAndVersion
     * @param gemName The gem name. (required)
     * @param version The gem version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicGemByNameAndVersionCall(String gemName, String version, String org, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/test/rubygems/{gemName}/{version}"
            .replace("{" + "gemName" + "}", localVarApiClient.escapeString(gemName.toString()))
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testForIssuesInAPublicGemByNameAndVersionValidateBeforeCall(String gemName, String version, String org, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'gemName' is set
        if (gemName == null) {
            throw new ApiException("Missing the required parameter 'gemName' when calling testForIssuesInAPublicGemByNameAndVersion(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling testForIssuesInAPublicGemByNameAndVersion(Async)");
        }

        return testForIssuesInAPublicGemByNameAndVersionCall(gemName, version, org, _callback);

    }

    /**
     * Test for issues in a public gem by name and version
     * You can test &#x60;rubygems&#x60; packages for issues according to their name and version.
     * @param gemName The gem name. (required)
     * @param version The gem version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testForIssuesInAPublicGemByNameAndVersion(String gemName, String version, String org) throws ApiException {
        testForIssuesInAPublicGemByNameAndVersionWithHttpInfo(gemName, version, org);
    }

    /**
     * Test for issues in a public gem by name and version
     * You can test &#x60;rubygems&#x60; packages for issues according to their name and version.
     * @param gemName The gem name. (required)
     * @param version The gem version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testForIssuesInAPublicGemByNameAndVersionWithHttpInfo(String gemName, String version, String org) throws ApiException {
        okhttp3.Call localVarCall = testForIssuesInAPublicGemByNameAndVersionValidateBeforeCall(gemName, version, org, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test for issues in a public gem by name and version (asynchronously)
     * You can test &#x60;rubygems&#x60; packages for issues according to their name and version.
     * @param gemName The gem name. (required)
     * @param version The gem version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicGemByNameAndVersionAsync(String gemName, String version, String org, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testForIssuesInAPublicGemByNameAndVersionValidateBeforeCall(gemName, version, org, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionCall(String groupId, String artifactId, String version, String org, String repository, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/test/maven/{groupId}/{artifactId}/{version}"
            .replace("{" + "groupId" + "}", localVarApiClient.escapeString(groupId.toString()))
            .replace("{" + "artifactId" + "}", localVarApiClient.escapeString(artifactId.toString()))
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionValidateBeforeCall(String groupId, String artifactId, String version, String org, String repository, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupId' is set
        if (groupId == null) {
            throw new ApiException("Missing the required parameter 'groupId' when calling testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(Async)");
        }

        // verify the required parameter 'artifactId' is set
        if (artifactId == null) {
            throw new ApiException("Missing the required parameter 'artifactId' when calling testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(Async)");
        }

        return testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionCall(groupId, artifactId, version, org, repository, _callback);

    }

    /**
     * Test for issues in a public package by group id, artifact id and version
     * You can test &#x60;maven&#x60; packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the &#x60;repository&#x60; query parameter).
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(String groupId, String artifactId, String version, String org, String repository) throws ApiException {
        testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionWithHttpInfo(groupId, artifactId, version, org, repository);
    }

    /**
     * Test for issues in a public package by group id, artifact id and version
     * You can test &#x60;maven&#x60; packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the &#x60;repository&#x60; query parameter).
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionWithHttpInfo(String groupId, String artifactId, String version, String org, String repository) throws ApiException {
        okhttp3.Call localVarCall = testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionValidateBeforeCall(groupId, artifactId, version, org, repository, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test for issues in a public package by group id, artifact id and version (asynchronously)
     * You can test &#x60;maven&#x60; packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the &#x60;repository&#x60; query parameter).
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionAsync(String groupId, String artifactId, String version, String org, String repository, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersionValidateBeforeCall(groupId, artifactId, version, org, repository, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testForIssuesInAPublicPackageByGroupNameAndVersion
     * @param group The package&#39;s group ID. (required)
     * @param name The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicPackageByGroupNameAndVersionCall(String group, String name, String version, String org, String repository, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/test/gradle/{group}/{name}/{version}"
            .replace("{" + "group" + "}", localVarApiClient.escapeString(group.toString()))
            .replace("{" + "name" + "}", localVarApiClient.escapeString(name.toString()))
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testForIssuesInAPublicPackageByGroupNameAndVersionValidateBeforeCall(String group, String name, String version, String org, String repository, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'group' is set
        if (group == null) {
            throw new ApiException("Missing the required parameter 'group' when calling testForIssuesInAPublicPackageByGroupNameAndVersion(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling testForIssuesInAPublicPackageByGroupNameAndVersion(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling testForIssuesInAPublicPackageByGroupNameAndVersion(Async)");
        }

        return testForIssuesInAPublicPackageByGroupNameAndVersionCall(group, name, version, org, repository, _callback);

    }

    /**
     * Test for issues in a public package by group, name and version
     * You can test &#x60;gradle&#x60; packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.
     * @param group The package&#39;s group ID. (required)
     * @param name The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testForIssuesInAPublicPackageByGroupNameAndVersion(String group, String name, String version, String org, String repository) throws ApiException {
        testForIssuesInAPublicPackageByGroupNameAndVersionWithHttpInfo(group, name, version, org, repository);
    }

    /**
     * Test for issues in a public package by group, name and version
     * You can test &#x60;gradle&#x60; packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.
     * @param group The package&#39;s group ID. (required)
     * @param name The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testForIssuesInAPublicPackageByGroupNameAndVersionWithHttpInfo(String group, String name, String version, String org, String repository) throws ApiException {
        okhttp3.Call localVarCall = testForIssuesInAPublicPackageByGroupNameAndVersionValidateBeforeCall(group, name, version, org, repository, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test for issues in a public package by group, name and version (asynchronously)
     * You can test &#x60;gradle&#x60; packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.
     * @param group The package&#39;s group ID. (required)
     * @param name The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicPackageByGroupNameAndVersionAsync(String group, String name, String version, String org, String repository, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testForIssuesInAPublicPackageByGroupNameAndVersionValidateBeforeCall(group, name, version, org, repository, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testForIssuesInAPublicPackageByNameAndVersion
     * @param packageName The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicPackageByNameAndVersionCall(String packageName, String version, String org, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/test/npm/{packageName}/{version}"
            .replace("{" + "packageName" + "}", localVarApiClient.escapeString(packageName.toString()))
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testForIssuesInAPublicPackageByNameAndVersionValidateBeforeCall(String packageName, String version, String org, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'packageName' is set
        if (packageName == null) {
            throw new ApiException("Missing the required parameter 'packageName' when calling testForIssuesInAPublicPackageByNameAndVersion(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling testForIssuesInAPublicPackageByNameAndVersion(Async)");
        }

        return testForIssuesInAPublicPackageByNameAndVersionCall(packageName, version, org, _callback);

    }

    /**
     * Test for issues in a public package by name and version
     * You can test &#x60;npm&#x60; packages for issues according to their name and version.
     * @param packageName The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testForIssuesInAPublicPackageByNameAndVersion(String packageName, String version, String org) throws ApiException {
        testForIssuesInAPublicPackageByNameAndVersionWithHttpInfo(packageName, version, org);
    }

    /**
     * Test for issues in a public package by name and version
     * You can test &#x60;npm&#x60; packages for issues according to their name and version.
     * @param packageName The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testForIssuesInAPublicPackageByNameAndVersionWithHttpInfo(String packageName, String version, String org) throws ApiException {
        okhttp3.Call localVarCall = testForIssuesInAPublicPackageByNameAndVersionValidateBeforeCall(packageName, version, org, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test for issues in a public package by name and version (asynchronously)
     * You can test &#x60;npm&#x60; packages for issues according to their name and version.
     * @param packageName The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testForIssuesInAPublicPackageByNameAndVersionAsync(String packageName, String version, String org, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testForIssuesInAPublicPackageByNameAndVersionValidateBeforeCall(packageName, version, org, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testGemfileLockFile
     * @param testGemfileLockFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testGemfileLockFileCall(TestGemfileLockFileRequest testGemfileLockFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testGemfileLockFileRequest;

        // create path and map variables
        String localVarPath = "/test/rubygems";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testGemfileLockFileValidateBeforeCall(TestGemfileLockFileRequest testGemfileLockFileRequest, final ApiCallback _callback) throws ApiException {
        return testGemfileLockFileCall(testGemfileLockFileRequest, _callback);

    }

    /**
     * Test gemfile.lock file
     * You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;Gemfile.lock&#x60;.
     * @param testGemfileLockFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testGemfileLockFile(TestGemfileLockFileRequest testGemfileLockFileRequest) throws ApiException {
        testGemfileLockFileWithHttpInfo(testGemfileLockFileRequest);
    }

    /**
     * Test gemfile.lock file
     * You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;Gemfile.lock&#x60;.
     * @param testGemfileLockFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testGemfileLockFileWithHttpInfo(TestGemfileLockFileRequest testGemfileLockFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testGemfileLockFileValidateBeforeCall(testGemfileLockFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test gemfile.lock file (asynchronously)
     * You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;Gemfile.lock&#x60;.
     * @param testGemfileLockFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testGemfileLockFileAsync(TestGemfileLockFileRequest testGemfileLockFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testGemfileLockFileValidateBeforeCall(testGemfileLockFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testGopkgTomlGopkgLockFile
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testGopkgTomlGopkgLockFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testGopkgTomlGopkgLockFileCall(String org, TestGopkgTomlGopkgLockFileRequest testGopkgTomlGopkgLockFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testGopkgTomlGopkgLockFileRequest;

        // create path and map variables
        String localVarPath = "/test/golangdep";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testGopkgTomlGopkgLockFileValidateBeforeCall(String org, TestGopkgTomlGopkgLockFileRequest testGopkgTomlGopkgLockFileRequest, final ApiCallback _callback) throws ApiException {
        return testGopkgTomlGopkgLockFileCall(org, testGopkgTomlGopkgLockFileRequest, _callback);

    }

    /**
     * Test Gopkg.toml &amp; Gopkg.lock File
     * You can test your Go dep packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;Gopkg.toml&#x60; and a &#x60;Gopkg.lock&#x60;.
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testGopkgTomlGopkgLockFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testGopkgTomlGopkgLockFile(String org, TestGopkgTomlGopkgLockFileRequest testGopkgTomlGopkgLockFileRequest) throws ApiException {
        testGopkgTomlGopkgLockFileWithHttpInfo(org, testGopkgTomlGopkgLockFileRequest);
    }

    /**
     * Test Gopkg.toml &amp; Gopkg.lock File
     * You can test your Go dep packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;Gopkg.toml&#x60; and a &#x60;Gopkg.lock&#x60;.
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testGopkgTomlGopkgLockFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testGopkgTomlGopkgLockFileWithHttpInfo(String org, TestGopkgTomlGopkgLockFileRequest testGopkgTomlGopkgLockFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testGopkgTomlGopkgLockFileValidateBeforeCall(org, testGopkgTomlGopkgLockFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test Gopkg.toml &amp; Gopkg.lock File (asynchronously)
     * You can test your Go dep packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;Gopkg.toml&#x60; and a &#x60;Gopkg.lock&#x60;.
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param testGopkgTomlGopkgLockFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testGopkgTomlGopkgLockFileAsync(String org, TestGopkgTomlGopkgLockFileRequest testGopkgTomlGopkgLockFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testGopkgTomlGopkgLockFileValidateBeforeCall(org, testGopkgTomlGopkgLockFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testGradleFile
     * @param testGradleFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testGradleFileCall(TestGradleFileRequest testGradleFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testGradleFileRequest;

        // create path and map variables
        String localVarPath = "/test/gradle";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testGradleFileValidateBeforeCall(TestGradleFileRequest testGradleFileRequest, final ApiCallback _callback) throws ApiException {
        return testGradleFileCall(testGradleFileRequest, _callback);

    }

    /**
     * Test gradle file
     * You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \&quot;target\&quot; &#x60;build.gradle&#x60;.
     * @param testGradleFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testGradleFile(TestGradleFileRequest testGradleFileRequest) throws ApiException {
        testGradleFileWithHttpInfo(testGradleFileRequest);
    }

    /**
     * Test gradle file
     * You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \&quot;target\&quot; &#x60;build.gradle&#x60;.
     * @param testGradleFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testGradleFileWithHttpInfo(TestGradleFileRequest testGradleFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testGradleFileValidateBeforeCall(testGradleFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test gradle file (asynchronously)
     * You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \&quot;target\&quot; &#x60;build.gradle&#x60;.
     * @param testGradleFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testGradleFileAsync(TestGradleFileRequest testGradleFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testGradleFileValidateBeforeCall(testGradleFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testMavenFile
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param testMavenFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testMavenFileCall(String org, String repository, TestMavenFileRequest testMavenFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testMavenFileRequest;

        // create path and map variables
        String localVarPath = "/test/maven";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testMavenFileValidateBeforeCall(String org, String repository, TestMavenFileRequest testMavenFileRequest, final ApiCallback _callback) throws ApiException {
        return testMavenFileCall(org, repository, testMavenFileRequest, _callback);

    }

    /**
     * Test maven file
     * You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;pom.xml&#x60;.  Additional manifest files, if they are needed, like parent &#x60;pom.xml&#x60; files, child poms, etc., according the the definitions in the target &#x60;pom.xml&#x60; file, should be supplied in the &#x60;additional&#x60; body parameter.
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param testMavenFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testMavenFile(String org, String repository, TestMavenFileRequest testMavenFileRequest) throws ApiException {
        testMavenFileWithHttpInfo(org, repository, testMavenFileRequest);
    }

    /**
     * Test maven file
     * You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;pom.xml&#x60;.  Additional manifest files, if they are needed, like parent &#x60;pom.xml&#x60; files, child poms, etc., according the the definitions in the target &#x60;pom.xml&#x60; file, should be supplied in the &#x60;additional&#x60; body parameter.
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param testMavenFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testMavenFileWithHttpInfo(String org, String repository, TestMavenFileRequest testMavenFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testMavenFileValidateBeforeCall(org, repository, testMavenFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test maven file (asynchronously)
     * You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;pom.xml&#x60;.  Additional manifest files, if they are needed, like parent &#x60;pom.xml&#x60; files, child poms, etc., according the the definitions in the target &#x60;pom.xml&#x60; file, should be supplied in the &#x60;additional&#x60; body parameter.
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param testMavenFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testMavenFileAsync(String org, String repository, TestMavenFileRequest testMavenFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testMavenFileValidateBeforeCall(org, repository, testMavenFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testPackageJsonPackageLockJsonFile
     * @param testPackageJsonPackageLockJsonFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testPackageJsonPackageLockJsonFileCall(TestPackageJsonPackageLockJsonFileRequest testPackageJsonPackageLockJsonFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testPackageJsonPackageLockJsonFileRequest;

        // create path and map variables
        String localVarPath = "/test/npm";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testPackageJsonPackageLockJsonFileValidateBeforeCall(TestPackageJsonPackageLockJsonFileRequest testPackageJsonPackageLockJsonFileRequest, final ApiCallback _callback) throws ApiException {
        return testPackageJsonPackageLockJsonFileCall(testPackageJsonPackageLockJsonFileRequest, _callback);

    }

    /**
     * Test package.json &amp; package-lock.json File
     * You can test your npm packages for issues according to their manifest file &amp; optional lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and optionally a &#x60;package-lock.json&#x60;.
     * @param testPackageJsonPackageLockJsonFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testPackageJsonPackageLockJsonFile(TestPackageJsonPackageLockJsonFileRequest testPackageJsonPackageLockJsonFileRequest) throws ApiException {
        testPackageJsonPackageLockJsonFileWithHttpInfo(testPackageJsonPackageLockJsonFileRequest);
    }

    /**
     * Test package.json &amp; package-lock.json File
     * You can test your npm packages for issues according to their manifest file &amp; optional lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and optionally a &#x60;package-lock.json&#x60;.
     * @param testPackageJsonPackageLockJsonFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testPackageJsonPackageLockJsonFileWithHttpInfo(TestPackageJsonPackageLockJsonFileRequest testPackageJsonPackageLockJsonFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testPackageJsonPackageLockJsonFileValidateBeforeCall(testPackageJsonPackageLockJsonFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test package.json &amp; package-lock.json File (asynchronously)
     * You can test your npm packages for issues according to their manifest file &amp; optional lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and optionally a &#x60;package-lock.json&#x60;.
     * @param testPackageJsonPackageLockJsonFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testPackageJsonPackageLockJsonFileAsync(TestPackageJsonPackageLockJsonFileRequest testPackageJsonPackageLockJsonFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testPackageJsonPackageLockJsonFileValidateBeforeCall(testPackageJsonPackageLockJsonFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testPackageJsonYarnLockFile
     * @param testPackageJsonYarnLockFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testPackageJsonYarnLockFileCall(TestPackageJsonYarnLockFileRequest testPackageJsonYarnLockFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testPackageJsonYarnLockFileRequest;

        // create path and map variables
        String localVarPath = "/test/yarn";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testPackageJsonYarnLockFileValidateBeforeCall(TestPackageJsonYarnLockFileRequest testPackageJsonYarnLockFileRequest, final ApiCallback _callback) throws ApiException {
        return testPackageJsonYarnLockFileCall(testPackageJsonYarnLockFileRequest, _callback);

    }

    /**
     * Test package.json &amp; yarn.lock File
     * You can test your yarn packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and a &#x60;yarn.lock&#x60;.
     * @param testPackageJsonYarnLockFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testPackageJsonYarnLockFile(TestPackageJsonYarnLockFileRequest testPackageJsonYarnLockFileRequest) throws ApiException {
        testPackageJsonYarnLockFileWithHttpInfo(testPackageJsonYarnLockFileRequest);
    }

    /**
     * Test package.json &amp; yarn.lock File
     * You can test your yarn packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and a &#x60;yarn.lock&#x60;.
     * @param testPackageJsonYarnLockFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testPackageJsonYarnLockFileWithHttpInfo(TestPackageJsonYarnLockFileRequest testPackageJsonYarnLockFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testPackageJsonYarnLockFileValidateBeforeCall(testPackageJsonYarnLockFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test package.json &amp; yarn.lock File (asynchronously)
     * You can test your yarn packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and a &#x60;yarn.lock&#x60;.
     * @param testPackageJsonYarnLockFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testPackageJsonYarnLockFileAsync(TestPackageJsonYarnLockFileRequest testPackageJsonYarnLockFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testPackageJsonYarnLockFileValidateBeforeCall(testPackageJsonYarnLockFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testPipPackageNameVersionGet
     * @param packageName The package name. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testPipPackageNameVersionGetCall(String packageName, String version, String org, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/test/pip/{packageName}/{version}"
            .replace("{" + "packageName" + "}", localVarApiClient.escapeString(packageName.toString()))
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testPipPackageNameVersionGetValidateBeforeCall(String packageName, String version, String org, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'packageName' is set
        if (packageName == null) {
            throw new ApiException("Missing the required parameter 'packageName' when calling testPipPackageNameVersionGet(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling testPipPackageNameVersionGet(Async)");
        }

        return testPipPackageNameVersionGetCall(packageName, version, org, _callback);

    }

    /**
     * Test for issues in a public package by name and version
     * You can test &#x60;pip&#x60; packages for issues according to their name and version.
     * @param packageName The package name. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testPipPackageNameVersionGet(String packageName, String version, String org) throws ApiException {
        testPipPackageNameVersionGetWithHttpInfo(packageName, version, org);
    }

    /**
     * Test for issues in a public package by name and version
     * You can test &#x60;pip&#x60; packages for issues according to their name and version.
     * @param packageName The package name. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testPipPackageNameVersionGetWithHttpInfo(String packageName, String version, String org) throws ApiException {
        okhttp3.Call localVarCall = testPipPackageNameVersionGetValidateBeforeCall(packageName, version, org, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test for issues in a public package by name and version (asynchronously)
     * You can test &#x60;pip&#x60; packages for issues according to their name and version.
     * @param packageName The package name. (required)
     * @param version The Package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testPipPackageNameVersionGetAsync(String packageName, String version, String org, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testPipPackageNameVersionGetValidateBeforeCall(packageName, version, org, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testRequirementsTxtFile
     * @param testRequirementsTxtFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testRequirementsTxtFileCall(TestRequirementsTxtFileRequest testRequirementsTxtFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testRequirementsTxtFileRequest;

        // create path and map variables
        String localVarPath = "/test/pip";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testRequirementsTxtFileValidateBeforeCall(TestRequirementsTxtFileRequest testRequirementsTxtFileRequest, final ApiCallback _callback) throws ApiException {
        return testRequirementsTxtFileCall(testRequirementsTxtFileRequest, _callback);

    }

    /**
     * Test requirements.txt file
     * You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;requirements.txt&#x60;.
     * @param testRequirementsTxtFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testRequirementsTxtFile(TestRequirementsTxtFileRequest testRequirementsTxtFileRequest) throws ApiException {
        testRequirementsTxtFileWithHttpInfo(testRequirementsTxtFileRequest);
    }

    /**
     * Test requirements.txt file
     * You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;requirements.txt&#x60;.
     * @param testRequirementsTxtFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testRequirementsTxtFileWithHttpInfo(TestRequirementsTxtFileRequest testRequirementsTxtFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testRequirementsTxtFileValidateBeforeCall(testRequirementsTxtFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test requirements.txt file (asynchronously)
     * You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;requirements.txt&#x60;.
     * @param testRequirementsTxtFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testRequirementsTxtFileAsync(TestRequirementsTxtFileRequest testRequirementsTxtFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testRequirementsTxtFileValidateBeforeCall(testRequirementsTxtFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testSbtFile
     * @param testSbtFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testSbtFileCall(TestSbtFileRequest testSbtFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testSbtFileRequest;

        // create path and map variables
        String localVarPath = "/test/sbt";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testSbtFileValidateBeforeCall(TestSbtFileRequest testSbtFileRequest, final ApiCallback _callback) throws ApiException {
        return testSbtFileCall(testSbtFileRequest, _callback);

    }

    /**
     * Test sbt file
     * You can test your &#x60;sbt&#x60; packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;build.sbt&#x60;.
     * @param testSbtFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testSbtFile(TestSbtFileRequest testSbtFileRequest) throws ApiException {
        testSbtFileWithHttpInfo(testSbtFileRequest);
    }

    /**
     * Test sbt file
     * You can test your &#x60;sbt&#x60; packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;build.sbt&#x60;.
     * @param testSbtFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testSbtFileWithHttpInfo(TestSbtFileRequest testSbtFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testSbtFileValidateBeforeCall(testSbtFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test sbt file (asynchronously)
     * You can test your &#x60;sbt&#x60; packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;build.sbt&#x60;.
     * @param testSbtFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testSbtFileAsync(TestSbtFileRequest testSbtFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testSbtFileValidateBeforeCall(testSbtFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testSbtGroupIdArtifactIdVersionGet
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testSbtGroupIdArtifactIdVersionGetCall(String groupId, String artifactId, String version, String org, String repository, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/test/sbt/{groupId}/{artifactId}/{version}"
            .replace("{" + "groupId" + "}", localVarApiClient.escapeString(groupId.toString()))
            .replace("{" + "artifactId" + "}", localVarApiClient.escapeString(artifactId.toString()))
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (org != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("org", org));
        }

        if (repository != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("repository", repository));
        }

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testSbtGroupIdArtifactIdVersionGetValidateBeforeCall(String groupId, String artifactId, String version, String org, String repository, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupId' is set
        if (groupId == null) {
            throw new ApiException("Missing the required parameter 'groupId' when calling testSbtGroupIdArtifactIdVersionGet(Async)");
        }

        // verify the required parameter 'artifactId' is set
        if (artifactId == null) {
            throw new ApiException("Missing the required parameter 'artifactId' when calling testSbtGroupIdArtifactIdVersionGet(Async)");
        }

        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling testSbtGroupIdArtifactIdVersionGet(Async)");
        }

        return testSbtGroupIdArtifactIdVersionGetCall(groupId, artifactId, version, org, repository, _callback);

    }

    /**
     * Test for issues in a public package by group id, artifact id and version
     * You can test &#x60;sbt&#x60; packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testSbtGroupIdArtifactIdVersionGet(String groupId, String artifactId, String version, String org, String repository) throws ApiException {
        testSbtGroupIdArtifactIdVersionGetWithHttpInfo(groupId, artifactId, version, org, repository);
    }

    /**
     * Test for issues in a public package by group id, artifact id and version
     * You can test &#x60;sbt&#x60; packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testSbtGroupIdArtifactIdVersionGetWithHttpInfo(String groupId, String artifactId, String version, String org, String repository) throws ApiException {
        okhttp3.Call localVarCall = testSbtGroupIdArtifactIdVersionGetValidateBeforeCall(groupId, artifactId, version, org, repository, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test for issues in a public package by group id, artifact id and version (asynchronously)
     * You can test &#x60;sbt&#x60; packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.
     * @param groupId The package&#39;s group ID. (required)
     * @param artifactId The package&#39;s artifact ID. (required)
     * @param version The package version to test. (required)
     * @param org The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. (optional)
     * @param repository The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testSbtGroupIdArtifactIdVersionGetAsync(String groupId, String artifactId, String version, String org, String repository, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testSbtGroupIdArtifactIdVersionGetValidateBeforeCall(groupId, artifactId, version, org, repository, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for testVendorJsonFile
     * @param testVendorJsonFileRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testVendorJsonFileCall(TestVendorJsonFileRequest testVendorJsonFileRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = testVendorJsonFileRequest;

        // create path and map variables
        String localVarPath = "/test/govendor";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call testVendorJsonFileValidateBeforeCall(TestVendorJsonFileRequest testVendorJsonFileRequest, final ApiCallback _callback) throws ApiException {
        return testVendorJsonFileCall(testVendorJsonFileRequest, _callback);

    }

    /**
     * Test vendor.json File
     * You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;vendor.json&#x60;.
     * @param testVendorJsonFileRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void testVendorJsonFile(TestVendorJsonFileRequest testVendorJsonFileRequest) throws ApiException {
        testVendorJsonFileWithHttpInfo(testVendorJsonFileRequest);
    }

    /**
     * Test vendor.json File
     * You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;vendor.json&#x60;.
     * @param testVendorJsonFileRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> testVendorJsonFileWithHttpInfo(TestVendorJsonFileRequest testVendorJsonFileRequest) throws ApiException {
        okhttp3.Call localVarCall = testVendorJsonFileValidateBeforeCall(testVendorJsonFileRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Test vendor.json File (asynchronously)
     * You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;vendor.json&#x60;.
     * @param testVendorJsonFileRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call testVendorJsonFileAsync(TestVendorJsonFileRequest testVendorJsonFileRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = testVendorJsonFileValidateBeforeCall(testVendorJsonFileRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
