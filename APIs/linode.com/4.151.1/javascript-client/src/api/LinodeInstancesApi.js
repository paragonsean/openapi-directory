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
import AddLinodeIPRequest from '../model/AddLinodeIPRequest';
import Backup from '../model/Backup';
import BootLinodeInstanceRequest from '../model/BootLinodeInstanceRequest';
import CloneLinodeInstanceRequest from '../model/CloneLinodeInstanceRequest';
import CreateLinodeInstanceRequest from '../model/CreateLinodeInstanceRequest';
import CreateSnapshotRequest from '../model/CreateSnapshotRequest';
import Disk from '../model/Disk';
import DiskRequest from '../model/DiskRequest';
import GetAccountDefaultResponse from '../model/GetAccountDefaultResponse';
import GetBackups200Response from '../model/GetBackups200Response';
import GetKernels200Response from '../model/GetKernels200Response';
import GetLinodeConfigs200Response from '../model/GetLinodeConfigs200Response';
import GetLinodeDisks200Response from '../model/GetLinodeDisks200Response';
import GetLinodeFirewalls200Response from '../model/GetLinodeFirewalls200Response';
import GetLinodeIPs200Response from '../model/GetLinodeIPs200Response';
import GetLinodeInstances200Response from '../model/GetLinodeInstances200Response';
import GetLinodeNodeBalancers200Response from '../model/GetLinodeNodeBalancers200Response';
import GetLinodeTransfer200Response from '../model/GetLinodeTransfer200Response';
import GetLinodeTransferByYearMonth200Response from '../model/GetLinodeTransferByYearMonth200Response';
import GetLinodeVolumes200Response from '../model/GetLinodeVolumes200Response';
import IPAddress from '../model/IPAddress';
import Kernel from '../model/Kernel';
import Linode from '../model/Linode';
import LinodeConfig from '../model/LinodeConfig';
import LinodeRequest from '../model/LinodeRequest';
import LinodeStats from '../model/LinodeStats';
import MigrateLinodeInstanceRequest from '../model/MigrateLinodeInstanceRequest';
import MutateLinodeInstanceRequest from '../model/MutateLinodeInstanceRequest';
import RebootLinodeInstanceRequest from '../model/RebootLinodeInstanceRequest';
import RescueLinodeInstanceRequest from '../model/RescueLinodeInstanceRequest';
import ResetDiskPasswordRequest from '../model/ResetDiskPasswordRequest';
import ResetLinodePasswordRequest from '../model/ResetLinodePasswordRequest';
import ResizeDiskRequest from '../model/ResizeDiskRequest';
import ResizeLinodeInstanceRequest from '../model/ResizeLinodeInstanceRequest';
import RestoreBackupRequest from '../model/RestoreBackupRequest';
import UNKNOWN_BASE_TYPE from '../model/UNKNOWN_BASE_TYPE';
import UpdateLinodeIPRequest from '../model/UpdateLinodeIPRequest';

/**
* LinodeInstances service.
* @module api/LinodeInstancesApi
* @version 4.151.1
*/
export default class LinodeInstancesApi {

    /**
    * Constructs a new LinodeInstancesApi. 
    * @alias module:api/LinodeInstancesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addLinodeConfig operation.
     * @callback module:api/LinodeInstancesApi~addLinodeConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LinodeConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configuration Profile Create
     * Adds a new Configuration profile to a Linode. 
     * @param {Number} linodeId ID of the Linode to look up Configuration profiles for.
     * @param {module:model/LinodeConfig} linodeConfig The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with. 
     * @param {module:api/LinodeInstancesApi~addLinodeConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LinodeConfig}
     */
    addLinodeConfig(linodeId, linodeConfig, callback) {
      let postBody = linodeConfig;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling addLinodeConfig");
      }
      // verify the required parameter 'linodeConfig' is set
      if (linodeConfig === undefined || linodeConfig === null) {
        throw new Error("Missing the required parameter 'linodeConfig' when calling addLinodeConfig");
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
      let returnType = LinodeConfig;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/configs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addLinodeDisk operation.
     * @callback module:api/LinodeInstancesApi~addLinodeDiskCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Disk} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk Create
     * Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a `label` is required.  * If no `label` is provided, an `image` is required instead.  * When creating a Disk from an Image, `root_pass` is required.  * The default filesystem for new Disks is `ext4`. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the `authorized_keys` field.   * You may also supply a list of usernames via the `authorized_users` field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {module:model/DiskRequest} diskRequest The parameters to set when creating the Disk. 
     * @param {module:api/LinodeInstancesApi~addLinodeDiskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Disk}
     */
    addLinodeDisk(linodeId, diskRequest, callback) {
      let postBody = diskRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling addLinodeDisk");
      }
      // verify the required parameter 'diskRequest' is set
      if (diskRequest === undefined || diskRequest === null) {
        throw new Error("Missing the required parameter 'diskRequest' when calling addLinodeDisk");
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
      let returnType = Disk;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/disks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addLinodeIP operation.
     * @callback module:api/LinodeInstancesApi~addLinodeIPCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IPAddress} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * IPv4 Address Allocate
     * Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {module:model/AddLinodeIPRequest} addLinodeIPRequest Information about the address you are creating.
     * @param {module:api/LinodeInstancesApi~addLinodeIPCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IPAddress}
     */
    addLinodeIP(linodeId, addLinodeIPRequest, callback) {
      let postBody = addLinodeIPRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling addLinodeIP");
      }
      // verify the required parameter 'addLinodeIPRequest' is set
      if (addLinodeIPRequest === undefined || addLinodeIPRequest === null) {
        throw new Error("Missing the required parameter 'addLinodeIPRequest' when calling addLinodeIP");
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
      let returnType = IPAddress;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/ips', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the bootLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~bootLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Boot
     * Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 
     * @param {Number} linodeId The ID of the Linode to boot.
     * @param {Object} opts Optional parameters
     * @param {module:model/BootLinodeInstanceRequest} [bootLinodeInstanceRequest] Optional configuration to boot into (see above).
     * @param {module:api/LinodeInstancesApi~bootLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    bootLinodeInstance(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['bootLinodeInstanceRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling bootLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/boot', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cancelBackups operation.
     * @callback module:api/LinodeInstancesApi~cancelBackupsCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Backups Cancel
     * Cancels the Backup service on the given Linode. Deletes all of this Linode's existing backups forever. 
     * @param {Number} linodeId The ID of the Linode to cancel backup service for.
     * @param {module:api/LinodeInstancesApi~cancelBackupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cancelBackups(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling cancelBackups");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/backups/cancel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cloneLinodeDisk operation.
     * @callback module:api/LinodeInstancesApi~cloneLinodeDiskCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Disk} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk Clone
     * Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} diskId ID of the Disk to clone.
     * @param {module:api/LinodeInstancesApi~cloneLinodeDiskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Disk}
     */
    cloneLinodeDisk(linodeId, diskId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling cloneLinodeDisk");
      }
      // verify the required parameter 'diskId' is set
      if (diskId === undefined || diskId === null) {
        throw new Error("Missing the required parameter 'diskId' when calling cloneLinodeDisk");
      }

      let pathParams = {
        'linodeId': linodeId,
        'diskId': diskId
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
      let returnType = Disk;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/disks/{diskId}/clone', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cloneLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~cloneLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Linode} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Clone
     * You can clone your Linode's existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the `add_linodes` grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 
     * @param {Number} linodeId ID of the Linode to clone.
     * @param {module:model/CloneLinodeInstanceRequest} cloneLinodeInstanceRequest The requested state your Linode will be cloned into.
     * @param {module:api/LinodeInstancesApi~cloneLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Linode}
     */
    cloneLinodeInstance(linodeId, cloneLinodeInstanceRequest, callback) {
      let postBody = cloneLinodeInstanceRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling cloneLinodeInstance");
      }
      // verify the required parameter 'cloneLinodeInstanceRequest' is set
      if (cloneLinodeInstanceRequest === undefined || cloneLinodeInstanceRequest === null) {
        throw new Error("Missing the required parameter 'cloneLinodeInstanceRequest' when calling cloneLinodeInstance");
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
      let returnType = Linode;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/clone', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~createLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Linode} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Create
     * Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the `add_linodes` grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type's specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be `running` after it completes `provisioning`.   * A default config with two Disks, one being a 512 swap disk, is created.     * `swap_size` can be used to customize the swap disk size.   * Requires a `root_pass` be supplied to use for the root User's Account.   * It is recommended to supply SSH keys for the root User using the `authorized_keys` field.   * You may also supply a list of usernames via the `authorized_users` field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be `running` after it completes `provisioning`.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a `root_pass` be supplied to use for the root User's Account.   * It is recommended to supply SSH keys for the root User using the `authorized_keys` field.   * You may also supply a list of usernames via the `authorized_users` field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode's backups.   * You must create a Linode large enough to accommodate the Backup's size.   * The Disks and Config will match that of the Linode that was backed up.   * The `root_pass` will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the `interfaces` property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain `offline` and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param {module:model/CreateLinodeInstanceRequest} createLinodeInstanceRequest The requested initial state of a new Linode.
     * @param {module:api/LinodeInstancesApi~createLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Linode}
     */
    createLinodeInstance(createLinodeInstanceRequest, callback) {
      let postBody = createLinodeInstanceRequest;
      // verify the required parameter 'createLinodeInstanceRequest' is set
      if (createLinodeInstanceRequest === undefined || createLinodeInstanceRequest === null) {
        throw new Error("Missing the required parameter 'createLinodeInstanceRequest' when calling createLinodeInstance");
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
      let returnType = Linode;
      return this.apiClient.callApi(
        '/linode/instances', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createSnapshot operation.
     * @callback module:api/LinodeInstancesApi~createSnapshotCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Backup} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Snapshot Create
     * Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 
     * @param {Number} linodeId The ID of the Linode the backups belong to.
     * @param {module:model/CreateSnapshotRequest} createSnapshotRequest 
     * @param {module:api/LinodeInstancesApi~createSnapshotCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Backup}
     */
    createSnapshot(linodeId, createSnapshotRequest, callback) {
      let postBody = createSnapshotRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling createSnapshot");
      }
      // verify the required parameter 'createSnapshotRequest' is set
      if (createSnapshotRequest === undefined || createSnapshotRequest === null) {
        throw new Error("Missing the required parameter 'createSnapshotRequest' when calling createSnapshot");
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
      let returnType = Backup;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/backups', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDisk operation.
     * @callback module:api/LinodeInstancesApi~deleteDiskCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk Delete
     * Deletes a Disk you have permission to `read_write`.  **Deleting a Disk is a destructive action and cannot be undone.** 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} diskId ID of the Disk to look up.
     * @param {module:api/LinodeInstancesApi~deleteDiskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteDisk(linodeId, diskId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling deleteDisk");
      }
      // verify the required parameter 'diskId' is set
      if (diskId === undefined || diskId === null) {
        throw new Error("Missing the required parameter 'diskId' when calling deleteDisk");
      }

      let pathParams = {
        'linodeId': linodeId,
        'diskId': diskId
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
        '/linode/instances/{linodeId}/disks/{diskId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteLinodeConfig operation.
     * @callback module:api/LinodeInstancesApi~deleteLinodeConfigCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configuration Profile Delete
     * Deletes the specified Configuration profile from the specified Linode. 
     * @param {Number} linodeId The ID of the Linode whose Configuration profile to look up.
     * @param {Number} configId The ID of the Configuration profile to look up.
     * @param {module:api/LinodeInstancesApi~deleteLinodeConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteLinodeConfig(linodeId, configId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling deleteLinodeConfig");
      }
      // verify the required parameter 'configId' is set
      if (configId === undefined || configId === null) {
        throw new Error("Missing the required parameter 'configId' when calling deleteLinodeConfig");
      }

      let pathParams = {
        'linodeId': linodeId,
        'configId': configId
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
        '/linode/instances/{linodeId}/configs/{configId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~deleteLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Delete
     * Deletes a Linode you have permission to `read_write`.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 
     * @param {Number} linodeId ID of the Linode to look up
     * @param {module:api/LinodeInstancesApi~deleteLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteLinodeInstance(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling deleteLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the enableBackups operation.
     * @callback module:api/LinodeInstancesApi~enableBackupsCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Backups Enable
     * Enables backups for the specified Linode. 
     * @param {Number} linodeId The ID of the Linode to enable backup service for.
     * @param {module:api/LinodeInstancesApi~enableBackupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    enableBackups(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling enableBackups");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/backups/enable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBackup operation.
     * @callback module:api/LinodeInstancesApi~getBackupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Backup} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Backup View
     * Returns information about a Backup. 
     * @param {Number} linodeId The ID of the Linode the Backup belongs to.
     * @param {Number} backupId The ID of the Backup to look up.
     * @param {module:api/LinodeInstancesApi~getBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Backup}
     */
    getBackup(linodeId, backupId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling getBackup");
      }

      let pathParams = {
        'linodeId': linodeId,
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
      let returnType = Backup;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/backups/{backupId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBackups operation.
     * @callback module:api/LinodeInstancesApi~getBackupsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetBackups200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Backups List
     * Returns information about this Linode's available backups. 
     * @param {Number} linodeId The ID of the Linode the backups belong to.
     * @param {module:api/LinodeInstancesApi~getBackupsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetBackups200Response}
     */
    getBackups(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getBackups");
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
      let returnType = GetBackups200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/backups', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKernel operation.
     * @callback module:api/LinodeInstancesApi~getKernelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Kernel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Kernel View
     * Returns information about a single Kernel. 
     * @param {String} kernelId ID of the Kernel to look up.
     * @param {module:api/LinodeInstancesApi~getKernelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Kernel}
     */
    getKernel(kernelId, callback) {
      let postBody = null;
      // verify the required parameter 'kernelId' is set
      if (kernelId === undefined || kernelId === null) {
        throw new Error("Missing the required parameter 'kernelId' when calling getKernel");
      }

      let pathParams = {
        'kernelId': kernelId
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
      let returnType = Kernel;
      return this.apiClient.callApi(
        '/linode/kernels/{kernelId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getKernels operation.
     * @callback module:api/LinodeInstancesApi~getKernelsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetKernels200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Kernels List
     * Lists available Kernels. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/LinodeInstancesApi~getKernelsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetKernels200Response}
     */
    getKernels(opts, callback) {
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
      let returnType = GetKernels200Response;
      return this.apiClient.callApi(
        '/linode/kernels', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeConfig operation.
     * @callback module:api/LinodeInstancesApi~getLinodeConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LinodeConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configuration Profile View
     * Returns information about a specific Configuration profile. 
     * @param {Number} linodeId The ID of the Linode whose Configuration profile to look up.
     * @param {Number} configId The ID of the Configuration profile to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LinodeConfig}
     */
    getLinodeConfig(linodeId, configId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeConfig");
      }
      // verify the required parameter 'configId' is set
      if (configId === undefined || configId === null) {
        throw new Error("Missing the required parameter 'configId' when calling getLinodeConfig");
      }

      let pathParams = {
        'linodeId': linodeId,
        'configId': configId
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
      let returnType = LinodeConfig;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/configs/{configId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeConfigs operation.
     * @callback module:api/LinodeInstancesApi~getLinodeConfigsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeConfigs200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configuration Profiles List
     * Lists Configuration profiles associated with a Linode. 
     * @param {Number} linodeId ID of the Linode to look up Configuration profiles for.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/LinodeInstancesApi~getLinodeConfigsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeConfigs200Response}
     */
    getLinodeConfigs(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeConfigs");
      }

      let pathParams = {
        'linodeId': linodeId
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
      let returnType = GetLinodeConfigs200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/configs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeDisk operation.
     * @callback module:api/LinodeInstancesApi~getLinodeDiskCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Disk} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk View
     * View Disk information for a Disk associated with this Linode. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} diskId ID of the Disk to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeDiskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Disk}
     */
    getLinodeDisk(linodeId, diskId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeDisk");
      }
      // verify the required parameter 'diskId' is set
      if (diskId === undefined || diskId === null) {
        throw new Error("Missing the required parameter 'diskId' when calling getLinodeDisk");
      }

      let pathParams = {
        'linodeId': linodeId,
        'diskId': diskId
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
      let returnType = Disk;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/disks/{diskId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeDisks operation.
     * @callback module:api/LinodeInstancesApi~getLinodeDisksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeDisks200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disks List
     * View Disk information for Disks associated with this Linode. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/LinodeInstancesApi~getLinodeDisksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeDisks200Response}
     */
    getLinodeDisks(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeDisks");
      }

      let pathParams = {
        'linodeId': linodeId
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
      let returnType = GetLinodeDisks200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/disks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeFirewalls operation.
     * @callback module:api/LinodeInstancesApi~getLinodeFirewallsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeFirewalls200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Firewalls List
     * View Firewall information for Firewalls associated with this Linode. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/LinodeInstancesApi~getLinodeFirewallsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeFirewalls200Response}
     */
    getLinodeFirewalls(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeFirewalls");
      }

      let pathParams = {
        'linodeId': linodeId
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
      let returnType = GetLinodeFirewalls200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/firewalls', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeIP operation.
     * @callback module:api/LinodeInstancesApi~getLinodeIPCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IPAddress} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * IP Address View
     * View information about the specified IP address associated with the specified Linode. 
     * @param {Number} linodeId The ID of the Linode to look up.
     * @param {String} address The IP address to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeIPCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IPAddress}
     */
    getLinodeIP(linodeId, address, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeIP");
      }
      // verify the required parameter 'address' is set
      if (address === undefined || address === null) {
        throw new Error("Missing the required parameter 'address' when calling getLinodeIP");
      }

      let pathParams = {
        'linodeId': linodeId,
        'address': address
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
      let returnType = IPAddress;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/ips/{address}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeIPs operation.
     * @callback module:api/LinodeInstancesApi~getLinodeIPsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeIPs200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Networking Information List
     * Returns networking information for a single Linode. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeIPsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeIPs200Response}
     */
    getLinodeIPs(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeIPs");
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
      let returnType = GetLinodeIPs200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/ips', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~getLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Linode} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode View
     * Get a specific Linode by ID.
     * @param {Number} linodeId ID of the Linode to look up
     * @param {module:api/LinodeInstancesApi~getLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Linode}
     */
    getLinodeInstance(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeInstance");
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
      let returnType = Linode;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeInstances operation.
     * @callback module:api/LinodeInstancesApi~getLinodeInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeInstances200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linodes List
     * Returns a paginated list of Linodes you have permission to view. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/LinodeInstancesApi~getLinodeInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeInstances200Response}
     */
    getLinodeInstances(opts, callback) {
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
      let returnType = GetLinodeInstances200Response;
      return this.apiClient.callApi(
        '/linode/instances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeNodeBalancers operation.
     * @callback module:api/LinodeInstancesApi~getLinodeNodeBalancersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeNodeBalancers200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode NodeBalancers View
     * Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User's Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 
     * @param {Number} linodeId ID of the Linode to look up
     * @param {module:api/LinodeInstancesApi~getLinodeNodeBalancersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeNodeBalancers200Response}
     */
    getLinodeNodeBalancers(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeNodeBalancers");
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
      let returnType = GetLinodeNodeBalancers200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/nodebalancers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeStats operation.
     * @callback module:api/LinodeInstancesApi~getLinodeStatsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LinodeStats} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Statistics View
     * Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeStatsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LinodeStats}
     */
    getLinodeStats(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeStats");
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
      let returnType = LinodeStats;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/stats', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeStatsByYearMonth operation.
     * @callback module:api/LinodeInstancesApi~getLinodeStatsByYearMonthCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LinodeStats} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Statistics View (year/month)
     * Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} year Numeric value representing the year to look up.
     * @param {Number} month Numeric value representing the month to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeStatsByYearMonthCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LinodeStats}
     */
    getLinodeStatsByYearMonth(linodeId, year, month, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeStatsByYearMonth");
      }
      // verify the required parameter 'year' is set
      if (year === undefined || year === null) {
        throw new Error("Missing the required parameter 'year' when calling getLinodeStatsByYearMonth");
      }
      // verify the required parameter 'month' is set
      if (month === undefined || month === null) {
        throw new Error("Missing the required parameter 'month' when calling getLinodeStatsByYearMonth");
      }

      let pathParams = {
        'linodeId': linodeId,
        'year': year,
        'month': month
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
      let returnType = LinodeStats;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/stats/{year}/{month}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeTransfer operation.
     * @callback module:api/LinodeInstancesApi~getLinodeTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeTransfer200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Network Transfer View
     * Returns a Linode's network transfer pool statistics for the current month. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeTransfer200Response}
     */
    getLinodeTransfer(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeTransfer");
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
      let returnType = GetLinodeTransfer200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/transfer', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeTransferByYearMonth operation.
     * @callback module:api/LinodeInstancesApi~getLinodeTransferByYearMonthCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeTransferByYearMonth200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Network Transfer View (year/month)
     * Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} year Numeric value representing the year to look up.
     * @param {Number} month Numeric value representing the month to look up.
     * @param {module:api/LinodeInstancesApi~getLinodeTransferByYearMonthCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeTransferByYearMonth200Response}
     */
    getLinodeTransferByYearMonth(linodeId, year, month, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeTransferByYearMonth");
      }
      // verify the required parameter 'year' is set
      if (year === undefined || year === null) {
        throw new Error("Missing the required parameter 'year' when calling getLinodeTransferByYearMonth");
      }
      // verify the required parameter 'month' is set
      if (month === undefined || month === null) {
        throw new Error("Missing the required parameter 'month' when calling getLinodeTransferByYearMonth");
      }

      let pathParams = {
        'linodeId': linodeId,
        'year': year,
        'month': month
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
      let returnType = GetLinodeTransferByYearMonth200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/transfer/{year}/{month}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinodeVolumes operation.
     * @callback module:api/LinodeInstancesApi~getLinodeVolumesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLinodeVolumes200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode's Volumes List
     * View Block Storage Volumes attached to this Linode. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/LinodeInstancesApi~getLinodeVolumesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLinodeVolumes200Response}
     */
    getLinodeVolumes(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling getLinodeVolumes");
      }

      let pathParams = {
        'linodeId': linodeId
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
      let returnType = GetLinodeVolumes200Response;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/volumes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the migrateLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~migrateLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * DC Migration/Pending Host Migration Initiate
     * Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a `region` parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 `/116` pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 
     * @param {Number} linodeId ID of the Linode to migrate.
     * @param {Object} opts Optional parameters
     * @param {module:model/MigrateLinodeInstanceRequest} [migrateLinodeInstanceRequest] 
     * @param {module:api/LinodeInstancesApi~migrateLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    migrateLinodeInstance(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['migrateLinodeInstanceRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling migrateLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/migrate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the mutateLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~mutateLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Upgrade
     * Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 
     * @param {Number} linodeId ID of the Linode to mutate.
     * @param {Object} opts Optional parameters
     * @param {module:model/MutateLinodeInstanceRequest} [mutateLinodeInstanceRequest] Whether to automatically resize disks or not.
     * @param {module:api/LinodeInstancesApi~mutateLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    mutateLinodeInstance(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['mutateLinodeInstanceRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling mutateLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/mutate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rebootLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~rebootLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Reboot
     * Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 
     * @param {Number} linodeId ID of the linode to reboot.
     * @param {Object} opts Optional parameters
     * @param {module:model/RebootLinodeInstanceRequest} [rebootLinodeInstanceRequest] Optional reboot parameters.
     * @param {module:api/LinodeInstancesApi~rebootLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    rebootLinodeInstance(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['rebootLinodeInstanceRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling rebootLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/reboot', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rebuildLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~rebuildLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Linode} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Rebuild
     * Rebuilds a Linode you have the `read_write` permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new `image` to the Linode with the given attributes. Additionally:    * Requires an `image` be supplied.   * Requires a `root_pass` be supplied to use for the root User's Account.   * It is recommended to supply SSH keys for the root User using the     `authorized_keys` field. 
     * @param {Number} linodeId ID of the Linode to rebuild.
     * @param {Object.<String, module:model/UNKNOWN_BASE_TYPE>} UNKNOWN_BASE_TYPE The requested state your Linode will be rebuilt into.
     * @param {module:api/LinodeInstancesApi~rebuildLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Linode}
     */
    rebuildLinodeInstance(linodeId, UNKNOWN_BASE_TYPE, callback) {
      let postBody = UNKNOWN_BASE_TYPE;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling rebuildLinodeInstance");
      }
      // verify the required parameter 'UNKNOWN_BASE_TYPE' is set
      if (UNKNOWN_BASE_TYPE === undefined || UNKNOWN_BASE_TYPE === null) {
        throw new Error("Missing the required parameter 'UNKNOWN_BASE_TYPE' when calling rebuildLinodeInstance");
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
      let returnType = Linode;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/rebuild', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the removeLinodeIP operation.
     * @callback module:api/LinodeInstancesApi~removeLinodeIPCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * IPv4 Address Delete
     * Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode's last remaining public IPv4 address. 
     * @param {Number} linodeId The ID of the Linode to look up.
     * @param {String} address The IP address to look up.
     * @param {module:api/LinodeInstancesApi~removeLinodeIPCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    removeLinodeIP(linodeId, address, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling removeLinodeIP");
      }
      // verify the required parameter 'address' is set
      if (address === undefined || address === null) {
        throw new Error("Missing the required parameter 'address' when calling removeLinodeIP");
      }

      let pathParams = {
        'linodeId': linodeId,
        'address': address
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
        '/linode/instances/{linodeId}/ips/{address}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the rescueLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~rescueLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Boot into Rescue Mode
     * Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \"sdh\" is reserved and unavailable during rescue. 
     * @param {Number} linodeId ID of the Linode to rescue.
     * @param {Object} opts Optional parameters
     * @param {module:model/RescueLinodeInstanceRequest} [rescueLinodeInstanceRequest] Optional object of devices to be mounted.
     * @param {module:api/LinodeInstancesApi~rescueLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    rescueLinodeInstance(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['rescueLinodeInstanceRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling rescueLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/rescue', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resetDiskPassword operation.
     * @callback module:api/LinodeInstancesApi~resetDiskPasswordCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk Root Password Reset
     * Resets the password of a Disk you have permission to `read_write`. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} diskId ID of the Disk to look up.
     * @param {module:model/ResetDiskPasswordRequest} resetDiskPasswordRequest The new password.
     * @param {module:api/LinodeInstancesApi~resetDiskPasswordCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    resetDiskPassword(linodeId, diskId, resetDiskPasswordRequest, callback) {
      let postBody = resetDiskPasswordRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling resetDiskPassword");
      }
      // verify the required parameter 'diskId' is set
      if (diskId === undefined || diskId === null) {
        throw new Error("Missing the required parameter 'diskId' when calling resetDiskPassword");
      }
      // verify the required parameter 'resetDiskPasswordRequest' is set
      if (resetDiskPasswordRequest === undefined || resetDiskPasswordRequest === null) {
        throw new Error("Missing the required parameter 'resetDiskPasswordRequest' when calling resetDiskPassword");
      }

      let pathParams = {
        'linodeId': linodeId,
        'diskId': diskId
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
        '/linode/instances/{linodeId}/disks/{diskId}/password', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resetLinodePassword operation.
     * @callback module:api/LinodeInstancesApi~resetLinodePasswordCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Root Password Reset
     * Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk's root password. * A `password_reset` event is generated when a root password reset is successful. 
     * @param {Number} linodeId ID of the Linode for which to reset its root password.
     * @param {Object} opts Optional parameters
     * @param {module:model/ResetLinodePasswordRequest} [resetLinodePasswordRequest] This Linode's new root password.
     * @param {module:api/LinodeInstancesApi~resetLinodePasswordCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    resetLinodePassword(linodeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['resetLinodePasswordRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling resetLinodePassword");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/password', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resizeDisk operation.
     * @callback module:api/LinodeInstancesApi~resizeDiskCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk Resize
     * Resizes a Disk you have permission to `read_write`.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode's active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} diskId ID of the Disk to look up.
     * @param {module:model/ResizeDiskRequest} resizeDiskRequest The new size of the Disk.
     * @param {module:api/LinodeInstancesApi~resizeDiskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    resizeDisk(linodeId, diskId, resizeDiskRequest, callback) {
      let postBody = resizeDiskRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling resizeDisk");
      }
      // verify the required parameter 'diskId' is set
      if (diskId === undefined || diskId === null) {
        throw new Error("Missing the required parameter 'diskId' when calling resizeDisk");
      }
      // verify the required parameter 'resizeDiskRequest' is set
      if (resizeDiskRequest === undefined || resizeDiskRequest === null) {
        throw new Error("Missing the required parameter 'resizeDiskRequest' when calling resizeDisk");
      }

      let pathParams = {
        'linodeId': linodeId,
        'diskId': diskId
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
        '/linode/instances/{linodeId}/disks/{diskId}/resize', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the resizeLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~resizeLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Resize
     * Resizes a Linode you have the `read_write` permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 
     * @param {Number} linodeId ID of the Linode to resize.
     * @param {module:model/ResizeLinodeInstanceRequest} resizeLinodeInstanceRequest The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode's disks. 
     * @param {module:api/LinodeInstancesApi~resizeLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    resizeLinodeInstance(linodeId, resizeLinodeInstanceRequest, callback) {
      let postBody = resizeLinodeInstanceRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling resizeLinodeInstance");
      }
      // verify the required parameter 'resizeLinodeInstanceRequest' is set
      if (resizeLinodeInstanceRequest === undefined || resizeLinodeInstanceRequest === null) {
        throw new Error("Missing the required parameter 'resizeLinodeInstanceRequest' when calling resizeLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/resize', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the restoreBackup operation.
     * @callback module:api/LinodeInstancesApi~restoreBackupCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Backup Restore
     * Restores a Linode's Backup to the specified Linode. 
     * @param {Number} linodeId The ID of the Linode that the Backup belongs to.
     * @param {Number} backupId The ID of the Backup to restore.
     * @param {module:model/RestoreBackupRequest} restoreBackupRequest Parameters to provide when restoring the Backup.
     * @param {module:api/LinodeInstancesApi~restoreBackupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    restoreBackup(linodeId, backupId, restoreBackupRequest, callback) {
      let postBody = restoreBackupRequest;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling restoreBackup");
      }
      // verify the required parameter 'backupId' is set
      if (backupId === undefined || backupId === null) {
        throw new Error("Missing the required parameter 'backupId' when calling restoreBackup");
      }
      // verify the required parameter 'restoreBackupRequest' is set
      if (restoreBackupRequest === undefined || restoreBackupRequest === null) {
        throw new Error("Missing the required parameter 'restoreBackupRequest' when calling restoreBackup");
      }

      let pathParams = {
        'linodeId': linodeId,
        'backupId': backupId
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
        '/linode/instances/{linodeId}/backups/{backupId}/restore', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the shutdownLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~shutdownLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Shut Down
     * Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 
     * @param {Number} linodeId ID of the Linode to shutdown.
     * @param {module:api/LinodeInstancesApi~shutdownLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    shutdownLinodeInstance(linodeId, callback) {
      let postBody = null;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling shutdownLinodeInstance");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/shutdown', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateDisk operation.
     * @callback module:api/LinodeInstancesApi~updateDiskCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Disk} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disk Update
     * Updates a Disk that you have permission to `read_write`. 
     * @param {Number} linodeId ID of the Linode to look up.
     * @param {Number} diskId ID of the Disk to look up.
     * @param {module:model/Disk} disk Updates the parameters of a single Disk. 
     * @param {module:api/LinodeInstancesApi~updateDiskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Disk}
     */
    updateDisk(linodeId, diskId, disk, callback) {
      let postBody = disk;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling updateDisk");
      }
      // verify the required parameter 'diskId' is set
      if (diskId === undefined || diskId === null) {
        throw new Error("Missing the required parameter 'diskId' when calling updateDisk");
      }
      // verify the required parameter 'disk' is set
      if (disk === undefined || disk === null) {
        throw new Error("Missing the required parameter 'disk' when calling updateDisk");
      }

      let pathParams = {
        'linodeId': linodeId,
        'diskId': diskId
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
      let returnType = Disk;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/disks/{diskId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateLinodeConfig operation.
     * @callback module:api/LinodeInstancesApi~updateLinodeConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LinodeConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configuration Profile Update
     * Updates a Configuration profile. 
     * @param {Number} linodeId The ID of the Linode whose Configuration profile to look up.
     * @param {Number} configId The ID of the Configuration profile to look up.
     * @param {module:model/LinodeConfig} linodeConfig The Configuration profile parameters to modify.
     * @param {module:api/LinodeInstancesApi~updateLinodeConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LinodeConfig}
     */
    updateLinodeConfig(linodeId, configId, linodeConfig, callback) {
      let postBody = linodeConfig;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling updateLinodeConfig");
      }
      // verify the required parameter 'configId' is set
      if (configId === undefined || configId === null) {
        throw new Error("Missing the required parameter 'configId' when calling updateLinodeConfig");
      }
      // verify the required parameter 'linodeConfig' is set
      if (linodeConfig === undefined || linodeConfig === null) {
        throw new Error("Missing the required parameter 'linodeConfig' when calling updateLinodeConfig");
      }

      let pathParams = {
        'linodeId': linodeId,
        'configId': configId
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
      let returnType = LinodeConfig;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/configs/{configId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateLinodeIP operation.
     * @callback module:api/LinodeInstancesApi~updateLinodeIPCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IPAddress} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * IP Address Update
     * Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to `null` for a public IPv4 address, resets it to the default \"ip.linodeusercontent.com\" RDNS value. 
     * @param {Number} linodeId The ID of the Linode to look up.
     * @param {String} address The IP address to look up.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateLinodeIPRequest} [updateLinodeIPRequest] The information to update for the IP address.
     * @param {module:api/LinodeInstancesApi~updateLinodeIPCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IPAddress}
     */
    updateLinodeIP(linodeId, address, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateLinodeIPRequest'];
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling updateLinodeIP");
      }
      // verify the required parameter 'address' is set
      if (address === undefined || address === null) {
        throw new Error("Missing the required parameter 'address' when calling updateLinodeIP");
      }

      let pathParams = {
        'linodeId': linodeId,
        'address': address
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
      let returnType = IPAddress;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}/ips/{address}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateLinodeInstance operation.
     * @callback module:api/LinodeInstancesApi~updateLinodeInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Linode} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Update
     * Updates a Linode that you have permission to `read_write`.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param {Number} linodeId ID of the Linode to look up
     * @param {module:model/Linode} linode Any field that is not marked as `readOnly` may be updated. Fields that are marked `readOnly` will be ignored. If any updated field fails to pass validation, the Linode will not be updated. 
     * @param {module:api/LinodeInstancesApi~updateLinodeInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Linode}
     */
    updateLinodeInstance(linodeId, linode, callback) {
      let postBody = linode;
      // verify the required parameter 'linodeId' is set
      if (linodeId === undefined || linodeId === null) {
        throw new Error("Missing the required parameter 'linodeId' when calling updateLinodeInstance");
      }
      // verify the required parameter 'linode' is set
      if (linode === undefined || linode === null) {
        throw new Error("Missing the required parameter 'linode' when calling updateLinodeInstance");
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
      let returnType = Linode;
      return this.apiClient.callApi(
        '/linode/instances/{linodeId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
