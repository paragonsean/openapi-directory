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
import org.openapitools.client.model.ListAllDependencies200ResponseResultsInnerLicensesInner;
import org.openapitools.client.model.ListAllDependencies200ResponseResultsInnerProjectsInner;

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
 * ListAllDependencies200ResponseResultsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:01.841417-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ListAllDependencies200ResponseResultsInner {
  public static final String SERIALIZED_NAME_COPYRIGHT = "copyright";
  @SerializedName(SERIALIZED_NAME_COPYRIGHT)
  private List<Object> copyright = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEPENDENCIES_WITH_ISSUES = "dependenciesWithIssues";
  @SerializedName(SERIALIZED_NAME_DEPENDENCIES_WITH_ISSUES)
  private List<Object> dependenciesWithIssues = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEPRECATED_VERSIONS = "deprecatedVersions";
  @SerializedName(SERIALIZED_NAME_DEPRECATED_VERSIONS)
  private List<Object> deprecatedVersions = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIRST_PUBLISHED_DATE = "firstPublishedDate";
  @SerializedName(SERIALIZED_NAME_FIRST_PUBLISHED_DATE)
  private String firstPublishedDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_DEPRECATED = "isDeprecated";
  @SerializedName(SERIALIZED_NAME_IS_DEPRECATED)
  private Boolean isDeprecated;

  public static final String SERIALIZED_NAME_ISSUES_CRITICAL = "issuesCritical";
  @SerializedName(SERIALIZED_NAME_ISSUES_CRITICAL)
  private BigDecimal issuesCritical;

  public static final String SERIALIZED_NAME_ISSUES_HIGH = "issuesHigh";
  @SerializedName(SERIALIZED_NAME_ISSUES_HIGH)
  private BigDecimal issuesHigh;

  public static final String SERIALIZED_NAME_ISSUES_LOW = "issuesLow";
  @SerializedName(SERIALIZED_NAME_ISSUES_LOW)
  private BigDecimal issuesLow;

  public static final String SERIALIZED_NAME_ISSUES_MEDIUM = "issuesMedium";
  @SerializedName(SERIALIZED_NAME_ISSUES_MEDIUM)
  private BigDecimal issuesMedium;

  public static final String SERIALIZED_NAME_LATEST_VERSION = "latestVersion";
  @SerializedName(SERIALIZED_NAME_LATEST_VERSION)
  private String latestVersion;

  public static final String SERIALIZED_NAME_LATEST_VERSION_PUBLISHED_DATE = "latestVersionPublishedDate";
  @SerializedName(SERIALIZED_NAME_LATEST_VERSION_PUBLISHED_DATE)
  private String latestVersionPublishedDate;

  public static final String SERIALIZED_NAME_LICENSES = "licenses";
  @SerializedName(SERIALIZED_NAME_LICENSES)
  private List<ListAllDependencies200ResponseResultsInnerLicensesInner> licenses = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROJECTS = "projects";
  @SerializedName(SERIALIZED_NAME_PROJECTS)
  private List<ListAllDependencies200ResponseResultsInnerProjectsInner> projects = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public ListAllDependencies200ResponseResultsInner() {
  }

  public ListAllDependencies200ResponseResultsInner copyright(List<Object> copyright) {
    this.copyright = copyright;
    return this;
  }

  public ListAllDependencies200ResponseResultsInner addCopyrightItem(Object copyrightItem) {
    if (this.copyright == null) {
      this.copyright = new ArrayList<>();
    }
    this.copyright.add(copyrightItem);
    return this;
  }

  /**
   * The copyright notices for the package
   * @return copyright
   */
  @javax.annotation.Nullable
  public List<Object> getCopyright() {
    return copyright;
  }

  public void setCopyright(List<Object> copyright) {
    this.copyright = copyright;
  }


  public ListAllDependencies200ResponseResultsInner dependenciesWithIssues(List<Object> dependenciesWithIssues) {
    this.dependenciesWithIssues = dependenciesWithIssues;
    return this;
  }

  public ListAllDependencies200ResponseResultsInner addDependenciesWithIssuesItem(Object dependenciesWithIssuesItem) {
    if (this.dependenciesWithIssues == null) {
      this.dependenciesWithIssues = new ArrayList<>();
    }
    this.dependenciesWithIssues.add(dependenciesWithIssuesItem);
    return this;
  }

  /**
   * The identifiers of dependencies with issues that are depended upon as a result of this dependency
   * @return dependenciesWithIssues
   */
  @javax.annotation.Nullable
  public List<Object> getDependenciesWithIssues() {
    return dependenciesWithIssues;
  }

  public void setDependenciesWithIssues(List<Object> dependenciesWithIssues) {
    this.dependenciesWithIssues = dependenciesWithIssues;
  }


  public ListAllDependencies200ResponseResultsInner deprecatedVersions(List<Object> deprecatedVersions) {
    this.deprecatedVersions = deprecatedVersions;
    return this;
  }

  public ListAllDependencies200ResponseResultsInner addDeprecatedVersionsItem(Object deprecatedVersionsItem) {
    if (this.deprecatedVersions == null) {
      this.deprecatedVersions = new ArrayList<>();
    }
    this.deprecatedVersions.add(deprecatedVersionsItem);
    return this;
  }

  /**
   * The numbers for those versions that are marked as deprecated
   * @return deprecatedVersions
   */
  @javax.annotation.Nullable
  public List<Object> getDeprecatedVersions() {
    return deprecatedVersions;
  }

  public void setDeprecatedVersions(List<Object> deprecatedVersions) {
    this.deprecatedVersions = deprecatedVersions;
  }


  public ListAllDependencies200ResponseResultsInner firstPublishedDate(String firstPublishedDate) {
    this.firstPublishedDate = firstPublishedDate;
    return this;
  }

  /**
   * The timestamp for when the specified package was first published.
   * @return firstPublishedDate
   */
  @javax.annotation.Nullable
  public String getFirstPublishedDate() {
    return firstPublishedDate;
  }

  public void setFirstPublishedDate(String firstPublishedDate) {
    this.firstPublishedDate = firstPublishedDate;
  }


  public ListAllDependencies200ResponseResultsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The identifier of the package
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public ListAllDependencies200ResponseResultsInner isDeprecated(Boolean isDeprecated) {
    this.isDeprecated = isDeprecated;
    return this;
  }

  /**
   * True if the latest version of the package is marked as deprecated; False otherwise.
   * @return isDeprecated
   */
  @javax.annotation.Nullable
  public Boolean getIsDeprecated() {
    return isDeprecated;
  }

  public void setIsDeprecated(Boolean isDeprecated) {
    this.isDeprecated = isDeprecated;
  }


  public ListAllDependencies200ResponseResultsInner issuesCritical(BigDecimal issuesCritical) {
    this.issuesCritical = issuesCritical;
    return this;
  }

  /**
   * The number of critical severity issues in this dependency
   * @return issuesCritical
   */
  @javax.annotation.Nullable
  public BigDecimal getIssuesCritical() {
    return issuesCritical;
  }

  public void setIssuesCritical(BigDecimal issuesCritical) {
    this.issuesCritical = issuesCritical;
  }


  public ListAllDependencies200ResponseResultsInner issuesHigh(BigDecimal issuesHigh) {
    this.issuesHigh = issuesHigh;
    return this;
  }

  /**
   * The number of high severity issues in this dependency
   * @return issuesHigh
   */
  @javax.annotation.Nullable
  public BigDecimal getIssuesHigh() {
    return issuesHigh;
  }

  public void setIssuesHigh(BigDecimal issuesHigh) {
    this.issuesHigh = issuesHigh;
  }


  public ListAllDependencies200ResponseResultsInner issuesLow(BigDecimal issuesLow) {
    this.issuesLow = issuesLow;
    return this;
  }

  /**
   * The number of low severity issues in this dependency
   * @return issuesLow
   */
  @javax.annotation.Nullable
  public BigDecimal getIssuesLow() {
    return issuesLow;
  }

  public void setIssuesLow(BigDecimal issuesLow) {
    this.issuesLow = issuesLow;
  }


  public ListAllDependencies200ResponseResultsInner issuesMedium(BigDecimal issuesMedium) {
    this.issuesMedium = issuesMedium;
    return this;
  }

  /**
   * The number of medium severity issues in this dependency
   * @return issuesMedium
   */
  @javax.annotation.Nullable
  public BigDecimal getIssuesMedium() {
    return issuesMedium;
  }

  public void setIssuesMedium(BigDecimal issuesMedium) {
    this.issuesMedium = issuesMedium;
  }


  public ListAllDependencies200ResponseResultsInner latestVersion(String latestVersion) {
    this.latestVersion = latestVersion;
    return this;
  }

  /**
   * The latest version available for the specified package
   * @return latestVersion
   */
  @javax.annotation.Nullable
  public String getLatestVersion() {
    return latestVersion;
  }

  public void setLatestVersion(String latestVersion) {
    this.latestVersion = latestVersion;
  }


  public ListAllDependencies200ResponseResultsInner latestVersionPublishedDate(String latestVersionPublishedDate) {
    this.latestVersionPublishedDate = latestVersionPublishedDate;
    return this;
  }

  /**
   * The timestamp for when the latest version of the specified package was published.
   * @return latestVersionPublishedDate
   */
  @javax.annotation.Nullable
  public String getLatestVersionPublishedDate() {
    return latestVersionPublishedDate;
  }

  public void setLatestVersionPublishedDate(String latestVersionPublishedDate) {
    this.latestVersionPublishedDate = latestVersionPublishedDate;
  }


  public ListAllDependencies200ResponseResultsInner licenses(List<ListAllDependencies200ResponseResultsInnerLicensesInner> licenses) {
    this.licenses = licenses;
    return this;
  }

  public ListAllDependencies200ResponseResultsInner addLicensesItem(ListAllDependencies200ResponseResultsInnerLicensesInner licensesItem) {
    if (this.licenses == null) {
      this.licenses = new ArrayList<>();
    }
    this.licenses.add(licensesItem);
    return this;
  }

  /**
   * The licenses of the dependency
   * @return licenses
   */
  @javax.annotation.Nonnull
  public List<ListAllDependencies200ResponseResultsInnerLicensesInner> getLicenses() {
    return licenses;
  }

  public void setLicenses(List<ListAllDependencies200ResponseResultsInnerLicensesInner> licenses) {
    this.licenses = licenses;
  }


  public ListAllDependencies200ResponseResultsInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the package
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ListAllDependencies200ResponseResultsInner projects(List<ListAllDependencies200ResponseResultsInnerProjectsInner> projects) {
    this.projects = projects;
    return this;
  }

  public ListAllDependencies200ResponseResultsInner addProjectsItem(ListAllDependencies200ResponseResultsInnerProjectsInner projectsItem) {
    if (this.projects == null) {
      this.projects = new ArrayList<>();
    }
    this.projects.add(projectsItem);
    return this;
  }

  /**
   * The projects which depend on the dependency
   * @return projects
   */
  @javax.annotation.Nonnull
  public List<ListAllDependencies200ResponseResultsInnerProjectsInner> getProjects() {
    return projects;
  }

  public void setProjects(List<ListAllDependencies200ResponseResultsInnerProjectsInner> projects) {
    this.projects = projects;
  }


  public ListAllDependencies200ResponseResultsInner type(String type) {
    this.type = type;
    return this;
  }

  /**
   * The package type of the dependency
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public ListAllDependencies200ResponseResultsInner version(String version) {
    this.version = version;
    return this;
  }

  /**
   * The version of the package
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
    ListAllDependencies200ResponseResultsInner listAllDependencies200ResponseResultsInner = (ListAllDependencies200ResponseResultsInner) o;
    return Objects.equals(this.copyright, listAllDependencies200ResponseResultsInner.copyright) &&
        Objects.equals(this.dependenciesWithIssues, listAllDependencies200ResponseResultsInner.dependenciesWithIssues) &&
        Objects.equals(this.deprecatedVersions, listAllDependencies200ResponseResultsInner.deprecatedVersions) &&
        Objects.equals(this.firstPublishedDate, listAllDependencies200ResponseResultsInner.firstPublishedDate) &&
        Objects.equals(this.id, listAllDependencies200ResponseResultsInner.id) &&
        Objects.equals(this.isDeprecated, listAllDependencies200ResponseResultsInner.isDeprecated) &&
        Objects.equals(this.issuesCritical, listAllDependencies200ResponseResultsInner.issuesCritical) &&
        Objects.equals(this.issuesHigh, listAllDependencies200ResponseResultsInner.issuesHigh) &&
        Objects.equals(this.issuesLow, listAllDependencies200ResponseResultsInner.issuesLow) &&
        Objects.equals(this.issuesMedium, listAllDependencies200ResponseResultsInner.issuesMedium) &&
        Objects.equals(this.latestVersion, listAllDependencies200ResponseResultsInner.latestVersion) &&
        Objects.equals(this.latestVersionPublishedDate, listAllDependencies200ResponseResultsInner.latestVersionPublishedDate) &&
        Objects.equals(this.licenses, listAllDependencies200ResponseResultsInner.licenses) &&
        Objects.equals(this.name, listAllDependencies200ResponseResultsInner.name) &&
        Objects.equals(this.projects, listAllDependencies200ResponseResultsInner.projects) &&
        Objects.equals(this.type, listAllDependencies200ResponseResultsInner.type) &&
        Objects.equals(this.version, listAllDependencies200ResponseResultsInner.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(copyright, dependenciesWithIssues, deprecatedVersions, firstPublishedDate, id, isDeprecated, issuesCritical, issuesHigh, issuesLow, issuesMedium, latestVersion, latestVersionPublishedDate, licenses, name, projects, type, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListAllDependencies200ResponseResultsInner {\n");
    sb.append("    copyright: ").append(toIndentedString(copyright)).append("\n");
    sb.append("    dependenciesWithIssues: ").append(toIndentedString(dependenciesWithIssues)).append("\n");
    sb.append("    deprecatedVersions: ").append(toIndentedString(deprecatedVersions)).append("\n");
    sb.append("    firstPublishedDate: ").append(toIndentedString(firstPublishedDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isDeprecated: ").append(toIndentedString(isDeprecated)).append("\n");
    sb.append("    issuesCritical: ").append(toIndentedString(issuesCritical)).append("\n");
    sb.append("    issuesHigh: ").append(toIndentedString(issuesHigh)).append("\n");
    sb.append("    issuesLow: ").append(toIndentedString(issuesLow)).append("\n");
    sb.append("    issuesMedium: ").append(toIndentedString(issuesMedium)).append("\n");
    sb.append("    latestVersion: ").append(toIndentedString(latestVersion)).append("\n");
    sb.append("    latestVersionPublishedDate: ").append(toIndentedString(latestVersionPublishedDate)).append("\n");
    sb.append("    licenses: ").append(toIndentedString(licenses)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    projects: ").append(toIndentedString(projects)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("copyright");
    openapiFields.add("dependenciesWithIssues");
    openapiFields.add("deprecatedVersions");
    openapiFields.add("firstPublishedDate");
    openapiFields.add("id");
    openapiFields.add("isDeprecated");
    openapiFields.add("issuesCritical");
    openapiFields.add("issuesHigh");
    openapiFields.add("issuesLow");
    openapiFields.add("issuesMedium");
    openapiFields.add("latestVersion");
    openapiFields.add("latestVersionPublishedDate");
    openapiFields.add("licenses");
    openapiFields.add("name");
    openapiFields.add("projects");
    openapiFields.add("type");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("licenses");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("projects");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("version");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ListAllDependencies200ResponseResultsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ListAllDependencies200ResponseResultsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ListAllDependencies200ResponseResultsInner is not found in the empty JSON string", ListAllDependencies200ResponseResultsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ListAllDependencies200ResponseResultsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ListAllDependencies200ResponseResultsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ListAllDependencies200ResponseResultsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("copyright") != null && !jsonObj.get("copyright").isJsonNull() && !jsonObj.get("copyright").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `copyright` to be an array in the JSON string but got `%s`", jsonObj.get("copyright").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("dependenciesWithIssues") != null && !jsonObj.get("dependenciesWithIssues").isJsonNull() && !jsonObj.get("dependenciesWithIssues").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `dependenciesWithIssues` to be an array in the JSON string but got `%s`", jsonObj.get("dependenciesWithIssues").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("deprecatedVersions") != null && !jsonObj.get("deprecatedVersions").isJsonNull() && !jsonObj.get("deprecatedVersions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `deprecatedVersions` to be an array in the JSON string but got `%s`", jsonObj.get("deprecatedVersions").toString()));
      }
      if ((jsonObj.get("firstPublishedDate") != null && !jsonObj.get("firstPublishedDate").isJsonNull()) && !jsonObj.get("firstPublishedDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstPublishedDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstPublishedDate").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("latestVersion") != null && !jsonObj.get("latestVersion").isJsonNull()) && !jsonObj.get("latestVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `latestVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("latestVersion").toString()));
      }
      if ((jsonObj.get("latestVersionPublishedDate") != null && !jsonObj.get("latestVersionPublishedDate").isJsonNull()) && !jsonObj.get("latestVersionPublishedDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `latestVersionPublishedDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("latestVersionPublishedDate").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("licenses").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `licenses` to be an array in the JSON string but got `%s`", jsonObj.get("licenses").toString()));
      }

      JsonArray jsonArraylicenses = jsonObj.getAsJsonArray("licenses");
      // validate the required field `licenses` (array)
      for (int i = 0; i < jsonArraylicenses.size(); i++) {
        ListAllDependencies200ResponseResultsInnerLicensesInner.validateJsonElement(jsonArraylicenses.get(i));
      };
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("projects").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `projects` to be an array in the JSON string but got `%s`", jsonObj.get("projects").toString()));
      }

      JsonArray jsonArrayprojects = jsonObj.getAsJsonArray("projects");
      // validate the required field `projects` (array)
      for (int i = 0; i < jsonArrayprojects.size(); i++) {
        ListAllDependencies200ResponseResultsInnerProjectsInner.validateJsonElement(jsonArrayprojects.get(i));
      };
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      if (!jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ListAllDependencies200ResponseResultsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ListAllDependencies200ResponseResultsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ListAllDependencies200ResponseResultsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ListAllDependencies200ResponseResultsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ListAllDependencies200ResponseResultsInner>() {
           @Override
           public void write(JsonWriter out, ListAllDependencies200ResponseResultsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ListAllDependencies200ResponseResultsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ListAllDependencies200ResponseResultsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ListAllDependencies200ResponseResultsInner
   * @throws IOException if the JSON string is invalid with respect to ListAllDependencies200ResponseResultsInner
   */
  public static ListAllDependencies200ResponseResultsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ListAllDependencies200ResponseResultsInner.class);
  }

  /**
   * Convert an instance of ListAllDependencies200ResponseResultsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

