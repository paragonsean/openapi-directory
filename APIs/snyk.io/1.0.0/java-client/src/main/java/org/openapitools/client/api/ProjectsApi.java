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


import org.openapitools.client.model.AddATagToAProject200Response;
import org.openapitools.client.model.AddATagToAProjectRequest;
import org.openapitools.client.model.AddIgnoreRequest;
import org.openapitools.client.model.ApplyingAttributes200Response;
import org.openapitools.client.model.ApplyingAttributesRequest;
import java.math.BigDecimal;
import org.openapitools.client.model.CreateJiraIssue200Response;
import org.openapitools.client.model.CreateJiraIssueRequest;
import org.openapitools.client.model.GetProjectDependencyGraph200Response;
import org.openapitools.client.model.ListAllAggregatedIssues200Response;
import org.openapitools.client.model.ListAllAggregatedIssuesRequest;
import org.openapitools.client.model.ListAllProjectSnapshotIssuePaths200Response;
import org.openapitools.client.model.ListAllProjectSnapshots200Response;
import org.openapitools.client.model.ListAllProjectSnapshotsRequest;
import org.openapitools.client.model.ListAllProjects200Response;
import org.openapitools.client.model.ListAllProjectsRequest;
import org.openapitools.client.model.ListProjectSettings200Response;
import org.openapitools.client.model.MoveProjectToADifferentOrganizationRequest;
import org.openapitools.client.model.RetrieveASingleProject200Response;
import org.openapitools.client.model.UpdateAProjectRequest;
import org.openapitools.client.model.UpdateProjectSettingsRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProjectsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProjectsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProjectsApi(ApiClient apiClient) {
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
     * Build call for activate
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call activateCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/activate"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call activateValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling activate(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling activate(Async)");
        }

        return activateCall(orgId, projectId, _callback);

    }

    /**
     * Activate
     * Activating a project will:  - Add a repository webhook for supported integrations.  - Enable pull request tests for new vulnerabilities.  - Open Fix pull request for newly disclosed vulnerabilities.  - Enable recurring tests, sending email alerts about newly disclosed vulnerabilities.
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void activate(String orgId, String projectId) throws ApiException {
        activateWithHttpInfo(orgId, projectId);
    }

    /**
     * Activate
     * Activating a project will:  - Add a repository webhook for supported integrations.  - Enable pull request tests for new vulnerabilities.  - Open Fix pull request for newly disclosed vulnerabilities.  - Enable recurring tests, sending email alerts about newly disclosed vulnerabilities.
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> activateWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = activateValidateBeforeCall(orgId, projectId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Activate (asynchronously)
     * Activating a project will:  - Add a repository webhook for supported integrations.  - Enable pull request tests for new vulnerabilities.  - Open Fix pull request for newly disclosed vulnerabilities.  - Enable recurring tests, sending email alerts about newly disclosed vulnerabilities.
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call activateAsync(String orgId, String projectId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = activateValidateBeforeCall(orgId, projectId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for addATagToAProject
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to apply the tag to (required)
     * @param addATagToAProjectRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addATagToAProjectCall(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addATagToAProjectRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/tags"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call addATagToAProjectValidateBeforeCall(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling addATagToAProject(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling addATagToAProject(Async)");
        }

        return addATagToAProjectCall(orgId, projectId, addATagToAProjectRequest, _callback);

    }

    /**
     * Add a tag to a project
     * ​
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to apply the tag to (required)
     * @param addATagToAProjectRequest  (optional)
     * @return AddATagToAProject200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AddATagToAProject200Response addATagToAProject(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest) throws ApiException {
        ApiResponse<AddATagToAProject200Response> localVarResp = addATagToAProjectWithHttpInfo(orgId, projectId, addATagToAProjectRequest);
        return localVarResp.getData();
    }

    /**
     * Add a tag to a project
     * ​
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to apply the tag to (required)
     * @param addATagToAProjectRequest  (optional)
     * @return ApiResponse&lt;AddATagToAProject200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddATagToAProject200Response> addATagToAProjectWithHttpInfo(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest) throws ApiException {
        okhttp3.Call localVarCall = addATagToAProjectValidateBeforeCall(orgId, projectId, addATagToAProjectRequest, null);
        Type localVarReturnType = new TypeToken<AddATagToAProject200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a tag to a project (asynchronously)
     * ​
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to apply the tag to (required)
     * @param addATagToAProjectRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addATagToAProjectAsync(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest, final ApiCallback<AddATagToAProject200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = addATagToAProjectValidateBeforeCall(orgId, projectId, addATagToAProjectRequest, _callback);
        Type localVarReturnType = new TypeToken<AddATagToAProject200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addIgnore
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param addIgnoreRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addIgnoreCall(String orgId, String projectId, String issueId, AddIgnoreRequest addIgnoreRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addIgnoreRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/ignore/{issueId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()));

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
    private okhttp3.Call addIgnoreValidateBeforeCall(String orgId, String projectId, String issueId, AddIgnoreRequest addIgnoreRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling addIgnore(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling addIgnore(Async)");
        }

        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling addIgnore(Async)");
        }

        return addIgnoreCall(orgId, projectId, issueId, addIgnoreRequest, _callback);

    }

    /**
     * Add ignore
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param addIgnoreRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object addIgnore(String orgId, String projectId, String issueId, AddIgnoreRequest addIgnoreRequest) throws ApiException {
        ApiResponse<Object> localVarResp = addIgnoreWithHttpInfo(orgId, projectId, issueId, addIgnoreRequest);
        return localVarResp.getData();
    }

    /**
     * Add ignore
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param addIgnoreRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> addIgnoreWithHttpInfo(String orgId, String projectId, String issueId, AddIgnoreRequest addIgnoreRequest) throws ApiException {
        okhttp3.Call localVarCall = addIgnoreValidateBeforeCall(orgId, projectId, issueId, addIgnoreRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add ignore (asynchronously)
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param addIgnoreRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addIgnoreAsync(String orgId, String projectId, String issueId, AddIgnoreRequest addIgnoreRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = addIgnoreValidateBeforeCall(orgId, projectId, issueId, addIgnoreRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for applyingAttributes
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param applyingAttributesRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call applyingAttributesCall(String orgId, String projectId, ApplyingAttributesRequest applyingAttributesRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = applyingAttributesRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/attributes"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call applyingAttributesValidateBeforeCall(String orgId, String projectId, ApplyingAttributesRequest applyingAttributesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling applyingAttributes(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling applyingAttributes(Async)");
        }

        return applyingAttributesCall(orgId, projectId, applyingAttributesRequest, _callback);

    }

    /**
     * Applying attributes
     * Applies an attribute to the provided project. It is possible to assign multiple values to each attribute, but you can only assign values to one of the predefined attribute categories, using the predefined options for this category. Assigning an attribute requires the caller to be either an Organization Administrator or a Group Administrator. Assigning an attribute will override any existing values that the specific attribute already has set. In order to clear out an attribute value, an empty array can be set.
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param applyingAttributesRequest  (optional)
     * @return ApplyingAttributes200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApplyingAttributes200Response applyingAttributes(String orgId, String projectId, ApplyingAttributesRequest applyingAttributesRequest) throws ApiException {
        ApiResponse<ApplyingAttributes200Response> localVarResp = applyingAttributesWithHttpInfo(orgId, projectId, applyingAttributesRequest);
        return localVarResp.getData();
    }

    /**
     * Applying attributes
     * Applies an attribute to the provided project. It is possible to assign multiple values to each attribute, but you can only assign values to one of the predefined attribute categories, using the predefined options for this category. Assigning an attribute requires the caller to be either an Organization Administrator or a Group Administrator. Assigning an attribute will override any existing values that the specific attribute already has set. In order to clear out an attribute value, an empty array can be set.
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param applyingAttributesRequest  (optional)
     * @return ApiResponse&lt;ApplyingAttributes200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ApplyingAttributes200Response> applyingAttributesWithHttpInfo(String orgId, String projectId, ApplyingAttributesRequest applyingAttributesRequest) throws ApiException {
        okhttp3.Call localVarCall = applyingAttributesValidateBeforeCall(orgId, projectId, applyingAttributesRequest, null);
        Type localVarReturnType = new TypeToken<ApplyingAttributes200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Applying attributes (asynchronously)
     * Applies an attribute to the provided project. It is possible to assign multiple values to each attribute, but you can only assign values to one of the predefined attribute categories, using the predefined options for this category. Assigning an attribute requires the caller to be either an Organization Administrator or a Group Administrator. Assigning an attribute will override any existing values that the specific attribute already has set. In order to clear out an attribute value, an empty array can be set.
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param applyingAttributesRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call applyingAttributesAsync(String orgId, String projectId, ApplyingAttributesRequest applyingAttributesRequest, final ApiCallback<ApplyingAttributes200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = applyingAttributesValidateBeforeCall(orgId, projectId, applyingAttributesRequest, _callback);
        Type localVarReturnType = new TypeToken<ApplyingAttributes200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createJiraIssue
     * @param issueId The issue ID to create Jira issue for. (required)
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param createJiraIssueRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createJiraIssueCall(String issueId, String orgId, String projectId, CreateJiraIssueRequest createJiraIssueRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createJiraIssueRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/issue/{issueId}/jira-issue"
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()))
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*"
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
    private okhttp3.Call createJiraIssueValidateBeforeCall(String issueId, String orgId, String projectId, CreateJiraIssueRequest createJiraIssueRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling createJiraIssue(Async)");
        }

        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling createJiraIssue(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling createJiraIssue(Async)");
        }

        return createJiraIssueCall(issueId, orgId, projectId, createJiraIssueRequest, _callback);

    }

    /**
     * Create jira issue
     * 
     * @param issueId The issue ID to create Jira issue for. (required)
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param createJiraIssueRequest  (optional)
     * @return CreateJiraIssue200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public CreateJiraIssue200Response createJiraIssue(String issueId, String orgId, String projectId, CreateJiraIssueRequest createJiraIssueRequest) throws ApiException {
        ApiResponse<CreateJiraIssue200Response> localVarResp = createJiraIssueWithHttpInfo(issueId, orgId, projectId, createJiraIssueRequest);
        return localVarResp.getData();
    }

    /**
     * Create jira issue
     * 
     * @param issueId The issue ID to create Jira issue for. (required)
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param createJiraIssueRequest  (optional)
     * @return ApiResponse&lt;CreateJiraIssue200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateJiraIssue200Response> createJiraIssueWithHttpInfo(String issueId, String orgId, String projectId, CreateJiraIssueRequest createJiraIssueRequest) throws ApiException {
        okhttp3.Call localVarCall = createJiraIssueValidateBeforeCall(issueId, orgId, projectId, createJiraIssueRequest, null);
        Type localVarReturnType = new TypeToken<CreateJiraIssue200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create jira issue (asynchronously)
     * 
     * @param issueId The issue ID to create Jira issue for. (required)
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param createJiraIssueRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createJiraIssueAsync(String issueId, String orgId, String projectId, CreateJiraIssueRequest createJiraIssueRequest, final ApiCallback<CreateJiraIssue200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createJiraIssueValidateBeforeCall(issueId, orgId, projectId, createJiraIssueRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateJiraIssue200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deactivate
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deactivateCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/deactivate"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deactivateValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling deactivate(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling deactivate(Async)");
        }

        return deactivateCall(orgId, projectId, _callback);

    }

    /**
     * Deactivate
     * Deactivating a project will:  - Disable pull request tests for new vulnerabilities.  - Disable Fix pull request from being opened for newly disclosed vulnerabilities.  - Disable recurring tests - email alerts about newly disclosed vulnerabilities will be turned off.  - If the repository has no other active projects, then remove any webhooks related to the project.
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deactivate(String orgId, String projectId) throws ApiException {
        deactivateWithHttpInfo(orgId, projectId);
    }

    /**
     * Deactivate
     * Deactivating a project will:  - Disable pull request tests for new vulnerabilities.  - Disable Fix pull request from being opened for newly disclosed vulnerabilities.  - Disable recurring tests - email alerts about newly disclosed vulnerabilities will be turned off.  - If the repository has no other active projects, then remove any webhooks related to the project.
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deactivateWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = deactivateValidateBeforeCall(orgId, projectId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Deactivate (asynchronously)
     * Deactivating a project will:  - Disable pull request tests for new vulnerabilities.  - Disable Fix pull request from being opened for newly disclosed vulnerabilities.  - Disable recurring tests - email alerts about newly disclosed vulnerabilities will be turned off.  - If the repository has no other active projects, then remove any webhooks related to the project.
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deactivateAsync(String orgId, String projectId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deactivateValidateBeforeCall(orgId, projectId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteAProject
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteAProjectCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteAProjectValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling deleteAProject(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling deleteAProject(Async)");
        }

        return deleteAProjectCall(orgId, projectId, _callback);

    }

    /**
     * Delete a project
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deleteAProject(String orgId, String projectId) throws ApiException {
        deleteAProjectWithHttpInfo(orgId, projectId);
    }

    /**
     * Delete a project
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteAProjectWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = deleteAProjectValidateBeforeCall(orgId, projectId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a project (asynchronously)
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteAProjectAsync(String orgId, String projectId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteAProjectValidateBeforeCall(orgId, projectId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteIgnores
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteIgnoresCall(String orgId, String projectId, String issueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/ignore/{issueId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteIgnoresValidateBeforeCall(String orgId, String projectId, String issueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling deleteIgnores(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling deleteIgnores(Async)");
        }

        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling deleteIgnores(Async)");
        }

        return deleteIgnoresCall(orgId, projectId, issueId, _callback);

    }

    /**
     * Delete ignores
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void deleteIgnores(String orgId, String projectId, String issueId) throws ApiException {
        deleteIgnoresWithHttpInfo(orgId, projectId, issueId);
    }

    /**
     * Delete ignores
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteIgnoresWithHttpInfo(String orgId, String projectId, String issueId) throws ApiException {
        okhttp3.Call localVarCall = deleteIgnoresValidateBeforeCall(orgId, projectId, issueId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete ignores (asynchronously)
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteIgnoresAsync(String orgId, String projectId, String issueId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteIgnoresValidateBeforeCall(orgId, projectId, issueId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteProjectSettings
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteProjectSettingsCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/settings"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteProjectSettingsValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling deleteProjectSettings(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling deleteProjectSettings(Async)");
        }

        return deleteProjectSettingsCall(orgId, projectId, _callback);

    }

    /**
     * Delete project settings
     * Deleting project settings will set the project to inherit default settings from its integration.
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void deleteProjectSettings(String orgId, String projectId) throws ApiException {
        deleteProjectSettingsWithHttpInfo(orgId, projectId);
    }

    /**
     * Delete project settings
     * Deleting project settings will set the project to inherit default settings from its integration.
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteProjectSettingsWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = deleteProjectSettingsValidateBeforeCall(orgId, projectId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete project settings (asynchronously)
     * Deleting project settings will set the project to inherit default settings from its integration.
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteProjectSettingsAsync(String orgId, String projectId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteProjectSettingsValidateBeforeCall(orgId, projectId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProjectDependencyGraph
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> * A reference implementation of the graph, as well as conversion functions to/from legacy tree format, can be found at: https://github.com/snyk/dep-graph.  * The object might contain additional fields in the future, in a backward-compatible way (&#x60;schemaVersion&#x60; will change accordingly). </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProjectDependencyGraphCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/dep-graph"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getProjectDependencyGraphValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling getProjectDependencyGraph(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling getProjectDependencyGraph(Async)");
        }

        return getProjectDependencyGraphCall(orgId, projectId, _callback);

    }

    /**
     * Get Project dependency graph
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @return GetProjectDependencyGraph200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> * A reference implementation of the graph, as well as conversion functions to/from legacy tree format, can be found at: https://github.com/snyk/dep-graph.  * The object might contain additional fields in the future, in a backward-compatible way (&#x60;schemaVersion&#x60; will change accordingly). </td><td>  -  </td></tr>
     </table>
     */
    public GetProjectDependencyGraph200Response getProjectDependencyGraph(String orgId, String projectId) throws ApiException {
        ApiResponse<GetProjectDependencyGraph200Response> localVarResp = getProjectDependencyGraphWithHttpInfo(orgId, projectId);
        return localVarResp.getData();
    }

    /**
     * Get Project dependency graph
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @return ApiResponse&lt;GetProjectDependencyGraph200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> * A reference implementation of the graph, as well as conversion functions to/from legacy tree format, can be found at: https://github.com/snyk/dep-graph.  * The object might contain additional fields in the future, in a backward-compatible way (&#x60;schemaVersion&#x60; will change accordingly). </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetProjectDependencyGraph200Response> getProjectDependencyGraphWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = getProjectDependencyGraphValidateBeforeCall(orgId, projectId, null);
        Type localVarReturnType = new TypeToken<GetProjectDependencyGraph200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Project dependency graph (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> * A reference implementation of the graph, as well as conversion functions to/from legacy tree format, can be found at: https://github.com/snyk/dep-graph.  * The object might contain additional fields in the future, in a backward-compatible way (&#x60;schemaVersion&#x60; will change accordingly). </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProjectDependencyGraphAsync(String orgId, String projectId, final ApiCallback<GetProjectDependencyGraph200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProjectDependencyGraphValidateBeforeCall(orgId, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetProjectDependencyGraph200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllAggregatedIssues
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllAggregatedIssuesCall(String orgId, String projectId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = listAllAggregatedIssuesRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/aggregated-issues"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call listAllAggregatedIssuesValidateBeforeCall(String orgId, String projectId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllAggregatedIssues(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllAggregatedIssues(Async)");
        }

        return listAllAggregatedIssuesCall(orgId, projectId, listAllAggregatedIssuesRequest, _callback);

    }

    /**
     * List all Aggregated issues
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @return ListAllAggregatedIssues200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ListAllAggregatedIssues200Response listAllAggregatedIssues(String orgId, String projectId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest) throws ApiException {
        ApiResponse<ListAllAggregatedIssues200Response> localVarResp = listAllAggregatedIssuesWithHttpInfo(orgId, projectId, listAllAggregatedIssuesRequest);
        return localVarResp.getData();
    }

    /**
     * List all Aggregated issues
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @return ApiResponse&lt;ListAllAggregatedIssues200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListAllAggregatedIssues200Response> listAllAggregatedIssuesWithHttpInfo(String orgId, String projectId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest) throws ApiException {
        okhttp3.Call localVarCall = listAllAggregatedIssuesValidateBeforeCall(orgId, projectId, listAllAggregatedIssuesRequest, null);
        Type localVarReturnType = new TypeToken<ListAllAggregatedIssues200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all Aggregated issues (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return issues for. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllAggregatedIssuesAsync(String orgId, String projectId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest, final ApiCallback<ListAllAggregatedIssues200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllAggregatedIssuesValidateBeforeCall(orgId, projectId, listAllAggregatedIssuesRequest, _callback);
        Type localVarReturnType = new TypeToken<ListAllAggregatedIssues200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllIgnores
     * @param orgId The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list ignores for. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllIgnoresCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/ignores"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listAllIgnoresValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllIgnores(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllIgnores(Async)");
        }

        return listAllIgnoresCall(orgId, projectId, _callback);

    }

    /**
     * List all ignores
     * Temporary ignores include an &#x60;expires&#x60; attribute, while permanent ignores do not.
     * @param orgId The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list ignores for. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object listAllIgnores(String orgId, String projectId) throws ApiException {
        ApiResponse<Object> localVarResp = listAllIgnoresWithHttpInfo(orgId, projectId);
        return localVarResp.getData();
    }

    /**
     * List all ignores
     * Temporary ignores include an &#x60;expires&#x60; attribute, while permanent ignores do not.
     * @param orgId The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list ignores for. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> listAllIgnoresWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = listAllIgnoresValidateBeforeCall(orgId, projectId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all ignores (asynchronously)
     * Temporary ignores include an &#x60;expires&#x60; attribute, while permanent ignores do not.
     * @param orgId The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list ignores for. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllIgnoresAsync(String orgId, String projectId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllIgnoresValidateBeforeCall(orgId, projectId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllJiraIssues
     * @param orgId The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list Jira issues for. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllJiraIssuesCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/jira-issues"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*"
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
    private okhttp3.Call listAllJiraIssuesValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllJiraIssues(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllJiraIssues(Async)");
        }

        return listAllJiraIssuesCall(orgId, projectId, _callback);

    }

    /**
     * List all jira issues
     * 
     * @param orgId The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list Jira issues for. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object listAllJiraIssues(String orgId, String projectId) throws ApiException {
        ApiResponse<Object> localVarResp = listAllJiraIssuesWithHttpInfo(orgId, projectId);
        return localVarResp.getData();
    }

    /**
     * List all jira issues
     * 
     * @param orgId The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list Jira issues for. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> listAllJiraIssuesWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = listAllJiraIssuesValidateBeforeCall(orgId, projectId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all jira issues (asynchronously)
     * 
     * @param orgId The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to list Jira issues for. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllJiraIssuesAsync(String orgId, String projectId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllJiraIssuesValidateBeforeCall(orgId, projectId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllProjectIssuePaths
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (optional, default to latest)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectIssuePathsCall(String orgId, String projectId, String issueId, String snapshotId, BigDecimal perPage, BigDecimal page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/issue/{issueId}/paths"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (snapshotId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("snapshotId", snapshotId));
        }

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("perPage", perPage));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        final String[] localVarAccepts = {
            "*/*"
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
    private okhttp3.Call listAllProjectIssuePathsValidateBeforeCall(String orgId, String projectId, String issueId, String snapshotId, BigDecimal perPage, BigDecimal page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllProjectIssuePaths(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllProjectIssuePaths(Async)");
        }

        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling listAllProjectIssuePaths(Async)");
        }

        return listAllProjectIssuePathsCall(orgId, projectId, issueId, snapshotId, perPage, page, _callback);

    }

    /**
     * List all project issue paths
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (optional, default to latest)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @return ListAllProjectSnapshotIssuePaths200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public ListAllProjectSnapshotIssuePaths200Response listAllProjectIssuePaths(String orgId, String projectId, String issueId, String snapshotId, BigDecimal perPage, BigDecimal page) throws ApiException {
        ApiResponse<ListAllProjectSnapshotIssuePaths200Response> localVarResp = listAllProjectIssuePathsWithHttpInfo(orgId, projectId, issueId, snapshotId, perPage, page);
        return localVarResp.getData();
    }

    /**
     * List all project issue paths
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (optional, default to latest)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @return ApiResponse&lt;ListAllProjectSnapshotIssuePaths200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<ListAllProjectSnapshotIssuePaths200Response> listAllProjectIssuePathsWithHttpInfo(String orgId, String projectId, String issueId, String snapshotId, BigDecimal perPage, BigDecimal page) throws ApiException {
        okhttp3.Call localVarCall = listAllProjectIssuePathsValidateBeforeCall(orgId, projectId, issueId, snapshotId, perPage, page, null);
        Type localVarReturnType = new TypeToken<ListAllProjectSnapshotIssuePaths200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all project issue paths (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (optional, default to latest)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectIssuePathsAsync(String orgId, String projectId, String issueId, String snapshotId, BigDecimal perPage, BigDecimal page, final ApiCallback<ListAllProjectSnapshotIssuePaths200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllProjectIssuePathsValidateBeforeCall(orgId, projectId, issueId, snapshotId, perPage, page, _callback);
        Type localVarReturnType = new TypeToken<ListAllProjectSnapshotIssuePaths200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllProjectSnapshotAggregatedIssues
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param snapshotId The snapshot ID. If set to latest, the most recent snapshot will be used. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectSnapshotAggregatedIssuesCall(String orgId, String projectId, String snapshotId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = listAllAggregatedIssuesRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/history/{snapshotId}/aggregated-issues"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "snapshotId" + "}", localVarApiClient.escapeString(snapshotId.toString()));

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
    private okhttp3.Call listAllProjectSnapshotAggregatedIssuesValidateBeforeCall(String orgId, String projectId, String snapshotId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllProjectSnapshotAggregatedIssues(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllProjectSnapshotAggregatedIssues(Async)");
        }

        // verify the required parameter 'snapshotId' is set
        if (snapshotId == null) {
            throw new ApiException("Missing the required parameter 'snapshotId' when calling listAllProjectSnapshotAggregatedIssues(Async)");
        }

        return listAllProjectSnapshotAggregatedIssuesCall(orgId, projectId, snapshotId, listAllAggregatedIssuesRequest, _callback);

    }

    /**
     * List all project snapshot aggregated issues
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param snapshotId The snapshot ID. If set to latest, the most recent snapshot will be used. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @return ListAllAggregatedIssues200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ListAllAggregatedIssues200Response listAllProjectSnapshotAggregatedIssues(String orgId, String projectId, String snapshotId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest) throws ApiException {
        ApiResponse<ListAllAggregatedIssues200Response> localVarResp = listAllProjectSnapshotAggregatedIssuesWithHttpInfo(orgId, projectId, snapshotId, listAllAggregatedIssuesRequest);
        return localVarResp.getData();
    }

    /**
     * List all project snapshot aggregated issues
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param snapshotId The snapshot ID. If set to latest, the most recent snapshot will be used. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @return ApiResponse&lt;ListAllAggregatedIssues200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListAllAggregatedIssues200Response> listAllProjectSnapshotAggregatedIssuesWithHttpInfo(String orgId, String projectId, String snapshotId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest) throws ApiException {
        okhttp3.Call localVarCall = listAllProjectSnapshotAggregatedIssuesValidateBeforeCall(orgId, projectId, snapshotId, listAllAggregatedIssuesRequest, null);
        Type localVarReturnType = new TypeToken<ListAllAggregatedIssues200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all project snapshot aggregated issues (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param snapshotId The snapshot ID. If set to latest, the most recent snapshot will be used. (required)
     * @param listAllAggregatedIssuesRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectSnapshotAggregatedIssuesAsync(String orgId, String projectId, String snapshotId, ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest, final ApiCallback<ListAllAggregatedIssues200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllProjectSnapshotAggregatedIssuesValidateBeforeCall(orgId, projectId, snapshotId, listAllAggregatedIssuesRequest, _callback);
        Type localVarReturnType = new TypeToken<ListAllAggregatedIssues200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllProjectSnapshotIssuePaths
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectSnapshotIssuePathsCall(String orgId, String projectId, String snapshotId, String issueId, BigDecimal perPage, BigDecimal page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/history/{snapshotId}/issue/{issueId}/paths"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "snapshotId" + "}", localVarApiClient.escapeString(snapshotId.toString()))
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("perPage", perPage));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        final String[] localVarAccepts = {
            "*/*"
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
    private okhttp3.Call listAllProjectSnapshotIssuePathsValidateBeforeCall(String orgId, String projectId, String snapshotId, String issueId, BigDecimal perPage, BigDecimal page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllProjectSnapshotIssuePaths(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllProjectSnapshotIssuePaths(Async)");
        }

        // verify the required parameter 'snapshotId' is set
        if (snapshotId == null) {
            throw new ApiException("Missing the required parameter 'snapshotId' when calling listAllProjectSnapshotIssuePaths(Async)");
        }

        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling listAllProjectSnapshotIssuePaths(Async)");
        }

        return listAllProjectSnapshotIssuePathsCall(orgId, projectId, snapshotId, issueId, perPage, page, _callback);

    }

    /**
     * List all project snapshot issue paths
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @return ListAllProjectSnapshotIssuePaths200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public ListAllProjectSnapshotIssuePaths200Response listAllProjectSnapshotIssuePaths(String orgId, String projectId, String snapshotId, String issueId, BigDecimal perPage, BigDecimal page) throws ApiException {
        ApiResponse<ListAllProjectSnapshotIssuePaths200Response> localVarResp = listAllProjectSnapshotIssuePathsWithHttpInfo(orgId, projectId, snapshotId, issueId, perPage, page);
        return localVarResp.getData();
    }

    /**
     * List all project snapshot issue paths
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @return ApiResponse&lt;ListAllProjectSnapshotIssuePaths200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<ListAllProjectSnapshotIssuePaths200Response> listAllProjectSnapshotIssuePathsWithHttpInfo(String orgId, String projectId, String snapshotId, String issueId, BigDecimal perPage, BigDecimal page) throws ApiException {
        okhttp3.Call localVarCall = listAllProjectSnapshotIssuePathsValidateBeforeCall(orgId, projectId, snapshotId, issueId, perPage, page, null);
        Type localVarReturnType = new TypeToken<ListAllProjectSnapshotIssuePaths200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all project snapshot issue paths (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID for which to return issue paths. (required)
     * @param snapshotId The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. (required)
     * @param issueId The issue ID for which to return issue paths. (required)
     * @param perPage The number of results to return per page (1 - 1000, inclusive). (optional, default to 100)
     * @param page The page of results to return. (optional, default to 1)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectSnapshotIssuePathsAsync(String orgId, String projectId, String snapshotId, String issueId, BigDecimal perPage, BigDecimal page, final ApiCallback<ListAllProjectSnapshotIssuePaths200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllProjectSnapshotIssuePathsValidateBeforeCall(orgId, projectId, snapshotId, issueId, perPage, page, _callback);
        Type localVarReturnType = new TypeToken<ListAllProjectSnapshotIssuePaths200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllProjectSnapshots
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return snapshots for. (required)
     * @param perPage The number of results to return (the default is 10, the maximum is 100). (optional)
     * @param page The offset from which to start returning results from. (optional)
     * @param listAllProjectSnapshotsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectSnapshotsCall(String orgId, String projectId, BigDecimal perPage, BigDecimal page, ListAllProjectSnapshotsRequest listAllProjectSnapshotsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = listAllProjectSnapshotsRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/history"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (perPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("perPage", perPage));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
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
    private okhttp3.Call listAllProjectSnapshotsValidateBeforeCall(String orgId, String projectId, BigDecimal perPage, BigDecimal page, ListAllProjectSnapshotsRequest listAllProjectSnapshotsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllProjectSnapshots(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listAllProjectSnapshots(Async)");
        }

        return listAllProjectSnapshotsCall(orgId, projectId, perPage, page, listAllProjectSnapshotsRequest, _callback);

    }

    /**
     * List all project snapshots
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return snapshots for. (required)
     * @param perPage The number of results to return (the default is 10, the maximum is 100). (optional)
     * @param page The offset from which to start returning results from. (optional)
     * @param listAllProjectSnapshotsRequest  (optional)
     * @return ListAllProjectSnapshots200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public ListAllProjectSnapshots200Response listAllProjectSnapshots(String orgId, String projectId, BigDecimal perPage, BigDecimal page, ListAllProjectSnapshotsRequest listAllProjectSnapshotsRequest) throws ApiException {
        ApiResponse<ListAllProjectSnapshots200Response> localVarResp = listAllProjectSnapshotsWithHttpInfo(orgId, projectId, perPage, page, listAllProjectSnapshotsRequest);
        return localVarResp.getData();
    }

    /**
     * List all project snapshots
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return snapshots for. (required)
     * @param perPage The number of results to return (the default is 10, the maximum is 100). (optional)
     * @param page The offset from which to start returning results from. (optional)
     * @param listAllProjectSnapshotsRequest  (optional)
     * @return ApiResponse&lt;ListAllProjectSnapshots200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<ListAllProjectSnapshots200Response> listAllProjectSnapshotsWithHttpInfo(String orgId, String projectId, BigDecimal perPage, BigDecimal page, ListAllProjectSnapshotsRequest listAllProjectSnapshotsRequest) throws ApiException {
        okhttp3.Call localVarCall = listAllProjectSnapshotsValidateBeforeCall(orgId, projectId, perPage, page, listAllProjectSnapshotsRequest, null);
        Type localVarReturnType = new TypeToken<ListAllProjectSnapshots200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all project snapshots (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to return snapshots for. (required)
     * @param perPage The number of results to return (the default is 10, the maximum is 100). (optional)
     * @param page The offset from which to start returning results from. (optional)
     * @param listAllProjectSnapshotsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Link -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectSnapshotsAsync(String orgId, String projectId, BigDecimal perPage, BigDecimal page, ListAllProjectSnapshotsRequest listAllProjectSnapshotsRequest, final ApiCallback<ListAllProjectSnapshots200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllProjectSnapshotsValidateBeforeCall(orgId, projectId, perPage, page, listAllProjectSnapshotsRequest, _callback);
        Type localVarReturnType = new TypeToken<ListAllProjectSnapshots200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listAllProjects
     * @param orgId The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param listAllProjectsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectsCall(String orgId, ListAllProjectsRequest listAllProjectsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = listAllProjectsRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/projects"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()));

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
    private okhttp3.Call listAllProjectsValidateBeforeCall(String orgId, ListAllProjectsRequest listAllProjectsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listAllProjects(Async)");
        }

        return listAllProjectsCall(orgId, listAllProjectsRequest, _callback);

    }

    /**
     * List all projects
     * 
     * @param orgId The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param listAllProjectsRequest  (optional)
     * @return ListAllProjects200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ListAllProjects200Response listAllProjects(String orgId, ListAllProjectsRequest listAllProjectsRequest) throws ApiException {
        ApiResponse<ListAllProjects200Response> localVarResp = listAllProjectsWithHttpInfo(orgId, listAllProjectsRequest);
        return localVarResp.getData();
    }

    /**
     * List all projects
     * 
     * @param orgId The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param listAllProjectsRequest  (optional)
     * @return ApiResponse&lt;ListAllProjects200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListAllProjects200Response> listAllProjectsWithHttpInfo(String orgId, ListAllProjectsRequest listAllProjectsRequest) throws ApiException {
        okhttp3.Call localVarCall = listAllProjectsValidateBeforeCall(orgId, listAllProjectsRequest, null);
        Type localVarReturnType = new TypeToken<ListAllProjects200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all projects (asynchronously)
     * 
     * @param orgId The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param listAllProjectsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listAllProjectsAsync(String orgId, ListAllProjectsRequest listAllProjectsRequest, final ApiCallback<ListAllProjects200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listAllProjectsValidateBeforeCall(orgId, listAllProjectsRequest, _callback);
        Type localVarReturnType = new TypeToken<ListAllProjects200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listProjectSettings
     * @param orgId The organization ID to which the project belongs. The API_KEY must have access to this organization. (required)
     * @param projectId The project ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain only attributes that can be updated (see &#x60;ATTRIBUTES&#x60; section in &#x60;Update project settings&#x60;) and that have been previously set. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listProjectSettingsCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/settings"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listProjectSettingsValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling listProjectSettings(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling listProjectSettings(Async)");
        }

        return listProjectSettingsCall(orgId, projectId, _callback);

    }

    /**
     * List project settings
     * 
     * @param orgId The organization ID to which the project belongs. The API_KEY must have access to this organization. (required)
     * @param projectId The project ID (required)
     * @return ListProjectSettings200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain only attributes that can be updated (see &#x60;ATTRIBUTES&#x60; section in &#x60;Update project settings&#x60;) and that have been previously set. </td><td>  -  </td></tr>
     </table>
     */
    public ListProjectSettings200Response listProjectSettings(String orgId, String projectId) throws ApiException {
        ApiResponse<ListProjectSettings200Response> localVarResp = listProjectSettingsWithHttpInfo(orgId, projectId);
        return localVarResp.getData();
    }

    /**
     * List project settings
     * 
     * @param orgId The organization ID to which the project belongs. The API_KEY must have access to this organization. (required)
     * @param projectId The project ID (required)
     * @return ApiResponse&lt;ListProjectSettings200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain only attributes that can be updated (see &#x60;ATTRIBUTES&#x60; section in &#x60;Update project settings&#x60;) and that have been previously set. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListProjectSettings200Response> listProjectSettingsWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = listProjectSettingsValidateBeforeCall(orgId, projectId, null);
        Type localVarReturnType = new TypeToken<ListProjectSettings200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List project settings (asynchronously)
     * 
     * @param orgId The organization ID to which the project belongs. The API_KEY must have access to this organization. (required)
     * @param projectId The project ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain only attributes that can be updated (see &#x60;ATTRIBUTES&#x60; section in &#x60;Update project settings&#x60;) and that have been previously set. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listProjectSettingsAsync(String orgId, String projectId, final ApiCallback<ListProjectSettings200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listProjectSettingsValidateBeforeCall(orgId, projectId, _callback);
        Type localVarReturnType = new TypeToken<ListProjectSettings200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for moveProjectToADifferentOrganization
     * @param orgId The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed. (required)
     * @param projectId The project ID. (required)
     * @param moveProjectToADifferentOrganizationRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call moveProjectToADifferentOrganizationCall(String orgId, String projectId, MoveProjectToADifferentOrganizationRequest moveProjectToADifferentOrganizationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = moveProjectToADifferentOrganizationRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/move"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call moveProjectToADifferentOrganizationValidateBeforeCall(String orgId, String projectId, MoveProjectToADifferentOrganizationRequest moveProjectToADifferentOrganizationRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling moveProjectToADifferentOrganization(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling moveProjectToADifferentOrganization(Async)");
        }

        return moveProjectToADifferentOrganizationCall(orgId, projectId, moveProjectToADifferentOrganizationRequest, _callback);

    }

    /**
     * Move project to a different organization
     * Note: when moving a project to a new organization, the historical data used for reporting does not move with it.
     * @param orgId The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed. (required)
     * @param projectId The project ID. (required)
     * @param moveProjectToADifferentOrganizationRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void moveProjectToADifferentOrganization(String orgId, String projectId, MoveProjectToADifferentOrganizationRequest moveProjectToADifferentOrganizationRequest) throws ApiException {
        moveProjectToADifferentOrganizationWithHttpInfo(orgId, projectId, moveProjectToADifferentOrganizationRequest);
    }

    /**
     * Move project to a different organization
     * Note: when moving a project to a new organization, the historical data used for reporting does not move with it.
     * @param orgId The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed. (required)
     * @param projectId The project ID. (required)
     * @param moveProjectToADifferentOrganizationRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> moveProjectToADifferentOrganizationWithHttpInfo(String orgId, String projectId, MoveProjectToADifferentOrganizationRequest moveProjectToADifferentOrganizationRequest) throws ApiException {
        okhttp3.Call localVarCall = moveProjectToADifferentOrganizationValidateBeforeCall(orgId, projectId, moveProjectToADifferentOrganizationRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Move project to a different organization (asynchronously)
     * Note: when moving a project to a new organization, the historical data used for reporting does not move with it.
     * @param orgId The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed. (required)
     * @param projectId The project ID. (required)
     * @param moveProjectToADifferentOrganizationRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call moveProjectToADifferentOrganizationAsync(String orgId, String projectId, MoveProjectToADifferentOrganizationRequest moveProjectToADifferentOrganizationRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = moveProjectToADifferentOrganizationValidateBeforeCall(orgId, projectId, moveProjectToADifferentOrganizationRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for removeATagFromAProject
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param addATagToAProjectRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeATagFromAProjectCall(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addATagToAProjectRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/tags/remove"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call removeATagFromAProjectValidateBeforeCall(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling removeATagFromAProject(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling removeATagFromAProject(Async)");
        }

        return removeATagFromAProjectCall(orgId, projectId, addATagToAProjectRequest, _callback);

    }

    /**
     * Remove a tag from a project
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param addATagToAProjectRequest  (optional)
     * @return AddATagToAProject200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public AddATagToAProject200Response removeATagFromAProject(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest) throws ApiException {
        ApiResponse<AddATagToAProject200Response> localVarResp = removeATagFromAProjectWithHttpInfo(orgId, projectId, addATagToAProjectRequest);
        return localVarResp.getData();
    }

    /**
     * Remove a tag from a project
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param addATagToAProjectRequest  (optional)
     * @return ApiResponse&lt;AddATagToAProject200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddATagToAProject200Response> removeATagFromAProjectWithHttpInfo(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest) throws ApiException {
        okhttp3.Call localVarCall = removeATagFromAProjectValidateBeforeCall(orgId, projectId, addATagToAProjectRequest, null);
        Type localVarReturnType = new TypeToken<AddATagToAProject200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Remove a tag from a project (asynchronously)
     * 
     * @param orgId The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to remove a tag from (required)
     * @param addATagToAProjectRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeATagFromAProjectAsync(String orgId, String projectId, AddATagToAProjectRequest addATagToAProjectRequest, final ApiCallback<AddATagToAProject200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = removeATagFromAProjectValidateBeforeCall(orgId, projectId, addATagToAProjectRequest, _callback);
        Type localVarReturnType = new TypeToken<AddATagToAProject200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for replaceIgnores
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call replaceIgnoresCall(String orgId, String projectId, String issueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/ignore/{issueId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call replaceIgnoresValidateBeforeCall(String orgId, String projectId, String issueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling replaceIgnores(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling replaceIgnores(Async)");
        }

        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling replaceIgnores(Async)");
        }

        return replaceIgnoresCall(orgId, projectId, issueId, _callback);

    }

    /**
     * Replace ignores
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @return List&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<Object> replaceIgnores(String orgId, String projectId, String issueId) throws ApiException {
        ApiResponse<List<Object>> localVarResp = replaceIgnoresWithHttpInfo(orgId, projectId, issueId);
        return localVarResp.getData();
    }

    /**
     * Replace ignores
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @return ApiResponse&lt;List&lt;Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Object>> replaceIgnoresWithHttpInfo(String orgId, String projectId, String issueId) throws ApiException {
        okhttp3.Call localVarCall = replaceIgnoresValidateBeforeCall(orgId, projectId, issueId, null);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Replace ignores (asynchronously)
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param issueId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call replaceIgnoresAsync(String orgId, String projectId, String issueId, final ApiCallback<List<Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = replaceIgnoresValidateBeforeCall(orgId, projectId, issueId, _callback);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for retrieveASingleProject
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call retrieveASingleProjectCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call retrieveASingleProjectValidateBeforeCall(String orgId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling retrieveASingleProject(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling retrieveASingleProject(Async)");
        }

        return retrieveASingleProjectCall(orgId, projectId, _callback);

    }

    /**
     * Retrieve a single project
     * 
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @return RetrieveASingleProject200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public RetrieveASingleProject200Response retrieveASingleProject(String orgId, String projectId) throws ApiException {
        ApiResponse<RetrieveASingleProject200Response> localVarResp = retrieveASingleProjectWithHttpInfo(orgId, projectId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a single project
     * 
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @return ApiResponse&lt;RetrieveASingleProject200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<RetrieveASingleProject200Response> retrieveASingleProjectWithHttpInfo(String orgId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = retrieveASingleProjectValidateBeforeCall(orgId, projectId, null);
        Type localVarReturnType = new TypeToken<RetrieveASingleProject200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a single project (asynchronously)
     * 
     * @param orgId The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call retrieveASingleProjectAsync(String orgId, String projectId, final ApiCallback<RetrieveASingleProject200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = retrieveASingleProjectValidateBeforeCall(orgId, projectId, _callback);
        Type localVarReturnType = new TypeToken<RetrieveASingleProject200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for retrieveIgnore
     * @param orgId The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to modify ignores for. (required)
     * @param issueId The issue ID to modify ignores for. Can be a vulnerability or a license Issue. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call retrieveIgnoreCall(String orgId, String projectId, String issueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/org/{orgId}/project/{projectId}/ignore/{issueId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "issueId" + "}", localVarApiClient.escapeString(issueId.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call retrieveIgnoreValidateBeforeCall(String orgId, String projectId, String issueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling retrieveIgnore(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling retrieveIgnore(Async)");
        }

        // verify the required parameter 'issueId' is set
        if (issueId == null) {
            throw new ApiException("Missing the required parameter 'issueId' when calling retrieveIgnore(Async)");
        }

        return retrieveIgnoreCall(orgId, projectId, issueId, _callback);

    }

    /**
     * Retrieve ignore
     * 
     * @param orgId The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to modify ignores for. (required)
     * @param issueId The issue ID to modify ignores for. Can be a vulnerability or a license Issue. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object retrieveIgnore(String orgId, String projectId, String issueId) throws ApiException {
        ApiResponse<Object> localVarResp = retrieveIgnoreWithHttpInfo(orgId, projectId, issueId);
        return localVarResp.getData();
    }

    /**
     * Retrieve ignore
     * 
     * @param orgId The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to modify ignores for. (required)
     * @param issueId The issue ID to modify ignores for. Can be a vulnerability or a license Issue. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> retrieveIgnoreWithHttpInfo(String orgId, String projectId, String issueId) throws ApiException {
        okhttp3.Call localVarCall = retrieveIgnoreValidateBeforeCall(orgId, projectId, issueId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve ignore (asynchronously)
     * 
     * @param orgId The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization. (required)
     * @param projectId The project ID to modify ignores for. (required)
     * @param issueId The issue ID to modify ignores for. Can be a vulnerability or a license Issue. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call retrieveIgnoreAsync(String orgId, String projectId, String issueId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = retrieveIgnoreValidateBeforeCall(orgId, projectId, issueId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateAProject
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateAProjectRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateAProjectCall(String orgId, String projectId, UpdateAProjectRequest updateAProjectRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateAProjectRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateAProjectValidateBeforeCall(String orgId, String projectId, UpdateAProjectRequest updateAProjectRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling updateAProject(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling updateAProject(Async)");
        }

        return updateAProjectCall(orgId, projectId, updateAProjectRequest, _callback);

    }

    /**
     * Update a project
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateAProjectRequest  (optional)
     * @return RetrieveASingleProject200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public RetrieveASingleProject200Response updateAProject(String orgId, String projectId, UpdateAProjectRequest updateAProjectRequest) throws ApiException {
        ApiResponse<RetrieveASingleProject200Response> localVarResp = updateAProjectWithHttpInfo(orgId, projectId, updateAProjectRequest);
        return localVarResp.getData();
    }

    /**
     * Update a project
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateAProjectRequest  (optional)
     * @return ApiResponse&lt;RetrieveASingleProject200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<RetrieveASingleProject200Response> updateAProjectWithHttpInfo(String orgId, String projectId, UpdateAProjectRequest updateAProjectRequest) throws ApiException {
        okhttp3.Call localVarCall = updateAProjectValidateBeforeCall(orgId, projectId, updateAProjectRequest, null);
        Type localVarReturnType = new TypeToken<RetrieveASingleProject200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a project (asynchronously)
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateAProjectRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateAProjectAsync(String orgId, String projectId, UpdateAProjectRequest updateAProjectRequest, final ApiCallback<RetrieveASingleProject200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateAProjectValidateBeforeCall(orgId, projectId, updateAProjectRequest, _callback);
        Type localVarReturnType = new TypeToken<RetrieveASingleProject200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateProjectSettings
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateProjectSettingsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain the attributes and values that have been sent in the request and successfully updated. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateProjectSettingsCall(String orgId, String projectId, UpdateProjectSettingsRequest updateProjectSettingsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateProjectSettingsRequest;

        // create path and map variables
        String localVarPath = "/org/{orgId}/project/{projectId}/settings"
            .replace("{" + "orgId" + "}", localVarApiClient.escapeString(orgId.toString()))
            .replace("{" + "projectId" + "}", localVarApiClient.escapeString(projectId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateProjectSettingsValidateBeforeCall(String orgId, String projectId, UpdateProjectSettingsRequest updateProjectSettingsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'orgId' is set
        if (orgId == null) {
            throw new ApiException("Missing the required parameter 'orgId' when calling updateProjectSettings(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling updateProjectSettings(Async)");
        }

        return updateProjectSettingsCall(orgId, projectId, updateProjectSettingsRequest, _callback);

    }

    /**
     * Update project settings
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateProjectSettingsRequest  (optional)
     * @return ListProjectSettings200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain the attributes and values that have been sent in the request and successfully updated. </td><td>  -  </td></tr>
     </table>
     */
    public ListProjectSettings200Response updateProjectSettings(String orgId, String projectId, UpdateProjectSettingsRequest updateProjectSettingsRequest) throws ApiException {
        ApiResponse<ListProjectSettings200Response> localVarResp = updateProjectSettingsWithHttpInfo(orgId, projectId, updateProjectSettingsRequest);
        return localVarResp.getData();
    }

    /**
     * Update project settings
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateProjectSettingsRequest  (optional)
     * @return ApiResponse&lt;ListProjectSettings200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain the attributes and values that have been sent in the request and successfully updated. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListProjectSettings200Response> updateProjectSettingsWithHttpInfo(String orgId, String projectId, UpdateProjectSettingsRequest updateProjectSettingsRequest) throws ApiException {
        okhttp3.Call localVarCall = updateProjectSettingsValidateBeforeCall(orgId, projectId, updateProjectSettingsRequest, null);
        Type localVarReturnType = new TypeToken<ListProjectSettings200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update project settings (asynchronously)
     * 
     * @param orgId Automatically added (required)
     * @param projectId Automatically added (required)
     * @param updateProjectSettingsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The response will contain the attributes and values that have been sent in the request and successfully updated. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateProjectSettingsAsync(String orgId, String projectId, UpdateProjectSettingsRequest updateProjectSettingsRequest, final ApiCallback<ListProjectSettings200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateProjectSettingsValidateBeforeCall(orgId, projectId, updateProjectSettingsRequest, _callback);
        Type localVarReturnType = new TypeToken<ListProjectSettings200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
