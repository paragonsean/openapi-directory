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


import ApiClient from "../ApiClient";
import CreateManagedCredentialRequest from '../model/CreateManagedCredentialRequest';
import GetAccountDefaultResponse from '../model/GetAccountDefaultResponse';
import GetManagedContacts200Response from '../model/GetManagedContacts200Response';
import GetManagedCredentials200Response from '../model/GetManagedCredentials200Response';
import GetManagedIssues200Response from '../model/GetManagedIssues200Response';
import GetManagedLinodeSettings200Response from '../model/GetManagedLinodeSettings200Response';
import GetManagedServices200Response from '../model/GetManagedServices200Response';
import GetManagedStats200Response from '../model/GetManagedStats200Response';
import ManagedContact from '../model/ManagedContact';
import ManagedCredential from '../model/ManagedCredential';
import ManagedIssue from '../model/ManagedIssue';
import ManagedLinodeSettings from '../model/ManagedLinodeSettings';
import ManagedService from '../model/ManagedService';
import UpdateManagedCredentialUsernamePasswordRequest from '../model/UpdateManagedCredentialUsernamePasswordRequest';
import ViewManagedSSHKey200Response from '../model/ViewManagedSSHKey200Response';

/**
* Managed service.
* @module api/ManagedApi
* @version 4.151.1
*/
export default class ManagedApi {

    /**
    * Constructs a new ManagedApi. 
    * @alias module:api/ManagedApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createManagedContact operation.
     * @callback module:api/ManagedApi~createManagedContactCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedContact} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Contact Create
     * Creates a Managed Contact.  A Managed Contact is someone Linode special forces can contact in the course of attempting to resolve an issue with a Managed Service.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {module:model/ManagedContact} [managedContact] Information about the contact to create.
     * @param {module:api/ManagedApi~createManagedContactCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedContact}
     */
    createManagedContact(opts, callback) {
      opts = opts || {};
      let postBody = opts['managedContact'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedContact;
      return this.apiClient.callApi(
        '/managed/contacts', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createManagedCredential operation.
     * @callback module:api/ManagedApi~createManagedCredentialCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedCredential} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Credential Create
     * Creates a Managed Credential. A Managed Credential is stored securely to allow Linode special forces to access your Managed Services and resolve issues.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateManagedCredentialRequest} [createManagedCredentialRequest] Information about the Credential to create.
     * @param {module:api/ManagedApi~createManagedCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedCredential}
     */
    createManagedCredential(opts, callback) {
      opts = opts || {};
      let postBody = opts['createManagedCredentialRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedCredential;
      return this.apiClient.callApi(
        '/managed/credentials', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createManagedService operation.
     * @callback module:api/ManagedApi~createManagedServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedService} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Service Create
     * Creates a Managed Service. Linode Managed will begin monitoring this service and reporting and attempting to resolve any Issues.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {module:model/ManagedService} [managedService] Information about the service to monitor.
     * @param {module:api/ManagedApi~createManagedServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedService}
     */
    createManagedService(opts, callback) {
      opts = opts || {};
      let postBody = opts['managedService'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedService;
      return this.apiClient.callApi(
        '/managed/services', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteManagedContact operation.
     * @callback module:api/ManagedApi~deleteManagedContactCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Contact Delete
     * Deletes a Managed Contact.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} contactId The ID of the contact to access.
     * @param {module:api/ManagedApi~deleteManagedContactCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteManagedContact(contactId, callback) {
      let postBody = null;
      // verify the required parameter 'contactId' is set
      if (contactId === undefined || contactId === null) {
        throw new Error("Missing the required parameter 'contactId' when calling deleteManagedContact");
      }

      let pathParams = {
        'contactId': contactId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/managed/contacts/{contactId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteManagedCredential operation.
     * @callback module:api/ManagedApi~deleteManagedCredentialCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Credential Delete
     * Deletes a Managed Credential.  Linode special forces will no longer have access to this Credential when attempting to resolve issues.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} credentialId The ID of the Credential to access.
     * @param {module:api/ManagedApi~deleteManagedCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteManagedCredential(credentialId, callback) {
      let postBody = null;
      // verify the required parameter 'credentialId' is set
      if (credentialId === undefined || credentialId === null) {
        throw new Error("Missing the required parameter 'credentialId' when calling deleteManagedCredential");
      }

      let pathParams = {
        'credentialId': credentialId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/managed/credentials/{credentialId}/revoke', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteManagedService operation.
     * @callback module:api/ManagedApi~deleteManagedServiceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Service Delete
     * Deletes a Managed Service.  This service will no longer be monitored by Linode Managed.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} serviceId The ID of the Managed Service to access.
     * @param {module:api/ManagedApi~deleteManagedServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteManagedService(serviceId, callback) {
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling deleteManagedService");
      }

      let pathParams = {
        'serviceId': serviceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/managed/services/{serviceId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disableManagedService operation.
     * @callback module:api/ManagedApi~disableManagedServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedService} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Service Disable
     * Temporarily disables monitoring of a Managed Service.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} serviceId The ID of the Managed Service to disable.
     * @param {module:api/ManagedApi~disableManagedServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedService}
     */
    disableManagedService(serviceId, callback) {
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling disableManagedService");
      }

      let pathParams = {
        'serviceId': serviceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedService;
      return this.apiClient.callApi(
        '/managed/services/{serviceId}/disable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the enableManagedService operation.
     * @callback module:api/ManagedApi~enableManagedServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedService} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Service Enable
     * Enables monitoring of a Managed Service.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} serviceId The ID of the Managed Service to enable.
     * @param {module:api/ManagedApi~enableManagedServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedService}
     */
    enableManagedService(serviceId, callback) {
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling enableManagedService");
      }

      let pathParams = {
        'serviceId': serviceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedService;
      return this.apiClient.callApi(
        '/managed/services/{serviceId}/enable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedContact operation.
     * @callback module:api/ManagedApi~getManagedContactCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedContact} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Contact View
     * Returns a single Managed Contact.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} contactId The ID of the contact to access.
     * @param {module:api/ManagedApi~getManagedContactCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedContact}
     */
    getManagedContact(contactId, callback) {
      let postBody = null;
      // verify the required parameter 'contactId' is set
      if (contactId === undefined || contactId === null) {
        throw new Error("Missing the required parameter 'contactId' when calling getManagedContact");
      }

      let pathParams = {
        'contactId': contactId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedContact;
      return this.apiClient.callApi(
        '/managed/contacts/{contactId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedContacts operation.
     * @callback module:api/ManagedApi~getManagedContactsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetManagedContacts200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Contacts List
     * Returns a paginated list of Managed Contacts on your Account.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ManagedApi~getManagedContactsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetManagedContacts200Response}
     */
    getManagedContacts(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page': opts['page'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetManagedContacts200Response;
      return this.apiClient.callApi(
        '/managed/contacts', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedCredential operation.
     * @callback module:api/ManagedApi~getManagedCredentialCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedCredential} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Credential View
     * Returns a single Managed Credential.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} credentialId The ID of the Credential to access.
     * @param {module:api/ManagedApi~getManagedCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedCredential}
     */
    getManagedCredential(credentialId, callback) {
      let postBody = null;
      // verify the required parameter 'credentialId' is set
      if (credentialId === undefined || credentialId === null) {
        throw new Error("Missing the required parameter 'credentialId' when calling getManagedCredential");
      }

      let pathParams = {
        'credentialId': credentialId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedCredential;
      return this.apiClient.callApi(
        '/managed/credentials/{credentialId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedCredentials operation.
     * @callback module:api/ManagedApi~getManagedCredentialsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetManagedCredentials200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Credentials List
     * Returns a paginated list of Managed Credentials on your Account.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ManagedApi~getManagedCredentialsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetManagedCredentials200Response}
     */
    getManagedCredentials(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page': opts['page'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetManagedCredentials200Response;
      return this.apiClient.callApi(
        '/managed/credentials', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedIssue operation.
     * @callback module:api/ManagedApi~getManagedIssueCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedIssue} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Issue View
     * Returns a single Issue that is impacting or did impact one of your Managed Services.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} issueId The Issue to look up.
     * @param {module:api/ManagedApi~getManagedIssueCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedIssue}
     */
    getManagedIssue(issueId, callback) {
      let postBody = null;
      // verify the required parameter 'issueId' is set
      if (issueId === undefined || issueId === null) {
        throw new Error("Missing the required parameter 'issueId' when calling getManagedIssue");
      }

      let pathParams = {
        'issueId': issueId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedIssue;
      return this.apiClient.callApi(
        '/managed/issues/{issueId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedIssues operation.
     * @callback module:api/ManagedApi~getManagedIssuesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetManagedIssues200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Issues List
     * Returns a paginated list of recent and ongoing issues detected on your Managed Services.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ManagedApi~getManagedIssuesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetManagedIssues200Response}
     */
    getManagedIssues(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page': opts['page'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetManagedIssues200Response;
      return this.apiClient.callApi(
        '/managed/issues', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedLinodeSetting operation.
     * @callback module:api/ManagedApi~getManagedLinodeSettingCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedLinodeSettings} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode's Managed Settings View
     * Returns a single Linode's Managed settings.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} linodeId The Linode ID whose settings we are accessing.
     * @param {module:api/ManagedApi~getManagedLinodeSettingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedLinodeSettings}
     */
    getManagedLinodeSetting(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getManagedLinodeSetting");
      }

      let pathParams = {
        'linodeId': linodeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedLinodeSettings;
      return this.apiClient.callApi(
        '/managed/linode-settings/{linodeId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedLinodeSettings operation.
     * @callback module:api/ManagedApi~getManagedLinodeSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetManagedLinodeSettings200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Linode Settings List
     * Returns a paginated list of Managed Settings for your Linodes. There will be one entry per Linode on your Account.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ManagedApi~getManagedLinodeSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetManagedLinodeSettings200Response}
     */
    getManagedLinodeSettings(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page': opts['page'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetManagedLinodeSettings200Response;
      return this.apiClient.callApi(
        '/managed/linode-settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedService operation.
     * @callback module:api/ManagedApi~getManagedServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedService} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Service View
     * Returns information about a single Managed Service on your Account.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} serviceId The ID of the Managed Service to access.
     * @param {module:api/ManagedApi~getManagedServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedService}
     */
    getManagedService(serviceId, callback) {
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling getManagedService");
      }

      let pathParams = {
        'serviceId': serviceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ManagedService;
      return this.apiClient.callApi(
        '/managed/services/{serviceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedServices operation.
     * @callback module:api/ManagedApi~getManagedServicesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetManagedServices200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Services List
     * Returns a paginated list of Managed Services on your Account. These are the services Linode Managed is monitoring and will report and attempt to resolve issues with.  This command can only be accessed by the unrestricted users of an account. 
     * @param {module:api/ManagedApi~getManagedServicesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetManagedServices200Response}
     */
    getManagedServices(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetManagedServices200Response;
      return this.apiClient.callApi(
        '/managed/services', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getManagedStats operation.
     * @callback module:api/ManagedApi~getManagedStatsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetManagedStats200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Stats List
     * Returns a list of Managed Stats on your Account in the form of x and y data points. You can use these data points to plot your own graph visualizations. These stats reflect the last 24 hours of combined usage across all managed Linodes on your account giving you a high-level snapshot of data for the following:   * cpu * disk * swap * network in * network out  This command can only be accessed by the unrestricted users of an account. 
     * @param {module:api/ManagedApi~getManagedStatsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetManagedStats200Response}
     */
    getManagedStats(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetManagedStats200Response;
      return this.apiClient.callApi(
        '/managed/stats', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateManagedContact operation.
     * @callback module:api/ManagedApi~updateManagedContactCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedContact} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Contact Update
     * Updates information about a Managed Contact. This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} contactId The ID of the contact to access.
     * @param {module:model/ManagedContact} managedContact The fields to update.
     * @param {module:api/ManagedApi~updateManagedContactCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedContact}
     */
    updateManagedContact(contactId, managedContact, callback) {
      let postBody = managedContact;
      // verify the required parameter 'contactId' is set
      if (contactId === undefined || contactId === null) {
        throw new Error("Missing the required parameter 'contactId' when calling updateManagedContact");
      }
      // verify the required parameter 'managedContact' is set
      if (managedContact === undefined || managedContact === null) {
        throw new Error("Missing the required parameter 'managedContact' when calling updateManagedContact");
      }

      let pathParams = {
        'contactId': contactId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedContact;
      return this.apiClient.callApi(
        '/managed/contacts/{contactId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateManagedCredential operation.
     * @callback module:api/ManagedApi~updateManagedCredentialCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedCredential} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Credential Update
     * Updates the label of a Managed Credential. This endpoint does not update the username and password for a Managed Credential. To do this, use the Managed Credential Username and Password Update ([POST /managed/credentials/{credentialId}/update](/docs/api/managed/#managed-credential-username-and-password-update)) endpoint instead. This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} credentialId The ID of the Credential to access.
     * @param {module:model/ManagedCredential} managedCredential The fields to update.
     * @param {module:api/ManagedApi~updateManagedCredentialCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedCredential}
     */
    updateManagedCredential(credentialId, managedCredential, callback) {
      let postBody = managedCredential;
      // verify the required parameter 'credentialId' is set
      if (credentialId === undefined || credentialId === null) {
        throw new Error("Missing the required parameter 'credentialId' when calling updateManagedCredential");
      }
      // verify the required parameter 'managedCredential' is set
      if (managedCredential === undefined || managedCredential === null) {
        throw new Error("Missing the required parameter 'managedCredential' when calling updateManagedCredential");
      }

      let pathParams = {
        'credentialId': credentialId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedCredential;
      return this.apiClient.callApi(
        '/managed/credentials/{credentialId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateManagedCredentialUsernamePassword operation.
     * @callback module:api/ManagedApi~updateManagedCredentialUsernamePasswordCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Credential Username and Password Update
     * Updates the username and password for a Managed Credential.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} credentialId The ID of the Credential to update.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateManagedCredentialUsernamePasswordRequest} [updateManagedCredentialUsernamePasswordRequest] The new username and password to assign to the Managed Credential. 
     * @param {module:api/ManagedApi~updateManagedCredentialUsernamePasswordCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateManagedCredentialUsernamePassword(credentialId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateManagedCredentialUsernamePasswordRequest'];
      // verify the required parameter 'credentialId' is set
      if (credentialId === undefined || credentialId === null) {
        throw new Error("Missing the required parameter 'credentialId' when calling updateManagedCredentialUsernamePassword");
      }

      let pathParams = {
        'credentialId': credentialId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/managed/credentials/{credentialId}/update', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateManagedLinodeSetting operation.
     * @callback module:api/ManagedApi~updateManagedLinodeSettingCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedLinodeSettings} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode's Managed Settings Update
     * Updates a single Linode's Managed settings. This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} linodeId The Linode ID whose settings we are accessing.
     * @param {module:model/ManagedLinodeSettings} managedLinodeSettings The settings to update.
     * @param {module:api/ManagedApi~updateManagedLinodeSettingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedLinodeSettings}
     */
    updateManagedLinodeSetting(linodeId, managedLinodeSettings, callback) {
      let postBody = managedLinodeSettings;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling updateManagedLinodeSetting");
      }
      // verify the required parameter 'managedLinodeSettings' is set
      if (managedLinodeSettings === undefined || managedLinodeSettings === null) {
        throw new Error("Missing the required parameter 'managedLinodeSettings' when calling updateManagedLinodeSetting");
      }

      let pathParams = {
        'linodeId': linodeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedLinodeSettings;
      return this.apiClient.callApi(
        '/managed/linode-settings/{linodeId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateManagedService operation.
     * @callback module:api/ManagedApi~updateManagedServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ManagedService} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Service Update
     * Updates information about a Managed Service.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Number} serviceId The ID of the Managed Service to access.
     * @param {module:model/ManagedService} managedService The fields to update.
     * @param {module:api/ManagedApi~updateManagedServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ManagedService}
     */
    updateManagedService(serviceId, managedService, callback) {
      let postBody = managedService;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling updateManagedService");
      }
      // verify the required parameter 'managedService' is set
      if (managedService === undefined || managedService === null) {
        throw new Error("Missing the required parameter 'managedService' when calling updateManagedService");
      }

      let pathParams = {
        'serviceId': serviceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ManagedService;
      return this.apiClient.callApi(
        '/managed/services/{serviceId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the viewManagedSSHKey operation.
     * @callback module:api/ManagedApi~viewManagedSSHKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ViewManagedSSHKey200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed SSH Key View
     * Returns the unique SSH public key assigned to your Linode account's Managed service. If you [add this public key](/docs/guides/linode-managed/#adding-the-public-key) to a Linode on your account, Linode special forces will be able to log in to the Linode with this key when attempting to resolve issues.  This command can only be accessed by the unrestricted users of an account. 
     * @param {module:api/ManagedApi~viewManagedSSHKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ViewManagedSSHKey200Response}
     */
    viewManagedSSHKey(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ViewManagedSSHKey200Response;
      return this.apiClient.callApi(
        '/managed/credentials/sshkey', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
