# snyk_api

SnykApi - JavaScript client for snyk_api
The Snyk API is available to customers on [Business and Enterprise plans](https://snyk.io/plans) and allows you to programatically integrate with Snyk.

## REST API

We are in the process of building a new, improved API (`https://api.snyk.io/rest`) built using the OpenAPI and JSON API standards. We welcome you to try it out as we shape and release endpoints until it, ultimately, becomes a full replacement for our current API.

Looking for our REST API docs? Please head over to [https://apidocs.snyk.io](https://apidocs.snyk.io)

## API vs CLI vs Snyk integration

The API detailed below has the ability to test a package for issues, as they are defined by Snyk. It is important to note that for many package managers, using this API will be less accurate than running the [Snyk CLI](https://snyk.io/docs/using-snyk) as part of your build pipe, or just using it locally on your package. The reason for this is that more than one package version fit the requirements given in manifest files. Running the CLI locally tests the actual deployed code, and has an accurate snapshot of the dependency versions in use, while the API can only infer it, with inferior accuracy. It should be noted that the Snyk CLI has the ability to output machine-readable JSON output (with the `--json` flag to `snyk test`).

A third option, is to allow Snyk access to your development flow via the existing [Snyk integrations](https://snyk.io/docs/). The advantage to this approach is having Snyk monitor every new pull request, and suggest fixes by opening new pull requests. This can be achieved either by integrating Snyk directly to your source code management (SCM) tool, or via a broker to allow greater security and auditability.

If those are not viable options, this API is your best choice.

## API url

The base URL for all API endpoints is https://api.snyk.io/v1/

## Authorization

To use this API, you must get your token from Snyk. It can be seen on https://snyk.io/account/ after you register with Snyk and login.

The token should be supplied in an `Authorization` header with the token, preceded by `token`:

```http
Authorization: token API_KEY
```

Otherwise, a 401 \"Unauthorized\" response will be returned.

```http
HTTP/1.1 401 Unauthorized

        {
            \"code\": 401,
            \"error\": \"Not authorised\",
            \"message\": \"Not authorised\"
        }
```

## Overview and entities

The API is a REST API. It has the following entities:

### Test result

The test result is the object returned from the API giving the results of testing a package for issues. It has the following fields:

| Property        | Type    | Description                                           | Example                                                         |
|----------------:|---------|-------------------------------------------------------|-----------------------------------------------------------------|
| ok              | boolean | Does this package have one or more issues?             | false                                                           |
| issues          | object  | The issues found. See below for details.              | See below                                                       |
| dependencyCount | number  | The number of dependencies the package has.           | 9                                                               |
| org             | object  | The organization this test was carried out for.       | {\"name\": \"anOrg\", \"id\": \"5d7013d9-2a57-4c89-993c-0304d960193c\"} |
| licensesPolicy  | object  | The organization's licenses policy used for this test | See in the examples                                             |
| packageManager  | string  | The package manager for this package                  | \"maven\"                                                         |
|                 |         |                                                       |                                                                 |

### Issue

An issue is either a vulnerability or a license issue, according to the organization's policy. It has the following fields:

| Property       | Type          | Description                                                                                                                | Example                                |
|---------------:|---------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| id             | string        | The issue ID                                                                                                               | \"SNYK-JS-BACKBONE-10054\"               |
| url            | string        | A link to the issue details on snyk.io                                                                                     | \"https://snyk.io/vuln/SNYK-JS-BACKBONE-10054 |
| title          | string        | The issue title                                                                                                            | \"Cross Site Scripting\"                 |
| type           | string        | The issue type: \"license\" or \"vulnerability\".                                                                              | \"license\"                              |
| paths          | array         | The paths to the dependencies which have an issue, and their corresponding upgrade path (if an upgrade is available). [More information about from and upgrade paths](#introduction/overview-and-entities/from-and-upgrade-paths) | [<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;\"from\": [\"a@1.0.0\", \"b@4.8.1\"],<br>&nbsp;&nbsp;&nbsp;&nbsp;\"upgrade\": [false, \"b@4.8.2\"]<br>&nbsp;&nbsp;}<br>] |
| package        | string        | The package identifier according to its package manager                                                                    | \"backbone\", \"org.apache.flex.blazeds:blazeds\"|
| version        | string        | The package version this issue is applicable to.                                                                           | \"0.4.0\"                                |
| severity       | string        | The Snyk defined severity level: \"critical\", \"high\", \"medium\" or \"low\".                                                    | \"high\"                                 |
| language       | string        | The package's programming language                                                                                         | \"js\"                                   |
| packageManager | string        | The package manager                                                                                                        | \"npm\"                                  |
| semver         | array[string] OR map[string]array[string] | One or more [semver](https://semver.org) ranges this issue is applicable to. The format varies according to package manager. | [\"<0.5.0, >=0.4.0\", \"<0.3.8, >=0.3.6\"] OR { \"vulnerable\": [\"[2.0.0, 3.0.0)\"], \"unaffected\": [\"[1, 2)\", \"[3, )\"] } |

### Vulnerability

A vulnerability in a package. In addition to all the fields present in an issue, a vulnerability also has these fields:

Property        | Type    | Description                                                                                                                                                                                                                      | Example                                        |
----------------:|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
 publicationTime | Date    | The vulnerability publication time                                                                                                                                                                                               | \"2016-02-11T07:16:18.857Z\"                     |
 disclosureTime  | Date    | The time this vulnerability was originally disclosed to the package maintainers                                                                                                                                                   | \"2016-02-11T07:16:18.857Z\"                     |
 isUpgradable    | boolean | Is this vulnerability fixable by upgrading a dependency?                                                                                                                                                                         | true                                           |
 description     | string  | The detailed description of the vulnerability, why and how it is exploitable. Provided in markdown format. | \"## Overview\\n[`org.apache.logging.log4j:log4j-core`](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22log4j-core%22)\\nIn Apache Log4j 2.x before 2.8.2, when using the TCP socket server or UDP socket server to receive serialized log events from another application, a specially crafted binary payload can be sent that, when deserialized, can execute arbitrary code.\\n\\n# Details\\nSerialization is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. The reverse process of creating object from sequence of bytes is called deserialization. Serialization is commonly used for communication (sharing objects between multiple hosts) and persistence (store the object state in a file or a database). It is an integral part of popular protocols like _Remote Method Invocation (RMI)_, _Java Management Extension (JMX)_, _Java Messaging System (JMS)_, _Action Message Format (AMF)_, _Java Server Faces (JSF) ViewState_, etc.\\n\\n_Deserialization of untrusted data_ ([CWE-502](https://cwe.mitre.org/data/definitions/502.html)), is when the application deserializes untrusted data without sufficiently verifying that the resulting data will be valid, letting the attacker to control the state or the flow of the execution. \\n\\nJava deserialization issues have been known for years. However, interest in the issue intensified greatly in 2015, when classes that could be abused to achieve remote code execution were found in a [popular library (Apache Commons Collection)](https://snyk.io/vuln/SNYK-JAVA-COMMONSCOLLECTIONS-30078). These classes were used in zero-days affecting IBM WebSphere, Oracle WebLogic and many other products.\\n\\nAn attacker just needs to identify a piece of software that has both a vulnerable class on its path, and performs deserialization on untrusted data. Then all they need to do is send the payload into the deserializer, getting the command executed.\\n\\n> Developers put too much trust in Java Object Serialization. Some even de-serialize objects pre-authentication. When deserializing an Object in Java you typically cast it to an expected type, and therefore Java's strict type system will ensure you only get valid object trees. Unfortunately, by the time the type checking happens, platform code has already created and executed significant logic. So, before the final type is checked a lot of code is executed from the readObject() methods of various objects, all of which is out of the developer's control. By combining the readObject() methods of various classes which are available on the classpath of the vulnerable application an attacker can execute functions (including calling Runtime.exec() to execute local OS commands).\\n- Apache Blog\\n\\n\\n## References\\n- [NVD](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2017-5645)\\n- [jira issue](https://issues.apache.org/jira/browse/LOG4J2-1863)\\n\" |
 isPatchable     | boolean | Is this vulnerability fixable by using a Snyk supplied patch?                                                                                                                                                                    | true                                           |
 isPinnable      | boolean | Is this vulnerability fixable by pinning a transitive dependency                                                                                                                                                                 | true                                           |
 identifiers     | object  | Additional vulnerability identifiers                                                                                                                                                                                             | {\"CWE\": [], \"CVE\": [\"CVE-2016-2402]}           |
 credit          | string  | The reporter of the vulnerability                                                                                                                                                                                                | \"Snyk Security Team\"                           |
 CVSSv3          | string  | Common Vulnerability Scoring System (CVSS) provides a way to capture the principal characteristics of a vulnerability, and produce a numerical score reflecting its severity, as well as a textual representation of that score. | \"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N\" |
 cvssScore       | number  | CVSS Score                                                                                                                                                                                                                       | 5.3                                            |
 patches         | array   | Patches to fix this issue, by snyk                                                                                                                                                                                               | see \"Patch\" below.                             |
 upgradePath     | object  | The path to upgrade this issue, if applicable                                                                                                                                                                                    | see below                                      |
 isPatched       | boolean | Is this vulnerability patched?                                                                                                                                                                                                   | false                                          |
 exploitMaturity | string  | The snyk exploit maturity level

#### Patch

A patch is an object like this one:

```json
{
  \"urls\": [
    \"https://snyk-patches.s3.amazonaws.com/npm/backbone/20110701/backbone_20110701_0_0_0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"
  ],
  \"version\": \"<0.5.0 >=0.3.3\",
  \"modificationTime\": \"2015-11-06T02:09:36.180Z\",
  \"comments\": [
    \"https://github.com/jashkenas/backbone/commit/0cdc525961d3fa98e810ffae6bcc8e3838e36d93.patch\"
  ],
  \"id\": \"patch:npm:backbone:20110701:0\"
}
```

### From and upgrade paths

Both from and upgrade paths are arrays, where each item within the array is a package `name@version`.

Take the following `from` path:

```
[
  \"my-project@1.0.0\",
  \"actionpack@4.2.5\",
  \"rack@1.6.4\"
]
```

Assuming this was returned as a result of a test, then we know:

- The package that was tested was `my-project@1.0.0`

- The dependency with an issue was included in the tested package via the direct dependency `actionpack@4.2.5`

- The dependency with an issue was [rack@1.6.4](https://snyk.io/vuln/rubygems:rack@1.6.4)

Take the following `upgrade` path:

```
[
  false,
  \"actionpack@5.0.0\",
  \"rack@2.0.1\"
]
```

Assuming this was returned as a result of a test, then we know:

- The package that was tested is not upgradable (`false`)

- The direct dependency `actionpack` should be upgraded to at least version `5.0.0` in order to fix the issue

- Upgrading `actionpack` to version `5.0.0` will cause `rack` to be installed at version `2.0.1`

If the `upgrade` path comes back as an empty array (`[]`) then this means that there is no upgrade path available which would fix the issue.

### License issue

A license issue has no additional fields other than the ones in \"Issue\".

### Snyk organization

The organization in Snyk this request is applicable to. The organization determines the access rights, licenses policy and is the unit of billing for private projects.

A Snyk organization has these fields:

Property    | Type   | Description                   | Example                                |
-----------:| ------ | ----------------------------- | -------------------------------------- |
name        | string | The organization display name | \"deelmaker\"                            |
id          | string | The ID of the organization    | \"3ab0f8d3-b17d-4953-ab6d-e1cbfe1df385\" |

## Errors

This is a beta release of this API. Therefore, despite our efforts, errors might occur. In the unlikely event of such an error, it will have the following structure as JSON in the body:

Property    | Type   | Description                   | Example                                |
-----------:| ------ | ----------------------------- | -------------------------------------- |
message     | string | Error message with reference  | Error calling Snyk api (reference: 39db46b1-ad57-47e6-a87d-e34f6968030b) |
errorRef    | V4 uuid | An error ref to contact Snyk with | 39db46b1-ad57-47e6-a87d-e34f6968030b |

The error reference will also be supplied in the `x-error-reference` header in the server reply.

Example response:

```http
HTTP/1.1 500 Internal Server Error
x-error-reference: a45ec9c1-065b-4f7b-baf8-dbd1552ffc9f
Content-Type: application/json; charset=utf-8
Content-Length: 1848
Vary: Accept-Encoding
Date: Sun, 10 Sep 2017 06:48:40 GMT
```

## Rate Limiting

To ensure resilience against increasing request rates, we are starting to introduce rate-limiting.
We are monitoring the rate-limiting system to ensure minimal impact on users while ensuring system stability.
The limit is up to 2000 requests per minute, per user, subject to change. As such, we recommend calls to the API are throttled regardless of the current limit.
All requests above the limit will get a response with status code `429` - `Too many requests` until requests stop for the duration of the rate-limiting interval (currently a minute).

## Consuming Webhooks

Webhooks are delivered with a `Content-Type` of `application/json`, with the event payload as JSON in the request body. We also send the following headers:

- `X-Snyk-Event` - the name of the event

- `X-Snyk-Transport-ID` - a GUID to identify this delivery

- `X-Snyk-Timestamp` - an ISO 8601 timestamp for when the event occurred, for example: `2020-09-25T15:27:53Z`

- `X-Hub-Signature` - the HMAC hex digest of the request body, used to secure your webhooks and ensure the request did indeed come from Snyk

- `User-Agent` - identifies the origin of the request, for example: `Snyk-Webhooks/XXX`

---

After your server is configured to receive payloads, it listens for any payload sent to the endpoint you configured. For security reasons, you should limit requests to those coming from Snyk.

### Validating payloads

All transports sent to your webhooks have a `X-Hub-Signature` header, which contains the hash signature for the transport. The signature is a HMAC hexdigest of the request body, generated using sha256 and your `secret` as the HMAC key.

You could use a function in Node.JS such as the following to validate these signatures on incoming requests from Snyk:

```javascript
import * as crypto from 'crypto';

function verifySignature(request, secret) {
  const hmac = crypto.createHmac('sha256', secret);
  const buffer = JSON.stringify(request.body);
  hmac.update(buffer, 'utf8');

  const signature = `sha256=${hmac.digest('hex')}`;

  return signature === request.headers['x-hub-signature'];
}
```

### Payload versioning

Payloads may evolve over time, and so are versioned. Payload versions are supplied as a suffix to the `X-Snyk-Event` header. For example, `project_snapshot/v0` indicates that the payload is `v0` of the `project_snapshot` event.

Version numbers only increment when a breaking change is made; for example, removing a field that used to exist, or changing the name of a field. Version numbers do not increment when making an additive change, such as adding a new field that never existed before.

**Note:** During the BETA phase, the structure of webhook payloads may change at any time, so we  recommend you check the payload version.

### Event types

While consuming a webhook event, `X-Snyk-Event` header must be checked, as an end-point may receive multiple event types.

#### ping

The ping event happens after a new webhook is created, and can also be manually triggered using the ping webhook API. This is useful to test that your webhook receives data from Snyk correctly.

The `ping` event makes the following request:

```jsx
POST /webhook-handler/snyk123 HTTP/1.1
Host: my.app.com
X-Snyk-Event: ping/v0
X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a
X-Snyk-Timestamp: 2020-09-25T15:27:53Z
X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6
User-Agent: Snyk-Webhooks/044aadd
Content-Type: application/json
{
  \"webhookId\": \"d3cf26b3-2d77-497b-bce2-23b33cc15362\"
}
```

#### project_snapshot

This event is triggered every time an existing project is tested and a new snapshot is created. It is triggered on every test of a project, whether or not there are new issues. This event is not triggered when a new project is created or imported. Currently supported targets/scan types are Open Source and container.

```jsx
POST /webhook-handler/snyk123 HTTP/1.1
Host: my.app.com
X-Snyk-Event: project_snapshot/v0
X-Snyk-Transport-ID: 998fe884-18a0-45db-8ae0-e379eea3bc0a
X-Snyk-Timestamp: 2020-09-25T15:27:53Z
X-Hub-Signature: sha256=7d38cdd689735b008b3c702edd92eea23791c5f6
User-Agent: Snyk-Webhooks/044aadd
Content-Type: application/json
{
  \"project\": { ... }, // project object matching API responses
  \"org\": { ... }, // organization object matching API responses
  \"group\": { ... }, // group object matching API responses
  \"newIssues\": [], // array of issues object matching API responses
  \"removedIssues\": [], // array of issues object matching API responses
}
```

####  Detailed example of a payload

##### project

see: [https://snyk.docs.apiary.io/#reference/projects](https://snyk.docs.apiary.io/#reference/projects)

```tsx
\"project\": {
  \"name\": \"snyk/goof\",
  \"id\": \"af137b96-6966-46c1-826b-2e79ac49bbd9\",
  \"created\": \"2018-10-29T09:50:54.014Z\",
  \"origin\": \"github\",
  \"type\": \"maven\",
  \"readOnly\": false,
  \"testFrequency\": \"daily\",
  \"totalDependencies\": 42,
  \"issueCountsBySeverity\": {
    \"low\": 13,
    \"medium\": 8,
    \"high\": 4,
    \"critical\": 5
  },
  \"imageId\": \"sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019\",
  \"imageTag\": \"latest\",
  \"imageBaseImage\": \"alpine:3\",
  \"imagePlatform\": \"linux/arm64\",
  \"imageCluster\": \"Production\",
  \"hostname\": null,
  \"remoteRepoUrl\": \"https://github.com/snyk/goof.git\",
  \"lastTestedDate\": \"2019-02-05T08:54:07.704Z\",
  \"browseUrl\": \"https://app.snyk.io/org/4a18d42f-0706-4ad0-b127-24078731fbed/project/af137b96-6966-46c1-826b-2e79ac49bbd9\",
  \"importingUser\": {
    \"id\": \"e713cf94-bb02-4ea0-89d9-613cce0caed2\",
    \"name\": \"example-user@snyk.io\",
    \"username\": \"exampleUser\",
    \"email\": \"example-user@snyk.io\"
  },
  \"isMonitored\": false,
  \"branch\": null,
  \"targetReference\": null,
  \"tags\": [
    {
      \"key\": \"example-tag-key\",
      \"value\": \"example-tag-value\"
    }
  ],
  \"attributes\": {
    \"criticality\": [
      \"high\"
    ],
    \"environment\": [
      \"backend\"
    ],
    \"lifecycle\": [
      \"development\"
    ]
  },
  \"remediation\": {
    \"upgrade\": {},
    \"patch\": {},
    \"pin\": {}
  }
}
```

##### org

see: [https://snyk.docs.apiary.io/#reference/organizations](https://snyk.docs.apiary.io/#reference/organizations)

```tsx
\"org\": {
  \"name\": \"My Org\",
  \"id\": \"a04d9cbd-ae6e-44af-b573-0556b0ad4bd2\",
  \"slug\": \"my-org\",
  \"url\": \"https://api.snyk.io/org/my-org\",
  \"created\": \"2020-11-18T10:39:00.983Z\"
}
```

##### group

see: [https://snyk.docs.apiary.io/#reference/groups](https://snyk.docs.apiary.io/#reference/groups)

```tsx
\"group\": {
  \"name\": \"ACME Inc.\",
   \"id\": \"a060a49f-636e-480f-9e14-38e773b2a97f\"
}
```

##### issue

see: https://snyk.docs.apiary.io/#reference/users/user-organization-notification-settings/list-all-aggregated-issues

```tsx
{
  \"id\": \"npm:ms:20170412\",
  \"issueType\": \"vuln\",
  \"pkgName\": \"ms\",
  \"pkgVersions\": [
    \"1.0.0\"
  ],
  \"issueData\": {
    \"id\": \"npm:ms:20170412\",
    \"title\": \"Regular Expression Denial of Service (ReDoS)\",
    \"severity\": \"low\",
    \"url\": \"https://snyk.io/vuln/npm:ms:20170412\",
    \"description\": \"Lorem ipsum\",
    \"identifiers\": {
      \"CVE\": [],
      \"CWE\": [
        \"CWE-400\"
      ],
      \"ALTERNATIVE\": [
        \"SNYK-JS-MS-10509\"
      ]
    },
    \"credit\": [
      \"Snyk Security Research Team\"
    ],
    \"exploitMaturity\": \"no-known-exploit\",
    \"semver\": {
      \"vulnerable\": [
        \">=0.7.1 <2.0.0\"
      ]
    },
    \"publicationTime\": \"2017-05-15T06:02:45Z\",
    \"disclosureTime\": \"2017-04-11T21:00:00Z\",
    \"CVSSv3\": \"CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L\",
    \"cvssScore\": 3.7,
    \"language\": \"js\",
    \"patches\": [
      {
        \"id\": \"patch:npm:ms:20170412:2\",
        \"urls\": [
          \"https://snyk-patches.s3.amazonaws.com/npm/ms/20170412/ms_071.patch\"
        ],
        \"version\": \"=0.7.1\",
        \"comments\": [],
        \"modificationTime\": \"2019-12-03T11:40:45.866206Z\"
      }
    ],
    \"nearestFixedInVersion\": \"2.0.0\"
  },
  \"isPatched\": false,
  \"isIgnored\": false,
  \"fixInfo\": {
    \"isUpgradable\": false,
    \"isPinnable\": false,
    \"isPatchable\": true,
    \"nearestFixedInVersion\": \"2.0.0\"
  },
  \"priority\": {
    \"score\": 399,
    \"factors\": [
      {
        \"name\": \"isFixable\",
        \"description\": \"Has a fix available\"
      },
      {
        \"name\": \"cvssScore\",
        \"description\": \"CVSS 3.7\"
      }
    ]
  }
}
```
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install snyk_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your snyk_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var SnykApi = require('snyk_api');


var api = new SnykApi.AuditLogsApi()
var groupId = "4a18d42f-0706-4ad0-b127-24078731fbea"; // {String} The group ID. The `API_KEY` must have access to this group.
var opts = {
  'from': "2019-07-01", // {String} The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
  'to': "2019-07-07", // {String} The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
  'page': 1, // {Number} The page of results to request. Audit logs are returned in page sizes of 100
  'sortOrder': "ASC", // {String} The sort order of the returned audit logs by date. Values: `ASC`, `DESC`. Default: `DESC`.
  'getGroupLevelAuditLogsRequest': new SnykApi.GetGroupLevelAuditLogsRequest() // {GetGroupLevelAuditLogsRequest} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.getGroupLevelAuditLogs(groupId, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.snyk.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SnykApi.AuditLogsApi* | [**getGroupLevelAuditLogs**](docs/AuditLogsApi.md#getGroupLevelAuditLogs) | **POST** /group/{groupId}/audit | Get group level audit logs
*SnykApi.AuditLogsApi* | [**getOrganizationLevelAuditLogs**](docs/AuditLogsApi.md#getOrganizationLevelAuditLogs) | **POST** /org/{orgId}/audit | Get organization level audit logs
*SnykApi.DependenciesApi* | [**listAllDependencies**](docs/DependenciesApi.md#listAllDependencies) | **POST** /org/{orgId}/dependencies | List all dependencies
*SnykApi.EntitlementsApi* | [**getAnOrganizationsEntitlementValue**](docs/EntitlementsApi.md#getAnOrganizationsEntitlementValue) | **GET** /org/{orgId}/entitlement/{entitlementKey} | Get an organization&#39;s entitlement value
*SnykApi.EntitlementsApi* | [**listAllEntitlements**](docs/EntitlementsApi.md#listAllEntitlements) | **GET** /org/{orgId}/entitlements | List all entitlements
*SnykApi.GroupsApi* | [**addAMemberToAnOrganizationWithinAGroup**](docs/GroupsApi.md#addAMemberToAnOrganizationWithinAGroup) | **POST** /group/{groupId}/org/{orgId}/members | Add a member to an organization within a group
*SnykApi.GroupsApi* | [**deleteTagFromGroup**](docs/GroupsApi.md#deleteTagFromGroup) | **POST** /group/{groupId}/tags/delete | Delete tag from group
*SnykApi.GroupsApi* | [**listAllMembersInAGroup**](docs/GroupsApi.md#listAllMembersInAGroup) | **GET** /group/{groupId}/members | List all members in a group
*SnykApi.GroupsApi* | [**listAllOrganizationsInAGroup**](docs/GroupsApi.md#listAllOrganizationsInAGroup) | **GET** /group/{groupId}/orgs | List all organizations in a group
*SnykApi.GroupsApi* | [**listAllRolesInAGroup**](docs/GroupsApi.md#listAllRolesInAGroup) | **GET** /group/{groupId}/roles | List all roles in a group
*SnykApi.GroupsApi* | [**listAllTagsInAGroup**](docs/GroupsApi.md#listAllTagsInAGroup) | **GET** /group/{groupId}/tags | List all tags in a group
*SnykApi.GroupsApi* | [**updateGroupSettings**](docs/GroupsApi.md#updateGroupSettings) | **PUT** /group/{groupId}/settings | Update group settings
*SnykApi.GroupsApi* | [**viewGroupSettings**](docs/GroupsApi.md#viewGroupSettings) | **GET** /group/{groupId}/settings | View group settings
*SnykApi.ImportProjectsApi* | [**getImportJobDetails**](docs/ImportProjectsApi.md#getImportJobDetails) | **GET** /org/{orgId}/integrations/{integrationId}/import/{jobId} | Get import job details
*SnykApi.ImportProjectsApi* | [**importTargets**](docs/ImportProjectsApi.md#importTargets) | **POST** /org/{orgId}/integrations/{integrationId}/import | Import targets
*SnykApi.IntegrationsApi* | [**addNewIntegration**](docs/IntegrationsApi.md#addNewIntegration) | **POST** /org/{orgId}/integrations | Add new integration
*SnykApi.IntegrationsApi* | [**cloneAnIntegrationWithSettingsAndCredentials**](docs/IntegrationsApi.md#cloneAnIntegrationWithSettingsAndCredentials) | **POST** /org/{orgId}/integrations/{integrationId}/clone | Clone an integration (with settings and credentials)
*SnykApi.IntegrationsApi* | [**deleteCredentials**](docs/IntegrationsApi.md#deleteCredentials) | **DELETE** /org/{orgId}/integrations/{integrationId}/authentication | Delete credentials
*SnykApi.IntegrationsApi* | [**getExistingIntegrationByType**](docs/IntegrationsApi.md#getExistingIntegrationByType) | **GET** /org/{orgId}/integrations/{type} | Get existing integration by type
*SnykApi.IntegrationsApi* | [**list**](docs/IntegrationsApi.md#list) | **GET** /org/{orgId}/integrations | List
*SnykApi.IntegrationsApi* | [**provisionNewBrokerToken**](docs/IntegrationsApi.md#provisionNewBrokerToken) | **POST** /org/{orgId}/integrations/{integrationId}/authentication/provision-token | Provision new broker token
*SnykApi.IntegrationsApi* | [**retrieve**](docs/IntegrationsApi.md#retrieve) | **GET** /org/{orgId}/integrations/{integrationId}/settings | Retrieve
*SnykApi.IntegrationsApi* | [**switchBetweenBrokerTokens**](docs/IntegrationsApi.md#switchBetweenBrokerTokens) | **POST** /org/{orgId}/integrations/{integrationId}/authentication/switch-token | Switch between broker tokens
*SnykApi.IntegrationsApi* | [**update**](docs/IntegrationsApi.md#update) | **PUT** /org/{orgId}/integrations/{integrationId}/settings | Update
*SnykApi.IntegrationsApi* | [**updateExistingIntegration**](docs/IntegrationsApi.md#updateExistingIntegration) | **PUT** /org/{orgId}/integrations/{integrationId} | Update existing integration
*SnykApi.LicensesApi* | [**listAllLicenses**](docs/LicensesApi.md#listAllLicenses) | **POST** /org/{orgId}/licenses | List all licenses
*SnykApi.MonitorApi* | [**monitorDepGraph**](docs/MonitorApi.md#monitorDepGraph) | **POST** /monitor/dep-graph | Monitor Dep Graph
*SnykApi.OrganizationsApi* | [**createANewOrganization**](docs/OrganizationsApi.md#createANewOrganization) | **POST** /org | Create a new organization
*SnykApi.OrganizationsApi* | [**deletePendingUserProvision**](docs/OrganizationsApi.md#deletePendingUserProvision) | **DELETE** /org/{orgId}/provision | Delete pending user provision
*SnykApi.OrganizationsApi* | [**inviteUsers**](docs/OrganizationsApi.md#inviteUsers) | **POST** /org/{orgId}/invite | Invite users
*SnykApi.OrganizationsApi* | [**listAllTheOrganizationsAUserBelongsTo**](docs/OrganizationsApi.md#listAllTheOrganizationsAUserBelongsTo) | **GET** /orgs | List all the organizations a user belongs to
*SnykApi.OrganizationsApi* | [**listMembers**](docs/OrganizationsApi.md#listMembers) | **GET** /org/{orgId}/members | List Members
*SnykApi.OrganizationsApi* | [**listPendingUserProvisions**](docs/OrganizationsApi.md#listPendingUserProvisions) | **GET** /org/{orgId}/provision | List pending user provisions
*SnykApi.OrganizationsApi* | [**orgOrgIdNotificationSettingsGet**](docs/OrganizationsApi.md#orgOrgIdNotificationSettingsGet) | **GET** /org/{orgId}/notification-settings | Get organization notification settings
*SnykApi.OrganizationsApi* | [**provisionAUserToTheOrganization**](docs/OrganizationsApi.md#provisionAUserToTheOrganization) | **POST** /org/{orgId}/provision | Provision a user to the organization
*SnykApi.OrganizationsApi* | [**removeAMemberFromTheOrganization**](docs/OrganizationsApi.md#removeAMemberFromTheOrganization) | **DELETE** /org/{orgId}/members/{userId} | Remove a member from the organization
*SnykApi.OrganizationsApi* | [**removeOrganization**](docs/OrganizationsApi.md#removeOrganization) | **DELETE** /org/{orgId} | Remove organization
*SnykApi.OrganizationsApi* | [**setNotificationSettings**](docs/OrganizationsApi.md#setNotificationSettings) | **PUT** /org/{orgId}/notification-settings | Set notification settings
*SnykApi.OrganizationsApi* | [**updateAMemberInTheOrganization**](docs/OrganizationsApi.md#updateAMemberInTheOrganization) | **PUT** /org/{orgId}/members/{userId} | Update a member in the organization
*SnykApi.OrganizationsApi* | [**updateAMembersRoleInTheOrganization**](docs/OrganizationsApi.md#updateAMembersRoleInTheOrganization) | **PUT** /org/{orgId}/members/update/{userId} | Update a member&#39;s role in the organization
*SnykApi.OrganizationsApi* | [**updateOrganizationSettings**](docs/OrganizationsApi.md#updateOrganizationSettings) | **PUT** /org/{orgId}/settings | Update organization settings
*SnykApi.OrganizationsApi* | [**viewOrganizationSettings**](docs/OrganizationsApi.md#viewOrganizationSettings) | **GET** /org/{orgId}/settings | View organization settings
*SnykApi.ProjectsApi* | [**activate**](docs/ProjectsApi.md#activate) | **POST** /org/{orgId}/project/{projectId}/activate | Activate
*SnykApi.ProjectsApi* | [**addATagToAProject**](docs/ProjectsApi.md#addATagToAProject) | **POST** /org/{orgId}/project/{projectId}/tags | Add a tag to a project
*SnykApi.ProjectsApi* | [**addIgnore**](docs/ProjectsApi.md#addIgnore) | **POST** /org/{orgId}/project/{projectId}/ignore/{issueId} | Add ignore
*SnykApi.ProjectsApi* | [**applyingAttributes**](docs/ProjectsApi.md#applyingAttributes) | **POST** /org/{orgId}/project/{projectId}/attributes | Applying attributes
*SnykApi.ProjectsApi* | [**createJiraIssue**](docs/ProjectsApi.md#createJiraIssue) | **POST** /org/{orgId}/project/{projectId}/issue/{issueId}/jira-issue | Create jira issue
*SnykApi.ProjectsApi* | [**deactivate**](docs/ProjectsApi.md#deactivate) | **POST** /org/{orgId}/project/{projectId}/deactivate | Deactivate
*SnykApi.ProjectsApi* | [**deleteAProject**](docs/ProjectsApi.md#deleteAProject) | **DELETE** /org/{orgId}/project/{projectId} | Delete a project
*SnykApi.ProjectsApi* | [**deleteIgnores**](docs/ProjectsApi.md#deleteIgnores) | **DELETE** /org/{orgId}/project/{projectId}/ignore/{issueId} | Delete ignores
*SnykApi.ProjectsApi* | [**deleteProjectSettings**](docs/ProjectsApi.md#deleteProjectSettings) | **DELETE** /org/{orgId}/project/{projectId}/settings | Delete project settings
*SnykApi.ProjectsApi* | [**getProjectDependencyGraph**](docs/ProjectsApi.md#getProjectDependencyGraph) | **GET** /org/{orgId}/project/{projectId}/dep-graph | Get Project dependency graph
*SnykApi.ProjectsApi* | [**listAllAggregatedIssues**](docs/ProjectsApi.md#listAllAggregatedIssues) | **POST** /org/{orgId}/project/{projectId}/aggregated-issues | List all Aggregated issues
*SnykApi.ProjectsApi* | [**listAllIgnores**](docs/ProjectsApi.md#listAllIgnores) | **GET** /org/{orgId}/project/{projectId}/ignores | List all ignores
*SnykApi.ProjectsApi* | [**listAllJiraIssues**](docs/ProjectsApi.md#listAllJiraIssues) | **GET** /org/{orgId}/project/{projectId}/jira-issues | List all jira issues
*SnykApi.ProjectsApi* | [**listAllProjectIssuePaths**](docs/ProjectsApi.md#listAllProjectIssuePaths) | **GET** /org/{orgId}/project/{projectId}/issue/{issueId}/paths | List all project issue paths
*SnykApi.ProjectsApi* | [**listAllProjectSnapshotAggregatedIssues**](docs/ProjectsApi.md#listAllProjectSnapshotAggregatedIssues) | **POST** /org/{orgId}/project/{projectId}/history/{snapshotId}/aggregated-issues | List all project snapshot aggregated issues
*SnykApi.ProjectsApi* | [**listAllProjectSnapshotIssuePaths**](docs/ProjectsApi.md#listAllProjectSnapshotIssuePaths) | **GET** /org/{orgId}/project/{projectId}/history/{snapshotId}/issue/{issueId}/paths | List all project snapshot issue paths
*SnykApi.ProjectsApi* | [**listAllProjectSnapshots**](docs/ProjectsApi.md#listAllProjectSnapshots) | **POST** /org/{orgId}/project/{projectId}/history | List all project snapshots
*SnykApi.ProjectsApi* | [**listAllProjects**](docs/ProjectsApi.md#listAllProjects) | **POST** /org/{orgId}/projects | List all projects
*SnykApi.ProjectsApi* | [**listProjectSettings**](docs/ProjectsApi.md#listProjectSettings) | **GET** /org/{orgId}/project/{projectId}/settings | List project settings
*SnykApi.ProjectsApi* | [**moveProjectToADifferentOrganization**](docs/ProjectsApi.md#moveProjectToADifferentOrganization) | **PUT** /org/{orgId}/project/{projectId}/move | Move project to a different organization
*SnykApi.ProjectsApi* | [**removeATagFromAProject**](docs/ProjectsApi.md#removeATagFromAProject) | **POST** /org/{orgId}/project/{projectId}/tags/remove | Remove a tag from a project
*SnykApi.ProjectsApi* | [**replaceIgnores**](docs/ProjectsApi.md#replaceIgnores) | **PUT** /org/{orgId}/project/{projectId}/ignore/{issueId} | Replace ignores
*SnykApi.ProjectsApi* | [**retrieveASingleProject**](docs/ProjectsApi.md#retrieveASingleProject) | **GET** /org/{orgId}/project/{projectId} | Retrieve a single project
*SnykApi.ProjectsApi* | [**retrieveIgnore**](docs/ProjectsApi.md#retrieveIgnore) | **GET** /org/{orgId}/project/{projectId}/ignore/{issueId} | Retrieve ignore
*SnykApi.ProjectsApi* | [**updateAProject**](docs/ProjectsApi.md#updateAProject) | **PUT** /org/{orgId}/project/{projectId} | Update a project
*SnykApi.ProjectsApi* | [**updateProjectSettings**](docs/ProjectsApi.md#updateProjectSettings) | **PUT** /org/{orgId}/project/{projectId}/settings | Update project settings
*SnykApi.ReportingAPIApi* | [**getIssueCounts**](docs/ReportingAPIApi.md#getIssueCounts) | **POST** /reporting/counts/issues | Get issue counts
*SnykApi.ReportingAPIApi* | [**getLatestIssueCounts**](docs/ReportingAPIApi.md#getLatestIssueCounts) | **POST** /reporting/counts/issues/latest | Get latest issue counts
*SnykApi.ReportingAPIApi* | [**getLatestProjectCounts**](docs/ReportingAPIApi.md#getLatestProjectCounts) | **POST** /reporting/counts/projects/latest | Get latest project counts
*SnykApi.ReportingAPIApi* | [**getListOfIssues**](docs/ReportingAPIApi.md#getListOfIssues) | **POST** /reporting/issues/ | Get list of issues
*SnykApi.ReportingAPIApi* | [**getListOfLatestIssues**](docs/ReportingAPIApi.md#getListOfLatestIssues) | **POST** /reporting/issues/latest | Get list of latest issues
*SnykApi.ReportingAPIApi* | [**getProjectCounts**](docs/ReportingAPIApi.md#getProjectCounts) | **POST** /reporting/counts/projects | Get project counts
*SnykApi.ReportingAPIApi* | [**getTestCounts**](docs/ReportingAPIApi.md#getTestCounts) | **POST** /reporting/counts/tests | Get test counts
*SnykApi.TestApi* | [**testComposerJsonComposerLockFile**](docs/TestApi.md#testComposerJsonComposerLockFile) | **POST** /test/composer | Test composer.json &amp; composer.lock file
*SnykApi.TestApi* | [**testDepGraph**](docs/TestApi.md#testDepGraph) | **POST** /test/dep-graph | Test Dep Graph
*SnykApi.TestApi* | [**testForIssuesInAPublicGemByNameAndVersion**](docs/TestApi.md#testForIssuesInAPublicGemByNameAndVersion) | **GET** /test/rubygems/{gemName}/{version} | Test for issues in a public gem by name and version
*SnykApi.TestApi* | [**testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion**](docs/TestApi.md#testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion) | **GET** /test/maven/{groupId}/{artifactId}/{version} | Test for issues in a public package by group id, artifact id and version
*SnykApi.TestApi* | [**testForIssuesInAPublicPackageByGroupNameAndVersion**](docs/TestApi.md#testForIssuesInAPublicPackageByGroupNameAndVersion) | **GET** /test/gradle/{group}/{name}/{version} | Test for issues in a public package by group, name and version
*SnykApi.TestApi* | [**testForIssuesInAPublicPackageByNameAndVersion**](docs/TestApi.md#testForIssuesInAPublicPackageByNameAndVersion) | **GET** /test/npm/{packageName}/{version} | Test for issues in a public package by name and version
*SnykApi.TestApi* | [**testGemfileLockFile**](docs/TestApi.md#testGemfileLockFile) | **POST** /test/rubygems | Test gemfile.lock file
*SnykApi.TestApi* | [**testGopkgTomlGopkgLockFile**](docs/TestApi.md#testGopkgTomlGopkgLockFile) | **POST** /test/golangdep | Test Gopkg.toml &amp; Gopkg.lock File
*SnykApi.TestApi* | [**testGradleFile**](docs/TestApi.md#testGradleFile) | **POST** /test/gradle | Test gradle file
*SnykApi.TestApi* | [**testMavenFile**](docs/TestApi.md#testMavenFile) | **POST** /test/maven | Test maven file
*SnykApi.TestApi* | [**testPackageJsonPackageLockJsonFile**](docs/TestApi.md#testPackageJsonPackageLockJsonFile) | **POST** /test/npm | Test package.json &amp; package-lock.json File
*SnykApi.TestApi* | [**testPackageJsonYarnLockFile**](docs/TestApi.md#testPackageJsonYarnLockFile) | **POST** /test/yarn | Test package.json &amp; yarn.lock File
*SnykApi.TestApi* | [**testPipPackageNameVersionGet**](docs/TestApi.md#testPipPackageNameVersionGet) | **GET** /test/pip/{packageName}/{version} | Test for issues in a public package by name and version
*SnykApi.TestApi* | [**testRequirementsTxtFile**](docs/TestApi.md#testRequirementsTxtFile) | **POST** /test/pip | Test requirements.txt file
*SnykApi.TestApi* | [**testSbtFile**](docs/TestApi.md#testSbtFile) | **POST** /test/sbt | Test sbt file
*SnykApi.TestApi* | [**testSbtGroupIdArtifactIdVersionGet**](docs/TestApi.md#testSbtGroupIdArtifactIdVersionGet) | **GET** /test/sbt/{groupId}/{artifactId}/{version} | Test for issues in a public package by group id, artifact id and version
*SnykApi.TestApi* | [**testVendorJsonFile**](docs/TestApi.md#testVendorJsonFile) | **POST** /test/govendor | Test vendor.json File
*SnykApi.UsersApi* | [**getMyDetails**](docs/UsersApi.md#getMyDetails) | **GET** /user/me | Get My Details
*SnykApi.UsersApi* | [**getOrganizationNotificationSettings**](docs/UsersApi.md#getOrganizationNotificationSettings) | **GET** /user/me/notification-settings/org/{orgId} | Get organization notification settings
*SnykApi.UsersApi* | [**getProjectNotificationSettings**](docs/UsersApi.md#getProjectNotificationSettings) | **GET** /user/me/notification-settings/org/{orgId}/project/{projectId} | Get project notification settings
*SnykApi.UsersApi* | [**getUserDetails**](docs/UsersApi.md#getUserDetails) | **GET** /user/{userId} | Get User Details
*SnykApi.UsersApi* | [**modifyOrganizationNotificationSettings**](docs/UsersApi.md#modifyOrganizationNotificationSettings) | **PUT** /user/me/notification-settings/org/{orgId} | Modify organization notification settings
*SnykApi.UsersApi* | [**modifyProjectNotificationSettings**](docs/UsersApi.md#modifyProjectNotificationSettings) | **PUT** /user/me/notification-settings/org/{orgId}/project/{projectId} | Modify project notification settings
*SnykApi.WebhooksApi* | [**createAWebhook**](docs/WebhooksApi.md#createAWebhook) | **POST** /org/{orgId}/webhooks | Create a webhook
*SnykApi.WebhooksApi* | [**deleteAWebhook**](docs/WebhooksApi.md#deleteAWebhook) | **DELETE** /org/{orgId}/webhooks/{webhookId} | Delete a webhook
*SnykApi.WebhooksApi* | [**listWebhooks**](docs/WebhooksApi.md#listWebhooks) | **GET** /org/{orgId}/webhooks | List webhooks
*SnykApi.WebhooksApi* | [**pingAWebhook**](docs/WebhooksApi.md#pingAWebhook) | **POST** /org/{orgId}/webhooks/{webhookId}/ping | Ping a webhook
*SnykApi.WebhooksApi* | [**retrieveAWebhook**](docs/WebhooksApi.md#retrieveAWebhook) | **GET** /org/{orgId}/webhooks/{webhookId} | Retrieve a webhook


## Documentation for Models

 - [SnykApi.AddAMemberToAnOrganizationWithinAGroupRequest](docs/AddAMemberToAnOrganizationWithinAGroupRequest.md)
 - [SnykApi.AddATagToAProject200Response](docs/AddATagToAProject200Response.md)
 - [SnykApi.AddATagToAProjectRequest](docs/AddATagToAProjectRequest.md)
 - [SnykApi.AddIgnoreRequest](docs/AddIgnoreRequest.md)
 - [SnykApi.AddMemberBody](docs/AddMemberBody.md)
 - [SnykApi.AddNewIntegrationRequest](docs/AddNewIntegrationRequest.md)
 - [SnykApi.AddNewIntegrationRequestAnyOf](docs/AddNewIntegrationRequestAnyOf.md)
 - [SnykApi.AddNewIntegrationRequestAnyOf1](docs/AddNewIntegrationRequestAnyOf1.md)
 - [SnykApi.AddNewIntegrationRequestAnyOf1Broker](docs/AddNewIntegrationRequestAnyOf1Broker.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentials](docs/AddNewIntegrationRequestAnyOfCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf1](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf1.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf10](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf10.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf10GitHubCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf11](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf11.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf11GitHubEnterpriseCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf12](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf12.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf12GitLabCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf13](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf13.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf13GitLabCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf14](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf14.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf14GoogleArtifactCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf15](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf15.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf15HarborCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf16](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf16.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf16NexusCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf17](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf17.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf17QuayCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf1ArtifactoryCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf2](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf2.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf2AzureReposCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf3](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf3.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf3BitbucketCloudCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf4](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf4.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf4BitbucketServerCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf5](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf5.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf5DigitalOceanCrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf6](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf6.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf6DockerHubCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf7](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf7.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf7EcrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf8](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf8.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf8GcrCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf9](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf9.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOf9GitHubCredentials.md)
 - [SnykApi.AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials](docs/AddNewIntegrationRequestAnyOfCredentialsOneOfAcrCredentials.md)
 - [SnykApi.AggregatedProjectIssues](docs/AggregatedProjectIssues.md)
 - [SnykApi.AggregatedProjectIssuesFilters](docs/AggregatedProjectIssuesFilters.md)
 - [SnykApi.AggregatedProjectIssuesIssuesInner](docs/AggregatedProjectIssuesIssuesInner.md)
 - [SnykApi.AggregatedProjectIssuesIssuesInnerIssueData](docs/AggregatedProjectIssuesIssuesInnerIssueData.md)
 - [SnykApi.AllIgnores](docs/AllIgnores.md)
 - [SnykApi.AllJiraIssues](docs/AllJiraIssues.md)
 - [SnykApi.ApplyingAttributes200Response](docs/ApplyingAttributes200Response.md)
 - [SnykApi.ApplyingAttributes200ResponseAttributes](docs/ApplyingAttributes200ResponseAttributes.md)
 - [SnykApi.ApplyingAttributesRequest](docs/ApplyingAttributesRequest.md)
 - [SnykApi.AssignmentType](docs/AssignmentType.md)
 - [SnykApi.AutoRemediationPrs](docs/AutoRemediationPrs.md)
 - [SnykApi.BrokerSettings](docs/BrokerSettings.md)
 - [SnykApi.CloneAnIntegrationWithSettingsAndCredentialsRequest](docs/CloneAnIntegrationWithSettingsAndCredentialsRequest.md)
 - [SnykApi.ComposerLock](docs/ComposerLock.md)
 - [SnykApi.ComposerRequestPayload](docs/ComposerRequestPayload.md)
 - [SnykApi.CreateANewOrganization400Response](docs/CreateANewOrganization400Response.md)
 - [SnykApi.CreateANewOrganizationRequest](docs/CreateANewOrganizationRequest.md)
 - [SnykApi.CreateAWebhookRequest](docs/CreateAWebhookRequest.md)
 - [SnykApi.CreateJiraIssue200Response](docs/CreateJiraIssue200Response.md)
 - [SnykApi.CreateJiraIssue200ResponseJiraIssue](docs/CreateJiraIssue200ResponseJiraIssue.md)
 - [SnykApi.CreateJiraIssueRequest](docs/CreateJiraIssueRequest.md)
 - [SnykApi.CreateJiraIssueRequestFields](docs/CreateJiraIssueRequestFields.md)
 - [SnykApi.CreateOrganizationsBody](docs/CreateOrganizationsBody.md)
 - [SnykApi.DeletePendingUserProvision200Response](docs/DeletePendingUserProvision200Response.md)
 - [SnykApi.DeleteTagBody](docs/DeleteTagBody.md)
 - [SnykApi.DeleteTagFromGroup200Response](docs/DeleteTagFromGroup200Response.md)
 - [SnykApi.DeleteTagFromGroupRequest](docs/DeleteTagFromGroupRequest.md)
 - [SnykApi.DepGraphData](docs/DepGraphData.md)
 - [SnykApi.Dependencies](docs/Dependencies.md)
 - [SnykApi.DependenciesFilters](docs/DependenciesFilters.md)
 - [SnykApi.DependenciesFiltersFilters](docs/DependenciesFiltersFilters.md)
 - [SnykApi.ErrorResponse](docs/ErrorResponse.md)
 - [SnykApi.Function](docs/Function.md)
 - [SnykApi.FunctionId](docs/FunctionId.md)
 - [SnykApi.GetExistingIntegrationByType200Response](docs/GetExistingIntegrationByType200Response.md)
 - [SnykApi.GetGroupLevelAuditLogsRequest](docs/GetGroupLevelAuditLogsRequest.md)
 - [SnykApi.GetGroupLevelAuditLogsRequestFilters](docs/GetGroupLevelAuditLogsRequestFilters.md)
 - [SnykApi.GetImportJobDetails200Response](docs/GetImportJobDetails200Response.md)
 - [SnykApi.GetIssueCounts200Response](docs/GetIssueCounts200Response.md)
 - [SnykApi.GetIssueCounts200ResponseResultsInner](docs/GetIssueCounts200ResponseResultsInner.md)
 - [SnykApi.GetIssueCounts200ResponseResultsInnerFixable](docs/GetIssueCounts200ResponseResultsInnerFixable.md)
 - [SnykApi.GetIssueCounts200ResponseResultsInnerSeverity](docs/GetIssueCounts200ResponseResultsInnerSeverity.md)
 - [SnykApi.GetIssueCounts400Response](docs/GetIssueCounts400Response.md)
 - [SnykApi.GetIssueCounts400ResponseError](docs/GetIssueCounts400ResponseError.md)
 - [SnykApi.GetIssueCountsRequest](docs/GetIssueCountsRequest.md)
 - [SnykApi.GetIssueCountsRequestFilters](docs/GetIssueCountsRequestFilters.md)
 - [SnykApi.GetIssueCountsRequestFiltersPriorityScore](docs/GetIssueCountsRequestFiltersPriorityScore.md)
 - [SnykApi.GetListOfIssues200Response](docs/GetListOfIssues200Response.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInner](docs/GetListOfIssues200ResponseResultsInner.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInnerIssue](docs/GetListOfIssues200ResponseResultsInnerIssue.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInnerIssueIdentifiers](docs/GetListOfIssues200ResponseResultsInnerIssueIdentifiers.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInnerIssueSemver](docs/GetListOfIssues200ResponseResultsInnerIssueSemver.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInnerOneOf](docs/GetListOfIssues200ResponseResultsInnerOneOf.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInnerOneOf1](docs/GetListOfIssues200ResponseResultsInnerOneOf1.md)
 - [SnykApi.GetListOfIssues200ResponseResultsInnerOneOf1Project](docs/GetListOfIssues200ResponseResultsInnerOneOf1Project.md)
 - [SnykApi.GetListOfIssuesRequest](docs/GetListOfIssuesRequest.md)
 - [SnykApi.GetListOfIssuesRequestFilters](docs/GetListOfIssuesRequestFilters.md)
 - [SnykApi.GetMyDetails200Response](docs/GetMyDetails200Response.md)
 - [SnykApi.GetOrganizationLevelAuditLogsRequest](docs/GetOrganizationLevelAuditLogsRequest.md)
 - [SnykApi.GetOrganizationLevelAuditLogsRequestFilters](docs/GetOrganizationLevelAuditLogsRequestFilters.md)
 - [SnykApi.GetProjectCounts200Response](docs/GetProjectCounts200Response.md)
 - [SnykApi.GetProjectCounts200ResponseResultsInner](docs/GetProjectCounts200ResponseResultsInner.md)
 - [SnykApi.GetProjectCountsRequest](docs/GetProjectCountsRequest.md)
 - [SnykApi.GetProjectCountsRequestFilters](docs/GetProjectCountsRequestFilters.md)
 - [SnykApi.GetProjectDependencyGraph200Response](docs/GetProjectDependencyGraph200Response.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraph](docs/GetProjectDependencyGraph200ResponseDepGraph.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphGraph](docs/GetProjectDependencyGraph200ResponseDepGraphGraph.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner](docs/GetProjectDependencyGraph200ResponseDepGraphGraphNodesInner.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner](docs/GetProjectDependencyGraph200ResponseDepGraphGraphNodesInnerDepsInner.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphPkgManager](docs/GetProjectDependencyGraph200ResponseDepGraphPkgManager.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner](docs/GetProjectDependencyGraph200ResponseDepGraphPkgManagerRepositoriesInner.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphPkgsInner](docs/GetProjectDependencyGraph200ResponseDepGraphPkgsInner.md)
 - [SnykApi.GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo](docs/GetProjectDependencyGraph200ResponseDepGraphPkgsInnerInfo.md)
 - [SnykApi.GetTestCounts200Response](docs/GetTestCounts200Response.md)
 - [SnykApi.GetTestCounts200ResponseResultsInner](docs/GetTestCounts200ResponseResultsInner.md)
 - [SnykApi.GetTestCounts200ResponseResultsInnerIsPrivate](docs/GetTestCounts200ResponseResultsInnerIsPrivate.md)
 - [SnykApi.GetTestCounts200ResponseResultsInnerIssuesPrevented](docs/GetTestCounts200ResponseResultsInnerIssuesPrevented.md)
 - [SnykApi.GetTestCountsRequest](docs/GetTestCountsRequest.md)
 - [SnykApi.GetTestCountsRequestFilters](docs/GetTestCountsRequestFilters.md)
 - [SnykApi.GetUserDetails200Response](docs/GetUserDetails200Response.md)
 - [SnykApi.GoPkgLock](docs/GoPkgLock.md)
 - [SnykApi.GolangdepRequestPayload](docs/GolangdepRequestPayload.md)
 - [SnykApi.GovendorRequestPayload](docs/GovendorRequestPayload.md)
 - [SnykApi.GradleFile](docs/GradleFile.md)
 - [SnykApi.GradleRequestPayload](docs/GradleRequestPayload.md)
 - [SnykApi.GradleRequestPayloadFiles](docs/GradleRequestPayloadFiles.md)
 - [SnykApi.Graph](docs/Graph.md)
 - [SnykApi.GraphDependency](docs/GraphDependency.md)
 - [SnykApi.GraphRequestPayload](docs/GraphRequestPayload.md)
 - [SnykApi.GroupSettings](docs/GroupSettings.md)
 - [SnykApi.GroupsAuditLogsFilters](docs/GroupsAuditLogsFilters.md)
 - [SnykApi.Ignore](docs/Ignore.md)
 - [SnykApi.IgnoreIgnorePath](docs/IgnoreIgnorePath.md)
 - [SnykApi.IgnoreIgnorePathIgnoredBy](docs/IgnoreIgnorePathIgnoredBy.md)
 - [SnykApi.IgnoreRule](docs/IgnoreRule.md)
 - [SnykApi.ImportTargetsRequest](docs/ImportTargetsRequest.md)
 - [SnykApi.ImportTargetsRequestAnyOf](docs/ImportTargetsRequestAnyOf.md)
 - [SnykApi.ImportTargetsRequestAnyOf1](docs/ImportTargetsRequestAnyOf1.md)
 - [SnykApi.ImportTargetsRequestAnyOf1Target](docs/ImportTargetsRequestAnyOf1Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf2](docs/ImportTargetsRequestAnyOf2.md)
 - [SnykApi.ImportTargetsRequestAnyOf2Target](docs/ImportTargetsRequestAnyOf2Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf3](docs/ImportTargetsRequestAnyOf3.md)
 - [SnykApi.ImportTargetsRequestAnyOf3Target](docs/ImportTargetsRequestAnyOf3Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf4](docs/ImportTargetsRequestAnyOf4.md)
 - [SnykApi.ImportTargetsRequestAnyOf4Target](docs/ImportTargetsRequestAnyOf4Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf5](docs/ImportTargetsRequestAnyOf5.md)
 - [SnykApi.ImportTargetsRequestAnyOf5Target](docs/ImportTargetsRequestAnyOf5Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf6](docs/ImportTargetsRequestAnyOf6.md)
 - [SnykApi.ImportTargetsRequestAnyOf6Target](docs/ImportTargetsRequestAnyOf6Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf7](docs/ImportTargetsRequestAnyOf7.md)
 - [SnykApi.ImportTargetsRequestAnyOf7Target](docs/ImportTargetsRequestAnyOf7Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf8](docs/ImportTargetsRequestAnyOf8.md)
 - [SnykApi.ImportTargetsRequestAnyOf8Target](docs/ImportTargetsRequestAnyOf8Target.md)
 - [SnykApi.ImportTargetsRequestAnyOf9](docs/ImportTargetsRequestAnyOf9.md)
 - [SnykApi.ImportTargetsRequestAnyOf9Target](docs/ImportTargetsRequestAnyOf9Target.md)
 - [SnykApi.ImportTargetsRequestAnyOfTarget](docs/ImportTargetsRequestAnyOfTarget.md)
 - [SnykApi.IntegrationSettings](docs/IntegrationSettings.md)
 - [SnykApi.IntegrationType](docs/IntegrationType.md)
 - [SnykApi.Integrations](docs/Integrations.md)
 - [SnykApi.InviteUsersRequest](docs/InviteUsersRequest.md)
 - [SnykApi.IssueCounts](docs/IssueCounts.md)
 - [SnykApi.IssueCountsFilters](docs/IssueCountsFilters.md)
 - [SnykApi.IssueCountsFiltersFilters](docs/IssueCountsFiltersFilters.md)
 - [SnykApi.IssuePaths](docs/IssuePaths.md)
 - [SnykApi.Issues](docs/Issues.md)
 - [SnykApi.IssuesFilters](docs/IssuesFilters.md)
 - [SnykApi.IssuesFiltersFilters](docs/IssuesFiltersFilters.md)
 - [SnykApi.IssuesResultsInner](docs/IssuesResultsInner.md)
 - [SnykApi.JiraIssue](docs/JiraIssue.md)
 - [SnykApi.JiraIssueRequest](docs/JiraIssueRequest.md)
 - [SnykApi.Licenses](docs/Licenses.md)
 - [SnykApi.LicensesFilters](docs/LicensesFilters.md)
 - [SnykApi.LicensesFiltersFilters](docs/LicensesFiltersFilters.md)
 - [SnykApi.ListAllAggregatedIssues200Response](docs/ListAllAggregatedIssues200Response.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInner](docs/ListAllAggregatedIssues200ResponseIssuesInner.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerFixInfo](docs/ListAllAggregatedIssues200ResponseIssuesInnerFixInfo.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerIssueData](docs/ListAllAggregatedIssues200ResponseIssuesInnerIssueData.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers](docs/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataIdentifiers.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver](docs/ListAllAggregatedIssues200ResponseIssuesInnerIssueDataSemver.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerLinks](docs/ListAllAggregatedIssues200ResponseIssuesInnerLinks.md)
 - [SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerPriority](docs/ListAllAggregatedIssues200ResponseIssuesInnerPriority.md)
 - [SnykApi.ListAllAggregatedIssuesRequest](docs/ListAllAggregatedIssuesRequest.md)
 - [SnykApi.ListAllAggregatedIssuesRequestFilters](docs/ListAllAggregatedIssuesRequestFilters.md)
 - [SnykApi.ListAllAggregatedIssuesRequestFiltersPriority](docs/ListAllAggregatedIssuesRequestFiltersPriority.md)
 - [SnykApi.ListAllAggregatedIssuesRequestFiltersPriorityScore](docs/ListAllAggregatedIssuesRequestFiltersPriorityScore.md)
 - [SnykApi.ListAllDependencies200Response](docs/ListAllDependencies200Response.md)
 - [SnykApi.ListAllDependencies200ResponseResultsInner](docs/ListAllDependencies200ResponseResultsInner.md)
 - [SnykApi.ListAllDependencies200ResponseResultsInnerLicensesInner](docs/ListAllDependencies200ResponseResultsInnerLicensesInner.md)
 - [SnykApi.ListAllDependencies200ResponseResultsInnerProjectsInner](docs/ListAllDependencies200ResponseResultsInnerProjectsInner.md)
 - [SnykApi.ListAllDependenciesRequest](docs/ListAllDependenciesRequest.md)
 - [SnykApi.ListAllDependenciesRequestFilters](docs/ListAllDependenciesRequestFilters.md)
 - [SnykApi.ListAllLicenses200Response](docs/ListAllLicenses200Response.md)
 - [SnykApi.ListAllLicenses200ResponseResultsInner](docs/ListAllLicenses200ResponseResultsInner.md)
 - [SnykApi.ListAllLicenses200ResponseResultsInnerDependenciesInner](docs/ListAllLicenses200ResponseResultsInnerDependenciesInner.md)
 - [SnykApi.ListAllLicensesRequest](docs/ListAllLicensesRequest.md)
 - [SnykApi.ListAllLicensesRequestFilters](docs/ListAllLicensesRequestFilters.md)
 - [SnykApi.ListAllProjectSnapshotIssuePaths200Response](docs/ListAllProjectSnapshotIssuePaths200Response.md)
 - [SnykApi.ListAllProjectSnapshotIssuePaths200ResponseLinks](docs/ListAllProjectSnapshotIssuePaths200ResponseLinks.md)
 - [SnykApi.ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner](docs/ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner.md)
 - [SnykApi.ListAllProjectSnapshots200Response](docs/ListAllProjectSnapshots200Response.md)
 - [SnykApi.ListAllProjectSnapshots200ResponseSnapshotsInner](docs/ListAllProjectSnapshots200ResponseSnapshotsInner.md)
 - [SnykApi.ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts](docs/ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCounts.md)
 - [SnykApi.ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense](docs/ListAllProjectSnapshots200ResponseSnapshotsInnerIssueCountsLicense.md)
 - [SnykApi.ListAllProjectSnapshotsRequest](docs/ListAllProjectSnapshotsRequest.md)
 - [SnykApi.ListAllProjectSnapshotsRequestFilters](docs/ListAllProjectSnapshotsRequestFilters.md)
 - [SnykApi.ListAllProjects](docs/ListAllProjects.md)
 - [SnykApi.ListAllProjects200Response](docs/ListAllProjects200Response.md)
 - [SnykApi.ListAllProjects200ResponseOrg](docs/ListAllProjects200ResponseOrg.md)
 - [SnykApi.ListAllProjects200ResponseProjectsInner](docs/ListAllProjects200ResponseProjectsInner.md)
 - [SnykApi.ListAllProjectsRequest](docs/ListAllProjectsRequest.md)
 - [SnykApi.ListAllProjectsRequestFilters](docs/ListAllProjectsRequestFilters.md)
 - [SnykApi.ListAllProjectsRequestFiltersAttributes](docs/ListAllProjectsRequestFiltersAttributes.md)
 - [SnykApi.ListAllProjectsRequestFiltersTags](docs/ListAllProjectsRequestFiltersTags.md)
 - [SnykApi.ListAllTagsInAGroup200Response](docs/ListAllTagsInAGroup200Response.md)
 - [SnykApi.ListProjectSettings200Response](docs/ListProjectSettings200Response.md)
 - [SnykApi.ListProjectSettings200ResponseAutoRemediationPrs](docs/ListProjectSettings200ResponseAutoRemediationPrs.md)
 - [SnykApi.MavenAdditionalFile](docs/MavenAdditionalFile.md)
 - [SnykApi.MavenFile](docs/MavenFile.md)
 - [SnykApi.MavenRequestPayload](docs/MavenRequestPayload.md)
 - [SnykApi.MavenRequestPayloadFiles](docs/MavenRequestPayloadFiles.md)
 - [SnykApi.ModifyProjectNotificationSettingsRequest](docs/ModifyProjectNotificationSettingsRequest.md)
 - [SnykApi.MonitorDepGraphData](docs/MonitorDepGraphData.md)
 - [SnykApi.MonitorDepGraphRequest](docs/MonitorDepGraphRequest.md)
 - [SnykApi.MonitorDepGraphRequestDepGraph](docs/MonitorDepGraphRequestDepGraph.md)
 - [SnykApi.MonitorDepGraphRequestDepGraphGraph](docs/MonitorDepGraphRequestDepGraphGraph.md)
 - [SnykApi.MonitorDepGraphRequestDepGraphPkgManager](docs/MonitorDepGraphRequestDepGraphPkgManager.md)
 - [SnykApi.MonitorDepGraphRequestMeta](docs/MonitorDepGraphRequestMeta.md)
 - [SnykApi.MonitorGraph](docs/MonitorGraph.md)
 - [SnykApi.MonitorGraphDependency](docs/MonitorGraphDependency.md)
 - [SnykApi.MonitorGraphPayload](docs/MonitorGraphPayload.md)
 - [SnykApi.MonitorMetaData](docs/MonitorMetaData.md)
 - [SnykApi.MonitorNode](docs/MonitorNode.md)
 - [SnykApi.MonitorPackage](docs/MonitorPackage.md)
 - [SnykApi.MonitorPackageInfo](docs/MonitorPackageInfo.md)
 - [SnykApi.MonitorPkgManager](docs/MonitorPkgManager.md)
 - [SnykApi.MonitorRepository](docs/MonitorRepository.md)
 - [SnykApi.MoveProjectToADifferentOrganizationRequest](docs/MoveProjectToADifferentOrganizationRequest.md)
 - [SnykApi.NewIssuesNotificationSettingRequest](docs/NewIssuesNotificationSettingRequest.md)
 - [SnykApi.Node](docs/Node.md)
 - [SnykApi.NotificationSettingResponse](docs/NotificationSettingResponse.md)
 - [SnykApi.NotificationSettingsRequest](docs/NotificationSettingsRequest.md)
 - [SnykApi.NotificationSettingsResponse](docs/NotificationSettingsResponse.md)
 - [SnykApi.NpmRequestPayload](docs/NpmRequestPayload.md)
 - [SnykApi.OrgAuditLogsFilters](docs/OrgAuditLogsFilters.md)
 - [SnykApi.OrgOrgIdNotificationSettingsGet200Response](docs/OrgOrgIdNotificationSettingsGet200Response.md)
 - [SnykApi.OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations](docs/OrgOrgIdNotificationSettingsGet200ResponseNewIssuesRemediations.md)
 - [SnykApi.OrgOrgIdNotificationSettingsGet200ResponseProjectImported](docs/OrgOrgIdNotificationSettingsGet200ResponseProjectImported.md)
 - [SnykApi.OrgSettingsRequest](docs/OrgSettingsRequest.md)
 - [SnykApi.OrgSettingsResponse](docs/OrgSettingsResponse.md)
 - [SnykApi.Package](docs/Package.md)
 - [SnykApi.PackageInfo](docs/PackageInfo.md)
 - [SnykApi.PackageLockJsonFile](docs/PackageLockJsonFile.md)
 - [SnykApi.Patch](docs/Patch.md)
 - [SnykApi.PipRequestPayload](docs/PipRequestPayload.md)
 - [SnykApi.PkgManager](docs/PkgManager.md)
 - [SnykApi.PriorityScore](docs/PriorityScore.md)
 - [SnykApi.Project](docs/Project.md)
 - [SnykApi.ProjectAttributes](docs/ProjectAttributes.md)
 - [SnykApi.ProjectCounts](docs/ProjectCounts.md)
 - [SnykApi.ProjectCountsFilters](docs/ProjectCountsFilters.md)
 - [SnykApi.ProjectCountsFiltersFilters](docs/ProjectCountsFiltersFilters.md)
 - [SnykApi.ProjectDependencyGraph](docs/ProjectDependencyGraph.md)
 - [SnykApi.ProjectIssuesFilters](docs/ProjectIssuesFilters.md)
 - [SnykApi.ProjectIssuesFiltersFilters](docs/ProjectIssuesFiltersFilters.md)
 - [SnykApi.ProjectIssuesFiltersFiltersPriorityScore](docs/ProjectIssuesFiltersFiltersPriorityScore.md)
 - [SnykApi.ProjectMove](docs/ProjectMove.md)
 - [SnykApi.ProjectSettings](docs/ProjectSettings.md)
 - [SnykApi.ProjectSnapshots](docs/ProjectSnapshots.md)
 - [SnykApi.ProjectSnapshotsFilters](docs/ProjectSnapshotsFilters.md)
 - [SnykApi.ProjectWithoutRemediation](docs/ProjectWithoutRemediation.md)
 - [SnykApi.ProjectsFilters](docs/ProjectsFilters.md)
 - [SnykApi.ProjectsFiltersFilters](docs/ProjectsFiltersFilters.md)
 - [SnykApi.ProvisionAUserToTheOrganization200Response](docs/ProvisionAUserToTheOrganization200Response.md)
 - [SnykApi.ProvisionAUserToTheOrganizationRequest](docs/ProvisionAUserToTheOrganizationRequest.md)
 - [SnykApi.PullRequestAssignment](docs/PullRequestAssignment.md)
 - [SnykApi.Repository](docs/Repository.md)
 - [SnykApi.Retrieve200Response](docs/Retrieve200Response.md)
 - [SnykApi.Retrieve200ResponseAutoRemediationPrs](docs/Retrieve200ResponseAutoRemediationPrs.md)
 - [SnykApi.Retrieve200ResponseManualRemediationPrs](docs/Retrieve200ResponseManualRemediationPrs.md)
 - [SnykApi.Retrieve200ResponsePullRequestAssignment](docs/Retrieve200ResponsePullRequestAssignment.md)
 - [SnykApi.RetrieveASingleProject200Response](docs/RetrieveASingleProject200Response.md)
 - [SnykApi.RetrieveASingleProject200ResponseAttributes](docs/RetrieveASingleProject200ResponseAttributes.md)
 - [SnykApi.RetrieveASingleProject200ResponseImportingUser](docs/RetrieveASingleProject200ResponseImportingUser.md)
 - [SnykApi.RetrieveASingleProject200ResponseIssueCountsBySeverity](docs/RetrieveASingleProject200ResponseIssueCountsBySeverity.md)
 - [SnykApi.RetrieveASingleProject200ResponseRemediation](docs/RetrieveASingleProject200ResponseRemediation.md)
 - [SnykApi.RubygemsRequestPayload](docs/RubygemsRequestPayload.md)
 - [SnykApi.SBTFile](docs/SBTFile.md)
 - [SnykApi.SbtRequestPayload](docs/SbtRequestPayload.md)
 - [SnykApi.SbtRequestPayloadFiles](docs/SbtRequestPayloadFiles.md)
 - [SnykApi.SemverObject](docs/SemverObject.md)
 - [SnykApi.SetNotificationSettingsRequest](docs/SetNotificationSettingsRequest.md)
 - [SnykApi.SetNotificationSettingsRequestNewIssuesRemediations](docs/SetNotificationSettingsRequestNewIssuesRemediations.md)
 - [SnykApi.SetNotificationSettingsRequestProjectImported](docs/SetNotificationSettingsRequestProjectImported.md)
 - [SnykApi.SimpleNotificationSettingRequest](docs/SimpleNotificationSettingRequest.md)
 - [SnykApi.SimpleNotificationSettingResponse](docs/SimpleNotificationSettingResponse.md)
 - [SnykApi.Tag](docs/Tag.md)
 - [SnykApi.TagBody](docs/TagBody.md)
 - [SnykApi.TestComposerJsonComposerLockFileRequest](docs/TestComposerJsonComposerLockFileRequest.md)
 - [SnykApi.TestComposerJsonComposerLockFileRequestFiles](docs/TestComposerJsonComposerLockFileRequestFiles.md)
 - [SnykApi.TestComposerJsonComposerLockFileRequestFilesTarget](docs/TestComposerJsonComposerLockFileRequestFilesTarget.md)
 - [SnykApi.TestDepGraphRequest](docs/TestDepGraphRequest.md)
 - [SnykApi.TestDepGraphRequestDepGraph](docs/TestDepGraphRequestDepGraph.md)
 - [SnykApi.TestDepGraphRequestDepGraphGraph](docs/TestDepGraphRequestDepGraphGraph.md)
 - [SnykApi.TestGemfileLockFileRequest](docs/TestGemfileLockFileRequest.md)
 - [SnykApi.TestGemfileLockFileRequestFiles](docs/TestGemfileLockFileRequestFiles.md)
 - [SnykApi.TestGemfileLockFileRequestFilesTarget](docs/TestGemfileLockFileRequestFilesTarget.md)
 - [SnykApi.TestGopkgTomlGopkgLockFileRequest](docs/TestGopkgTomlGopkgLockFileRequest.md)
 - [SnykApi.TestGopkgTomlGopkgLockFileRequestFiles](docs/TestGopkgTomlGopkgLockFileRequestFiles.md)
 - [SnykApi.TestGopkgTomlGopkgLockFileRequestFilesTarget](docs/TestGopkgTomlGopkgLockFileRequestFilesTarget.md)
 - [SnykApi.TestGradleFileRequest](docs/TestGradleFileRequest.md)
 - [SnykApi.TestGradleFileRequestFiles](docs/TestGradleFileRequestFiles.md)
 - [SnykApi.TestGradleFileRequestFilesTarget](docs/TestGradleFileRequestFilesTarget.md)
 - [SnykApi.TestMavenFileRequest](docs/TestMavenFileRequest.md)
 - [SnykApi.TestMavenFileRequestFiles](docs/TestMavenFileRequestFiles.md)
 - [SnykApi.TestMavenFileRequestFilesTarget](docs/TestMavenFileRequestFilesTarget.md)
 - [SnykApi.TestPackageJsonPackageLockJsonFileRequest](docs/TestPackageJsonPackageLockJsonFileRequest.md)
 - [SnykApi.TestPackageJsonPackageLockJsonFileRequestFiles](docs/TestPackageJsonPackageLockJsonFileRequestFiles.md)
 - [SnykApi.TestPackageJsonPackageLockJsonFileRequestFilesTarget](docs/TestPackageJsonPackageLockJsonFileRequestFilesTarget.md)
 - [SnykApi.TestPackageJsonYarnLockFileRequest](docs/TestPackageJsonYarnLockFileRequest.md)
 - [SnykApi.TestRequirementsTxtFileRequest](docs/TestRequirementsTxtFileRequest.md)
 - [SnykApi.TestRequirementsTxtFileRequestFiles](docs/TestRequirementsTxtFileRequestFiles.md)
 - [SnykApi.TestRequirementsTxtFileRequestFilesTarget](docs/TestRequirementsTxtFileRequestFilesTarget.md)
 - [SnykApi.TestSbtFileRequest](docs/TestSbtFileRequest.md)
 - [SnykApi.TestVendorJsonFileRequest](docs/TestVendorJsonFileRequest.md)
 - [SnykApi.TestVendorJsonFileRequestFiles](docs/TestVendorJsonFileRequestFiles.md)
 - [SnykApi.TestVendorJsonFileRequestFilesTarget](docs/TestVendorJsonFileRequestFilesTarget.md)
 - [SnykApi.TestsFilters](docs/TestsFilters.md)
 - [SnykApi.TestsFiltersFilters](docs/TestsFiltersFilters.md)
 - [SnykApi.UpdateAMemberInTheOrganizationRequest](docs/UpdateAMemberInTheOrganizationRequest.md)
 - [SnykApi.UpdateAMemberSRoleInTheOrganizationRequest](docs/UpdateAMemberSRoleInTheOrganizationRequest.md)
 - [SnykApi.UpdateAProjectRequest](docs/UpdateAProjectRequest.md)
 - [SnykApi.UpdateAProjectRequestOwner](docs/UpdateAProjectRequestOwner.md)
 - [SnykApi.UpdateExistingIntegrationRequest](docs/UpdateExistingIntegrationRequest.md)
 - [SnykApi.UpdateExistingIntegrationRequestAnyOf](docs/UpdateExistingIntegrationRequestAnyOf.md)
 - [SnykApi.UpdateExistingIntegrationRequestAnyOf1](docs/UpdateExistingIntegrationRequestAnyOf1.md)
 - [SnykApi.UpdateExistingIntegrationRequestAnyOf2](docs/UpdateExistingIntegrationRequestAnyOf2.md)
 - [SnykApi.UpdateOrganizationSettingsRequest](docs/UpdateOrganizationSettingsRequest.md)
 - [SnykApi.UpdateOrganizationSettingsRequestRequestAccess](docs/UpdateOrganizationSettingsRequestRequestAccess.md)
 - [SnykApi.UpdateProjectSettingsRequest](docs/UpdateProjectSettingsRequest.md)
 - [SnykApi.UpdateRequest](docs/UpdateRequest.md)
 - [SnykApi.ViewGroupSettings200Response](docs/ViewGroupSettings200Response.md)
 - [SnykApi.ViewGroupSettings200ResponseRequestAccess](docs/ViewGroupSettings200ResponseRequestAccess.md)
 - [SnykApi.ViewOrganizationSettings200Response](docs/ViewOrganizationSettings200Response.md)
 - [SnykApi.ViewOrganizationSettings200ResponseRequestAccess](docs/ViewOrganizationSettings200ResponseRequestAccess.md)
 - [SnykApi.Vulnerability](docs/Vulnerability.md)
 - [SnykApi.YarnLockFile](docs/YarnLockFile.md)
 - [SnykApi.YarnRequestPayload](docs/YarnRequestPayload.md)


## Documentation for Authorization

Endpoints do not require authorization.

