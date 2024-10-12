# openapi-java-client

Public Api
- API version: v2
  - Build date: 2024-10-12T09:58:18.229870-04:00[America/New_York]
  - Generator version: 7.9.0

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


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>v2</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:v2"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-v2.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    CreateAccount createAccount = new CreateAccount(); // CreateAccount | 
    try {
      apiInstance.createAccount(createAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#createAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to */v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**createAccount**](docs/AccountsApi.md#createAccount) | **POST** /accounts | Create a new account
*AccountsApi* | [**getAccount**](docs/AccountsApi.md#getAccount) | **GET** /accounts/{accountId} | Get a specific account
*AccountsApi* | [**getAccounts**](docs/AccountsApi.md#getAccounts) | **GET** /accounts | Overview of accounts
*DnsRecordsApi* | [**dnsDomainNameRecordsGet**](docs/DnsRecordsApi.md#dnsDomainNameRecordsGet) | **GET** /dns/{domainName}/records | Get records
*DnsRecordsApi* | [**dnsDomainNameRecordsPost**](docs/DnsRecordsApi.md#dnsDomainNameRecordsPost) | **POST** /dns/{domainName}/records | Create a record
*DnsRecordsApi* | [**dnsDomainNameRecordsRecordIdDelete**](docs/DnsRecordsApi.md#dnsDomainNameRecordsRecordIdDelete) | **DELETE** /dns/{domainName}/records/{recordId} | Delete a record
*DnsRecordsApi* | [**dnsDomainNameRecordsRecordIdGet**](docs/DnsRecordsApi.md#dnsDomainNameRecordsRecordIdGet) | **GET** /dns/{domainName}/records/{recordId} | Get specific record
*DnsRecordsApi* | [**dnsDomainNameRecordsRecordIdPut**](docs/DnsRecordsApi.md#dnsDomainNameRecordsRecordIdPut) | **PUT** /dns/{domainName}/records/{recordId} | Edit a record
*DomainsApi* | [**configureDomain**](docs/DomainsApi.md#configureDomain) | **PUT** /domains/{domainName}/renew | Edit domain name renew state
*DomainsApi* | [**editNameServers**](docs/DomainsApi.md#editNameServers) | **PUT** /domains/{domainName}/nameservers | Edit domain name servers
*DomainsApi* | [**getDomain**](docs/DomainsApi.md#getDomain) | **GET** /domains/{domainName} | Details of a domain
*DomainsApi* | [**getDomains**](docs/DomainsApi.md#getDomains) | **GET** /domains | Overviews of domains
*DomainsApi* | [**register**](docs/DomainsApi.md#register) | **POST** /domains/registrations | Register a domain
*DomainsApi* | [**transfer**](docs/DomainsApi.md#transfer) | **POST** /domains/transfers | Transfer a domain
*LinuxHostingsApi* | [**addScheduledTasks**](docs/LinuxHostingsApi.md#addScheduledTasks) | **POST** /linuxhostings/{domainName}/scheduledtasks | Add a scheduled task
*LinuxHostingsApi* | [**addSshKey**](docs/LinuxHostingsApi.md#addSshKey) | **POST** /linuxhostings/{domainName}/ssh/keys | Add a SSH key
*LinuxHostingsApi* | [**changeApcu**](docs/LinuxHostingsApi.md#changeApcu) | **PUT** /linuxhostings/{domainName}/phpsettings/apcu | Configure PHP APCu setting
*LinuxHostingsApi* | [**changeAutoRedirect**](docs/LinuxHostingsApi.md#changeAutoRedirect) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/autoredirect | Configure auto redirect
*LinuxHostingsApi* | [**changeGzipCompression**](docs/LinuxHostingsApi.md#changeGzipCompression) | **PUT** /linuxhostings/{domainName}/settings/gzipcompression | Enable/disable GZIP compression
*LinuxHostingsApi* | [**changeLetsEncrypt**](docs/LinuxHostingsApi.md#changeLetsEncrypt) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/letsencrypt | Configure let&#39;s encrypt
*LinuxHostingsApi* | [**changePhpMemoryLimit**](docs/LinuxHostingsApi.md#changePhpMemoryLimit) | **PUT** /linuxhostings/{domainName}/phpsettings/memorylimit | Configure PHP memory limit
*LinuxHostingsApi* | [**changePhpVersion**](docs/LinuxHostingsApi.md#changePhpVersion) | **PUT** /linuxhostings/{domainName}/phpsettings/version | Change the Linux hosting PHP version.
*LinuxHostingsApi* | [**configureFtp**](docs/LinuxHostingsApi.md#configureFtp) | **PUT** /linuxhostings/{domainName}/ftp/configuration | Configure FTP
*LinuxHostingsApi* | [**configureHttp2**](docs/LinuxHostingsApi.md#configureHttp2) | **PUT** /linuxhostings/{domainName}/sites/{siteName}/http2/configuration | Configure HTTP/2
*LinuxHostingsApi* | [**configureScheduledTask**](docs/LinuxHostingsApi.md#configureScheduledTask) | **PUT** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Configure a scheduled task
*LinuxHostingsApi* | [**configureSsh**](docs/LinuxHostingsApi.md#configureSsh) | **PUT** /linuxhostings/{domainName}/ssh/configuration | Configure SSH
*LinuxHostingsApi* | [**createHostHeader**](docs/LinuxHostingsApi.md#createHostHeader) | **POST** /linuxhostings/{domainName}/sites/{siteName}/hostheaders | Create a host header
*LinuxHostingsApi* | [**createSubsite**](docs/LinuxHostingsApi.md#createSubsite) | **POST** /linuxhostings/{domainName}/subsites | Create a subsite
*LinuxHostingsApi* | [**deleteScheduledTask**](docs/LinuxHostingsApi.md#deleteScheduledTask) | **DELETE** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Delete a scheduled task
*LinuxHostingsApi* | [**deleteSshKey**](docs/LinuxHostingsApi.md#deleteSshKey) | **DELETE** /linuxhostings/{domainName}/ssh/keys/{fingerprint} | Delete a SSH key
*LinuxHostingsApi* | [**deleteSubsite**](docs/LinuxHostingsApi.md#deleteSubsite) | **DELETE** /linuxhostings/{domainName}/subsites/{siteName} | Delete a subsite
*LinuxHostingsApi* | [**getAvailablePhpVersions**](docs/LinuxHostingsApi.md#getAvailablePhpVersions) | **GET** /linuxhostings/{domainName}/phpsettings/availableversions | Get the available PHP versions.
*LinuxHostingsApi* | [**getLinuxHosting**](docs/LinuxHostingsApi.md#getLinuxHosting) | **GET** /linuxhostings/{domainName} | Linux hosting detail
*LinuxHostingsApi* | [**getLinuxHostings**](docs/LinuxHostingsApi.md#getLinuxHostings) | **GET** /linuxhostings | Overview of linux hostings
*LinuxHostingsApi* | [**getScheduledTask**](docs/LinuxHostingsApi.md#getScheduledTask) | **GET** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Get scheduled task detail
*LinuxHostingsApi* | [**getScheduledTasks**](docs/LinuxHostingsApi.md#getScheduledTasks) | **GET** /linuxhostings/{domainName}/scheduledtasks | Overview of scheduled tasks
*LinuxHostingsApi* | [**getSshKeys**](docs/LinuxHostingsApi.md#getSshKeys) | **GET** /linuxhostings/{domainName}/ssh/keys | Overview of SSH keys
*MailZonesApi* | [**configureAlias**](docs/MailZonesApi.md#configureAlias) | **PUT** /mailzones/{domainName}/aliases/{emailAddress} | Configure a alias
*MailZonesApi* | [**configureAntiSpam**](docs/MailZonesApi.md#configureAntiSpam) | **PUT** /mailzones/{domainName}/antispam | Configure anti-spam for mail zone
*MailZonesApi* | [**configureSmtpDomain**](docs/MailZonesApi.md#configureSmtpDomain) | **PUT** /mailzones/{domainName}/smtpdomains/{hostname} | Configure an extra smtp domain
*MailZonesApi* | [**createAlias**](docs/MailZonesApi.md#createAlias) | **POST** /mailzones/{domainName}/aliases | Create a new alias
*MailZonesApi* | [**createCatchAll**](docs/MailZonesApi.md#createCatchAll) | **POST** /mailzones/{domainName}/catchall | Create a catch-all on the mail zone
*MailZonesApi* | [**createSmtpDomain**](docs/MailZonesApi.md#createSmtpDomain) | **POST** /mailzones/{domainName}/smtpdomains | Create an extra smtp domain
*MailZonesApi* | [**deleteAlias**](docs/MailZonesApi.md#deleteAlias) | **DELETE** /mailzones/{domainName}/aliases/{emailAddress} | Delete a alias
*MailZonesApi* | [**deleteCatchAll**](docs/MailZonesApi.md#deleteCatchAll) | **DELETE** /mailzones/{domainName}/catchall/{emailAddress} | Delete a catch-all on the mail zone
*MailZonesApi* | [**deleteSmtpDomain**](docs/MailZonesApi.md#deleteSmtpDomain) | **DELETE** /mailzones/{domainName}/smtpdomains/{hostname} | Delete an extra smtp domain
*MailZonesApi* | [**getMailZone**](docs/MailZonesApi.md#getMailZone) | **GET** /mailzones/{domainName} | Get the mail zone.
*MailboxesApi* | [**changeMailboxPassword**](docs/MailboxesApi.md#changeMailboxPassword) | **PUT** /mailboxes/{mailboxName}/password | Change password for mailbox
*MailboxesApi* | [**configureMailboxAutoForward**](docs/MailboxesApi.md#configureMailboxAutoForward) | **PUT** /mailboxes/{mailboxName}/autoforward | Configure auto-forward for mailbox
*MailboxesApi* | [**configureMailboxAutoReply**](docs/MailboxesApi.md#configureMailboxAutoReply) | **PUT** /mailboxes/{mailboxName}/autoreply | Configure auto-reply for mailbox
*MailboxesApi* | [**createMailbox**](docs/MailboxesApi.md#createMailbox) | **POST** /mailboxes | Create a new mailbox.
*MailboxesApi* | [**deleteMailbox**](docs/MailboxesApi.md#deleteMailbox) | **DELETE** /mailboxes/{mailboxName} | Delete a mailbox
*MailboxesApi* | [**getMailbox**](docs/MailboxesApi.md#getMailbox) | **GET** /mailboxes/{mailboxName} | Get a specific mailbox
*MailboxesApi* | [**getMailboxes**](docs/MailboxesApi.md#getMailboxes) | **GET** /mailboxes | Gets your mailboxes.
*MySqlDatabasesApi* | [**changeDatabaseUserPassword**](docs/MySqlDatabasesApi.md#changeDatabaseUserPassword) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/password | Change password for mysql user
*MySqlDatabasesApi* | [**changeDatabaseUserStatus**](docs/MySqlDatabasesApi.md#changeDatabaseUserStatus) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/status | Enable/disable mysql user
*MySqlDatabasesApi* | [**createMySqlDatabase**](docs/MySqlDatabasesApi.md#createMySqlDatabase) | **POST** /mysqldatabases | Create a new mysql database
*MySqlDatabasesApi* | [**createMySqlUser**](docs/MySqlDatabasesApi.md#createMySqlUser) | **POST** /mysqldatabases/{databaseName}/users | Create a new mysql user
*MySqlDatabasesApi* | [**deleteDatabase**](docs/MySqlDatabasesApi.md#deleteDatabase) | **DELETE** /mysqldatabases/{databaseName} | Delete a mysql database
*MySqlDatabasesApi* | [**deleteDatabaseUser**](docs/MySqlDatabasesApi.md#deleteDatabaseUser) | **DELETE** /mysqldatabases/{databaseName}/users/{userName} | Delete a mysql user
*MySqlDatabasesApi* | [**getDatabaseUsers**](docs/MySqlDatabasesApi.md#getDatabaseUsers) | **GET** /mysqldatabases/{databaseName}/users | Overview of mysql users
*MySqlDatabasesApi* | [**getMySqlDatabase**](docs/MySqlDatabasesApi.md#getMySqlDatabase) | **GET** /mysqldatabases/{databaseName} | Get a specific database
*MySqlDatabasesApi* | [**getMySqlDatabases**](docs/MySqlDatabasesApi.md#getMySqlDatabases) | **GET** /mysqldatabases | Overview of mysql databases
*ProvisioningJobsApi* | [**provisioningjobsJobIdGet**](docs/ProvisioningJobsApi.md#provisioningjobsJobIdGet) | **GET** /provisioningjobs/{jobId} | Detail of a provisioning job
*ServicepacksApi* | [**servicepacks**](docs/ServicepacksApi.md#servicepacks) | **GET** /servicepacks | Overview of service packs
*SshApi* | [**getAllSshKeys**](docs/SshApi.md#getAllSshKeys) | **GET** /ssh | Overview of SSH keys
*SslCertificateRequestsApi* | [**addSslCertificateRequest**](docs/SslCertificateRequestsApi.md#addSslCertificateRequest) | **POST** /sslcertificaterequests | Add a SSL certificate request
*SslCertificateRequestsApi* | [**getSslCertificateRequest**](docs/SslCertificateRequestsApi.md#getSslCertificateRequest) | **GET** /sslcertificaterequests/{id} | Detail of a SSL certificate request
*SslCertificateRequestsApi* | [**getSslCertificateRequests**](docs/SslCertificateRequestsApi.md#getSslCertificateRequests) | **GET** /sslcertificaterequests | Overview of SSL certificate requests
*SslCertificateRequestsApi* | [**verifySslCertificateRequestDomainValidations**](docs/SslCertificateRequestsApi.md#verifySslCertificateRequestDomainValidations) | **PUT** /sslcertificaterequests/{id} | Verify the SSL certificate request domain validations
*SslCertificatesApi* | [**downloadCertificate**](docs/SslCertificatesApi.md#downloadCertificate) | **GET** /sslcertificates/{sha1Fingerprint}/download | Download a SSL certificate
*SslCertificatesApi* | [**getSslCertificate**](docs/SslCertificatesApi.md#getSslCertificate) | **GET** /sslcertificates/{sha1Fingerprint} | Detail of a SSL certificate
*SslCertificatesApi* | [**getSslCertificates**](docs/SslCertificatesApi.md#getSslCertificates) | **GET** /sslcertificates | Overview of SSL certificates
*WindowsHostingsApi* | [**getWindowsHosting**](docs/WindowsHostingsApi.md#getWindowsHosting) | **GET** /windowshostings/{domainName} | Windows hosting detail
*WindowsHostingsApi* | [**getWindowsHostings**](docs/WindowsHostingsApi.md#getWindowsHostings) | **GET** /windowshostings | Overview of windows hostings


## Documentation for Models

 - [Account](docs/Account.md)
 - [AccountDetail](docs/AccountDetail.md)
 - [AddHostHeaderRequest](docs/AddHostHeaderRequest.md)
 - [AddSshKeyRequest](docs/AddSshKeyRequest.md)
 - [AddSubsiteRequest](docs/AddSubsiteRequest.md)
 - [AdditionalValidationAttribute](docs/AdditionalValidationAttribute.md)
 - [Addon](docs/Addon.md)
 - [Alias](docs/Alias.md)
 - [AntiSpam](docs/AntiSpam.md)
 - [AntiSpamTypes](docs/AntiSpamTypes.md)
 - [ApplicationPool](docs/ApplicationPool.md)
 - [AssetType](docs/AssetType.md)
 - [AutoForward](docs/AutoForward.md)
 - [AutoRedirectConfig](docs/AutoRedirectConfig.md)
 - [AutoReply](docs/AutoReply.md)
 - [BadRequestResponse](docs/BadRequestResponse.md)
 - [CatchAll](docs/CatchAll.md)
 - [CompletionEstimation](docs/CompletionEstimation.md)
 - [CreateAccount](docs/CreateAccount.md)
 - [CreateAliasRequest](docs/CreateAliasRequest.md)
 - [CreateCatchAllRequest](docs/CreateCatchAllRequest.md)
 - [CreateMailboxRequest](docs/CreateMailboxRequest.md)
 - [CreateMySqlDatabase](docs/CreateMySqlDatabase.md)
 - [CreateMySqlUser](docs/CreateMySqlUser.md)
 - [CreateSmtpDomainRequest](docs/CreateSmtpDomainRequest.md)
 - [CreateSslCertificateRequest](docs/CreateSslCertificateRequest.md)
 - [DnsRecord](docs/DnsRecord.md)
 - [Domain](docs/Domain.md)
 - [DomainDetail](docs/DomainDetail.md)
 - [EditDomainWillRenewRequest](docs/EditDomainWillRenewRequest.md)
 - [EditNameServers](docs/EditNameServers.md)
 - [ExtraField](docs/ExtraField.md)
 - [FtpConfiguration](docs/FtpConfiguration.md)
 - [GzipConfig](docs/GzipConfig.md)
 - [HostHeader](docs/HostHeader.md)
 - [Http2Configuration](docs/Http2Configuration.md)
 - [LetsEncryptConfig](docs/LetsEncryptConfig.md)
 - [LinuxHosting](docs/LinuxHosting.md)
 - [LinuxHostingDetail](docs/LinuxHostingDetail.md)
 - [LinuxIpType](docs/LinuxIpType.md)
 - [LinuxSite](docs/LinuxSite.md)
 - [MailZone](docs/MailZone.md)
 - [MailZoneAccount](docs/MailZoneAccount.md)
 - [Mailbox](docs/Mailbox.md)
 - [MailboxDetail](docs/MailboxDetail.md)
 - [MySqlDatabase](docs/MySqlDatabase.md)
 - [MySqlUser](docs/MySqlUser.md)
 - [NameServer](docs/NameServer.md)
 - [PhpVersion](docs/PhpVersion.md)
 - [ProvisioningJobCompletion](docs/ProvisioningJobCompletion.md)
 - [ProvisioningJobInfo](docs/ProvisioningJobInfo.md)
 - [ProvisioningJobStatus](docs/ProvisioningJobStatus.md)
 - [RegisterDomain](docs/RegisterDomain.md)
 - [Registrant](docs/Registrant.md)
 - [RegistrantInput](docs/RegistrantInput.md)
 - [ScheduledTask](docs/ScheduledTask.md)
 - [Servicepack](docs/Servicepack.md)
 - [SiteBinding](docs/SiteBinding.md)
 - [SmtpDomain](docs/SmtpDomain.md)
 - [SshConfiguration](docs/SshConfiguration.md)
 - [SshKey](docs/SshKey.md)
 - [SshKeyDetail](docs/SshKeyDetail.md)
 - [SslCertificate](docs/SslCertificate.md)
 - [SslCertificateDetail](docs/SslCertificateDetail.md)
 - [SslCertificateFileFormat](docs/SslCertificateFileFormat.md)
 - [SslCertificateRequest](docs/SslCertificateRequest.md)
 - [SslCertificateRequestDetail](docs/SslCertificateRequestDetail.md)
 - [SslCertificateRequestValidation](docs/SslCertificateRequestValidation.md)
 - [SslCertificateRequestValidationType](docs/SslCertificateRequestValidationType.md)
 - [SslCertificateType](docs/SslCertificateType.md)
 - [SslCertificateValidationLevel](docs/SslCertificateValidationLevel.md)
 - [SslCertificateVendor](docs/SslCertificateVendor.md)
 - [SslSubjectAltName](docs/SslSubjectAltName.md)
 - [SslSubjectAltNameType](docs/SslSubjectAltNameType.md)
 - [TransferDomain](docs/TransferDomain.md)
 - [UpdateAliasRequest](docs/UpdateAliasRequest.md)
 - [UpdateAntiSpamRequest](docs/UpdateAntiSpamRequest.md)
 - [UpdateMailboxPasswordRequest](docs/UpdateMailboxPasswordRequest.md)
 - [UpdatePhpAPcuRequest](docs/UpdatePhpAPcuRequest.md)
 - [UpdatePhpMemoryLimitRequest](docs/UpdatePhpMemoryLimitRequest.md)
 - [UpdateSmtpDomainRequest](docs/UpdateSmtpDomainRequest.md)
 - [UpdateUserPasswordRequest](docs/UpdateUserPasswordRequest.md)
 - [UpdateUserStatusRequest](docs/UpdateUserStatusRequest.md)
 - [UserRights](docs/UserRights.md)
 - [ValidationErrorMessage](docs/ValidationErrorMessage.md)
 - [WindowsHosting](docs/WindowsHosting.md)
 - [WindowsHostingDetail](docs/WindowsHostingDetail.md)
 - [WindowsIpType](docs/WindowsIpType.md)
 - [WindowsSite](docs/WindowsSite.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



