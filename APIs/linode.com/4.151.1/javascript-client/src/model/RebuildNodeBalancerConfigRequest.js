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

import ApiClient from '../ApiClient';
import NodeBalancerConfig from './NodeBalancerConfig';
import NodeBalancerConfigNodesStatus from './NodeBalancerConfigNodesStatus';
import RebuildNodeBalancerConfigRequestAllOfNodesInner from './RebuildNodeBalancerConfigRequestAllOfNodesInner';

/**
 * The RebuildNodeBalancerConfigRequest model module.
 * @module model/RebuildNodeBalancerConfigRequest
 * @version 4.151.1
 */
class RebuildNodeBalancerConfigRequest {
    /**
     * Constructs a new <code>RebuildNodeBalancerConfigRequest</code>.
     * @alias module:model/RebuildNodeBalancerConfigRequest
     * @implements module:model/NodeBalancerConfig
     * @param nodes {Array.<module:model/RebuildNodeBalancerConfigRequestAllOfNodesInner>} The NodeBalancer Node(s) that serve this Config.  Some considerations for Nodes when rebuilding a config:   * Current Nodes excluded from the request body will be deleted from the Config.   * Current Nodes (identified by their Node ID) will be updated.   * New Nodes (included without a Node ID) will be created. 
     */
    constructor(nodes) { 
        NodeBalancerConfig.initialize(this);
        RebuildNodeBalancerConfigRequest.initialize(this, nodes);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, nodes) { 
        obj['algorithm'] = 'roundrobin';
        obj['check'] = 'none';
        obj['check_attempts'] = 3;
        obj['check_interval'] = 31;
        obj['check_passive'] = true;
        obj['check_timeout'] = 30;
        obj['cipher_suite'] = 'recommended';
        obj['port'] = 80;
        obj['protocol'] = 'http';
        obj['proxy_protocol'] = 'none';
        obj['stickiness'] = 'none';
        obj['nodes'] = nodes;
    }

    /**
     * Constructs a <code>RebuildNodeBalancerConfigRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RebuildNodeBalancerConfigRequest} obj Optional instance to populate.
     * @return {module:model/RebuildNodeBalancerConfigRequest} The populated <code>RebuildNodeBalancerConfigRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RebuildNodeBalancerConfigRequest();
            NodeBalancerConfig.constructFromObject(data, obj);

            if (data.hasOwnProperty('algorithm')) {
                obj['algorithm'] = ApiClient.convertToType(data['algorithm'], 'String');
            }
            if (data.hasOwnProperty('check')) {
                obj['check'] = ApiClient.convertToType(data['check'], 'String');
            }
            if (data.hasOwnProperty('check_attempts')) {
                obj['check_attempts'] = ApiClient.convertToType(data['check_attempts'], 'Number');
            }
            if (data.hasOwnProperty('check_body')) {
                obj['check_body'] = ApiClient.convertToType(data['check_body'], 'String');
            }
            if (data.hasOwnProperty('check_interval')) {
                obj['check_interval'] = ApiClient.convertToType(data['check_interval'], 'Number');
            }
            if (data.hasOwnProperty('check_passive')) {
                obj['check_passive'] = ApiClient.convertToType(data['check_passive'], 'Boolean');
            }
            if (data.hasOwnProperty('check_path')) {
                obj['check_path'] = ApiClient.convertToType(data['check_path'], 'String');
            }
            if (data.hasOwnProperty('check_timeout')) {
                obj['check_timeout'] = ApiClient.convertToType(data['check_timeout'], 'Number');
            }
            if (data.hasOwnProperty('cipher_suite')) {
                obj['cipher_suite'] = ApiClient.convertToType(data['cipher_suite'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('nodebalancer_id')) {
                obj['nodebalancer_id'] = ApiClient.convertToType(data['nodebalancer_id'], 'Number');
            }
            if (data.hasOwnProperty('nodes_status')) {
                obj['nodes_status'] = NodeBalancerConfigNodesStatus.constructFromObject(data['nodes_status']);
            }
            if (data.hasOwnProperty('port')) {
                obj['port'] = ApiClient.convertToType(data['port'], 'Number');
            }
            if (data.hasOwnProperty('protocol')) {
                obj['protocol'] = ApiClient.convertToType(data['protocol'], 'String');
            }
            if (data.hasOwnProperty('proxy_protocol')) {
                obj['proxy_protocol'] = ApiClient.convertToType(data['proxy_protocol'], 'String');
            }
            if (data.hasOwnProperty('ssl_cert')) {
                obj['ssl_cert'] = ApiClient.convertToType(data['ssl_cert'], 'String');
            }
            if (data.hasOwnProperty('ssl_commonname')) {
                obj['ssl_commonname'] = ApiClient.convertToType(data['ssl_commonname'], 'String');
            }
            if (data.hasOwnProperty('ssl_fingerprint')) {
                obj['ssl_fingerprint'] = ApiClient.convertToType(data['ssl_fingerprint'], 'String');
            }
            if (data.hasOwnProperty('ssl_key')) {
                obj['ssl_key'] = ApiClient.convertToType(data['ssl_key'], 'String');
            }
            if (data.hasOwnProperty('stickiness')) {
                obj['stickiness'] = ApiClient.convertToType(data['stickiness'], 'String');
            }
            if (data.hasOwnProperty('nodes')) {
                obj['nodes'] = ApiClient.convertToType(data['nodes'], [RebuildNodeBalancerConfigRequestAllOfNodesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RebuildNodeBalancerConfigRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RebuildNodeBalancerConfigRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RebuildNodeBalancerConfigRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['algorithm'] && !(typeof data['algorithm'] === 'string' || data['algorithm'] instanceof String)) {
            throw new Error("Expected the field `algorithm` to be a primitive type in the JSON string but got " + data['algorithm']);
        }
        // ensure the json data is a string
        if (data['check'] && !(typeof data['check'] === 'string' || data['check'] instanceof String)) {
            throw new Error("Expected the field `check` to be a primitive type in the JSON string but got " + data['check']);
        }
        // ensure the json data is a string
        if (data['check_body'] && !(typeof data['check_body'] === 'string' || data['check_body'] instanceof String)) {
            throw new Error("Expected the field `check_body` to be a primitive type in the JSON string but got " + data['check_body']);
        }
        // ensure the json data is a string
        if (data['check_path'] && !(typeof data['check_path'] === 'string' || data['check_path'] instanceof String)) {
            throw new Error("Expected the field `check_path` to be a primitive type in the JSON string but got " + data['check_path']);
        }
        // ensure the json data is a string
        if (data['cipher_suite'] && !(typeof data['cipher_suite'] === 'string' || data['cipher_suite'] instanceof String)) {
            throw new Error("Expected the field `cipher_suite` to be a primitive type in the JSON string but got " + data['cipher_suite']);
        }
        // validate the optional field `nodes_status`
        if (data['nodes_status']) { // data not null
          NodeBalancerConfigNodesStatus.validateJSON(data['nodes_status']);
        }
        // ensure the json data is a string
        if (data['protocol'] && !(typeof data['protocol'] === 'string' || data['protocol'] instanceof String)) {
            throw new Error("Expected the field `protocol` to be a primitive type in the JSON string but got " + data['protocol']);
        }
        // ensure the json data is a string
        if (data['proxy_protocol'] && !(typeof data['proxy_protocol'] === 'string' || data['proxy_protocol'] instanceof String)) {
            throw new Error("Expected the field `proxy_protocol` to be a primitive type in the JSON string but got " + data['proxy_protocol']);
        }
        // ensure the json data is a string
        if (data['ssl_cert'] && !(typeof data['ssl_cert'] === 'string' || data['ssl_cert'] instanceof String)) {
            throw new Error("Expected the field `ssl_cert` to be a primitive type in the JSON string but got " + data['ssl_cert']);
        }
        // ensure the json data is a string
        if (data['ssl_commonname'] && !(typeof data['ssl_commonname'] === 'string' || data['ssl_commonname'] instanceof String)) {
            throw new Error("Expected the field `ssl_commonname` to be a primitive type in the JSON string but got " + data['ssl_commonname']);
        }
        // ensure the json data is a string
        if (data['ssl_fingerprint'] && !(typeof data['ssl_fingerprint'] === 'string' || data['ssl_fingerprint'] instanceof String)) {
            throw new Error("Expected the field `ssl_fingerprint` to be a primitive type in the JSON string but got " + data['ssl_fingerprint']);
        }
        // ensure the json data is a string
        if (data['ssl_key'] && !(typeof data['ssl_key'] === 'string' || data['ssl_key'] instanceof String)) {
            throw new Error("Expected the field `ssl_key` to be a primitive type in the JSON string but got " + data['ssl_key']);
        }
        // ensure the json data is a string
        if (data['stickiness'] && !(typeof data['stickiness'] === 'string' || data['stickiness'] instanceof String)) {
            throw new Error("Expected the field `stickiness` to be a primitive type in the JSON string but got " + data['stickiness']);
        }
        if (data['nodes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['nodes'])) {
                throw new Error("Expected the field `nodes` to be an array in the JSON data but got " + data['nodes']);
            }
            // validate the optional field `nodes` (array)
            for (const item of data['nodes']) {
                RebuildNodeBalancerConfigRequestAllOfNodesInner.validateJSON(item);
            };
        }

        return true;
    }


}

RebuildNodeBalancerConfigRequest.RequiredProperties = ["nodes"];

/**
 * What algorithm this NodeBalancer should use for routing traffic to backends. 
 * @member {module:model/RebuildNodeBalancerConfigRequest.AlgorithmEnum} algorithm
 * @default 'roundrobin'
 */
RebuildNodeBalancerConfigRequest.prototype['algorithm'] = 'roundrobin';

/**
 * The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. * If `none` no check is performed. * `connection` requires only a connection to the backend to succeed. * `http` and `http_body` rely on the backend serving HTTP, and that   the response returned matches what is expected. 
 * @member {module:model/RebuildNodeBalancerConfigRequest.CheckEnum} check
 * @default 'none'
 */
RebuildNodeBalancerConfigRequest.prototype['check'] = 'none';

/**
 * How many times to attempt a check before considering a backend to be down. 
 * @member {Number} check_attempts
 * @default 3
 */
RebuildNodeBalancerConfigRequest.prototype['check_attempts'] = 3;

/**
 * This value must be present in the response body of the check in order for it to pass. If this value is not present in the response body of a check request, the backend is considered to be down. 
 * @member {String} check_body
 */
RebuildNodeBalancerConfigRequest.prototype['check_body'] = undefined;

/**
 * How often, in seconds, to check that backends are up and serving requests.  Must be greater than `check_timeout`. 
 * @member {Number} check_interval
 * @default 31
 */
RebuildNodeBalancerConfigRequest.prototype['check_interval'] = 31;

/**
 * If true, any response from this backend with a `5xx` status code will be enough for it to be considered unhealthy and taken out of rotation. 
 * @member {Boolean} check_passive
 * @default true
 */
RebuildNodeBalancerConfigRequest.prototype['check_passive'] = true;

/**
 * The URL path to check on each backend. If the backend does not respond to this request it is considered to be down. 
 * @member {String} check_path
 */
RebuildNodeBalancerConfigRequest.prototype['check_path'] = undefined;

/**
 * How long, in seconds, to wait for a check attempt before considering it failed.  Must be less than `check_interval`. 
 * @member {Number} check_timeout
 * @default 30
 */
RebuildNodeBalancerConfigRequest.prototype['check_timeout'] = 30;

/**
 * What ciphers to use for SSL connections served by this NodeBalancer.  * `legacy` is considered insecure and should only be used if necessary. 
 * @member {module:model/RebuildNodeBalancerConfigRequest.CipherSuiteEnum} cipher_suite
 * @default 'recommended'
 */
RebuildNodeBalancerConfigRequest.prototype['cipher_suite'] = 'recommended';

/**
 * This config's unique ID
 * @member {Number} id
 */
RebuildNodeBalancerConfigRequest.prototype['id'] = undefined;

/**
 * The ID for the NodeBalancer this config belongs to. 
 * @member {Number} nodebalancer_id
 */
RebuildNodeBalancerConfigRequest.prototype['nodebalancer_id'] = undefined;

/**
 * @member {module:model/NodeBalancerConfigNodesStatus} nodes_status
 */
RebuildNodeBalancerConfigRequest.prototype['nodes_status'] = undefined;

/**
 * The port this Config is for. These values must be unique across configs on a single NodeBalancer (you can't have two configs for port 80, for example).  While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. 
 * @member {Number} port
 * @default 80
 */
RebuildNodeBalancerConfigRequest.prototype['port'] = 80;

/**
 * The protocol this port is configured to serve.  * The `http` and `tcp` protocols do not support `ssl_cert` and `ssl_key`.  * The `https` protocol is mutually required with `ssl_cert` and `ssl_key`.  Review our guide on [Available Protocols](/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features. 
 * @member {module:model/RebuildNodeBalancerConfigRequest.ProtocolEnum} protocol
 * @default 'http'
 */
RebuildNodeBalancerConfigRequest.prototype['protocol'] = 'http';

/**
 * ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.  * If ommited, or set to `none`, the NodeBalancer doesn't send any auxilary data over TCP connections. This is the default. * If set to `v1`, the human-readable header format (Version 1) is used. Requires `tcp` protocol. * If set to `v2`, the binary header format (Version 2) is used. Requires `tcp` protocol. 
 * @member {module:model/RebuildNodeBalancerConfigRequest.ProxyProtocolEnum} proxy_protocol
 * @default 'none'
 */
RebuildNodeBalancerConfigRequest.prototype['proxy_protocol'] = 'none';

/**
 * The PEM-formatted public SSL certificate (or the combined PEM-formatted SSL certificate and Certificate Authority chain) that should be served on this NodeBalancerConfig's port.  Line breaks must be represented as \"\\n\" in the string for requests (but not when using the Linode CLI).  [Diffie-Hellman Parameters](/docs/products/networking/nodebalancers/guides/ssl-termination/#diffie-hellman-parameters) can be included in this value to enable forward secrecy.  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, `<REDACTED>` will be printed where the field appears.  The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig. 
 * @member {String} ssl_cert
 */
RebuildNodeBalancerConfigRequest.prototype['ssl_cert'] = undefined;

/**
 * The read-only common name automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig. 
 * @member {String} ssl_commonname
 */
RebuildNodeBalancerConfigRequest.prototype['ssl_commonname'] = undefined;

/**
 * The read-only SHA1-encoded fingerprint automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig. 
 * @member {String} ssl_fingerprint
 */
RebuildNodeBalancerConfigRequest.prototype['ssl_fingerprint'] = undefined;

/**
 * The PEM-formatted private key for the SSL certificate set in the `ssl_cert` field.  Line breaks must be represented as \"\\n\" in the string for requests (but not when using the Linode CLI).  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, `<REDACTED>` will be printed where the field appears.  The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig. 
 * @member {String} ssl_key
 */
RebuildNodeBalancerConfigRequest.prototype['ssl_key'] = undefined;

/**
 * Controls how session stickiness is handled on this port. * If set to `none` connections will always be assigned a backend based on the algorithm configured. * If set to `table` sessions from the same remote address will be routed to the same   backend.  * For HTTP or HTTPS clients, `http_cookie` allows sessions to be   routed to the same backend based on a cookie set by the NodeBalancer. 
 * @member {module:model/RebuildNodeBalancerConfigRequest.StickinessEnum} stickiness
 * @default 'none'
 */
RebuildNodeBalancerConfigRequest.prototype['stickiness'] = 'none';

/**
 * The NodeBalancer Node(s) that serve this Config.  Some considerations for Nodes when rebuilding a config:   * Current Nodes excluded from the request body will be deleted from the Config.   * Current Nodes (identified by their Node ID) will be updated.   * New Nodes (included without a Node ID) will be created. 
 * @member {Array.<module:model/RebuildNodeBalancerConfigRequestAllOfNodesInner>} nodes
 */
RebuildNodeBalancerConfigRequest.prototype['nodes'] = undefined;


// Implement NodeBalancerConfig interface:
/**
 * What algorithm this NodeBalancer should use for routing traffic to backends. 
 * @member {module:model/NodeBalancerConfig.AlgorithmEnum} algorithm
 * @default 'roundrobin'
 */
NodeBalancerConfig.prototype['algorithm'] = 'roundrobin';
/**
 * The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down. * If `none` no check is performed. * `connection` requires only a connection to the backend to succeed. * `http` and `http_body` rely on the backend serving HTTP, and that   the response returned matches what is expected. 
 * @member {module:model/NodeBalancerConfig.CheckEnum} check
 * @default 'none'
 */
NodeBalancerConfig.prototype['check'] = 'none';
/**
 * How many times to attempt a check before considering a backend to be down. 
 * @member {Number} check_attempts
 * @default 3
 */
NodeBalancerConfig.prototype['check_attempts'] = 3;
/**
 * This value must be present in the response body of the check in order for it to pass. If this value is not present in the response body of a check request, the backend is considered to be down. 
 * @member {String} check_body
 */
NodeBalancerConfig.prototype['check_body'] = undefined;
/**
 * How often, in seconds, to check that backends are up and serving requests.  Must be greater than `check_timeout`. 
 * @member {Number} check_interval
 * @default 31
 */
NodeBalancerConfig.prototype['check_interval'] = 31;
/**
 * If true, any response from this backend with a `5xx` status code will be enough for it to be considered unhealthy and taken out of rotation. 
 * @member {Boolean} check_passive
 * @default true
 */
NodeBalancerConfig.prototype['check_passive'] = true;
/**
 * The URL path to check on each backend. If the backend does not respond to this request it is considered to be down. 
 * @member {String} check_path
 */
NodeBalancerConfig.prototype['check_path'] = undefined;
/**
 * How long, in seconds, to wait for a check attempt before considering it failed.  Must be less than `check_interval`. 
 * @member {Number} check_timeout
 * @default 30
 */
NodeBalancerConfig.prototype['check_timeout'] = 30;
/**
 * What ciphers to use for SSL connections served by this NodeBalancer.  * `legacy` is considered insecure and should only be used if necessary. 
 * @member {module:model/NodeBalancerConfig.CipherSuiteEnum} cipher_suite
 * @default 'recommended'
 */
NodeBalancerConfig.prototype['cipher_suite'] = 'recommended';
/**
 * This config's unique ID
 * @member {Number} id
 */
NodeBalancerConfig.prototype['id'] = undefined;
/**
 * The ID for the NodeBalancer this config belongs to. 
 * @member {Number} nodebalancer_id
 */
NodeBalancerConfig.prototype['nodebalancer_id'] = undefined;
/**
 * @member {module:model/NodeBalancerConfigNodesStatus} nodes_status
 */
NodeBalancerConfig.prototype['nodes_status'] = undefined;
/**
 * The port this Config is for. These values must be unique across configs on a single NodeBalancer (you can't have two configs for port 80, for example).  While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443. 
 * @member {Number} port
 * @default 80
 */
NodeBalancerConfig.prototype['port'] = 80;
/**
 * The protocol this port is configured to serve.  * The `http` and `tcp` protocols do not support `ssl_cert` and `ssl_key`.  * The `https` protocol is mutually required with `ssl_cert` and `ssl_key`.  Review our guide on [Available Protocols](/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features. 
 * @member {module:model/NodeBalancerConfig.ProtocolEnum} protocol
 * @default 'http'
 */
NodeBalancerConfig.prototype['protocol'] = 'http';
/**
 * ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.  * If ommited, or set to `none`, the NodeBalancer doesn't send any auxilary data over TCP connections. This is the default. * If set to `v1`, the human-readable header format (Version 1) is used. Requires `tcp` protocol. * If set to `v2`, the binary header format (Version 2) is used. Requires `tcp` protocol. 
 * @member {module:model/NodeBalancerConfig.ProxyProtocolEnum} proxy_protocol
 * @default 'none'
 */
NodeBalancerConfig.prototype['proxy_protocol'] = 'none';
/**
 * The PEM-formatted public SSL certificate (or the combined PEM-formatted SSL certificate and Certificate Authority chain) that should be served on this NodeBalancerConfig's port.  Line breaks must be represented as \"\\n\" in the string for requests (but not when using the Linode CLI).  [Diffie-Hellman Parameters](/docs/products/networking/nodebalancers/guides/ssl-termination/#diffie-hellman-parameters) can be included in this value to enable forward secrecy.  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, `<REDACTED>` will be printed where the field appears.  The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig. 
 * @member {String} ssl_cert
 */
NodeBalancerConfig.prototype['ssl_cert'] = undefined;
/**
 * The read-only common name automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig. 
 * @member {String} ssl_commonname
 */
NodeBalancerConfig.prototype['ssl_commonname'] = undefined;
/**
 * The read-only SHA1-encoded fingerprint automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig. 
 * @member {String} ssl_fingerprint
 */
NodeBalancerConfig.prototype['ssl_fingerprint'] = undefined;
/**
 * The PEM-formatted private key for the SSL certificate set in the `ssl_cert` field.  Line breaks must be represented as \"\\n\" in the string for requests (but not when using the Linode CLI).  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, `<REDACTED>` will be printed where the field appears.  The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig. 
 * @member {String} ssl_key
 */
NodeBalancerConfig.prototype['ssl_key'] = undefined;
/**
 * Controls how session stickiness is handled on this port. * If set to `none` connections will always be assigned a backend based on the algorithm configured. * If set to `table` sessions from the same remote address will be routed to the same   backend.  * For HTTP or HTTPS clients, `http_cookie` allows sessions to be   routed to the same backend based on a cookie set by the NodeBalancer. 
 * @member {module:model/NodeBalancerConfig.StickinessEnum} stickiness
 * @default 'none'
 */
NodeBalancerConfig.prototype['stickiness'] = 'none';



/**
 * Allowed values for the <code>algorithm</code> property.
 * @enum {String}
 * @readonly
 */
RebuildNodeBalancerConfigRequest['AlgorithmEnum'] = {

    /**
     * value: "roundrobin"
     * @const
     */
    "roundrobin": "roundrobin",

    /**
     * value: "leastconn"
     * @const
     */
    "leastconn": "leastconn",

    /**
     * value: "source"
     * @const
     */
    "source": "source"
};


/**
 * Allowed values for the <code>check</code> property.
 * @enum {String}
 * @readonly
 */
RebuildNodeBalancerConfigRequest['CheckEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "connection"
     * @const
     */
    "connection": "connection",

    /**
     * value: "http"
     * @const
     */
    "http": "http",

    /**
     * value: "http_body"
     * @const
     */
    "http_body": "http_body"
};


/**
 * Allowed values for the <code>cipher_suite</code> property.
 * @enum {String}
 * @readonly
 */
RebuildNodeBalancerConfigRequest['CipherSuiteEnum'] = {

    /**
     * value: "recommended"
     * @const
     */
    "recommended": "recommended",

    /**
     * value: "legacy"
     * @const
     */
    "legacy": "legacy"
};


/**
 * Allowed values for the <code>protocol</code> property.
 * @enum {String}
 * @readonly
 */
RebuildNodeBalancerConfigRequest['ProtocolEnum'] = {

    /**
     * value: "http"
     * @const
     */
    "http": "http",

    /**
     * value: "https"
     * @const
     */
    "https": "https",

    /**
     * value: "tcp"
     * @const
     */
    "tcp": "tcp"
};


/**
 * Allowed values for the <code>proxy_protocol</code> property.
 * @enum {String}
 * @readonly
 */
RebuildNodeBalancerConfigRequest['ProxyProtocolEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "v1"
     * @const
     */
    "v1": "v1",

    /**
     * value: "v2"
     * @const
     */
    "v2": "v2"
};


/**
 * Allowed values for the <code>stickiness</code> property.
 * @enum {String}
 * @readonly
 */
RebuildNodeBalancerConfigRequest['StickinessEnum'] = {

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "table"
     * @const
     */
    "table": "table",

    /**
     * value: "http_cookie"
     * @const
     */
    "http_cookie": "http_cookie"
};



export default RebuildNodeBalancerConfigRequest;

