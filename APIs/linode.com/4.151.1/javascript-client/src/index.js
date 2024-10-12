/**
 * Linode API
 * ## Introduction The Linode API provides the ability to programmatically manage the full range of Linode products and services.  This reference is designed to assist application developers and system administrators.  Each endpoint includes descriptions, request syntax, and examples using standard HTTP requests. Response data is returned in JSON format.   This document was generated from our OpenAPI Specification.  See the <a target=\"_top\" href=\"https://www.openapis.org\">OpenAPI website</a> for more information.  <a target=\"_top\" href=\"/docs/api/openapi.yaml\">Download the Linode OpenAPI Specification</a>.   ## Changelog  <a target=\"_top\" href=\"/docs/products/tools/api/release-notes/\">View our Changelog</a> to see release notes on all changes made to our API.  ## Access and Authentication  Some endpoints are publicly accessible without requiring authentication. All endpoints affecting your Account, however, require either a Personal Access Token or OAuth authentication (when using third-party applications).  ### Personal Access Token  The easiest way to access the API is with a Personal Access Token (PAT) generated from the <a target=\"_top\" href=\"https://cloud.linode.com/profile/tokens\">Linode Cloud Manager</a> or the [Create Personal Access Token](/docs/api/profile/#personal-access-token-create) endpoint.  All scopes for the OAuth security model ([defined below](/docs/api/#oauth)) apply to this security model as well.  ### Authentication  | Security Scheme Type: | HTTP | |-----------------------|------| | **HTTP Authorization Scheme** | bearer |  ## OAuth  If you only need to access the Linode API for personal use, we recommend that you create a [personal access token](/docs/api/#personal-access-token). If you're designing an application that can authenticate with an arbitrary Linode user, then you should use the OAuth 2.0 workflows presented in this section.  For a more detailed example of an OAuth 2.0 implementation, see our guide on [How to Create an OAuth App with the Linode Python API Library](/docs/products/tools/api/guides/create-an-oauth-app-with-the-python-api-library/#oauth-2-authentication-exchange).  Before you implement OAuth in your application, you first need to create an OAuth client. You can do this [with the Linode API](/docs/api/account/#oauth-client-create) or [via the Cloud Manager](https://cloud.linode.com/profile/clients):    - When creating the client, you'll supply a `label` and a `redirect_uri` (referred to as the Callback URL in the Cloud Manager).   - The response from this endpoint will give you a `client_id` and a `secret`.   - Clients can be public or private, and are private by default. You can choose to make the client public when it is created.     - A private client is used with applications which can securely store the client secret (that is, the secret returned to you when you first created the client). For example, an application running on a secured server that only the developer has access to would use a private OAuth client. This is also called a confidential client in some OAuth documentation.     - A public client is used with applications where the client secret is not guaranteed to be secure. For example, a native app running on a user's computer may not be able to keep the client secret safe, as a user could potentially inspect the source of the application. So, native apps or apps that run in a user's browser should use a public client.     - Public and private clients follow different workflows, as described below.  ### OAuth Workflow  The OAuth workflow is a series of exchanges between your third-party app and Linode. The workflow is used to authenticate a user before an application can start making API calls on the user's behalf.  Notes:  - With respect to the diagram in [section 1.2 of RFC 6749](https://tools.ietf.org/html/rfc6749#section-1.2), login.linode.com (referred to in this section as the *login server*) is the Resource Owner and the Authorization Server; api.linode.com (referred to here as the *api server*) is the Resource Server. - The OAuth spec refers to the private and public workflows listed below as the [authorization code flow](https://tools.ietf.org/html/rfc6749#section-1.3.1) and [implicit flow](https://tools.ietf.org/html/rfc6749#section-1.3.2).  | PRIVATE WORKFLOW | PUBLIC WORKFLOW | |------------------|------------------| | 1.  The user visits the application's website and is directed to login with Linode. | 1.  The user visits the application's website and is directed to login with Linode. | | 2.  Your application then redirects the user to Linode's [login server](https://login.linode.com) with the client application's `client_id` and requested OAuth `scope`, which should appear in the URL of the login page. | 2.  Your application then redirects the user to Linode's [login server](https://login.linode.com) with the client application's `client_id` and requested OAuth `scope`, which should appear in the URL of the login page. | | 3.  The user logs into the login server with their username and password. | 3.  The user logs into the login server with their username and password. | | 4.  The login server redirects the user to the specificed redirect URL with a temporary authorization `code` (exchange code) in the URL. | 4.  The login server redirects the user back to your application with an OAuth `access_token` embedded in the redirect URL's hash. This is temporary and expires in two hours. No `refresh_token` is issued. Therefore, once the `access_token` expires, a new one will need to be issued by having the user log in again. | | 5.  The application issues a POST request (*see additional details below*) to the login server with the exchange code, `client_id`, and the client application's `client_secret`. | | | 6.  The login server responds to the client application with a new OAuth `access_token` and `refresh_token`. The `access_token` is set to expire in two hours. | | | 7.  The `refresh_token` can be used by contacting the login server with the `client_id`, `client_secret`, `grant_type`, and `refresh_token` to get a new OAuth `access_token` and `refresh_token`. The new `access_token` is good for another two hours, and the new `refresh_token` can be used to extend the session again by this same method (*see additional details below*). | |  #### OAuth Private Workflow - Additional Details  The following information expands on steps 5 through 7 of the private workflow:  Once the user has logged into Linode and you have received an exchange code, you will need to trade that exchange code for an `access_token` and `refresh_token`. You do this by making an HTTP POST request to the following address:  ``` https://login.linode.com/oauth/token ```  Make this request as `application/x-www-form-urlencoded` or as `multipart/form-data` and include the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | client_id | Your app's client ID. | | client_secret | Your app's client secret. | | code | The code you just received from the redirect. |  You'll get a response like this:  ```json {   \"scope\": \"linodes:read_write\",   \"access_token\": \"03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c\",   \"refresh_token\": \"f2ec9712e616fdb5a2a21aa0e88cfadea7502ebc62cf5bd758dbcd65e1803bad\",   \"token_type\": \"bearer\",   \"expires_in\": 7200 } ```  Included in the response is an `access_token`. With this token, you can proceed to make authenticated HTTP requests to the API by adding this header to each request:  ``` Authorization: Bearer 03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c ```  This `access_token` is set to expire in two hours. To refresh access prior to expiration, make another request to the same URL with the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | grant_type | The grant type you're using. Use \"refresh_token\" when refreshing access. | | client_id | Your app's client ID. | | client_secret | Your app's client secret. | | refresh_token | The `refresh_token` received from the previous response. |  You'll get another response with an updated `access_token` and `refresh_token`, which can then be used to refresh access again.  ### OAuth Reference  | Security Scheme Type | OAuth 2.0 | |-----------------------|--------| | **Authorization URL** | `https://login.linode.com/oauth/authorize` | | **Token URL** | `https://login.linode.com/oauth/token` | | **Scopes** | <ul><li>`account:read_only` - Allows access to GET information about your Account.</li><li>`account:read_write` - Allows access to all endpoints related to your Account.</li><li>`databases:read_only` - Allows access to GET Managed Databases on your Account.</li><li>`databases:read_write` - Allows access to all endpoints related to your Managed Databases.</li><li>`domains:read_only` - Allows access to GET Domains on your Account.</li><li>`domains:read_write` - Allows access to all Domain endpoints.</li><li>`events:read_only` - Allows access to GET your Events.</li><li>`events:read_write` - Allows access to all endpoints related to your Events.</li><li>`firewall:read_only` - Allows access to GET information about your Firewalls.</li><li>`firewall:read_write` - Allows access to all Firewall endpoints.</li><li>`images:read_only` - Allows access to GET your Images.</li><li>`images:read_write` - Allows access to all endpoints related to your Images.</li><li>`ips:read_only` - Allows access to GET your ips.</li><li>`ips:read_write` - Allows access to all endpoints related to your ips.</li><li>`linodes:read_only` - Allows access to GET Linodes on your Account.</li><li>`linodes:read_write` - Allow access to all endpoints related to your Linodes.</li><li>`lke:read_only` - Allows access to GET LKE Clusters on your Account.</li><li>`lke:read_write` - Allows access to all endpoints related to LKE Clusters on your Account.</li><li>`longview:read_only` - Allows access to GET your Longview Clients.</li><li>`longview:read_write` - Allows access to all endpoints related to your Longview Clients.</li><li>`nodebalancers:read_only` - Allows access to GET NodeBalancers on your Account.</li><li>`nodebalancers:read_write` - Allows access to all NodeBalancer endpoints.</li><li>`object_storage:read_only` - Allows access to GET information related to your Object Storage.</li><li>`object_storage:read_write` - Allows access to all Object Storage endpoints.</li><li>`stackscripts:read_only` - Allows access to GET your StackScripts.</li><li>`stackscripts:read_write` - Allows access to all endpoints related to your StackScripts.</li><li>`volumes:read_only` - Allows access to GET your Volumes.</li><li>`volumes:read_write` - Allows access to all endpoints related to your Volumes.</li></ul><br/>|  ## Requests  Requests must be made over HTTPS to ensure transactions are encrypted. Data included in requests must be supplied in json format unless otherwise specified in the command description.  The following request methods are supported:  | METHOD  | USAGE | |---------|-------| | GET     | Retrieves data about collections and individual resources. | | POST    | For collections, creates a new resource of that type. Also used to perform actions on action endpoints. | | PUT     | Updates an existing resource. | | DELETE  | Deletes a resource. This is a destructive action. | | HEAD    | Returns only the response header information of a GET request | | OPTIONS | Provides permitted communication options for a command |  ## Responses  ### Response Status Codes  Actions will return one of the following HTTP response status codes:  | STATUS  | DESCRIPTION | |---------|-------------| | 200 OK  | The request was successful. | | 202 Accepted | The request was successful, but processing has not been completed. The response body includes a \"warnings\" array containing the details of incomplete processes. | | 204 No Content | The server successfully fulfilled the request and there is no additional content to send. | | 299 Deprecated | The request was successful, but involved a deprecated endpoint. The response body includes a \"warnings\" array containing warning messages. | | 400 Bad Request | You submitted an invalid request (missing parameters, etc.). | | 401 Unauthorized | You failed to authenticate for this resource. | | 403 Forbidden | You are authenticated, but don't have permission to do this. | | 404 Not Found | The resource you're requesting does not exist. | | 429 Too Many Requests | You've hit a rate limit. | | 500 Internal Server Error | Please [open a Support Ticket](/docs/api/support/#support-ticket-open). |  ### Response Headers  There are many ways to access response header information for individual command URLs, depending on how you are accessing the Linode API. For example, to view HTTP response headers for the `/regions` endpoint when making requests with `curl`, use the `-I` or `--head` option as follows:  ```Shell curl -I https://api.linode.com/v4/regions ```  Responses may include the following headers:  | HEADER | DESCRIPTION | EXAMPLE | |--------|-------------|---------| | Access-Control-Allow-Credentials | Responses to credentialed requests are exposed to frontend JavaScript code. | true | | Access-Control-Allow-Headers | All permissible request headers for this endpoint. | Authorization, Origin, X-Requested-With, Content-Type, Accept, X-Filter | | Access-Control-Allow-Methods | Permissible HTTP methods for this endpoint | HEAD, GET, OPTIONS, POST, PUT, DELETE | | Access-Control-Allow-Origin | Indicates origin access permissions. The wildcard character `*` means any origin can access the resource. | * | | Access-Control-Expose-Headers | Available headers to include in response to cross-origin requests. | X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Status | | Cache-Control | Controls caching in browsers and shared caches such as CDNs. | private, max-age=60, s-maxage=60 | | Content-Security-Policy | Controls which resources are allowed to load. By default, resources do not load. | default-src 'none' | | Content-Type | All responses are in json format. | application/json | | Content-Warning | A message containing instructions for successful requests that were not able to be completed. | Please contact support for assistance. | | Retry-After | The remaining time in seconds until the current [rate limit](#rate-limiting) window resets. | 60 | | Strict-Transport-Security | Enforces HTTPS-only access until the returned time in seconds. | max-age=31536000 | | Vary | Optional request headers that affected the response content. | Authorization, X-Filter | | X-Accepted-OAuth-Scopes | Required [scopes](#oauth-reference) for accessing the requested command. | linodes:read_only | | X-Customer-UUID | A unique identifier for the account owning the the [personal access token](#personal-access-token) that was used for the request. | ABCDEF01-3456-789A-BCDEF0123456789A | | X-OAuth-Scopes | Allowed [scopes](#oauth-reference) associated with the [personal access token](#personal-access-token) that was used for the request. A value of `*` indicates read/write access for all scope categories. | images:read_write linodes:read_only | | X-RateLimit-Limit | The maximum number of permitted requests during the [rate limit](#rate-limiting) window for this endpoint. | 800 | | X-RateLimit-Remaining | The remaining number of permitted requests in the current [rate limit](#rate-limiting) window. | 798 | | X-RateLimit-Reset | The time when the current [rate limit](#rate-limiting) window rests in UTC epoch seconds. | 1674747739 | | X-Spec-Version | The current API version that handled the request. | 4.150.0 |  ## Errors  Success is indicated via <a href=\"https://en.wikipedia.org/wiki/List_of_HTTP_status_codes\" target=\"_top\">Standard HTTP status codes</a>. `2xx` codes indicate success, `4xx` codes indicate a request error, and `5xx` errors indicate a server error. A request error might be an invalid input, a required parameter being omitted, or a malformed request. A server error means something went wrong processing your request. If this occurs, please [open a Support Ticket](/docs/api/support/#support-ticket-open) and let us know. Though errors are logged and we work quickly to resolve issues, opening a ticket and providing us with reproducable steps and data is always helpful.  The `errors` field is an array of the things that went wrong with your request. We will try to include as many of the problems in the response as possible, but it's conceivable that fixing these errors and resubmitting may result in new errors coming back once we are able to get further along in the process of handling your request.  Within each error object, the `field` parameter will be included if the error pertains to a specific field in the JSON you've submitted. This will be omitted if there is no relevant field. The `reason` is a human-readable explanation of the error, and will always be included.  ## Pagination  Resource lists are always paginated. The response will look similar to this:  ```json {     \"data\": [ ... ],     \"page\": 1,     \"pages\": 3,     \"results\": 300 } ```  * Pages start at 1. You may retrieve a specific page of results by adding `?page=x` to your URL (for example, `?page=4`). If the value of `page` exceeds `2^64/page_size`, the last possible page will be returned.   * Page sizes default to 100, and can be set to return between 25 and 500. Page size can be set using `?page_size=x`.  ## Filtering and Sorting  Collections are searchable by fields they include, marked in the spec as `x-linode-filterable: true`. Filters are passed in the `X-Filter` header and are formatted as JSON objects. Here is a request call for Linode Types in our \"standard\" class:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"class\": \"standard\" }' ```  The filter object's keys are the keys of the object you're filtering, and the values are accepted values. You can add multiple filters by including more than one key. For example, filtering for \"standard\" Linode Types that offer one vcpu:  ```Shell  curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"class\": \"standard\", \"vcpus\": 1 }' ```  In the above example, both filters are combined with an \"and\" operation. However, if you wanted either Types with one vcpu or Types in our \"standard\" class, you can add an operator:   ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"+or\": [ { \"vcpus\": 1 }, { \"class\": \"standard\" } ] }' ```  Each filter in the `+or` array is its own filter object, and all conditions in it are combined with an \"and\" operation as they were in the previous example.  Other operators are also available. Operators are keys of a Filter JSON object. Their value must be of the appropriate type, and they are evaluated as described below:  | OPERATOR | TYPE   | DESCRIPTION                       | |----------|--------|-----------------------------------| | +and     | array  | All conditions must be true.       | | +or      | array  | One condition must be true.        | | +gt      | number | Value must be greater than number. | | +gte     | number | Value must be greater than or equal to number. | | +lt      | number | Value must be less than number. | | +lte     | number | Value must be less than or equal to number. | | +contains | string | Given string must be in the value. | | +neq      | string | Does not equal the value.          | | +order_by | string | Attribute to order the results by - must be filterable. | | +order    | string | Either \"asc\" or \"desc\". Defaults to \"asc\". Requires `+order_by`. |  For example, filtering for [Linode Types](/docs/api/linode-types/) that offer memory equal to or higher than 61440:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H '     X-Filter: {       \"memory\": {         \"+gte\": 61440       }     }' ```  You can combine and nest operators to construct arbitrarily-complex queries. For example, give me all [Linode Types](/docs/api/linode-types/) which are either `standard` or `highmem` class, or have between 12 and 20 vcpus:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H '     X-Filter: {       \"+or\": [         {           \"+or\": [             {               \"class\": \"standard\"             },             {               \"class\": \"highmem\"             }           ]         },         {           \"+and\": [             {               \"vcpus\": {                 \"+gte\": 12               }             },             {               \"vcpus\": {                 \"+lte\": 20               }             }           ]         }       ]     }' ``` ## Time Values  All times returned by the API are in UTC, regardless of the timezone configured within your user's profile (see `timezone` property within [Profile View](/docs/api/profile/#profile-view__responses)).  ## Rate Limiting  Rate limits on API requests help maintain the health and stability of the Linode API. Accordingly, every endpoint of the Linode API applies a rate limit on a per user basis as determined by OAuth token for authenticated requests or IP address for public endpoints.  Each rate limit consists of a total number of requests and a time window. For example, if an endpoint has a rate limit of 800 requests per minute, then up to 800 requests over a one minute window are permitted. Subsequent requests to an endpoint after hitting a rate limit return a 429 error. You can successfully remake requests to that endpoint after the rate limit window resets.  ### Linode APIv4 Rate Limits  With the Linode API, you can generally make up to 1,600 general API requests every two minutes. Additionally, all endpoints have a rate limit of 800 requests per minute unless otherwise specified below.  **Note:** There may be rate limiting applied at other levels outside of the API, for example, at the load balancer.  Creating Linodes has a dedicated rate limit of 10 requests per 30 seconds. That endpoint is:  * [Linode Create](/docs/api/linode-instances/#linode-create)  `/stats` endpoints have their own dedicated rate limits of 100 requests per minute. These endpoints are:  * [View Linode Statistics](/docs/api/linode-instances/#linode-statistics-view) * [View Linode Statistics (year/month)](/docs/api/linode-instances/#statistics-yearmonth-view) * [View NodeBalancer Statistics](/docs/api/nodebalancers/#nodebalancer-statistics-view) * [List Managed Stats](/docs/api/managed/#managed-stats-list)  Object Storage endpoints have a dedicated rate limit of 750 requests per second. The Object Storage endpoints are:  * [Object Storage Endpoints](/docs/api/object-storage/)  Opening Support Tickets has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Open Support Ticket](/docs/api/support/#support-ticket-open)  Accepting Service Transfers has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Service Transfer Accept](/docs/api/account/#service-transfer-accept)  ### Rate Limit HTTP Response Headers  The Linode API includes the following HTTP response headers which are designed to help you avoid hitting rate limits which might disrupt your applications:  * **X-RateLimit-Limit**: The maximum number of permitted requests during the rate limit window for this endpoint. * **X-RateLimit-Remaining**: The remaining number of permitted requests in the current rate limit window. * **X-RateLimit-Reset**: The time when the current rate limit window rests in UTC epoch seconds. * **Retry-After**: The remaining time in seconds until the current rate limit window resets.  ## CLI (Command Line Interface)  The <a href=\"https://github.com/linode/linode-cli\" target=\"_top\">Linode CLI</a> allows you to easily work with the API using intuitive and simple syntax. It requires a [Personal Access Token](/docs/api/#personal-access-token) for authentication, and gives you access to all of the features and functionality of the Linode API that are documented here with CLI examples.  Endpoints that do not have CLI examples are currently unavailable through the CLI, but can be accessed via other methods such as Shell commands and other third-party applications. 
 *
 * The version of the OpenAPI document: 4.151.1
 * Contact: support@linode.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Account from './model/Account';
import AccountCreditCard from './model/AccountCreditCard';
import AccountSettings from './model/AccountSettings';
import AddLinodeIPRequest from './model/AddLinodeIPRequest';
import AllocateIPRequest from './model/AllocateIPRequest';
import AttachVolumeRequest from './model/AttachVolumeRequest';
import AuthorizedApp from './model/AuthorizedApp';
import Backup from './model/Backup';
import BackupDisksInner from './model/BackupDisksInner';
import BootLinodeInstanceRequest from './model/BootLinodeInstanceRequest';
import CancelAccount200Response from './model/CancelAccount200Response';
import CancelAccount409Response from './model/CancelAccount409Response';
import CancelAccount409ResponseErrorsInner from './model/CancelAccount409ResponseErrorsInner';
import CancelAccountRequest from './model/CancelAccountRequest';
import CloneDomainRequest from './model/CloneDomainRequest';
import CloneLinodeInstanceRequest from './model/CloneLinodeInstanceRequest';
import CloneVolumeRequest from './model/CloneVolumeRequest';
import CreateEntityTransferRequest from './model/CreateEntityTransferRequest';
import CreateFirewallsRequest from './model/CreateFirewallsRequest';
import CreateFirewallsRequestDevices from './model/CreateFirewallsRequestDevices';
import CreateFirewallsRequestRules from './model/CreateFirewallsRequestRules';
import CreateImageRequest from './model/CreateImageRequest';
import CreateLKEClusterRequest from './model/CreateLKEClusterRequest';
import CreateLKEClusterRequestControlPlane from './model/CreateLKEClusterRequestControlPlane';
import CreateLinodeInstanceRequest from './model/CreateLinodeInstanceRequest';
import CreateManagedCredentialRequest from './model/CreateManagedCredentialRequest';
import CreateNodeBalancerRequest from './model/CreateNodeBalancerRequest';
import CreateNodeBalancerRequestConfigsInner from './model/CreateNodeBalancerRequestConfigsInner';
import CreateObjectStorageBucketRequest from './model/CreateObjectStorageBucketRequest';
import CreateObjectStorageObjectURL200Response from './model/CreateObjectStorageObjectURL200Response';
import CreateObjectStorageObjectURLRequest from './model/CreateObjectStorageObjectURLRequest';
import CreatePayPalPayment200Response from './model/CreatePayPalPayment200Response';
import CreatePayment202Response from './model/CreatePayment202Response';
import CreatePaymentMethodRequest from './model/CreatePaymentMethodRequest';
import CreatePersonalAccessTokenRequest from './model/CreatePersonalAccessTokenRequest';
import CreatePromoCreditRequest from './model/CreatePromoCreditRequest';
import CreateServiceTransferRequest from './model/CreateServiceTransferRequest';
import CreateSnapshotRequest from './model/CreateSnapshotRequest';
import CreateTagRequest from './model/CreateTagRequest';
import CreateTicketReplyRequest from './model/CreateTicketReplyRequest';
import CreateVolumeRequest from './model/CreateVolumeRequest';
import CreditCard from './model/CreditCard';
import CreditCardData from './model/CreditCardData';
import Database from './model/Database';
import DatabaseBackup from './model/DatabaseBackup';
import DatabaseBackupSnapshot from './model/DatabaseBackupSnapshot';
import DatabaseCredentials from './model/DatabaseCredentials';
import DatabaseEngine from './model/DatabaseEngine';
import DatabaseHosts from './model/DatabaseHosts';
import DatabaseMongoDB from './model/DatabaseMongoDB';
import DatabaseMongoDBHosts from './model/DatabaseMongoDBHosts';
import DatabaseMongoDBRequest from './model/DatabaseMongoDBRequest';
import DatabaseMySQL from './model/DatabaseMySQL';
import DatabaseMySQLRequest from './model/DatabaseMySQLRequest';
import DatabasePostgreSQL from './model/DatabasePostgreSQL';
import DatabasePostgreSQLHosts from './model/DatabasePostgreSQLHosts';
import DatabasePostgreSQLRequest from './model/DatabasePostgreSQLRequest';
import DatabaseSSL from './model/DatabaseSSL';
import DatabaseType from './model/DatabaseType';
import DatabaseTypeEngine from './model/DatabaseTypeEngine';
import DatabaseTypeEnginePrice from './model/DatabaseTypeEnginePrice';
import DatabaseTypeEngines from './model/DatabaseTypeEngines';
import DatabaseUpdates from './model/DatabaseUpdates';
import Device from './model/Device';
import Devices from './model/Devices';
import Disk from './model/Disk';
import DiskRequest from './model/DiskRequest';
import Domain from './model/Domain';
import DomainRecord from './model/DomainRecord';
import EntityTransfer from './model/EntityTransfer';
import EntityTransferEntities from './model/EntityTransferEntities';
import ErrorObject from './model/ErrorObject';
import Event from './model/Event';
import EventEntity from './model/EventEntity';
import EventSecondaryEntity from './model/EventSecondaryEntity';
import Firewall from './model/Firewall';
import FirewallDevices from './model/FirewallDevices';
import FirewallDevicesEntity from './model/FirewallDevicesEntity';
import FirewallRuleConfig from './model/FirewallRuleConfig';
import FirewallRuleConfigAddresses from './model/FirewallRuleConfigAddresses';
import FirewallRules from './model/FirewallRules';
import GetAccountDefaultResponse from './model/GetAccountDefaultResponse';
import GetAccountLogins200Response from './model/GetAccountLogins200Response';
import GetBackups200Response from './model/GetBackups200Response';
import GetBackups200ResponseAutomaticInner from './model/GetBackups200ResponseAutomaticInner';
import GetBackups200ResponseSnapshot from './model/GetBackups200ResponseSnapshot';
import GetClients200Response from './model/GetClients200Response';
import GetDatabasesEngines200Response from './model/GetDatabasesEngines200Response';
import GetDatabasesInstances200Response from './model/GetDatabasesInstances200Response';
import GetDatabasesMongoDBInstanceBackups200Response from './model/GetDatabasesMongoDBInstanceBackups200Response';
import GetDatabasesMongoDBInstances200Response from './model/GetDatabasesMongoDBInstances200Response';
import GetDatabasesMySQLInstances200Response from './model/GetDatabasesMySQLInstances200Response';
import GetDatabasesPostgreSQLInstances200Response from './model/GetDatabasesPostgreSQLInstances200Response';
import GetDatabasesTypes200Response from './model/GetDatabasesTypes200Response';
import GetDevices200Response from './model/GetDevices200Response';
import GetDomainRecords200Response from './model/GetDomainRecords200Response';
import GetDomainZone200Response from './model/GetDomainZone200Response';
import GetDomains200Response from './model/GetDomains200Response';
import GetEntityTransfers200Response from './model/GetEntityTransfers200Response';
import GetEvents200Response from './model/GetEvents200Response';
import GetFirewallDevices200Response from './model/GetFirewallDevices200Response';
import GetIPs200Response from './model/GetIPs200Response';
import GetIPv6Pools200Response from './model/GetIPv6Pools200Response';
import GetIPv6Ranges200Response from './model/GetIPv6Ranges200Response';
import GetImages200Response from './model/GetImages200Response';
import GetInvoiceItems200Response from './model/GetInvoiceItems200Response';
import GetInvoices200Response from './model/GetInvoices200Response';
import GetKernels200Response from './model/GetKernels200Response';
import GetLKEClusterAPIEndpoints200Response from './model/GetLKEClusterAPIEndpoints200Response';
import GetLKEClusterAPIEndpoints200ResponseDataInner from './model/GetLKEClusterAPIEndpoints200ResponseDataInner';
import GetLKEClusterDashboard200Response from './model/GetLKEClusterDashboard200Response';
import GetLKEClusterKubeconfig200Response from './model/GetLKEClusterKubeconfig200Response';
import GetLKEClusterNode200Response from './model/GetLKEClusterNode200Response';
import GetLKEClusterPools200Response from './model/GetLKEClusterPools200Response';
import GetLKEClusters200Response from './model/GetLKEClusters200Response';
import GetLKEVersions200Response from './model/GetLKEVersions200Response';
import GetLinodeConfigs200Response from './model/GetLinodeConfigs200Response';
import GetLinodeDisks200Response from './model/GetLinodeDisks200Response';
import GetLinodeFirewalls200Response from './model/GetLinodeFirewalls200Response';
import GetLinodeIPs200Response from './model/GetLinodeIPs200Response';
import GetLinodeIPs200ResponseIpv4 from './model/GetLinodeIPs200ResponseIpv4';
import GetLinodeIPs200ResponseIpv6 from './model/GetLinodeIPs200ResponseIpv6';
import GetLinodeInstances200Response from './model/GetLinodeInstances200Response';
import GetLinodeNodeBalancers200Response from './model/GetLinodeNodeBalancers200Response';
import GetLinodeTransfer200Response from './model/GetLinodeTransfer200Response';
import GetLinodeTransferByYearMonth200Response from './model/GetLinodeTransferByYearMonth200Response';
import GetLinodeTypes200Response from './model/GetLinodeTypes200Response';
import GetLinodeVolumes200Response from './model/GetLinodeVolumes200Response';
import GetLongviewClients200Response from './model/GetLongviewClients200Response';
import GetLongviewSubscriptions200Response from './model/GetLongviewSubscriptions200Response';
import GetMaintenance200Response from './model/GetMaintenance200Response';
import GetManagedContacts200Response from './model/GetManagedContacts200Response';
import GetManagedCredentials200Response from './model/GetManagedCredentials200Response';
import GetManagedIssues200Response from './model/GetManagedIssues200Response';
import GetManagedLinodeSettings200Response from './model/GetManagedLinodeSettings200Response';
import GetManagedServices200Response from './model/GetManagedServices200Response';
import GetManagedStats200Response from './model/GetManagedStats200Response';
import GetManagedStats200ResponseData from './model/GetManagedStats200ResponseData';
import GetNodeBalancerConfigNodes200Response from './model/GetNodeBalancerConfigNodes200Response';
import GetNodeBalancerConfigs200Response from './model/GetNodeBalancerConfigs200Response';
import GetNotifications200Response from './model/GetNotifications200Response';
import GetObjectStorageBucketContent200Response from './model/GetObjectStorageBucketContent200Response';
import GetObjectStorageBuckets200Response from './model/GetObjectStorageBuckets200Response';
import GetObjectStorageClusters200Response from './model/GetObjectStorageClusters200Response';
import GetObjectStorageKeys200Response from './model/GetObjectStorageKeys200Response';
import GetObjectStorageTransfer200Response from './model/GetObjectStorageTransfer200Response';
import GetPaymentMethods200Response from './model/GetPaymentMethods200Response';
import GetPayments200Response from './model/GetPayments200Response';
import GetPersonalAccessTokens200Response from './model/GetPersonalAccessTokens200Response';
import GetProfileApps200Response from './model/GetProfileApps200Response';
import GetRegions200Response from './model/GetRegions200Response';
import GetSSHKeys200Response from './model/GetSSHKeys200Response';
import GetServiceTransfers200Response from './model/GetServiceTransfers200Response';
import GetStackScripts200Response from './model/GetStackScripts200Response';
import GetTaggedObjects200Response from './model/GetTaggedObjects200Response';
import GetTaggedObjects200ResponseDataInner from './model/GetTaggedObjects200ResponseDataInner';
import GetTaggedObjects200ResponseDataInnerData from './model/GetTaggedObjects200ResponseDataInnerData';
import GetTags200Response from './model/GetTags200Response';
import GetTicketReplies200Response from './model/GetTicketReplies200Response';
import GetTickets200Response from './model/GetTickets200Response';
import GetUsers200Response from './model/GetUsers200Response';
import GetVLANs200Response from './model/GetVLANs200Response';
import GooglePayData from './model/GooglePayData';
import Grant from './model/Grant';
import GrantsResponse from './model/GrantsResponse';
import GrantsResponseGlobal from './model/GrantsResponseGlobal';
import IPAddress from './model/IPAddress';
import IPAddressPrivate from './model/IPAddressPrivate';
import IPAddressV6LinkLocal from './model/IPAddressV6LinkLocal';
import IPAddressV6Slaac from './model/IPAddressV6Slaac';
import IPAddressesAssignRequest from './model/IPAddressesAssignRequest';
import IPAddressesAssignRequestAssignmentsInner from './model/IPAddressesAssignRequestAssignmentsInner';
import IPAddressesShareRequest from './model/IPAddressesShareRequest';
import IPv6Pool from './model/IPv6Pool';
import IPv6Range from './model/IPv6Range';
import IPv6RangeBGP from './model/IPv6RangeBGP';
import Image from './model/Image';
import ImagesUploadPost200Response from './model/ImagesUploadPost200Response';
import ImagesUploadPostRequest from './model/ImagesUploadPostRequest';
import ImportDomainRequest from './model/ImportDomainRequest';
import Invoice from './model/Invoice';
import InvoiceItem from './model/InvoiceItem';
import InvoiceTaxSummaryInner from './model/InvoiceTaxSummaryInner';
import Kernel from './model/Kernel';
import LKECluster from './model/LKECluster';
import LKEClusterControlPlane from './model/LKEClusterControlPlane';
import LKENodePool from './model/LKENodePool';
import LKENodePoolAutoscaler from './model/LKENodePoolAutoscaler';
import LKENodePoolDisksInner from './model/LKENodePoolDisksInner';
import LKENodePoolRequestBody from './model/LKENodePoolRequestBody';
import LKENodePoolRequestBodyAutoscaler from './model/LKENodePoolRequestBodyAutoscaler';
import LKENodeStatus from './model/LKENodeStatus';
import LKEVersion from './model/LKEVersion';
import Linode from './model/Linode';
import LinodeAlerts from './model/LinodeAlerts';
import LinodeBackups from './model/LinodeBackups';
import LinodeBackupsSchedule from './model/LinodeBackupsSchedule';
import LinodeConfig from './model/LinodeConfig';
import LinodeConfigHelpers from './model/LinodeConfigHelpers';
import LinodeConfigInterface from './model/LinodeConfigInterface';
import LinodeRequest from './model/LinodeRequest';
import LinodeSpecs from './model/LinodeSpecs';
import LinodeStats from './model/LinodeStats';
import LinodeStatsIo from './model/LinodeStatsIo';
import LinodeStatsNetv4 from './model/LinodeStatsNetv4';
import LinodeStatsNetv6 from './model/LinodeStatsNetv6';
import LinodeType from './model/LinodeType';
import LinodeTypeAddons from './model/LinodeTypeAddons';
import LinodeTypeAddonsBackups from './model/LinodeTypeAddonsBackups';
import LinodeTypeAddonsBackupsPrice from './model/LinodeTypeAddonsBackupsPrice';
import LinodeTypePrice from './model/LinodeTypePrice';
import Login from './model/Login';
import LongviewClient from './model/LongviewClient';
import LongviewClientApps from './model/LongviewClientApps';
import LongviewPlan from './model/LongviewPlan';
import LongviewSubscription from './model/LongviewSubscription';
import LongviewSubscriptionPrice from './model/LongviewSubscriptionPrice';
import Maintenance from './model/Maintenance';
import MaintenanceEntity from './model/MaintenanceEntity';
import ManagedContact from './model/ManagedContact';
import ManagedContactPhone from './model/ManagedContactPhone';
import ManagedCredential from './model/ManagedCredential';
import ManagedIssue from './model/ManagedIssue';
import ManagedIssueEntity from './model/ManagedIssueEntity';
import ManagedLinodeSettings from './model/ManagedLinodeSettings';
import ManagedLinodeSettingsSsh from './model/ManagedLinodeSettingsSsh';
import ManagedService from './model/ManagedService';
import MigrateLinodeInstanceRequest from './model/MigrateLinodeInstanceRequest';
import MutateLinodeInstanceRequest from './model/MutateLinodeInstanceRequest';
import NodeBalancer from './model/NodeBalancer';
import NodeBalancerConfig from './model/NodeBalancerConfig';
import NodeBalancerConfigNodesStatus from './model/NodeBalancerConfigNodesStatus';
import NodeBalancerNode from './model/NodeBalancerNode';
import NodeBalancerStats from './model/NodeBalancerStats';
import NodeBalancerStatsData from './model/NodeBalancerStatsData';
import NodeBalancerStatsDataTraffic from './model/NodeBalancerStatsDataTraffic';
import NodeBalancerTransfer from './model/NodeBalancerTransfer';
import Notification from './model/Notification';
import NotificationEntity from './model/NotificationEntity';
import OAuthClient from './model/OAuthClient';
import ObjectStorageBucket from './model/ObjectStorageBucket';
import ObjectStorageCluster from './model/ObjectStorageCluster';
import ObjectStorageKey from './model/ObjectStorageKey';
import ObjectStorageKeyBucketAccessInner from './model/ObjectStorageKeyBucketAccessInner';
import ObjectStorageObject from './model/ObjectStorageObject';
import ObjectStorageSSL from './model/ObjectStorageSSL';
import ObjectStorageSSLResponse from './model/ObjectStorageSSLResponse';
import PaginationEnvelope from './model/PaginationEnvelope';
import PayPal from './model/PayPal';
import PayPalData from './model/PayPalData';
import PayPalExecute from './model/PayPalExecute';
import Payment from './model/Payment';
import PaymentMethod from './model/PaymentMethod';
import PaymentMethodData from './model/PaymentMethodData';
import PaymentRequest from './model/PaymentRequest';
import PersonalAccessToken from './model/PersonalAccessToken';
import PostIPv6Range200Response from './model/PostIPv6Range200Response';
import PostIPv6RangeRequest from './model/PostIPv6RangeRequest';
import PostLKEClusterRegenerateRequest from './model/PostLKEClusterRegenerateRequest';
import PostProfilePhoneNumberRequest from './model/PostProfilePhoneNumberRequest';
import PostProfilePhoneNumberVerifyRequest from './model/PostProfilePhoneNumberVerifyRequest';
import Profile from './model/Profile';
import ProfileReferrals from './model/ProfileReferrals';
import Promotion from './model/Promotion';
import PutDatabasesMongoDBInstanceRequest from './model/PutDatabasesMongoDBInstanceRequest';
import PutDatabasesMySQLInstanceRequest from './model/PutDatabasesMySQLInstanceRequest';
import PutDatabasesPostgreSQLInstanceRequest from './model/PutDatabasesPostgreSQLInstanceRequest';
import PutLKECluster200Response from './model/PutLKECluster200Response';
import PutLKEClusterRequest from './model/PutLKEClusterRequest';
import PutLKEClusterRequestControlPlane from './model/PutLKEClusterRequestControlPlane';
import PutLKENodePoolRequest from './model/PutLKENodePoolRequest';
import RebootLinodeInstanceRequest from './model/RebootLinodeInstanceRequest';
import RebuildNodeBalancerConfigRequest from './model/RebuildNodeBalancerConfigRequest';
import RebuildNodeBalancerConfigRequestAllOfNodesInner from './model/RebuildNodeBalancerConfigRequestAllOfNodesInner';
import Region from './model/Region';
import RegionResolvers from './model/RegionResolvers';
import RescueDevices from './model/RescueDevices';
import RescueLinodeInstanceRequest from './model/RescueLinodeInstanceRequest';
import ResetDiskPasswordRequest from './model/ResetDiskPasswordRequest';
import ResetLinodePasswordRequest from './model/ResetLinodePasswordRequest';
import ResizeDiskRequest from './model/ResizeDiskRequest';
import ResizeLinodeInstanceRequest from './model/ResizeLinodeInstanceRequest';
import ResizeVolumeRequest from './model/ResizeVolumeRequest';
import RestoreBackupRequest from './model/RestoreBackupRequest';
import SSHKey from './model/SSHKey';
import SecurityQuestion from './model/SecurityQuestion';
import SecurityQuestionsGet from './model/SecurityQuestionsGet';
import SecurityQuestionsGetSecurityQuestionsInner from './model/SecurityQuestionsGetSecurityQuestionsInner';
import SecurityQuestionsPost from './model/SecurityQuestionsPost';
import SecurityQuestionsPostSecurityQuestionsInner from './model/SecurityQuestionsPostSecurityQuestionsInner';
import ServiceTransfer from './model/ServiceTransfer';
import ServiceTransferEntities from './model/ServiceTransferEntities';
import StackScript from './model/StackScript';
import StatsData from './model/StatsData';
import StatsDataAvailable from './model/StatsDataAvailable';
import SupportTicket from './model/SupportTicket';
import SupportTicketEntity from './model/SupportTicketEntity';
import SupportTicketReply from './model/SupportTicketReply';
import SupportTicketRequest from './model/SupportTicketRequest';
import Tag from './model/Tag';
import TfaConfirm200Response from './model/TfaConfirm200Response';
import TfaConfirmRequest from './model/TfaConfirmRequest';
import TfaEnable200Response from './model/TfaEnable200Response';
import Transfer from './model/Transfer';
import TrustedDevice from './model/TrustedDevice';
import UpdateDomainRecordRequest from './model/UpdateDomainRecordRequest';
import UpdateFirewallRequest from './model/UpdateFirewallRequest';
import UpdateIPRequest from './model/UpdateIPRequest';
import UpdateLinodeIPRequest from './model/UpdateLinodeIPRequest';
import UpdateManagedCredentialUsernamePasswordRequest from './model/UpdateManagedCredentialUsernamePasswordRequest';
import UpdateObjectStorageBucketACLRequest from './model/UpdateObjectStorageBucketACLRequest';
import UpdateObjectStorageBucketAccessRequest from './model/UpdateObjectStorageBucketAccessRequest';
import UpdateObjectStorageKeyRequest from './model/UpdateObjectStorageKeyRequest';
import UpdateSSHKeyRequest from './model/UpdateSSHKeyRequest';
import UpdateVolumeRequest from './model/UpdateVolumeRequest';
import User from './model/User';
import UserDefinedField from './model/UserDefinedField';
import ViewManagedSSHKey200Response from './model/ViewManagedSSHKey200Response';
import ViewObjectStorageBucketACL200Response from './model/ViewObjectStorageBucketACL200Response';
import Vlans from './model/Vlans';
import Volume from './model/Volume';
import WarningObject from './model/WarningObject';
import AccountApi from './api/AccountApi';
import DatabasesApi from './api/DatabasesApi';
import DomainsApi from './api/DomainsApi';
import ImagesApi from './api/ImagesApi';
import LinodeInstancesApi from './api/LinodeInstancesApi';
import LinodeKubernetesEngineLKEApi from './api/LinodeKubernetesEngineLKEApi';
import LinodeTypesApi from './api/LinodeTypesApi';
import LongviewApi from './api/LongviewApi';
import ManagedApi from './api/ManagedApi';
import NetworkingApi from './api/NetworkingApi';
import NodeBalancersApi from './api/NodeBalancersApi';
import ObjectStorageApi from './api/ObjectStorageApi';
import ProfileApi from './api/ProfileApi';
import RegionsApi from './api/RegionsApi';
import StackScriptsApi from './api/StackScriptsApi';
import SupportApi from './api/SupportApi';
import TagsApi from './api/TagsApi';
import VolumesApi from './api/VolumesApi';


/**
* ## Introduction The Linode API provides the ability to programmatically manage the full range of Linode products and services.  This reference is designed to assist application developers and system administrators.  Each endpoint includes descriptions, request syntax, and examples using standard HTTP requests. Response data is returned in JSON format.   This document was generated from our OpenAPI Specification.  See the &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://www.openapis.org\&quot;&gt;OpenAPI website&lt;/a&gt; for more information.  &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;/docs/api/openapi.yaml\&quot;&gt;Download the Linode OpenAPI Specification&lt;/a&gt;.   ## Changelog  &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;/docs/products/tools/api/release-notes/\&quot;&gt;View our Changelog&lt;/a&gt; to see release notes on all changes made to our API.  ## Access and Authentication  Some endpoints are publicly accessible without requiring authentication. All endpoints affecting your Account, however, require either a Personal Access Token or OAuth authentication (when using third-party applications).  ### Personal Access Token  The easiest way to access the API is with a Personal Access Token (PAT) generated from the &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://cloud.linode.com/profile/tokens\&quot;&gt;Linode Cloud Manager&lt;/a&gt; or the [Create Personal Access Token](/docs/api/profile/#personal-access-token-create) endpoint.  All scopes for the OAuth security model ([defined below](/docs/api/#oauth)) apply to this security model as well.  ### Authentication  | Security Scheme Type: | HTTP | |-----------------------|------| | **HTTP Authorization Scheme** | bearer |  ## OAuth  If you only need to access the Linode API for personal use, we recommend that you create a [personal access token](/docs/api/#personal-access-token). If you&#39;re designing an application that can authenticate with an arbitrary Linode user, then you should use the OAuth 2.0 workflows presented in this section.  For a more detailed example of an OAuth 2.0 implementation, see our guide on [How to Create an OAuth App with the Linode Python API Library](/docs/products/tools/api/guides/create-an-oauth-app-with-the-python-api-library/#oauth-2-authentication-exchange).  Before you implement OAuth in your application, you first need to create an OAuth client. You can do this [with the Linode API](/docs/api/account/#oauth-client-create) or [via the Cloud Manager](https://cloud.linode.com/profile/clients):    - When creating the client, you&#39;ll supply a &#x60;label&#x60; and a &#x60;redirect_uri&#x60; (referred to as the Callback URL in the Cloud Manager).   - The response from this endpoint will give you a &#x60;client_id&#x60; and a &#x60;secret&#x60;.   - Clients can be public or private, and are private by default. You can choose to make the client public when it is created.     - A private client is used with applications which can securely store the client secret (that is, the secret returned to you when you first created the client). For example, an application running on a secured server that only the developer has access to would use a private OAuth client. This is also called a confidential client in some OAuth documentation.     - A public client is used with applications where the client secret is not guaranteed to be secure. For example, a native app running on a user&#39;s computer may not be able to keep the client secret safe, as a user could potentially inspect the source of the application. So, native apps or apps that run in a user&#39;s browser should use a public client.     - Public and private clients follow different workflows, as described below.  ### OAuth Workflow  The OAuth workflow is a series of exchanges between your third-party app and Linode. The workflow is used to authenticate a user before an application can start making API calls on the user&#39;s behalf.  Notes:  - With respect to the diagram in [section 1.2 of RFC 6749](https://tools.ietf.org/html/rfc6749#section-1.2), login.linode.com (referred to in this section as the *login server*) is the Resource Owner and the Authorization Server; api.linode.com (referred to here as the *api server*) is the Resource Server. - The OAuth spec refers to the private and public workflows listed below as the [authorization code flow](https://tools.ietf.org/html/rfc6749#section-1.3.1) and [implicit flow](https://tools.ietf.org/html/rfc6749#section-1.3.2).  | PRIVATE WORKFLOW | PUBLIC WORKFLOW | |------------------|------------------| | 1.  The user visits the application&#39;s website and is directed to login with Linode. | 1.  The user visits the application&#39;s website and is directed to login with Linode. | | 2.  Your application then redirects the user to Linode&#39;s [login server](https://login.linode.com) with the client application&#39;s &#x60;client_id&#x60; and requested OAuth &#x60;scope&#x60;, which should appear in the URL of the login page. | 2.  Your application then redirects the user to Linode&#39;s [login server](https://login.linode.com) with the client application&#39;s &#x60;client_id&#x60; and requested OAuth &#x60;scope&#x60;, which should appear in the URL of the login page. | | 3.  The user logs into the login server with their username and password. | 3.  The user logs into the login server with their username and password. | | 4.  The login server redirects the user to the specificed redirect URL with a temporary authorization &#x60;code&#x60; (exchange code) in the URL. | 4.  The login server redirects the user back to your application with an OAuth &#x60;access_token&#x60; embedded in the redirect URL&#39;s hash. This is temporary and expires in two hours. No &#x60;refresh_token&#x60; is issued. Therefore, once the &#x60;access_token&#x60; expires, a new one will need to be issued by having the user log in again. | | 5.  The application issues a POST request (*see additional details below*) to the login server with the exchange code, &#x60;client_id&#x60;, and the client application&#39;s &#x60;client_secret&#x60;. | | | 6.  The login server responds to the client application with a new OAuth &#x60;access_token&#x60; and &#x60;refresh_token&#x60;. The &#x60;access_token&#x60; is set to expire in two hours. | | | 7.  The &#x60;refresh_token&#x60; can be used by contacting the login server with the &#x60;client_id&#x60;, &#x60;client_secret&#x60;, &#x60;grant_type&#x60;, and &#x60;refresh_token&#x60; to get a new OAuth &#x60;access_token&#x60; and &#x60;refresh_token&#x60;. The new &#x60;access_token&#x60; is good for another two hours, and the new &#x60;refresh_token&#x60; can be used to extend the session again by this same method (*see additional details below*). | |  #### OAuth Private Workflow - Additional Details  The following information expands on steps 5 through 7 of the private workflow:  Once the user has logged into Linode and you have received an exchange code, you will need to trade that exchange code for an &#x60;access_token&#x60; and &#x60;refresh_token&#x60;. You do this by making an HTTP POST request to the following address:  &#x60;&#x60;&#x60; https://login.linode.com/oauth/token &#x60;&#x60;&#x60;  Make this request as &#x60;application/x-www-form-urlencoded&#x60; or as &#x60;multipart/form-data&#x60; and include the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | client_id | Your app&#39;s client ID. | | client_secret | Your app&#39;s client secret. | | code | The code you just received from the redirect. |  You&#39;ll get a response like this:  &#x60;&#x60;&#x60;json {   \&quot;scope\&quot;: \&quot;linodes:read_write\&quot;,   \&quot;access_token\&quot;: \&quot;03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c\&quot;,   \&quot;refresh_token\&quot;: \&quot;f2ec9712e616fdb5a2a21aa0e88cfadea7502ebc62cf5bd758dbcd65e1803bad\&quot;,   \&quot;token_type\&quot;: \&quot;bearer\&quot;,   \&quot;expires_in\&quot;: 7200 } &#x60;&#x60;&#x60;  Included in the response is an &#x60;access_token&#x60;. With this token, you can proceed to make authenticated HTTP requests to the API by adding this header to each request:  &#x60;&#x60;&#x60; Authorization: Bearer 03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c &#x60;&#x60;&#x60;  This &#x60;access_token&#x60; is set to expire in two hours. To refresh access prior to expiration, make another request to the same URL with the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | grant_type | The grant type you&#39;re using. Use \&quot;refresh_token\&quot; when refreshing access. | | client_id | Your app&#39;s client ID. | | client_secret | Your app&#39;s client secret. | | refresh_token | The &#x60;refresh_token&#x60; received from the previous response. |  You&#39;ll get another response with an updated &#x60;access_token&#x60; and &#x60;refresh_token&#x60;, which can then be used to refresh access again.  ### OAuth Reference  | Security Scheme Type | OAuth 2.0 | |-----------------------|--------| | **Authorization URL** | &#x60;https://login.linode.com/oauth/authorize&#x60; | | **Token URL** | &#x60;https://login.linode.com/oauth/token&#x60; | | **Scopes** | &lt;ul&gt;&lt;li&gt;&#x60;account:read_only&#x60; - Allows access to GET information about your Account.&lt;/li&gt;&lt;li&gt;&#x60;account:read_write&#x60; - Allows access to all endpoints related to your Account.&lt;/li&gt;&lt;li&gt;&#x60;databases:read_only&#x60; - Allows access to GET Managed Databases on your Account.&lt;/li&gt;&lt;li&gt;&#x60;databases:read_write&#x60; - Allows access to all endpoints related to your Managed Databases.&lt;/li&gt;&lt;li&gt;&#x60;domains:read_only&#x60; - Allows access to GET Domains on your Account.&lt;/li&gt;&lt;li&gt;&#x60;domains:read_write&#x60; - Allows access to all Domain endpoints.&lt;/li&gt;&lt;li&gt;&#x60;events:read_only&#x60; - Allows access to GET your Events.&lt;/li&gt;&lt;li&gt;&#x60;events:read_write&#x60; - Allows access to all endpoints related to your Events.&lt;/li&gt;&lt;li&gt;&#x60;firewall:read_only&#x60; - Allows access to GET information about your Firewalls.&lt;/li&gt;&lt;li&gt;&#x60;firewall:read_write&#x60; - Allows access to all Firewall endpoints.&lt;/li&gt;&lt;li&gt;&#x60;images:read_only&#x60; - Allows access to GET your Images.&lt;/li&gt;&lt;li&gt;&#x60;images:read_write&#x60; - Allows access to all endpoints related to your Images.&lt;/li&gt;&lt;li&gt;&#x60;ips:read_only&#x60; - Allows access to GET your ips.&lt;/li&gt;&lt;li&gt;&#x60;ips:read_write&#x60; - Allows access to all endpoints related to your ips.&lt;/li&gt;&lt;li&gt;&#x60;linodes:read_only&#x60; - Allows access to GET Linodes on your Account.&lt;/li&gt;&lt;li&gt;&#x60;linodes:read_write&#x60; - Allow access to all endpoints related to your Linodes.&lt;/li&gt;&lt;li&gt;&#x60;lke:read_only&#x60; - Allows access to GET LKE Clusters on your Account.&lt;/li&gt;&lt;li&gt;&#x60;lke:read_write&#x60; - Allows access to all endpoints related to LKE Clusters on your Account.&lt;/li&gt;&lt;li&gt;&#x60;longview:read_only&#x60; - Allows access to GET your Longview Clients.&lt;/li&gt;&lt;li&gt;&#x60;longview:read_write&#x60; - Allows access to all endpoints related to your Longview Clients.&lt;/li&gt;&lt;li&gt;&#x60;nodebalancers:read_only&#x60; - Allows access to GET NodeBalancers on your Account.&lt;/li&gt;&lt;li&gt;&#x60;nodebalancers:read_write&#x60; - Allows access to all NodeBalancer endpoints.&lt;/li&gt;&lt;li&gt;&#x60;object_storage:read_only&#x60; - Allows access to GET information related to your Object Storage.&lt;/li&gt;&lt;li&gt;&#x60;object_storage:read_write&#x60; - Allows access to all Object Storage endpoints.&lt;/li&gt;&lt;li&gt;&#x60;stackscripts:read_only&#x60; - Allows access to GET your StackScripts.&lt;/li&gt;&lt;li&gt;&#x60;stackscripts:read_write&#x60; - Allows access to all endpoints related to your StackScripts.&lt;/li&gt;&lt;li&gt;&#x60;volumes:read_only&#x60; - Allows access to GET your Volumes.&lt;/li&gt;&lt;li&gt;&#x60;volumes:read_write&#x60; - Allows access to all endpoints related to your Volumes.&lt;/li&gt;&lt;/ul&gt;&lt;br/&gt;|  ## Requests  Requests must be made over HTTPS to ensure transactions are encrypted. Data included in requests must be supplied in json format unless otherwise specified in the command description.  The following request methods are supported:  | METHOD  | USAGE | |---------|-------| | GET     | Retrieves data about collections and individual resources. | | POST    | For collections, creates a new resource of that type. Also used to perform actions on action endpoints. | | PUT     | Updates an existing resource. | | DELETE  | Deletes a resource. This is a destructive action. | | HEAD    | Returns only the response header information of a GET request | | OPTIONS | Provides permitted communication options for a command |  ## Responses  ### Response Status Codes  Actions will return one of the following HTTP response status codes:  | STATUS  | DESCRIPTION | |---------|-------------| | 200 OK  | The request was successful. | | 202 Accepted | The request was successful, but processing has not been completed. The response body includes a \&quot;warnings\&quot; array containing the details of incomplete processes. | | 204 No Content | The server successfully fulfilled the request and there is no additional content to send. | | 299 Deprecated | The request was successful, but involved a deprecated endpoint. The response body includes a \&quot;warnings\&quot; array containing warning messages. | | 400 Bad Request | You submitted an invalid request (missing parameters, etc.). | | 401 Unauthorized | You failed to authenticate for this resource. | | 403 Forbidden | You are authenticated, but don&#39;t have permission to do this. | | 404 Not Found | The resource you&#39;re requesting does not exist. | | 429 Too Many Requests | You&#39;ve hit a rate limit. | | 500 Internal Server Error | Please [open a Support Ticket](/docs/api/support/#support-ticket-open). |  ### Response Headers  There are many ways to access response header information for individual command URLs, depending on how you are accessing the Linode API. For example, to view HTTP response headers for the &#x60;/regions&#x60; endpoint when making requests with &#x60;curl&#x60;, use the &#x60;-I&#x60; or &#x60;--head&#x60; option as follows:  &#x60;&#x60;&#x60;Shell curl -I https://api.linode.com/v4/regions &#x60;&#x60;&#x60;  Responses may include the following headers:  | HEADER | DESCRIPTION | EXAMPLE | |--------|-------------|---------| | Access-Control-Allow-Credentials | Responses to credentialed requests are exposed to frontend JavaScript code. | true | | Access-Control-Allow-Headers | All permissible request headers for this endpoint. | Authorization, Origin, X-Requested-With, Content-Type, Accept, X-Filter | | Access-Control-Allow-Methods | Permissible HTTP methods for this endpoint | HEAD, GET, OPTIONS, POST, PUT, DELETE | | Access-Control-Allow-Origin | Indicates origin access permissions. The wildcard character &#x60;*&#x60; means any origin can access the resource. | * | | Access-Control-Expose-Headers | Available headers to include in response to cross-origin requests. | X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Status | | Cache-Control | Controls caching in browsers and shared caches such as CDNs. | private, max-age&#x3D;60, s-maxage&#x3D;60 | | Content-Security-Policy | Controls which resources are allowed to load. By default, resources do not load. | default-src &#39;none&#39; | | Content-Type | All responses are in json format. | application/json | | Content-Warning | A message containing instructions for successful requests that were not able to be completed. | Please contact support for assistance. | | Retry-After | The remaining time in seconds until the current [rate limit](#rate-limiting) window resets. | 60 | | Strict-Transport-Security | Enforces HTTPS-only access until the returned time in seconds. | max-age&#x3D;31536000 | | Vary | Optional request headers that affected the response content. | Authorization, X-Filter | | X-Accepted-OAuth-Scopes | Required [scopes](#oauth-reference) for accessing the requested command. | linodes:read_only | | X-Customer-UUID | A unique identifier for the account owning the the [personal access token](#personal-access-token) that was used for the request. | ABCDEF01-3456-789A-BCDEF0123456789A | | X-OAuth-Scopes | Allowed [scopes](#oauth-reference) associated with the [personal access token](#personal-access-token) that was used for the request. A value of &#x60;*&#x60; indicates read/write access for all scope categories. | images:read_write linodes:read_only | | X-RateLimit-Limit | The maximum number of permitted requests during the [rate limit](#rate-limiting) window for this endpoint. | 800 | | X-RateLimit-Remaining | The remaining number of permitted requests in the current [rate limit](#rate-limiting) window. | 798 | | X-RateLimit-Reset | The time when the current [rate limit](#rate-limiting) window rests in UTC epoch seconds. | 1674747739 | | X-Spec-Version | The current API version that handled the request. | 4.150.0 |  ## Errors  Success is indicated via &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/List_of_HTTP_status_codes\&quot; target&#x3D;\&quot;_top\&quot;&gt;Standard HTTP status codes&lt;/a&gt;. &#x60;2xx&#x60; codes indicate success, &#x60;4xx&#x60; codes indicate a request error, and &#x60;5xx&#x60; errors indicate a server error. A request error might be an invalid input, a required parameter being omitted, or a malformed request. A server error means something went wrong processing your request. If this occurs, please [open a Support Ticket](/docs/api/support/#support-ticket-open) and let us know. Though errors are logged and we work quickly to resolve issues, opening a ticket and providing us with reproducable steps and data is always helpful.  The &#x60;errors&#x60; field is an array of the things that went wrong with your request. We will try to include as many of the problems in the response as possible, but it&#39;s conceivable that fixing these errors and resubmitting may result in new errors coming back once we are able to get further along in the process of handling your request.  Within each error object, the &#x60;field&#x60; parameter will be included if the error pertains to a specific field in the JSON you&#39;ve submitted. This will be omitted if there is no relevant field. The &#x60;reason&#x60; is a human-readable explanation of the error, and will always be included.  ## Pagination  Resource lists are always paginated. The response will look similar to this:  &#x60;&#x60;&#x60;json {     \&quot;data\&quot;: [ ... ],     \&quot;page\&quot;: 1,     \&quot;pages\&quot;: 3,     \&quot;results\&quot;: 300 } &#x60;&#x60;&#x60;  * Pages start at 1. You may retrieve a specific page of results by adding &#x60;?page&#x3D;x&#x60; to your URL (for example, &#x60;?page&#x3D;4&#x60;). If the value of &#x60;page&#x60; exceeds &#x60;2^64/page_size&#x60;, the last possible page will be returned.   * Page sizes default to 100, and can be set to return between 25 and 500. Page size can be set using &#x60;?page_size&#x3D;x&#x60;.  ## Filtering and Sorting  Collections are searchable by fields they include, marked in the spec as &#x60;x-linode-filterable: true&#x60;. Filters are passed in the &#x60;X-Filter&#x60; header and are formatted as JSON objects. Here is a request call for Linode Types in our \&quot;standard\&quot; class:  &#x60;&#x60;&#x60;Shell curl \&quot;https://api.linode.com/v4/linode/types\&quot; \\   -H &#39;X-Filter: { \&quot;class\&quot;: \&quot;standard\&quot; }&#39; &#x60;&#x60;&#x60;  The filter object&#39;s keys are the keys of the object you&#39;re filtering, and the values are accepted values. You can add multiple filters by including more than one key. For example, filtering for \&quot;standard\&quot; Linode Types that offer one vcpu:  &#x60;&#x60;&#x60;Shell  curl \&quot;https://api.linode.com/v4/linode/types\&quot; \\   -H &#39;X-Filter: { \&quot;class\&quot;: \&quot;standard\&quot;, \&quot;vcpus\&quot;: 1 }&#39; &#x60;&#x60;&#x60;  In the above example, both filters are combined with an \&quot;and\&quot; operation. However, if you wanted either Types with one vcpu or Types in our \&quot;standard\&quot; class, you can add an operator:   &#x60;&#x60;&#x60;Shell curl \&quot;https://api.linode.com/v4/linode/types\&quot; \\   -H &#39;X-Filter: { \&quot;+or\&quot;: [ { \&quot;vcpus\&quot;: 1 }, { \&quot;class\&quot;: \&quot;standard\&quot; } ] }&#39; &#x60;&#x60;&#x60;  Each filter in the &#x60;+or&#x60; array is its own filter object, and all conditions in it are combined with an \&quot;and\&quot; operation as they were in the previous example.  Other operators are also available. Operators are keys of a Filter JSON object. Their value must be of the appropriate type, and they are evaluated as described below:  | OPERATOR | TYPE   | DESCRIPTION                       | |----------|--------|-----------------------------------| | +and     | array  | All conditions must be true.       | | +or      | array  | One condition must be true.        | | +gt      | number | Value must be greater than number. | | +gte     | number | Value must be greater than or equal to number. | | +lt      | number | Value must be less than number. | | +lte     | number | Value must be less than or equal to number. | | +contains | string | Given string must be in the value. | | +neq      | string | Does not equal the value.          | | +order_by | string | Attribute to order the results by - must be filterable. | | +order    | string | Either \&quot;asc\&quot; or \&quot;desc\&quot;. Defaults to \&quot;asc\&quot;. Requires &#x60;+order_by&#x60;. |  For example, filtering for [Linode Types](/docs/api/linode-types/) that offer memory equal to or higher than 61440:  &#x60;&#x60;&#x60;Shell curl \&quot;https://api.linode.com/v4/linode/types\&quot; \\   -H &#39;     X-Filter: {       \&quot;memory\&quot;: {         \&quot;+gte\&quot;: 61440       }     }&#39; &#x60;&#x60;&#x60;  You can combine and nest operators to construct arbitrarily-complex queries. For example, give me all [Linode Types](/docs/api/linode-types/) which are either &#x60;standard&#x60; or &#x60;highmem&#x60; class, or have between 12 and 20 vcpus:  &#x60;&#x60;&#x60;Shell curl \&quot;https://api.linode.com/v4/linode/types\&quot; \\   -H &#39;     X-Filter: {       \&quot;+or\&quot;: [         {           \&quot;+or\&quot;: [             {               \&quot;class\&quot;: \&quot;standard\&quot;             },             {               \&quot;class\&quot;: \&quot;highmem\&quot;             }           ]         },         {           \&quot;+and\&quot;: [             {               \&quot;vcpus\&quot;: {                 \&quot;+gte\&quot;: 12               }             },             {               \&quot;vcpus\&quot;: {                 \&quot;+lte\&quot;: 20               }             }           ]         }       ]     }&#39; &#x60;&#x60;&#x60; ## Time Values  All times returned by the API are in UTC, regardless of the timezone configured within your user&#39;s profile (see &#x60;timezone&#x60; property within [Profile View](/docs/api/profile/#profile-view__responses)).  ## Rate Limiting  Rate limits on API requests help maintain the health and stability of the Linode API. Accordingly, every endpoint of the Linode API applies a rate limit on a per user basis as determined by OAuth token for authenticated requests or IP address for public endpoints.  Each rate limit consists of a total number of requests and a time window. For example, if an endpoint has a rate limit of 800 requests per minute, then up to 800 requests over a one minute window are permitted. Subsequent requests to an endpoint after hitting a rate limit return a 429 error. You can successfully remake requests to that endpoint after the rate limit window resets.  ### Linode APIv4 Rate Limits  With the Linode API, you can generally make up to 1,600 general API requests every two minutes. Additionally, all endpoints have a rate limit of 800 requests per minute unless otherwise specified below.  **Note:** There may be rate limiting applied at other levels outside of the API, for example, at the load balancer.  Creating Linodes has a dedicated rate limit of 10 requests per 30 seconds. That endpoint is:  * [Linode Create](/docs/api/linode-instances/#linode-create)  &#x60;/stats&#x60; endpoints have their own dedicated rate limits of 100 requests per minute. These endpoints are:  * [View Linode Statistics](/docs/api/linode-instances/#linode-statistics-view) * [View Linode Statistics (year/month)](/docs/api/linode-instances/#statistics-yearmonth-view) * [View NodeBalancer Statistics](/docs/api/nodebalancers/#nodebalancer-statistics-view) * [List Managed Stats](/docs/api/managed/#managed-stats-list)  Object Storage endpoints have a dedicated rate limit of 750 requests per second. The Object Storage endpoints are:  * [Object Storage Endpoints](/docs/api/object-storage/)  Opening Support Tickets has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Open Support Ticket](/docs/api/support/#support-ticket-open)  Accepting Service Transfers has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Service Transfer Accept](/docs/api/account/#service-transfer-accept)  ### Rate Limit HTTP Response Headers  The Linode API includes the following HTTP response headers which are designed to help you avoid hitting rate limits which might disrupt your applications:  * **X-RateLimit-Limit**: The maximum number of permitted requests during the rate limit window for this endpoint. * **X-RateLimit-Remaining**: The remaining number of permitted requests in the current rate limit window. * **X-RateLimit-Reset**: The time when the current rate limit window rests in UTC epoch seconds. * **Retry-After**: The remaining time in seconds until the current rate limit window resets.  ## CLI (Command Line Interface)  The &lt;a href&#x3D;\&quot;https://github.com/linode/linode-cli\&quot; target&#x3D;\&quot;_top\&quot;&gt;Linode CLI&lt;/a&gt; allows you to easily work with the API using intuitive and simple syntax. It requires a [Personal Access Token](/docs/api/#personal-access-token) for authentication, and gives you access to all of the features and functionality of the Linode API that are documented here with CLI examples.  Endpoints that do not have CLI examples are currently unavailable through the CLI, but can be accessed via other methods such as Shell commands and other third-party applications. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var LinodeApi = require('index'); // See note below*.
* var xxxSvc = new LinodeApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new LinodeApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new LinodeApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new LinodeApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 4.151.1
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
     * The AccountCreditCard model constructor.
     * @property {module:model/AccountCreditCard}
     */
    AccountCreditCard,

    /**
     * The AccountSettings model constructor.
     * @property {module:model/AccountSettings}
     */
    AccountSettings,

    /**
     * The AddLinodeIPRequest model constructor.
     * @property {module:model/AddLinodeIPRequest}
     */
    AddLinodeIPRequest,

    /**
     * The AllocateIPRequest model constructor.
     * @property {module:model/AllocateIPRequest}
     */
    AllocateIPRequest,

    /**
     * The AttachVolumeRequest model constructor.
     * @property {module:model/AttachVolumeRequest}
     */
    AttachVolumeRequest,

    /**
     * The AuthorizedApp model constructor.
     * @property {module:model/AuthorizedApp}
     */
    AuthorizedApp,

    /**
     * The Backup model constructor.
     * @property {module:model/Backup}
     */
    Backup,

    /**
     * The BackupDisksInner model constructor.
     * @property {module:model/BackupDisksInner}
     */
    BackupDisksInner,

    /**
     * The BootLinodeInstanceRequest model constructor.
     * @property {module:model/BootLinodeInstanceRequest}
     */
    BootLinodeInstanceRequest,

    /**
     * The CancelAccount200Response model constructor.
     * @property {module:model/CancelAccount200Response}
     */
    CancelAccount200Response,

    /**
     * The CancelAccount409Response model constructor.
     * @property {module:model/CancelAccount409Response}
     */
    CancelAccount409Response,

    /**
     * The CancelAccount409ResponseErrorsInner model constructor.
     * @property {module:model/CancelAccount409ResponseErrorsInner}
     */
    CancelAccount409ResponseErrorsInner,

    /**
     * The CancelAccountRequest model constructor.
     * @property {module:model/CancelAccountRequest}
     */
    CancelAccountRequest,

    /**
     * The CloneDomainRequest model constructor.
     * @property {module:model/CloneDomainRequest}
     */
    CloneDomainRequest,

    /**
     * The CloneLinodeInstanceRequest model constructor.
     * @property {module:model/CloneLinodeInstanceRequest}
     */
    CloneLinodeInstanceRequest,

    /**
     * The CloneVolumeRequest model constructor.
     * @property {module:model/CloneVolumeRequest}
     */
    CloneVolumeRequest,

    /**
     * The CreateEntityTransferRequest model constructor.
     * @property {module:model/CreateEntityTransferRequest}
     */
    CreateEntityTransferRequest,

    /**
     * The CreateFirewallsRequest model constructor.
     * @property {module:model/CreateFirewallsRequest}
     */
    CreateFirewallsRequest,

    /**
     * The CreateFirewallsRequestDevices model constructor.
     * @property {module:model/CreateFirewallsRequestDevices}
     */
    CreateFirewallsRequestDevices,

    /**
     * The CreateFirewallsRequestRules model constructor.
     * @property {module:model/CreateFirewallsRequestRules}
     */
    CreateFirewallsRequestRules,

    /**
     * The CreateImageRequest model constructor.
     * @property {module:model/CreateImageRequest}
     */
    CreateImageRequest,

    /**
     * The CreateLKEClusterRequest model constructor.
     * @property {module:model/CreateLKEClusterRequest}
     */
    CreateLKEClusterRequest,

    /**
     * The CreateLKEClusterRequestControlPlane model constructor.
     * @property {module:model/CreateLKEClusterRequestControlPlane}
     */
    CreateLKEClusterRequestControlPlane,

    /**
     * The CreateLinodeInstanceRequest model constructor.
     * @property {module:model/CreateLinodeInstanceRequest}
     */
    CreateLinodeInstanceRequest,

    /**
     * The CreateManagedCredentialRequest model constructor.
     * @property {module:model/CreateManagedCredentialRequest}
     */
    CreateManagedCredentialRequest,

    /**
     * The CreateNodeBalancerRequest model constructor.
     * @property {module:model/CreateNodeBalancerRequest}
     */
    CreateNodeBalancerRequest,

    /**
     * The CreateNodeBalancerRequestConfigsInner model constructor.
     * @property {module:model/CreateNodeBalancerRequestConfigsInner}
     */
    CreateNodeBalancerRequestConfigsInner,

    /**
     * The CreateObjectStorageBucketRequest model constructor.
     * @property {module:model/CreateObjectStorageBucketRequest}
     */
    CreateObjectStorageBucketRequest,

    /**
     * The CreateObjectStorageObjectURL200Response model constructor.
     * @property {module:model/CreateObjectStorageObjectURL200Response}
     */
    CreateObjectStorageObjectURL200Response,

    /**
     * The CreateObjectStorageObjectURLRequest model constructor.
     * @property {module:model/CreateObjectStorageObjectURLRequest}
     */
    CreateObjectStorageObjectURLRequest,

    /**
     * The CreatePayPalPayment200Response model constructor.
     * @property {module:model/CreatePayPalPayment200Response}
     */
    CreatePayPalPayment200Response,

    /**
     * The CreatePayment202Response model constructor.
     * @property {module:model/CreatePayment202Response}
     */
    CreatePayment202Response,

    /**
     * The CreatePaymentMethodRequest model constructor.
     * @property {module:model/CreatePaymentMethodRequest}
     */
    CreatePaymentMethodRequest,

    /**
     * The CreatePersonalAccessTokenRequest model constructor.
     * @property {module:model/CreatePersonalAccessTokenRequest}
     */
    CreatePersonalAccessTokenRequest,

    /**
     * The CreatePromoCreditRequest model constructor.
     * @property {module:model/CreatePromoCreditRequest}
     */
    CreatePromoCreditRequest,

    /**
     * The CreateServiceTransferRequest model constructor.
     * @property {module:model/CreateServiceTransferRequest}
     */
    CreateServiceTransferRequest,

    /**
     * The CreateSnapshotRequest model constructor.
     * @property {module:model/CreateSnapshotRequest}
     */
    CreateSnapshotRequest,

    /**
     * The CreateTagRequest model constructor.
     * @property {module:model/CreateTagRequest}
     */
    CreateTagRequest,

    /**
     * The CreateTicketReplyRequest model constructor.
     * @property {module:model/CreateTicketReplyRequest}
     */
    CreateTicketReplyRequest,

    /**
     * The CreateVolumeRequest model constructor.
     * @property {module:model/CreateVolumeRequest}
     */
    CreateVolumeRequest,

    /**
     * The CreditCard model constructor.
     * @property {module:model/CreditCard}
     */
    CreditCard,

    /**
     * The CreditCardData model constructor.
     * @property {module:model/CreditCardData}
     */
    CreditCardData,

    /**
     * The Database model constructor.
     * @property {module:model/Database}
     */
    Database,

    /**
     * The DatabaseBackup model constructor.
     * @property {module:model/DatabaseBackup}
     */
    DatabaseBackup,

    /**
     * The DatabaseBackupSnapshot model constructor.
     * @property {module:model/DatabaseBackupSnapshot}
     */
    DatabaseBackupSnapshot,

    /**
     * The DatabaseCredentials model constructor.
     * @property {module:model/DatabaseCredentials}
     */
    DatabaseCredentials,

    /**
     * The DatabaseEngine model constructor.
     * @property {module:model/DatabaseEngine}
     */
    DatabaseEngine,

    /**
     * The DatabaseHosts model constructor.
     * @property {module:model/DatabaseHosts}
     */
    DatabaseHosts,

    /**
     * The DatabaseMongoDB model constructor.
     * @property {module:model/DatabaseMongoDB}
     */
    DatabaseMongoDB,

    /**
     * The DatabaseMongoDBHosts model constructor.
     * @property {module:model/DatabaseMongoDBHosts}
     */
    DatabaseMongoDBHosts,

    /**
     * The DatabaseMongoDBRequest model constructor.
     * @property {module:model/DatabaseMongoDBRequest}
     */
    DatabaseMongoDBRequest,

    /**
     * The DatabaseMySQL model constructor.
     * @property {module:model/DatabaseMySQL}
     */
    DatabaseMySQL,

    /**
     * The DatabaseMySQLRequest model constructor.
     * @property {module:model/DatabaseMySQLRequest}
     */
    DatabaseMySQLRequest,

    /**
     * The DatabasePostgreSQL model constructor.
     * @property {module:model/DatabasePostgreSQL}
     */
    DatabasePostgreSQL,

    /**
     * The DatabasePostgreSQLHosts model constructor.
     * @property {module:model/DatabasePostgreSQLHosts}
     */
    DatabasePostgreSQLHosts,

    /**
     * The DatabasePostgreSQLRequest model constructor.
     * @property {module:model/DatabasePostgreSQLRequest}
     */
    DatabasePostgreSQLRequest,

    /**
     * The DatabaseSSL model constructor.
     * @property {module:model/DatabaseSSL}
     */
    DatabaseSSL,

    /**
     * The DatabaseType model constructor.
     * @property {module:model/DatabaseType}
     */
    DatabaseType,

    /**
     * The DatabaseTypeEngine model constructor.
     * @property {module:model/DatabaseTypeEngine}
     */
    DatabaseTypeEngine,

    /**
     * The DatabaseTypeEnginePrice model constructor.
     * @property {module:model/DatabaseTypeEnginePrice}
     */
    DatabaseTypeEnginePrice,

    /**
     * The DatabaseTypeEngines model constructor.
     * @property {module:model/DatabaseTypeEngines}
     */
    DatabaseTypeEngines,

    /**
     * The DatabaseUpdates model constructor.
     * @property {module:model/DatabaseUpdates}
     */
    DatabaseUpdates,

    /**
     * The Device model constructor.
     * @property {module:model/Device}
     */
    Device,

    /**
     * The Devices model constructor.
     * @property {module:model/Devices}
     */
    Devices,

    /**
     * The Disk model constructor.
     * @property {module:model/Disk}
     */
    Disk,

    /**
     * The DiskRequest model constructor.
     * @property {module:model/DiskRequest}
     */
    DiskRequest,

    /**
     * The Domain model constructor.
     * @property {module:model/Domain}
     */
    Domain,

    /**
     * The DomainRecord model constructor.
     * @property {module:model/DomainRecord}
     */
    DomainRecord,

    /**
     * The EntityTransfer model constructor.
     * @property {module:model/EntityTransfer}
     */
    EntityTransfer,

    /**
     * The EntityTransferEntities model constructor.
     * @property {module:model/EntityTransferEntities}
     */
    EntityTransferEntities,

    /**
     * The ErrorObject model constructor.
     * @property {module:model/ErrorObject}
     */
    ErrorObject,

    /**
     * The Event model constructor.
     * @property {module:model/Event}
     */
    Event,

    /**
     * The EventEntity model constructor.
     * @property {module:model/EventEntity}
     */
    EventEntity,

    /**
     * The EventSecondaryEntity model constructor.
     * @property {module:model/EventSecondaryEntity}
     */
    EventSecondaryEntity,

    /**
     * The Firewall model constructor.
     * @property {module:model/Firewall}
     */
    Firewall,

    /**
     * The FirewallDevices model constructor.
     * @property {module:model/FirewallDevices}
     */
    FirewallDevices,

    /**
     * The FirewallDevicesEntity model constructor.
     * @property {module:model/FirewallDevicesEntity}
     */
    FirewallDevicesEntity,

    /**
     * The FirewallRuleConfig model constructor.
     * @property {module:model/FirewallRuleConfig}
     */
    FirewallRuleConfig,

    /**
     * The FirewallRuleConfigAddresses model constructor.
     * @property {module:model/FirewallRuleConfigAddresses}
     */
    FirewallRuleConfigAddresses,

    /**
     * The FirewallRules model constructor.
     * @property {module:model/FirewallRules}
     */
    FirewallRules,

    /**
     * The GetAccountDefaultResponse model constructor.
     * @property {module:model/GetAccountDefaultResponse}
     */
    GetAccountDefaultResponse,

    /**
     * The GetAccountLogins200Response model constructor.
     * @property {module:model/GetAccountLogins200Response}
     */
    GetAccountLogins200Response,

    /**
     * The GetBackups200Response model constructor.
     * @property {module:model/GetBackups200Response}
     */
    GetBackups200Response,

    /**
     * The GetBackups200ResponseAutomaticInner model constructor.
     * @property {module:model/GetBackups200ResponseAutomaticInner}
     */
    GetBackups200ResponseAutomaticInner,

    /**
     * The GetBackups200ResponseSnapshot model constructor.
     * @property {module:model/GetBackups200ResponseSnapshot}
     */
    GetBackups200ResponseSnapshot,

    /**
     * The GetClients200Response model constructor.
     * @property {module:model/GetClients200Response}
     */
    GetClients200Response,

    /**
     * The GetDatabasesEngines200Response model constructor.
     * @property {module:model/GetDatabasesEngines200Response}
     */
    GetDatabasesEngines200Response,

    /**
     * The GetDatabasesInstances200Response model constructor.
     * @property {module:model/GetDatabasesInstances200Response}
     */
    GetDatabasesInstances200Response,

    /**
     * The GetDatabasesMongoDBInstanceBackups200Response model constructor.
     * @property {module:model/GetDatabasesMongoDBInstanceBackups200Response}
     */
    GetDatabasesMongoDBInstanceBackups200Response,

    /**
     * The GetDatabasesMongoDBInstances200Response model constructor.
     * @property {module:model/GetDatabasesMongoDBInstances200Response}
     */
    GetDatabasesMongoDBInstances200Response,

    /**
     * The GetDatabasesMySQLInstances200Response model constructor.
     * @property {module:model/GetDatabasesMySQLInstances200Response}
     */
    GetDatabasesMySQLInstances200Response,

    /**
     * The GetDatabasesPostgreSQLInstances200Response model constructor.
     * @property {module:model/GetDatabasesPostgreSQLInstances200Response}
     */
    GetDatabasesPostgreSQLInstances200Response,

    /**
     * The GetDatabasesTypes200Response model constructor.
     * @property {module:model/GetDatabasesTypes200Response}
     */
    GetDatabasesTypes200Response,

    /**
     * The GetDevices200Response model constructor.
     * @property {module:model/GetDevices200Response}
     */
    GetDevices200Response,

    /**
     * The GetDomainRecords200Response model constructor.
     * @property {module:model/GetDomainRecords200Response}
     */
    GetDomainRecords200Response,

    /**
     * The GetDomainZone200Response model constructor.
     * @property {module:model/GetDomainZone200Response}
     */
    GetDomainZone200Response,

    /**
     * The GetDomains200Response model constructor.
     * @property {module:model/GetDomains200Response}
     */
    GetDomains200Response,

    /**
     * The GetEntityTransfers200Response model constructor.
     * @property {module:model/GetEntityTransfers200Response}
     */
    GetEntityTransfers200Response,

    /**
     * The GetEvents200Response model constructor.
     * @property {module:model/GetEvents200Response}
     */
    GetEvents200Response,

    /**
     * The GetFirewallDevices200Response model constructor.
     * @property {module:model/GetFirewallDevices200Response}
     */
    GetFirewallDevices200Response,

    /**
     * The GetIPs200Response model constructor.
     * @property {module:model/GetIPs200Response}
     */
    GetIPs200Response,

    /**
     * The GetIPv6Pools200Response model constructor.
     * @property {module:model/GetIPv6Pools200Response}
     */
    GetIPv6Pools200Response,

    /**
     * The GetIPv6Ranges200Response model constructor.
     * @property {module:model/GetIPv6Ranges200Response}
     */
    GetIPv6Ranges200Response,

    /**
     * The GetImages200Response model constructor.
     * @property {module:model/GetImages200Response}
     */
    GetImages200Response,

    /**
     * The GetInvoiceItems200Response model constructor.
     * @property {module:model/GetInvoiceItems200Response}
     */
    GetInvoiceItems200Response,

    /**
     * The GetInvoices200Response model constructor.
     * @property {module:model/GetInvoices200Response}
     */
    GetInvoices200Response,

    /**
     * The GetKernels200Response model constructor.
     * @property {module:model/GetKernels200Response}
     */
    GetKernels200Response,

    /**
     * The GetLKEClusterAPIEndpoints200Response model constructor.
     * @property {module:model/GetLKEClusterAPIEndpoints200Response}
     */
    GetLKEClusterAPIEndpoints200Response,

    /**
     * The GetLKEClusterAPIEndpoints200ResponseDataInner model constructor.
     * @property {module:model/GetLKEClusterAPIEndpoints200ResponseDataInner}
     */
    GetLKEClusterAPIEndpoints200ResponseDataInner,

    /**
     * The GetLKEClusterDashboard200Response model constructor.
     * @property {module:model/GetLKEClusterDashboard200Response}
     */
    GetLKEClusterDashboard200Response,

    /**
     * The GetLKEClusterKubeconfig200Response model constructor.
     * @property {module:model/GetLKEClusterKubeconfig200Response}
     */
    GetLKEClusterKubeconfig200Response,

    /**
     * The GetLKEClusterNode200Response model constructor.
     * @property {module:model/GetLKEClusterNode200Response}
     */
    GetLKEClusterNode200Response,

    /**
     * The GetLKEClusterPools200Response model constructor.
     * @property {module:model/GetLKEClusterPools200Response}
     */
    GetLKEClusterPools200Response,

    /**
     * The GetLKEClusters200Response model constructor.
     * @property {module:model/GetLKEClusters200Response}
     */
    GetLKEClusters200Response,

    /**
     * The GetLKEVersions200Response model constructor.
     * @property {module:model/GetLKEVersions200Response}
     */
    GetLKEVersions200Response,

    /**
     * The GetLinodeConfigs200Response model constructor.
     * @property {module:model/GetLinodeConfigs200Response}
     */
    GetLinodeConfigs200Response,

    /**
     * The GetLinodeDisks200Response model constructor.
     * @property {module:model/GetLinodeDisks200Response}
     */
    GetLinodeDisks200Response,

    /**
     * The GetLinodeFirewalls200Response model constructor.
     * @property {module:model/GetLinodeFirewalls200Response}
     */
    GetLinodeFirewalls200Response,

    /**
     * The GetLinodeIPs200Response model constructor.
     * @property {module:model/GetLinodeIPs200Response}
     */
    GetLinodeIPs200Response,

    /**
     * The GetLinodeIPs200ResponseIpv4 model constructor.
     * @property {module:model/GetLinodeIPs200ResponseIpv4}
     */
    GetLinodeIPs200ResponseIpv4,

    /**
     * The GetLinodeIPs200ResponseIpv6 model constructor.
     * @property {module:model/GetLinodeIPs200ResponseIpv6}
     */
    GetLinodeIPs200ResponseIpv6,

    /**
     * The GetLinodeInstances200Response model constructor.
     * @property {module:model/GetLinodeInstances200Response}
     */
    GetLinodeInstances200Response,

    /**
     * The GetLinodeNodeBalancers200Response model constructor.
     * @property {module:model/GetLinodeNodeBalancers200Response}
     */
    GetLinodeNodeBalancers200Response,

    /**
     * The GetLinodeTransfer200Response model constructor.
     * @property {module:model/GetLinodeTransfer200Response}
     */
    GetLinodeTransfer200Response,

    /**
     * The GetLinodeTransferByYearMonth200Response model constructor.
     * @property {module:model/GetLinodeTransferByYearMonth200Response}
     */
    GetLinodeTransferByYearMonth200Response,

    /**
     * The GetLinodeTypes200Response model constructor.
     * @property {module:model/GetLinodeTypes200Response}
     */
    GetLinodeTypes200Response,

    /**
     * The GetLinodeVolumes200Response model constructor.
     * @property {module:model/GetLinodeVolumes200Response}
     */
    GetLinodeVolumes200Response,

    /**
     * The GetLongviewClients200Response model constructor.
     * @property {module:model/GetLongviewClients200Response}
     */
    GetLongviewClients200Response,

    /**
     * The GetLongviewSubscriptions200Response model constructor.
     * @property {module:model/GetLongviewSubscriptions200Response}
     */
    GetLongviewSubscriptions200Response,

    /**
     * The GetMaintenance200Response model constructor.
     * @property {module:model/GetMaintenance200Response}
     */
    GetMaintenance200Response,

    /**
     * The GetManagedContacts200Response model constructor.
     * @property {module:model/GetManagedContacts200Response}
     */
    GetManagedContacts200Response,

    /**
     * The GetManagedCredentials200Response model constructor.
     * @property {module:model/GetManagedCredentials200Response}
     */
    GetManagedCredentials200Response,

    /**
     * The GetManagedIssues200Response model constructor.
     * @property {module:model/GetManagedIssues200Response}
     */
    GetManagedIssues200Response,

    /**
     * The GetManagedLinodeSettings200Response model constructor.
     * @property {module:model/GetManagedLinodeSettings200Response}
     */
    GetManagedLinodeSettings200Response,

    /**
     * The GetManagedServices200Response model constructor.
     * @property {module:model/GetManagedServices200Response}
     */
    GetManagedServices200Response,

    /**
     * The GetManagedStats200Response model constructor.
     * @property {module:model/GetManagedStats200Response}
     */
    GetManagedStats200Response,

    /**
     * The GetManagedStats200ResponseData model constructor.
     * @property {module:model/GetManagedStats200ResponseData}
     */
    GetManagedStats200ResponseData,

    /**
     * The GetNodeBalancerConfigNodes200Response model constructor.
     * @property {module:model/GetNodeBalancerConfigNodes200Response}
     */
    GetNodeBalancerConfigNodes200Response,

    /**
     * The GetNodeBalancerConfigs200Response model constructor.
     * @property {module:model/GetNodeBalancerConfigs200Response}
     */
    GetNodeBalancerConfigs200Response,

    /**
     * The GetNotifications200Response model constructor.
     * @property {module:model/GetNotifications200Response}
     */
    GetNotifications200Response,

    /**
     * The GetObjectStorageBucketContent200Response model constructor.
     * @property {module:model/GetObjectStorageBucketContent200Response}
     */
    GetObjectStorageBucketContent200Response,

    /**
     * The GetObjectStorageBuckets200Response model constructor.
     * @property {module:model/GetObjectStorageBuckets200Response}
     */
    GetObjectStorageBuckets200Response,

    /**
     * The GetObjectStorageClusters200Response model constructor.
     * @property {module:model/GetObjectStorageClusters200Response}
     */
    GetObjectStorageClusters200Response,

    /**
     * The GetObjectStorageKeys200Response model constructor.
     * @property {module:model/GetObjectStorageKeys200Response}
     */
    GetObjectStorageKeys200Response,

    /**
     * The GetObjectStorageTransfer200Response model constructor.
     * @property {module:model/GetObjectStorageTransfer200Response}
     */
    GetObjectStorageTransfer200Response,

    /**
     * The GetPaymentMethods200Response model constructor.
     * @property {module:model/GetPaymentMethods200Response}
     */
    GetPaymentMethods200Response,

    /**
     * The GetPayments200Response model constructor.
     * @property {module:model/GetPayments200Response}
     */
    GetPayments200Response,

    /**
     * The GetPersonalAccessTokens200Response model constructor.
     * @property {module:model/GetPersonalAccessTokens200Response}
     */
    GetPersonalAccessTokens200Response,

    /**
     * The GetProfileApps200Response model constructor.
     * @property {module:model/GetProfileApps200Response}
     */
    GetProfileApps200Response,

    /**
     * The GetRegions200Response model constructor.
     * @property {module:model/GetRegions200Response}
     */
    GetRegions200Response,

    /**
     * The GetSSHKeys200Response model constructor.
     * @property {module:model/GetSSHKeys200Response}
     */
    GetSSHKeys200Response,

    /**
     * The GetServiceTransfers200Response model constructor.
     * @property {module:model/GetServiceTransfers200Response}
     */
    GetServiceTransfers200Response,

    /**
     * The GetStackScripts200Response model constructor.
     * @property {module:model/GetStackScripts200Response}
     */
    GetStackScripts200Response,

    /**
     * The GetTaggedObjects200Response model constructor.
     * @property {module:model/GetTaggedObjects200Response}
     */
    GetTaggedObjects200Response,

    /**
     * The GetTaggedObjects200ResponseDataInner model constructor.
     * @property {module:model/GetTaggedObjects200ResponseDataInner}
     */
    GetTaggedObjects200ResponseDataInner,

    /**
     * The GetTaggedObjects200ResponseDataInnerData model constructor.
     * @property {module:model/GetTaggedObjects200ResponseDataInnerData}
     */
    GetTaggedObjects200ResponseDataInnerData,

    /**
     * The GetTags200Response model constructor.
     * @property {module:model/GetTags200Response}
     */
    GetTags200Response,

    /**
     * The GetTicketReplies200Response model constructor.
     * @property {module:model/GetTicketReplies200Response}
     */
    GetTicketReplies200Response,

    /**
     * The GetTickets200Response model constructor.
     * @property {module:model/GetTickets200Response}
     */
    GetTickets200Response,

    /**
     * The GetUsers200Response model constructor.
     * @property {module:model/GetUsers200Response}
     */
    GetUsers200Response,

    /**
     * The GetVLANs200Response model constructor.
     * @property {module:model/GetVLANs200Response}
     */
    GetVLANs200Response,

    /**
     * The GooglePayData model constructor.
     * @property {module:model/GooglePayData}
     */
    GooglePayData,

    /**
     * The Grant model constructor.
     * @property {module:model/Grant}
     */
    Grant,

    /**
     * The GrantsResponse model constructor.
     * @property {module:model/GrantsResponse}
     */
    GrantsResponse,

    /**
     * The GrantsResponseGlobal model constructor.
     * @property {module:model/GrantsResponseGlobal}
     */
    GrantsResponseGlobal,

    /**
     * The IPAddress model constructor.
     * @property {module:model/IPAddress}
     */
    IPAddress,

    /**
     * The IPAddressPrivate model constructor.
     * @property {module:model/IPAddressPrivate}
     */
    IPAddressPrivate,

    /**
     * The IPAddressV6LinkLocal model constructor.
     * @property {module:model/IPAddressV6LinkLocal}
     */
    IPAddressV6LinkLocal,

    /**
     * The IPAddressV6Slaac model constructor.
     * @property {module:model/IPAddressV6Slaac}
     */
    IPAddressV6Slaac,

    /**
     * The IPAddressesAssignRequest model constructor.
     * @property {module:model/IPAddressesAssignRequest}
     */
    IPAddressesAssignRequest,

    /**
     * The IPAddressesAssignRequestAssignmentsInner model constructor.
     * @property {module:model/IPAddressesAssignRequestAssignmentsInner}
     */
    IPAddressesAssignRequestAssignmentsInner,

    /**
     * The IPAddressesShareRequest model constructor.
     * @property {module:model/IPAddressesShareRequest}
     */
    IPAddressesShareRequest,

    /**
     * The IPv6Pool model constructor.
     * @property {module:model/IPv6Pool}
     */
    IPv6Pool,

    /**
     * The IPv6Range model constructor.
     * @property {module:model/IPv6Range}
     */
    IPv6Range,

    /**
     * The IPv6RangeBGP model constructor.
     * @property {module:model/IPv6RangeBGP}
     */
    IPv6RangeBGP,

    /**
     * The Image model constructor.
     * @property {module:model/Image}
     */
    Image,

    /**
     * The ImagesUploadPost200Response model constructor.
     * @property {module:model/ImagesUploadPost200Response}
     */
    ImagesUploadPost200Response,

    /**
     * The ImagesUploadPostRequest model constructor.
     * @property {module:model/ImagesUploadPostRequest}
     */
    ImagesUploadPostRequest,

    /**
     * The ImportDomainRequest model constructor.
     * @property {module:model/ImportDomainRequest}
     */
    ImportDomainRequest,

    /**
     * The Invoice model constructor.
     * @property {module:model/Invoice}
     */
    Invoice,

    /**
     * The InvoiceItem model constructor.
     * @property {module:model/InvoiceItem}
     */
    InvoiceItem,

    /**
     * The InvoiceTaxSummaryInner model constructor.
     * @property {module:model/InvoiceTaxSummaryInner}
     */
    InvoiceTaxSummaryInner,

    /**
     * The Kernel model constructor.
     * @property {module:model/Kernel}
     */
    Kernel,

    /**
     * The LKECluster model constructor.
     * @property {module:model/LKECluster}
     */
    LKECluster,

    /**
     * The LKEClusterControlPlane model constructor.
     * @property {module:model/LKEClusterControlPlane}
     */
    LKEClusterControlPlane,

    /**
     * The LKENodePool model constructor.
     * @property {module:model/LKENodePool}
     */
    LKENodePool,

    /**
     * The LKENodePoolAutoscaler model constructor.
     * @property {module:model/LKENodePoolAutoscaler}
     */
    LKENodePoolAutoscaler,

    /**
     * The LKENodePoolDisksInner model constructor.
     * @property {module:model/LKENodePoolDisksInner}
     */
    LKENodePoolDisksInner,

    /**
     * The LKENodePoolRequestBody model constructor.
     * @property {module:model/LKENodePoolRequestBody}
     */
    LKENodePoolRequestBody,

    /**
     * The LKENodePoolRequestBodyAutoscaler model constructor.
     * @property {module:model/LKENodePoolRequestBodyAutoscaler}
     */
    LKENodePoolRequestBodyAutoscaler,

    /**
     * The LKENodeStatus model constructor.
     * @property {module:model/LKENodeStatus}
     */
    LKENodeStatus,

    /**
     * The LKEVersion model constructor.
     * @property {module:model/LKEVersion}
     */
    LKEVersion,

    /**
     * The Linode model constructor.
     * @property {module:model/Linode}
     */
    Linode,

    /**
     * The LinodeAlerts model constructor.
     * @property {module:model/LinodeAlerts}
     */
    LinodeAlerts,

    /**
     * The LinodeBackups model constructor.
     * @property {module:model/LinodeBackups}
     */
    LinodeBackups,

    /**
     * The LinodeBackupsSchedule model constructor.
     * @property {module:model/LinodeBackupsSchedule}
     */
    LinodeBackupsSchedule,

    /**
     * The LinodeConfig model constructor.
     * @property {module:model/LinodeConfig}
     */
    LinodeConfig,

    /**
     * The LinodeConfigHelpers model constructor.
     * @property {module:model/LinodeConfigHelpers}
     */
    LinodeConfigHelpers,

    /**
     * The LinodeConfigInterface model constructor.
     * @property {module:model/LinodeConfigInterface}
     */
    LinodeConfigInterface,

    /**
     * The LinodeRequest model constructor.
     * @property {module:model/LinodeRequest}
     */
    LinodeRequest,

    /**
     * The LinodeSpecs model constructor.
     * @property {module:model/LinodeSpecs}
     */
    LinodeSpecs,

    /**
     * The LinodeStats model constructor.
     * @property {module:model/LinodeStats}
     */
    LinodeStats,

    /**
     * The LinodeStatsIo model constructor.
     * @property {module:model/LinodeStatsIo}
     */
    LinodeStatsIo,

    /**
     * The LinodeStatsNetv4 model constructor.
     * @property {module:model/LinodeStatsNetv4}
     */
    LinodeStatsNetv4,

    /**
     * The LinodeStatsNetv6 model constructor.
     * @property {module:model/LinodeStatsNetv6}
     */
    LinodeStatsNetv6,

    /**
     * The LinodeType model constructor.
     * @property {module:model/LinodeType}
     */
    LinodeType,

    /**
     * The LinodeTypeAddons model constructor.
     * @property {module:model/LinodeTypeAddons}
     */
    LinodeTypeAddons,

    /**
     * The LinodeTypeAddonsBackups model constructor.
     * @property {module:model/LinodeTypeAddonsBackups}
     */
    LinodeTypeAddonsBackups,

    /**
     * The LinodeTypeAddonsBackupsPrice model constructor.
     * @property {module:model/LinodeTypeAddonsBackupsPrice}
     */
    LinodeTypeAddonsBackupsPrice,

    /**
     * The LinodeTypePrice model constructor.
     * @property {module:model/LinodeTypePrice}
     */
    LinodeTypePrice,

    /**
     * The Login model constructor.
     * @property {module:model/Login}
     */
    Login,

    /**
     * The LongviewClient model constructor.
     * @property {module:model/LongviewClient}
     */
    LongviewClient,

    /**
     * The LongviewClientApps model constructor.
     * @property {module:model/LongviewClientApps}
     */
    LongviewClientApps,

    /**
     * The LongviewPlan model constructor.
     * @property {module:model/LongviewPlan}
     */
    LongviewPlan,

    /**
     * The LongviewSubscription model constructor.
     * @property {module:model/LongviewSubscription}
     */
    LongviewSubscription,

    /**
     * The LongviewSubscriptionPrice model constructor.
     * @property {module:model/LongviewSubscriptionPrice}
     */
    LongviewSubscriptionPrice,

    /**
     * The Maintenance model constructor.
     * @property {module:model/Maintenance}
     */
    Maintenance,

    /**
     * The MaintenanceEntity model constructor.
     * @property {module:model/MaintenanceEntity}
     */
    MaintenanceEntity,

    /**
     * The ManagedContact model constructor.
     * @property {module:model/ManagedContact}
     */
    ManagedContact,

    /**
     * The ManagedContactPhone model constructor.
     * @property {module:model/ManagedContactPhone}
     */
    ManagedContactPhone,

    /**
     * The ManagedCredential model constructor.
     * @property {module:model/ManagedCredential}
     */
    ManagedCredential,

    /**
     * The ManagedIssue model constructor.
     * @property {module:model/ManagedIssue}
     */
    ManagedIssue,

    /**
     * The ManagedIssueEntity model constructor.
     * @property {module:model/ManagedIssueEntity}
     */
    ManagedIssueEntity,

    /**
     * The ManagedLinodeSettings model constructor.
     * @property {module:model/ManagedLinodeSettings}
     */
    ManagedLinodeSettings,

    /**
     * The ManagedLinodeSettingsSsh model constructor.
     * @property {module:model/ManagedLinodeSettingsSsh}
     */
    ManagedLinodeSettingsSsh,

    /**
     * The ManagedService model constructor.
     * @property {module:model/ManagedService}
     */
    ManagedService,

    /**
     * The MigrateLinodeInstanceRequest model constructor.
     * @property {module:model/MigrateLinodeInstanceRequest}
     */
    MigrateLinodeInstanceRequest,

    /**
     * The MutateLinodeInstanceRequest model constructor.
     * @property {module:model/MutateLinodeInstanceRequest}
     */
    MutateLinodeInstanceRequest,

    /**
     * The NodeBalancer model constructor.
     * @property {module:model/NodeBalancer}
     */
    NodeBalancer,

    /**
     * The NodeBalancerConfig model constructor.
     * @property {module:model/NodeBalancerConfig}
     */
    NodeBalancerConfig,

    /**
     * The NodeBalancerConfigNodesStatus model constructor.
     * @property {module:model/NodeBalancerConfigNodesStatus}
     */
    NodeBalancerConfigNodesStatus,

    /**
     * The NodeBalancerNode model constructor.
     * @property {module:model/NodeBalancerNode}
     */
    NodeBalancerNode,

    /**
     * The NodeBalancerStats model constructor.
     * @property {module:model/NodeBalancerStats}
     */
    NodeBalancerStats,

    /**
     * The NodeBalancerStatsData model constructor.
     * @property {module:model/NodeBalancerStatsData}
     */
    NodeBalancerStatsData,

    /**
     * The NodeBalancerStatsDataTraffic model constructor.
     * @property {module:model/NodeBalancerStatsDataTraffic}
     */
    NodeBalancerStatsDataTraffic,

    /**
     * The NodeBalancerTransfer model constructor.
     * @property {module:model/NodeBalancerTransfer}
     */
    NodeBalancerTransfer,

    /**
     * The Notification model constructor.
     * @property {module:model/Notification}
     */
    Notification,

    /**
     * The NotificationEntity model constructor.
     * @property {module:model/NotificationEntity}
     */
    NotificationEntity,

    /**
     * The OAuthClient model constructor.
     * @property {module:model/OAuthClient}
     */
    OAuthClient,

    /**
     * The ObjectStorageBucket model constructor.
     * @property {module:model/ObjectStorageBucket}
     */
    ObjectStorageBucket,

    /**
     * The ObjectStorageCluster model constructor.
     * @property {module:model/ObjectStorageCluster}
     */
    ObjectStorageCluster,

    /**
     * The ObjectStorageKey model constructor.
     * @property {module:model/ObjectStorageKey}
     */
    ObjectStorageKey,

    /**
     * The ObjectStorageKeyBucketAccessInner model constructor.
     * @property {module:model/ObjectStorageKeyBucketAccessInner}
     */
    ObjectStorageKeyBucketAccessInner,

    /**
     * The ObjectStorageObject model constructor.
     * @property {module:model/ObjectStorageObject}
     */
    ObjectStorageObject,

    /**
     * The ObjectStorageSSL model constructor.
     * @property {module:model/ObjectStorageSSL}
     */
    ObjectStorageSSL,

    /**
     * The ObjectStorageSSLResponse model constructor.
     * @property {module:model/ObjectStorageSSLResponse}
     */
    ObjectStorageSSLResponse,

    /**
     * The PaginationEnvelope model constructor.
     * @property {module:model/PaginationEnvelope}
     */
    PaginationEnvelope,

    /**
     * The PayPal model constructor.
     * @property {module:model/PayPal}
     */
    PayPal,

    /**
     * The PayPalData model constructor.
     * @property {module:model/PayPalData}
     */
    PayPalData,

    /**
     * The PayPalExecute model constructor.
     * @property {module:model/PayPalExecute}
     */
    PayPalExecute,

    /**
     * The Payment model constructor.
     * @property {module:model/Payment}
     */
    Payment,

    /**
     * The PaymentMethod model constructor.
     * @property {module:model/PaymentMethod}
     */
    PaymentMethod,

    /**
     * The PaymentMethodData model constructor.
     * @property {module:model/PaymentMethodData}
     */
    PaymentMethodData,

    /**
     * The PaymentRequest model constructor.
     * @property {module:model/PaymentRequest}
     */
    PaymentRequest,

    /**
     * The PersonalAccessToken model constructor.
     * @property {module:model/PersonalAccessToken}
     */
    PersonalAccessToken,

    /**
     * The PostIPv6Range200Response model constructor.
     * @property {module:model/PostIPv6Range200Response}
     */
    PostIPv6Range200Response,

    /**
     * The PostIPv6RangeRequest model constructor.
     * @property {module:model/PostIPv6RangeRequest}
     */
    PostIPv6RangeRequest,

    /**
     * The PostLKEClusterRegenerateRequest model constructor.
     * @property {module:model/PostLKEClusterRegenerateRequest}
     */
    PostLKEClusterRegenerateRequest,

    /**
     * The PostProfilePhoneNumberRequest model constructor.
     * @property {module:model/PostProfilePhoneNumberRequest}
     */
    PostProfilePhoneNumberRequest,

    /**
     * The PostProfilePhoneNumberVerifyRequest model constructor.
     * @property {module:model/PostProfilePhoneNumberVerifyRequest}
     */
    PostProfilePhoneNumberVerifyRequest,

    /**
     * The Profile model constructor.
     * @property {module:model/Profile}
     */
    Profile,

    /**
     * The ProfileReferrals model constructor.
     * @property {module:model/ProfileReferrals}
     */
    ProfileReferrals,

    /**
     * The Promotion model constructor.
     * @property {module:model/Promotion}
     */
    Promotion,

    /**
     * The PutDatabasesMongoDBInstanceRequest model constructor.
     * @property {module:model/PutDatabasesMongoDBInstanceRequest}
     */
    PutDatabasesMongoDBInstanceRequest,

    /**
     * The PutDatabasesMySQLInstanceRequest model constructor.
     * @property {module:model/PutDatabasesMySQLInstanceRequest}
     */
    PutDatabasesMySQLInstanceRequest,

    /**
     * The PutDatabasesPostgreSQLInstanceRequest model constructor.
     * @property {module:model/PutDatabasesPostgreSQLInstanceRequest}
     */
    PutDatabasesPostgreSQLInstanceRequest,

    /**
     * The PutLKECluster200Response model constructor.
     * @property {module:model/PutLKECluster200Response}
     */
    PutLKECluster200Response,

    /**
     * The PutLKEClusterRequest model constructor.
     * @property {module:model/PutLKEClusterRequest}
     */
    PutLKEClusterRequest,

    /**
     * The PutLKEClusterRequestControlPlane model constructor.
     * @property {module:model/PutLKEClusterRequestControlPlane}
     */
    PutLKEClusterRequestControlPlane,

    /**
     * The PutLKENodePoolRequest model constructor.
     * @property {module:model/PutLKENodePoolRequest}
     */
    PutLKENodePoolRequest,

    /**
     * The RebootLinodeInstanceRequest model constructor.
     * @property {module:model/RebootLinodeInstanceRequest}
     */
    RebootLinodeInstanceRequest,

    /**
     * The RebuildNodeBalancerConfigRequest model constructor.
     * @property {module:model/RebuildNodeBalancerConfigRequest}
     */
    RebuildNodeBalancerConfigRequest,

    /**
     * The RebuildNodeBalancerConfigRequestAllOfNodesInner model constructor.
     * @property {module:model/RebuildNodeBalancerConfigRequestAllOfNodesInner}
     */
    RebuildNodeBalancerConfigRequestAllOfNodesInner,

    /**
     * The Region model constructor.
     * @property {module:model/Region}
     */
    Region,

    /**
     * The RegionResolvers model constructor.
     * @property {module:model/RegionResolvers}
     */
    RegionResolvers,

    /**
     * The RescueDevices model constructor.
     * @property {module:model/RescueDevices}
     */
    RescueDevices,

    /**
     * The RescueLinodeInstanceRequest model constructor.
     * @property {module:model/RescueLinodeInstanceRequest}
     */
    RescueLinodeInstanceRequest,

    /**
     * The ResetDiskPasswordRequest model constructor.
     * @property {module:model/ResetDiskPasswordRequest}
     */
    ResetDiskPasswordRequest,

    /**
     * The ResetLinodePasswordRequest model constructor.
     * @property {module:model/ResetLinodePasswordRequest}
     */
    ResetLinodePasswordRequest,

    /**
     * The ResizeDiskRequest model constructor.
     * @property {module:model/ResizeDiskRequest}
     */
    ResizeDiskRequest,

    /**
     * The ResizeLinodeInstanceRequest model constructor.
     * @property {module:model/ResizeLinodeInstanceRequest}
     */
    ResizeLinodeInstanceRequest,

    /**
     * The ResizeVolumeRequest model constructor.
     * @property {module:model/ResizeVolumeRequest}
     */
    ResizeVolumeRequest,

    /**
     * The RestoreBackupRequest model constructor.
     * @property {module:model/RestoreBackupRequest}
     */
    RestoreBackupRequest,

    /**
     * The SSHKey model constructor.
     * @property {module:model/SSHKey}
     */
    SSHKey,

    /**
     * The SecurityQuestion model constructor.
     * @property {module:model/SecurityQuestion}
     */
    SecurityQuestion,

    /**
     * The SecurityQuestionsGet model constructor.
     * @property {module:model/SecurityQuestionsGet}
     */
    SecurityQuestionsGet,

    /**
     * The SecurityQuestionsGetSecurityQuestionsInner model constructor.
     * @property {module:model/SecurityQuestionsGetSecurityQuestionsInner}
     */
    SecurityQuestionsGetSecurityQuestionsInner,

    /**
     * The SecurityQuestionsPost model constructor.
     * @property {module:model/SecurityQuestionsPost}
     */
    SecurityQuestionsPost,

    /**
     * The SecurityQuestionsPostSecurityQuestionsInner model constructor.
     * @property {module:model/SecurityQuestionsPostSecurityQuestionsInner}
     */
    SecurityQuestionsPostSecurityQuestionsInner,

    /**
     * The ServiceTransfer model constructor.
     * @property {module:model/ServiceTransfer}
     */
    ServiceTransfer,

    /**
     * The ServiceTransferEntities model constructor.
     * @property {module:model/ServiceTransferEntities}
     */
    ServiceTransferEntities,

    /**
     * The StackScript model constructor.
     * @property {module:model/StackScript}
     */
    StackScript,

    /**
     * The StatsData model constructor.
     * @property {module:model/StatsData}
     */
    StatsData,

    /**
     * The StatsDataAvailable model constructor.
     * @property {module:model/StatsDataAvailable}
     */
    StatsDataAvailable,

    /**
     * The SupportTicket model constructor.
     * @property {module:model/SupportTicket}
     */
    SupportTicket,

    /**
     * The SupportTicketEntity model constructor.
     * @property {module:model/SupportTicketEntity}
     */
    SupportTicketEntity,

    /**
     * The SupportTicketReply model constructor.
     * @property {module:model/SupportTicketReply}
     */
    SupportTicketReply,

    /**
     * The SupportTicketRequest model constructor.
     * @property {module:model/SupportTicketRequest}
     */
    SupportTicketRequest,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The TfaConfirm200Response model constructor.
     * @property {module:model/TfaConfirm200Response}
     */
    TfaConfirm200Response,

    /**
     * The TfaConfirmRequest model constructor.
     * @property {module:model/TfaConfirmRequest}
     */
    TfaConfirmRequest,

    /**
     * The TfaEnable200Response model constructor.
     * @property {module:model/TfaEnable200Response}
     */
    TfaEnable200Response,

    /**
     * The Transfer model constructor.
     * @property {module:model/Transfer}
     */
    Transfer,

    /**
     * The TrustedDevice model constructor.
     * @property {module:model/TrustedDevice}
     */
    TrustedDevice,

    /**
     * The UpdateDomainRecordRequest model constructor.
     * @property {module:model/UpdateDomainRecordRequest}
     */
    UpdateDomainRecordRequest,

    /**
     * The UpdateFirewallRequest model constructor.
     * @property {module:model/UpdateFirewallRequest}
     */
    UpdateFirewallRequest,

    /**
     * The UpdateIPRequest model constructor.
     * @property {module:model/UpdateIPRequest}
     */
    UpdateIPRequest,

    /**
     * The UpdateLinodeIPRequest model constructor.
     * @property {module:model/UpdateLinodeIPRequest}
     */
    UpdateLinodeIPRequest,

    /**
     * The UpdateManagedCredentialUsernamePasswordRequest model constructor.
     * @property {module:model/UpdateManagedCredentialUsernamePasswordRequest}
     */
    UpdateManagedCredentialUsernamePasswordRequest,

    /**
     * The UpdateObjectStorageBucketACLRequest model constructor.
     * @property {module:model/UpdateObjectStorageBucketACLRequest}
     */
    UpdateObjectStorageBucketACLRequest,

    /**
     * The UpdateObjectStorageBucketAccessRequest model constructor.
     * @property {module:model/UpdateObjectStorageBucketAccessRequest}
     */
    UpdateObjectStorageBucketAccessRequest,

    /**
     * The UpdateObjectStorageKeyRequest model constructor.
     * @property {module:model/UpdateObjectStorageKeyRequest}
     */
    UpdateObjectStorageKeyRequest,

    /**
     * The UpdateSSHKeyRequest model constructor.
     * @property {module:model/UpdateSSHKeyRequest}
     */
    UpdateSSHKeyRequest,

    /**
     * The UpdateVolumeRequest model constructor.
     * @property {module:model/UpdateVolumeRequest}
     */
    UpdateVolumeRequest,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
     * The UserDefinedField model constructor.
     * @property {module:model/UserDefinedField}
     */
    UserDefinedField,

    /**
     * The ViewManagedSSHKey200Response model constructor.
     * @property {module:model/ViewManagedSSHKey200Response}
     */
    ViewManagedSSHKey200Response,

    /**
     * The ViewObjectStorageBucketACL200Response model constructor.
     * @property {module:model/ViewObjectStorageBucketACL200Response}
     */
    ViewObjectStorageBucketACL200Response,

    /**
     * The Vlans model constructor.
     * @property {module:model/Vlans}
     */
    Vlans,

    /**
     * The Volume model constructor.
     * @property {module:model/Volume}
     */
    Volume,

    /**
     * The WarningObject model constructor.
     * @property {module:model/WarningObject}
     */
    WarningObject,

    /**
    * The AccountApi service constructor.
    * @property {module:api/AccountApi}
    */
    AccountApi,

    /**
    * The DatabasesApi service constructor.
    * @property {module:api/DatabasesApi}
    */
    DatabasesApi,

    /**
    * The DomainsApi service constructor.
    * @property {module:api/DomainsApi}
    */
    DomainsApi,

    /**
    * The ImagesApi service constructor.
    * @property {module:api/ImagesApi}
    */
    ImagesApi,

    /**
    * The LinodeInstancesApi service constructor.
    * @property {module:api/LinodeInstancesApi}
    */
    LinodeInstancesApi,

    /**
    * The LinodeKubernetesEngineLKEApi service constructor.
    * @property {module:api/LinodeKubernetesEngineLKEApi}
    */
    LinodeKubernetesEngineLKEApi,

    /**
    * The LinodeTypesApi service constructor.
    * @property {module:api/LinodeTypesApi}
    */
    LinodeTypesApi,

    /**
    * The LongviewApi service constructor.
    * @property {module:api/LongviewApi}
    */
    LongviewApi,

    /**
    * The ManagedApi service constructor.
    * @property {module:api/ManagedApi}
    */
    ManagedApi,

    /**
    * The NetworkingApi service constructor.
    * @property {module:api/NetworkingApi}
    */
    NetworkingApi,

    /**
    * The NodeBalancersApi service constructor.
    * @property {module:api/NodeBalancersApi}
    */
    NodeBalancersApi,

    /**
    * The ObjectStorageApi service constructor.
    * @property {module:api/ObjectStorageApi}
    */
    ObjectStorageApi,

    /**
    * The ProfileApi service constructor.
    * @property {module:api/ProfileApi}
    */
    ProfileApi,

    /**
    * The RegionsApi service constructor.
    * @property {module:api/RegionsApi}
    */
    RegionsApi,

    /**
    * The StackScriptsApi service constructor.
    * @property {module:api/StackScriptsApi}
    */
    StackScriptsApi,

    /**
    * The SupportApi service constructor.
    * @property {module:api/SupportApi}
    */
    SupportApi,

    /**
    * The TagsApi service constructor.
    * @property {module:api/TagsApi}
    */
    TagsApi,

    /**
    * The VolumesApi service constructor.
    * @property {module:api/VolumesApi}
    */
    VolumesApi
};
