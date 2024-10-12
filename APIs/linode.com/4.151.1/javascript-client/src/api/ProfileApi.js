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
import AuthorizedApp from '../model/AuthorizedApp';
import CreatePersonalAccessTokenRequest from '../model/CreatePersonalAccessTokenRequest';
import GetAccountDefaultResponse from '../model/GetAccountDefaultResponse';
import GetAccountLogins200Response from '../model/GetAccountLogins200Response';
import GetDevices200Response from '../model/GetDevices200Response';
import GetPersonalAccessTokens200Response from '../model/GetPersonalAccessTokens200Response';
import GetProfileApps200Response from '../model/GetProfileApps200Response';
import GetSSHKeys200Response from '../model/GetSSHKeys200Response';
import GrantsResponse from '../model/GrantsResponse';
import Login from '../model/Login';
import PersonalAccessToken from '../model/PersonalAccessToken';
import PostProfilePhoneNumberRequest from '../model/PostProfilePhoneNumberRequest';
import PostProfilePhoneNumberVerifyRequest from '../model/PostProfilePhoneNumberVerifyRequest';
import Profile from '../model/Profile';
import SSHKey from '../model/SSHKey';
import SecurityQuestionsGet from '../model/SecurityQuestionsGet';
import SecurityQuestionsPost from '../model/SecurityQuestionsPost';
import TfaConfirm200Response from '../model/TfaConfirm200Response';
import TfaConfirmRequest from '../model/TfaConfirmRequest';
import TfaEnable200Response from '../model/TfaEnable200Response';
import TrustedDevice from '../model/TrustedDevice';
import UpdateSSHKeyRequest from '../model/UpdateSSHKeyRequest';

/**
* Profile service.
* @module api/ProfileApi
* @version 4.151.1
*/
export default class ProfileApi {

    /**
    * Constructs a new ProfileApi. 
    * @alias module:api/ProfileApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addSSHKey operation.
     * @callback module:api/ProfileApi~addSSHKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SSHKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * SSH Key Add
     * Adds an SSH Key to your Account profile. 
     * @param {Object} opts Optional parameters
     * @param {module:model/SSHKey} [sSHKey] Add SSH Key
     * @param {module:api/ProfileApi~addSSHKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SSHKey}
     */
    addSSHKey(opts, callback) {
      opts = opts || {};
      let postBody = opts['sSHKey'];

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
      let returnType = SSHKey;
      return this.apiClient.callApi(
        '/profile/sshkeys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPersonalAccessToken operation.
     * @callback module:api/ProfileApi~createPersonalAccessTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PersonalAccessToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Personal Access Token Create
     * Creates a Personal Access Token for your User. The raw token will be returned in the response, but will never be returned again afterward so be sure to take note of it. You may create a token with _at most_ the scopes of your current token. The created token will be able to access your Account until the given expiry, or until it is revoked. 
     * @param {module:model/CreatePersonalAccessTokenRequest} createPersonalAccessTokenRequest Information about the requested token.
     * @param {module:api/ProfileApi~createPersonalAccessTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PersonalAccessToken}
     */
    createPersonalAccessToken(createPersonalAccessTokenRequest, callback) {
      let postBody = createPersonalAccessTokenRequest;
      // verify the required parameter 'createPersonalAccessTokenRequest' is set
      if (createPersonalAccessTokenRequest === undefined || createPersonalAccessTokenRequest === null) {
        throw new Error("Missing the required parameter 'createPersonalAccessTokenRequest' when calling createPersonalAccessToken");
      }

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
      let returnType = PersonalAccessToken;
      return this.apiClient.callApi(
        '/profile/tokens', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePersonalAccessToken operation.
     * @callback module:api/ProfileApi~deletePersonalAccessTokenCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Personal Access Token Revoke
     * Revokes a Personal Access Token. The token will be invalidated immediately, and requests using that token will fail with a 401. It is possible to revoke access to the token making the request to revoke a token, but keep in mind that doing so could lose you access to the api and require you to create a new token through some other means. 
     * @param {Number} tokenId The ID of the token to access.
     * @param {module:api/ProfileApi~deletePersonalAccessTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deletePersonalAccessToken(tokenId, callback) {
      let postBody = null;
      // verify the required parameter 'tokenId' is set
      if (tokenId === undefined || tokenId === null) {
        throw new Error("Missing the required parameter 'tokenId' when calling deletePersonalAccessToken");
      }

      let pathParams = {
        'tokenId': tokenId
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
        '/profile/tokens/{tokenId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteProfileApp operation.
     * @callback module:api/ProfileApi~deleteProfileAppCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * App Access Revoke
     * Expires this app token. This token may no longer be used to access your Account. 
     * @param {Number} appId The authorized app ID to manage.
     * @param {module:api/ProfileApi~deleteProfileAppCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteProfileApp(appId, callback) {
      let postBody = null;
      // verify the required parameter 'appId' is set
      if (appId === undefined || appId === null) {
        throw new Error("Missing the required parameter 'appId' when calling deleteProfileApp");
      }

      let pathParams = {
        'appId': appId
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
        '/profile/apps/{appId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteProfilePhoneNumber operation.
     * @callback module:api/ProfileApi~deleteProfilePhoneNumberCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Phone Number Delete
     * Delete the verified phone number for the User making this request.  Use this command to opt out of SMS messages for the requesting User after a phone number has been verified with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command. 
     * @param {module:api/ProfileApi~deleteProfilePhoneNumberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteProfilePhoneNumber(callback) {
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/profile/phone-number', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteSSHKey operation.
     * @callback module:api/ProfileApi~deleteSSHKeyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * SSH Key Delete
     * Deletes an SSH Key you have access to.  **Note:** deleting an SSH Key will *not* remove it from any Linode or Disk that was deployed with `authorized_keys`. In those cases, the keys must be manually deleted on the Linode or Disk. This endpoint will only delete the key's association from your Profile. 
     * @param {Number} sshKeyId The ID of the SSHKey
     * @param {module:api/ProfileApi~deleteSSHKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteSSHKey(sshKeyId, callback) {
      let postBody = null;
      // verify the required parameter 'sshKeyId' is set
      if (sshKeyId === undefined || sshKeyId === null) {
        throw new Error("Missing the required parameter 'sshKeyId' when calling deleteSSHKey");
      }

      let pathParams = {
        'sshKeyId': sshKeyId
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
        '/profile/sshkeys/{sshKeyId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDevices operation.
     * @callback module:api/ProfileApi~getDevicesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDevices200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trusted Devices List
     * Returns a paginated list of active TrustedDevices for your User. Browsers with an active Remember Me Session are logged into your account until the session expires or is revoked. 
     * @param {module:api/ProfileApi~getDevicesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDevices200Response}
     */
    getDevices(callback) {
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
      let returnType = GetDevices200Response;
      return this.apiClient.callApi(
        '/profile/devices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPersonalAccessToken operation.
     * @callback module:api/ProfileApi~getPersonalAccessTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PersonalAccessToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Personal Access Token View
     * Returns a single Personal Access Token. 
     * @param {Number} tokenId The ID of the token to access.
     * @param {module:api/ProfileApi~getPersonalAccessTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PersonalAccessToken}
     */
    getPersonalAccessToken(tokenId, callback) {
      let postBody = null;
      // verify the required parameter 'tokenId' is set
      if (tokenId === undefined || tokenId === null) {
        throw new Error("Missing the required parameter 'tokenId' when calling getPersonalAccessToken");
      }

      let pathParams = {
        'tokenId': tokenId
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
      let returnType = PersonalAccessToken;
      return this.apiClient.callApi(
        '/profile/tokens/{tokenId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPersonalAccessTokens operation.
     * @callback module:api/ProfileApi~getPersonalAccessTokensCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPersonalAccessTokens200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Personal Access Tokens List
     * Returns a paginated list of Personal Access Tokens currently active for your User. 
     * @param {module:api/ProfileApi~getPersonalAccessTokensCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPersonalAccessTokens200Response}
     */
    getPersonalAccessTokens(callback) {
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
      let returnType = GetPersonalAccessTokens200Response;
      return this.apiClient.callApi(
        '/profile/tokens', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProfile operation.
     * @callback module:api/ProfileApi~getProfileCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Profile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Profile View
     * Returns information about the current User. This can be used to see who is acting in applications where more than one token is managed. For example, in third-party OAuth applications.  This endpoint is always accessible, no matter what OAuth scopes the acting token has. 
     * @param {module:api/ProfileApi~getProfileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Profile}
     */
    getProfile(callback) {
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
      let returnType = Profile;
      return this.apiClient.callApi(
        '/profile', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProfileApp operation.
     * @callback module:api/ProfileApi~getProfileAppCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthorizedApp} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Authorized App View
     * Returns information about a single app you've authorized to access your Account. 
     * @param {Number} appId The authorized app ID to manage.
     * @param {module:api/ProfileApi~getProfileAppCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthorizedApp}
     */
    getProfileApp(appId, callback) {
      let postBody = null;
      // verify the required parameter 'appId' is set
      if (appId === undefined || appId === null) {
        throw new Error("Missing the required parameter 'appId' when calling getProfileApp");
      }

      let pathParams = {
        'appId': appId
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
      let returnType = AuthorizedApp;
      return this.apiClient.callApi(
        '/profile/apps/{appId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProfileApps operation.
     * @callback module:api/ProfileApi~getProfileAppsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetProfileApps200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Authorized Apps List
     * This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ProfileApi~getProfileAppsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetProfileApps200Response}
     */
    getProfileApps(opts, callback) {
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
      let returnType = GetProfileApps200Response;
      return this.apiClient.callApi(
        '/profile/apps', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProfileGrants operation.
     * @callback module:api/ProfileApi~getProfileGrantsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GrantsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Grants List
     * This returns a GrantsResponse describing what the acting User has been granted access to.  For unrestricted users, this will return a  204 and no body because unrestricted users have access to everything without grants.  This will not return information about entities you do not have access to.  This endpoint is useful when writing third-party OAuth applications to see what options you should present to the acting User.  For example, if they do not have `global.add_linodes`, you might not display a button to deploy a new Linode.  Any client may access this endpoint; no OAuth scopes are required. 
     * @param {module:api/ProfileApi~getProfileGrantsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GrantsResponse}
     */
    getProfileGrants(callback) {
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
      let returnType = GrantsResponse;
      return this.apiClient.callApi(
        '/profile/grants', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProfileLogin operation.
     * @callback module:api/ProfileApi~getProfileLoginCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Login} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Login View
     * Returns a login object displaying information about a successful account login from this user. 
     * @param {Number} loginId The ID of the login object to access.
     * @param {module:api/ProfileApi~getProfileLoginCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Login}
     */
    getProfileLogin(loginId, callback) {
      let postBody = null;
      // verify the required parameter 'loginId' is set
      if (loginId === undefined || loginId === null) {
        throw new Error("Missing the required parameter 'loginId' when calling getProfileLogin");
      }

      let pathParams = {
        'loginId': loginId
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
      let returnType = Login;
      return this.apiClient.callApi(
        '/profile/logins/{loginId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getProfileLogins operation.
     * @callback module:api/ProfileApi~getProfileLoginsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAccountLogins200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Logins List
     * Returns a collection of successful account logins from this user during the last 90 days. 
     * @param {module:api/ProfileApi~getProfileLoginsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAccountLogins200Response}
     */
    getProfileLogins(callback) {
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
      let returnType = GetAccountLogins200Response;
      return this.apiClient.callApi(
        '/profile/logins', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSSHKey operation.
     * @callback module:api/ProfileApi~getSSHKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SSHKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * SSH Key View
     * Returns a single SSH Key object identified by `id` that you have access to view. 
     * @param {Number} sshKeyId The ID of the SSHKey
     * @param {module:api/ProfileApi~getSSHKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SSHKey}
     */
    getSSHKey(sshKeyId, callback) {
      let postBody = null;
      // verify the required parameter 'sshKeyId' is set
      if (sshKeyId === undefined || sshKeyId === null) {
        throw new Error("Missing the required parameter 'sshKeyId' when calling getSSHKey");
      }

      let pathParams = {
        'sshKeyId': sshKeyId
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
      let returnType = SSHKey;
      return this.apiClient.callApi(
        '/profile/sshkeys/{sshKeyId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSSHKeys operation.
     * @callback module:api/ProfileApi~getSSHKeysCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSSHKeys200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * SSH Keys List
     * Returns a collection of SSH Keys you've added to your Profile. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ProfileApi~getSSHKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSSHKeys200Response}
     */
    getSSHKeys(opts, callback) {
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
      let returnType = GetSSHKeys200Response;
      return this.apiClient.callApi(
        '/profile/sshkeys', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSecurityQuestions operation.
     * @callback module:api/ProfileApi~getSecurityQuestionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SecurityQuestionsGet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Security Questions List
     * Returns a collection of security questions and their responses, if any, for your User Profile. 
     * @param {module:api/ProfileApi~getSecurityQuestionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SecurityQuestionsGet}
     */
    getSecurityQuestions(opts, callback) {
      opts = opts || {};
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
      let returnType = SecurityQuestionsGet;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/profile/security-questions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getTrustedDevice operation.
     * @callback module:api/ProfileApi~getTrustedDeviceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TrustedDevice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trusted Device View
     * Returns a single active TrustedDevice for your User. 
     * @param {Number} deviceId The ID of the TrustedDevice
     * @param {module:api/ProfileApi~getTrustedDeviceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TrustedDevice}
     */
    getTrustedDevice(deviceId, callback) {
      let postBody = null;
      // verify the required parameter 'deviceId' is set
      if (deviceId === undefined || deviceId === null) {
        throw new Error("Missing the required parameter 'deviceId' when calling getTrustedDevice");
      }

      let pathParams = {
        'deviceId': deviceId
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
      let returnType = TrustedDevice;
      return this.apiClient.callApi(
        '/profile/devices/{deviceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUserPreferences operation.
     * @callback module:api/ProfileApi~getUserPreferencesCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User Preferences View
     * View a list of user preferences tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user's font size preference or preferred display name. User preferences are available for each OAuth client registered to your account, and as such an account can have multiple user preferences. 
     * @param {module:api/ProfileApi~getUserPreferencesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getUserPreferences(callback) {
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/profile/preferences', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postProfilePhoneNumber operation.
     * @callback module:api/ProfileApi~postProfilePhoneNumberCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Phone Number Verification Code Send
     * Send a one-time verification code via SMS message to the submitted phone number. Providing your phone number helps ensure you can securely access your Account in case other ways to connect are lost. Your phone number is only used to verify your identity by sending an SMS message. Standard carrier messaging fees may apply.  * By accessing this command you are opting in to receive SMS messages. You can opt out of SMS messages by using the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command after your phone number is verified.  * Verification codes are valid for 10 minutes after they are sent.  * Subsequent requests made prior to code expiration result in sending the same code.  Once a verification code is received, verify your phone number with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command. 
     * @param {Object} opts Optional parameters
     * @param {module:model/PostProfilePhoneNumberRequest} [postProfilePhoneNumberRequest] Enter a phone number and country code for verification.
     * @param {module:api/ProfileApi~postProfilePhoneNumberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postProfilePhoneNumber(opts, callback) {
      opts = opts || {};
      let postBody = opts['postProfilePhoneNumberRequest'];

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
      let returnType = Object;
      return this.apiClient.callApi(
        '/profile/phone-number', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postProfilePhoneNumberVerify operation.
     * @callback module:api/ProfileApi~postProfilePhoneNumberVerifyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Phone Number Verify
     * Verify a phone number by confirming the one-time code received via SMS message after accessing the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command.  * Verification codes are valid for 10 minutes after they are sent.  * Only the same User that made the verification code request can use that code with this command.  Once completed, the verified phone number is assigned to the User making the request. To change the verified phone number for a User, first use the **Phone Number Delete** ([DELETE /profile/phone-number](/docs/api/profile/#phone-number-delete)) command, then begin the verification process again with the **Phone Verification Code Send** ([POST /profile/phone-number](/docs/api/profile/#phone-number-verification-code-send)) command. 
     * @param {Object} opts Optional parameters
     * @param {module:model/PostProfilePhoneNumberVerifyRequest} [postProfilePhoneNumberVerifyRequest] Enter a phone verification code for confirmation.
     * @param {module:api/ProfileApi~postProfilePhoneNumberVerifyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postProfilePhoneNumberVerify(opts, callback) {
      opts = opts || {};
      let postBody = opts['postProfilePhoneNumberVerifyRequest'];

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
      let returnType = Object;
      return this.apiClient.callApi(
        '/profile/phone-number/verify', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSecurityQuestions operation.
     * @callback module:api/ProfileApi~postSecurityQuestionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SecurityQuestionsPost} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Security Questions Answer
     * Adds security question responses for your User.  Requires exactly three unique questions.  Previous responses are overwritten if answered or reset to `null` if unanswered.  **Note**: Security questions must be answered for your User prior to accessing the **Two Factor Secret Create** ([POST /profile/tfa-enable](/docs/api/profile/#two-factor-secret-create)) command. 
     * @param {Object} opts Optional parameters
     * @param {module:model/SecurityQuestionsPost} [securityQuestionsPost] Answer Security Questions
     * @param {module:api/ProfileApi~postSecurityQuestionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SecurityQuestionsPost}
     */
    postSecurityQuestions(opts, callback) {
      opts = opts || {};
      let postBody = opts['securityQuestionsPost'];

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
      let returnType = SecurityQuestionsPost;
      return this.apiClient.callApi(
        '/profile/security-questions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the revokeTrustedDevice operation.
     * @callback module:api/ProfileApi~revokeTrustedDeviceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trusted Device Revoke
     * Revoke an active TrustedDevice for your User.  Once a TrustedDevice is revoked, this device will have to log in again before accessing your Linode account. 
     * @param {Number} deviceId The ID of the TrustedDevice
     * @param {module:api/ProfileApi~revokeTrustedDeviceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    revokeTrustedDevice(deviceId, callback) {
      let postBody = null;
      // verify the required parameter 'deviceId' is set
      if (deviceId === undefined || deviceId === null) {
        throw new Error("Missing the required parameter 'deviceId' when calling revokeTrustedDevice");
      }

      let pathParams = {
        'deviceId': deviceId
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
        '/profile/devices/{deviceId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tfaConfirm operation.
     * @callback module:api/ProfileApi~tfaConfirmCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TfaConfirm200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Two Factor Authentication Confirm/Enable
     * Confirms that you can successfully generate Two Factor codes and enables TFA on your Account. Once this is complete, login attempts from untrusted computers will be required to provide a Two Factor code before they are successful. 
     * @param {module:model/TfaConfirmRequest} tfaConfirmRequest The Two Factor code you generated with your Two Factor secret.
     * @param {module:api/ProfileApi~tfaConfirmCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TfaConfirm200Response}
     */
    tfaConfirm(tfaConfirmRequest, callback) {
      let postBody = tfaConfirmRequest;
      // verify the required parameter 'tfaConfirmRequest' is set
      if (tfaConfirmRequest === undefined || tfaConfirmRequest === null) {
        throw new Error("Missing the required parameter 'tfaConfirmRequest' when calling tfaConfirm");
      }

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
      let returnType = TfaConfirm200Response;
      return this.apiClient.callApi(
        '/profile/tfa-enable-confirm', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tfaDisable operation.
     * @callback module:api/ProfileApi~tfaDisableCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Two Factor Authentication Disable
     * Disables Two Factor Authentication for your User. Once successful, login attempts from untrusted computers will only require a password before being successful. This is less secure, and is discouraged. 
     * @param {module:api/ProfileApi~tfaDisableCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    tfaDisable(callback) {
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/profile/tfa-disable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tfaEnable operation.
     * @callback module:api/ProfileApi~tfaEnableCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TfaEnable200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Two Factor Secret Create
     * Generates a Two Factor secret for your User. To enable TFA for your User, enter the secret obtained from this command with the **Two Factor Authentication Confirm/Enable** ([POST /profile/tfa-enable-confirm](/docs/api/profile/#two-factor-authentication-confirmenable)) command. Once enabled, logins from untrusted computers are required to provide a TFA code before they are successful.  **Note**: Before you can enable TFA, security questions must be answered for your User by accessing the **Security Questions Answer** ([POST /profile/security-questions](/docs/api/profile/#security-questions-answer)) command. 
     * @param {module:api/ProfileApi~tfaEnableCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TfaEnable200Response}
     */
    tfaEnable(callback) {
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
      let returnType = TfaEnable200Response;
      return this.apiClient.callApi(
        '/profile/tfa-enable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePersonalAccessToken operation.
     * @callback module:api/ProfileApi~updatePersonalAccessTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PersonalAccessToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Personal Access Token Update
     * Updates a Personal Access Token. 
     * @param {Number} tokenId The ID of the token to access.
     * @param {module:model/PersonalAccessToken} personalAccessToken The fields to update.
     * @param {module:api/ProfileApi~updatePersonalAccessTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PersonalAccessToken}
     */
    updatePersonalAccessToken(tokenId, personalAccessToken, callback) {
      let postBody = personalAccessToken;
      // verify the required parameter 'tokenId' is set
      if (tokenId === undefined || tokenId === null) {
        throw new Error("Missing the required parameter 'tokenId' when calling updatePersonalAccessToken");
      }
      // verify the required parameter 'personalAccessToken' is set
      if (personalAccessToken === undefined || personalAccessToken === null) {
        throw new Error("Missing the required parameter 'personalAccessToken' when calling updatePersonalAccessToken");
      }

      let pathParams = {
        'tokenId': tokenId
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
      let returnType = PersonalAccessToken;
      return this.apiClient.callApi(
        '/profile/tokens/{tokenId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateProfile operation.
     * @callback module:api/ProfileApi~updateProfileCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Profile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Profile Update
     * Update information in your Profile.  This endpoint requires the \"account:read_write\" OAuth Scope. 
     * @param {module:model/Profile} profile The fields to update.
     * @param {module:api/ProfileApi~updateProfileCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Profile}
     */
    updateProfile(profile, callback) {
      let postBody = profile;
      // verify the required parameter 'profile' is set
      if (profile === undefined || profile === null) {
        throw new Error("Missing the required parameter 'profile' when calling updateProfile");
      }

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
      let returnType = Profile;
      return this.apiClient.callApi(
        '/profile', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateSSHKey operation.
     * @callback module:api/ProfileApi~updateSSHKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SSHKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * SSH Key Update
     * Updates an SSH Key that you have permission to `read_write`.  Only SSH key labels can be updated. 
     * @param {Number} sshKeyId The ID of the SSHKey
     * @param {module:model/UpdateSSHKeyRequest} updateSSHKeyRequest The fields to update. 
     * @param {module:api/ProfileApi~updateSSHKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SSHKey}
     */
    updateSSHKey(sshKeyId, updateSSHKeyRequest, callback) {
      let postBody = updateSSHKeyRequest;
      // verify the required parameter 'sshKeyId' is set
      if (sshKeyId === undefined || sshKeyId === null) {
        throw new Error("Missing the required parameter 'sshKeyId' when calling updateSSHKey");
      }
      // verify the required parameter 'updateSSHKeyRequest' is set
      if (updateSSHKeyRequest === undefined || updateSSHKeyRequest === null) {
        throw new Error("Missing the required parameter 'updateSSHKeyRequest' when calling updateSSHKey");
      }

      let pathParams = {
        'sshKeyId': sshKeyId
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
      let returnType = SSHKey;
      return this.apiClient.callApi(
        '/profile/sshkeys/{sshKeyId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateUserPreferences operation.
     * @callback module:api/ProfileApi~updateUserPreferencesCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User Preferences Update
     * Updates a user's preferences. These preferences are tied to the OAuth client that generated the token making the request. The user preferences endpoints allow consumers of the API to store arbitrary JSON data, such as a user's font size preference or preferred display name. An account may have multiple preferences. Preferences, and the pertaining request body, may contain any arbitrary JSON data that the user would like to store. 
     * @param {Object.<String, Object>} body The user preferences to update or store. 
     * @param {module:api/ProfileApi~updateUserPreferencesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateUserPreferences(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateUserPreferences");
      }

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
      let returnType = Object;
      return this.apiClient.callApi(
        '/profile/preferences', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
