# public_api

PublicApi - JavaScript client for public_api
# Introduction

This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.

# Conventions

## Requests

The API supports different methods depending on the required action.

| Method | Description
| ---  | ---
| GET  | Retrieve resources in a collection or get a single resource.<br/>Getters will never have any effect on the queried resources.
| POST  | Create a new resource in a collection.
| PUT  | Update an existing resource with its new representation.
| DELETE | Delete an existing resource.

## HTTP status codes

The API will reply with different HTTP statuscodes:

| StatusCode    | Description
| ---      | ---
| 200 OK     | The requests was processed and you receive data as a result.
| 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation.
| 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation.
| 204 NOCONTENT    | The request has been processed, but no details can be returned.
| 400 BADREQUEST   | Your request is malformed.
| 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation.
| 403 FORBIDDEN    | Access to the resource or operation is not allowed.
| 404 NOTFOUND    | The resource cannot be found.
| 410 GONE                  | The resource is permanently no longer available.
| 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details.
| 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.

In the event of a problem, the body of the response will usually contain an errorcode and errormessage.
In rare cases additional details about the error are reported.

Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request.
We will not take any action besides monitoring. 

Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.

## Formatting

Snake casing is applied on resources and query parameters.
The API is strictly returning JSON. No other formats are supported.

Datetimes are returned in ISO-8601 format.

## Pagination

Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.  
**Skip** indicates the number of results to skip and where to start the new take.  
**Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.

Paged results will have headers with useful information regarding the paging.

| Header    | Description
| ---     | ---
| X-Paging-Skipped  | The number of results that have been skipped.
| X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response.
| X-Paging-TotalResults | The total number of results regardless of paging.

## Rate limiting

The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.

| Header    | Description
| ---     | ---
| X-RateLimit-Limit  | The number of requests that can be made in a specific time interval.
| X-RateLimit-Usage  | The number of requests already made in the current time interval.
| X-RateLimit-Remaining | The number of requests remaining until the reset.
| X-RateLimit-Reset  | The number of seconds until the reset.<br />After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header.
| Retry-After   | The number of seconds you have to wait until you can make new requests.<br />This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.

When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase '*Too many requests, retry later.*'.

# Authentication

The Api uses HMAC authentication.  
Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.  
Both the integrity and the authenticity of the message are verified this way.

## Steps to generate the HMAC

1. Get your api key and secret from your controlpanel.  
It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.  
In case your secret is compromised, you can generate a new api key and secret on your controlpanel.
2. Construct the input value for generating the hmac.  
Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.

|          | Description
| ---         | ---
| apikey        | The key that is linked to your user.
| request method      | lowercased (eg: get, post, delete,...)
| path and querystring information  | urlencoding of the lowercased relative path and querystring.<br />The path **MUST start with the api version (/v2)**.<br />The hexadecimal codes (percent encoding) MUST be uppercased.
| unix timestamp      | the unix timestamp in **seconds**.
| nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request.
| content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.<br />An empty body should not be encoded.

3. Hash the concatenated string using your api secret and the SHA-256 algorithm.
4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.

## Sending an authorized request

An authorized request can be made by sending the generated HMAC in the authorization header.  
A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.

Create the authorization parameter by concatenating:
  * apikey
  * colon ':'
  * generated HMAC signature (see above)
  * colon ':'
  * nonce (the one used to generate the signature)
  * colon ':'
  * unix timestamp (the one used to generate the signature)

A sample (illustrated):

* The first line is the string you create to feed to the hashing algorithm.
* The second line is the authorization header that should be sent in the request.

![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \"authorization header illustrated\")

## IP whitelisting

Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.

# Versioning

Because of breaking contract changes compared to v1, we released v2 of the API.  
V1 will still be available, but you are strongly encouraged to migrate to the latest version.  
New features will only be available on v2.

# Policy

### Fair use policy

Please respect the rate limits and do not use the api for any purposes of abuse.  
All requests are being monitored and logged.  
Intentional abuse might result in api key revocation.

# Errors

The API attempts to return appropriate HTTP status codes for every request.  
When the status code indicates failure, the API will also provide an error message in most cases.

An error message contains a machine-parseable error code accompanied by a descriptive error text.  
The text for an error message might change over time, but codes will stay the same.

[An overview of error codes can be found here](/v2/documentation/errorcodes).

# Change log

[An overview of new changes can be found here](/v2/documentation/changelog).

# Provisioning information

## Terminology

| Term   | Definition                |
| ---   | ---                  |
| Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.<br/>It also limits the size of individual assets within the same account. |
| Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. |
| Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...<br/>Some assets are created at the moment when the account is created. Other assets can be created afterwards.
 
## Common provisioning scenario

**Provisioning of an account with Linux hosting with one MySql database**

*Without a pre-existing account:*

1. Create a new account.<br/>Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name).
2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job).
3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/>
When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/>
This will usually hold only one link, but to be futureproof, this has been designed to return a collection.
4. The created resource will point to an account. You now know the account's Id and can continue with the provisioning of a MySql database on this account.
5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information.
6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job).
7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/>
When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/>
This will usually hold only one link, but to be futureproof, this has been designed to return a collection.
8. The created resource will point to a MySql database resource.

## SSL certificate requests

**Requesting an SSL certificate causes the purchase of a paying product.**

1. A certificate is created by adding an ssl certificate request.
2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header.
3. The resource request can respond with different statuscodes:
<ul>
    <li>200: the certificate request is ongoing.<br/>
Check the validations collection for validation values that are not auto_validated. Those should be set by you system.<br/>
Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.</li>
    <li>303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.</li>
    <li>410: the certificate request does not exist anymore, there is no certificate created as a result of the request.</li>
</ul>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: v2
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install public_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your public_api from, and run:

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
var PublicApi = require('public_api');


var api = new PublicApi.AccountsApi()
var opts = {
  'createAccount': new PublicApi.CreateAccount() // {CreateAccount} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.createAccount(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to */v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PublicApi.AccountsApi* | [**createAccount**](docs/AccountsApi.md#createAccount) | **POST** /accounts | Create a new account
*PublicApi.AccountsApi* | [**getAccount**](docs/AccountsApi.md#getAccount) | **GET** /accounts/{accountId} | Get a specific account
*PublicApi.AccountsApi* | [**getAccounts**](docs/AccountsApi.md#getAccounts) | **GET** /accounts | Overview of accounts
*PublicApi.DNSRecordsApi* | [**dnsDomainNameRecordsGet**](docs/DNSRecordsApi.md#dnsDomainNameRecordsGet) | **GET** /dns/{domainName}/records | Get records
*PublicApi.DNSRecordsApi* | [**dnsDomainNameRecordsPost**](docs/DNSRecordsApi.md#dnsDomainNameRecordsPost) | **POST** /dns/{domainName}/records | Create a record
*PublicApi.DNSRecordsApi* | [**dnsDomainNameRecordsRecordIdDelete**](docs/DNSRecordsApi.md#dnsDomainNameRecordsRecordIdDelete) | **DELETE** /dns/{domainName}/records/{recordId} | Delete a record
*PublicApi.DNSRecordsApi* | [**dnsDomainNameRecordsRecordIdGet**](docs/DNSRecordsApi.md#dnsDomainNameRecordsRecordIdGet) | **GET** /dns/{domainName}/records/{recordId} | Get specific record
*PublicApi.DNSRecordsApi* | [**dnsDomainNameRecordsRecordIdPut**](docs/DNSRecordsApi.md#dnsDomainNameRecordsRecordIdPut) | **PUT** /dns/{domainName}/records/{recordId} | Edit a record
*PublicApi.DomainsApi* | [**configureDomain**](docs/DomainsApi.md#configureDomain) | **PUT** /domains/{domainName}/renew | Edit domain name renew state
*PublicApi.DomainsApi* | [**editNameServers**](docs/DomainsApi.md#editNameServers) | **PUT** /domains/{domainName}/nameservers | Edit domain name servers
*PublicApi.DomainsApi* | [**getDomain**](docs/DomainsApi.md#getDomain) | **GET** /domains/{domainName} | Details of a domain
*PublicApi.DomainsApi* | [**getDomains**](docs/DomainsApi.md#getDomains) | **GET** /domains | Overviews of domains
*PublicApi.DomainsApi* | [**register**](docs/DomainsApi.md#register) | **POST** /domains/registrations | Register a domain
*PublicApi.DomainsApi* | [**transfer**](docs/DomainsApi.md#transfer) | **POST** /domains/transfers | Transfer a domain
*PublicApi.LinuxHostingsApi* | [**addScheduledTasks**](docs/LinuxHostingsApi.md#addScheduledTasks) | **POST** /linuxhostings/{domainName}/scheduledtasks | Add a scheduled task
*PublicApi.LinuxHostingsApi* | [**addSshKey**](docs/LinuxHostingsApi.md#addSshKey) | **POST** /linuxhostings/{domainName}/ssh/keys | Add a SSH key
*PublicApi.LinuxHostingsApi* | [**changeApcu**](docs/LinuxHostingsApi.md#changeApcu) | **PUT** /linuxhostings/{domainName}/phpsettings/apcu | Configure PHP APCu setting
*PublicApi.LinuxHostingsApi* | [**changeAutoRedirect**](docs/LinuxHostingsApi.md#changeAutoRedirect) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/autoredirect | Configure auto redirect
*PublicApi.LinuxHostingsApi* | [**changeGzipCompression**](docs/LinuxHostingsApi.md#changeGzipCompression) | **PUT** /linuxhostings/{domainName}/settings/gzipcompression | Enable/disable GZIP compression
*PublicApi.LinuxHostingsApi* | [**changeLetsEncrypt**](docs/LinuxHostingsApi.md#changeLetsEncrypt) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/letsencrypt | Configure let&#39;s encrypt
*PublicApi.LinuxHostingsApi* | [**changePhpMemoryLimit**](docs/LinuxHostingsApi.md#changePhpMemoryLimit) | **PUT** /linuxhostings/{domainName}/phpsettings/memorylimit | Configure PHP memory limit
*PublicApi.LinuxHostingsApi* | [**changePhpVersion**](docs/LinuxHostingsApi.md#changePhpVersion) | **PUT** /linuxhostings/{domainName}/phpsettings/version | Change the Linux hosting PHP version.
*PublicApi.LinuxHostingsApi* | [**configureFtp**](docs/LinuxHostingsApi.md#configureFtp) | **PUT** /linuxhostings/{domainName}/ftp/configuration | Configure FTP
*PublicApi.LinuxHostingsApi* | [**configureHttp2**](docs/LinuxHostingsApi.md#configureHttp2) | **PUT** /linuxhostings/{domainName}/sites/{siteName}/http2/configuration | Configure HTTP/2
*PublicApi.LinuxHostingsApi* | [**configureScheduledTask**](docs/LinuxHostingsApi.md#configureScheduledTask) | **PUT** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Configure a scheduled task
*PublicApi.LinuxHostingsApi* | [**configureSsh**](docs/LinuxHostingsApi.md#configureSsh) | **PUT** /linuxhostings/{domainName}/ssh/configuration | Configure SSH
*PublicApi.LinuxHostingsApi* | [**createHostHeader**](docs/LinuxHostingsApi.md#createHostHeader) | **POST** /linuxhostings/{domainName}/sites/{siteName}/hostheaders | Create a host header
*PublicApi.LinuxHostingsApi* | [**createSubsite**](docs/LinuxHostingsApi.md#createSubsite) | **POST** /linuxhostings/{domainName}/subsites | Create a subsite
*PublicApi.LinuxHostingsApi* | [**deleteScheduledTask**](docs/LinuxHostingsApi.md#deleteScheduledTask) | **DELETE** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Delete a scheduled task
*PublicApi.LinuxHostingsApi* | [**deleteSshKey**](docs/LinuxHostingsApi.md#deleteSshKey) | **DELETE** /linuxhostings/{domainName}/ssh/keys/{fingerprint} | Delete a SSH key
*PublicApi.LinuxHostingsApi* | [**deleteSubsite**](docs/LinuxHostingsApi.md#deleteSubsite) | **DELETE** /linuxhostings/{domainName}/subsites/{siteName} | Delete a subsite
*PublicApi.LinuxHostingsApi* | [**getAvailablePhpVersions**](docs/LinuxHostingsApi.md#getAvailablePhpVersions) | **GET** /linuxhostings/{domainName}/phpsettings/availableversions | Get the available PHP versions.
*PublicApi.LinuxHostingsApi* | [**getLinuxHosting**](docs/LinuxHostingsApi.md#getLinuxHosting) | **GET** /linuxhostings/{domainName} | Linux hosting detail
*PublicApi.LinuxHostingsApi* | [**getLinuxHostings**](docs/LinuxHostingsApi.md#getLinuxHostings) | **GET** /linuxhostings | Overview of linux hostings
*PublicApi.LinuxHostingsApi* | [**getScheduledTask**](docs/LinuxHostingsApi.md#getScheduledTask) | **GET** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Get scheduled task detail
*PublicApi.LinuxHostingsApi* | [**getScheduledTasks**](docs/LinuxHostingsApi.md#getScheduledTasks) | **GET** /linuxhostings/{domainName}/scheduledtasks | Overview of scheduled tasks
*PublicApi.LinuxHostingsApi* | [**getSshKeys**](docs/LinuxHostingsApi.md#getSshKeys) | **GET** /linuxhostings/{domainName}/ssh/keys | Overview of SSH keys
*PublicApi.MailZonesApi* | [**configureAlias**](docs/MailZonesApi.md#configureAlias) | **PUT** /mailzones/{domainName}/aliases/{emailAddress} | Configure a alias
*PublicApi.MailZonesApi* | [**configureAntiSpam**](docs/MailZonesApi.md#configureAntiSpam) | **PUT** /mailzones/{domainName}/antispam | Configure anti-spam for mail zone
*PublicApi.MailZonesApi* | [**configureSmtpDomain**](docs/MailZonesApi.md#configureSmtpDomain) | **PUT** /mailzones/{domainName}/smtpdomains/{hostname} | Configure an extra smtp domain
*PublicApi.MailZonesApi* | [**createAlias**](docs/MailZonesApi.md#createAlias) | **POST** /mailzones/{domainName}/aliases | Create a new alias
*PublicApi.MailZonesApi* | [**createCatchAll**](docs/MailZonesApi.md#createCatchAll) | **POST** /mailzones/{domainName}/catchall | Create a catch-all on the mail zone
*PublicApi.MailZonesApi* | [**createSmtpDomain**](docs/MailZonesApi.md#createSmtpDomain) | **POST** /mailzones/{domainName}/smtpdomains | Create an extra smtp domain
*PublicApi.MailZonesApi* | [**deleteAlias**](docs/MailZonesApi.md#deleteAlias) | **DELETE** /mailzones/{domainName}/aliases/{emailAddress} | Delete a alias
*PublicApi.MailZonesApi* | [**deleteCatchAll**](docs/MailZonesApi.md#deleteCatchAll) | **DELETE** /mailzones/{domainName}/catchall/{emailAddress} | Delete a catch-all on the mail zone
*PublicApi.MailZonesApi* | [**deleteSmtpDomain**](docs/MailZonesApi.md#deleteSmtpDomain) | **DELETE** /mailzones/{domainName}/smtpdomains/{hostname} | Delete an extra smtp domain
*PublicApi.MailZonesApi* | [**getMailZone**](docs/MailZonesApi.md#getMailZone) | **GET** /mailzones/{domainName} | Get the mail zone.
*PublicApi.MailboxesApi* | [**changeMailboxPassword**](docs/MailboxesApi.md#changeMailboxPassword) | **PUT** /mailboxes/{mailboxName}/password | Change password for mailbox
*PublicApi.MailboxesApi* | [**configureMailboxAutoForward**](docs/MailboxesApi.md#configureMailboxAutoForward) | **PUT** /mailboxes/{mailboxName}/autoforward | Configure auto-forward for mailbox
*PublicApi.MailboxesApi* | [**configureMailboxAutoReply**](docs/MailboxesApi.md#configureMailboxAutoReply) | **PUT** /mailboxes/{mailboxName}/autoreply | Configure auto-reply for mailbox
*PublicApi.MailboxesApi* | [**createMailbox**](docs/MailboxesApi.md#createMailbox) | **POST** /mailboxes | Create a new mailbox.
*PublicApi.MailboxesApi* | [**deleteMailbox**](docs/MailboxesApi.md#deleteMailbox) | **DELETE** /mailboxes/{mailboxName} | Delete a mailbox
*PublicApi.MailboxesApi* | [**getMailbox**](docs/MailboxesApi.md#getMailbox) | **GET** /mailboxes/{mailboxName} | Get a specific mailbox
*PublicApi.MailboxesApi* | [**getMailboxes**](docs/MailboxesApi.md#getMailboxes) | **GET** /mailboxes | Gets your mailboxes.
*PublicApi.MySqlDatabasesApi* | [**changeDatabaseUserPassword**](docs/MySqlDatabasesApi.md#changeDatabaseUserPassword) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/password | Change password for mysql user
*PublicApi.MySqlDatabasesApi* | [**changeDatabaseUserStatus**](docs/MySqlDatabasesApi.md#changeDatabaseUserStatus) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/status | Enable/disable mysql user
*PublicApi.MySqlDatabasesApi* | [**createMySqlDatabase**](docs/MySqlDatabasesApi.md#createMySqlDatabase) | **POST** /mysqldatabases | Create a new mysql database
*PublicApi.MySqlDatabasesApi* | [**createMySqlUser**](docs/MySqlDatabasesApi.md#createMySqlUser) | **POST** /mysqldatabases/{databaseName}/users | Create a new mysql user
*PublicApi.MySqlDatabasesApi* | [**deleteDatabase**](docs/MySqlDatabasesApi.md#deleteDatabase) | **DELETE** /mysqldatabases/{databaseName} | Delete a mysql database
*PublicApi.MySqlDatabasesApi* | [**deleteDatabaseUser**](docs/MySqlDatabasesApi.md#deleteDatabaseUser) | **DELETE** /mysqldatabases/{databaseName}/users/{userName} | Delete a mysql user
*PublicApi.MySqlDatabasesApi* | [**getDatabaseUsers**](docs/MySqlDatabasesApi.md#getDatabaseUsers) | **GET** /mysqldatabases/{databaseName}/users | Overview of mysql users
*PublicApi.MySqlDatabasesApi* | [**getMySqlDatabase**](docs/MySqlDatabasesApi.md#getMySqlDatabase) | **GET** /mysqldatabases/{databaseName} | Get a specific database
*PublicApi.MySqlDatabasesApi* | [**getMySqlDatabases**](docs/MySqlDatabasesApi.md#getMySqlDatabases) | **GET** /mysqldatabases | Overview of mysql databases
*PublicApi.ProvisioningJobsApi* | [**provisioningjobsJobIdGet**](docs/ProvisioningJobsApi.md#provisioningjobsJobIdGet) | **GET** /provisioningjobs/{jobId} | Detail of a provisioning job
*PublicApi.SSHApi* | [**getAllSshKeys**](docs/SSHApi.md#getAllSshKeys) | **GET** /ssh | Overview of SSH keys
*PublicApi.SSLCertificateRequestsApi* | [**addSslCertificateRequest**](docs/SSLCertificateRequestsApi.md#addSslCertificateRequest) | **POST** /sslcertificaterequests | Add a SSL certificate request
*PublicApi.SSLCertificateRequestsApi* | [**getSslCertificateRequest**](docs/SSLCertificateRequestsApi.md#getSslCertificateRequest) | **GET** /sslcertificaterequests/{id} | Detail of a SSL certificate request
*PublicApi.SSLCertificateRequestsApi* | [**getSslCertificateRequests**](docs/SSLCertificateRequestsApi.md#getSslCertificateRequests) | **GET** /sslcertificaterequests | Overview of SSL certificate requests
*PublicApi.SSLCertificateRequestsApi* | [**verifySslCertificateRequestDomainValidations**](docs/SSLCertificateRequestsApi.md#verifySslCertificateRequestDomainValidations) | **PUT** /sslcertificaterequests/{id} | Verify the SSL certificate request domain validations
*PublicApi.SSLCertificatesApi* | [**downloadCertificate**](docs/SSLCertificatesApi.md#downloadCertificate) | **GET** /sslcertificates/{sha1Fingerprint}/download | Download a SSL certificate
*PublicApi.SSLCertificatesApi* | [**getSslCertificate**](docs/SSLCertificatesApi.md#getSslCertificate) | **GET** /sslcertificates/{sha1Fingerprint} | Detail of a SSL certificate
*PublicApi.SSLCertificatesApi* | [**getSslCertificates**](docs/SSLCertificatesApi.md#getSslCertificates) | **GET** /sslcertificates | Overview of SSL certificates
*PublicApi.ServicepacksApi* | [**servicepacks**](docs/ServicepacksApi.md#servicepacks) | **GET** /servicepacks | Overview of service packs
*PublicApi.WindowsHostingsApi* | [**getWindowsHosting**](docs/WindowsHostingsApi.md#getWindowsHosting) | **GET** /windowshostings/{domainName} | Windows hosting detail
*PublicApi.WindowsHostingsApi* | [**getWindowsHostings**](docs/WindowsHostingsApi.md#getWindowsHostings) | **GET** /windowshostings | Overview of windows hostings


## Documentation for Models

 - [PublicApi.Account](docs/Account.md)
 - [PublicApi.AccountDetail](docs/AccountDetail.md)
 - [PublicApi.AddHostHeaderRequest](docs/AddHostHeaderRequest.md)
 - [PublicApi.AddSshKeyRequest](docs/AddSshKeyRequest.md)
 - [PublicApi.AddSubsiteRequest](docs/AddSubsiteRequest.md)
 - [PublicApi.AdditionalValidationAttribute](docs/AdditionalValidationAttribute.md)
 - [PublicApi.Addon](docs/Addon.md)
 - [PublicApi.Alias](docs/Alias.md)
 - [PublicApi.AntiSpam](docs/AntiSpam.md)
 - [PublicApi.AntiSpamTypes](docs/AntiSpamTypes.md)
 - [PublicApi.ApplicationPool](docs/ApplicationPool.md)
 - [PublicApi.AssetType](docs/AssetType.md)
 - [PublicApi.AutoForward](docs/AutoForward.md)
 - [PublicApi.AutoRedirectConfig](docs/AutoRedirectConfig.md)
 - [PublicApi.AutoReply](docs/AutoReply.md)
 - [PublicApi.BadRequestResponse](docs/BadRequestResponse.md)
 - [PublicApi.CatchAll](docs/CatchAll.md)
 - [PublicApi.CompletionEstimation](docs/CompletionEstimation.md)
 - [PublicApi.CreateAccount](docs/CreateAccount.md)
 - [PublicApi.CreateAliasRequest](docs/CreateAliasRequest.md)
 - [PublicApi.CreateCatchAllRequest](docs/CreateCatchAllRequest.md)
 - [PublicApi.CreateMailboxRequest](docs/CreateMailboxRequest.md)
 - [PublicApi.CreateMySqlDatabase](docs/CreateMySqlDatabase.md)
 - [PublicApi.CreateMySqlUser](docs/CreateMySqlUser.md)
 - [PublicApi.CreateSmtpDomainRequest](docs/CreateSmtpDomainRequest.md)
 - [PublicApi.CreateSslCertificateRequest](docs/CreateSslCertificateRequest.md)
 - [PublicApi.DnsRecord](docs/DnsRecord.md)
 - [PublicApi.Domain](docs/Domain.md)
 - [PublicApi.DomainDetail](docs/DomainDetail.md)
 - [PublicApi.EditDomainWillRenewRequest](docs/EditDomainWillRenewRequest.md)
 - [PublicApi.EditNameServers](docs/EditNameServers.md)
 - [PublicApi.ExtraField](docs/ExtraField.md)
 - [PublicApi.FtpConfiguration](docs/FtpConfiguration.md)
 - [PublicApi.GzipConfig](docs/GzipConfig.md)
 - [PublicApi.HostHeader](docs/HostHeader.md)
 - [PublicApi.Http2Configuration](docs/Http2Configuration.md)
 - [PublicApi.LetsEncryptConfig](docs/LetsEncryptConfig.md)
 - [PublicApi.LinuxHosting](docs/LinuxHosting.md)
 - [PublicApi.LinuxHostingDetail](docs/LinuxHostingDetail.md)
 - [PublicApi.LinuxIpType](docs/LinuxIpType.md)
 - [PublicApi.LinuxSite](docs/LinuxSite.md)
 - [PublicApi.MailZone](docs/MailZone.md)
 - [PublicApi.MailZoneAccount](docs/MailZoneAccount.md)
 - [PublicApi.Mailbox](docs/Mailbox.md)
 - [PublicApi.MailboxDetail](docs/MailboxDetail.md)
 - [PublicApi.MySqlDatabase](docs/MySqlDatabase.md)
 - [PublicApi.MySqlUser](docs/MySqlUser.md)
 - [PublicApi.NameServer](docs/NameServer.md)
 - [PublicApi.PhpVersion](docs/PhpVersion.md)
 - [PublicApi.ProvisioningJobCompletion](docs/ProvisioningJobCompletion.md)
 - [PublicApi.ProvisioningJobInfo](docs/ProvisioningJobInfo.md)
 - [PublicApi.ProvisioningJobStatus](docs/ProvisioningJobStatus.md)
 - [PublicApi.RegisterDomain](docs/RegisterDomain.md)
 - [PublicApi.Registrant](docs/Registrant.md)
 - [PublicApi.RegistrantInput](docs/RegistrantInput.md)
 - [PublicApi.ScheduledTask](docs/ScheduledTask.md)
 - [PublicApi.Servicepack](docs/Servicepack.md)
 - [PublicApi.SiteBinding](docs/SiteBinding.md)
 - [PublicApi.SmtpDomain](docs/SmtpDomain.md)
 - [PublicApi.SshConfiguration](docs/SshConfiguration.md)
 - [PublicApi.SshKey](docs/SshKey.md)
 - [PublicApi.SshKeyDetail](docs/SshKeyDetail.md)
 - [PublicApi.SslCertificate](docs/SslCertificate.md)
 - [PublicApi.SslCertificateDetail](docs/SslCertificateDetail.md)
 - [PublicApi.SslCertificateFileFormat](docs/SslCertificateFileFormat.md)
 - [PublicApi.SslCertificateRequest](docs/SslCertificateRequest.md)
 - [PublicApi.SslCertificateRequestDetail](docs/SslCertificateRequestDetail.md)
 - [PublicApi.SslCertificateRequestValidation](docs/SslCertificateRequestValidation.md)
 - [PublicApi.SslCertificateRequestValidationType](docs/SslCertificateRequestValidationType.md)
 - [PublicApi.SslCertificateType](docs/SslCertificateType.md)
 - [PublicApi.SslCertificateValidationLevel](docs/SslCertificateValidationLevel.md)
 - [PublicApi.SslCertificateVendor](docs/SslCertificateVendor.md)
 - [PublicApi.SslSubjectAltName](docs/SslSubjectAltName.md)
 - [PublicApi.SslSubjectAltNameType](docs/SslSubjectAltNameType.md)
 - [PublicApi.TransferDomain](docs/TransferDomain.md)
 - [PublicApi.UpdateAliasRequest](docs/UpdateAliasRequest.md)
 - [PublicApi.UpdateAntiSpamRequest](docs/UpdateAntiSpamRequest.md)
 - [PublicApi.UpdateMailboxPasswordRequest](docs/UpdateMailboxPasswordRequest.md)
 - [PublicApi.UpdatePhpAPcuRequest](docs/UpdatePhpAPcuRequest.md)
 - [PublicApi.UpdatePhpMemoryLimitRequest](docs/UpdatePhpMemoryLimitRequest.md)
 - [PublicApi.UpdateSmtpDomainRequest](docs/UpdateSmtpDomainRequest.md)
 - [PublicApi.UpdateUserPasswordRequest](docs/UpdateUserPasswordRequest.md)
 - [PublicApi.UpdateUserStatusRequest](docs/UpdateUserStatusRequest.md)
 - [PublicApi.UserRights](docs/UserRights.md)
 - [PublicApi.ValidationErrorMessage](docs/ValidationErrorMessage.md)
 - [PublicApi.WindowsHosting](docs/WindowsHosting.md)
 - [PublicApi.WindowsHostingDetail](docs/WindowsHostingDetail.md)
 - [PublicApi.WindowsIpType](docs/WindowsIpType.md)
 - [PublicApi.WindowsSite](docs/WindowsSite.md)


## Documentation for Authorization

Endpoints do not require authorization.

