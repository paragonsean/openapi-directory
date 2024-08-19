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


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetListOfIssues200ResponseResultsInnerIssueIdentifiers;
import org.openapitools.client.model.GetListOfIssues200ResponseResultsInnerIssueSemver;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * GetListOfIssues200ResponseResultsInnerIssue
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:01.841417-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetListOfIssues200ResponseResultsInnerIssue {
  public static final String SERIALIZED_NAME_CV_S_SV3 = "CVSSv3";
  @SerializedName(SERIALIZED_NAME_CV_S_SV3)
  private String cvSSv3;

  public static final String SERIALIZED_NAME_CREDIT = "credit";
  @SerializedName(SERIALIZED_NAME_CREDIT)
  private List<Object> credit = new ArrayList<>();

  public static final String SERIALIZED_NAME_CVSS_SCORE = "cvssScore";
  @SerializedName(SERIALIZED_NAME_CVSS_SCORE)
  private BigDecimal cvssScore;

  public static final String SERIALIZED_NAME_DISCLOSURE_TIME = "disclosureTime";
  @SerializedName(SERIALIZED_NAME_DISCLOSURE_TIME)
  private String disclosureTime;

  public static final String SERIALIZED_NAME_EXPLOIT_MATURITY = "exploitMaturity";
  @SerializedName(SERIALIZED_NAME_EXPLOIT_MATURITY)
  private String exploitMaturity;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IDENTIFIERS = "identifiers";
  @SerializedName(SERIALIZED_NAME_IDENTIFIERS)
  private GetListOfIssues200ResponseResultsInnerIssueIdentifiers identifiers;

  public static final String SERIALIZED_NAME_IGNORED = "ignored";
  @SerializedName(SERIALIZED_NAME_IGNORED)
  private List<Object> ignored = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_IGNORED = "isIgnored";
  @SerializedName(SERIALIZED_NAME_IS_IGNORED)
  private Boolean isIgnored;

  public static final String SERIALIZED_NAME_IS_PATCHABLE = "isPatchable";
  @SerializedName(SERIALIZED_NAME_IS_PATCHABLE)
  private Boolean isPatchable;

  public static final String SERIALIZED_NAME_IS_PATCHED = "isPatched";
  @SerializedName(SERIALIZED_NAME_IS_PATCHED)
  private Boolean isPatched;

  public static final String SERIALIZED_NAME_IS_PINNABLE = "isPinnable";
  @SerializedName(SERIALIZED_NAME_IS_PINNABLE)
  private Boolean isPinnable;

  public static final String SERIALIZED_NAME_IS_UPGRADABLE = "isUpgradable";
  @SerializedName(SERIALIZED_NAME_IS_UPGRADABLE)
  private Boolean isUpgradable;

  public static final String SERIALIZED_NAME_JIRA_ISSUE_URL = "jiraIssueUrl";
  @SerializedName(SERIALIZED_NAME_JIRA_ISSUE_URL)
  private String jiraIssueUrl;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_ORIGINAL_SEVERITY = "originalSeverity";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_SEVERITY)
  private String originalSeverity;

  public static final String SERIALIZED_NAME_PACKAGE = "package";
  @SerializedName(SERIALIZED_NAME_PACKAGE)
  private String _package;

  public static final String SERIALIZED_NAME_PACKAGE_MANAGER = "packageManager";
  @SerializedName(SERIALIZED_NAME_PACKAGE_MANAGER)
  private String packageManager;

  public static final String SERIALIZED_NAME_PATCHES = "patches";
  @SerializedName(SERIALIZED_NAME_PATCHES)
  private List<Object> patches = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRIORITY_SCORE = "priorityScore";
  @SerializedName(SERIALIZED_NAME_PRIORITY_SCORE)
  private BigDecimal priorityScore;

  public static final String SERIALIZED_NAME_PUBLICATION_TIME = "publicationTime";
  @SerializedName(SERIALIZED_NAME_PUBLICATION_TIME)
  private String publicationTime;

  public static final String SERIALIZED_NAME_SEMVER = "semver";
  @SerializedName(SERIALIZED_NAME_SEMVER)
  private GetListOfIssues200ResponseResultsInnerIssueSemver semver;

  public static final String SERIALIZED_NAME_SEVERITY = "severity";
  @SerializedName(SERIALIZED_NAME_SEVERITY)
  private String severity;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_UNIQUE_SEVERITIES_LIST = "uniqueSeveritiesList";
  @SerializedName(SERIALIZED_NAME_UNIQUE_SEVERITIES_LIST)
  private List<Object> uniqueSeveritiesList = new ArrayList<>();

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public GetListOfIssues200ResponseResultsInnerIssue() {
  }

  public GetListOfIssues200ResponseResultsInnerIssue cvSSv3(String cvSSv3) {
    this.cvSSv3 = cvSSv3;
    return this;
  }

  /**
   * The CVSS v3 string that signifies how the CVSS score was calculated (not applicable to licenses)
   * @return cvSSv3
   */
  @javax.annotation.Nullable
  public String getCvSSv3() {
    return cvSSv3;
  }

  public void setCvSSv3(String cvSSv3) {
    this.cvSSv3 = cvSSv3;
  }


  public GetListOfIssues200ResponseResultsInnerIssue credit(List<Object> credit) {
    this.credit = credit;
    return this;
  }

  public GetListOfIssues200ResponseResultsInnerIssue addCreditItem(Object creditItem) {
    if (this.credit == null) {
      this.credit = new ArrayList<>();
    }
    this.credit.add(creditItem);
    return this;
  }

  /**
   * The list of people responsible for first uncovering or reporting the issue (not applicable to licenses)
   * @return credit
   */
  @javax.annotation.Nullable
  public List<Object> getCredit() {
    return credit;
  }

  public void setCredit(List<Object> credit) {
    this.credit = credit;
  }


  public GetListOfIssues200ResponseResultsInnerIssue cvssScore(BigDecimal cvssScore) {
    this.cvssScore = cvssScore;
    return this;
  }

  /**
   * The CVSS score that results from running the CVSSv3 string (not applicable to licenses)
   * @return cvssScore
   */
  @javax.annotation.Nullable
  public BigDecimal getCvssScore() {
    return cvssScore;
  }

  public void setCvssScore(BigDecimal cvssScore) {
    this.cvssScore = cvssScore;
  }


  public GetListOfIssues200ResponseResultsInnerIssue disclosureTime(String disclosureTime) {
    this.disclosureTime = disclosureTime;
    return this;
  }

  /**
   * The date that the vulnerability was first disclosed (not applicable to licenses)
   * @return disclosureTime
   */
  @javax.annotation.Nullable
  public String getDisclosureTime() {
    return disclosureTime;
  }

  public void setDisclosureTime(String disclosureTime) {
    this.disclosureTime = disclosureTime;
  }


  public GetListOfIssues200ResponseResultsInnerIssue exploitMaturity(String exploitMaturity) {
    this.exploitMaturity = exploitMaturity;
    return this;
  }

  /**
   * The exploit maturity of the issue
   * @return exploitMaturity
   */
  @javax.annotation.Nonnull
  public String getExploitMaturity() {
    return exploitMaturity;
  }

  public void setExploitMaturity(String exploitMaturity) {
    this.exploitMaturity = exploitMaturity;
  }


  public GetListOfIssues200ResponseResultsInnerIssue id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The identifier of the issue
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public GetListOfIssues200ResponseResultsInnerIssue identifiers(GetListOfIssues200ResponseResultsInnerIssueIdentifiers identifiers) {
    this.identifiers = identifiers;
    return this;
  }

  /**
   * Get identifiers
   * @return identifiers
   */
  @javax.annotation.Nullable
  public GetListOfIssues200ResponseResultsInnerIssueIdentifiers getIdentifiers() {
    return identifiers;
  }

  public void setIdentifiers(GetListOfIssues200ResponseResultsInnerIssueIdentifiers identifiers) {
    this.identifiers = identifiers;
  }


  public GetListOfIssues200ResponseResultsInnerIssue ignored(List<Object> ignored) {
    this.ignored = ignored;
    return this;
  }

  public GetListOfIssues200ResponseResultsInnerIssue addIgnoredItem(Object ignoredItem) {
    if (this.ignored == null) {
      this.ignored = new ArrayList<>();
    }
    this.ignored.add(ignoredItem);
    return this;
  }

  /**
   * The list of ignore rules that were applied to the issue (only present if issue was ignored and no &#x60;groupBy&#x60; in the API request)
   * @return ignored
   */
  @javax.annotation.Nullable
  public List<Object> getIgnored() {
    return ignored;
  }

  public void setIgnored(List<Object> ignored) {
    this.ignored = ignored;
  }


  public GetListOfIssues200ResponseResultsInnerIssue isIgnored(Boolean isIgnored) {
    this.isIgnored = isIgnored;
    return this;
  }

  /**
   * Whether the issue has been ignored (only present if there is no &#x60;groupBy&#x60; in the API request)
   * @return isIgnored
   */
  @javax.annotation.Nullable
  public Boolean getIsIgnored() {
    return isIgnored;
  }

  public void setIsIgnored(Boolean isIgnored) {
    this.isIgnored = isIgnored;
  }


  public GetListOfIssues200ResponseResultsInnerIssue isPatchable(Boolean isPatchable) {
    this.isPatchable = isPatchable;
    return this;
  }

  /**
   * Whether the issue can be patched
   * @return isPatchable
   */
  @javax.annotation.Nullable
  public Boolean getIsPatchable() {
    return isPatchable;
  }

  public void setIsPatchable(Boolean isPatchable) {
    this.isPatchable = isPatchable;
  }


  public GetListOfIssues200ResponseResultsInnerIssue isPatched(Boolean isPatched) {
    this.isPatched = isPatched;
    return this;
  }

  /**
   * Whether the issue has been patched (not applicable to licenses and only present if there is no &#x60;groupBy&#x60; in the API request)
   * @return isPatched
   */
  @javax.annotation.Nullable
  public Boolean getIsPatched() {
    return isPatched;
  }

  public void setIsPatched(Boolean isPatched) {
    this.isPatched = isPatched;
  }


  public GetListOfIssues200ResponseResultsInnerIssue isPinnable(Boolean isPinnable) {
    this.isPinnable = isPinnable;
    return this;
  }

  /**
   * Whether the issue can be pinned
   * @return isPinnable
   */
  @javax.annotation.Nullable
  public Boolean getIsPinnable() {
    return isPinnable;
  }

  public void setIsPinnable(Boolean isPinnable) {
    this.isPinnable = isPinnable;
  }


  public GetListOfIssues200ResponseResultsInnerIssue isUpgradable(Boolean isUpgradable) {
    this.isUpgradable = isUpgradable;
    return this;
  }

  /**
   * Whether the issue can be fixed by upgrading to a later version of the dependency
   * @return isUpgradable
   */
  @javax.annotation.Nullable
  public Boolean getIsUpgradable() {
    return isUpgradable;
  }

  public void setIsUpgradable(Boolean isUpgradable) {
    this.isUpgradable = isUpgradable;
  }


  public GetListOfIssues200ResponseResultsInnerIssue jiraIssueUrl(String jiraIssueUrl) {
    this.jiraIssueUrl = jiraIssueUrl;
    return this;
  }

  /**
   * The link to the Jira issue attached to the vulnerability
   * @return jiraIssueUrl
   */
  @javax.annotation.Nullable
  public String getJiraIssueUrl() {
    return jiraIssueUrl;
  }

  public void setJiraIssueUrl(String jiraIssueUrl) {
    this.jiraIssueUrl = jiraIssueUrl;
  }


  public GetListOfIssues200ResponseResultsInnerIssue language(String language) {
    this.language = language;
    return this;
  }

  /**
   * The language of the issue
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public GetListOfIssues200ResponseResultsInnerIssue originalSeverity(String originalSeverity) {
    this.originalSeverity = originalSeverity;
    return this;
  }

  /**
   * The original severity status of the issue, as retrieved from Snyk Vulnerability database, before policies are applied
   * @return originalSeverity
   */
  @javax.annotation.Nonnull
  public String getOriginalSeverity() {
    return originalSeverity;
  }

  public void setOriginalSeverity(String originalSeverity) {
    this.originalSeverity = originalSeverity;
  }


  public GetListOfIssues200ResponseResultsInnerIssue _package(String _package) {
    this._package = _package;
    return this;
  }

  /**
   * The name of the package that the issue relates to
   * @return _package
   */
  @javax.annotation.Nonnull
  public String getPackage() {
    return _package;
  }

  public void setPackage(String _package) {
    this._package = _package;
  }


  public GetListOfIssues200ResponseResultsInnerIssue packageManager(String packageManager) {
    this.packageManager = packageManager;
    return this;
  }

  /**
   * The package manager of the issue
   * @return packageManager
   */
  @javax.annotation.Nullable
  public String getPackageManager() {
    return packageManager;
  }

  public void setPackageManager(String packageManager) {
    this.packageManager = packageManager;
  }


  public GetListOfIssues200ResponseResultsInnerIssue patches(List<Object> patches) {
    this.patches = patches;
    return this;
  }

  public GetListOfIssues200ResponseResultsInnerIssue addPatchesItem(Object patchesItem) {
    if (this.patches == null) {
      this.patches = new ArrayList<>();
    }
    this.patches.add(patchesItem);
    return this;
  }

  /**
   * A list of patches available for the given issue (not applicable to licenses)
   * @return patches
   */
  @javax.annotation.Nullable
  public List<Object> getPatches() {
    return patches;
  }

  public void setPatches(List<Object> patches) {
    this.patches = patches;
  }


  public GetListOfIssues200ResponseResultsInnerIssue priorityScore(BigDecimal priorityScore) {
    this.priorityScore = priorityScore;
    return this;
  }

  /**
   * The priority score ranging between 0-1000
   * @return priorityScore
   */
  @javax.annotation.Nullable
  public BigDecimal getPriorityScore() {
    return priorityScore;
  }

  public void setPriorityScore(BigDecimal priorityScore) {
    this.priorityScore = priorityScore;
  }


  public GetListOfIssues200ResponseResultsInnerIssue publicationTime(String publicationTime) {
    this.publicationTime = publicationTime;
    return this;
  }

  /**
   * The date that the vulnerability was first published by Snyk (not applicable to licenses)
   * @return publicationTime
   */
  @javax.annotation.Nullable
  public String getPublicationTime() {
    return publicationTime;
  }

  public void setPublicationTime(String publicationTime) {
    this.publicationTime = publicationTime;
  }


  public GetListOfIssues200ResponseResultsInnerIssue semver(GetListOfIssues200ResponseResultsInnerIssueSemver semver) {
    this.semver = semver;
    return this;
  }

  /**
   * Get semver
   * @return semver
   */
  @javax.annotation.Nullable
  public GetListOfIssues200ResponseResultsInnerIssueSemver getSemver() {
    return semver;
  }

  public void setSemver(GetListOfIssues200ResponseResultsInnerIssueSemver semver) {
    this.semver = semver;
  }


  public GetListOfIssues200ResponseResultsInnerIssue severity(String severity) {
    this.severity = severity;
    return this;
  }

  /**
   * The severity status of the issue, after policies are applied
   * @return severity
   */
  @javax.annotation.Nonnull
  public String getSeverity() {
    return severity;
  }

  public void setSeverity(String severity) {
    this.severity = severity;
  }


  public GetListOfIssues200ResponseResultsInnerIssue title(String title) {
    this.title = title;
    return this;
  }

  /**
   * The issue title
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public GetListOfIssues200ResponseResultsInnerIssue type(String type) {
    this.type = type;
    return this;
  }

  /**
   * The issue type, can be \&quot;vuln\&quot;, \&quot;license\&quot;
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public GetListOfIssues200ResponseResultsInnerIssue uniqueSeveritiesList(List<Object> uniqueSeveritiesList) {
    this.uniqueSeveritiesList = uniqueSeveritiesList;
    return this;
  }

  public GetListOfIssues200ResponseResultsInnerIssue addUniqueSeveritiesListItem(Object uniqueSeveritiesListItem) {
    if (this.uniqueSeveritiesList == null) {
      this.uniqueSeveritiesList = new ArrayList<>();
    }
    this.uniqueSeveritiesList.add(uniqueSeveritiesListItem);
    return this;
  }

  /**
   * A list of all severities in issue per projects
   * @return uniqueSeveritiesList
   */
  @javax.annotation.Nullable
  public List<Object> getUniqueSeveritiesList() {
    return uniqueSeveritiesList;
  }

  public void setUniqueSeveritiesList(List<Object> uniqueSeveritiesList) {
    this.uniqueSeveritiesList = uniqueSeveritiesList;
  }


  public GetListOfIssues200ResponseResultsInnerIssue url(String url) {
    this.url = url;
    return this;
  }

  /**
   * URL to a page containing information about the issue
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }


  public GetListOfIssues200ResponseResultsInnerIssue version(String version) {
    this.version = version;
    return this;
  }

  /**
   * The version of the package that the issue relates to
   * @return version
   */
  @javax.annotation.Nonnull
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetListOfIssues200ResponseResultsInnerIssue getListOfIssues200ResponseResultsInnerIssue = (GetListOfIssues200ResponseResultsInnerIssue) o;
    return Objects.equals(this.cvSSv3, getListOfIssues200ResponseResultsInnerIssue.cvSSv3) &&
        Objects.equals(this.credit, getListOfIssues200ResponseResultsInnerIssue.credit) &&
        Objects.equals(this.cvssScore, getListOfIssues200ResponseResultsInnerIssue.cvssScore) &&
        Objects.equals(this.disclosureTime, getListOfIssues200ResponseResultsInnerIssue.disclosureTime) &&
        Objects.equals(this.exploitMaturity, getListOfIssues200ResponseResultsInnerIssue.exploitMaturity) &&
        Objects.equals(this.id, getListOfIssues200ResponseResultsInnerIssue.id) &&
        Objects.equals(this.identifiers, getListOfIssues200ResponseResultsInnerIssue.identifiers) &&
        Objects.equals(this.ignored, getListOfIssues200ResponseResultsInnerIssue.ignored) &&
        Objects.equals(this.isIgnored, getListOfIssues200ResponseResultsInnerIssue.isIgnored) &&
        Objects.equals(this.isPatchable, getListOfIssues200ResponseResultsInnerIssue.isPatchable) &&
        Objects.equals(this.isPatched, getListOfIssues200ResponseResultsInnerIssue.isPatched) &&
        Objects.equals(this.isPinnable, getListOfIssues200ResponseResultsInnerIssue.isPinnable) &&
        Objects.equals(this.isUpgradable, getListOfIssues200ResponseResultsInnerIssue.isUpgradable) &&
        Objects.equals(this.jiraIssueUrl, getListOfIssues200ResponseResultsInnerIssue.jiraIssueUrl) &&
        Objects.equals(this.language, getListOfIssues200ResponseResultsInnerIssue.language) &&
        Objects.equals(this.originalSeverity, getListOfIssues200ResponseResultsInnerIssue.originalSeverity) &&
        Objects.equals(this._package, getListOfIssues200ResponseResultsInnerIssue._package) &&
        Objects.equals(this.packageManager, getListOfIssues200ResponseResultsInnerIssue.packageManager) &&
        Objects.equals(this.patches, getListOfIssues200ResponseResultsInnerIssue.patches) &&
        Objects.equals(this.priorityScore, getListOfIssues200ResponseResultsInnerIssue.priorityScore) &&
        Objects.equals(this.publicationTime, getListOfIssues200ResponseResultsInnerIssue.publicationTime) &&
        Objects.equals(this.semver, getListOfIssues200ResponseResultsInnerIssue.semver) &&
        Objects.equals(this.severity, getListOfIssues200ResponseResultsInnerIssue.severity) &&
        Objects.equals(this.title, getListOfIssues200ResponseResultsInnerIssue.title) &&
        Objects.equals(this.type, getListOfIssues200ResponseResultsInnerIssue.type) &&
        Objects.equals(this.uniqueSeveritiesList, getListOfIssues200ResponseResultsInnerIssue.uniqueSeveritiesList) &&
        Objects.equals(this.url, getListOfIssues200ResponseResultsInnerIssue.url) &&
        Objects.equals(this.version, getListOfIssues200ResponseResultsInnerIssue.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cvSSv3, credit, cvssScore, disclosureTime, exploitMaturity, id, identifiers, ignored, isIgnored, isPatchable, isPatched, isPinnable, isUpgradable, jiraIssueUrl, language, originalSeverity, _package, packageManager, patches, priorityScore, publicationTime, semver, severity, title, type, uniqueSeveritiesList, url, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetListOfIssues200ResponseResultsInnerIssue {\n");
    sb.append("    cvSSv3: ").append(toIndentedString(cvSSv3)).append("\n");
    sb.append("    credit: ").append(toIndentedString(credit)).append("\n");
    sb.append("    cvssScore: ").append(toIndentedString(cvssScore)).append("\n");
    sb.append("    disclosureTime: ").append(toIndentedString(disclosureTime)).append("\n");
    sb.append("    exploitMaturity: ").append(toIndentedString(exploitMaturity)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    identifiers: ").append(toIndentedString(identifiers)).append("\n");
    sb.append("    ignored: ").append(toIndentedString(ignored)).append("\n");
    sb.append("    isIgnored: ").append(toIndentedString(isIgnored)).append("\n");
    sb.append("    isPatchable: ").append(toIndentedString(isPatchable)).append("\n");
    sb.append("    isPatched: ").append(toIndentedString(isPatched)).append("\n");
    sb.append("    isPinnable: ").append(toIndentedString(isPinnable)).append("\n");
    sb.append("    isUpgradable: ").append(toIndentedString(isUpgradable)).append("\n");
    sb.append("    jiraIssueUrl: ").append(toIndentedString(jiraIssueUrl)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    originalSeverity: ").append(toIndentedString(originalSeverity)).append("\n");
    sb.append("    _package: ").append(toIndentedString(_package)).append("\n");
    sb.append("    packageManager: ").append(toIndentedString(packageManager)).append("\n");
    sb.append("    patches: ").append(toIndentedString(patches)).append("\n");
    sb.append("    priorityScore: ").append(toIndentedString(priorityScore)).append("\n");
    sb.append("    publicationTime: ").append(toIndentedString(publicationTime)).append("\n");
    sb.append("    semver: ").append(toIndentedString(semver)).append("\n");
    sb.append("    severity: ").append(toIndentedString(severity)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    uniqueSeveritiesList: ").append(toIndentedString(uniqueSeveritiesList)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("CVSSv3");
    openapiFields.add("credit");
    openapiFields.add("cvssScore");
    openapiFields.add("disclosureTime");
    openapiFields.add("exploitMaturity");
    openapiFields.add("id");
    openapiFields.add("identifiers");
    openapiFields.add("ignored");
    openapiFields.add("isIgnored");
    openapiFields.add("isPatchable");
    openapiFields.add("isPatched");
    openapiFields.add("isPinnable");
    openapiFields.add("isUpgradable");
    openapiFields.add("jiraIssueUrl");
    openapiFields.add("language");
    openapiFields.add("originalSeverity");
    openapiFields.add("package");
    openapiFields.add("packageManager");
    openapiFields.add("patches");
    openapiFields.add("priorityScore");
    openapiFields.add("publicationTime");
    openapiFields.add("semver");
    openapiFields.add("severity");
    openapiFields.add("title");
    openapiFields.add("type");
    openapiFields.add("uniqueSeveritiesList");
    openapiFields.add("url");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("exploitMaturity");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("originalSeverity");
    openapiRequiredFields.add("package");
    openapiRequiredFields.add("severity");
    openapiRequiredFields.add("title");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("url");
    openapiRequiredFields.add("version");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetListOfIssues200ResponseResultsInnerIssue
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetListOfIssues200ResponseResultsInnerIssue.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetListOfIssues200ResponseResultsInnerIssue is not found in the empty JSON string", GetListOfIssues200ResponseResultsInnerIssue.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetListOfIssues200ResponseResultsInnerIssue.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetListOfIssues200ResponseResultsInnerIssue` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetListOfIssues200ResponseResultsInnerIssue.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("CVSSv3") != null && !jsonObj.get("CVSSv3").isJsonNull()) && !jsonObj.get("CVSSv3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CVSSv3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CVSSv3").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("credit") != null && !jsonObj.get("credit").isJsonNull() && !jsonObj.get("credit").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `credit` to be an array in the JSON string but got `%s`", jsonObj.get("credit").toString()));
      }
      if ((jsonObj.get("disclosureTime") != null && !jsonObj.get("disclosureTime").isJsonNull()) && !jsonObj.get("disclosureTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `disclosureTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("disclosureTime").toString()));
      }
      if (!jsonObj.get("exploitMaturity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exploitMaturity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exploitMaturity").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `identifiers`
      if (jsonObj.get("identifiers") != null && !jsonObj.get("identifiers").isJsonNull()) {
        GetListOfIssues200ResponseResultsInnerIssueIdentifiers.validateJsonElement(jsonObj.get("identifiers"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("ignored") != null && !jsonObj.get("ignored").isJsonNull() && !jsonObj.get("ignored").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ignored` to be an array in the JSON string but got `%s`", jsonObj.get("ignored").toString()));
      }
      if ((jsonObj.get("jiraIssueUrl") != null && !jsonObj.get("jiraIssueUrl").isJsonNull()) && !jsonObj.get("jiraIssueUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `jiraIssueUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("jiraIssueUrl").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if (!jsonObj.get("originalSeverity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `originalSeverity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("originalSeverity").toString()));
      }
      if (!jsonObj.get("package").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `package` to be a primitive type in the JSON string but got `%s`", jsonObj.get("package").toString()));
      }
      if ((jsonObj.get("packageManager") != null && !jsonObj.get("packageManager").isJsonNull()) && !jsonObj.get("packageManager").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `packageManager` to be a primitive type in the JSON string but got `%s`", jsonObj.get("packageManager").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("patches") != null && !jsonObj.get("patches").isJsonNull() && !jsonObj.get("patches").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `patches` to be an array in the JSON string but got `%s`", jsonObj.get("patches").toString()));
      }
      if ((jsonObj.get("publicationTime") != null && !jsonObj.get("publicationTime").isJsonNull()) && !jsonObj.get("publicationTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicationTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicationTime").toString()));
      }
      // validate the optional field `semver`
      if (jsonObj.get("semver") != null && !jsonObj.get("semver").isJsonNull()) {
        GetListOfIssues200ResponseResultsInnerIssueSemver.validateJsonElement(jsonObj.get("semver"));
      }
      if (!jsonObj.get("severity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `severity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("severity").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("uniqueSeveritiesList") != null && !jsonObj.get("uniqueSeveritiesList").isJsonNull() && !jsonObj.get("uniqueSeveritiesList").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `uniqueSeveritiesList` to be an array in the JSON string but got `%s`", jsonObj.get("uniqueSeveritiesList").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
      if (!jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetListOfIssues200ResponseResultsInnerIssue.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetListOfIssues200ResponseResultsInnerIssue' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetListOfIssues200ResponseResultsInnerIssue> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetListOfIssues200ResponseResultsInnerIssue.class));

       return (TypeAdapter<T>) new TypeAdapter<GetListOfIssues200ResponseResultsInnerIssue>() {
           @Override
           public void write(JsonWriter out, GetListOfIssues200ResponseResultsInnerIssue value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetListOfIssues200ResponseResultsInnerIssue read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetListOfIssues200ResponseResultsInnerIssue given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetListOfIssues200ResponseResultsInnerIssue
   * @throws IOException if the JSON string is invalid with respect to GetListOfIssues200ResponseResultsInnerIssue
   */
  public static GetListOfIssues200ResponseResultsInnerIssue fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetListOfIssues200ResponseResultsInnerIssue.class);
  }

  /**
   * Convert an instance of GetListOfIssues200ResponseResultsInnerIssue to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

