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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ImportTargetsRequestAnyOf;
import org.openapitools.client.model.ImportTargetsRequestAnyOf1;
import org.openapitools.client.model.ImportTargetsRequestAnyOf2;
import org.openapitools.client.model.ImportTargetsRequestAnyOf3;
import org.openapitools.client.model.ImportTargetsRequestAnyOf4;
import org.openapitools.client.model.ImportTargetsRequestAnyOf5;
import org.openapitools.client.model.ImportTargetsRequestAnyOf6;
import org.openapitools.client.model.ImportTargetsRequestAnyOf7;
import org.openapitools.client.model.ImportTargetsRequestAnyOf8;
import org.openapitools.client.model.ImportTargetsRequestAnyOf9;
import org.openapitools.client.model.ImportTargetsRequestAnyOf9Target;



import java.io.IOException;
import java.lang.reflect.Type;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.JsonPrimitive;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;
import com.google.gson.JsonParseException;

import org.openapitools.client.JSON;

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:01.841417-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImportTargetsRequest extends AbstractOpenApiSchema {
    private static final Logger log = Logger.getLogger(ImportTargetsRequest.class.getName());

    public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            if (!ImportTargetsRequest.class.isAssignableFrom(type.getRawType())) {
                return null; // this class only serializes 'ImportTargetsRequest' and its subtypes
            }
            final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
            final TypeAdapter<ImportTargetsRequestAnyOf> adapterImportTargetsRequestAnyOf = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf.class));
            final TypeAdapter<ImportTargetsRequestAnyOf1> adapterImportTargetsRequestAnyOf1 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf1.class));
            final TypeAdapter<ImportTargetsRequestAnyOf2> adapterImportTargetsRequestAnyOf2 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf2.class));
            final TypeAdapter<ImportTargetsRequestAnyOf3> adapterImportTargetsRequestAnyOf3 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf3.class));
            final TypeAdapter<ImportTargetsRequestAnyOf4> adapterImportTargetsRequestAnyOf4 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf4.class));
            final TypeAdapter<ImportTargetsRequestAnyOf5> adapterImportTargetsRequestAnyOf5 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf5.class));
            final TypeAdapter<ImportTargetsRequestAnyOf6> adapterImportTargetsRequestAnyOf6 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf6.class));
            final TypeAdapter<ImportTargetsRequestAnyOf7> adapterImportTargetsRequestAnyOf7 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf7.class));
            final TypeAdapter<ImportTargetsRequestAnyOf8> adapterImportTargetsRequestAnyOf8 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf8.class));
            final TypeAdapter<ImportTargetsRequestAnyOf9> adapterImportTargetsRequestAnyOf9 = gson.getDelegateAdapter(this, TypeToken.get(ImportTargetsRequestAnyOf9.class));

            return (TypeAdapter<T>) new TypeAdapter<ImportTargetsRequest>() {
                @Override
                public void write(JsonWriter out, ImportTargetsRequest value) throws IOException {
                    if (value == null || value.getActualInstance() == null) {
                        elementAdapter.write(out, null);
                        return;
                    }

                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf) {
                        JsonElement element = adapterImportTargetsRequestAnyOf.toJsonTree((ImportTargetsRequestAnyOf)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf1`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf1) {
                        JsonElement element = adapterImportTargetsRequestAnyOf1.toJsonTree((ImportTargetsRequestAnyOf1)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf2`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf2) {
                        JsonElement element = adapterImportTargetsRequestAnyOf2.toJsonTree((ImportTargetsRequestAnyOf2)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf3`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf3) {
                        JsonElement element = adapterImportTargetsRequestAnyOf3.toJsonTree((ImportTargetsRequestAnyOf3)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf4`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf4) {
                        JsonElement element = adapterImportTargetsRequestAnyOf4.toJsonTree((ImportTargetsRequestAnyOf4)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf5`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf5) {
                        JsonElement element = adapterImportTargetsRequestAnyOf5.toJsonTree((ImportTargetsRequestAnyOf5)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf6`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf6) {
                        JsonElement element = adapterImportTargetsRequestAnyOf6.toJsonTree((ImportTargetsRequestAnyOf6)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf7`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf7) {
                        JsonElement element = adapterImportTargetsRequestAnyOf7.toJsonTree((ImportTargetsRequestAnyOf7)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf8`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf8) {
                        JsonElement element = adapterImportTargetsRequestAnyOf8.toJsonTree((ImportTargetsRequestAnyOf8)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    // check if the actual instance is of the type `ImportTargetsRequestAnyOf9`
                    if (value.getActualInstance() instanceof ImportTargetsRequestAnyOf9) {
                        JsonElement element = adapterImportTargetsRequestAnyOf9.toJsonTree((ImportTargetsRequestAnyOf9)value.getActualInstance());
                        elementAdapter.write(out, element);
                        return;
                    }
                    throw new IOException("Failed to serialize as the type doesn't match anyOf schemas: ImportTargetsRequestAnyOf, ImportTargetsRequestAnyOf1, ImportTargetsRequestAnyOf2, ImportTargetsRequestAnyOf3, ImportTargetsRequestAnyOf4, ImportTargetsRequestAnyOf5, ImportTargetsRequestAnyOf6, ImportTargetsRequestAnyOf7, ImportTargetsRequestAnyOf8, ImportTargetsRequestAnyOf9");
                }

                @Override
                public ImportTargetsRequest read(JsonReader in) throws IOException {
                    Object deserialized = null;
                    JsonElement jsonElement = elementAdapter.read(in);

                    ArrayList<String> errorMessages = new ArrayList<>();
                    TypeAdapter actualAdapter = elementAdapter;

                    // deserialize ImportTargetsRequestAnyOf
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf1
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf1.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf1;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf1 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf1'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf2
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf2.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf2;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf2 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf2'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf3
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf3.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf3;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf3 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf3'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf4
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf4.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf4;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf4 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf4'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf5
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf5.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf5;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf5 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf5'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf6
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf6.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf6;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf6 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf6'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf7
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf7.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf7;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf7 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf7'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf8
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf8.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf8;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf8 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf8'", e);
                    }
                    // deserialize ImportTargetsRequestAnyOf9
                    try {
                        // validate the JSON object to see if any exception is thrown
                        ImportTargetsRequestAnyOf9.validateJsonElement(jsonElement);
                        actualAdapter = adapterImportTargetsRequestAnyOf9;
                        ImportTargetsRequest ret = new ImportTargetsRequest();
                        ret.setActualInstance(actualAdapter.fromJsonTree(jsonElement));
                        return ret;
                    } catch (Exception e) {
                        // deserialization failed, continue
                        errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf9 failed with `%s`.", e.getMessage()));
                        log.log(Level.FINER, "Input data does not match schema 'ImportTargetsRequestAnyOf9'", e);
                    }

                    throw new IOException(String.format("Failed deserialization for ImportTargetsRequest: no class matches result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
                }
            }.nullSafe();
        }
    }

    // store a list of schema names defined in anyOf
    public static final Map<String, Class<?>> schemas = new HashMap<String, Class<?>>();

    public ImportTargetsRequest() {
        super("anyOf", Boolean.FALSE);
    }

    public ImportTargetsRequest(Object o) {
        super("anyOf", Boolean.FALSE);
        setActualInstance(o);
    }

    static {
        schemas.put("ImportTargetsRequestAnyOf", ImportTargetsRequestAnyOf.class);
        schemas.put("ImportTargetsRequestAnyOf1", ImportTargetsRequestAnyOf1.class);
        schemas.put("ImportTargetsRequestAnyOf2", ImportTargetsRequestAnyOf2.class);
        schemas.put("ImportTargetsRequestAnyOf3", ImportTargetsRequestAnyOf3.class);
        schemas.put("ImportTargetsRequestAnyOf4", ImportTargetsRequestAnyOf4.class);
        schemas.put("ImportTargetsRequestAnyOf5", ImportTargetsRequestAnyOf5.class);
        schemas.put("ImportTargetsRequestAnyOf6", ImportTargetsRequestAnyOf6.class);
        schemas.put("ImportTargetsRequestAnyOf7", ImportTargetsRequestAnyOf7.class);
        schemas.put("ImportTargetsRequestAnyOf8", ImportTargetsRequestAnyOf8.class);
        schemas.put("ImportTargetsRequestAnyOf9", ImportTargetsRequestAnyOf9.class);
    }

    @Override
    public Map<String, Class<?>> getSchemas() {
        return ImportTargetsRequest.schemas;
    }

    /**
     * Set the instance that matches the anyOf child schema, check
     * the instance parameter is valid against the anyOf child schemas:
     * ImportTargetsRequestAnyOf, ImportTargetsRequestAnyOf1, ImportTargetsRequestAnyOf2, ImportTargetsRequestAnyOf3, ImportTargetsRequestAnyOf4, ImportTargetsRequestAnyOf5, ImportTargetsRequestAnyOf6, ImportTargetsRequestAnyOf7, ImportTargetsRequestAnyOf8, ImportTargetsRequestAnyOf9
     *
     * It could be an instance of the 'anyOf' schemas.
     */
    @Override
    public void setActualInstance(Object instance) {
        if (instance instanceof ImportTargetsRequestAnyOf) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf1) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf2) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf3) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf4) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf5) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf6) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf7) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf8) {
            super.setActualInstance(instance);
            return;
        }

        if (instance instanceof ImportTargetsRequestAnyOf9) {
            super.setActualInstance(instance);
            return;
        }

        throw new RuntimeException("Invalid instance type. Must be ImportTargetsRequestAnyOf, ImportTargetsRequestAnyOf1, ImportTargetsRequestAnyOf2, ImportTargetsRequestAnyOf3, ImportTargetsRequestAnyOf4, ImportTargetsRequestAnyOf5, ImportTargetsRequestAnyOf6, ImportTargetsRequestAnyOf7, ImportTargetsRequestAnyOf8, ImportTargetsRequestAnyOf9");
    }

    /**
     * Get the actual instance, which can be the following:
     * ImportTargetsRequestAnyOf, ImportTargetsRequestAnyOf1, ImportTargetsRequestAnyOf2, ImportTargetsRequestAnyOf3, ImportTargetsRequestAnyOf4, ImportTargetsRequestAnyOf5, ImportTargetsRequestAnyOf6, ImportTargetsRequestAnyOf7, ImportTargetsRequestAnyOf8, ImportTargetsRequestAnyOf9
     *
     * @return The actual instance (ImportTargetsRequestAnyOf, ImportTargetsRequestAnyOf1, ImportTargetsRequestAnyOf2, ImportTargetsRequestAnyOf3, ImportTargetsRequestAnyOf4, ImportTargetsRequestAnyOf5, ImportTargetsRequestAnyOf6, ImportTargetsRequestAnyOf7, ImportTargetsRequestAnyOf8, ImportTargetsRequestAnyOf9)
     */
    @SuppressWarnings("unchecked")
    @Override
    public Object getActualInstance() {
        return super.getActualInstance();
    }

    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf`. If the actual instance is not `ImportTargetsRequestAnyOf`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf`
     */
    public ImportTargetsRequestAnyOf getImportTargetsRequestAnyOf() throws ClassCastException {
        return (ImportTargetsRequestAnyOf)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf1`. If the actual instance is not `ImportTargetsRequestAnyOf1`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf1`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf1`
     */
    public ImportTargetsRequestAnyOf1 getImportTargetsRequestAnyOf1() throws ClassCastException {
        return (ImportTargetsRequestAnyOf1)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf2`. If the actual instance is not `ImportTargetsRequestAnyOf2`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf2`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf2`
     */
    public ImportTargetsRequestAnyOf2 getImportTargetsRequestAnyOf2() throws ClassCastException {
        return (ImportTargetsRequestAnyOf2)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf3`. If the actual instance is not `ImportTargetsRequestAnyOf3`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf3`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf3`
     */
    public ImportTargetsRequestAnyOf3 getImportTargetsRequestAnyOf3() throws ClassCastException {
        return (ImportTargetsRequestAnyOf3)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf4`. If the actual instance is not `ImportTargetsRequestAnyOf4`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf4`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf4`
     */
    public ImportTargetsRequestAnyOf4 getImportTargetsRequestAnyOf4() throws ClassCastException {
        return (ImportTargetsRequestAnyOf4)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf5`. If the actual instance is not `ImportTargetsRequestAnyOf5`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf5`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf5`
     */
    public ImportTargetsRequestAnyOf5 getImportTargetsRequestAnyOf5() throws ClassCastException {
        return (ImportTargetsRequestAnyOf5)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf6`. If the actual instance is not `ImportTargetsRequestAnyOf6`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf6`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf6`
     */
    public ImportTargetsRequestAnyOf6 getImportTargetsRequestAnyOf6() throws ClassCastException {
        return (ImportTargetsRequestAnyOf6)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf7`. If the actual instance is not `ImportTargetsRequestAnyOf7`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf7`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf7`
     */
    public ImportTargetsRequestAnyOf7 getImportTargetsRequestAnyOf7() throws ClassCastException {
        return (ImportTargetsRequestAnyOf7)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf8`. If the actual instance is not `ImportTargetsRequestAnyOf8`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf8`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf8`
     */
    public ImportTargetsRequestAnyOf8 getImportTargetsRequestAnyOf8() throws ClassCastException {
        return (ImportTargetsRequestAnyOf8)super.getActualInstance();
    }
    /**
     * Get the actual instance of `ImportTargetsRequestAnyOf9`. If the actual instance is not `ImportTargetsRequestAnyOf9`,
     * the ClassCastException will be thrown.
     *
     * @return The actual instance of `ImportTargetsRequestAnyOf9`
     * @throws ClassCastException if the instance is not `ImportTargetsRequestAnyOf9`
     */
    public ImportTargetsRequestAnyOf9 getImportTargetsRequestAnyOf9() throws ClassCastException {
        return (ImportTargetsRequestAnyOf9)super.getActualInstance();
    }

    /**
     * Validates the JSON Element and throws an exception if issues found
     *
     * @param jsonElement JSON Element
     * @throws IOException if the JSON Element is invalid with respect to ImportTargetsRequest
     */
    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
        // validate anyOf schemas one by one
        ArrayList<String> errorMessages = new ArrayList<>();
        // validate the json string with ImportTargetsRequestAnyOf
        try {
            ImportTargetsRequestAnyOf.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf1
        try {
            ImportTargetsRequestAnyOf1.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf1 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf2
        try {
            ImportTargetsRequestAnyOf2.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf2 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf3
        try {
            ImportTargetsRequestAnyOf3.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf3 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf4
        try {
            ImportTargetsRequestAnyOf4.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf4 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf5
        try {
            ImportTargetsRequestAnyOf5.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf5 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf6
        try {
            ImportTargetsRequestAnyOf6.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf6 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf7
        try {
            ImportTargetsRequestAnyOf7.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf7 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf8
        try {
            ImportTargetsRequestAnyOf8.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf8 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        // validate the json string with ImportTargetsRequestAnyOf9
        try {
            ImportTargetsRequestAnyOf9.validateJsonElement(jsonElement);
            return;
        } catch (Exception e) {
            errorMessages.add(String.format("Deserialization for ImportTargetsRequestAnyOf9 failed with `%s`.", e.getMessage()));
            // continue to the next one
        }
        throw new IOException(String.format("The JSON string is invalid for ImportTargetsRequest with anyOf schemas: ImportTargetsRequestAnyOf, ImportTargetsRequestAnyOf1, ImportTargetsRequestAnyOf2, ImportTargetsRequestAnyOf3, ImportTargetsRequestAnyOf4, ImportTargetsRequestAnyOf5, ImportTargetsRequestAnyOf6, ImportTargetsRequestAnyOf7, ImportTargetsRequestAnyOf8, ImportTargetsRequestAnyOf9. no class match the result, expected at least 1. Detailed failure message for anyOf schemas: %s. JSON: %s", errorMessages, jsonElement.toString()));
    }

    /**
     * Create an instance of ImportTargetsRequest given an JSON string
     *
     * @param jsonString JSON string
     * @return An instance of ImportTargetsRequest
     * @throws IOException if the JSON string is invalid with respect to ImportTargetsRequest
     */
    public static ImportTargetsRequest fromJson(String jsonString) throws IOException {
        return JSON.getGson().fromJson(jsonString, ImportTargetsRequest.class);
    }

    /**
     * Convert an instance of ImportTargetsRequest to an JSON string
     *
     * @return JSON string
     */
    public String toJson() {
        return JSON.getGson().toJson(this);
    }
}

