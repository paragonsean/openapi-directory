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
import Account from '../model/Account';
import AccountSettings from '../model/AccountSettings';
import CancelAccount200Response from '../model/CancelAccount200Response';
import CancelAccount409Response from '../model/CancelAccount409Response';
import CancelAccountRequest from '../model/CancelAccountRequest';
import CreateEntityTransferRequest from '../model/CreateEntityTransferRequest';
import CreatePayPalPayment200Response from '../model/CreatePayPalPayment200Response';
import CreatePayment202Response from '../model/CreatePayment202Response';
import CreatePaymentMethodRequest from '../model/CreatePaymentMethodRequest';
import CreatePromoCreditRequest from '../model/CreatePromoCreditRequest';
import CreateServiceTransferRequest from '../model/CreateServiceTransferRequest';
import CreditCard from '../model/CreditCard';
import EntityTransfer from '../model/EntityTransfer';
import Event from '../model/Event';
import GetAccountDefaultResponse from '../model/GetAccountDefaultResponse';
import GetAccountLogins200Response from '../model/GetAccountLogins200Response';
import GetClients200Response from '../model/GetClients200Response';
import GetEntityTransfers200Response from '../model/GetEntityTransfers200Response';
import GetEvents200Response from '../model/GetEvents200Response';
import GetInvoiceItems200Response from '../model/GetInvoiceItems200Response';
import GetInvoices200Response from '../model/GetInvoices200Response';
import GetMaintenance200Response from '../model/GetMaintenance200Response';
import GetNotifications200Response from '../model/GetNotifications200Response';
import GetPaymentMethods200Response from '../model/GetPaymentMethods200Response';
import GetPayments200Response from '../model/GetPayments200Response';
import GetServiceTransfers200Response from '../model/GetServiceTransfers200Response';
import GetUsers200Response from '../model/GetUsers200Response';
import GrantsResponse from '../model/GrantsResponse';
import Invoice from '../model/Invoice';
import Login from '../model/Login';
import OAuthClient from '../model/OAuthClient';
import PayPal from '../model/PayPal';
import PayPalExecute from '../model/PayPalExecute';
import Payment from '../model/Payment';
import PaymentMethod from '../model/PaymentMethod';
import PaymentRequest from '../model/PaymentRequest';
import Promotion from '../model/Promotion';
import ServiceTransfer from '../model/ServiceTransfer';
import Transfer from '../model/Transfer';
import User from '../model/User';

/**
* Account service.
* @module api/AccountApi
* @version 4.151.1
*/
export default class AccountApi {

    /**
    * Constructs a new AccountApi. 
    * @alias module:api/AccountApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the acceptEntityTransfer operation.
     * @callback module:api/AccountApi~acceptEntityTransferCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Entity Transfer Accept
     * **DEPRECATED**. Please use [Service Transfer Accept](/docs/api/account/#service-transfer-accept). 
     * @param {String} token The UUID of the Entity Transfer.
     * @param {module:api/AccountApi~acceptEntityTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    acceptEntityTransfer(token, callback) {
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling acceptEntityTransfer");
      }

      let pathParams = {
        'token': token
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
        '/account/entity-transfers/{token}/accept', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the acceptServiceTransfer operation.
     * @callback module:api/AccountApi~acceptServiceTransferCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Service Transfer Accept
     * Accept a Service Transfer for the provided token to receive the services included in the transfer to your account. At this time, only Linodes can be transferred.  When accepted, email confirmations are sent to the accounts that created and accepted the transfer. A transfer can take up to three hours to complete once accepted. Once a transfer is completed, billing for transferred services ends for the sending account and begins for the receiving account.  This command can only be accessed by the unrestricted users of the account that receives the transfer. Users of the same account that created a transfer cannot accept the transfer.  There are several conditions that must be met in order to accept a transfer request:  1. Only transfers with a `pending` status can be accepted.  1. The account accepting the transfer must have a registered payment method and must not have a past due   balance or other account limitations for the services to be transferred.  1. Both the account that created the transfer and the account that is accepting the transfer must not have any active Terms of Service violations.  1. The service must still be owned by the account that created the transfer.  1. Linodes must not:      * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.      * have any attached Block Storage Volumes.      * have any shared IP addresses.      * have any assigned /56, /64, or /116 IPv6 ranges.  Any and all of the above conditions must be cured and maintained by the relevant account prior to the transfer's expiration to allow the transfer to be accepted by the receiving account. 
     * @param {String} token The UUID of the Service Transfer.
     * @param {module:api/AccountApi~acceptServiceTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    acceptServiceTransfer(token, callback) {
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling acceptServiceTransfer");
      }

      let pathParams = {
        'token': token
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
        '/account/service-transfers/{token}/accept', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cancelAccount operation.
     * @callback module:api/AccountApi~cancelAccountCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CancelAccount200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Account Cancel
     * Cancels an active Linode account. This action will cause Linode to attempt to charge the credit card on file for the remaining balance. An error will occur if Linode fails to charge the credit card on file. Restricted users will not be able to cancel an account. 
     * @param {module:model/CancelAccountRequest} cancelAccountRequest Supply a comment stating the reason that you are cancelling your account. 
     * @param {module:api/AccountApi~cancelAccountCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CancelAccount200Response}
     */
    cancelAccount(cancelAccountRequest, callback) {
      let postBody = cancelAccountRequest;
      // verify the required parameter 'cancelAccountRequest' is set
      if (cancelAccountRequest === undefined || cancelAccountRequest === null) {
        throw new Error("Missing the required parameter 'cancelAccountRequest' when calling cancelAccount");
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
      let returnType = CancelAccount200Response;
      return this.apiClient.callApi(
        '/account/cancel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createClient operation.
     * @callback module:api/AccountApi~createClientCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OAuthClient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client Create
     * Creates an OAuth Client, which can be used to allow users (using their Linode account) to log in to your own application, and optionally grant your application some amount of access to their Linodes or other entities. 
     * @param {Object} opts Optional parameters
     * @param {module:model/OAuthClient} [oAuthClient] Information about the OAuth Client to create.
     * @param {module:api/AccountApi~createClientCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OAuthClient}
     */
    createClient(opts, callback) {
      opts = opts || {};
      let postBody = opts['oAuthClient'];

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
      let returnType = OAuthClient;
      return this.apiClient.callApi(
        '/account/oauth-clients', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createCreditCard operation.
     * @callback module:api/AccountApi~createCreditCardCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Credit Card Add/Edit
     * **DEPRECATED**. Please use Payment Method Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)).  Adds a credit card Payment Method to your account and sets it as the default method. 
     * @param {module:model/CreditCard} creditCard Update the credit card information associated with your Account.
     * @param {module:api/AccountApi~createCreditCardCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createCreditCard(creditCard, callback) {
      let postBody = creditCard;
      // verify the required parameter 'creditCard' is set
      if (creditCard === undefined || creditCard === null) {
        throw new Error("Missing the required parameter 'creditCard' when calling createCreditCard");
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
        '/account/credit-card', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createEntityTransfer operation.
     * @callback module:api/AccountApi~createEntityTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EntityTransfer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Entity Transfer Create
     * **DEPRECATED**. Please use [Service Transfer Create](/docs/api/account/#service-transfer-create). 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateEntityTransferRequest} [createEntityTransferRequest] The entities to include in this transfer request.
     * @param {module:api/AccountApi~createEntityTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EntityTransfer}
     */
    createEntityTransfer(opts, callback) {
      opts = opts || {};
      let postBody = opts['createEntityTransferRequest'];

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
      let returnType = EntityTransfer;
      return this.apiClient.callApi(
        '/account/entity-transfers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPayPalPayment operation.
     * @callback module:api/AccountApi~createPayPalPaymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreatePayPalPayment200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * PayPal Payment Stage
     * **Note**: This endpoint is disabled and no longer accessible. PayPal can be designated as a Payment Method for automated payments using the Cloud Manager. See [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/). 
     * @param {module:model/PayPal} payPal The amount of the Payment to submit via PayPal. 
     * @param {module:api/AccountApi~createPayPalPaymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreatePayPalPayment200Response}
     */
    createPayPalPayment(payPal, callback) {
      let postBody = payPal;
      // verify the required parameter 'payPal' is set
      if (payPal === undefined || payPal === null) {
        throw new Error("Missing the required parameter 'payPal' when calling createPayPalPayment");
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
      let returnType = CreatePayPalPayment200Response;
      return this.apiClient.callApi(
        '/account/payments/paypal', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPayment operation.
     * @callback module:api/AccountApi~createPaymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Payment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment Make
     * Makes a Payment to your Account.  * The requested amount is charged to the default Payment Method if no `payment_method_id` is specified.  * A `payment_submitted` event is generated when a payment is successfully submitted. 
     * @param {module:model/PaymentRequest} paymentRequest Information about the Payment you are making.
     * @param {module:api/AccountApi~createPaymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Payment}
     */
    createPayment(paymentRequest, callback) {
      let postBody = paymentRequest;
      // verify the required parameter 'paymentRequest' is set
      if (paymentRequest === undefined || paymentRequest === null) {
        throw new Error("Missing the required parameter 'paymentRequest' when calling createPayment");
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
      let returnType = Payment;
      return this.apiClient.callApi(
        '/account/payments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createPaymentMethod operation.
     * @callback module:api/AccountApi~createPaymentMethodCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment Method Add
     * Adds a Payment Method to your Account with the option to set it as the default method.  * Adding a default Payment Method removes the default status from any other Payment Method.  * An Account can have up to 6 active Payment Methods.  * Up to 60 Payment Methods can be added each day.  * Prior to adding a Payment Method, ensure that your billing address information is up-to-date with a valid `zip` by using the Account Update ([PUT /account](/docs/api/account/#account-update)) endpoint.  * A `payment_method_add` event is generated when a payment is successfully submitted. 
     * @param {module:model/CreatePaymentMethodRequest} createPaymentMethodRequest The details of the Payment Method to add.
     * @param {module:api/AccountApi~createPaymentMethodCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createPaymentMethod(createPaymentMethodRequest, opts, callback) {
      opts = opts || {};
      let postBody = createPaymentMethodRequest;
      // verify the required parameter 'createPaymentMethodRequest' is set
      if (createPaymentMethodRequest === undefined || createPaymentMethodRequest === null) {
        throw new Error("Missing the required parameter 'createPaymentMethodRequest' when calling createPaymentMethod");
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
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/account/payment-methods', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the createPromoCredit operation.
     * @callback module:api/AccountApi~createPromoCreditCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Promotion} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Promo Credit Add
     * Adds an expiring Promo Credit to your account.  The following restrictions apply:  * Your account must be less than 90 days old. * There must not be an existing Promo Credit already on your account. * The requesting User must be unrestricted. Use the User Update   ([PUT /account/users/{username}](/docs/api/account/#user-update)) to change a User's restricted status. * The `promo_code` must be valid and unexpired. 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreatePromoCreditRequest} [createPromoCreditRequest] Enter a Promo Code to add its associated credit to your Account.
     * @param {module:api/AccountApi~createPromoCreditCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Promotion}
     */
    createPromoCredit(opts, callback) {
      opts = opts || {};
      let postBody = opts['createPromoCreditRequest'];

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
      let returnType = Promotion;
      return this.apiClient.callApi(
        '/account/promo-codes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createServiceTransfer operation.
     * @callback module:api/AccountApi~createServiceTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceTransfer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Service Transfer Create
     * Creates a transfer request for the specified services. A request can contain any of the specified service types and any number of each service type. At this time, only Linodes can be transferred.  When created successfully, a confirmation email is sent to the account that created this transfer containing a transfer token and instructions on completing the transfer.  When a transfer is [accepted](/docs/api/account/#service-transfer-accept), the requested services are moved to the receiving account. Linode services will not experience interruptions due to the transfer process. Backups for Linodes are transferred as well.  DNS records that are associated with requested services will not be transferred or updated. Please ensure that associated DNS records have been updated or communicated to the recipient prior to the transfer.  A transfer can take up to three hours to complete once accepted. When a transfer is completed, billing for transferred services ends for the sending account and begins for the receiving account.  This command can only be accessed by the unrestricted users of an account.  There are several conditions that must be met in order to successfully create a transfer request:  1. The account creating the transfer must not have a past due balance or active Terms of Service violation.  1. The service must be owned by the account that is creating the transfer.  1. The service must not be assigned to another Service Transfer that is pending or that has been accepted and is incomplete.  1. Linodes must not:      * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.      * have any attached Block Storage Volumes.      * have any shared IP addresses.      * have any assigned /56, /64, or /116 IPv6 ranges. 
     * @param {Object} opts Optional parameters
     * @param {module:model/CreateServiceTransferRequest} [createServiceTransferRequest] The services to include in this transfer request.
     * @param {module:api/AccountApi~createServiceTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceTransfer}
     */
    createServiceTransfer(opts, callback) {
      opts = opts || {};
      let postBody = opts['createServiceTransferRequest'];

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
      let returnType = ServiceTransfer;
      return this.apiClient.callApi(
        '/account/service-transfers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createUser operation.
     * @callback module:api/AccountApi~createUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User Create
     * Creates a User on your Account. Once created, a confirmation message containing password creation and login instructions is sent to the User's email address.  This command can only be accessed by the unrestricted users of an account.  The User's account access is determined by whether or not they are restricted, and what grants they have been given. 
     * @param {Object} opts Optional parameters
     * @param {module:model/User} [user] Information about the User to create.
     * @param {module:api/AccountApi~createUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    createUser(opts, callback) {
      opts = opts || {};
      let postBody = opts['user'];

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
      let returnType = User;
      return this.apiClient.callApi(
        '/account/users', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteClient operation.
     * @callback module:api/AccountApi~deleteClientCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client Delete
     * Deletes an OAuth Client registered with Linode. The Client ID and Client secret will no longer be accepted by <a target=\"_top\" href=\"https://login.linode.com\">https://login.linode.com</a>, and all tokens issued to this client will be invalidated (meaning that if your application was using a token, it will no longer work). 
     * @param {String} clientId The OAuth Client ID to look up.
     * @param {module:api/AccountApi~deleteClientCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteClient(clientId, callback) {
      let postBody = null;
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling deleteClient");
      }

      let pathParams = {
        'clientId': clientId
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
        '/account/oauth-clients/{clientId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteEntityTransfer operation.
     * @callback module:api/AccountApi~deleteEntityTransferCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Entity Transfer Cancel
     * **DEPRECATED**. Please use [Service Transfer Cancel](/docs/api/account/#service-transfer-cancel). 
     * @param {String} token The UUID of the Entity Transfer.
     * @param {module:api/AccountApi~deleteEntityTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteEntityTransfer(token, callback) {
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling deleteEntityTransfer");
      }

      let pathParams = {
        'token': token
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
        '/account/entity-transfers/{token}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePaymentMethod operation.
     * @callback module:api/AccountApi~deletePaymentMethodCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment Method Delete
     * Deactivate the specified Payment Method.  The default Payment Method can not be deleted. To add a new default Payment Method, access the Payment Method Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)) endpoint. To designate an existing Payment Method as the default method, access the Payment Method Make Default ([POST /account/payment-methods/{paymentMethodId}/make-default](/docs/api/account/#payment-method-make-default)) endpoint. 
     * @param {Number} paymentMethodId The ID of the Payment Method to look up.
     * @param {module:api/AccountApi~deletePaymentMethodCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deletePaymentMethod(paymentMethodId, callback) {
      let postBody = null;
      // verify the required parameter 'paymentMethodId' is set
      if (paymentMethodId === undefined || paymentMethodId === null) {
        throw new Error("Missing the required parameter 'paymentMethodId' when calling deletePaymentMethod");
      }

      let pathParams = {
        'paymentMethodId': paymentMethodId
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
        '/account/payment-methods/{paymentMethodId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteServiceTransfer operation.
     * @callback module:api/AccountApi~deleteServiceTransferCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Service Transfer Cancel
     * Cancels the Service Transfer for the provided token. Once cancelled, a transfer cannot be accepted or otherwise acted on in any way. If cancelled in error, the transfer must be [created](/docs/api/account/#service-transfer-create) again.  When cancelled, an email notification for the cancellation is sent to the account that created this transfer. Transfers can not be cancelled if they are expired or have been accepted.  This command can only be accessed by the unrestricted users of the account that created this transfer. 
     * @param {String} token The UUID of the Service Transfer.
     * @param {module:api/AccountApi~deleteServiceTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteServiceTransfer(token, callback) {
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling deleteServiceTransfer");
      }

      let pathParams = {
        'token': token
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
        '/account/service-transfers/{token}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteUser operation.
     * @callback module:api/AccountApi~deleteUserCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User Delete
     * Deletes a User. The deleted User will be immediately logged out and may no longer log in or perform any actions. All of the User's Grants will be removed.  This command can only be accessed by the unrestricted users of an account. 
     * @param {String} username The username to look up.
     * @param {module:api/AccountApi~deleteUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteUser(username, callback) {
      let postBody = null;
      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling deleteUser");
      }

      let pathParams = {
        'username': username
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
        '/account/users/{username}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the enableAccountManaged operation.
     * @callback module:api/AccountApi~enableAccountManagedCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linode Managed Enable
     * Enables Linode Managed for the entire account and sends a welcome email to the account's associated email address. Linode Managed can monitor any service or software stack reachable over TCP or HTTP. See our [Linode Managed guide](/docs/guides/linode-managed/) to learn more. 
     * @param {module:api/AccountApi~enableAccountManagedCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    enableAccountManaged(callback) {
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
        '/account/settings/managed-enable', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventRead operation.
     * @callback module:api/AccountApi~eventReadCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event Mark as Read
     * Marks a single Event as read.
     * @param {Number} eventId The ID of the Event to designate as read.
     * @param {module:api/AccountApi~eventReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    eventRead(eventId, callback) {
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling eventRead");
      }

      let pathParams = {
        'eventId': eventId
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
        '/account/events/{eventId}/read', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventSeen operation.
     * @callback module:api/AccountApi~eventSeenCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event Mark as Seen
     * Marks all Events up to and including this Event by ID as seen. 
     * @param {Number} eventId The ID of the Event to designate as seen.
     * @param {module:api/AccountApi~eventSeenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    eventSeen(eventId, callback) {
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling eventSeen");
      }

      let pathParams = {
        'eventId': eventId
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
        '/account/events/{eventId}/seen', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the executePayPalPayment operation.
     * @callback module:api/AccountApi~executePayPalPaymentCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Staged/Approved PayPal Payment Execute
     * **Note**: This endpoint is disabled and no longer accessible. PayPal can be designated as a Payment Method for automated payments using the Cloud Manager. See [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/). 
     * @param {module:model/PayPalExecute} payPalExecute The details of the Payment to execute. 
     * @param {module:api/AccountApi~executePayPalPaymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    executePayPalPayment(payPalExecute, callback) {
      let postBody = payPalExecute;
      // verify the required parameter 'payPalExecute' is set
      if (payPalExecute === undefined || payPalExecute === null) {
        throw new Error("Missing the required parameter 'payPalExecute' when calling executePayPalPayment");
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
        '/account/payments/paypal/execute', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccount operation.
     * @callback module:api/AccountApi~getAccountCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Account} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Account View
     * Returns the contact and billing information related to your Account. 
     * @param {module:api/AccountApi~getAccountCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Account}
     */
    getAccount(callback) {
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
      let returnType = Account;
      return this.apiClient.callApi(
        '/account', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccountLogin operation.
     * @callback module:api/AccountApi~getAccountLoginCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Login} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Login View
     * Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account. 
     * @param {Number} loginId The ID of the login object to access.
     * @param {module:api/AccountApi~getAccountLoginCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Login}
     */
    getAccountLogin(loginId, callback) {
      let postBody = null;
      // verify the required parameter 'loginId' is set
      if (loginId === undefined || loginId === null) {
        throw new Error("Missing the required parameter 'loginId' when calling getAccountLogin");
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
        '/account/logins/{loginId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccountLogins operation.
     * @callback module:api/AccountApi~getAccountLoginsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetAccountLogins200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User Logins List All
     * Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account. 
     * @param {module:api/AccountApi~getAccountLoginsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetAccountLogins200Response}
     */
    getAccountLogins(callback) {
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
        '/account/logins', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAccountSettings operation.
     * @callback module:api/AccountApi~getAccountSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AccountSettings} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Account Settings View
     * Returns information related to your Account settings: Managed service subscription, Longview subscription, and network helper. 
     * @param {module:api/AccountApi~getAccountSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AccountSettings}
     */
    getAccountSettings(callback) {
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
      let returnType = AccountSettings;
      return this.apiClient.callApi(
        '/account/settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getClient operation.
     * @callback module:api/AccountApi~getClientCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OAuthClient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client View
     * Returns information about a single OAuth client. 
     * @param {String} clientId The OAuth Client ID to look up.
     * @param {module:api/AccountApi~getClientCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OAuthClient}
     */
    getClient(clientId, callback) {
      let postBody = null;
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling getClient");
      }

      let pathParams = {
        'clientId': clientId
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
      let returnType = OAuthClient;
      return this.apiClient.callApi(
        '/account/oauth-clients/{clientId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getClientThumbnail operation.
     * @callback module:api/AccountApi~getClientThumbnailCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client Thumbnail View
     * Returns the thumbnail for this OAuth Client.  This is a publicly-viewable endpoint, and can be accessed without authentication. 
     * @param {String} clientId The OAuth Client ID to look up.
     * @param {module:api/AccountApi~getClientThumbnailCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    getClientThumbnail(clientId, callback) {
      let postBody = null;
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling getClientThumbnail");
      }

      let pathParams = {
        'clientId': clientId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['image/png', 'application/json'];
      let returnType = File;
      return this.apiClient.callApi(
        '/account/oauth-clients/{clientId}/thumbnail', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getClients operation.
     * @callback module:api/AccountApi~getClientsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetClients200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Clients List
     * Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getClientsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetClients200Response}
     */
    getClients(opts, callback) {
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
      let returnType = GetClients200Response;
      return this.apiClient.callApi(
        '/account/oauth-clients', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEntityTransfer operation.
     * @callback module:api/AccountApi~getEntityTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EntityTransfer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Entity Transfer View
     * **DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view). 
     * @param {String} token The UUID of the Entity Transfer.
     * @param {module:api/AccountApi~getEntityTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EntityTransfer}
     */
    getEntityTransfer(token, callback) {
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling getEntityTransfer");
      }

      let pathParams = {
        'token': token
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
      let returnType = EntityTransfer;
      return this.apiClient.callApi(
        '/account/entity-transfers/{token}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEntityTransfers operation.
     * @callback module:api/AccountApi~getEntityTransfersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEntityTransfers200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Entity Transfers List
     * **DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list). 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getEntityTransfersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEntityTransfers200Response}
     */
    getEntityTransfers(opts, callback) {
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
      let returnType = GetEntityTransfers200Response;
      return this.apiClient.callApi(
        '/account/entity-transfers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEvent operation.
     * @callback module:api/AccountApi~getEventCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Event} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event View
     * Returns a single Event object. 
     * @param {Number} eventId The ID of the Event.
     * @param {module:api/AccountApi~getEventCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Event}
     */
    getEvent(eventId, callback) {
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling getEvent");
      }

      let pathParams = {
        'eventId': eventId
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
      let returnType = Event;
      return this.apiClient.callApi(
        '/account/events/{eventId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getEvents operation.
     * @callback module:api/AccountApi~getEventsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetEvents200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Events List
     * Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getEventsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetEvents200Response}
     */
    getEvents(opts, callback) {
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
      let returnType = GetEvents200Response;
      return this.apiClient.callApi(
        '/account/events', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoice operation.
     * @callback module:api/AccountApi~getInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Invoice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Invoice View
     * Returns a single Invoice object.
     * @param {Number} invoiceId The ID of the Invoice.
     * @param {module:api/AccountApi~getInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Invoice}
     */
    getInvoice(invoiceId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling getInvoice");
      }

      let pathParams = {
        'invoiceId': invoiceId
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
      let returnType = Invoice;
      return this.apiClient.callApi(
        '/account/invoices/{invoiceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoiceItems operation.
     * @callback module:api/AccountApi~getInvoiceItemsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetInvoiceItems200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Invoice Items List
     * Returns a paginated list of Invoice items.
     * @param {Number} invoiceId The ID of the Invoice.
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getInvoiceItemsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetInvoiceItems200Response}
     */
    getInvoiceItems(invoiceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling getInvoiceItems");
      }

      let pathParams = {
        'invoiceId': invoiceId
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
      let returnType = GetInvoiceItems200Response;
      return this.apiClient.callApi(
        '/account/invoices/{invoiceId}/items', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvoices operation.
     * @callback module:api/AccountApi~getInvoicesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetInvoices200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Invoices List
     * Returns a paginated list of Invoices against your Account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getInvoicesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetInvoices200Response}
     */
    getInvoices(opts, callback) {
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
      let returnType = GetInvoices200Response;
      return this.apiClient.callApi(
        '/account/invoices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMaintenance operation.
     * @callback module:api/AccountApi~getMaintenanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetMaintenance200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Maintenance List
     * Returns a collection of Maintenance objects for any entity a user has permissions to view. Cancelled Maintenance objects are not returned.  Currently, Linodes are the only entities available for viewing. 
     * @param {module:api/AccountApi~getMaintenanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetMaintenance200Response}
     */
    getMaintenance(opts, callback) {
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
      let returnType = GetMaintenance200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/account/maintenance', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getNotifications operation.
     * @callback module:api/AccountApi~getNotificationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNotifications200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Notifications List
     * Returns a collection of Notification objects representing important, often time-sensitive items related to your Account. You cannot interact directly with Notifications, and a Notification will disappear when the circumstances causing it have been resolved. For example, if you have an important Ticket open, you must respond to the Ticket to dismiss the Notification. 
     * @param {module:api/AccountApi~getNotificationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNotifications200Response}
     */
    getNotifications(callback) {
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
      let returnType = GetNotifications200Response;
      return this.apiClient.callApi(
        '/account/notifications', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPayment operation.
     * @callback module:api/AccountApi~getPaymentCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Payment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment View
     * Returns information about a specific Payment. 
     * @param {Number} paymentId The ID of the Payment to look up.
     * @param {module:api/AccountApi~getPaymentCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Payment}
     */
    getPayment(paymentId, callback) {
      let postBody = null;
      // verify the required parameter 'paymentId' is set
      if (paymentId === undefined || paymentId === null) {
        throw new Error("Missing the required parameter 'paymentId' when calling getPayment");
      }

      let pathParams = {
        'paymentId': paymentId
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
      let returnType = Payment;
      return this.apiClient.callApi(
        '/account/payments/{paymentId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPaymentMethod operation.
     * @callback module:api/AccountApi~getPaymentMethodCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaymentMethod} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment Method View
     * View the details of the specified Payment Method. 
     * @param {Number} paymentMethodId The ID of the Payment Method to look up.
     * @param {module:api/AccountApi~getPaymentMethodCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaymentMethod}
     */
    getPaymentMethod(paymentMethodId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'paymentMethodId' is set
      if (paymentMethodId === undefined || paymentMethodId === null) {
        throw new Error("Missing the required parameter 'paymentMethodId' when calling getPaymentMethod");
      }

      let pathParams = {
        'paymentMethodId': paymentMethodId
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
      let returnType = PaymentMethod;
      let basePaths = ['https://api.linode.com/v4'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/account/payment-methods/{paymentMethodId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getPaymentMethods operation.
     * @callback module:api/AccountApi~getPaymentMethodsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPaymentMethods200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment Methods List
     * Returns a paginated list of Payment Methods for this Account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getPaymentMethodsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPaymentMethods200Response}
     */
    getPaymentMethods(opts, callback) {
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
      let returnType = GetPaymentMethods200Response;
      let basePaths = ['https://api.linode.com/v4', 'https://api.linode.com/v4beta'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/account/payment-methods', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the getPayments operation.
     * @callback module:api/AccountApi~getPaymentsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPayments200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payments List
     * Returns a paginated list of Payments made on this Account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getPaymentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPayments200Response}
     */
    getPayments(opts, callback) {
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
      let returnType = GetPayments200Response;
      return this.apiClient.callApi(
        '/account/payments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceTransfer operation.
     * @callback module:api/AccountApi~getServiceTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceTransfer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Service Transfer View
     * Returns the details of the Service Transfer for the provided token.  While a transfer is pending, any unrestricted user *of any account* can access this command. After a transfer has been accepted, it can only be viewed by unrestricted users of the accounts that created and accepted the transfer. If cancelled or expired, only unrestricted users of the account that created the transfer can view it. 
     * @param {String} token The UUID of the Service Transfer.
     * @param {module:api/AccountApi~getServiceTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceTransfer}
     */
    getServiceTransfer(token, callback) {
      let postBody = null;
      // verify the required parameter 'token' is set
      if (token === undefined || token === null) {
        throw new Error("Missing the required parameter 'token' when calling getServiceTransfer");
      }

      let pathParams = {
        'token': token
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
      let returnType = ServiceTransfer;
      return this.apiClient.callApi(
        '/account/service-transfers/{token}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceTransfers operation.
     * @callback module:api/AccountApi~getServiceTransfersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetServiceTransfers200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Service Transfers List
     * Returns a collection of all created and accepted Service Transfers for this account, regardless of the user that created or accepted the transfer.  This command can only be accessed by the unrestricted users of an account. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getServiceTransfersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetServiceTransfers200Response}
     */
    getServiceTransfers(opts, callback) {
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
      let returnType = GetServiceTransfers200Response;
      return this.apiClient.callApi(
        '/account/service-transfers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTransfer operation.
     * @callback module:api/AccountApi~getTransferCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Transfer} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Network Utilization View
     * Returns a Transfer object showing your network utilization, in GB, for the current month. 
     * @param {module:api/AccountApi~getTransferCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Transfer}
     */
    getTransfer(callback) {
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
      let returnType = Transfer;
      return this.apiClient.callApi(
        '/account/transfer', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUser operation.
     * @callback module:api/AccountApi~getUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User View
     * Returns information about a single User on your Account.  This command can only be accessed by the unrestricted users of an account. 
     * @param {String} username The username to look up.
     * @param {module:api/AccountApi~getUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    getUser(username, callback) {
      let postBody = null;
      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling getUser");
      }

      let pathParams = {
        'username': username
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
      let returnType = User;
      return this.apiClient.callApi(
        '/account/users/{username}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUserGrants operation.
     * @callback module:api/AccountApi~getUserGrantsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GrantsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User's Grants View
     * Returns the full grants structure for the specified account User (other than the account owner, see below for details). This includes all entities on the Account alongside the level of access this User has to each of them.  This command can only be accessed by the unrestricted users of an account.  The current authenticated User, including the account owner, may view their own grants at the [/profile/grants](/docs/api/profile/#grants-list) endpoint, but will not see entities that they do not have access to. 
     * @param {String} username The username to look up.
     * @param {module:api/AccountApi~getUserGrantsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GrantsResponse}
     */
    getUserGrants(username, callback) {
      let postBody = null;
      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling getUserGrants");
      }

      let pathParams = {
        'username': username
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
        '/account/users/{username}/grants', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUsers operation.
     * @callback module:api/AccountApi~getUsersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetUsers200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Users List
     * Returns a paginated list of Users on your Account.  This command can only be accessed by the unrestricted users of an account.  Users may access all or part of your Account based on their restricted status and grants.  An unrestricted User may access everything on the account, whereas restricted User may only access entities or perform actions they've been given specific grants to. 
     * @param {Object} opts Optional parameters
     * @param {Number} [page = 1)] The page of a collection to return.
     * @param {Number} [pageSize = 100)] The number of items to return per page.
     * @param {module:api/AccountApi~getUsersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetUsers200Response}
     */
    getUsers(opts, callback) {
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
      let returnType = GetUsers200Response;
      return this.apiClient.callApi(
        '/account/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the makePaymentMethodDefault operation.
     * @callback module:api/AccountApi~makePaymentMethodDefaultCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Payment Method Make Default
     * Make the specified Payment Method the default method for automatically processing payments.  Removes the default status from any other Payment Method. 
     * @param {Number} paymentMethodId The ID of the Payment Method to make default.
     * @param {module:api/AccountApi~makePaymentMethodDefaultCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    makePaymentMethodDefault(paymentMethodId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'paymentMethodId' is set
      if (paymentMethodId === undefined || paymentMethodId === null) {
        throw new Error("Missing the required parameter 'paymentMethodId' when calling makePaymentMethodDefault");
      }

      let pathParams = {
        'paymentMethodId': paymentMethodId
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
        '/account/payment-methods/{paymentMethodId}/make-default', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }

    /**
     * Callback function to receive the result of the resetClientSecret operation.
     * @callback module:api/AccountApi~resetClientSecretCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OAuthClient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client Secret Reset
     * Resets the OAuth Client secret for a client you own, and returns the OAuth Client with the plaintext secret. This secret is not supposed to be publicly known or disclosed anywhere. This can be used to generate a new secret in case the one you have has been leaked, or to get a new secret if you lost the original. The old secret is expired immediately, and logins to your client with the old secret will fail. 
     * @param {String} clientId The OAuth Client ID to look up.
     * @param {module:api/AccountApi~resetClientSecretCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OAuthClient}
     */
    resetClientSecret(clientId, callback) {
      let postBody = null;
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling resetClientSecret");
      }

      let pathParams = {
        'clientId': clientId
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
      let returnType = OAuthClient;
      return this.apiClient.callApi(
        '/account/oauth-clients/{clientId}/reset-secret', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setClientThumbnail operation.
     * @callback module:api/AccountApi~setClientThumbnailCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client Thumbnail Update
     * Upload a thumbnail for a client you own.  You must upload an image file that will be returned when the thumbnail is retrieved.  This image will be publicly-viewable. 
     * @param {String} clientId The OAuth Client ID to look up.
     * @param {File} body The image to set as the thumbnail.
     * @param {module:api/AccountApi~setClientThumbnailCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    setClientThumbnail(clientId, body, callback) {
      let postBody = body;
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling setClientThumbnail");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling setClientThumbnail");
      }

      let pathParams = {
        'clientId': clientId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['personalAccessToken', 'oauth'];
      let contentTypes = ['image/png'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/account/oauth-clients/{clientId}/thumbnail', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateAccount operation.
     * @callback module:api/AccountApi~updateAccountCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Account} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Account Update
     * Updates contact and billing information related to your Account. 
     * @param {module:model/Account} account Update contact and billing information.  Account properties that are excluded from a request remain unchanged.  When updating an Account's `country` to \"US\", an error is returned if the Account's `zip` is not a valid US zip code. 
     * @param {module:api/AccountApi~updateAccountCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Account}
     */
    updateAccount(account, callback) {
      let postBody = account;
      // verify the required parameter 'account' is set
      if (account === undefined || account === null) {
        throw new Error("Missing the required parameter 'account' when calling updateAccount");
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
      let returnType = Account;
      return this.apiClient.callApi(
        '/account', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateAccountSettings operation.
     * @callback module:api/AccountApi~updateAccountSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AccountSettings} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Account Settings Update
     * Updates your Account settings.  To update your Longview subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update). 
     * @param {module:model/AccountSettings} accountSettings Update Account settings information.
     * @param {module:api/AccountApi~updateAccountSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AccountSettings}
     */
    updateAccountSettings(accountSettings, callback) {
      let postBody = accountSettings;
      // verify the required parameter 'accountSettings' is set
      if (accountSettings === undefined || accountSettings === null) {
        throw new Error("Missing the required parameter 'accountSettings' when calling updateAccountSettings");
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
      let returnType = AccountSettings;
      return this.apiClient.callApi(
        '/account/settings', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateClient operation.
     * @callback module:api/AccountApi~updateClientCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OAuthClient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * OAuth Client Update
     * Update information about an OAuth Client on your Account. This can be especially useful to update the `redirect_uri` of your client in the event that the callback url changed in your application. 
     * @param {String} clientId The OAuth Client ID to look up.
     * @param {Object} opts Optional parameters
     * @param {module:model/OAuthClient} [oAuthClient] The fields to update.
     * @param {module:api/AccountApi~updateClientCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OAuthClient}
     */
    updateClient(clientId, opts, callback) {
      opts = opts || {};
      let postBody = opts['oAuthClient'];
      // verify the required parameter 'clientId' is set
      if (clientId === undefined || clientId === null) {
        throw new Error("Missing the required parameter 'clientId' when calling updateClient");
      }

      let pathParams = {
        'clientId': clientId
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
      let returnType = OAuthClient;
      return this.apiClient.callApi(
        '/account/oauth-clients/{clientId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateUser operation.
     * @callback module:api/AccountApi~updateUserCallback
     * @param {String} error Error message, if any.
     * @param {module:model/User} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User Update
     * Update information about a User on your Account. This can be used to change the restricted status of a User. When making a User restricted, no grants will be configured by default and you must then set up grants in order for the User to access anything on the Account.  This command can only be accessed by the unrestricted users of an account. 
     * @param {String} username The username to look up.
     * @param {Object} opts Optional parameters
     * @param {module:model/User} [user] The information to update.
     * @param {module:api/AccountApi~updateUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/User}
     */
    updateUser(username, opts, callback) {
      opts = opts || {};
      let postBody = opts['user'];
      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling updateUser");
      }

      let pathParams = {
        'username': username
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
      let returnType = User;
      return this.apiClient.callApi(
        '/account/users/{username}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateUserGrants operation.
     * @callback module:api/AccountApi~updateUserGrantsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GrantsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User's Grants Update
     * Update the grants a User has. This can be used to give a User access to new entities or actions, or take access away.  You do not need to include the grant for every entity on the Account in this request; any that are not included will remain unchanged.  This command can only be accessed by the unrestricted users of an account. 
     * @param {String} username The username to look up.
     * @param {module:model/GrantsResponse} grantsResponse The grants to update. Omitted grants will be left unchanged.
     * @param {module:api/AccountApi~updateUserGrantsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GrantsResponse}
     */
    updateUserGrants(username, grantsResponse, callback) {
      let postBody = grantsResponse;
      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling updateUserGrants");
      }
      // verify the required parameter 'grantsResponse' is set
      if (grantsResponse === undefined || grantsResponse === null) {
        throw new Error("Missing the required parameter 'grantsResponse' when calling updateUserGrants");
      }

      let pathParams = {
        'username': username
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
      let returnType = GrantsResponse;
      return this.apiClient.callApi(
        '/account/users/{username}/grants', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
