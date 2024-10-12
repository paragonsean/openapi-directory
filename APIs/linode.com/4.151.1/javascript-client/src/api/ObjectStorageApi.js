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
import CreateObjectStorageBucketRequest from '../model/CreateObjectStorageBucketRequest';
import CreateObjectStorageObjectURL200Response from '../model/CreateObjectStorageObjectURL200Response';
import CreateObjectStorageObjectURLRequest from '../model/CreateObjectStorageObjectURLRequest';
import GetAccountDefaultResponse from '../model/GetAccountDefaultResponse';
import GetObjectStorageBucketContent200Response from '../model/GetObjectStorageBucketContent200Response';
import GetObjectStorageBuckets200Response from '../model/GetObjectStorageBuckets200Response';
import GetObjectStorageClusters200Response from '../model/GetObjectStorageClusters200Response';
import GetObjectStorageKeys200Response from '../model/GetObjectStorageKeys200Response';
import GetObjectStorageTransfer200Response from '../model/GetObjectStorageTransfer200Response';
import ObjectStorageBucket from '../model/ObjectStorageBucket';
import ObjectStorageCluster from '../model/ObjectStorageCluster';
import ObjectStorageKey from '../model/ObjectStorageKey';
import ObjectStorageSSL from '../model/ObjectStorageSSL';
import ObjectStorageSSLResponse from '../model/ObjectStorageSSLResponse';
import UpdateObjectStorageBucketACLRequest from '../model/UpdateObjectStorageBucketACLRequest';
import UpdateObjectStorageBucketAccessRequest from '../model/UpdateObjectStorageBucketAccessRequest';
import UpdateObjectStorageKeyRequest from '../model/UpdateObjectStorageKeyRequest';
import ViewObjectStorageBucketACL200Response from '../model/ViewObjectStorageBucketACL200Response';

/**
* ObjectStorage service.
* @module api/ObjectStorageApi
* @version 4.151.1
*/
export default class ObjectStorageApi {

    /**
    * Constructs a new ObjectStorageApi. 
    * @alias module:api/ObjectStorageApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the cancelObjectStorage operation.
     * @callback module:api/ObjectStorageApi~cancelObjectStorageCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Cancel
     * Cancel Object Storage on an Account.  **Warning**: Removes all buckets and their contents from your Account. This data is irretrievable once removed. 
     * @param {module:api/ObjectStorageApi~cancelObjectStorageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cancelObjectStorage(opts, callback) {
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
      let returnType = Object;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/cancel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the createObjectStorageBucket operation.
     * @callback module:api/ObjectStorageApi~createObjectStorageBucketCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageBucket} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Bucket Create
     * Creates an Object Storage Bucket in the specified cluster.  Accounts with negative balances cannot access this command.  If the bucket already exists and is owned by you, this endpoint returns a `200` response with that bucket as if it had just been created.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly. 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateObjectStorageBucketRequest} [createObjectStorageBucketRequest] Information about the bucket you want to create. 
     * @param {module:api/ObjectStorageApi~createObjectStorageBucketCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageBucket}
     */
    createObjectStorageBucket(opts, callback) {
      opts = opts || {};
      let postBody = opts['createObjectStorageBucketRequest'];

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
      let returnType = ObjectStorageBucket;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the createObjectStorageKeys operation.
     * @callback module:api/ObjectStorageApi~createObjectStorageKeysCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Key Create
     * Provisions a new Object Storage Key on your account.  Accounts with negative balances cannot access this command.  * To create a Limited Access Key with specific permissions, send a `bucket_access` array.  * To create a Limited Access Key without access to any buckets, send an empty `bucket_access` array.  * To create an Access Key with unlimited access to all clusters and all buckets, omit the `bucket_access` array. 
     * @param {Object} opts Optional parameters
     * @param {module:model/ObjectStorageKey} [objectStorageKey] The label of the key to create. This is used to identify the created key. 
     * @param {module:api/ObjectStorageApi~createObjectStorageKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageKey}
     */
    createObjectStorageKeys(opts, callback) {
      opts = opts || {};
      let postBody = opts['objectStorageKey'];

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
      let returnType = ObjectStorageKey;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/keys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the createObjectStorageObjectURL operation.
     * @callback module:api/ObjectStorageApi~createObjectStorageObjectURLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateObjectStorageObjectURL200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Object URL Create
     * Creates a pre-signed URL to access a single Object in a bucket. This can be used to share objects, and also to create/delete objects by using the appropriate HTTP method in your request body's `method` parameter.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateObjectStorageObjectURLRequest} [createObjectStorageObjectURLRequest] Information about the request to sign.
     * @param {module:api/ObjectStorageApi~createObjectStorageObjectURLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateObjectStorageObjectURL200Response}
     */
    createObjectStorageObjectURL(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = opts['createObjectStorageObjectURLRequest'];
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling createObjectStorageObjectURL");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling createObjectStorageObjectURL");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let returnType = CreateObjectStorageObjectURL200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/object-url', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the createObjectStorageSSL operation.
     * @callback module:api/ObjectStorageApi~createObjectStorageSSLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageSSLResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage TLS/SSL Cert Upload
     * Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.   To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete) and upload a new one. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {Object} opts Optional parameters
     * @param {module:model/ObjectStorageSSL} [objectStorageSSL] Upload this TLS/SSL certificate with its corresponding secret key.
     * @param {module:api/ObjectStorageApi~createObjectStorageSSLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageSSLResponse}
     */
    createObjectStorageSSL(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = opts['objectStorageSSL'];
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling createObjectStorageSSL");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling createObjectStorageSSL");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let returnType = ObjectStorageSSLResponse;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/ssl', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteObjectStorageBucket operation.
     * @callback module:api/ObjectStorageApi~deleteObjectStorageBucketCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Bucket Remove
     * Removes a single bucket.  Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations can fail if the bucket contains too many objects. The recommended way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that remove all objects, then delete the bucket.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {module:api/ObjectStorageApi~deleteObjectStorageBucketCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteObjectStorageBucket(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling deleteObjectStorageBucket");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling deleteObjectStorageBucket");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteObjectStorageKey operation.
     * @callback module:api/ObjectStorageApi~deleteObjectStorageKeyCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Key Revoke
     * Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients. 
     * @param {Number} keyId The key to look up.
     * @param {module:api/ObjectStorageApi~deleteObjectStorageKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteObjectStorageKey(keyId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'keyId' is set
      if (keyId === undefined || keyId === null) {
        throw new Error("Missing the required parameter 'keyId' when calling deleteObjectStorageKey");
      }

      let pathParams = {
        'keyId': keyId
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
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/keys/{keyId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteObjectStorageSSL operation.
     * @callback module:api/ObjectStorageApi~deleteObjectStorageSSLCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage TLS/SSL Cert Delete
     * Deletes this Object Storage bucket's user uploaded TLS/SSL certificate and private key. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {module:api/ObjectStorageApi~deleteObjectStorageSSLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteObjectStorageSSL(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling deleteObjectStorageSSL");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling deleteObjectStorageSSL");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/ssl', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageBucket operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageBucketCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageBucket} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Bucket View
     * Returns a single Object Storage Bucket.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {module:api/ObjectStorageApi~getObjectStorageBucketCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageBucket}
     */
    getObjectStorageBucket(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling getObjectStorageBucket");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling getObjectStorageBucket");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let returnType = ObjectStorageBucket;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageBucketContent operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageBucketContentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetObjectStorageBucketContent200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Bucket Contents List
     * Returns the contents of a bucket. The contents are paginated using a `marker`, which is the name of the last object on the previous page.  Objects may be filtered by `prefix` and `delimiter` as well; see Query Parameters for more information.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {Object} opts Optional parameters
     * @param {String} [marker] The \"marker\" for this request, which can be used to paginate through large buckets. Its value should be the value of the `next_marker` property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the `next_marker` property in the responses section for more details. 
     * @param {String} [delimiter] The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the `/` character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with `prefix` to see object names past the first occurrence of the delimiter. 
     * @param {String} [prefix] Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with `delimiter` to allow transversal of bucket contents in a manner similar to a filesystem. 
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/ObjectStorageApi~getObjectStorageBucketContentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetObjectStorageBucketContent200Response}
     */
    getObjectStorageBucketContent(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling getObjectStorageBucketContent");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling getObjectStorageBucketContent");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
      };
      let queryParams = {
        'marker': opts['marker'],
        'delimiter': opts['delimiter'],
        'prefix': opts['prefix'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetObjectStorageBucketContent200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/object-list', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageBucketinCluster operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageBucketinClusterCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetObjectStorageBuckets200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Buckets in Cluster List
     * Returns a list of Buckets in this cluster belonging to this Account.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {module:api/ObjectStorageApi~getObjectStorageBucketinClusterCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetObjectStorageBuckets200Response}
     */
    getObjectStorageBucketinCluster(clusterId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling getObjectStorageBucketinCluster");
      }

      let pathParams = {
        'clusterId': clusterId
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
      let returnType = GetObjectStorageBuckets200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageBuckets operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageBucketsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetObjectStorageBuckets200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Buckets List
     * Returns a paginated list of all Object Storage Buckets that you own.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly. 
     * @param {module:api/ObjectStorageApi~getObjectStorageBucketsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetObjectStorageBuckets200Response}
     */
    getObjectStorageBuckets(opts, callback) {
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
      let returnType = GetObjectStorageBuckets200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageCluster operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageClusterCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageCluster} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Cluster View
     * Returns a single Object Storage Cluster. 
     * @param {String} clusterId The ID of the Cluster.
     * @param {module:api/ObjectStorageApi~getObjectStorageClusterCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageCluster}
     */
    getObjectStorageCluster(clusterId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling getObjectStorageCluster");
      }

      let pathParams = {
        'clusterId': clusterId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ObjectStorageCluster;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/clusters/{clusterId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageClusters operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageClustersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetObjectStorageClusters200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Clusters List
     * Returns a paginated list of Object Storage Clusters that are available for use.  Users can connect to the clusters with third party clients to create buckets and upload objects. 
     * @param {module:api/ObjectStorageApi~getObjectStorageClustersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetObjectStorageClusters200Response}
     */
    getObjectStorageClusters(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetObjectStorageClusters200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/clusters', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageKey operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Key View
     * Returns a single Object Storage Key provisioned for your account. 
     * @param {Number} keyId The key to look up.
     * @param {module:api/ObjectStorageApi~getObjectStorageKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageKey}
     */
    getObjectStorageKey(keyId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'keyId' is set
      if (keyId === undefined || keyId === null) {
        throw new Error("Missing the required parameter 'keyId' when calling getObjectStorageKey");
      }

      let pathParams = {
        'keyId': keyId
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
      let returnType = ObjectStorageKey;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/keys/{keyId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageKeys operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageKeysCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetObjectStorageKeys200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Keys List
     * Returns a paginated list of Object Storage Keys for authenticating to the Object Storage S3 API. 
     * @param {module:api/ObjectStorageApi~getObjectStorageKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetObjectStorageKeys200Response}
     */
    getObjectStorageKeys(opts, callback) {
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
      let returnType = GetObjectStorageKeys200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/keys', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageSSL operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageSSLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageSSLResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage TLS/SSL Cert View
     * Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {module:api/ObjectStorageApi~getObjectStorageSSLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageSSLResponse}
     */
    getObjectStorageSSL(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling getObjectStorageSSL");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling getObjectStorageSSL");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let returnType = ObjectStorageSSLResponse;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/ssl', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getObjectStorageTransfer operation.
     * @callback module:api/ObjectStorageApi~getObjectStorageTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetObjectStorageTransfer200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Transfer View
     * The amount of outbound data transfer used by your account's Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas. 
     * @param {module:api/ObjectStorageApi~getObjectStorageTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetObjectStorageTransfer200Response}
     */
    getObjectStorageTransfer(opts, callback) {
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
      let returnType = GetObjectStorageTransfer200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/transfer', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the modifyObjectStorageBucketAccess operation.
     * @callback module:api/ObjectStorageApi~modifyObjectStorageBucketAccessCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Bucket Access Modify
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateObjectStorageBucketAccessRequest} [updateObjectStorageBucketAccessRequest] The changes to make to the bucket's access controls.
     * @param {module:api/ObjectStorageApi~modifyObjectStorageBucketAccessCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    modifyObjectStorageBucketAccess(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateObjectStorageBucketAccessRequest'];
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling modifyObjectStorageBucketAccess");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling modifyObjectStorageBucketAccess");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/access', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the updateObjectStorageBucketACL operation.
     * @callback module:api/ObjectStorageApi~updateObjectStorageBucketACLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ViewObjectStorageBucketACL200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Object ACL Config Update
     * Update an Object's configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateObjectStorageBucketACLRequest} [updateObjectStorageBucketACLRequest] The changes to make to this Object's access controls.
     * @param {module:api/ObjectStorageApi~updateObjectStorageBucketACLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ViewObjectStorageBucketACL200Response}
     */
    updateObjectStorageBucketACL(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateObjectStorageBucketACLRequest'];
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling updateObjectStorageBucketACL");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling updateObjectStorageBucketACL");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let returnType = ViewObjectStorageBucketACL200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/object-acl', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the updateObjectStorageBucketAccess operation.
     * @callback module:api/ObjectStorageApi~updateObjectStorageBucketAccessCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Bucket Access Update
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateObjectStorageBucketAccessRequest} [updateObjectStorageBucketAccessRequest] The changes to make to the bucket's access controls.
     * @param {module:api/ObjectStorageApi~updateObjectStorageBucketAccessCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateObjectStorageBucketAccess(clusterId, bucket, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateObjectStorageBucketAccessRequest'];
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling updateObjectStorageBucketAccess");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling updateObjectStorageBucketAccess");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
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
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/access', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the updateObjectStorageKey operation.
     * @callback module:api/ObjectStorageApi~updateObjectStorageKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ObjectStorageKey} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Key Update
     * Updates an Object Storage Key on your account. 
     * @param {Number} keyId The key to look up.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateObjectStorageKeyRequest} [updateObjectStorageKeyRequest] The fields to update.
     * @param {module:api/ObjectStorageApi~updateObjectStorageKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ObjectStorageKey}
     */
    updateObjectStorageKey(keyId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateObjectStorageKeyRequest'];
      // verify the required parameter 'keyId' is set
      if (keyId === undefined || keyId === null) {
        throw new Error("Missing the required parameter 'keyId' when calling updateObjectStorageKey");
      }

      let pathParams = {
        'keyId': keyId
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
      let returnType = ObjectStorageKey;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/keys/{keyId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the viewObjectStorageBucketACL operation.
     * @callback module:api/ObjectStorageApi~viewObjectStorageBucketACLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ViewObjectStorageBucketACL200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Object Storage Object ACL Config View
     * View an Object's configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly. 
     * @param {String} clusterId The ID of the cluster this bucket exists in.
     * @param {String} bucket The bucket name.
     * @param {String} name The `name` of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket. 
     * @param {module:api/ObjectStorageApi~viewObjectStorageBucketACLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ViewObjectStorageBucketACL200Response}
     */
    viewObjectStorageBucketACL(clusterId, bucket, name, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterId' is set
      if (clusterId === undefined || clusterId === null) {
        throw new Error("Missing the required parameter 'clusterId' when calling viewObjectStorageBucketACL");
      }
      // verify the required parameter 'bucket' is set
      if (bucket === undefined || bucket === null) {
        throw new Error("Missing the required parameter 'bucket' when calling viewObjectStorageBucketACL");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling viewObjectStorageBucketACL");
      }

      let pathParams = {
        'clusterId': clusterId,
        'bucket': bucket
      };
      let queryParams = {
        'name': name
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ViewObjectStorageBucketACL200Response;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/object-storage/buckets/{clusterId}/{bucket}/object-acl', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }


}
