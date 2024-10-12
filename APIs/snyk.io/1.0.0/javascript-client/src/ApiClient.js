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


import superagent from "superagent";
import querystring from "querystring";

/**
* @module ApiClient
* @version 1.0.0
*/

/**
* Manages low level client-server communications, parameter marshalling, etc. There should not be any need for an
* application to use this class directly - the *Api and model classes provide the public API for the service. The
* contents of this file should be regarded as internal but are documented for completeness.
* @alias module:ApiClient
* @class
*/
class ApiClient {
    /**
     * The base URL against which to resolve every API call's (relative) path.
     * Overrides the default value set in spec file if present
     * @param {String} basePath
     */
    constructor(basePath = 'https://api.snyk.io/v1') {
        /**
         * The base URL against which to resolve every API call's (relative) path.
         * @type {String}
         * @default https://api.snyk.io/v1
         */
        this.basePath = basePath.replace(/\/+$/, '');

        /**
         * The authentication methods to be included for all API calls.
         * @type {Array.<String>}
         */
        this.authentications = {
        }

        /**
         * The default HTTP headers to be included for all API calls.
         * @type {Array.<String>}
         * @default {}
         */
        this.defaultHeaders = {
            'User-Agent': 'OpenAPI-Generator/1.0.0/Javascript'
        };

        /**
         * The default HTTP timeout for all API calls.
         * @type {Number}
         * @default 60000
         */
        this.timeout = 60000;

        /**
         * If set to false an additional timestamp parameter is added to all API GET calls to
         * prevent browser caching
         * @type {Boolean}
         * @default true
         */
        this.cache = true;

        /**
         * If set to true, the client will save the cookies from each server
         * response, and return them in the next request.
         * @default false
         */
        this.enableCookies = false;

        /*
         * Used to save and return cookies in a node.js (non-browser) setting,
         * if this.enableCookies is set to true.
         */
        if (typeof window === 'undefined') {
          this.agent = new superagent.agent();
        }

        /*
         * Allow user to override superagent agent
         */
         this.requestAgent = null;

        /*
         * Allow user to add superagent plugins
         */
        this.plugins = null;

    }

    /**
    * Returns a string representation for an actual parameter.
    * @param param The actual parameter.
    * @returns {String} The string representation of <code>param</code>.
    */
    paramToString(param) {
        if (param == undefined || param == null) {
            return '';
        }
        if (param instanceof Date) {
            return param.toJSON();
        }
        if (ApiClient.canBeJsonified(param)) {
            return JSON.stringify(param);
        }

        return param.toString();
    }

    /**
    * Returns a boolean indicating if the parameter could be JSON.stringified
    * @param param The actual parameter
    * @returns {Boolean} Flag indicating if <code>param</code> can be JSON.stringified
    */
    static canBeJsonified(str) {
        if (typeof str !== 'string' && typeof str !== 'object') return false;
        try {
            const type = str.toString();
            return type === '[object Object]'
                || type === '[object Array]';
        } catch (err) {
            return false;
        }
    };

   /**
    * Builds full URL by appending the given path to the base URL and replacing path parameter place-holders with parameter values.
    * NOTE: query parameters are not handled here.
    * @param {String} path The path to append to the base URL.
    * @param {Object} pathParams The parameter values to append.
    * @param {String} apiBasePath Base path defined in the path, operation level to override the default one
    * @returns {String} The encoded path with parameter values substituted.
    */
    buildUrl(path, pathParams, apiBasePath) {
        if (!path.match(/^\//)) {
            path = '/' + path;
        }

        var url = this.basePath + path;

        // use API (operation, path) base path if defined
        if (apiBasePath !== null && apiBasePath !== undefined) {
            url = apiBasePath + path;
        }

        url = url.replace(/\{([\w-\.#]+)\}/g, (fullMatch, key) => {
            var value;
            if (pathParams.hasOwnProperty(key)) {
                value = this.paramToString(pathParams[key]);
            } else {
                value = fullMatch;
            }

            return encodeURIComponent(value);
        });

        return url;
    }

    /**
    * Checks whether the given content type represents JSON.<br>
    * JSON content type examples:<br>
    * <ul>
    * <li>application/json</li>
    * <li>application/json; charset=UTF8</li>
    * <li>APPLICATION/JSON</li>
    * </ul>
    * @param {String} contentType The MIME content type to check.
    * @returns {Boolean} <code>true</code> if <code>contentType</code> represents JSON, otherwise <code>false</code>.
    */
    isJsonMime(contentType) {
        return Boolean(contentType != null && contentType.match(/^application\/json(;.*)?$/i));
    }

    /**
    * Chooses a content type from the given array, with JSON preferred; i.e. return JSON if included, otherwise return the first.
    * @param {Array.<String>} contentTypes
    * @returns {String} The chosen content type, preferring JSON.
    */
    jsonPreferredMime(contentTypes) {
        for (var i = 0; i < contentTypes.length; i++) {
            if (this.isJsonMime(contentTypes[i])) {
                return contentTypes[i];
            }
        }

        return contentTypes[0];
    }

    /**
    * Checks whether the given parameter value represents file-like content.
    * @param param The parameter to check.
    * @returns {Boolean} <code>true</code> if <code>param</code> represents a file.
    */
    isFileParam(param) {
        // fs.ReadStream in Node.js and Electron (but not in runtime like browserify)
        if (typeof require === 'function') {
            let fs;
            try {
                fs = require('fs');
            } catch (err) {}
            if (fs && fs.ReadStream && param instanceof fs.ReadStream) {
                return true;
            }
        }

        // Buffer in Node.js
        if (typeof Buffer === 'function' && param instanceof Buffer) {
            return true;
        }

        // Blob in browser
        if (typeof Blob === 'function' && param instanceof Blob) {
            return true;
        }

        // File in browser (it seems File object is also instance of Blob, but keep this for safe)
        if (typeof File === 'function' && param instanceof File) {
            return true;
        }

        return false;
    }

    /**
    * Normalizes parameter values:
    * <ul>
    * <li>remove nils</li>
    * <li>keep files and arrays</li>
    * <li>format to string with `paramToString` for other cases</li>
    * </ul>
    * @param {Object.<String, Object>} params The parameters as object properties.
    * @returns {Object.<String, Object>} normalized parameters.
    */
    normalizeParams(params) {
        var newParams = {};
        for (var key in params) {
            if (params.hasOwnProperty(key) && params[key] != undefined && params[key] != null) {
                var value = params[key];
                if (this.isFileParam(value) || Array.isArray(value)) {
                    newParams[key] = value;
                } else {
                    newParams[key] = this.paramToString(value);
                }
            }
        }

        return newParams;
    }

    /**
    * Builds a string representation of an array-type actual parameter, according to the given collection format.
    * @param {Array} param An array parameter.
    * @param {module:ApiClient.CollectionFormatEnum} collectionFormat The array element separator strategy.
    * @returns {String|Array} A string representation of the supplied collection, using the specified delimiter. Returns
    * <code>param</code> as is if <code>collectionFormat</code> is <code>multi</code>.
    */
    buildCollectionParam(param, collectionFormat) {
        if (param == null) {
            return null;
        }
        switch (collectionFormat) {
            case 'csv':
                return param.map(this.paramToString, this).join(',');
            case 'ssv':
                return param.map(this.paramToString, this).join(' ');
            case 'tsv':
                return param.map(this.paramToString, this).join('\t');
            case 'pipes':
                return param.map(this.paramToString, this).join('|');
            case 'multi':
                //return the array directly as SuperAgent will handle it as expected
                return param.map(this.paramToString, this);
            case 'passthrough':
                return param;
            default:
                throw new Error('Unknown collection format: ' + collectionFormat);
        }
    }

    /**
    * Applies authentication headers to the request.
    * @param {Object} request The request object created by a <code>superagent()</code> call.
    * @param {Array.<String>} authNames An array of authentication method names.
    */
    applyAuthToRequest(request, authNames) {
        authNames.forEach((authName) => {
            var auth = this.authentications[authName];
            switch (auth.type) {
                case 'basic':
                    if (auth.username || auth.password) {
                        request.auth(auth.username || '', auth.password || '');
                    }

                    break;
                case 'bearer':
                    if (auth.accessToken) {
                        var localVarBearerToken = typeof auth.accessToken === 'function'
                          ? auth.accessToken()
                          : auth.accessToken
                        request.set({'Authorization': 'Bearer ' + localVarBearerToken});
                    }

                    break;
                case 'apiKey':
                    if (auth.apiKey) {
                        var data = {};
                        if (auth.apiKeyPrefix) {
                            data[auth.name] = auth.apiKeyPrefix + ' ' + auth.apiKey;
                        } else {
                            data[auth.name] = auth.apiKey;
                        }

                        if (auth['in'] === 'header') {
                            request.set(data);
                        } else {
                            request.query(data);
                        }
                    }

                    break;
                case 'oauth2':
                    if (auth.accessToken) {
                        request.set({'Authorization': 'Bearer ' + auth.accessToken});
                    }

                    break;
                default:
                    throw new Error('Unknown authentication type: ' + auth.type);
            }
        });
    }

   /**
    * Deserializes an HTTP response body into a value of the specified type.
    * @param {Object} response A SuperAgent response object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} returnType The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns A value of the specified type.
    */
    deserialize(response, returnType) {
        if (response == null || returnType == null || response.status == 204) {
            return null;
        }

        // Rely on SuperAgent for parsing response body.
        // See http://visionmedia.github.io/superagent/#parsing-response-bodies
        var data = response.body;
        if (data == null || (typeof data === 'object' && typeof data.length === 'undefined' && !Object.keys(data).length)) {
            // SuperAgent does not always produce a body; use the unparsed response as a fallback
            data = response.text;
        }

        return ApiClient.convertToType(data, returnType);
    }

   /**
    * Callback function to receive the result of the operation.
    * @callback module:ApiClient~callApiCallback
    * @param {String} error Error message, if any.
    * @param data The data returned by the service call.
    * @param {String} response The complete HTTP response.
    */

   /**
    * Invokes the REST service using the supplied settings and parameters.
    * @param {String} path The base URL to invoke.
    * @param {String} httpMethod The HTTP method to use.
    * @param {Object.<String, String>} pathParams A map of path parameters and their values.
    * @param {Object.<String, Object>} queryParams A map of query parameters and their values.
    * @param {Object.<String, Object>} headerParams A map of header parameters and their values.
    * @param {Object.<String, Object>} formParams A map of form parameters and their values.
    * @param {Object} bodyParam The value to pass as the request body.
    * @param {Array.<String>} authNames An array of authentication type names.
    * @param {Array.<String>} contentTypes An array of request MIME types.
    * @param {Array.<String>} accepts An array of acceptable response MIME types.
    * @param {(String|Array|ObjectFunction)} returnType The required type to return; can be a string for simple types or the
    * constructor for a complex type.
    * @param {String} apiBasePath base path defined in the operation/path level to override the default one
    * @param {module:ApiClient~callApiCallback} callback The callback function.
    * @returns {Object} The SuperAgent request object.
    */
    callApi(path, httpMethod, pathParams,
        queryParams, headerParams, formParams, bodyParam, authNames, contentTypes, accepts,
        returnType, apiBasePath, callback) {

        var url = this.buildUrl(path, pathParams, apiBasePath);
        var request = superagent(httpMethod, url);

        if (this.plugins !== null) {
            for (var index in this.plugins) {
                if (this.plugins.hasOwnProperty(index)) {
                    request.use(this.plugins[index])
                }
            }
        }

        // apply authentications
        this.applyAuthToRequest(request, authNames);

        // set query parameters
        if (httpMethod.toUpperCase() === 'GET' && this.cache === false) {
            queryParams['_'] = new Date().getTime();
        }

        request.query(this.normalizeParams(queryParams));

        // set header parameters
        request.set(this.defaultHeaders).set(this.normalizeParams(headerParams));

        // set requestAgent if it is set by user
        if (this.requestAgent) {
          request.agent(this.requestAgent);
        }

        // set request timeout
        request.timeout(this.timeout);

        var contentType = this.jsonPreferredMime(contentTypes);
        if (contentType) {
            // Issue with superagent and multipart/form-data (https://github.com/visionmedia/superagent/issues/746)
            if(contentType != 'multipart/form-data') {
                request.type(contentType);
            }
        }

        if (contentType === 'application/x-www-form-urlencoded') {
            request.send(querystring.stringify(this.normalizeParams(formParams)));
        } else if (contentType == 'multipart/form-data') {
            var _formParams = this.normalizeParams(formParams);
            for (var key in _formParams) {
                if (_formParams.hasOwnProperty(key)) {
                    let _formParamsValue = _formParams[key];
                    if (this.isFileParam(_formParamsValue)) {
                        // file field
                        request.attach(key, _formParamsValue);
                    } else if (Array.isArray(_formParamsValue) && _formParamsValue.length
                        && this.isFileParam(_formParamsValue[0])) {
                        // multiple files
                        _formParamsValue.forEach(file => request.attach(key, file));
                    } else {
                        request.field(key, _formParamsValue);
                    }
                }
            }
        } else if (bodyParam !== null && bodyParam !== undefined) {
            if (!request.header['Content-Type']) {
                request.type('application/json');
            }
            request.send(bodyParam);
        }

        var accept = this.jsonPreferredMime(accepts);
        if (accept) {
            request.accept(accept);
        }

        if (returnType === 'Blob') {
          request.responseType('blob');
        } else if (returnType === 'String') {
          request.responseType('text');
        }

        // Attach previously saved cookies, if enabled
        if (this.enableCookies){
            if (typeof window === 'undefined') {
                this.agent._attachCookies(request);
            }
            else {
                request.withCredentials();
            }
        }

        request.end((error, response) => {
            if (callback) {
                var data = null;
                if (!error) {
                    try {
                        data = this.deserialize(response, returnType);
                        if (this.enableCookies && typeof window === 'undefined'){
                            this.agent._saveCookies(response);
                        }
                    } catch (err) {
                        error = err;
                    }
                }

                callback(error, data, response);
            }
        });

        return request;
    }

    /**
    * Parses an ISO-8601 string representation or epoch representation of a date value.
    * @param {String} str The date value as a string.
    * @returns {Date} The parsed date object.
    */
    static parseDate(str) {
        if (isNaN(str)) {
            return new Date(str.replace(/(\d)(T)(\d)/i, '$1 $3'));
        }
        return new Date(+str);
    }

    /**
    * Converts a value to the specified type.
    * @param {(String|Object)} data The data to convert, as a string or object.
    * @param {(String|Array.<String>|Object.<String, Object>|Function)} type The type to return. Pass a string for simple types
    * or the constructor function for a complex type. Pass an array containing the type name to return an array of that type. To
    * return an object, pass an object with one property whose name is the key type and whose value is the corresponding value type:
    * all properties on <code>data<code> will be converted to this type.
    * @returns An instance of the specified type or null or undefined if data is null or undefined.
    */
    static convertToType(data, type) {
        if (data === null || data === undefined)
            return data

        switch (type) {
            case 'Boolean':
                return Boolean(data);
            case 'Integer':
                return parseInt(data, 10);
            case 'Number':
                return parseFloat(data);
            case 'String':
                return String(data);
            case 'Date':
                return ApiClient.parseDate(String(data));
            case 'Blob':
                return data;
            default:
                if (type === Object) {
                    // generic object, return directly
                    return data;
                } else if (typeof type.constructFromObject === 'function') {
                    // for model type like User and enum class
                    return type.constructFromObject(data);
                } else if (Array.isArray(type)) {
                    // for array type like: ['String']
                    var itemType = type[0];

                    return data.map((item) => {
                        return ApiClient.convertToType(item, itemType);
                    });
                } else if (typeof type === 'object') {
                    // for plain object type like: {'String': 'Integer'}
                    var keyType, valueType;
                    for (var k in type) {
                        if (type.hasOwnProperty(k)) {
                            keyType = k;
                            valueType = type[k];
                            break;
                        }
                    }

                    var result = {};
                    for (var k in data) {
                        if (data.hasOwnProperty(k)) {
                            var key = ApiClient.convertToType(k, keyType);
                            var value = ApiClient.convertToType(data[k], valueType);
                            result[key] = value;
                        }
                    }

                    return result;
                } else {
                    // for unknown type, return the data directly
                    return data;
                }
        }
    }

  /**
    * Gets an array of host settings
    * @returns An array of host settings
    */
    hostSettings() {
        return [
            {
              'url': "https://api.snyk.io/v1",
              'description': "No description provided",
            }
      ];
    }

    getBasePathFromSettings(index, variables={}) {
        var servers = this.hostSettings();

        // check array index out of bound
        if (index < 0 || index >= servers.length) {
            throw new Error("Invalid index " + index + " when selecting the host settings. Must be less than " + servers.length);
        }

        var server = servers[index];
        var url = server['url'];

        // go through variable and assign a value
        for (var variable_name in server['variables']) {
            if (variable_name in variables) {
                let variable = server['variables'][variable_name];
                if ( !('enum_values' in variable) || variable['enum_values'].includes(variables[variable_name]) ) {
                    url = url.replace("{" + variable_name + "}", variables[variable_name]);
                } else {
                    throw new Error("The variable `" + variable_name + "` in the host URL has invalid value " + variables[variable_name] + ". Must be " + server['variables'][variable_name]['enum_values'] + ".");
                }
            } else {
                // use default value
                url = url.replace("{" + variable_name + "}", server['variables'][variable_name]['default_value'])
            }
        }
        return url;
    }

    /**
    * Constructs a new map or array model from REST data.
    * @param data {Object|Array} The REST data.
    * @param obj {Object|Array} The target object or array.
    */
    static constructFromObject(data, obj, itemType) {
        if (Array.isArray(data)) {
            for (var i = 0; i < data.length; i++) {
                if (data.hasOwnProperty(i))
                    obj[i] = ApiClient.convertToType(data[i], itemType);
            }
        } else {
            for (var k in data) {
                if (data.hasOwnProperty(k))
                    obj[k] = ApiClient.convertToType(data[k], itemType);
            }
        }
    };
}

/**
 * Enumeration of collection format separator strategies.
 * @enum {String}
 * @readonly
 */
ApiClient.CollectionFormatEnum = {
    /**
     * Comma-separated values. Value: <code>csv</code>
     * @const
     */
    CSV: ',',

    /**
     * Space-separated values. Value: <code>ssv</code>
     * @const
     */
    SSV: ' ',

    /**
     * Tab-separated values. Value: <code>tsv</code>
     * @const
     */
    TSV: '\t',

    /**
     * Pipe(|)-separated values. Value: <code>pipes</code>
     * @const
     */
    PIPES: '|',

    /**
     * Native array. Value: <code>multi</code>
     * @const
     */
    MULTI: 'multi'
};

/**
* The default API client implementation.
* @type {module:ApiClient}
*/
ApiClient.instance = new ApiClient();
export default ApiClient;
