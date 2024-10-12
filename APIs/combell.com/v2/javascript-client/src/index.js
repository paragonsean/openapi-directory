/**
 * Public Api
 * # Introduction  This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.  # Conventions  ## Requests  The API supports different methods depending on the required action.  | Method | Description | ---  | --- | GET  | Retrieve resources in a collection or get a single resource.<br/>Getters will never have any effect on the queried resources. | POST  | Create a new resource in a collection. | PUT  | Update an existing resource with its new representation. | DELETE | Delete an existing resource.  ## HTTP status codes  The API will reply with different HTTP statuscodes:  | StatusCode    | Description | ---      | --- | 200 OK     | The requests was processed and you receive data as a result. | 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation. | 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation. | 204 NOCONTENT    | The request has been processed, but no details can be returned. | 400 BADREQUEST   | Your request is malformed. | 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation. | 403 FORBIDDEN    | Access to the resource or operation is not allowed. | 404 NOTFOUND    | The resource cannot be found. | 410 GONE                  | The resource is permanently no longer available. | 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details. | 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.  In the event of a problem, the body of the response will usually contain an errorcode and errormessage. In rare cases additional details about the error are reported.  Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request. We will not take any action besides monitoring.   Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.  ## Formatting  Snake casing is applied on resources and query parameters. The API is strictly returning JSON. No other formats are supported.  Datetimes are returned in ISO-8601 format.  ## Pagination  Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.   **Skip** indicates the number of results to skip and where to start the new take.   **Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.  Paged results will have headers with useful information regarding the paging.  | Header    | Description | ---     | --- | X-Paging-Skipped  | The number of results that have been skipped. | X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. | X-Paging-TotalResults | The total number of results regardless of paging.  ## Rate limiting  The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.  | Header    | Description | ---     | --- | X-RateLimit-Limit  | The number of requests that can be made in a specific time interval. | X-RateLimit-Usage  | The number of requests already made in the current time interval. | X-RateLimit-Remaining | The number of requests remaining until the reset. | X-RateLimit-Reset  | The number of seconds until the reset.<br />After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header. | Retry-After   | The number of seconds you have to wait until you can make new requests.<br />This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.  When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase '*Too many requests, retry later.*'.  # Authentication  The Api uses HMAC authentication.   Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.   Both the integrity and the authenticity of the message are verified this way.  ## Steps to generate the HMAC  1. Get your api key and secret from your controlpanel.   It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.   In case your secret is compromised, you can generate a new api key and secret on your controlpanel. 2. Construct the input value for generating the hmac.   Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.  |          | Description | ---         | --- | apikey        | The key that is linked to your user. | request method      | lowercased (eg: get, post, delete,...) | path and querystring information  | urlencoding of the lowercased relative path and querystring.<br />The path **MUST start with the api version (/v2)**.<br />The hexadecimal codes (percent encoding) MUST be uppercased. | unix timestamp      | the unix timestamp in **seconds**. | nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request. | content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.<br />An empty body should not be encoded.  3. Hash the concatenated string using your api secret and the SHA-256 algorithm. 4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.  ## Sending an authorized request  An authorized request can be made by sending the generated HMAC in the authorization header.   A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.  Create the authorization parameter by concatenating:   * apikey   * colon ':'   * generated HMAC signature (see above)   * colon ':'   * nonce (the one used to generate the signature)   * colon ':'   * unix timestamp (the one used to generate the signature)  A sample (illustrated):  * The first line is the string you create to feed to the hashing algorithm. * The second line is the authorization header that should be sent in the request.  ![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \"authorization header illustrated\")  ## IP whitelisting  Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.  # Versioning  Because of breaking contract changes compared to v1, we released v2 of the API.   V1 will still be available, but you are strongly encouraged to migrate to the latest version.   New features will only be available on v2.  # Policy  ### Fair use policy  Please respect the rate limits and do not use the api for any purposes of abuse.   All requests are being monitored and logged.   Intentional abuse might result in api key revocation.  # Errors  The API attempts to return appropriate HTTP status codes for every request.   When the status code indicates failure, the API will also provide an error message in most cases.  An error message contains a machine-parseable error code accompanied by a descriptive error text.   The text for an error message might change over time, but codes will stay the same.  [An overview of error codes can be found here](/v2/documentation/errorcodes).  # Change log  [An overview of new changes can be found here](/v2/documentation/changelog).  # Provisioning information  ## Terminology  | Term   | Definition                | | ---   | ---                  | | Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.<br/>It also limits the size of individual assets within the same account. | | Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. | | Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...<br/>Some assets are created at the moment when the account is created. Other assets can be created afterwards.   ## Common provisioning scenario  **Provisioning of an account with Linux hosting with one MySql database**  *Without a pre-existing account:*  1. Create a new account.<br/>Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name). 2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 4. The created resource will point to an account. You now know the account's Id and can continue with the provisioning of a MySql database on this account. 5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information. 6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 8. The created resource will point to a MySql database resource.  ## SSL certificate requests  **Requesting an SSL certificate causes the purchase of a paying product.**  1. A certificate is created by adding an ssl certificate request. 2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header. 3. The resource request can respond with different statuscodes: <ul>     <li>200: the certificate request is ongoing.<br/> Check the validations collection for validation values that are not auto_validated. Those should be set by you system.<br/> Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.</li>     <li>303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.</li>     <li>410: the certificate request does not exist anymore, there is no certificate created as a result of the request.</li> </ul>
 *
 * The version of the OpenAPI document: v2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Account from './model/Account';
import AccountDetail from './model/AccountDetail';
import AddHostHeaderRequest from './model/AddHostHeaderRequest';
import AddSshKeyRequest from './model/AddSshKeyRequest';
import AddSubsiteRequest from './model/AddSubsiteRequest';
import AdditionalValidationAttribute from './model/AdditionalValidationAttribute';
import Addon from './model/Addon';
import Alias from './model/Alias';
import AntiSpam from './model/AntiSpam';
import AntiSpamTypes from './model/AntiSpamTypes';
import ApplicationPool from './model/ApplicationPool';
import AssetType from './model/AssetType';
import AutoForward from './model/AutoForward';
import AutoRedirectConfig from './model/AutoRedirectConfig';
import AutoReply from './model/AutoReply';
import BadRequestResponse from './model/BadRequestResponse';
import CatchAll from './model/CatchAll';
import CompletionEstimation from './model/CompletionEstimation';
import CreateAccount from './model/CreateAccount';
import CreateAliasRequest from './model/CreateAliasRequest';
import CreateCatchAllRequest from './model/CreateCatchAllRequest';
import CreateMailboxRequest from './model/CreateMailboxRequest';
import CreateMySqlDatabase from './model/CreateMySqlDatabase';
import CreateMySqlUser from './model/CreateMySqlUser';
import CreateSmtpDomainRequest from './model/CreateSmtpDomainRequest';
import CreateSslCertificateRequest from './model/CreateSslCertificateRequest';
import DnsRecord from './model/DnsRecord';
import Domain from './model/Domain';
import DomainDetail from './model/DomainDetail';
import EditDomainWillRenewRequest from './model/EditDomainWillRenewRequest';
import EditNameServers from './model/EditNameServers';
import ExtraField from './model/ExtraField';
import FtpConfiguration from './model/FtpConfiguration';
import GzipConfig from './model/GzipConfig';
import HostHeader from './model/HostHeader';
import Http2Configuration from './model/Http2Configuration';
import LetsEncryptConfig from './model/LetsEncryptConfig';
import LinuxHosting from './model/LinuxHosting';
import LinuxHostingDetail from './model/LinuxHostingDetail';
import LinuxIpType from './model/LinuxIpType';
import LinuxSite from './model/LinuxSite';
import MailZone from './model/MailZone';
import MailZoneAccount from './model/MailZoneAccount';
import Mailbox from './model/Mailbox';
import MailboxDetail from './model/MailboxDetail';
import MySqlDatabase from './model/MySqlDatabase';
import MySqlUser from './model/MySqlUser';
import NameServer from './model/NameServer';
import PhpVersion from './model/PhpVersion';
import ProvisioningJobCompletion from './model/ProvisioningJobCompletion';
import ProvisioningJobInfo from './model/ProvisioningJobInfo';
import ProvisioningJobStatus from './model/ProvisioningJobStatus';
import RegisterDomain from './model/RegisterDomain';
import Registrant from './model/Registrant';
import RegistrantInput from './model/RegistrantInput';
import ScheduledTask from './model/ScheduledTask';
import Servicepack from './model/Servicepack';
import SiteBinding from './model/SiteBinding';
import SmtpDomain from './model/SmtpDomain';
import SshConfiguration from './model/SshConfiguration';
import SshKey from './model/SshKey';
import SshKeyDetail from './model/SshKeyDetail';
import SslCertificate from './model/SslCertificate';
import SslCertificateDetail from './model/SslCertificateDetail';
import SslCertificateFileFormat from './model/SslCertificateFileFormat';
import SslCertificateRequest from './model/SslCertificateRequest';
import SslCertificateRequestDetail from './model/SslCertificateRequestDetail';
import SslCertificateRequestValidation from './model/SslCertificateRequestValidation';
import SslCertificateRequestValidationType from './model/SslCertificateRequestValidationType';
import SslCertificateType from './model/SslCertificateType';
import SslCertificateValidationLevel from './model/SslCertificateValidationLevel';
import SslCertificateVendor from './model/SslCertificateVendor';
import SslSubjectAltName from './model/SslSubjectAltName';
import SslSubjectAltNameType from './model/SslSubjectAltNameType';
import TransferDomain from './model/TransferDomain';
import UpdateAliasRequest from './model/UpdateAliasRequest';
import UpdateAntiSpamRequest from './model/UpdateAntiSpamRequest';
import UpdateMailboxPasswordRequest from './model/UpdateMailboxPasswordRequest';
import UpdatePhpAPcuRequest from './model/UpdatePhpAPcuRequest';
import UpdatePhpMemoryLimitRequest from './model/UpdatePhpMemoryLimitRequest';
import UpdateSmtpDomainRequest from './model/UpdateSmtpDomainRequest';
import UpdateUserPasswordRequest from './model/UpdateUserPasswordRequest';
import UpdateUserStatusRequest from './model/UpdateUserStatusRequest';
import UserRights from './model/UserRights';
import ValidationErrorMessage from './model/ValidationErrorMessage';
import WindowsHosting from './model/WindowsHosting';
import WindowsHostingDetail from './model/WindowsHostingDetail';
import WindowsIpType from './model/WindowsIpType';
import WindowsSite from './model/WindowsSite';
import AccountsApi from './api/AccountsApi';
import DNSRecordsApi from './api/DNSRecordsApi';
import DomainsApi from './api/DomainsApi';
import LinuxHostingsApi from './api/LinuxHostingsApi';
import MailZonesApi from './api/MailZonesApi';
import MailboxesApi from './api/MailboxesApi';
import MySqlDatabasesApi from './api/MySqlDatabasesApi';
import ProvisioningJobsApi from './api/ProvisioningJobsApi';
import SSHApi from './api/SSHApi';
import SSLCertificateRequestsApi from './api/SSLCertificateRequestsApi';
import SSLCertificatesApi from './api/SSLCertificatesApi';
import ServicepacksApi from './api/ServicepacksApi';
import WindowsHostingsApi from './api/WindowsHostingsApi';


/**
* # Introduction  This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.  # Conventions  ## Requests  The API supports different methods depending on the required action.  | Method | Description | ---  | --- | GET  | Retrieve resources in a collection or get a single resource.&lt;br/&gt;Getters will never have any effect on the queried resources. | POST  | Create a new resource in a collection. | PUT  | Update an existing resource with its new representation. | DELETE | Delete an existing resource.  ## HTTP status codes  The API will reply with different HTTP statuscodes:  | StatusCode    | Description | ---      | --- | 200 OK     | The requests was processed and you receive data as a result. | 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation. | 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation. | 204 NOCONTENT    | The request has been processed, but no details can be returned. | 400 BADREQUEST   | Your request is malformed. | 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation. | 403 FORBIDDEN    | Access to the resource or operation is not allowed. | 404 NOTFOUND    | The resource cannot be found. | 410 GONE                  | The resource is permanently no longer available. | 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details. | 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.  In the event of a problem, the body of the response will usually contain an errorcode and errormessage. In rare cases additional details about the error are reported.  Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request. We will not take any action besides monitoring.   Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.  ## Formatting  Snake casing is applied on resources and query parameters. The API is strictly returning JSON. No other formats are supported.  Datetimes are returned in ISO-8601 format.  ## Pagination  Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.   **Skip** indicates the number of results to skip and where to start the new take.   **Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.  Paged results will have headers with useful information regarding the paging.  | Header    | Description | ---     | --- | X-Paging-Skipped  | The number of results that have been skipped. | X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. | X-Paging-TotalResults | The total number of results regardless of paging.  ## Rate limiting  The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.  | Header    | Description | ---     | --- | X-RateLimit-Limit  | The number of requests that can be made in a specific time interval. | X-RateLimit-Usage  | The number of requests already made in the current time interval. | X-RateLimit-Remaining | The number of requests remaining until the reset. | X-RateLimit-Reset  | The number of seconds until the reset.&lt;br /&gt;After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header. | Retry-After   | The number of seconds you have to wait until you can make new requests.&lt;br /&gt;This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.  When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase &#39;*Too many requests, retry later.*&#39;.  # Authentication  The Api uses HMAC authentication.   Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.   Both the integrity and the authenticity of the message are verified this way.  ## Steps to generate the HMAC  1. Get your api key and secret from your controlpanel.   It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.   In case your secret is compromised, you can generate a new api key and secret on your controlpanel. 2. Construct the input value for generating the hmac.   Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.  |          | Description | ---         | --- | apikey        | The key that is linked to your user. | request method      | lowercased (eg: get, post, delete,...) | path and querystring information  | urlencoding of the lowercased relative path and querystring.&lt;br /&gt;The path **MUST start with the api version (/v2)**.&lt;br /&gt;The hexadecimal codes (percent encoding) MUST be uppercased. | unix timestamp      | the unix timestamp in **seconds**. | nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request. | content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.&lt;br /&gt;An empty body should not be encoded.  3. Hash the concatenated string using your api secret and the SHA-256 algorithm. 4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.  ## Sending an authorized request  An authorized request can be made by sending the generated HMAC in the authorization header.   A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.  Create the authorization parameter by concatenating:   * apikey   * colon &#39;:&#39;   * generated HMAC signature (see above)   * colon &#39;:&#39;   * nonce (the one used to generate the signature)   * colon &#39;:&#39;   * unix timestamp (the one used to generate the signature)  A sample (illustrated):  * The first line is the string you create to feed to the hashing algorithm. * The second line is the authorization header that should be sent in the request.  ![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \&quot;authorization header illustrated\&quot;)  ## IP whitelisting  Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.  # Versioning  Because of breaking contract changes compared to v1, we released v2 of the API.   V1 will still be available, but you are strongly encouraged to migrate to the latest version.   New features will only be available on v2.  # Policy  ### Fair use policy  Please respect the rate limits and do not use the api for any purposes of abuse.   All requests are being monitored and logged.   Intentional abuse might result in api key revocation.  # Errors  The API attempts to return appropriate HTTP status codes for every request.   When the status code indicates failure, the API will also provide an error message in most cases.  An error message contains a machine-parseable error code accompanied by a descriptive error text.   The text for an error message might change over time, but codes will stay the same.  [An overview of error codes can be found here](/v2/documentation/errorcodes).  # Change log  [An overview of new changes can be found here](/v2/documentation/changelog).  # Provisioning information  ## Terminology  | Term   | Definition                | | ---   | ---                  | | Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.&lt;br/&gt;It also limits the size of individual assets within the same account. | | Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. | | Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...&lt;br/&gt;Some assets are created at the moment when the account is created. Other assets can be created afterwards.   ## Common provisioning scenario  **Provisioning of an account with Linux hosting with one MySql database**  *Without a pre-existing account:*  1. Create a new account.&lt;br/&gt;Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name). 2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).&lt;br/&gt; When the response returns 201(Created), you should read the response body. This will contain links to the created resources.&lt;br/&gt; This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 4. The created resource will point to an account. You now know the account&#39;s Id and can continue with the provisioning of a MySql database on this account. 5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information. 6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).&lt;br/&gt; When the response returns 201(Created), you should read the response body. This will contain links to the created resources.&lt;br/&gt; This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 8. The created resource will point to a MySql database resource.  ## SSL certificate requests  **Requesting an SSL certificate causes the purchase of a paying product.**  1. A certificate is created by adding an ssl certificate request. 2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header. 3. The resource request can respond with different statuscodes: &lt;ul&gt;     &lt;li&gt;200: the certificate request is ongoing.&lt;br/&gt; Check the validations collection for validation values that are not auto_validated. Those should be set by you system.&lt;br/&gt; Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.&lt;/li&gt;     &lt;li&gt;303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.&lt;/li&gt;     &lt;li&gt;410: the certificate request does not exist anymore, there is no certificate created as a result of the request.&lt;/li&gt; &lt;/ul&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var PublicApi = require('index'); // See note below*.
* var xxxSvc = new PublicApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new PublicApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new PublicApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new PublicApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version v2
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Account model constructor.
     * @property {module:model/Account}
     */
    Account,

    /**
     * The AccountDetail model constructor.
     * @property {module:model/AccountDetail}
     */
    AccountDetail,

    /**
     * The AddHostHeaderRequest model constructor.
     * @property {module:model/AddHostHeaderRequest}
     */
    AddHostHeaderRequest,

    /**
     * The AddSshKeyRequest model constructor.
     * @property {module:model/AddSshKeyRequest}
     */
    AddSshKeyRequest,

    /**
     * The AddSubsiteRequest model constructor.
     * @property {module:model/AddSubsiteRequest}
     */
    AddSubsiteRequest,

    /**
     * The AdditionalValidationAttribute model constructor.
     * @property {module:model/AdditionalValidationAttribute}
     */
    AdditionalValidationAttribute,

    /**
     * The Addon model constructor.
     * @property {module:model/Addon}
     */
    Addon,

    /**
     * The Alias model constructor.
     * @property {module:model/Alias}
     */
    Alias,

    /**
     * The AntiSpam model constructor.
     * @property {module:model/AntiSpam}
     */
    AntiSpam,

    /**
     * The AntiSpamTypes model constructor.
     * @property {module:model/AntiSpamTypes}
     */
    AntiSpamTypes,

    /**
     * The ApplicationPool model constructor.
     * @property {module:model/ApplicationPool}
     */
    ApplicationPool,

    /**
     * The AssetType model constructor.
     * @property {module:model/AssetType}
     */
    AssetType,

    /**
     * The AutoForward model constructor.
     * @property {module:model/AutoForward}
     */
    AutoForward,

    /**
     * The AutoRedirectConfig model constructor.
     * @property {module:model/AutoRedirectConfig}
     */
    AutoRedirectConfig,

    /**
     * The AutoReply model constructor.
     * @property {module:model/AutoReply}
     */
    AutoReply,

    /**
     * The BadRequestResponse model constructor.
     * @property {module:model/BadRequestResponse}
     */
    BadRequestResponse,

    /**
     * The CatchAll model constructor.
     * @property {module:model/CatchAll}
     */
    CatchAll,

    /**
     * The CompletionEstimation model constructor.
     * @property {module:model/CompletionEstimation}
     */
    CompletionEstimation,

    /**
     * The CreateAccount model constructor.
     * @property {module:model/CreateAccount}
     */
    CreateAccount,

    /**
     * The CreateAliasRequest model constructor.
     * @property {module:model/CreateAliasRequest}
     */
    CreateAliasRequest,

    /**
     * The CreateCatchAllRequest model constructor.
     * @property {module:model/CreateCatchAllRequest}
     */
    CreateCatchAllRequest,

    /**
     * The CreateMailboxRequest model constructor.
     * @property {module:model/CreateMailboxRequest}
     */
    CreateMailboxRequest,

    /**
     * The CreateMySqlDatabase model constructor.
     * @property {module:model/CreateMySqlDatabase}
     */
    CreateMySqlDatabase,

    /**
     * The CreateMySqlUser model constructor.
     * @property {module:model/CreateMySqlUser}
     */
    CreateMySqlUser,

    /**
     * The CreateSmtpDomainRequest model constructor.
     * @property {module:model/CreateSmtpDomainRequest}
     */
    CreateSmtpDomainRequest,

    /**
     * The CreateSslCertificateRequest model constructor.
     * @property {module:model/CreateSslCertificateRequest}
     */
    CreateSslCertificateRequest,

    /**
     * The DnsRecord model constructor.
     * @property {module:model/DnsRecord}
     */
    DnsRecord,

    /**
     * The Domain model constructor.
     * @property {module:model/Domain}
     */
    Domain,

    /**
     * The DomainDetail model constructor.
     * @property {module:model/DomainDetail}
     */
    DomainDetail,

    /**
     * The EditDomainWillRenewRequest model constructor.
     * @property {module:model/EditDomainWillRenewRequest}
     */
    EditDomainWillRenewRequest,

    /**
     * The EditNameServers model constructor.
     * @property {module:model/EditNameServers}
     */
    EditNameServers,

    /**
     * The ExtraField model constructor.
     * @property {module:model/ExtraField}
     */
    ExtraField,

    /**
     * The FtpConfiguration model constructor.
     * @property {module:model/FtpConfiguration}
     */
    FtpConfiguration,

    /**
     * The GzipConfig model constructor.
     * @property {module:model/GzipConfig}
     */
    GzipConfig,

    /**
     * The HostHeader model constructor.
     * @property {module:model/HostHeader}
     */
    HostHeader,

    /**
     * The Http2Configuration model constructor.
     * @property {module:model/Http2Configuration}
     */
    Http2Configuration,

    /**
     * The LetsEncryptConfig model constructor.
     * @property {module:model/LetsEncryptConfig}
     */
    LetsEncryptConfig,

    /**
     * The LinuxHosting model constructor.
     * @property {module:model/LinuxHosting}
     */
    LinuxHosting,

    /**
     * The LinuxHostingDetail model constructor.
     * @property {module:model/LinuxHostingDetail}
     */
    LinuxHostingDetail,

    /**
     * The LinuxIpType model constructor.
     * @property {module:model/LinuxIpType}
     */
    LinuxIpType,

    /**
     * The LinuxSite model constructor.
     * @property {module:model/LinuxSite}
     */
    LinuxSite,

    /**
     * The MailZone model constructor.
     * @property {module:model/MailZone}
     */
    MailZone,

    /**
     * The MailZoneAccount model constructor.
     * @property {module:model/MailZoneAccount}
     */
    MailZoneAccount,

    /**
     * The Mailbox model constructor.
     * @property {module:model/Mailbox}
     */
    Mailbox,

    /**
     * The MailboxDetail model constructor.
     * @property {module:model/MailboxDetail}
     */
    MailboxDetail,

    /**
     * The MySqlDatabase model constructor.
     * @property {module:model/MySqlDatabase}
     */
    MySqlDatabase,

    /**
     * The MySqlUser model constructor.
     * @property {module:model/MySqlUser}
     */
    MySqlUser,

    /**
     * The NameServer model constructor.
     * @property {module:model/NameServer}
     */
    NameServer,

    /**
     * The PhpVersion model constructor.
     * @property {module:model/PhpVersion}
     */
    PhpVersion,

    /**
     * The ProvisioningJobCompletion model constructor.
     * @property {module:model/ProvisioningJobCompletion}
     */
    ProvisioningJobCompletion,

    /**
     * The ProvisioningJobInfo model constructor.
     * @property {module:model/ProvisioningJobInfo}
     */
    ProvisioningJobInfo,

    /**
     * The ProvisioningJobStatus model constructor.
     * @property {module:model/ProvisioningJobStatus}
     */
    ProvisioningJobStatus,

    /**
     * The RegisterDomain model constructor.
     * @property {module:model/RegisterDomain}
     */
    RegisterDomain,

    /**
     * The Registrant model constructor.
     * @property {module:model/Registrant}
     */
    Registrant,

    /**
     * The RegistrantInput model constructor.
     * @property {module:model/RegistrantInput}
     */
    RegistrantInput,

    /**
     * The ScheduledTask model constructor.
     * @property {module:model/ScheduledTask}
     */
    ScheduledTask,

    /**
     * The Servicepack model constructor.
     * @property {module:model/Servicepack}
     */
    Servicepack,

    /**
     * The SiteBinding model constructor.
     * @property {module:model/SiteBinding}
     */
    SiteBinding,

    /**
     * The SmtpDomain model constructor.
     * @property {module:model/SmtpDomain}
     */
    SmtpDomain,

    /**
     * The SshConfiguration model constructor.
     * @property {module:model/SshConfiguration}
     */
    SshConfiguration,

    /**
     * The SshKey model constructor.
     * @property {module:model/SshKey}
     */
    SshKey,

    /**
     * The SshKeyDetail model constructor.
     * @property {module:model/SshKeyDetail}
     */
    SshKeyDetail,

    /**
     * The SslCertificate model constructor.
     * @property {module:model/SslCertificate}
     */
    SslCertificate,

    /**
     * The SslCertificateDetail model constructor.
     * @property {module:model/SslCertificateDetail}
     */
    SslCertificateDetail,

    /**
     * The SslCertificateFileFormat model constructor.
     * @property {module:model/SslCertificateFileFormat}
     */
    SslCertificateFileFormat,

    /**
     * The SslCertificateRequest model constructor.
     * @property {module:model/SslCertificateRequest}
     */
    SslCertificateRequest,

    /**
     * The SslCertificateRequestDetail model constructor.
     * @property {module:model/SslCertificateRequestDetail}
     */
    SslCertificateRequestDetail,

    /**
     * The SslCertificateRequestValidation model constructor.
     * @property {module:model/SslCertificateRequestValidation}
     */
    SslCertificateRequestValidation,

    /**
     * The SslCertificateRequestValidationType model constructor.
     * @property {module:model/SslCertificateRequestValidationType}
     */
    SslCertificateRequestValidationType,

    /**
     * The SslCertificateType model constructor.
     * @property {module:model/SslCertificateType}
     */
    SslCertificateType,

    /**
     * The SslCertificateValidationLevel model constructor.
     * @property {module:model/SslCertificateValidationLevel}
     */
    SslCertificateValidationLevel,

    /**
     * The SslCertificateVendor model constructor.
     * @property {module:model/SslCertificateVendor}
     */
    SslCertificateVendor,

    /**
     * The SslSubjectAltName model constructor.
     * @property {module:model/SslSubjectAltName}
     */
    SslSubjectAltName,

    /**
     * The SslSubjectAltNameType model constructor.
     * @property {module:model/SslSubjectAltNameType}
     */
    SslSubjectAltNameType,

    /**
     * The TransferDomain model constructor.
     * @property {module:model/TransferDomain}
     */
    TransferDomain,

    /**
     * The UpdateAliasRequest model constructor.
     * @property {module:model/UpdateAliasRequest}
     */
    UpdateAliasRequest,

    /**
     * The UpdateAntiSpamRequest model constructor.
     * @property {module:model/UpdateAntiSpamRequest}
     */
    UpdateAntiSpamRequest,

    /**
     * The UpdateMailboxPasswordRequest model constructor.
     * @property {module:model/UpdateMailboxPasswordRequest}
     */
    UpdateMailboxPasswordRequest,

    /**
     * The UpdatePhpAPcuRequest model constructor.
     * @property {module:model/UpdatePhpAPcuRequest}
     */
    UpdatePhpAPcuRequest,

    /**
     * The UpdatePhpMemoryLimitRequest model constructor.
     * @property {module:model/UpdatePhpMemoryLimitRequest}
     */
    UpdatePhpMemoryLimitRequest,

    /**
     * The UpdateSmtpDomainRequest model constructor.
     * @property {module:model/UpdateSmtpDomainRequest}
     */
    UpdateSmtpDomainRequest,

    /**
     * The UpdateUserPasswordRequest model constructor.
     * @property {module:model/UpdateUserPasswordRequest}
     */
    UpdateUserPasswordRequest,

    /**
     * The UpdateUserStatusRequest model constructor.
     * @property {module:model/UpdateUserStatusRequest}
     */
    UpdateUserStatusRequest,

    /**
     * The UserRights model constructor.
     * @property {module:model/UserRights}
     */
    UserRights,

    /**
     * The ValidationErrorMessage model constructor.
     * @property {module:model/ValidationErrorMessage}
     */
    ValidationErrorMessage,

    /**
     * The WindowsHosting model constructor.
     * @property {module:model/WindowsHosting}
     */
    WindowsHosting,

    /**
     * The WindowsHostingDetail model constructor.
     * @property {module:model/WindowsHostingDetail}
     */
    WindowsHostingDetail,

    /**
     * The WindowsIpType model constructor.
     * @property {module:model/WindowsIpType}
     */
    WindowsIpType,

    /**
     * The WindowsSite model constructor.
     * @property {module:model/WindowsSite}
     */
    WindowsSite,

    /**
    * The AccountsApi service constructor.
    * @property {module:api/AccountsApi}
    */
    AccountsApi,

    /**
    * The DNSRecordsApi service constructor.
    * @property {module:api/DNSRecordsApi}
    */
    DNSRecordsApi,

    /**
    * The DomainsApi service constructor.
    * @property {module:api/DomainsApi}
    */
    DomainsApi,

    /**
    * The LinuxHostingsApi service constructor.
    * @property {module:api/LinuxHostingsApi}
    */
    LinuxHostingsApi,

    /**
    * The MailZonesApi service constructor.
    * @property {module:api/MailZonesApi}
    */
    MailZonesApi,

    /**
    * The MailboxesApi service constructor.
    * @property {module:api/MailboxesApi}
    */
    MailboxesApi,

    /**
    * The MySqlDatabasesApi service constructor.
    * @property {module:api/MySqlDatabasesApi}
    */
    MySqlDatabasesApi,

    /**
    * The ProvisioningJobsApi service constructor.
    * @property {module:api/ProvisioningJobsApi}
    */
    ProvisioningJobsApi,

    /**
    * The SSHApi service constructor.
    * @property {module:api/SSHApi}
    */
    SSHApi,

    /**
    * The SSLCertificateRequestsApi service constructor.
    * @property {module:api/SSLCertificateRequestsApi}
    */
    SSLCertificateRequestsApi,

    /**
    * The SSLCertificatesApi service constructor.
    * @property {module:api/SSLCertificatesApi}
    */
    SSLCertificatesApi,

    /**
    * The ServicepacksApi service constructor.
    * @property {module:api/ServicepacksApi}
    */
    ServicepacksApi,

    /**
    * The WindowsHostingsApi service constructor.
    * @property {module:api/WindowsHostingsApi}
    */
    WindowsHostingsApi
};
