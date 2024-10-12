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
import org.openapitools.client.model.AddLinodeIPRequest;
import org.openapitools.client.model.Backup;
import org.openapitools.client.model.BootLinodeInstanceRequest;
import org.openapitools.client.model.CloneLinodeInstanceRequest;
import org.openapitools.client.model.CreateLinodeInstanceRequest;
import org.openapitools.client.model.CreateSnapshotRequest;
import org.openapitools.client.model.Disk;
import org.openapitools.client.model.DiskRequest;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetBackups200Response;
import org.openapitools.client.model.GetKernels200Response;
import org.openapitools.client.model.GetLinodeConfigs200Response;
import org.openapitools.client.model.GetLinodeDisks200Response;
import org.openapitools.client.model.GetLinodeFirewalls200Response;
import org.openapitools.client.model.GetLinodeIPs200Response;
import org.openapitools.client.model.GetLinodeInstances200Response;
import org.openapitools.client.model.GetLinodeNodeBalancers200Response;
import org.openapitools.client.model.GetLinodeTransfer200Response;
import org.openapitools.client.model.GetLinodeTransferByYearMonth200Response;
import org.openapitools.client.model.GetLinodeVolumes200Response;
import org.openapitools.client.model.IPAddress;
import org.openapitools.client.model.Kernel;
import org.openapitools.client.model.Linode;
import org.openapitools.client.model.LinodeConfig;
import org.openapitools.client.model.LinodeRequest;
import org.openapitools.client.model.LinodeStats;
import org.openapitools.client.model.MigrateLinodeInstanceRequest;
import org.openapitools.client.model.MutateLinodeInstanceRequest;
import org.openapitools.client.model.RebootLinodeInstanceRequest;
import org.openapitools.client.model.RescueLinodeInstanceRequest;
import org.openapitools.client.model.ResetDiskPasswordRequest;
import org.openapitools.client.model.ResetLinodePasswordRequest;
import org.openapitools.client.model.ResizeDiskRequest;
import org.openapitools.client.model.ResizeLinodeInstanceRequest;
import org.openapitools.client.model.RestoreBackupRequest;
import org.openapitools.client.model.UNKNOWN_BASE_TYPE;
import org.openapitools.client.model.UpdateLinodeIPRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LinodeInstancesApi
 */
@Disabled
public class LinodeInstancesApiTest {

    private final LinodeInstancesApi api = new LinodeInstancesApi();

    /**
     * Configuration Profile Create
     *
     * Adds a new Configuration profile to a Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addLinodeConfigTest() throws ApiException {
        Integer linodeId = null;
        LinodeConfig linodeConfig = null;
        LinodeConfig response = api.addLinodeConfig(linodeId, linodeConfig);
        // TODO: test validations
    }

    /**
     * Disk Create
     *
     * Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a &#x60;label&#x60; is required.  * If no &#x60;label&#x60; is provided, an &#x60;image&#x60; is required instead.  * When creating a Disk from an Image, &#x60;root_pass&#x60; is required.  * The default filesystem for new Disks is &#x60;ext4&#x60;. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addLinodeDiskTest() throws ApiException {
        Integer linodeId = null;
        DiskRequest diskRequest = null;
        Disk response = api.addLinodeDisk(linodeId, diskRequest);
        // TODO: test validations
    }

    /**
     * IPv4 Address Allocate
     *
     * Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addLinodeIPTest() throws ApiException {
        Integer linodeId = null;
        AddLinodeIPRequest addLinodeIPRequest = null;
        IPAddress response = api.addLinodeIP(linodeId, addLinodeIPRequest);
        // TODO: test validations
    }

    /**
     * Linode Boot
     *
     * Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void bootLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        BootLinodeInstanceRequest bootLinodeInstanceRequest = null;
        Object response = api.bootLinodeInstance(linodeId, bootLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Backups Cancel
     *
     * Cancels the Backup service on the given Linode. Deletes all of this Linode&#39;s existing backups forever. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cancelBackupsTest() throws ApiException {
        Integer linodeId = null;
        Object response = api.cancelBackups(linodeId);
        // TODO: test validations
    }

    /**
     * Disk Clone
     *
     * Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cloneLinodeDiskTest() throws ApiException {
        Integer linodeId = null;
        Integer diskId = null;
        Disk response = api.cloneLinodeDisk(linodeId, diskId);
        // TODO: test validations
    }

    /**
     * Linode Clone
     *
     * You can clone your Linode&#39;s existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void cloneLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        CloneLinodeInstanceRequest cloneLinodeInstanceRequest = null;
        Linode response = api.cloneLinodeInstance(linodeId, cloneLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Linode Create
     *
     * Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type&#39;s specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * A default config with two Disks, one being a 512 swap disk, is created.     * &#x60;swap_size&#x60; can be used to customize the swap disk size.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode&#39;s backups.   * You must create a Linode large enough to accommodate the Backup&#39;s size.   * The Disks and Config will match that of the Linode that was backed up.   * The &#x60;root_pass&#x60; will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the &#x60;interfaces&#x60; property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain &#x60;offline&#x60; and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createLinodeInstanceTest() throws ApiException {
        CreateLinodeInstanceRequest createLinodeInstanceRequest = null;
        Linode response = api.createLinodeInstance(createLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Snapshot Create
     *
     * Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createSnapshotTest() throws ApiException {
        Integer linodeId = null;
        CreateSnapshotRequest createSnapshotRequest = null;
        Backup response = api.createSnapshot(linodeId, createSnapshotRequest);
        // TODO: test validations
    }

    /**
     * Disk Delete
     *
     * Deletes a Disk you have permission to &#x60;read_write&#x60;.  **Deleting a Disk is a destructive action and cannot be undone.** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDiskTest() throws ApiException {
        Integer linodeId = null;
        Integer diskId = null;
        Object response = api.deleteDisk(linodeId, diskId);
        // TODO: test validations
    }

    /**
     * Configuration Profile Delete
     *
     * Deletes the specified Configuration profile from the specified Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLinodeConfigTest() throws ApiException {
        Integer linodeId = null;
        Integer configId = null;
        Object response = api.deleteLinodeConfig(linodeId, configId);
        // TODO: test validations
    }

    /**
     * Linode Delete
     *
     * Deletes a Linode you have permission to &#x60;read_write&#x60;.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        Object response = api.deleteLinodeInstance(linodeId);
        // TODO: test validations
    }

    /**
     * Backups Enable
     *
     * Enables backups for the specified Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enableBackupsTest() throws ApiException {
        Integer linodeId = null;
        Object response = api.enableBackups(linodeId);
        // TODO: test validations
    }

    /**
     * Backup View
     *
     * Returns information about a Backup. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBackupTest() throws ApiException {
        Integer linodeId = null;
        Integer backupId = null;
        Backup response = api.getBackup(linodeId, backupId);
        // TODO: test validations
    }

    /**
     * Backups List
     *
     * Returns information about this Linode&#39;s available backups. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getBackupsTest() throws ApiException {
        Integer linodeId = null;
        GetBackups200Response response = api.getBackups(linodeId);
        // TODO: test validations
    }

    /**
     * Kernel View
     *
     * Returns information about a single Kernel. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getKernelTest() throws ApiException {
        String kernelId = null;
        Kernel response = api.getKernel(kernelId);
        // TODO: test validations
    }

    /**
     * Kernels List
     *
     * Lists available Kernels. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getKernelsTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetKernels200Response response = api.getKernels(page, pageSize);
        // TODO: test validations
    }

    /**
     * Configuration Profile View
     *
     * Returns information about a specific Configuration profile. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeConfigTest() throws ApiException {
        Integer linodeId = null;
        Integer configId = null;
        LinodeConfig response = api.getLinodeConfig(linodeId, configId);
        // TODO: test validations
    }

    /**
     * Configuration Profiles List
     *
     * Lists Configuration profiles associated with a Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeConfigsTest() throws ApiException {
        Integer linodeId = null;
        Integer page = null;
        Integer pageSize = null;
        GetLinodeConfigs200Response response = api.getLinodeConfigs(linodeId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Disk View
     *
     * View Disk information for a Disk associated with this Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeDiskTest() throws ApiException {
        Integer linodeId = null;
        Integer diskId = null;
        Disk response = api.getLinodeDisk(linodeId, diskId);
        // TODO: test validations
    }

    /**
     * Disks List
     *
     * View Disk information for Disks associated with this Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeDisksTest() throws ApiException {
        Integer linodeId = null;
        Integer page = null;
        Integer pageSize = null;
        GetLinodeDisks200Response response = api.getLinodeDisks(linodeId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Firewalls List
     *
     * View Firewall information for Firewalls associated with this Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeFirewallsTest() throws ApiException {
        Integer linodeId = null;
        Integer page = null;
        Integer pageSize = null;
        GetLinodeFirewalls200Response response = api.getLinodeFirewalls(linodeId, page, pageSize);
        // TODO: test validations
    }

    /**
     * IP Address View
     *
     * View information about the specified IP address associated with the specified Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeIPTest() throws ApiException {
        Integer linodeId = null;
        String address = null;
        IPAddress response = api.getLinodeIP(linodeId, address);
        // TODO: test validations
    }

    /**
     * Networking Information List
     *
     * Returns networking information for a single Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeIPsTest() throws ApiException {
        Integer linodeId = null;
        GetLinodeIPs200Response response = api.getLinodeIPs(linodeId);
        // TODO: test validations
    }

    /**
     * Linode View
     *
     * Get a specific Linode by ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        Linode response = api.getLinodeInstance(linodeId);
        // TODO: test validations
    }

    /**
     * Linodes List
     *
     * Returns a paginated list of Linodes you have permission to view. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeInstancesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetLinodeInstances200Response response = api.getLinodeInstances(page, pageSize);
        // TODO: test validations
    }

    /**
     * Linode NodeBalancers View
     *
     * Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User&#39;s Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeNodeBalancersTest() throws ApiException {
        Integer linodeId = null;
        GetLinodeNodeBalancers200Response response = api.getLinodeNodeBalancers(linodeId);
        // TODO: test validations
    }

    /**
     * Linode Statistics View
     *
     * Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeStatsTest() throws ApiException {
        Integer linodeId = null;
        LinodeStats response = api.getLinodeStats(linodeId);
        // TODO: test validations
    }

    /**
     * Statistics View (year/month)
     *
     * Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeStatsByYearMonthTest() throws ApiException {
        Integer linodeId = null;
        Integer year = null;
        Integer month = null;
        LinodeStats response = api.getLinodeStatsByYearMonth(linodeId, year, month);
        // TODO: test validations
    }

    /**
     * Network Transfer View
     *
     * Returns a Linode&#39;s network transfer pool statistics for the current month. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeTransferTest() throws ApiException {
        Integer linodeId = null;
        GetLinodeTransfer200Response response = api.getLinodeTransfer(linodeId);
        // TODO: test validations
    }

    /**
     * Network Transfer View (year/month)
     *
     * Returns a Linode&#39;s network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeTransferByYearMonthTest() throws ApiException {
        Integer linodeId = null;
        Integer year = null;
        Integer month = null;
        GetLinodeTransferByYearMonth200Response response = api.getLinodeTransferByYearMonth(linodeId, year, month);
        // TODO: test validations
    }

    /**
     * Linode&#39;s Volumes List
     *
     * View Block Storage Volumes attached to this Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLinodeVolumesTest() throws ApiException {
        Integer linodeId = null;
        Integer page = null;
        Integer pageSize = null;
        GetLinodeVolumes200Response response = api.getLinodeVolumes(linodeId, page, pageSize);
        // TODO: test validations
    }

    /**
     * DC Migration/Pending Host Migration Initiate
     *
     * Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a &#x60;region&#x60; parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 &#x60;/116&#x60; pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void migrateLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        MigrateLinodeInstanceRequest migrateLinodeInstanceRequest = null;
        Object response = api.migrateLinodeInstance(linodeId, migrateLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Linode Upgrade
     *
     * Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void mutateLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        MutateLinodeInstanceRequest mutateLinodeInstanceRequest = null;
        Object response = api.mutateLinodeInstance(linodeId, mutateLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Linode Reboot
     *
     * Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rebootLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        RebootLinodeInstanceRequest rebootLinodeInstanceRequest = null;
        Object response = api.rebootLinodeInstance(linodeId, rebootLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Linode Rebuild
     *
     * Rebuilds a Linode you have the &#x60;read_write&#x60; permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new &#x60;image&#x60; to the Linode with the given attributes. Additionally:    * Requires an &#x60;image&#x60; be supplied.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the     &#x60;authorized_keys&#x60; field. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rebuildLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = null;
        Linode response = api.rebuildLinodeInstance(linodeId, UNKNOWN_BASE_TYPE);
        // TODO: test validations
    }

    /**
     * IPv4 Address Delete
     *
     * Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode&#39;s last remaining public IPv4 address. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void removeLinodeIPTest() throws ApiException {
        Integer linodeId = null;
        String address = null;
        Object response = api.removeLinodeIP(linodeId, address);
        // TODO: test validations
    }

    /**
     * Linode Boot into Rescue Mode
     *
     * Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \&quot;sdh\&quot; is reserved and unavailable during rescue. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rescueLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        RescueLinodeInstanceRequest rescueLinodeInstanceRequest = null;
        Object response = api.rescueLinodeInstance(linodeId, rescueLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Disk Root Password Reset
     *
     * Resets the password of a Disk you have permission to &#x60;read_write&#x60;. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resetDiskPasswordTest() throws ApiException {
        Integer linodeId = null;
        Integer diskId = null;
        ResetDiskPasswordRequest resetDiskPasswordRequest = null;
        Object response = api.resetDiskPassword(linodeId, diskId, resetDiskPasswordRequest);
        // TODO: test validations
    }

    /**
     * Linode Root Password Reset
     *
     * Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk&#39;s root password. * A &#x60;password_reset&#x60; event is generated when a root password reset is successful. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resetLinodePasswordTest() throws ApiException {
        Integer linodeId = null;
        ResetLinodePasswordRequest resetLinodePasswordRequest = null;
        Object response = api.resetLinodePassword(linodeId, resetLinodePasswordRequest);
        // TODO: test validations
    }

    /**
     * Disk Resize
     *
     * Resizes a Disk you have permission to &#x60;read_write&#x60;.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode&#39;s active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resizeDiskTest() throws ApiException {
        Integer linodeId = null;
        Integer diskId = null;
        ResizeDiskRequest resizeDiskRequest = null;
        Object response = api.resizeDisk(linodeId, diskId, resizeDiskRequest);
        // TODO: test validations
    }

    /**
     * Linode Resize
     *
     * Resizes a Linode you have the &#x60;read_write&#x60; permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resizeLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        ResizeLinodeInstanceRequest resizeLinodeInstanceRequest = null;
        Object response = api.resizeLinodeInstance(linodeId, resizeLinodeInstanceRequest);
        // TODO: test validations
    }

    /**
     * Backup Restore
     *
     * Restores a Linode&#39;s Backup to the specified Linode. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void restoreBackupTest() throws ApiException {
        Integer linodeId = null;
        Integer backupId = null;
        RestoreBackupRequest restoreBackupRequest = null;
        Object response = api.restoreBackup(linodeId, backupId, restoreBackupRequest);
        // TODO: test validations
    }

    /**
     * Linode Shut Down
     *
     * Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void shutdownLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        Object response = api.shutdownLinodeInstance(linodeId);
        // TODO: test validations
    }

    /**
     * Disk Update
     *
     * Updates a Disk that you have permission to &#x60;read_write&#x60;. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDiskTest() throws ApiException {
        Integer linodeId = null;
        Integer diskId = null;
        Disk disk = null;
        Disk response = api.updateDisk(linodeId, diskId, disk);
        // TODO: test validations
    }

    /**
     * Configuration Profile Update
     *
     * Updates a Configuration profile. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateLinodeConfigTest() throws ApiException {
        Integer linodeId = null;
        Integer configId = null;
        LinodeConfig linodeConfig = null;
        LinodeConfig response = api.updateLinodeConfig(linodeId, configId, linodeConfig);
        // TODO: test validations
    }

    /**
     * IP Address Update
     *
     * Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to &#x60;null&#x60; for a public IPv4 address, resets it to the default \&quot;ip.linodeusercontent.com\&quot; RDNS value. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateLinodeIPTest() throws ApiException {
        Integer linodeId = null;
        String address = null;
        UpdateLinodeIPRequest updateLinodeIPRequest = null;
        IPAddress response = api.updateLinodeIP(linodeId, address, updateLinodeIPRequest);
        // TODO: test validations
    }

    /**
     * Linode Update
     *
     * Updates a Linode that you have permission to &#x60;read_write&#x60;.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateLinodeInstanceTest() throws ApiException {
        Integer linodeId = null;
        Linode linode = null;
        Linode response = api.updateLinodeInstance(linodeId, linode);
        // TODO: test validations
    }

}
