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
import DatabaseBackup from '../model/DatabaseBackup';
import DatabaseBackupSnapshot from '../model/DatabaseBackupSnapshot';
import DatabaseCredentials from '../model/DatabaseCredentials';
import DatabaseEngine from '../model/DatabaseEngine';
import DatabaseMongoDB from '../model/DatabaseMongoDB';
import DatabaseMySQL from '../model/DatabaseMySQL';
import DatabaseMySQLRequest from '../model/DatabaseMySQLRequest';
import DatabasePostgreSQL from '../model/DatabasePostgreSQL';
import DatabasePostgreSQLRequest from '../model/DatabasePostgreSQLRequest';
import DatabaseSSL from '../model/DatabaseSSL';
import DatabaseType from '../model/DatabaseType';
import GetAccountDefaultResponse from '../model/GetAccountDefaultResponse';
import GetDatabasesEngines200Response from '../model/GetDatabasesEngines200Response';
import GetDatabasesInstances200Response from '../model/GetDatabasesInstances200Response';
import GetDatabasesMongoDBInstanceBackups200Response from '../model/GetDatabasesMongoDBInstanceBackups200Response';
import GetDatabasesMongoDBInstances200Response from '../model/GetDatabasesMongoDBInstances200Response';
import GetDatabasesMySQLInstances200Response from '../model/GetDatabasesMySQLInstances200Response';
import GetDatabasesPostgreSQLInstances200Response from '../model/GetDatabasesPostgreSQLInstances200Response';
import GetDatabasesTypes200Response from '../model/GetDatabasesTypes200Response';
import PutDatabasesMongoDBInstanceRequest from '../model/PutDatabasesMongoDBInstanceRequest';
import PutDatabasesMySQLInstanceRequest from '../model/PutDatabasesMySQLInstanceRequest';
import PutDatabasesPostgreSQLInstanceRequest from '../model/PutDatabasesPostgreSQLInstanceRequest';

/**
* Databases service.
* @module api/DatabasesApi
* @version 4.151.1
*/
export default class DatabasesApi {

    /**
    * Constructs a new DatabasesApi. 
    * @alias module:api/DatabasesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteDatabaseMongoDBInstanceBackup operation.
     * @callback module:api/DatabasesApi~deleteDatabaseMongoDBInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Backup Delete
     * Delete a single backup for an accessible Managed MongoDB Database.  Requires `read_write` access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {Number} backupId The ID of the Managed MongoDB Database backup.
     * @param {module:api/DatabasesApi~deleteDatabaseMongoDBInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDatabaseMongoDBInstanceBackup(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling deleteDatabaseMongoDBInstanceBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling deleteDatabaseMongoDBInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/backups/{backupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDatabaseMySQLInstanceBackup operation.
     * @callback module:api/DatabasesApi~deleteDatabaseMySQLInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Backup Delete
     * Delete a single backup for an accessible Managed MySQL Database.  Requires `read_write` access to the Database.  The Database must not be provisioning to perform this command. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {Number} backupId The ID of the Managed MySQL Database backup.
     * @param {module:api/DatabasesApi~deleteDatabaseMySQLInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDatabaseMySQLInstanceBackup(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling deleteDatabaseMySQLInstanceBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling deleteDatabaseMySQLInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/backups/{backupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDatabasePostgreSQLInstanceBackup operation.
     * @callback module:api/DatabasesApi~deleteDatabasePostgreSQLInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Backup Delete
     * Delete a single backup for an accessible Managed PostgreSQL Database.  Requires `read_write` access to the Database.  The Database must not be provisioning to perform this command. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {Number} backupId The ID of the Managed PostgreSQL Database backup.
     * @param {module:api/DatabasesApi~deleteDatabasePostgreSQLInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDatabasePostgreSQLInstanceBackup(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling deleteDatabasePostgreSQLInstanceBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling deleteDatabasePostgreSQLInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/backups/{backupId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDatabasesMongoDBInstance operation.
     * @callback module:api/DatabasesApi~deleteDatabasesMongoDBInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Delete
     * Remove a Managed MongoDB Database from your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `failed`, or `degraded` status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~deleteDatabasesMongoDBInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDatabasesMongoDBInstance(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling deleteDatabasesMongoDBInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDatabasesMySQLInstance operation.
     * @callback module:api/DatabasesApi~deleteDatabasesMySQLInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Delete
     * Remove a Managed MySQL Database from your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `failed`, or `degraded` status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:api/DatabasesApi~deleteDatabasesMySQLInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDatabasesMySQLInstance(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling deleteDatabasesMySQLInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDatabasesPostgreSQLInstance operation.
     * @callback module:api/DatabasesApi~deleteDatabasesPostgreSQLInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Delete
     * Remove a Managed PostgreSQL Database from your Account.  Requires `read_write` access to the Database.  The Database must have an `active`, `failed`, or `degraded` status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~deleteDatabasesPostgreSQLInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDatabasesPostgreSQLInstance(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling deleteDatabasesPostgreSQLInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesEngine operation.
     * @callback module:api/DatabasesApi~getDatabasesEngineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseEngine} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Database Engine View
     * Display information for a single Managed Database engine type and version. 
     * @param {String} engineId The ID of the Managed Database engine.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesEngineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseEngine}
     */
    getDatabasesEngine(engineId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'engineId' is set
      if (engineId === undefined || engineId === null) {
        throw new Error("Missing the required parameter 'engineId' when calling getDatabasesEngine");
      }

      let pathParams = {
        'engineId': engineId
      };
      let queryParams = {
        'page': opts['page'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DatabaseEngine;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/engines/{engineId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesEngines operation.
     * @callback module:api/DatabasesApi~getDatabasesEnginesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesEngines200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Database Engines List
     * Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesEnginesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesEngines200Response}
     */
    getDatabasesEngines(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDatabasesEngines200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/engines', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesInstances operation.
     * @callback module:api/DatabasesApi~getDatabasesInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesInstances200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Databases List All
     * Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its `instance_uri`. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesInstances200Response}
     */
    getDatabasesInstances(opts, callback) {
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
      let returnType = GetDatabasesInstances200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/instances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMongoDBInstance operation.
     * @callback module:api/DatabasesApi~getDatabasesMongoDBInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseMongoDB} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database View
     * Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~getDatabasesMongoDBInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseMongoDB}
     */
    getDatabasesMongoDBInstance(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseMongoDB;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMongoDBInstanceBackup operation.
     * @callback module:api/DatabasesApi~getDatabasesMongoDBInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseBackup} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Backup View
     * Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {Number} backupId The ID of the Managed MongoDB Database backup.
     * @param {module:api/DatabasesApi~getDatabasesMongoDBInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseBackup}
     */
    getDatabasesMongoDBInstanceBackup(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling getDatabasesMongoDBInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let returnType = DatabaseBackup;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/backups/{backupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMongoDBInstanceBackups operation.
     * @callback module:api/DatabasesApi~getDatabasesMongoDBInstanceBackupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesMongoDBInstanceBackups200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Backups List
     * Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database `auto` type backups are created every 24 hours at 0:00 UTC. Each `auto` backup is retained for 7 days.  Database `snapshot` type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesMongoDBInstanceBackupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesMongoDBInstanceBackups200Response}
     */
    getDatabasesMongoDBInstanceBackups(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceBackups");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = GetDatabasesMongoDBInstanceBackups200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/backups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMongoDBInstanceCredentials operation.
     * @callback module:api/DatabasesApi~getDatabasesMongoDBInstanceCredentialsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseCredentials} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Credentials View
     * Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an `active` status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~getDatabasesMongoDBInstanceCredentialsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseCredentials}
     */
    getDatabasesMongoDBInstanceCredentials(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceCredentials");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseCredentials;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/credentials', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMongoDBInstanceSSL operation.
     * @callback module:api/DatabasesApi~getDatabasesMongoDBInstanceSSLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseSSL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an `active` status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~getDatabasesMongoDBInstanceSSLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseSSL}
     */
    getDatabasesMongoDBInstanceSSL(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceSSL");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseSSL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/ssl', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMongoDBInstances operation.
     * @callback module:api/DatabasesApi~getDatabasesMongoDBInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesMongoDBInstances200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Databases List
     * Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesMongoDBInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesMongoDBInstances200Response}
     */
    getDatabasesMongoDBInstances(opts, callback) {
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
      let returnType = GetDatabasesMongoDBInstances200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMySQLInstance operation.
     * @callback module:api/DatabasesApi~getDatabasesMySQLInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseMySQL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database View
     * Display information for a single, accessible Managed MySQL Database. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:api/DatabasesApi~getDatabasesMySQLInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseMySQL}
     */
    getDatabasesMySQLInstance(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseMySQL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMySQLInstanceBackup operation.
     * @callback module:api/DatabasesApi~getDatabasesMySQLInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseBackup} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Backup View
     * Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {Number} backupId The ID of the Managed MySQL Database backup.
     * @param {module:api/DatabasesApi~getDatabasesMySQLInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseBackup}
     */
    getDatabasesMySQLInstanceBackup(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling getDatabasesMySQLInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let returnType = DatabaseBackup;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/backups/{backupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMySQLInstanceBackups operation.
     * @callback module:api/DatabasesApi~getDatabasesMySQLInstanceBackupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesMongoDBInstanceBackups200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Backups List
     * Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database `auto` type backups are created every 24 hours at 0:00 UTC. Each `auto` backup is retained for 7 days.  Database `snapshot` type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesMySQLInstanceBackupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesMongoDBInstanceBackups200Response}
     */
    getDatabasesMySQLInstanceBackups(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceBackups");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = GetDatabasesMongoDBInstanceBackups200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/backups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMySQLInstanceCredentials operation.
     * @callback module:api/DatabasesApi~getDatabasesMySQLInstanceCredentialsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseCredentials} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Credentials View
     * Display the root username and password for an accessible Managed MySQL Database.  The Database must have an `active` status to perform this command. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:api/DatabasesApi~getDatabasesMySQLInstanceCredentialsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseCredentials}
     */
    getDatabasesMySQLInstanceCredentials(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceCredentials");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseCredentials;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/credentials', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMySQLInstanceSSL operation.
     * @callback module:api/DatabasesApi~getDatabasesMySQLInstanceSSLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseSSL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an `active` status to perform this command. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:api/DatabasesApi~getDatabasesMySQLInstanceSSLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseSSL}
     */
    getDatabasesMySQLInstanceSSL(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceSSL");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseSSL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/ssl', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesMySQLInstances operation.
     * @callback module:api/DatabasesApi~getDatabasesMySQLInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesMySQLInstances200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Databases List
     * Display all accessible Managed MySQL Databases. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesMySQLInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesMySQLInstances200Response}
     */
    getDatabasesMySQLInstances(opts, callback) {
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
      let returnType = GetDatabasesMySQLInstances200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesPostgreSQLInstance operation.
     * @callback module:api/DatabasesApi~getDatabasesPostgreSQLInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabasePostgreSQL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database View
     * Display information for a single, accessible Managed PostgreSQL Database. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~getDatabasesPostgreSQLInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabasePostgreSQL}
     */
    getDatabasesPostgreSQLInstance(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabasePostgreSQL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesPostgreSQLInstanceBackup operation.
     * @callback module:api/DatabasesApi~getDatabasesPostgreSQLInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseBackup} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Backup View
     * Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {Number} backupId The ID of the Managed PostgreSQL Database backup.
     * @param {module:api/DatabasesApi~getDatabasesPostgreSQLInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseBackup}
     */
    getDatabasesPostgreSQLInstanceBackup(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling getDatabasesPostgreSQLInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let returnType = DatabaseBackup;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/backups/{backupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesPostgreSQLInstanceBackups operation.
     * @callback module:api/DatabasesApi~getDatabasesPostgreSQLInstanceBackupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesMongoDBInstanceBackups200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Backups List
     * Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database `auto` type backups are created every 24 hours at 0:00 UTC. Each `auto` backup is retained for 7 days.  Database `snapshot` type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesPostgreSQLInstanceBackupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesMongoDBInstanceBackups200Response}
     */
    getDatabasesPostgreSQLInstanceBackups(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceBackups");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = GetDatabasesMongoDBInstanceBackups200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/backups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesPostgreSQLInstanceCredentials operation.
     * @callback module:api/DatabasesApi~getDatabasesPostgreSQLInstanceCredentialsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseCredentials} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Credentials View
     * Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an `active` status to perform this command. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~getDatabasesPostgreSQLInstanceCredentialsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseCredentials}
     */
    getDatabasesPostgreSQLInstanceCredentials(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceCredentials");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseCredentials;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/credentials', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesPostgreSQLInstanceSSL operation.
     * @callback module:api/DatabasesApi~getDatabasesPostgreSQLInstanceSSLCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseSSL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an `active` status to perform this command. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~getDatabasesPostgreSQLInstanceSSLCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseSSL}
     */
    getDatabasesPostgreSQLInstanceSSL(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceSSL");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseSSL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/ssl', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesPostgreSQLInstances operation.
     * @callback module:api/DatabasesApi~getDatabasesPostgreSQLInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesPostgreSQLInstances200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Databases List
     * Display all accessible Managed PostgreSQL Databases. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesPostgreSQLInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesPostgreSQLInstances200Response}
     */
    getDatabasesPostgreSQLInstances(opts, callback) {
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
      let returnType = GetDatabasesPostgreSQLInstances200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesType operation.
     * @callback module:api/DatabasesApi~getDatabasesTypeCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Database Type View
     * Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 
     * @param {String} typeId The ID of the Managed Database type.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesTypeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseType}
     */
    getDatabasesType(typeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'typeId' is set
      if (typeId === undefined || typeId === null) {
        throw new Error("Missing the required parameter 'typeId' when calling getDatabasesType");
      }

      let pathParams = {
        'typeId': typeId
      };
      let queryParams = {
        'page': opts['page'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DatabaseType;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/types/{typeId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatabasesTypes operation.
     * @callback module:api/DatabasesApi~getDatabasesTypesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatabasesTypes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed Database Types List
     * Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/DatabasesApi~getDatabasesTypesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatabasesTypes200Response}
     */
    getDatabasesTypes(opts, callback) {
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

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDatabasesTypes200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMongoDBInstanceBackup operation.
     * @callback module:api/DatabasesApi~postDatabasesMongoDBInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed MongoDB Database.  Requires `read_write` access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type `snapshot`. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an `active` status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {Object} opts Optional parameters
     * @param {module:model/DatabaseBackupSnapshot} [databaseBackupSnapshot] Information about the snapshot backup to create.
     * @param {module:api/DatabasesApi~postDatabasesMongoDBInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMongoDBInstanceBackup(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = opts['databaseBackupSnapshot'];
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/backups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMongoDBInstanceBackupRestore operation.
     * @callback module:api/DatabasesApi~postDatabasesMongoDBInstanceBackupRestoreCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Backup Restore
     * Restore a backup to a Managed MongoDB Database on your Account.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {Number} backupId The ID of the Managed MongoDB Database backup.
     * @param {module:api/DatabasesApi~postDatabasesMongoDBInstanceBackupRestoreCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMongoDBInstanceBackupRestore(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstanceBackupRestore");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling postDatabasesMongoDBInstanceBackupRestore");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/backups/{backupId}/restore', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMongoDBInstanceCredentialsReset operation.
     * @callback module:api/DatabasesApi~postDatabasesMongoDBInstanceCredentialsResetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Credentials Reset
     * Reset the root password for a Managed MongoDB Database.  Requires `read_write` access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~postDatabasesMongoDBInstanceCredentialsResetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMongoDBInstanceCredentialsReset(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstanceCredentialsReset");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/credentials/reset', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMongoDBInstancePatch operation.
     * @callback module:api/DatabasesApi~postDatabasesMongoDBInstancePatchCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~postDatabasesMongoDBInstancePatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMongoDBInstancePatch(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstancePatch");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}/patch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMySQLInstanceBackup operation.
     * @callback module:api/DatabasesApi~postDatabasesMySQLInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed MySQL Database.  Requires `read_write` access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type `snapshot`. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an `active` status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {Object} opts Optional parameters
     * @param {module:model/DatabaseBackupSnapshot} [databaseBackupSnapshot] Information about the snapshot backup to create.
     * @param {module:api/DatabasesApi~postDatabasesMySQLInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMySQLInstanceBackup(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = opts['databaseBackupSnapshot'];
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/backups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMySQLInstanceBackupRestore operation.
     * @callback module:api/DatabasesApi~postDatabasesMySQLInstanceBackupRestoreCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Backup Restore
     * Restore a backup to a Managed MySQL Database on your Account.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {Number} backupId The ID of the Managed MySQL Database backup.
     * @param {module:api/DatabasesApi~postDatabasesMySQLInstanceBackupRestoreCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMySQLInstanceBackupRestore(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstanceBackupRestore");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling postDatabasesMySQLInstanceBackupRestore");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/backups/{backupId}/restore', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMySQLInstanceCredentialsReset operation.
     * @callback module:api/DatabasesApi~postDatabasesMySQLInstanceCredentialsResetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Credentials Reset
     * Reset the root password for a Managed MySQL Database.  Requires `read_write` access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:api/DatabasesApi~postDatabasesMySQLInstanceCredentialsResetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMySQLInstanceCredentialsReset(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstanceCredentialsReset");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/credentials/reset', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMySQLInstancePatch operation.
     * @callback module:api/DatabasesApi~postDatabasesMySQLInstancePatchCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:api/DatabasesApi~postDatabasesMySQLInstancePatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesMySQLInstancePatch(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstancePatch");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}/patch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesMySQLInstances operation.
     * @callback module:api/DatabasesApi~postDatabasesMySQLInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseMySQL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Create
     * Provision a Managed MySQL Database.  Restricted Users must have the `add_databases` grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The `allow_list` is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 
     * @param {module:model/DatabaseMySQLRequest} databaseMySQLRequest Information about the Managed MySQL Database you are creating.
     * @param {module:api/DatabasesApi~postDatabasesMySQLInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseMySQL}
     */
    postDatabasesMySQLInstances(databaseMySQLRequest, opts, callback) {
      opts = opts || {};
      let postBody = databaseMySQLRequest;
      // verify the required parameter 'databaseMySQLRequest' is set
      if (databaseMySQLRequest === undefined || databaseMySQLRequest === null) {
        throw new Error("Missing the required parameter 'databaseMySQLRequest' when calling postDatabasesMySQLInstances");
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
      let returnType = DatabaseMySQL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesPostgreSQLInstanceBackup operation.
     * @callback module:api/DatabasesApi~postDatabasesPostgreSQLInstanceBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed PostgreSQL Database.  Requires `read_write` access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type `snapshot`. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an `active` status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {Object} opts Optional parameters
     * @param {module:model/DatabaseBackupSnapshot} [databaseBackupSnapshot] Information about the snapshot backup to create.
     * @param {module:api/DatabasesApi~postDatabasesPostgreSQLInstanceBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesPostgreSQLInstanceBackup(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = opts['databaseBackupSnapshot'];
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstanceBackup");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/backups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesPostgreSQLInstanceBackupRestore operation.
     * @callback module:api/DatabasesApi~postDatabasesPostgreSQLInstanceBackupRestoreCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Backup Restore
     * Restore a backup to a Managed PostgreSQL Database on your Account.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {Number} backupId The ID of the Managed PostgreSQL Database backup.
     * @param {module:api/DatabasesApi~postDatabasesPostgreSQLInstanceBackupRestoreCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesPostgreSQLInstanceBackupRestore(instanceId, backupId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstanceBackupRestore");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling postDatabasesPostgreSQLInstanceBackupRestore");
      }

      let pathParams = {
        'instanceId': instanceId,
        'backupId': backupId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/backups/{backupId}/restore', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesPostgreSQLInstanceCredentialsReset operation.
     * @callback module:api/DatabasesApi~postDatabasesPostgreSQLInstanceCredentialsResetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Credentials Reset
     * Reset the root password for a Managed PostgreSQL Database.  Requires `read_write` access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~postDatabasesPostgreSQLInstanceCredentialsResetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesPostgreSQLInstanceCredentialsReset(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstanceCredentialsReset");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/credentials/reset', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesPostgreSQLInstancePatch operation.
     * @callback module:api/DatabasesApi~postDatabasesPostgreSQLInstancePatchCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~postDatabasesPostgreSQLInstancePatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    postDatabasesPostgreSQLInstancePatch(instanceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstancePatch");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}/patch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the postDatabasesPostgreSQLInstances operation.
     * @callback module:api/DatabasesApi~postDatabasesPostgreSQLInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabasePostgreSQL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Create
     * Provision a Managed PostgreSQL Database.  Restricted Users must have the `add_databases` grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The `allow_list` is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 
     * @param {module:model/DatabasePostgreSQLRequest} databasePostgreSQLRequest Information about the Managed PostgreSQL Database you are creating.
     * @param {module:api/DatabasesApi~postDatabasesPostgreSQLInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabasePostgreSQL}
     */
    postDatabasesPostgreSQLInstances(databasePostgreSQLRequest, opts, callback) {
      opts = opts || {};
      let postBody = databasePostgreSQLRequest;
      // verify the required parameter 'databasePostgreSQLRequest' is set
      if (databasePostgreSQLRequest === undefined || databasePostgreSQLRequest === null) {
        throw new Error("Missing the required parameter 'databasePostgreSQLRequest' when calling postDatabasesPostgreSQLInstances");
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
      let returnType = DatabasePostgreSQL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the putDatabasesMongoDBInstance operation.
     * @callback module:api/DatabasesApi~putDatabasesMongoDBInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseMongoDB} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MongoDB Database Update
     * Update a Managed MongoDB Database.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  Updating addresses in the `allow_list` overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the `allow_list` may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param {Number} instanceId The ID of the Managed MongoDB Database.
     * @param {module:model/PutDatabasesMongoDBInstanceRequest} putDatabasesMongoDBInstanceRequest Updated information for the Managed MongoDB Database.
     * @param {module:api/DatabasesApi~putDatabasesMongoDBInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseMongoDB}
     */
    putDatabasesMongoDBInstance(instanceId, putDatabasesMongoDBInstanceRequest, opts, callback) {
      opts = opts || {};
      let postBody = putDatabasesMongoDBInstanceRequest;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling putDatabasesMongoDBInstance");
      }
      // verify the required parameter 'putDatabasesMongoDBInstanceRequest' is set
      if (putDatabasesMongoDBInstanceRequest === undefined || putDatabasesMongoDBInstanceRequest === null) {
        throw new Error("Missing the required parameter 'putDatabasesMongoDBInstanceRequest' when calling putDatabasesMongoDBInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseMongoDB;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mongodb/instances/{instanceId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the putDatabasesMySQLInstance operation.
     * @callback module:api/DatabasesApi~putDatabasesMySQLInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabaseMySQL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed MySQL Database Update
     * Update a Managed MySQL Database.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  Updating addresses in the `allow_list` overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the `allow_list` may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param {Number} instanceId The ID of the Managed MySQL Database.
     * @param {module:model/PutDatabasesMySQLInstanceRequest} putDatabasesMySQLInstanceRequest Updated information for the Managed MySQL Database.
     * @param {module:api/DatabasesApi~putDatabasesMySQLInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabaseMySQL}
     */
    putDatabasesMySQLInstance(instanceId, putDatabasesMySQLInstanceRequest, opts, callback) {
      opts = opts || {};
      let postBody = putDatabasesMySQLInstanceRequest;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling putDatabasesMySQLInstance");
      }
      // verify the required parameter 'putDatabasesMySQLInstanceRequest' is set
      if (putDatabasesMySQLInstanceRequest === undefined || putDatabasesMySQLInstanceRequest === null) {
        throw new Error("Missing the required parameter 'putDatabasesMySQLInstanceRequest' when calling putDatabasesMySQLInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabaseMySQL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/mysql/instances/{instanceId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the putDatabasesPostgreSQLInstance operation.
     * @callback module:api/DatabasesApi~putDatabasesPostgreSQLInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatabasePostgreSQL} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Managed PostgreSQL Database Update
     * Update a Managed PostgreSQL Database.  Requires `read_write` access to the Database.  The Database must have an `active` status to perform this command.  Updating addresses in the `allow_list` overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If `0.0.0.0/0` is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (`[]`) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the `allow_list` may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database's `updates` property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It's recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param {Number} instanceId The ID of the Managed PostgreSQL Database.
     * @param {module:model/PutDatabasesPostgreSQLInstanceRequest} putDatabasesPostgreSQLInstanceRequest Updated information for the Managed PostgreSQL Database.
     * @param {module:api/DatabasesApi~putDatabasesPostgreSQLInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatabasePostgreSQL}
     */
    putDatabasesPostgreSQLInstance(instanceId, putDatabasesPostgreSQLInstanceRequest, opts, callback) {
      opts = opts || {};
      let postBody = putDatabasesPostgreSQLInstanceRequest;
      // verify the required parameter 'instanceId' is set
      if (instanceId === undefined || instanceId === null) {
        throw new Error("Missing the required parameter 'instanceId' when calling putDatabasesPostgreSQLInstance");
      }
      // verify the required parameter 'putDatabasesPostgreSQLInstanceRequest' is set
      if (putDatabasesPostgreSQLInstanceRequest === undefined || putDatabasesPostgreSQLInstanceRequest === null) {
        throw new Error("Missing the required parameter 'putDatabasesPostgreSQLInstanceRequest' when calling putDatabasesPostgreSQLInstance");
      }

      let pathParams = {
        'instanceId': instanceId
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
      let returnType = DatabasePostgreSQL;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/databases/postgresql/instances/{instanceId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }


}
