/*
 * Linode API
 * ## Introduction The Linode API provides the ability to programmatically manage the full range of Linode products and services.  This reference is designed to assist application developers and system administrators.  Each endpoint includes descriptions, request syntax, and examples using standard HTTP requests. Response data is returned in JSON format.   This document was generated from our OpenAPI Specification.  See the <a target=\"_top\" href=\"https://www.openapis.org\">OpenAPI website</a> for more information.  <a target=\"_top\" href=\"/docs/api/openapi.yaml\">Download the Linode OpenAPI Specification</a>.   ## Changelog  <a target=\"_top\" href=\"/docs/products/tools/api/release-notes/\">View our Changelog</a> to see release notes on all changes made to our API.  ## Access and Authentication  Some endpoints are publicly accessible without requiring authentication. All endpoints affecting your Account, however, require either a Personal Access Token or OAuth authentication (when using third-party applications).  ### Personal Access Token  The easiest way to access the API is with a Personal Access Token (PAT) generated from the <a target=\"_top\" href=\"https://cloud.linode.com/profile/tokens\">Linode Cloud Manager</a> or the [Create Personal Access Token](/docs/api/profile/#personal-access-token-create) endpoint.  All scopes for the OAuth security model ([defined below](/docs/api/#oauth)) apply to this security model as well.  ### Authentication  | Security Scheme Type: | HTTP | |-----------------------|------| | **HTTP Authorization Scheme** | bearer |  ## OAuth  If you only need to access the Linode API for personal use, we recommend that you create a [personal access token](/docs/api/#personal-access-token). If you're designing an application that can authenticate with an arbitrary Linode user, then you should use the OAuth 2.0 workflows presented in this section.  For a more detailed example of an OAuth 2.0 implementation, see our guide on [How to Create an OAuth App with the Linode Python API Library](/docs/products/tools/api/guides/create-an-oauth-app-with-the-python-api-library/#oauth-2-authentication-exchange).  Before you implement OAuth in your application, you first need to create an OAuth client. You can do this [with the Linode API](/docs/api/account/#oauth-client-create) or [via the Cloud Manager](https://cloud.linode.com/profile/clients):    - When creating the client, you'll supply a `label` and a `redirect_uri` (referred to as the Callback URL in the Cloud Manager).   - The response from this endpoint will give you a `client_id` and a `secret`.   - Clients can be public or private, and are private by default. You can choose to make the client public when it is created.     - A private client is used with applications which can securely store the client secret (that is, the secret returned to you when you first created the client). For example, an application running on a secured server that only the developer has access to would use a private OAuth client. This is also called a confidential client in some OAuth documentation.     - A public client is used with applications where the client secret is not guaranteed to be secure. For example, a native app running on a user's computer may not be able to keep the client secret safe, as a user could potentially inspect the source of the application. So, native apps or apps that run in a user's browser should use a public client.     - Public and private clients follow different workflows, as described below.  ### OAuth Workflow  The OAuth workflow is a series of exchanges between your third-party app and Linode. The workflow is used to authenticate a user before an application can start making API calls on the user's behalf.  Notes:  - With respect to the diagram in [section 1.2 of RFC 6749](https://tools.ietf.org/html/rfc6749#section-1.2), login.linode.com (referred to in this section as the *login server*) is the Resource Owner and the Authorization Server; api.linode.com (referred to here as the *api server*) is the Resource Server. - The OAuth spec refers to the private and public workflows listed below as the [authorization code flow](https://tools.ietf.org/html/rfc6749#section-1.3.1) and [implicit flow](https://tools.ietf.org/html/rfc6749#section-1.3.2).  | PRIVATE WORKFLOW | PUBLIC WORKFLOW | |------------------|------------------| | 1.  The user visits the application's website and is directed to login with Linode. | 1.  The user visits the application's website and is directed to login with Linode. | | 2.  Your application then redirects the user to Linode's [login server](https://login.linode.com) with the client application's `client_id` and requested OAuth `scope`, which should appear in the URL of the login page. | 2.  Your application then redirects the user to Linode's [login server](https://login.linode.com) with the client application's `client_id` and requested OAuth `scope`, which should appear in the URL of the login page. | | 3.  The user logs into the login server with their username and password. | 3.  The user logs into the login server with their username and password. | | 4.  The login server redirects the user to the specificed redirect URL with a temporary authorization `code` (exchange code) in the URL. | 4.  The login server redirects the user back to your application with an OAuth `access_token` embedded in the redirect URL's hash. This is temporary and expires in two hours. No `refresh_token` is issued. Therefore, once the `access_token` expires, a new one will need to be issued by having the user log in again. | | 5.  The application issues a POST request (*see additional details below*) to the login server with the exchange code, `client_id`, and the client application's `client_secret`. | | | 6.  The login server responds to the client application with a new OAuth `access_token` and `refresh_token`. The `access_token` is set to expire in two hours. | | | 7.  The `refresh_token` can be used by contacting the login server with the `client_id`, `client_secret`, `grant_type`, and `refresh_token` to get a new OAuth `access_token` and `refresh_token`. The new `access_token` is good for another two hours, and the new `refresh_token` can be used to extend the session again by this same method (*see additional details below*). | |  #### OAuth Private Workflow - Additional Details  The following information expands on steps 5 through 7 of the private workflow:  Once the user has logged into Linode and you have received an exchange code, you will need to trade that exchange code for an `access_token` and `refresh_token`. You do this by making an HTTP POST request to the following address:  ``` https://login.linode.com/oauth/token ```  Make this request as `application/x-www-form-urlencoded` or as `multipart/form-data` and include the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | client_id | Your app's client ID. | | client_secret | Your app's client secret. | | code | The code you just received from the redirect. |  You'll get a response like this:  ```json {   \"scope\": \"linodes:read_write\",   \"access_token\": \"03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c\",   \"refresh_token\": \"f2ec9712e616fdb5a2a21aa0e88cfadea7502ebc62cf5bd758dbcd65e1803bad\",   \"token_type\": \"bearer\",   \"expires_in\": 7200 } ```  Included in the response is an `access_token`. With this token, you can proceed to make authenticated HTTP requests to the API by adding this header to each request:  ``` Authorization: Bearer 03d084436a6c91fbafd5c4b20c82e5056a2e9ce1635920c30dc8d81dc7a6665c ```  This `access_token` is set to expire in two hours. To refresh access prior to expiration, make another request to the same URL with the following parameters in the POST body:  | PARAMETER | DESCRIPTION | |-----------|-------------| | grant_type | The grant type you're using. Use \"refresh_token\" when refreshing access. | | client_id | Your app's client ID. | | client_secret | Your app's client secret. | | refresh_token | The `refresh_token` received from the previous response. |  You'll get another response with an updated `access_token` and `refresh_token`, which can then be used to refresh access again.  ### OAuth Reference  | Security Scheme Type | OAuth 2.0 | |-----------------------|--------| | **Authorization URL** | `https://login.linode.com/oauth/authorize` | | **Token URL** | `https://login.linode.com/oauth/token` | | **Scopes** | <ul><li>`account:read_only` - Allows access to GET information about your Account.</li><li>`account:read_write` - Allows access to all endpoints related to your Account.</li><li>`databases:read_only` - Allows access to GET Managed Databases on your Account.</li><li>`databases:read_write` - Allows access to all endpoints related to your Managed Databases.</li><li>`domains:read_only` - Allows access to GET Domains on your Account.</li><li>`domains:read_write` - Allows access to all Domain endpoints.</li><li>`events:read_only` - Allows access to GET your Events.</li><li>`events:read_write` - Allows access to all endpoints related to your Events.</li><li>`firewall:read_only` - Allows access to GET information about your Firewalls.</li><li>`firewall:read_write` - Allows access to all Firewall endpoints.</li><li>`images:read_only` - Allows access to GET your Images.</li><li>`images:read_write` - Allows access to all endpoints related to your Images.</li><li>`ips:read_only` - Allows access to GET your ips.</li><li>`ips:read_write` - Allows access to all endpoints related to your ips.</li><li>`linodes:read_only` - Allows access to GET Linodes on your Account.</li><li>`linodes:read_write` - Allow access to all endpoints related to your Linodes.</li><li>`lke:read_only` - Allows access to GET LKE Clusters on your Account.</li><li>`lke:read_write` - Allows access to all endpoints related to LKE Clusters on your Account.</li><li>`longview:read_only` - Allows access to GET your Longview Clients.</li><li>`longview:read_write` - Allows access to all endpoints related to your Longview Clients.</li><li>`nodebalancers:read_only` - Allows access to GET NodeBalancers on your Account.</li><li>`nodebalancers:read_write` - Allows access to all NodeBalancer endpoints.</li><li>`object_storage:read_only` - Allows access to GET information related to your Object Storage.</li><li>`object_storage:read_write` - Allows access to all Object Storage endpoints.</li><li>`stackscripts:read_only` - Allows access to GET your StackScripts.</li><li>`stackscripts:read_write` - Allows access to all endpoints related to your StackScripts.</li><li>`volumes:read_only` - Allows access to GET your Volumes.</li><li>`volumes:read_write` - Allows access to all endpoints related to your Volumes.</li></ul><br/>|  ## Requests  Requests must be made over HTTPS to ensure transactions are encrypted. Data included in requests must be supplied in json format unless otherwise specified in the command description.  The following request methods are supported:  | METHOD  | USAGE | |---------|-------| | GET     | Retrieves data about collections and individual resources. | | POST    | For collections, creates a new resource of that type. Also used to perform actions on action endpoints. | | PUT     | Updates an existing resource. | | DELETE  | Deletes a resource. This is a destructive action. | | HEAD    | Returns only the response header information of a GET request | | OPTIONS | Provides permitted communication options for a command |  ## Responses  ### Response Status Codes  Actions will return one of the following HTTP response status codes:  | STATUS  | DESCRIPTION | |---------|-------------| | 200 OK  | The request was successful. | | 202 Accepted | The request was successful, but processing has not been completed. The response body includes a \"warnings\" array containing the details of incomplete processes. | | 204 No Content | The server successfully fulfilled the request and there is no additional content to send. | | 299 Deprecated | The request was successful, but involved a deprecated endpoint. The response body includes a \"warnings\" array containing warning messages. | | 400 Bad Request | You submitted an invalid request (missing parameters, etc.). | | 401 Unauthorized | You failed to authenticate for this resource. | | 403 Forbidden | You are authenticated, but don't have permission to do this. | | 404 Not Found | The resource you're requesting does not exist. | | 429 Too Many Requests | You've hit a rate limit. | | 500 Internal Server Error | Please [open a Support Ticket](/docs/api/support/#support-ticket-open). |  ### Response Headers  There are many ways to access response header information for individual command URLs, depending on how you are accessing the Linode API. For example, to view HTTP response headers for the `/regions` endpoint when making requests with `curl`, use the `-I` or `--head` option as follows:  ```Shell curl -I https://api.linode.com/v4/regions ```  Responses may include the following headers:  | HEADER | DESCRIPTION | EXAMPLE | |--------|-------------|---------| | Access-Control-Allow-Credentials | Responses to credentialed requests are exposed to frontend JavaScript code. | true | | Access-Control-Allow-Headers | All permissible request headers for this endpoint. | Authorization, Origin, X-Requested-With, Content-Type, Accept, X-Filter | | Access-Control-Allow-Methods | Permissible HTTP methods for this endpoint | HEAD, GET, OPTIONS, POST, PUT, DELETE | | Access-Control-Allow-Origin | Indicates origin access permissions. The wildcard character `*` means any origin can access the resource. | * | | Access-Control-Expose-Headers | Available headers to include in response to cross-origin requests. | X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Status | | Cache-Control | Controls caching in browsers and shared caches such as CDNs. | private, max-age=60, s-maxage=60 | | Content-Security-Policy | Controls which resources are allowed to load. By default, resources do not load. | default-src 'none' | | Content-Type | All responses are in json format. | application/json | | Content-Warning | A message containing instructions for successful requests that were not able to be completed. | Please contact support for assistance. | | Retry-After | The remaining time in seconds until the current [rate limit](#rate-limiting) window resets. | 60 | | Strict-Transport-Security | Enforces HTTPS-only access until the returned time in seconds. | max-age=31536000 | | Vary | Optional request headers that affected the response content. | Authorization, X-Filter | | X-Accepted-OAuth-Scopes | Required [scopes](#oauth-reference) for accessing the requested command. | linodes:read_only | | X-Customer-UUID | A unique identifier for the account owning the the [personal access token](#personal-access-token) that was used for the request. | ABCDEF01-3456-789A-BCDEF0123456789A | | X-OAuth-Scopes | Allowed [scopes](#oauth-reference) associated with the [personal access token](#personal-access-token) that was used for the request. A value of `*` indicates read/write access for all scope categories. | images:read_write linodes:read_only | | X-RateLimit-Limit | The maximum number of permitted requests during the [rate limit](#rate-limiting) window for this endpoint. | 800 | | X-RateLimit-Remaining | The remaining number of permitted requests in the current [rate limit](#rate-limiting) window. | 798 | | X-RateLimit-Reset | The time when the current [rate limit](#rate-limiting) window rests in UTC epoch seconds. | 1674747739 | | X-Spec-Version | The current API version that handled the request. | 4.150.0 |  ## Errors  Success is indicated via <a href=\"https://en.wikipedia.org/wiki/List_of_HTTP_status_codes\" target=\"_top\">Standard HTTP status codes</a>. `2xx` codes indicate success, `4xx` codes indicate a request error, and `5xx` errors indicate a server error. A request error might be an invalid input, a required parameter being omitted, or a malformed request. A server error means something went wrong processing your request. If this occurs, please [open a Support Ticket](/docs/api/support/#support-ticket-open) and let us know. Though errors are logged and we work quickly to resolve issues, opening a ticket and providing us with reproducable steps and data is always helpful.  The `errors` field is an array of the things that went wrong with your request. We will try to include as many of the problems in the response as possible, but it's conceivable that fixing these errors and resubmitting may result in new errors coming back once we are able to get further along in the process of handling your request.  Within each error object, the `field` parameter will be included if the error pertains to a specific field in the JSON you've submitted. This will be omitted if there is no relevant field. The `reason` is a human-readable explanation of the error, and will always be included.  ## Pagination  Resource lists are always paginated. The response will look similar to this:  ```json {     \"data\": [ ... ],     \"page\": 1,     \"pages\": 3,     \"results\": 300 } ```  * Pages start at 1. You may retrieve a specific page of results by adding `?page=x` to your URL (for example, `?page=4`). If the value of `page` exceeds `2^64/page_size`, the last possible page will be returned.   * Page sizes default to 100, and can be set to return between 25 and 500. Page size can be set using `?page_size=x`.  ## Filtering and Sorting  Collections are searchable by fields they include, marked in the spec as `x-linode-filterable: true`. Filters are passed in the `X-Filter` header and are formatted as JSON objects. Here is a request call for Linode Types in our \"standard\" class:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"class\": \"standard\" }' ```  The filter object's keys are the keys of the object you're filtering, and the values are accepted values. You can add multiple filters by including more than one key. For example, filtering for \"standard\" Linode Types that offer one vcpu:  ```Shell  curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"class\": \"standard\", \"vcpus\": 1 }' ```  In the above example, both filters are combined with an \"and\" operation. However, if you wanted either Types with one vcpu or Types in our \"standard\" class, you can add an operator:   ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H 'X-Filter: { \"+or\": [ { \"vcpus\": 1 }, { \"class\": \"standard\" } ] }' ```  Each filter in the `+or` array is its own filter object, and all conditions in it are combined with an \"and\" operation as they were in the previous example.  Other operators are also available. Operators are keys of a Filter JSON object. Their value must be of the appropriate type, and they are evaluated as described below:  | OPERATOR | TYPE   | DESCRIPTION                       | |----------|--------|-----------------------------------| | +and     | array  | All conditions must be true.       | | +or      | array  | One condition must be true.        | | +gt      | number | Value must be greater than number. | | +gte     | number | Value must be greater than or equal to number. | | +lt      | number | Value must be less than number. | | +lte     | number | Value must be less than or equal to number. | | +contains | string | Given string must be in the value. | | +neq      | string | Does not equal the value.          | | +order_by | string | Attribute to order the results by - must be filterable. | | +order    | string | Either \"asc\" or \"desc\". Defaults to \"asc\". Requires `+order_by`. |  For example, filtering for [Linode Types](/docs/api/linode-types/) that offer memory equal to or higher than 61440:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H '     X-Filter: {       \"memory\": {         \"+gte\": 61440       }     }' ```  You can combine and nest operators to construct arbitrarily-complex queries. For example, give me all [Linode Types](/docs/api/linode-types/) which are either `standard` or `highmem` class, or have between 12 and 20 vcpus:  ```Shell curl \"https://api.linode.com/v4/linode/types\" \\   -H '     X-Filter: {       \"+or\": [         {           \"+or\": [             {               \"class\": \"standard\"             },             {               \"class\": \"highmem\"             }           ]         },         {           \"+and\": [             {               \"vcpus\": {                 \"+gte\": 12               }             },             {               \"vcpus\": {                 \"+lte\": 20               }             }           ]         }       ]     }' ``` ## Time Values  All times returned by the API are in UTC, regardless of the timezone configured within your user's profile (see `timezone` property within [Profile View](/docs/api/profile/#profile-view__responses)).  ## Rate Limiting  Rate limits on API requests help maintain the health and stability of the Linode API. Accordingly, every endpoint of the Linode API applies a rate limit on a per user basis as determined by OAuth token for authenticated requests or IP address for public endpoints.  Each rate limit consists of a total number of requests and a time window. For example, if an endpoint has a rate limit of 800 requests per minute, then up to 800 requests over a one minute window are permitted. Subsequent requests to an endpoint after hitting a rate limit return a 429 error. You can successfully remake requests to that endpoint after the rate limit window resets.  ### Linode APIv4 Rate Limits  With the Linode API, you can generally make up to 1,600 general API requests every two minutes. Additionally, all endpoints have a rate limit of 800 requests per minute unless otherwise specified below.  **Note:** There may be rate limiting applied at other levels outside of the API, for example, at the load balancer.  Creating Linodes has a dedicated rate limit of 10 requests per 30 seconds. That endpoint is:  * [Linode Create](/docs/api/linode-instances/#linode-create)  `/stats` endpoints have their own dedicated rate limits of 100 requests per minute. These endpoints are:  * [View Linode Statistics](/docs/api/linode-instances/#linode-statistics-view) * [View Linode Statistics (year/month)](/docs/api/linode-instances/#statistics-yearmonth-view) * [View NodeBalancer Statistics](/docs/api/nodebalancers/#nodebalancer-statistics-view) * [List Managed Stats](/docs/api/managed/#managed-stats-list)  Object Storage endpoints have a dedicated rate limit of 750 requests per second. The Object Storage endpoints are:  * [Object Storage Endpoints](/docs/api/object-storage/)  Opening Support Tickets has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Open Support Ticket](/docs/api/support/#support-ticket-open)  Accepting Service Transfers has a dedicated rate limit of 2 requests per minute. That endpoint is:  * [Service Transfer Accept](/docs/api/account/#service-transfer-accept)  ### Rate Limit HTTP Response Headers  The Linode API includes the following HTTP response headers which are designed to help you avoid hitting rate limits which might disrupt your applications:  * **X-RateLimit-Limit**: The maximum number of permitted requests during the rate limit window for this endpoint. * **X-RateLimit-Remaining**: The remaining number of permitted requests in the current rate limit window. * **X-RateLimit-Reset**: The time when the current rate limit window rests in UTC epoch seconds. * **Retry-After**: The remaining time in seconds until the current rate limit window resets.  ## CLI (Command Line Interface)  The <a href=\"https://github.com/linode/linode-cli\" target=\"_top\">Linode CLI</a> allows you to easily work with the API using intuitive and simple syntax. It requires a [Personal Access Token](/docs/api/#personal-access-token) for authentication, and gives you access to all of the features and functionality of the Linode API that are documented here with CLI examples.  Endpoints that do not have CLI examples are currently unavailable through the CLI, but can be accessed via other methods such as Shell commands and other third-party applications. 
 *
 * The version of the OpenAPI document: 4.151.1
 * Contact: support@linode.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Account;
import org.openapitools.client.model.AccountSettings;
import org.openapitools.client.model.CancelAccount200Response;
import org.openapitools.client.model.CancelAccount409Response;
import org.openapitools.client.model.CancelAccountRequest;
import org.openapitools.client.model.CreateEntityTransferRequest;
import org.openapitools.client.model.CreatePayPalPayment200Response;
import org.openapitools.client.model.CreatePayment202Response;
import org.openapitools.client.model.CreatePaymentMethodRequest;
import org.openapitools.client.model.CreatePromoCreditRequest;
import org.openapitools.client.model.CreateServiceTransferRequest;
import org.openapitools.client.model.CreditCard;
import org.openapitools.client.model.EntityTransfer;
import org.openapitools.client.model.Event;
import java.io.File;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetAccountLogins200Response;
import org.openapitools.client.model.GetClients200Response;
import org.openapitools.client.model.GetEntityTransfers200Response;
import org.openapitools.client.model.GetEvents200Response;
import org.openapitools.client.model.GetInvoiceItems200Response;
import org.openapitools.client.model.GetInvoices200Response;
import org.openapitools.client.model.GetMaintenance200Response;
import org.openapitools.client.model.GetNotifications200Response;
import org.openapitools.client.model.GetPaymentMethods200Response;
import org.openapitools.client.model.GetPayments200Response;
import org.openapitools.client.model.GetServiceTransfers200Response;
import org.openapitools.client.model.GetUsers200Response;
import org.openapitools.client.model.GrantsResponse;
import org.openapitools.client.model.Invoice;
import org.openapitools.client.model.Login;
import org.openapitools.client.model.OAuthClient;
import org.openapitools.client.model.PayPal;
import org.openapitools.client.model.PayPalExecute;
import org.openapitools.client.model.Payment;
import org.openapitools.client.model.PaymentMethod;
import org.openapitools.client.model.PaymentRequest;
import org.openapitools.client.model.Promotion;
import org.openapitools.client.model.ServiceTransfer;
import org.openapitools.client.model.Transfer;
import java.util.UUID;
import org.openapitools.client.model.User;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AccountApi
 */
@Disabled
public class AccountApiTest {

    private final AccountApi api = new AccountApi();

    /**
     * Entity Transfer Accept
     *
     * **DEPRECATED**. Please use [Service Transfer Accept](/docs/api/account/#service-transfer-accept). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void acceptEntityTransferTest() throws ApiException {
        UUID token = null;
        Object response = api.acceptEntityTransfer(token);
        // TODO: test validations
    }

    /**
     * Service Transfer Accept
     *
     * Accept a Service Transfer for the provided token to receive the services included in the transfer to your account. At this time, only Linodes can be transferred.  When accepted, email confirmations are sent to the accounts that created and accepted the transfer. A transfer can take up to three hours to complete once accepted. Once a transfer is completed, billing for transferred services ends for the sending account and begins for the receiving account.  This command can only be accessed by the unrestricted users of the account that receives the transfer. Users of the same account that created a transfer cannot accept the transfer.  There are several conditions that must be met in order to accept a transfer request:  1. Only transfers with a &#x60;pending&#x60; status can be accepted.  1. The account accepting the transfer must have a registered payment method and must not have a past due   balance or other account limitations for the services to be transferred.  1. Both the account that created the transfer and the account that is accepting the transfer must not have any active Terms of Service violations.  1. The service must still be owned by the account that created the transfer.  1. Linodes must not:      * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.      * have any attached Block Storage Volumes.      * have any shared IP addresses.      * have any assigned /56, /64, or /116 IPv6 ranges.  Any and all of the above conditions must be cured and maintained by the relevant account prior to the transfer&#39;s expiration to allow the transfer to be accepted by the receiving account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void acceptServiceTransferTest() throws ApiException {
        UUID token = null;
        Object response = api.acceptServiceTransfer(token);
        // TODO: test validations
    }

    /**
     * Account Cancel
     *
     * Cancels an active Linode account. This action will cause Linode to attempt to charge the credit card on file for the remaining balance. An error will occur if Linode fails to charge the credit card on file. Restricted users will not be able to cancel an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelAccountTest() throws ApiException {
        CancelAccountRequest cancelAccountRequest = null;
        CancelAccount200Response response = api.cancelAccount(cancelAccountRequest);
        // TODO: test validations
    }

    /**
     * OAuth Client Create
     *
     * Creates an OAuth Client, which can be used to allow users (using their Linode account) to log in to your own application, and optionally grant your application some amount of access to their Linodes or other entities. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createClientTest() throws ApiException {
        OAuthClient oauthClient = null;
        OAuthClient response = api.createClient(oauthClient);
        // TODO: test validations
    }

    /**
     * Credit Card Add/Edit
     *
     * **DEPRECATED**. Please use Payment Method Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)).  Adds a credit card Payment Method to your account and sets it as the default method. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createCreditCardTest() throws ApiException {
        CreditCard creditCard = null;
        Object response = api.createCreditCard(creditCard);
        // TODO: test validations
    }

    /**
     * Entity Transfer Create
     *
     * **DEPRECATED**. Please use [Service Transfer Create](/docs/api/account/#service-transfer-create). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createEntityTransferTest() throws ApiException {
        CreateEntityTransferRequest createEntityTransferRequest = null;
        EntityTransfer response = api.createEntityTransfer(createEntityTransferRequest);
        // TODO: test validations
    }

    /**
     * PayPal Payment Stage
     *
     * **Note**: This endpoint is disabled and no longer accessible. PayPal can be designated as a Payment Method for automated payments using the Cloud Manager. See [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPayPalPaymentTest() throws ApiException {
        PayPal payPal = null;
        CreatePayPalPayment200Response response = api.createPayPalPayment(payPal);
        // TODO: test validations
    }

    /**
     * Payment Make
     *
     * Makes a Payment to your Account.  * The requested amount is charged to the default Payment Method if no &#x60;payment_method_id&#x60; is specified.  * A &#x60;payment_submitted&#x60; event is generated when a payment is successfully submitted. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPaymentTest() throws ApiException {
        PaymentRequest paymentRequest = null;
        Payment response = api.createPayment(paymentRequest);
        // TODO: test validations
    }

    /**
     * Payment Method Add
     *
     * Adds a Payment Method to your Account with the option to set it as the default method.  * Adding a default Payment Method removes the default status from any other Payment Method.  * An Account can have up to 6 active Payment Methods.  * Up to 60 Payment Methods can be added each day.  * Prior to adding a Payment Method, ensure that your billing address information is up-to-date with a valid &#x60;zip&#x60; by using the Account Update ([PUT /account](/docs/api/account/#account-update)) endpoint.  * A &#x60;payment_method_add&#x60; event is generated when a payment is successfully submitted. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPaymentMethodTest() throws ApiException {
        CreatePaymentMethodRequest createPaymentMethodRequest = null;
        Object response = api.createPaymentMethod(createPaymentMethodRequest);
        // TODO: test validations
    }

    /**
     * Promo Credit Add
     *
     * Adds an expiring Promo Credit to your account.  The following restrictions apply:  * Your account must be less than 90 days old. * There must not be an existing Promo Credit already on your account. * The requesting User must be unrestricted. Use the User Update   ([PUT /account/users/{username}](/docs/api/account/#user-update)) to change a User&#39;s restricted status. * The &#x60;promo_code&#x60; must be valid and unexpired. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createPromoCreditTest() throws ApiException {
        CreatePromoCreditRequest createPromoCreditRequest = null;
        Promotion response = api.createPromoCredit(createPromoCreditRequest);
        // TODO: test validations
    }

    /**
     * Service Transfer Create
     *
     * Creates a transfer request for the specified services. A request can contain any of the specified service types and any number of each service type. At this time, only Linodes can be transferred.  When created successfully, a confirmation email is sent to the account that created this transfer containing a transfer token and instructions on completing the transfer.  When a transfer is [accepted](/docs/api/account/#service-transfer-accept), the requested services are moved to the receiving account. Linode services will not experience interruptions due to the transfer process. Backups for Linodes are transferred as well.  DNS records that are associated with requested services will not be transferred or updated. Please ensure that associated DNS records have been updated or communicated to the recipient prior to the transfer.  A transfer can take up to three hours to complete once accepted. When a transfer is completed, billing for transferred services ends for the sending account and begins for the receiving account.  This command can only be accessed by the unrestricted users of an account.  There are several conditions that must be met in order to successfully create a transfer request:  1. The account creating the transfer must not have a past due balance or active Terms of Service violation.  1. The service must be owned by the account that is creating the transfer.  1. The service must not be assigned to another Service Transfer that is pending or that has been accepted and is incomplete.  1. Linodes must not:      * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.      * have any attached Block Storage Volumes.      * have any shared IP addresses.      * have any assigned /56, /64, or /116 IPv6 ranges. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceTransferTest() throws ApiException {
        CreateServiceTransferRequest createServiceTransferRequest = null;
        ServiceTransfer response = api.createServiceTransfer(createServiceTransferRequest);
        // TODO: test validations
    }

    /**
     * User Create
     *
     * Creates a User on your Account. Once created, a confirmation message containing password creation and login instructions is sent to the User&#39;s email address.  This command can only be accessed by the unrestricted users of an account.  The User&#39;s account access is determined by whether or not they are restricted, and what grants they have been given. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createUserTest() throws ApiException {
        User user = null;
        User response = api.createUser(user);
        // TODO: test validations
    }

    /**
     * OAuth Client Delete
     *
     * Deletes an OAuth Client registered with Linode. The Client ID and Client secret will no longer be accepted by &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://login.linode.com\&quot;&gt;https://login.linode.com&lt;/a&gt;, and all tokens issued to this client will be invalidated (meaning that if your application was using a token, it will no longer work). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteClientTest() throws ApiException {
        String clientId = null;
        Object response = api.deleteClient(clientId);
        // TODO: test validations
    }

    /**
     * Entity Transfer Cancel
     *
     * **DEPRECATED**. Please use [Service Transfer Cancel](/docs/api/account/#service-transfer-cancel). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteEntityTransferTest() throws ApiException {
        UUID token = null;
        Object response = api.deleteEntityTransfer(token);
        // TODO: test validations
    }

    /**
     * Payment Method Delete
     *
     * Deactivate the specified Payment Method.  The default Payment Method can not be deleted. To add a new default Payment Method, access the Payment Method Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)) endpoint. To designate an existing Payment Method as the default method, access the Payment Method Make Default ([POST /account/payment-methods/{paymentMethodId}/make-default](/docs/api/account/#payment-method-make-default)) endpoint. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePaymentMethodTest() throws ApiException {
        Integer paymentMethodId = null;
        Object response = api.deletePaymentMethod(paymentMethodId);
        // TODO: test validations
    }

    /**
     * Service Transfer Cancel
     *
     * Cancels the Service Transfer for the provided token. Once cancelled, a transfer cannot be accepted or otherwise acted on in any way. If cancelled in error, the transfer must be [created](/docs/api/account/#service-transfer-create) again.  When cancelled, an email notification for the cancellation is sent to the account that created this transfer. Transfers can not be cancelled if they are expired or have been accepted.  This command can only be accessed by the unrestricted users of the account that created this transfer. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceTransferTest() throws ApiException {
        UUID token = null;
        Object response = api.deleteServiceTransfer(token);
        // TODO: test validations
    }

    /**
     * User Delete
     *
     * Deletes a User. The deleted User will be immediately logged out and may no longer log in or perform any actions. All of the User&#39;s Grants will be removed.  This command can only be accessed by the unrestricted users of an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteUserTest() throws ApiException {
        String username = null;
        Object response = api.deleteUser(username);
        // TODO: test validations
    }

    /**
     * Linode Managed Enable
     *
     * Enables Linode Managed for the entire account and sends a welcome email to the account&#39;s associated email address. Linode Managed can monitor any service or software stack reachable over TCP or HTTP. See our [Linode Managed guide](/docs/guides/linode-managed/) to learn more. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enableAccountManagedTest() throws ApiException {
        Object response = api.enableAccountManaged();
        // TODO: test validations
    }

    /**
     * Event Mark as Read
     *
     * Marks a single Event as read.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void eventReadTest() throws ApiException {
        Integer eventId = null;
        Object response = api.eventRead(eventId);
        // TODO: test validations
    }

    /**
     * Event Mark as Seen
     *
     * Marks all Events up to and including this Event by ID as seen. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void eventSeenTest() throws ApiException {
        Integer eventId = null;
        Object response = api.eventSeen(eventId);
        // TODO: test validations
    }

    /**
     * Staged/Approved PayPal Payment Execute
     *
     * **Note**: This endpoint is disabled and no longer accessible. PayPal can be designated as a Payment Method for automated payments using the Cloud Manager. See [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void executePayPalPaymentTest() throws ApiException {
        PayPalExecute payPalExecute = null;
        Object response = api.executePayPalPayment(payPalExecute);
        // TODO: test validations
    }

    /**
     * Account View
     *
     * Returns the contact and billing information related to your Account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountTest() throws ApiException {
        Account response = api.getAccount();
        // TODO: test validations
    }

    /**
     * Login View
     *
     * Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountLoginTest() throws ApiException {
        Integer loginId = null;
        Login response = api.getAccountLogin(loginId);
        // TODO: test validations
    }

    /**
     * User Logins List All
     *
     * Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountLoginsTest() throws ApiException {
        GetAccountLogins200Response response = api.getAccountLogins();
        // TODO: test validations
    }

    /**
     * Account Settings View
     *
     * Returns information related to your Account settings: Managed service subscription, Longview subscription, and network helper. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountSettingsTest() throws ApiException {
        AccountSettings response = api.getAccountSettings();
        // TODO: test validations
    }

    /**
     * OAuth Client View
     *
     * Returns information about a single OAuth client. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getClientTest() throws ApiException {
        String clientId = null;
        OAuthClient response = api.getClient(clientId);
        // TODO: test validations
    }

    /**
     * OAuth Client Thumbnail View
     *
     * Returns the thumbnail for this OAuth Client.  This is a publicly-viewable endpoint, and can be accessed without authentication. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getClientThumbnailTest() throws ApiException {
        String clientId = null;
        File response = api.getClientThumbnail(clientId);
        // TODO: test validations
    }

    /**
     * OAuth Clients List
     *
     * Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getClientsTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetClients200Response response = api.getClients(page, pageSize);
        // TODO: test validations
    }

    /**
     * Entity Transfer View
     *
     * **DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEntityTransferTest() throws ApiException {
        UUID token = null;
        EntityTransfer response = api.getEntityTransfer(token);
        // TODO: test validations
    }

    /**
     * Entity Transfers List
     *
     * **DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEntityTransfersTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetEntityTransfers200Response response = api.getEntityTransfers(page, pageSize);
        // TODO: test validations
    }

    /**
     * Event View
     *
     * Returns a single Event object. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTest() throws ApiException {
        Integer eventId = null;
        Event response = api.getEvent(eventId);
        // TODO: test validations
    }

    /**
     * Events List
     *
     * Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetEvents200Response response = api.getEvents(page, pageSize);
        // TODO: test validations
    }

    /**
     * Invoice View
     *
     * Returns a single Invoice object.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInvoiceTest() throws ApiException {
        Integer invoiceId = null;
        Invoice response = api.getInvoice(invoiceId);
        // TODO: test validations
    }

    /**
     * Invoice Items List
     *
     * Returns a paginated list of Invoice items.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInvoiceItemsTest() throws ApiException {
        Integer invoiceId = null;
        Integer page = null;
        Integer pageSize = null;
        GetInvoiceItems200Response response = api.getInvoiceItems(invoiceId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Invoices List
     *
     * Returns a paginated list of Invoices against your Account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInvoicesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetInvoices200Response response = api.getInvoices(page, pageSize);
        // TODO: test validations
    }

    /**
     * Maintenance List
     *
     * Returns a collection of Maintenance objects for any entity a user has permissions to view. Cancelled Maintenance objects are not returned.  Currently, Linodes are the only entities available for viewing. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMaintenanceTest() throws ApiException {
        GetMaintenance200Response response = api.getMaintenance();
        // TODO: test validations
    }

    /**
     * Notifications List
     *
     * Returns a collection of Notification objects representing important, often time-sensitive items related to your Account. You cannot interact directly with Notifications, and a Notification will disappear when the circumstances causing it have been resolved. For example, if you have an important Ticket open, you must respond to the Ticket to dismiss the Notification. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNotificationsTest() throws ApiException {
        GetNotifications200Response response = api.getNotifications();
        // TODO: test validations
    }

    /**
     * Payment View
     *
     * Returns information about a specific Payment. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentTest() throws ApiException {
        Integer paymentId = null;
        Payment response = api.getPayment(paymentId);
        // TODO: test validations
    }

    /**
     * Payment Method View
     *
     * View the details of the specified Payment Method. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentMethodTest() throws ApiException {
        Integer paymentMethodId = null;
        PaymentMethod response = api.getPaymentMethod(paymentMethodId);
        // TODO: test validations
    }

    /**
     * Payment Methods List
     *
     * Returns a paginated list of Payment Methods for this Account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentMethodsTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetPaymentMethods200Response response = api.getPaymentMethods(page, pageSize);
        // TODO: test validations
    }

    /**
     * Payments List
     *
     * Returns a paginated list of Payments made on this Account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPaymentsTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetPayments200Response response = api.getPayments(page, pageSize);
        // TODO: test validations
    }

    /**
     * Service Transfer View
     *
     * Returns the details of the Service Transfer for the provided token.  While a transfer is pending, any unrestricted user *of any account* can access this command. After a transfer has been accepted, it can only be viewed by unrestricted users of the accounts that created and accepted the transfer. If cancelled or expired, only unrestricted users of the account that created the transfer can view it. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceTransferTest() throws ApiException {
        UUID token = null;
        ServiceTransfer response = api.getServiceTransfer(token);
        // TODO: test validations
    }

    /**
     * Service Transfers List
     *
     * Returns a collection of all created and accepted Service Transfers for this account, regardless of the user that created or accepted the transfer.  This command can only be accessed by the unrestricted users of an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceTransfersTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetServiceTransfers200Response response = api.getServiceTransfers(page, pageSize);
        // TODO: test validations
    }

    /**
     * Network Utilization View
     *
     * Returns a Transfer object showing your network utilization, in GB, for the current month. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTransferTest() throws ApiException {
        Transfer response = api.getTransfer();
        // TODO: test validations
    }

    /**
     * User View
     *
     * Returns information about a single User on your Account.  This command can only be accessed by the unrestricted users of an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getUserTest() throws ApiException {
        String username = null;
        User response = api.getUser(username);
        // TODO: test validations
    }

    /**
     * User&#39;s Grants View
     *
     * Returns the full grants structure for the specified account User (other than the account owner, see below for details). This includes all entities on the Account alongside the level of access this User has to each of them.  This command can only be accessed by the unrestricted users of an account.  The current authenticated User, including the account owner, may view their own grants at the [/profile/grants](/docs/api/profile/#grants-list) endpoint, but will not see entities that they do not have access to. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getUserGrantsTest() throws ApiException {
        String username = null;
        GrantsResponse response = api.getUserGrants(username);
        // TODO: test validations
    }

    /**
     * Users List
     *
     * Returns a paginated list of Users on your Account.  This command can only be accessed by the unrestricted users of an account.  Users may access all or part of your Account based on their restricted status and grants.  An unrestricted User may access everything on the account, whereas restricted User may only access entities or perform actions they&#39;ve been given specific grants to. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getUsersTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetUsers200Response response = api.getUsers(page, pageSize);
        // TODO: test validations
    }

    /**
     * Payment Method Make Default
     *
     * Make the specified Payment Method the default method for automatically processing payments.  Removes the default status from any other Payment Method. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void makePaymentMethodDefaultTest() throws ApiException {
        Integer paymentMethodId = null;
        Object response = api.makePaymentMethodDefault(paymentMethodId);
        // TODO: test validations
    }

    /**
     * OAuth Client Secret Reset
     *
     * Resets the OAuth Client secret for a client you own, and returns the OAuth Client with the plaintext secret. This secret is not supposed to be publicly known or disclosed anywhere. This can be used to generate a new secret in case the one you have has been leaked, or to get a new secret if you lost the original. The old secret is expired immediately, and logins to your client with the old secret will fail. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resetClientSecretTest() throws ApiException {
        String clientId = null;
        OAuthClient response = api.resetClientSecret(clientId);
        // TODO: test validations
    }

    /**
     * OAuth Client Thumbnail Update
     *
     * Upload a thumbnail for a client you own.  You must upload an image file that will be returned when the thumbnail is retrieved.  This image will be publicly-viewable. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setClientThumbnailTest() throws ApiException {
        String clientId = null;
        File body = null;
        Object response = api.setClientThumbnail(clientId, body);
        // TODO: test validations
    }

    /**
     * Account Update
     *
     * Updates contact and billing information related to your Account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateAccountTest() throws ApiException {
        Account account = null;
        Account response = api.updateAccount(account);
        // TODO: test validations
    }

    /**
     * Account Settings Update
     *
     * Updates your Account settings.  To update your Longview subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateAccountSettingsTest() throws ApiException {
        AccountSettings accountSettings = null;
        AccountSettings response = api.updateAccountSettings(accountSettings);
        // TODO: test validations
    }

    /**
     * OAuth Client Update
     *
     * Update information about an OAuth Client on your Account. This can be especially useful to update the &#x60;redirect_uri&#x60; of your client in the event that the callback url changed in your application. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateClientTest() throws ApiException {
        String clientId = null;
        OAuthClient oauthClient = null;
        OAuthClient response = api.updateClient(clientId, oauthClient);
        // TODO: test validations
    }

    /**
     * User Update
     *
     * Update information about a User on your Account. This can be used to change the restricted status of a User. When making a User restricted, no grants will be configured by default and you must then set up grants in order for the User to access anything on the Account.  This command can only be accessed by the unrestricted users of an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateUserTest() throws ApiException {
        String username = null;
        User user = null;
        User response = api.updateUser(username, user);
        // TODO: test validations
    }

    /**
     * User&#39;s Grants Update
     *
     * Update the grants a User has. This can be used to give a User access to new entities or actions, or take access away.  You do not need to include the grant for every entity on the Account in this request; any that are not included will remain unchanged.  This command can only be accessed by the unrestricted users of an account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateUserGrantsTest() throws ApiException {
        String username = null;
        GrantsResponse grantsResponse = null;
        GrantsResponse response = api.updateUserGrants(username, grantsResponse);
        // TODO: test validations
    }

}
