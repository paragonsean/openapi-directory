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

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


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

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LinodeInstancesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LinodeInstancesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LinodeInstancesApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for addLinodeConfig
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param linodeConfig The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile was created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLinodeConfigCall(Integer linodeId, LinodeConfig linodeConfig, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = linodeConfig;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/configs"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addLinodeConfigValidateBeforeCall(Integer linodeId, LinodeConfig linodeConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling addLinodeConfig(Async)");
        }

        // verify the required parameter 'linodeConfig' is set
        if (linodeConfig == null) {
            throw new ApiException("Missing the required parameter 'linodeConfig' when calling addLinodeConfig(Async)");
        }

        return addLinodeConfigCall(linodeId, linodeConfig, _callback);

    }

    /**
     * Configuration Profile Create
     * Adds a new Configuration profile to a Linode. 
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param linodeConfig The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with.  (required)
     * @return LinodeConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile was created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LinodeConfig addLinodeConfig(Integer linodeId, LinodeConfig linodeConfig) throws ApiException {
        ApiResponse<LinodeConfig> localVarResp = addLinodeConfigWithHttpInfo(linodeId, linodeConfig);
        return localVarResp.getData();
    }

    /**
     * Configuration Profile Create
     * Adds a new Configuration profile to a Linode. 
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param linodeConfig The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with.  (required)
     * @return ApiResponse&lt;LinodeConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile was created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LinodeConfig> addLinodeConfigWithHttpInfo(Integer linodeId, LinodeConfig linodeConfig) throws ApiException {
        okhttp3.Call localVarCall = addLinodeConfigValidateBeforeCall(linodeId, linodeConfig, null);
        Type localVarReturnType = new TypeToken<LinodeConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Configuration Profile Create (asynchronously)
     * Adds a new Configuration profile to a Linode. 
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param linodeConfig The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile was created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLinodeConfigAsync(Integer linodeId, LinodeConfig linodeConfig, final ApiCallback<LinodeConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = addLinodeConfigValidateBeforeCall(linodeId, linodeConfig, _callback);
        Type localVarReturnType = new TypeToken<LinodeConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addLinodeDisk
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskRequest The parameters to set when creating the Disk.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLinodeDiskCall(Integer linodeId, DiskRequest diskRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = diskRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addLinodeDiskValidateBeforeCall(Integer linodeId, DiskRequest diskRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling addLinodeDisk(Async)");
        }

        // verify the required parameter 'diskRequest' is set
        if (diskRequest == null) {
            throw new ApiException("Missing the required parameter 'diskRequest' when calling addLinodeDisk(Async)");
        }

        return addLinodeDiskCall(linodeId, diskRequest, _callback);

    }

    /**
     * Disk Create
     * Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a &#x60;label&#x60; is required.  * If no &#x60;label&#x60; is provided, an &#x60;image&#x60; is required instead.  * When creating a Disk from an Image, &#x60;root_pass&#x60; is required.  * The default filesystem for new Disks is &#x60;ext4&#x60;. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskRequest The parameters to set when creating the Disk.  (required)
     * @return Disk
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Disk addLinodeDisk(Integer linodeId, DiskRequest diskRequest) throws ApiException {
        ApiResponse<Disk> localVarResp = addLinodeDiskWithHttpInfo(linodeId, diskRequest);
        return localVarResp.getData();
    }

    /**
     * Disk Create
     * Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a &#x60;label&#x60; is required.  * If no &#x60;label&#x60; is provided, an &#x60;image&#x60; is required instead.  * When creating a Disk from an Image, &#x60;root_pass&#x60; is required.  * The default filesystem for new Disks is &#x60;ext4&#x60;. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskRequest The parameters to set when creating the Disk.  (required)
     * @return ApiResponse&lt;Disk&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Disk> addLinodeDiskWithHttpInfo(Integer linodeId, DiskRequest diskRequest) throws ApiException {
        okhttp3.Call localVarCall = addLinodeDiskValidateBeforeCall(linodeId, diskRequest, null);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk Create (asynchronously)
     * Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a &#x60;label&#x60; is required.  * If no &#x60;label&#x60; is provided, an &#x60;image&#x60; is required instead.  * When creating a Disk from an Image, &#x60;root_pass&#x60; is required.  * The default filesystem for new Disks is &#x60;ext4&#x60;. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskRequest The parameters to set when creating the Disk.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLinodeDiskAsync(Integer linodeId, DiskRequest diskRequest, final ApiCallback<Disk> _callback) throws ApiException {

        okhttp3.Call localVarCall = addLinodeDiskValidateBeforeCall(linodeId, diskRequest, _callback);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for addLinodeIP
     * @param linodeId ID of the Linode to look up. (required)
     * @param addLinodeIPRequest Information about the address you are creating. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address was successfully allocated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLinodeIPCall(Integer linodeId, AddLinodeIPRequest addLinodeIPRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = addLinodeIPRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/ips"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addLinodeIPValidateBeforeCall(Integer linodeId, AddLinodeIPRequest addLinodeIPRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling addLinodeIP(Async)");
        }

        // verify the required parameter 'addLinodeIPRequest' is set
        if (addLinodeIPRequest == null) {
            throw new ApiException("Missing the required parameter 'addLinodeIPRequest' when calling addLinodeIP(Async)");
        }

        return addLinodeIPCall(linodeId, addLinodeIPRequest, _callback);

    }

    /**
     * IPv4 Address Allocate
     * Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param addLinodeIPRequest Information about the address you are creating. (required)
     * @return IPAddress
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address was successfully allocated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPAddress addLinodeIP(Integer linodeId, AddLinodeIPRequest addLinodeIPRequest) throws ApiException {
        ApiResponse<IPAddress> localVarResp = addLinodeIPWithHttpInfo(linodeId, addLinodeIPRequest);
        return localVarResp.getData();
    }

    /**
     * IPv4 Address Allocate
     * Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param addLinodeIPRequest Information about the address you are creating. (required)
     * @return ApiResponse&lt;IPAddress&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address was successfully allocated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPAddress> addLinodeIPWithHttpInfo(Integer linodeId, AddLinodeIPRequest addLinodeIPRequest) throws ApiException {
        okhttp3.Call localVarCall = addLinodeIPValidateBeforeCall(linodeId, addLinodeIPRequest, null);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv4 Address Allocate (asynchronously)
     * Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param addLinodeIPRequest Information about the address you are creating. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address was successfully allocated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addLinodeIPAsync(Integer linodeId, AddLinodeIPRequest addLinodeIPRequest, final ApiCallback<IPAddress> _callback) throws ApiException {

        okhttp3.Call localVarCall = addLinodeIPValidateBeforeCall(linodeId, addLinodeIPRequest, _callback);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for bootLinodeInstance
     * @param linodeId The ID of the Linode to boot. (required)
     * @param bootLinodeInstanceRequest Optional configuration to boot into (see above). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Boot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call bootLinodeInstanceCall(Integer linodeId, BootLinodeInstanceRequest bootLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = bootLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/boot"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call bootLinodeInstanceValidateBeforeCall(Integer linodeId, BootLinodeInstanceRequest bootLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling bootLinodeInstance(Async)");
        }

        return bootLinodeInstanceCall(linodeId, bootLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Boot
     * Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 
     * @param linodeId The ID of the Linode to boot. (required)
     * @param bootLinodeInstanceRequest Optional configuration to boot into (see above). (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Boot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object bootLinodeInstance(Integer linodeId, BootLinodeInstanceRequest bootLinodeInstanceRequest) throws ApiException {
        ApiResponse<Object> localVarResp = bootLinodeInstanceWithHttpInfo(linodeId, bootLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Boot
     * Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 
     * @param linodeId The ID of the Linode to boot. (required)
     * @param bootLinodeInstanceRequest Optional configuration to boot into (see above). (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Boot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> bootLinodeInstanceWithHttpInfo(Integer linodeId, BootLinodeInstanceRequest bootLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = bootLinodeInstanceValidateBeforeCall(linodeId, bootLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Boot (asynchronously)
     * Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 
     * @param linodeId The ID of the Linode to boot. (required)
     * @param bootLinodeInstanceRequest Optional configuration to boot into (see above). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Boot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call bootLinodeInstanceAsync(Integer linodeId, BootLinodeInstanceRequest bootLinodeInstanceRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = bootLinodeInstanceValidateBeforeCall(linodeId, bootLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for cancelBackups
     * @param linodeId The ID of the Linode to cancel backup service for. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was cancelled for the specified Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cancelBackupsCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/backups/cancel"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cancelBackupsValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling cancelBackups(Async)");
        }

        return cancelBackupsCall(linodeId, _callback);

    }

    /**
     * Backups Cancel
     * Cancels the Backup service on the given Linode. Deletes all of this Linode&#39;s existing backups forever. 
     * @param linodeId The ID of the Linode to cancel backup service for. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was cancelled for the specified Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object cancelBackups(Integer linodeId) throws ApiException {
        ApiResponse<Object> localVarResp = cancelBackupsWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Backups Cancel
     * Cancels the Backup service on the given Linode. Deletes all of this Linode&#39;s existing backups forever. 
     * @param linodeId The ID of the Linode to cancel backup service for. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was cancelled for the specified Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> cancelBackupsWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = cancelBackupsValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Backups Cancel (asynchronously)
     * Cancels the Backup service on the given Linode. Deletes all of this Linode&#39;s existing backups forever. 
     * @param linodeId The ID of the Linode to cancel backup service for. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was cancelled for the specified Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cancelBackupsAsync(Integer linodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = cancelBackupsValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for cloneLinodeDisk
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to clone. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk clone initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloneLinodeDiskCall(Integer linodeId, Integer diskId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks/{diskId}/clone"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "diskId" + "}", localVarApiClient.escapeString(diskId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cloneLinodeDiskValidateBeforeCall(Integer linodeId, Integer diskId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling cloneLinodeDisk(Async)");
        }

        // verify the required parameter 'diskId' is set
        if (diskId == null) {
            throw new ApiException("Missing the required parameter 'diskId' when calling cloneLinodeDisk(Async)");
        }

        return cloneLinodeDiskCall(linodeId, diskId, _callback);

    }

    /**
     * Disk Clone
     * Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to clone. (required)
     * @return Disk
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk clone initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Disk cloneLinodeDisk(Integer linodeId, Integer diskId) throws ApiException {
        ApiResponse<Disk> localVarResp = cloneLinodeDiskWithHttpInfo(linodeId, diskId);
        return localVarResp.getData();
    }

    /**
     * Disk Clone
     * Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to clone. (required)
     * @return ApiResponse&lt;Disk&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk clone initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Disk> cloneLinodeDiskWithHttpInfo(Integer linodeId, Integer diskId) throws ApiException {
        okhttp3.Call localVarCall = cloneLinodeDiskValidateBeforeCall(linodeId, diskId, null);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk Clone (asynchronously)
     * Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to clone. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Disk clone initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloneLinodeDiskAsync(Integer linodeId, Integer diskId, final ApiCallback<Disk> _callback) throws ApiException {

        okhttp3.Call localVarCall = cloneLinodeDiskValidateBeforeCall(linodeId, diskId, _callback);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for cloneLinodeInstance
     * @param linodeId ID of the Linode to clone. (required)
     * @param cloneLinodeInstanceRequest The requested state your Linode will be cloned into. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Clone started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloneLinodeInstanceCall(Integer linodeId, CloneLinodeInstanceRequest cloneLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = cloneLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/clone"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cloneLinodeInstanceValidateBeforeCall(Integer linodeId, CloneLinodeInstanceRequest cloneLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling cloneLinodeInstance(Async)");
        }

        // verify the required parameter 'cloneLinodeInstanceRequest' is set
        if (cloneLinodeInstanceRequest == null) {
            throw new ApiException("Missing the required parameter 'cloneLinodeInstanceRequest' when calling cloneLinodeInstance(Async)");
        }

        return cloneLinodeInstanceCall(linodeId, cloneLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Clone
     * You can clone your Linode&#39;s existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 
     * @param linodeId ID of the Linode to clone. (required)
     * @param cloneLinodeInstanceRequest The requested state your Linode will be cloned into. (required)
     * @return Linode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Clone started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Linode cloneLinodeInstance(Integer linodeId, CloneLinodeInstanceRequest cloneLinodeInstanceRequest) throws ApiException {
        ApiResponse<Linode> localVarResp = cloneLinodeInstanceWithHttpInfo(linodeId, cloneLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Clone
     * You can clone your Linode&#39;s existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 
     * @param linodeId ID of the Linode to clone. (required)
     * @param cloneLinodeInstanceRequest The requested state your Linode will be cloned into. (required)
     * @return ApiResponse&lt;Linode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Clone started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Linode> cloneLinodeInstanceWithHttpInfo(Integer linodeId, CloneLinodeInstanceRequest cloneLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = cloneLinodeInstanceValidateBeforeCall(linodeId, cloneLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Clone (asynchronously)
     * You can clone your Linode&#39;s existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 
     * @param linodeId ID of the Linode to clone. (required)
     * @param cloneLinodeInstanceRequest The requested state your Linode will be cloned into. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Clone started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloneLinodeInstanceAsync(Integer linodeId, CloneLinodeInstanceRequest cloneLinodeInstanceRequest, final ApiCallback<Linode> _callback) throws ApiException {

        okhttp3.Call localVarCall = cloneLinodeInstanceValidateBeforeCall(linodeId, cloneLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createLinodeInstance
     * @param createLinodeInstanceRequest The requested initial state of a new Linode. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Linode is being created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createLinodeInstanceCall(CreateLinodeInstanceRequest createLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createLinodeInstanceValidateBeforeCall(CreateLinodeInstanceRequest createLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createLinodeInstanceRequest' is set
        if (createLinodeInstanceRequest == null) {
            throw new ApiException("Missing the required parameter 'createLinodeInstanceRequest' when calling createLinodeInstance(Async)");
        }

        return createLinodeInstanceCall(createLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Create
     * Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type&#39;s specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * A default config with two Disks, one being a 512 swap disk, is created.     * &#x60;swap_size&#x60; can be used to customize the swap disk size.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode&#39;s backups.   * You must create a Linode large enough to accommodate the Backup&#39;s size.   * The Disks and Config will match that of the Linode that was backed up.   * The &#x60;root_pass&#x60; will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the &#x60;interfaces&#x60; property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain &#x60;offline&#x60; and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param createLinodeInstanceRequest The requested initial state of a new Linode. (required)
     * @return Linode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Linode is being created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Linode createLinodeInstance(CreateLinodeInstanceRequest createLinodeInstanceRequest) throws ApiException {
        ApiResponse<Linode> localVarResp = createLinodeInstanceWithHttpInfo(createLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Create
     * Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type&#39;s specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * A default config with two Disks, one being a 512 swap disk, is created.     * &#x60;swap_size&#x60; can be used to customize the swap disk size.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode&#39;s backups.   * You must create a Linode large enough to accommodate the Backup&#39;s size.   * The Disks and Config will match that of the Linode that was backed up.   * The &#x60;root_pass&#x60; will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the &#x60;interfaces&#x60; property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain &#x60;offline&#x60; and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param createLinodeInstanceRequest The requested initial state of a new Linode. (required)
     * @return ApiResponse&lt;Linode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Linode is being created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Linode> createLinodeInstanceWithHttpInfo(CreateLinodeInstanceRequest createLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = createLinodeInstanceValidateBeforeCall(createLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Create (asynchronously)
     * Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type&#39;s specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * A default config with two Disks, one being a 512 swap disk, is created.     * &#x60;swap_size&#x60; can be used to customize the swap disk size.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode&#39;s backups.   * You must create a Linode large enough to accommodate the Backup&#39;s size.   * The Disks and Config will match that of the Linode that was backed up.   * The &#x60;root_pass&#x60; will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the &#x60;interfaces&#x60; property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain &#x60;offline&#x60; and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param createLinodeInstanceRequest The requested initial state of a new Linode. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Linode is being created.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createLinodeInstanceAsync(CreateLinodeInstanceRequest createLinodeInstanceRequest, final ApiCallback<Linode> _callback) throws ApiException {

        okhttp3.Call localVarCall = createLinodeInstanceValidateBeforeCall(createLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createSnapshot
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @param createSnapshotRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Snapshot request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createSnapshotCall(Integer linodeId, CreateSnapshotRequest createSnapshotRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createSnapshotRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/backups"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createSnapshotValidateBeforeCall(Integer linodeId, CreateSnapshotRequest createSnapshotRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling createSnapshot(Async)");
        }

        // verify the required parameter 'createSnapshotRequest' is set
        if (createSnapshotRequest == null) {
            throw new ApiException("Missing the required parameter 'createSnapshotRequest' when calling createSnapshot(Async)");
        }

        return createSnapshotCall(linodeId, createSnapshotRequest, _callback);

    }

    /**
     * Snapshot Create
     * Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @param createSnapshotRequest  (required)
     * @return Backup
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Snapshot request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Backup createSnapshot(Integer linodeId, CreateSnapshotRequest createSnapshotRequest) throws ApiException {
        ApiResponse<Backup> localVarResp = createSnapshotWithHttpInfo(linodeId, createSnapshotRequest);
        return localVarResp.getData();
    }

    /**
     * Snapshot Create
     * Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @param createSnapshotRequest  (required)
     * @return ApiResponse&lt;Backup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Snapshot request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Backup> createSnapshotWithHttpInfo(Integer linodeId, CreateSnapshotRequest createSnapshotRequest) throws ApiException {
        okhttp3.Call localVarCall = createSnapshotValidateBeforeCall(linodeId, createSnapshotRequest, null);
        Type localVarReturnType = new TypeToken<Backup>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Snapshot Create (asynchronously)
     * Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @param createSnapshotRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Snapshot request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createSnapshotAsync(Integer linodeId, CreateSnapshotRequest createSnapshotRequest, final ApiCallback<Backup> _callback) throws ApiException {

        okhttp3.Call localVarCall = createSnapshotValidateBeforeCall(linodeId, createSnapshotRequest, _callback);
        Type localVarReturnType = new TypeToken<Backup>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDisk
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDiskCall(Integer linodeId, Integer diskId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks/{diskId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "diskId" + "}", localVarApiClient.escapeString(diskId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDiskValidateBeforeCall(Integer linodeId, Integer diskId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling deleteDisk(Async)");
        }

        // verify the required parameter 'diskId' is set
        if (diskId == null) {
            throw new ApiException("Missing the required parameter 'diskId' when calling deleteDisk(Async)");
        }

        return deleteDiskCall(linodeId, diskId, _callback);

    }

    /**
     * Disk Delete
     * Deletes a Disk you have permission to &#x60;read_write&#x60;.  **Deleting a Disk is a destructive action and cannot be undone.** 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDisk(Integer linodeId, Integer diskId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDiskWithHttpInfo(linodeId, diskId);
        return localVarResp.getData();
    }

    /**
     * Disk Delete
     * Deletes a Disk you have permission to &#x60;read_write&#x60;.  **Deleting a Disk is a destructive action and cannot be undone.** 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDiskWithHttpInfo(Integer linodeId, Integer diskId) throws ApiException {
        okhttp3.Call localVarCall = deleteDiskValidateBeforeCall(linodeId, diskId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk Delete (asynchronously)
     * Deletes a Disk you have permission to &#x60;read_write&#x60;.  **Deleting a Disk is a destructive action and cannot be undone.** 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDiskAsync(Integer linodeId, Integer diskId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDiskValidateBeforeCall(linodeId, diskId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLinodeConfig
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully deleted.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLinodeConfigCall(Integer linodeId, Integer configId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/configs/{configId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteLinodeConfigValidateBeforeCall(Integer linodeId, Integer configId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling deleteLinodeConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling deleteLinodeConfig(Async)");
        }

        return deleteLinodeConfigCall(linodeId, configId, _callback);

    }

    /**
     * Configuration Profile Delete
     * Deletes the specified Configuration profile from the specified Linode. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully deleted.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteLinodeConfig(Integer linodeId, Integer configId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteLinodeConfigWithHttpInfo(linodeId, configId);
        return localVarResp.getData();
    }

    /**
     * Configuration Profile Delete
     * Deletes the specified Configuration profile from the specified Linode. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully deleted.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteLinodeConfigWithHttpInfo(Integer linodeId, Integer configId) throws ApiException {
        okhttp3.Call localVarCall = deleteLinodeConfigValidateBeforeCall(linodeId, configId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Configuration Profile Delete (asynchronously)
     * Deletes the specified Configuration profile from the specified Linode. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully deleted.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLinodeConfigAsync(Integer linodeId, Integer configId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLinodeConfigValidateBeforeCall(linodeId, configId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLinodeInstance
     * @param linodeId ID of the Linode to look up (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLinodeInstanceCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteLinodeInstanceValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling deleteLinodeInstance(Async)");
        }

        return deleteLinodeInstanceCall(linodeId, _callback);

    }

    /**
     * Linode Delete
     * Deletes a Linode you have permission to &#x60;read_write&#x60;.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 
     * @param linodeId ID of the Linode to look up (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteLinodeInstance(Integer linodeId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteLinodeInstanceWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Linode Delete
     * Deletes a Linode you have permission to &#x60;read_write&#x60;.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 
     * @param linodeId ID of the Linode to look up (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteLinodeInstanceWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = deleteLinodeInstanceValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Delete (asynchronously)
     * Deletes a Linode you have permission to &#x60;read_write&#x60;.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 
     * @param linodeId ID of the Linode to look up (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLinodeInstanceAsync(Integer linodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLinodeInstanceValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for enableBackups
     * @param linodeId The ID of the Linode to enable backup service for. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was enabled. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call enableBackupsCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/backups/enable"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call enableBackupsValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling enableBackups(Async)");
        }

        return enableBackupsCall(linodeId, _callback);

    }

    /**
     * Backups Enable
     * Enables backups for the specified Linode. 
     * @param linodeId The ID of the Linode to enable backup service for. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was enabled. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object enableBackups(Integer linodeId) throws ApiException {
        ApiResponse<Object> localVarResp = enableBackupsWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Backups Enable
     * Enables backups for the specified Linode. 
     * @param linodeId The ID of the Linode to enable backup service for. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was enabled. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> enableBackupsWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = enableBackupsValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Backups Enable (asynchronously)
     * Enables backups for the specified Linode. 
     * @param linodeId The ID of the Linode to enable backup service for. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Backup service was enabled. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call enableBackupsAsync(Integer linodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = enableBackupsValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBackup
     * @param linodeId The ID of the Linode the Backup belongs to. (required)
     * @param backupId The ID of the Backup to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Backup. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBackupCall(Integer linodeId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/backups/{backupId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "backupId" + "}", localVarApiClient.escapeString(backupId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBackupValidateBeforeCall(Integer linodeId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling getBackup(Async)");
        }

        return getBackupCall(linodeId, backupId, _callback);

    }

    /**
     * Backup View
     * Returns information about a Backup. 
     * @param linodeId The ID of the Linode the Backup belongs to. (required)
     * @param backupId The ID of the Backup to look up. (required)
     * @return Backup
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Backup. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Backup getBackup(Integer linodeId, Integer backupId) throws ApiException {
        ApiResponse<Backup> localVarResp = getBackupWithHttpInfo(linodeId, backupId);
        return localVarResp.getData();
    }

    /**
     * Backup View
     * Returns information about a Backup. 
     * @param linodeId The ID of the Linode the Backup belongs to. (required)
     * @param backupId The ID of the Backup to look up. (required)
     * @return ApiResponse&lt;Backup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Backup. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Backup> getBackupWithHttpInfo(Integer linodeId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = getBackupValidateBeforeCall(linodeId, backupId, null);
        Type localVarReturnType = new TypeToken<Backup>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Backup View (asynchronously)
     * Returns information about a Backup. 
     * @param linodeId The ID of the Linode the Backup belongs to. (required)
     * @param backupId The ID of the Backup to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Backup. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBackupAsync(Integer linodeId, Integer backupId, final ApiCallback<Backup> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBackupValidateBeforeCall(linodeId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Backup>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBackups
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s available backups. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBackupsCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/backups"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBackupsValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getBackups(Async)");
        }

        return getBackupsCall(linodeId, _callback);

    }

    /**
     * Backups List
     * Returns information about this Linode&#39;s available backups. 
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @return GetBackups200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s available backups. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetBackups200Response getBackups(Integer linodeId) throws ApiException {
        ApiResponse<GetBackups200Response> localVarResp = getBackupsWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Backups List
     * Returns information about this Linode&#39;s available backups. 
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @return ApiResponse&lt;GetBackups200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s available backups. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetBackups200Response> getBackupsWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = getBackupsValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<GetBackups200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Backups List (asynchronously)
     * Returns information about this Linode&#39;s available backups. 
     * @param linodeId The ID of the Linode the backups belong to. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s available backups. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBackupsAsync(Integer linodeId, final ApiCallback<GetBackups200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBackupsValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<GetBackups200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getKernel
     * @param kernelId ID of the Kernel to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Kernel object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getKernelCall(String kernelId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/kernels/{kernelId}"
            .replace("{" + "kernelId" + "}", localVarApiClient.escapeString(kernelId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getKernelValidateBeforeCall(String kernelId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'kernelId' is set
        if (kernelId == null) {
            throw new ApiException("Missing the required parameter 'kernelId' when calling getKernel(Async)");
        }

        return getKernelCall(kernelId, _callback);

    }

    /**
     * Kernel View
     * Returns information about a single Kernel. 
     * @param kernelId ID of the Kernel to look up. (required)
     * @return Kernel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Kernel object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Kernel getKernel(String kernelId) throws ApiException {
        ApiResponse<Kernel> localVarResp = getKernelWithHttpInfo(kernelId);
        return localVarResp.getData();
    }

    /**
     * Kernel View
     * Returns information about a single Kernel. 
     * @param kernelId ID of the Kernel to look up. (required)
     * @return ApiResponse&lt;Kernel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Kernel object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Kernel> getKernelWithHttpInfo(String kernelId) throws ApiException {
        okhttp3.Call localVarCall = getKernelValidateBeforeCall(kernelId, null);
        Type localVarReturnType = new TypeToken<Kernel>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kernel View (asynchronously)
     * Returns information about a single Kernel. 
     * @param kernelId ID of the Kernel to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Kernel object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getKernelAsync(String kernelId, final ApiCallback<Kernel> _callback) throws ApiException {

        okhttp3.Call localVarCall = getKernelValidateBeforeCall(kernelId, _callback);
        Type localVarReturnType = new TypeToken<Kernel>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getKernels
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Kernels. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getKernelsCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/kernels";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getKernelsValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getKernelsCall(page, pageSize, _callback);

    }

    /**
     * Kernels List
     * Lists available Kernels. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetKernels200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Kernels. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetKernels200Response getKernels(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetKernels200Response> localVarResp = getKernelsWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Kernels List
     * Lists available Kernels. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetKernels200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Kernels. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetKernels200Response> getKernelsWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getKernelsValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetKernels200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kernels List (asynchronously)
     * Lists available Kernels. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Kernels. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getKernelsAsync(Integer page, Integer pageSize, final ApiCallback<GetKernels200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getKernelsValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetKernels200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeConfig
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeConfigCall(Integer linodeId, Integer configId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/configs/{configId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeConfigValidateBeforeCall(Integer linodeId, Integer configId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling getLinodeConfig(Async)");
        }

        return getLinodeConfigCall(linodeId, configId, _callback);

    }

    /**
     * Configuration Profile View
     * Returns information about a specific Configuration profile. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @return LinodeConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LinodeConfig getLinodeConfig(Integer linodeId, Integer configId) throws ApiException {
        ApiResponse<LinodeConfig> localVarResp = getLinodeConfigWithHttpInfo(linodeId, configId);
        return localVarResp.getData();
    }

    /**
     * Configuration Profile View
     * Returns information about a specific Configuration profile. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @return ApiResponse&lt;LinodeConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LinodeConfig> getLinodeConfigWithHttpInfo(Integer linodeId, Integer configId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeConfigValidateBeforeCall(linodeId, configId, null);
        Type localVarReturnType = new TypeToken<LinodeConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Configuration Profile View (asynchronously)
     * Returns information about a specific Configuration profile. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Configuration profile object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeConfigAsync(Integer linodeId, Integer configId, final ApiCallback<LinodeConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeConfigValidateBeforeCall(linodeId, configId, _callback);
        Type localVarReturnType = new TypeToken<LinodeConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeConfigs
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Configuration profiles associated with this Linode.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeConfigsCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/configs"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeConfigsValidateBeforeCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeConfigs(Async)");
        }

        return getLinodeConfigsCall(linodeId, page, pageSize, _callback);

    }

    /**
     * Configuration Profiles List
     * Lists Configuration profiles associated with a Linode. 
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeConfigs200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Configuration profiles associated with this Linode.  </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeConfigs200Response getLinodeConfigs(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeConfigs200Response> localVarResp = getLinodeConfigsWithHttpInfo(linodeId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Configuration Profiles List
     * Lists Configuration profiles associated with a Linode. 
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeConfigs200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Configuration profiles associated with this Linode.  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeConfigs200Response> getLinodeConfigsWithHttpInfo(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getLinodeConfigsValidateBeforeCall(linodeId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeConfigs200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Configuration Profiles List (asynchronously)
     * Lists Configuration profiles associated with a Linode. 
     * @param linodeId ID of the Linode to look up Configuration profiles for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Configuration profiles associated with this Linode.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeConfigsAsync(Integer linodeId, Integer page, Integer pageSize, final ApiCallback<GetLinodeConfigs200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeConfigsValidateBeforeCall(linodeId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeConfigs200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeDisk
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeDiskCall(Integer linodeId, Integer diskId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks/{diskId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "diskId" + "}", localVarApiClient.escapeString(diskId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeDiskValidateBeforeCall(Integer linodeId, Integer diskId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeDisk(Async)");
        }

        // verify the required parameter 'diskId' is set
        if (diskId == null) {
            throw new ApiException("Missing the required parameter 'diskId' when calling getLinodeDisk(Async)");
        }

        return getLinodeDiskCall(linodeId, diskId, _callback);

    }

    /**
     * Disk View
     * View Disk information for a Disk associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @return Disk
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Disk getLinodeDisk(Integer linodeId, Integer diskId) throws ApiException {
        ApiResponse<Disk> localVarResp = getLinodeDiskWithHttpInfo(linodeId, diskId);
        return localVarResp.getData();
    }

    /**
     * Disk View
     * View Disk information for a Disk associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @return ApiResponse&lt;Disk&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Disk> getLinodeDiskWithHttpInfo(Integer linodeId, Integer diskId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeDiskValidateBeforeCall(linodeId, diskId, null);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk View (asynchronously)
     * View Disk information for a Disk associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeDiskAsync(Integer linodeId, Integer diskId, final ApiCallback<Disk> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeDiskValidateBeforeCall(linodeId, diskId, _callback);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeDisks
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of disks associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeDisksCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeDisksValidateBeforeCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeDisks(Async)");
        }

        return getLinodeDisksCall(linodeId, page, pageSize, _callback);

    }

    /**
     * Disks List
     * View Disk information for Disks associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeDisks200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of disks associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeDisks200Response getLinodeDisks(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeDisks200Response> localVarResp = getLinodeDisksWithHttpInfo(linodeId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Disks List
     * View Disk information for Disks associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeDisks200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of disks associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeDisks200Response> getLinodeDisksWithHttpInfo(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getLinodeDisksValidateBeforeCall(linodeId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeDisks200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disks List (asynchronously)
     * View Disk information for Disks associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of disks associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeDisksAsync(Integer linodeId, Integer page, Integer pageSize, final ApiCallback<GetLinodeDisks200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeDisksValidateBeforeCall(linodeId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeDisks200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeFirewalls
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of Firewalls associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeFirewallsCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/firewalls"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeFirewallsValidateBeforeCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeFirewalls(Async)");
        }

        return getLinodeFirewallsCall(linodeId, page, pageSize, _callback);

    }

    /**
     * Firewalls List
     * View Firewall information for Firewalls associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeFirewalls200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of Firewalls associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeFirewalls200Response getLinodeFirewalls(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeFirewalls200Response> localVarResp = getLinodeFirewallsWithHttpInfo(linodeId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Firewalls List
     * View Firewall information for Firewalls associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeFirewalls200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of Firewalls associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeFirewalls200Response> getLinodeFirewallsWithHttpInfo(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getLinodeFirewallsValidateBeforeCall(linodeId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeFirewalls200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewalls List (asynchronously)
     * View Firewall information for Firewalls associated with this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of Firewalls associated with this Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeFirewallsAsync(Integer linodeId, Integer page, Integer pageSize, final ApiCallback<GetLinodeFirewalls200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeFirewallsValidateBeforeCall(linodeId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeFirewalls200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeIP
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single IP address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeIPCall(Integer linodeId, String address, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/ips/{address}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "address" + "}", localVarApiClient.escapeString(address.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeIPValidateBeforeCall(Integer linodeId, String address, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeIP(Async)");
        }

        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling getLinodeIP(Async)");
        }

        return getLinodeIPCall(linodeId, address, _callback);

    }

    /**
     * IP Address View
     * View information about the specified IP address associated with the specified Linode. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @return IPAddress
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single IP address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPAddress getLinodeIP(Integer linodeId, String address) throws ApiException {
        ApiResponse<IPAddress> localVarResp = getLinodeIPWithHttpInfo(linodeId, address);
        return localVarResp.getData();
    }

    /**
     * IP Address View
     * View information about the specified IP address associated with the specified Linode. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @return ApiResponse&lt;IPAddress&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single IP address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPAddress> getLinodeIPWithHttpInfo(Integer linodeId, String address) throws ApiException {
        okhttp3.Call localVarCall = getLinodeIPValidateBeforeCall(linodeId, address, null);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Address View (asynchronously)
     * View information about the specified IP address associated with the specified Linode. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single IP address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeIPAsync(Integer linodeId, String address, final ApiCallback<IPAddress> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeIPValidateBeforeCall(linodeId, address, _callback);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeIPs
     * @param linodeId ID of the Linode to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Requested Linode&#39;s networking configuration. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeIPsCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/ips"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeIPsValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeIPs(Async)");
        }

        return getLinodeIPsCall(linodeId, _callback);

    }

    /**
     * Networking Information List
     * Returns networking information for a single Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @return GetLinodeIPs200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Requested Linode&#39;s networking configuration. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeIPs200Response getLinodeIPs(Integer linodeId) throws ApiException {
        ApiResponse<GetLinodeIPs200Response> localVarResp = getLinodeIPsWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Networking Information List
     * Returns networking information for a single Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @return ApiResponse&lt;GetLinodeIPs200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Requested Linode&#39;s networking configuration. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeIPs200Response> getLinodeIPsWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeIPsValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<GetLinodeIPs200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Networking Information List (asynchronously)
     * Returns networking information for a single Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Requested Linode&#39;s networking configuration. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeIPsAsync(Integer linodeId, final ApiCallback<GetLinodeIPs200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeIPsValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeIPs200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeInstance
     * @param linodeId ID of the Linode to look up (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Linode object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeInstanceCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeInstanceValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeInstance(Async)");
        }

        return getLinodeInstanceCall(linodeId, _callback);

    }

    /**
     * Linode View
     * Get a specific Linode by ID.
     * @param linodeId ID of the Linode to look up (required)
     * @return Linode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Linode object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Linode getLinodeInstance(Integer linodeId) throws ApiException {
        ApiResponse<Linode> localVarResp = getLinodeInstanceWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Linode View
     * Get a specific Linode by ID.
     * @param linodeId ID of the Linode to look up (required)
     * @return ApiResponse&lt;Linode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Linode object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Linode> getLinodeInstanceWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeInstanceValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode View (asynchronously)
     * Get a specific Linode by ID.
     * @param linodeId ID of the Linode to look up (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Linode object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeInstanceAsync(Integer linodeId, final ApiCallback<Linode> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeInstanceValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeInstances
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Linodes on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeInstancesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeInstancesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getLinodeInstancesCall(page, pageSize, _callback);

    }

    /**
     * Linodes List
     * Returns a paginated list of Linodes you have permission to view. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeInstances200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Linodes on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeInstances200Response getLinodeInstances(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeInstances200Response> localVarResp = getLinodeInstancesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Linodes List
     * Returns a paginated list of Linodes you have permission to view. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeInstances200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Linodes on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeInstances200Response> getLinodeInstancesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getLinodeInstancesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeInstances200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linodes List (asynchronously)
     * Returns a paginated list of Linodes you have permission to view. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Linodes on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeInstancesAsync(Integer page, Integer pageSize, final ApiCallback<GetLinodeInstances200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeInstancesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeInstances200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeNodeBalancers
     * @param linodeId ID of the Linode to look up (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of NodeBalancers. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeNodeBalancersCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/nodebalancers"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeNodeBalancersValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeNodeBalancers(Async)");
        }

        return getLinodeNodeBalancersCall(linodeId, _callback);

    }

    /**
     * Linode NodeBalancers View
     * Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User&#39;s Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 
     * @param linodeId ID of the Linode to look up (required)
     * @return GetLinodeNodeBalancers200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of NodeBalancers. </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeNodeBalancers200Response getLinodeNodeBalancers(Integer linodeId) throws ApiException {
        ApiResponse<GetLinodeNodeBalancers200Response> localVarResp = getLinodeNodeBalancersWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Linode NodeBalancers View
     * Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User&#39;s Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 
     * @param linodeId ID of the Linode to look up (required)
     * @return ApiResponse&lt;GetLinodeNodeBalancers200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of NodeBalancers. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeNodeBalancers200Response> getLinodeNodeBalancersWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeNodeBalancersValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<GetLinodeNodeBalancers200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode NodeBalancers View (asynchronously)
     * Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User&#39;s Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 
     * @param linodeId ID of the Linode to look up (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of NodeBalancers. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeNodeBalancersAsync(Integer linodeId, final ApiCallback<GetLinodeNodeBalancers200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeNodeBalancersValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeNodeBalancers200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeStats
     * @param linodeId ID of the Linode to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s stats for the past 24 hours. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeStatsCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/stats"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeStatsValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeStats(Async)");
        }

        return getLinodeStatsCall(linodeId, _callback);

    }

    /**
     * Linode Statistics View
     * Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 
     * @param linodeId ID of the Linode to look up. (required)
     * @return LinodeStats
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s stats for the past 24 hours. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LinodeStats getLinodeStats(Integer linodeId) throws ApiException {
        ApiResponse<LinodeStats> localVarResp = getLinodeStatsWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Linode Statistics View
     * Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 
     * @param linodeId ID of the Linode to look up. (required)
     * @return ApiResponse&lt;LinodeStats&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s stats for the past 24 hours. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LinodeStats> getLinodeStatsWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeStatsValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<LinodeStats>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Statistics View (asynchronously)
     * Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s stats for the past 24 hours. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeStatsAsync(Integer linodeId, final ApiCallback<LinodeStats> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeStatsValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<LinodeStats>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeStatsByYearMonth
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s statistics for the requested period. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeStatsByYearMonthCall(Integer linodeId, Integer year, Integer month, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/stats/{year}/{month}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "year" + "}", localVarApiClient.escapeString(year.toString()))
            .replace("{" + "month" + "}", localVarApiClient.escapeString(month.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeStatsByYearMonthValidateBeforeCall(Integer linodeId, Integer year, Integer month, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeStatsByYearMonth(Async)");
        }

        // verify the required parameter 'year' is set
        if (year == null) {
            throw new ApiException("Missing the required parameter 'year' when calling getLinodeStatsByYearMonth(Async)");
        }

        // verify the required parameter 'month' is set
        if (month == null) {
            throw new ApiException("Missing the required parameter 'month' when calling getLinodeStatsByYearMonth(Async)");
        }

        return getLinodeStatsByYearMonthCall(linodeId, year, month, _callback);

    }

    /**
     * Statistics View (year/month)
     * Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @return LinodeStats
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s statistics for the requested period. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LinodeStats getLinodeStatsByYearMonth(Integer linodeId, Integer year, Integer month) throws ApiException {
        ApiResponse<LinodeStats> localVarResp = getLinodeStatsByYearMonthWithHttpInfo(linodeId, year, month);
        return localVarResp.getData();
    }

    /**
     * Statistics View (year/month)
     * Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @return ApiResponse&lt;LinodeStats&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s statistics for the requested period. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LinodeStats> getLinodeStatsByYearMonthWithHttpInfo(Integer linodeId, Integer year, Integer month) throws ApiException {
        okhttp3.Call localVarCall = getLinodeStatsByYearMonthValidateBeforeCall(linodeId, year, month, null);
        Type localVarReturnType = new TypeToken<LinodeStats>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Statistics View (year/month) (asynchronously)
     * Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Linode&#39;s statistics for the requested period. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeStatsByYearMonthAsync(Integer linodeId, Integer year, Integer month, final ApiCallback<LinodeStats> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeStatsByYearMonthValidateBeforeCall(linodeId, year, month, _callback);
        Type localVarReturnType = new TypeToken<LinodeStats>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeTransfer
     * @param linodeId ID of the Linode to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeTransferCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/transfer"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeTransferValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeTransfer(Async)");
        }

        return getLinodeTransferCall(linodeId, _callback);

    }

    /**
     * Network Transfer View
     * Returns a Linode&#39;s network transfer pool statistics for the current month. 
     * @param linodeId ID of the Linode to look up. (required)
     * @return GetLinodeTransfer200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeTransfer200Response getLinodeTransfer(Integer linodeId) throws ApiException {
        ApiResponse<GetLinodeTransfer200Response> localVarResp = getLinodeTransferWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Network Transfer View
     * Returns a Linode&#39;s network transfer pool statistics for the current month. 
     * @param linodeId ID of the Linode to look up. (required)
     * @return ApiResponse&lt;GetLinodeTransfer200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeTransfer200Response> getLinodeTransferWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = getLinodeTransferValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<GetLinodeTransfer200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Network Transfer View (asynchronously)
     * Returns a Linode&#39;s network transfer pool statistics for the current month. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeTransferAsync(Integer linodeId, final ApiCallback<GetLinodeTransfer200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeTransferValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeTransfer200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeTransferByYearMonth
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics for the requested month.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeTransferByYearMonthCall(Integer linodeId, Integer year, Integer month, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/transfer/{year}/{month}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "year" + "}", localVarApiClient.escapeString(year.toString()))
            .replace("{" + "month" + "}", localVarApiClient.escapeString(month.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeTransferByYearMonthValidateBeforeCall(Integer linodeId, Integer year, Integer month, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeTransferByYearMonth(Async)");
        }

        // verify the required parameter 'year' is set
        if (year == null) {
            throw new ApiException("Missing the required parameter 'year' when calling getLinodeTransferByYearMonth(Async)");
        }

        // verify the required parameter 'month' is set
        if (month == null) {
            throw new ApiException("Missing the required parameter 'month' when calling getLinodeTransferByYearMonth(Async)");
        }

        return getLinodeTransferByYearMonthCall(linodeId, year, month, _callback);

    }

    /**
     * Network Transfer View (year/month)
     * Returns a Linode&#39;s network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @return GetLinodeTransferByYearMonth200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics for the requested month.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeTransferByYearMonth200Response getLinodeTransferByYearMonth(Integer linodeId, Integer year, Integer month) throws ApiException {
        ApiResponse<GetLinodeTransferByYearMonth200Response> localVarResp = getLinodeTransferByYearMonthWithHttpInfo(linodeId, year, month);
        return localVarResp.getData();
    }

    /**
     * Network Transfer View (year/month)
     * Returns a Linode&#39;s network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @return ApiResponse&lt;GetLinodeTransferByYearMonth200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics for the requested month.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeTransferByYearMonth200Response> getLinodeTransferByYearMonthWithHttpInfo(Integer linodeId, Integer year, Integer month) throws ApiException {
        okhttp3.Call localVarCall = getLinodeTransferByYearMonthValidateBeforeCall(linodeId, year, month, null);
        Type localVarReturnType = new TypeToken<GetLinodeTransferByYearMonth200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Network Transfer View (year/month) (asynchronously)
     * Returns a Linode&#39;s network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param year Numeric value representing the year to look up. (required)
     * @param month Numeric value representing the month to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A collection of the specified Linode&#39;s network transfer statistics for the requested month.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeTransferByYearMonthAsync(Integer linodeId, Integer year, Integer month, final ApiCallback<GetLinodeTransferByYearMonth200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeTransferByYearMonthValidateBeforeCall(linodeId, year, month, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeTransferByYearMonth200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinodeVolumes
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Block Storage Volumes attached to this Linode.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeVolumesCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/volumes"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLinodeVolumesValidateBeforeCall(Integer linodeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling getLinodeVolumes(Async)");
        }

        return getLinodeVolumesCall(linodeId, page, pageSize, _callback);

    }

    /**
     * Linode&#39;s Volumes List
     * View Block Storage Volumes attached to this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeVolumes200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Block Storage Volumes attached to this Linode.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeVolumes200Response getLinodeVolumes(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeVolumes200Response> localVarResp = getLinodeVolumesWithHttpInfo(linodeId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Linode&#39;s Volumes List
     * View Block Storage Volumes attached to this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeVolumes200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Block Storage Volumes attached to this Linode.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeVolumes200Response> getLinodeVolumesWithHttpInfo(Integer linodeId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getLinodeVolumesValidateBeforeCall(linodeId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeVolumes200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode&#39;s Volumes List (asynchronously)
     * View Block Storage Volumes attached to this Linode. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Block Storage Volumes attached to this Linode.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinodeVolumesAsync(Integer linodeId, Integer page, Integer pageSize, final ApiCallback<GetLinodeVolumes200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinodeVolumesValidateBeforeCall(linodeId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeVolumes200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for migrateLinodeInstance
     * @param linodeId ID of the Linode to migrate. (required)
     * @param migrateLinodeInstanceRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Scheduled migration started </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call migrateLinodeInstanceCall(Integer linodeId, MigrateLinodeInstanceRequest migrateLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = migrateLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/migrate"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call migrateLinodeInstanceValidateBeforeCall(Integer linodeId, MigrateLinodeInstanceRequest migrateLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling migrateLinodeInstance(Async)");
        }

        return migrateLinodeInstanceCall(linodeId, migrateLinodeInstanceRequest, _callback);

    }

    /**
     * DC Migration/Pending Host Migration Initiate
     * Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a &#x60;region&#x60; parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 &#x60;/116&#x60; pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 
     * @param linodeId ID of the Linode to migrate. (required)
     * @param migrateLinodeInstanceRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Scheduled migration started </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object migrateLinodeInstance(Integer linodeId, MigrateLinodeInstanceRequest migrateLinodeInstanceRequest) throws ApiException {
        ApiResponse<Object> localVarResp = migrateLinodeInstanceWithHttpInfo(linodeId, migrateLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * DC Migration/Pending Host Migration Initiate
     * Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a &#x60;region&#x60; parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 &#x60;/116&#x60; pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 
     * @param linodeId ID of the Linode to migrate. (required)
     * @param migrateLinodeInstanceRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Scheduled migration started </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> migrateLinodeInstanceWithHttpInfo(Integer linodeId, MigrateLinodeInstanceRequest migrateLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = migrateLinodeInstanceValidateBeforeCall(linodeId, migrateLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * DC Migration/Pending Host Migration Initiate (asynchronously)
     * Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a &#x60;region&#x60; parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 &#x60;/116&#x60; pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 
     * @param linodeId ID of the Linode to migrate. (required)
     * @param migrateLinodeInstanceRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Scheduled migration started </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call migrateLinodeInstanceAsync(Integer linodeId, MigrateLinodeInstanceRequest migrateLinodeInstanceRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = migrateLinodeInstanceValidateBeforeCall(linodeId, migrateLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for mutateLinodeInstance
     * @param linodeId ID of the Linode to mutate. (required)
     * @param mutateLinodeInstanceRequest Whether to automatically resize disks or not. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Mutate started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call mutateLinodeInstanceCall(Integer linodeId, MutateLinodeInstanceRequest mutateLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = mutateLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/mutate"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call mutateLinodeInstanceValidateBeforeCall(Integer linodeId, MutateLinodeInstanceRequest mutateLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling mutateLinodeInstance(Async)");
        }

        return mutateLinodeInstanceCall(linodeId, mutateLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Upgrade
     * Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 
     * @param linodeId ID of the Linode to mutate. (required)
     * @param mutateLinodeInstanceRequest Whether to automatically resize disks or not. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Mutate started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object mutateLinodeInstance(Integer linodeId, MutateLinodeInstanceRequest mutateLinodeInstanceRequest) throws ApiException {
        ApiResponse<Object> localVarResp = mutateLinodeInstanceWithHttpInfo(linodeId, mutateLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Upgrade
     * Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 
     * @param linodeId ID of the Linode to mutate. (required)
     * @param mutateLinodeInstanceRequest Whether to automatically resize disks or not. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Mutate started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> mutateLinodeInstanceWithHttpInfo(Integer linodeId, MutateLinodeInstanceRequest mutateLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = mutateLinodeInstanceValidateBeforeCall(linodeId, mutateLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Upgrade (asynchronously)
     * Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 
     * @param linodeId ID of the Linode to mutate. (required)
     * @param mutateLinodeInstanceRequest Whether to automatically resize disks or not. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Mutate started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call mutateLinodeInstanceAsync(Integer linodeId, MutateLinodeInstanceRequest mutateLinodeInstanceRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = mutateLinodeInstanceValidateBeforeCall(linodeId, mutateLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for rebootLinodeInstance
     * @param linodeId ID of the linode to reboot. (required)
     * @param rebootLinodeInstanceRequest Optional reboot parameters. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reboot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rebootLinodeInstanceCall(Integer linodeId, RebootLinodeInstanceRequest rebootLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = rebootLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/reboot"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call rebootLinodeInstanceValidateBeforeCall(Integer linodeId, RebootLinodeInstanceRequest rebootLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling rebootLinodeInstance(Async)");
        }

        return rebootLinodeInstanceCall(linodeId, rebootLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Reboot
     * Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 
     * @param linodeId ID of the linode to reboot. (required)
     * @param rebootLinodeInstanceRequest Optional reboot parameters. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reboot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object rebootLinodeInstance(Integer linodeId, RebootLinodeInstanceRequest rebootLinodeInstanceRequest) throws ApiException {
        ApiResponse<Object> localVarResp = rebootLinodeInstanceWithHttpInfo(linodeId, rebootLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Reboot
     * Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 
     * @param linodeId ID of the linode to reboot. (required)
     * @param rebootLinodeInstanceRequest Optional reboot parameters. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reboot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> rebootLinodeInstanceWithHttpInfo(Integer linodeId, RebootLinodeInstanceRequest rebootLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = rebootLinodeInstanceValidateBeforeCall(linodeId, rebootLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Reboot (asynchronously)
     * Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 
     * @param linodeId ID of the linode to reboot. (required)
     * @param rebootLinodeInstanceRequest Optional reboot parameters. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reboot started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rebootLinodeInstanceAsync(Integer linodeId, RebootLinodeInstanceRequest rebootLinodeInstanceRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = rebootLinodeInstanceValidateBeforeCall(linodeId, rebootLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for rebuildLinodeInstance
     * @param linodeId ID of the Linode to rebuild. (required)
     * @param UNKNOWN_BASE_TYPE The requested state your Linode will be rebuilt into. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rebuild started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rebuildLinodeInstanceCall(Integer linodeId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = UNKNOWN_BASE_TYPE;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/rebuild"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call rebuildLinodeInstanceValidateBeforeCall(Integer linodeId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling rebuildLinodeInstance(Async)");
        }

        // verify the required parameter 'UNKNOWN_BASE_TYPE' is set
        if (UNKNOWN_BASE_TYPE == null) {
            throw new ApiException("Missing the required parameter 'UNKNOWN_BASE_TYPE' when calling rebuildLinodeInstance(Async)");
        }

        return rebuildLinodeInstanceCall(linodeId, UNKNOWN_BASE_TYPE, _callback);

    }

    /**
     * Linode Rebuild
     * Rebuilds a Linode you have the &#x60;read_write&#x60; permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new &#x60;image&#x60; to the Linode with the given attributes. Additionally:    * Requires an &#x60;image&#x60; be supplied.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the     &#x60;authorized_keys&#x60; field. 
     * @param linodeId ID of the Linode to rebuild. (required)
     * @param UNKNOWN_BASE_TYPE The requested state your Linode will be rebuilt into. (required)
     * @return Linode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rebuild started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Linode rebuildLinodeInstance(Integer linodeId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) throws ApiException {
        ApiResponse<Linode> localVarResp = rebuildLinodeInstanceWithHttpInfo(linodeId, UNKNOWN_BASE_TYPE);
        return localVarResp.getData();
    }

    /**
     * Linode Rebuild
     * Rebuilds a Linode you have the &#x60;read_write&#x60; permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new &#x60;image&#x60; to the Linode with the given attributes. Additionally:    * Requires an &#x60;image&#x60; be supplied.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the     &#x60;authorized_keys&#x60; field. 
     * @param linodeId ID of the Linode to rebuild. (required)
     * @param UNKNOWN_BASE_TYPE The requested state your Linode will be rebuilt into. (required)
     * @return ApiResponse&lt;Linode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rebuild started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Linode> rebuildLinodeInstanceWithHttpInfo(Integer linodeId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) throws ApiException {
        okhttp3.Call localVarCall = rebuildLinodeInstanceValidateBeforeCall(linodeId, UNKNOWN_BASE_TYPE, null);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Rebuild (asynchronously)
     * Rebuilds a Linode you have the &#x60;read_write&#x60; permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new &#x60;image&#x60; to the Linode with the given attributes. Additionally:    * Requires an &#x60;image&#x60; be supplied.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the     &#x60;authorized_keys&#x60; field. 
     * @param linodeId ID of the Linode to rebuild. (required)
     * @param UNKNOWN_BASE_TYPE The requested state your Linode will be rebuilt into. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rebuild started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rebuildLinodeInstanceAsync(Integer linodeId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback<Linode> _callback) throws ApiException {

        okhttp3.Call localVarCall = rebuildLinodeInstanceValidateBeforeCall(linodeId, UNKNOWN_BASE_TYPE, _callback);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for removeLinodeIP
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address successfully removed. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeLinodeIPCall(Integer linodeId, String address, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/ips/{address}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "address" + "}", localVarApiClient.escapeString(address.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call removeLinodeIPValidateBeforeCall(Integer linodeId, String address, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling removeLinodeIP(Async)");
        }

        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling removeLinodeIP(Async)");
        }

        return removeLinodeIPCall(linodeId, address, _callback);

    }

    /**
     * IPv4 Address Delete
     * Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode&#39;s last remaining public IPv4 address. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address successfully removed. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object removeLinodeIP(Integer linodeId, String address) throws ApiException {
        ApiResponse<Object> localVarResp = removeLinodeIPWithHttpInfo(linodeId, address);
        return localVarResp.getData();
    }

    /**
     * IPv4 Address Delete
     * Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode&#39;s last remaining public IPv4 address. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address successfully removed. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> removeLinodeIPWithHttpInfo(Integer linodeId, String address) throws ApiException {
        okhttp3.Call localVarCall = removeLinodeIPValidateBeforeCall(linodeId, address, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv4 Address Delete (asynchronously)
     * Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode&#39;s last remaining public IPv4 address. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP address successfully removed. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeLinodeIPAsync(Integer linodeId, String address, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = removeLinodeIPValidateBeforeCall(linodeId, address, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for rescueLinodeInstance
     * @param linodeId ID of the Linode to rescue. (required)
     * @param rescueLinodeInstanceRequest Optional object of devices to be mounted. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rescue started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rescueLinodeInstanceCall(Integer linodeId, RescueLinodeInstanceRequest rescueLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = rescueLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/rescue"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call rescueLinodeInstanceValidateBeforeCall(Integer linodeId, RescueLinodeInstanceRequest rescueLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling rescueLinodeInstance(Async)");
        }

        return rescueLinodeInstanceCall(linodeId, rescueLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Boot into Rescue Mode
     * Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \&quot;sdh\&quot; is reserved and unavailable during rescue. 
     * @param linodeId ID of the Linode to rescue. (required)
     * @param rescueLinodeInstanceRequest Optional object of devices to be mounted. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rescue started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object rescueLinodeInstance(Integer linodeId, RescueLinodeInstanceRequest rescueLinodeInstanceRequest) throws ApiException {
        ApiResponse<Object> localVarResp = rescueLinodeInstanceWithHttpInfo(linodeId, rescueLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Boot into Rescue Mode
     * Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \&quot;sdh\&quot; is reserved and unavailable during rescue. 
     * @param linodeId ID of the Linode to rescue. (required)
     * @param rescueLinodeInstanceRequest Optional object of devices to be mounted. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rescue started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> rescueLinodeInstanceWithHttpInfo(Integer linodeId, RescueLinodeInstanceRequest rescueLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = rescueLinodeInstanceValidateBeforeCall(linodeId, rescueLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Boot into Rescue Mode (asynchronously)
     * Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \&quot;sdh\&quot; is reserved and unavailable during rescue. 
     * @param linodeId ID of the Linode to rescue. (required)
     * @param rescueLinodeInstanceRequest Optional object of devices to be mounted. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rescue started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rescueLinodeInstanceAsync(Integer linodeId, RescueLinodeInstanceRequest rescueLinodeInstanceRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = rescueLinodeInstanceValidateBeforeCall(linodeId, rescueLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resetDiskPassword
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resetDiskPasswordRequest The new password. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetDiskPasswordCall(Integer linodeId, Integer diskId, ResetDiskPasswordRequest resetDiskPasswordRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = resetDiskPasswordRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks/{diskId}/password"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "diskId" + "}", localVarApiClient.escapeString(diskId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resetDiskPasswordValidateBeforeCall(Integer linodeId, Integer diskId, ResetDiskPasswordRequest resetDiskPasswordRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling resetDiskPassword(Async)");
        }

        // verify the required parameter 'diskId' is set
        if (diskId == null) {
            throw new ApiException("Missing the required parameter 'diskId' when calling resetDiskPassword(Async)");
        }

        // verify the required parameter 'resetDiskPasswordRequest' is set
        if (resetDiskPasswordRequest == null) {
            throw new ApiException("Missing the required parameter 'resetDiskPasswordRequest' when calling resetDiskPassword(Async)");
        }

        return resetDiskPasswordCall(linodeId, diskId, resetDiskPasswordRequest, _callback);

    }

    /**
     * Disk Root Password Reset
     * Resets the password of a Disk you have permission to &#x60;read_write&#x60;. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resetDiskPasswordRequest The new password. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object resetDiskPassword(Integer linodeId, Integer diskId, ResetDiskPasswordRequest resetDiskPasswordRequest) throws ApiException {
        ApiResponse<Object> localVarResp = resetDiskPasswordWithHttpInfo(linodeId, diskId, resetDiskPasswordRequest);
        return localVarResp.getData();
    }

    /**
     * Disk Root Password Reset
     * Resets the password of a Disk you have permission to &#x60;read_write&#x60;. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resetDiskPasswordRequest The new password. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> resetDiskPasswordWithHttpInfo(Integer linodeId, Integer diskId, ResetDiskPasswordRequest resetDiskPasswordRequest) throws ApiException {
        okhttp3.Call localVarCall = resetDiskPasswordValidateBeforeCall(linodeId, diskId, resetDiskPasswordRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk Root Password Reset (asynchronously)
     * Resets the password of a Disk you have permission to &#x60;read_write&#x60;. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resetDiskPasswordRequest The new password. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Disk object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetDiskPasswordAsync(Integer linodeId, Integer diskId, ResetDiskPasswordRequest resetDiskPasswordRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = resetDiskPasswordValidateBeforeCall(linodeId, diskId, resetDiskPasswordRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resetLinodePassword
     * @param linodeId ID of the Linode for which to reset its root password. (required)
     * @param resetLinodePasswordRequest This Linode&#39;s new root password. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Password Reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetLinodePasswordCall(Integer linodeId, ResetLinodePasswordRequest resetLinodePasswordRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = resetLinodePasswordRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/password"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resetLinodePasswordValidateBeforeCall(Integer linodeId, ResetLinodePasswordRequest resetLinodePasswordRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling resetLinodePassword(Async)");
        }

        return resetLinodePasswordCall(linodeId, resetLinodePasswordRequest, _callback);

    }

    /**
     * Linode Root Password Reset
     * Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk&#39;s root password. * A &#x60;password_reset&#x60; event is generated when a root password reset is successful. 
     * @param linodeId ID of the Linode for which to reset its root password. (required)
     * @param resetLinodePasswordRequest This Linode&#39;s new root password. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Password Reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object resetLinodePassword(Integer linodeId, ResetLinodePasswordRequest resetLinodePasswordRequest) throws ApiException {
        ApiResponse<Object> localVarResp = resetLinodePasswordWithHttpInfo(linodeId, resetLinodePasswordRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Root Password Reset
     * Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk&#39;s root password. * A &#x60;password_reset&#x60; event is generated when a root password reset is successful. 
     * @param linodeId ID of the Linode for which to reset its root password. (required)
     * @param resetLinodePasswordRequest This Linode&#39;s new root password. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Password Reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> resetLinodePasswordWithHttpInfo(Integer linodeId, ResetLinodePasswordRequest resetLinodePasswordRequest) throws ApiException {
        okhttp3.Call localVarCall = resetLinodePasswordValidateBeforeCall(linodeId, resetLinodePasswordRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Root Password Reset (asynchronously)
     * Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk&#39;s root password. * A &#x60;password_reset&#x60; event is generated when a root password reset is successful. 
     * @param linodeId ID of the Linode for which to reset its root password. (required)
     * @param resetLinodePasswordRequest This Linode&#39;s new root password. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Password Reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resetLinodePasswordAsync(Integer linodeId, ResetLinodePasswordRequest resetLinodePasswordRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = resetLinodePasswordValidateBeforeCall(linodeId, resetLinodePasswordRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resizeDisk
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resizeDiskRequest The new size of the Disk. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resizeDiskCall(Integer linodeId, Integer diskId, ResizeDiskRequest resizeDiskRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = resizeDiskRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks/{diskId}/resize"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "diskId" + "}", localVarApiClient.escapeString(diskId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resizeDiskValidateBeforeCall(Integer linodeId, Integer diskId, ResizeDiskRequest resizeDiskRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling resizeDisk(Async)");
        }

        // verify the required parameter 'diskId' is set
        if (diskId == null) {
            throw new ApiException("Missing the required parameter 'diskId' when calling resizeDisk(Async)");
        }

        // verify the required parameter 'resizeDiskRequest' is set
        if (resizeDiskRequest == null) {
            throw new ApiException("Missing the required parameter 'resizeDiskRequest' when calling resizeDisk(Async)");
        }

        return resizeDiskCall(linodeId, diskId, resizeDiskRequest, _callback);

    }

    /**
     * Disk Resize
     * Resizes a Disk you have permission to &#x60;read_write&#x60;.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode&#39;s active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resizeDiskRequest The new size of the Disk. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object resizeDisk(Integer linodeId, Integer diskId, ResizeDiskRequest resizeDiskRequest) throws ApiException {
        ApiResponse<Object> localVarResp = resizeDiskWithHttpInfo(linodeId, diskId, resizeDiskRequest);
        return localVarResp.getData();
    }

    /**
     * Disk Resize
     * Resizes a Disk you have permission to &#x60;read_write&#x60;.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode&#39;s active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resizeDiskRequest The new size of the Disk. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> resizeDiskWithHttpInfo(Integer linodeId, Integer diskId, ResizeDiskRequest resizeDiskRequest) throws ApiException {
        okhttp3.Call localVarCall = resizeDiskValidateBeforeCall(linodeId, diskId, resizeDiskRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk Resize (asynchronously)
     * Resizes a Disk you have permission to &#x60;read_write&#x60;.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode&#39;s active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param resizeDiskRequest The new size of the Disk. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resizeDiskAsync(Integer linodeId, Integer diskId, ResizeDiskRequest resizeDiskRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = resizeDiskValidateBeforeCall(linodeId, diskId, resizeDiskRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resizeLinodeInstance
     * @param linodeId ID of the Linode to resize. (required)
     * @param resizeLinodeInstanceRequest The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode&#39;s disks.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resizeLinodeInstanceCall(Integer linodeId, ResizeLinodeInstanceRequest resizeLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = resizeLinodeInstanceRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/resize"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resizeLinodeInstanceValidateBeforeCall(Integer linodeId, ResizeLinodeInstanceRequest resizeLinodeInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling resizeLinodeInstance(Async)");
        }

        // verify the required parameter 'resizeLinodeInstanceRequest' is set
        if (resizeLinodeInstanceRequest == null) {
            throw new ApiException("Missing the required parameter 'resizeLinodeInstanceRequest' when calling resizeLinodeInstance(Async)");
        }

        return resizeLinodeInstanceCall(linodeId, resizeLinodeInstanceRequest, _callback);

    }

    /**
     * Linode Resize
     * Resizes a Linode you have the &#x60;read_write&#x60; permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 
     * @param linodeId ID of the Linode to resize. (required)
     * @param resizeLinodeInstanceRequest The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode&#39;s disks.  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object resizeLinodeInstance(Integer linodeId, ResizeLinodeInstanceRequest resizeLinodeInstanceRequest) throws ApiException {
        ApiResponse<Object> localVarResp = resizeLinodeInstanceWithHttpInfo(linodeId, resizeLinodeInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Linode Resize
     * Resizes a Linode you have the &#x60;read_write&#x60; permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 
     * @param linodeId ID of the Linode to resize. (required)
     * @param resizeLinodeInstanceRequest The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode&#39;s disks.  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> resizeLinodeInstanceWithHttpInfo(Integer linodeId, ResizeLinodeInstanceRequest resizeLinodeInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = resizeLinodeInstanceValidateBeforeCall(linodeId, resizeLinodeInstanceRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Resize (asynchronously)
     * Resizes a Linode you have the &#x60;read_write&#x60; permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 
     * @param linodeId ID of the Linode to resize. (required)
     * @param resizeLinodeInstanceRequest The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode&#39;s disks.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resize started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resizeLinodeInstanceAsync(Integer linodeId, ResizeLinodeInstanceRequest resizeLinodeInstanceRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = resizeLinodeInstanceValidateBeforeCall(linodeId, resizeLinodeInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for restoreBackup
     * @param linodeId The ID of the Linode that the Backup belongs to. (required)
     * @param backupId The ID of the Backup to restore. (required)
     * @param restoreBackupRequest Parameters to provide when restoring the Backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Restore from Backup was initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call restoreBackupCall(Integer linodeId, Integer backupId, RestoreBackupRequest restoreBackupRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = restoreBackupRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/backups/{backupId}/restore"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "backupId" + "}", localVarApiClient.escapeString(backupId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call restoreBackupValidateBeforeCall(Integer linodeId, Integer backupId, RestoreBackupRequest restoreBackupRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling restoreBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling restoreBackup(Async)");
        }

        // verify the required parameter 'restoreBackupRequest' is set
        if (restoreBackupRequest == null) {
            throw new ApiException("Missing the required parameter 'restoreBackupRequest' when calling restoreBackup(Async)");
        }

        return restoreBackupCall(linodeId, backupId, restoreBackupRequest, _callback);

    }

    /**
     * Backup Restore
     * Restores a Linode&#39;s Backup to the specified Linode. 
     * @param linodeId The ID of the Linode that the Backup belongs to. (required)
     * @param backupId The ID of the Backup to restore. (required)
     * @param restoreBackupRequest Parameters to provide when restoring the Backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Restore from Backup was initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object restoreBackup(Integer linodeId, Integer backupId, RestoreBackupRequest restoreBackupRequest) throws ApiException {
        ApiResponse<Object> localVarResp = restoreBackupWithHttpInfo(linodeId, backupId, restoreBackupRequest);
        return localVarResp.getData();
    }

    /**
     * Backup Restore
     * Restores a Linode&#39;s Backup to the specified Linode. 
     * @param linodeId The ID of the Linode that the Backup belongs to. (required)
     * @param backupId The ID of the Backup to restore. (required)
     * @param restoreBackupRequest Parameters to provide when restoring the Backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Restore from Backup was initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> restoreBackupWithHttpInfo(Integer linodeId, Integer backupId, RestoreBackupRequest restoreBackupRequest) throws ApiException {
        okhttp3.Call localVarCall = restoreBackupValidateBeforeCall(linodeId, backupId, restoreBackupRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Backup Restore (asynchronously)
     * Restores a Linode&#39;s Backup to the specified Linode. 
     * @param linodeId The ID of the Linode that the Backup belongs to. (required)
     * @param backupId The ID of the Backup to restore. (required)
     * @param restoreBackupRequest Parameters to provide when restoring the Backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Restore from Backup was initiated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call restoreBackupAsync(Integer linodeId, Integer backupId, RestoreBackupRequest restoreBackupRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = restoreBackupValidateBeforeCall(linodeId, backupId, restoreBackupRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for shutdownLinodeInstance
     * @param linodeId ID of the Linode to shutdown. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Shutdown started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call shutdownLinodeInstanceCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/shutdown"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call shutdownLinodeInstanceValidateBeforeCall(Integer linodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling shutdownLinodeInstance(Async)");
        }

        return shutdownLinodeInstanceCall(linodeId, _callback);

    }

    /**
     * Linode Shut Down
     * Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 
     * @param linodeId ID of the Linode to shutdown. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Shutdown started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object shutdownLinodeInstance(Integer linodeId) throws ApiException {
        ApiResponse<Object> localVarResp = shutdownLinodeInstanceWithHttpInfo(linodeId);
        return localVarResp.getData();
    }

    /**
     * Linode Shut Down
     * Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 
     * @param linodeId ID of the Linode to shutdown. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Shutdown started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> shutdownLinodeInstanceWithHttpInfo(Integer linodeId) throws ApiException {
        okhttp3.Call localVarCall = shutdownLinodeInstanceValidateBeforeCall(linodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Shut Down (asynchronously)
     * Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 
     * @param linodeId ID of the Linode to shutdown. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Shutdown started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call shutdownLinodeInstanceAsync(Integer linodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = shutdownLinodeInstanceValidateBeforeCall(linodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateDisk
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param disk Updates the parameters of a single Disk.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Disk. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDiskCall(Integer linodeId, Integer diskId, Disk disk, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = disk;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/disks/{diskId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "diskId" + "}", localVarApiClient.escapeString(diskId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateDiskValidateBeforeCall(Integer linodeId, Integer diskId, Disk disk, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling updateDisk(Async)");
        }

        // verify the required parameter 'diskId' is set
        if (diskId == null) {
            throw new ApiException("Missing the required parameter 'diskId' when calling updateDisk(Async)");
        }

        // verify the required parameter 'disk' is set
        if (disk == null) {
            throw new ApiException("Missing the required parameter 'disk' when calling updateDisk(Async)");
        }

        return updateDiskCall(linodeId, diskId, disk, _callback);

    }

    /**
     * Disk Update
     * Updates a Disk that you have permission to &#x60;read_write&#x60;. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param disk Updates the parameters of a single Disk.  (required)
     * @return Disk
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Disk. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Disk updateDisk(Integer linodeId, Integer diskId, Disk disk) throws ApiException {
        ApiResponse<Disk> localVarResp = updateDiskWithHttpInfo(linodeId, diskId, disk);
        return localVarResp.getData();
    }

    /**
     * Disk Update
     * Updates a Disk that you have permission to &#x60;read_write&#x60;. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param disk Updates the parameters of a single Disk.  (required)
     * @return ApiResponse&lt;Disk&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Disk. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Disk> updateDiskWithHttpInfo(Integer linodeId, Integer diskId, Disk disk) throws ApiException {
        okhttp3.Call localVarCall = updateDiskValidateBeforeCall(linodeId, diskId, disk, null);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disk Update (asynchronously)
     * Updates a Disk that you have permission to &#x60;read_write&#x60;. 
     * @param linodeId ID of the Linode to look up. (required)
     * @param diskId ID of the Disk to look up. (required)
     * @param disk Updates the parameters of a single Disk.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Disk. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDiskAsync(Integer linodeId, Integer diskId, Disk disk, final ApiCallback<Disk> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateDiskValidateBeforeCall(linodeId, diskId, disk, _callback);
        Type localVarReturnType = new TypeToken<Disk>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateLinodeConfig
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param linodeConfig The Configuration profile parameters to modify. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLinodeConfigCall(Integer linodeId, Integer configId, LinodeConfig linodeConfig, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = linodeConfig;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/configs/{configId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateLinodeConfigValidateBeforeCall(Integer linodeId, Integer configId, LinodeConfig linodeConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling updateLinodeConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling updateLinodeConfig(Async)");
        }

        // verify the required parameter 'linodeConfig' is set
        if (linodeConfig == null) {
            throw new ApiException("Missing the required parameter 'linodeConfig' when calling updateLinodeConfig(Async)");
        }

        return updateLinodeConfigCall(linodeId, configId, linodeConfig, _callback);

    }

    /**
     * Configuration Profile Update
     * Updates a Configuration profile. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param linodeConfig The Configuration profile parameters to modify. (required)
     * @return LinodeConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LinodeConfig updateLinodeConfig(Integer linodeId, Integer configId, LinodeConfig linodeConfig) throws ApiException {
        ApiResponse<LinodeConfig> localVarResp = updateLinodeConfigWithHttpInfo(linodeId, configId, linodeConfig);
        return localVarResp.getData();
    }

    /**
     * Configuration Profile Update
     * Updates a Configuration profile. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param linodeConfig The Configuration profile parameters to modify. (required)
     * @return ApiResponse&lt;LinodeConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LinodeConfig> updateLinodeConfigWithHttpInfo(Integer linodeId, Integer configId, LinodeConfig linodeConfig) throws ApiException {
        okhttp3.Call localVarCall = updateLinodeConfigValidateBeforeCall(linodeId, configId, linodeConfig, null);
        Type localVarReturnType = new TypeToken<LinodeConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Configuration Profile Update (asynchronously)
     * Updates a Configuration profile. 
     * @param linodeId The ID of the Linode whose Configuration profile to look up. (required)
     * @param configId The ID of the Configuration profile to look up. (required)
     * @param linodeConfig The Configuration profile parameters to modify. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Configuration profile successfully updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLinodeConfigAsync(Integer linodeId, Integer configId, LinodeConfig linodeConfig, final ApiCallback<LinodeConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateLinodeConfigValidateBeforeCall(linodeId, configId, linodeConfig, _callback);
        Type localVarReturnType = new TypeToken<LinodeConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateLinodeIP
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param updateLinodeIPRequest The information to update for the IP address. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated IP address record. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLinodeIPCall(Integer linodeId, String address, UpdateLinodeIPRequest updateLinodeIPRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateLinodeIPRequest;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}/ips/{address}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()))
            .replace("{" + "address" + "}", localVarApiClient.escapeString(address.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateLinodeIPValidateBeforeCall(Integer linodeId, String address, UpdateLinodeIPRequest updateLinodeIPRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling updateLinodeIP(Async)");
        }

        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling updateLinodeIP(Async)");
        }

        return updateLinodeIPCall(linodeId, address, updateLinodeIPRequest, _callback);

    }

    /**
     * IP Address Update
     * Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to &#x60;null&#x60; for a public IPv4 address, resets it to the default \&quot;ip.linodeusercontent.com\&quot; RDNS value. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param updateLinodeIPRequest The information to update for the IP address. (optional)
     * @return IPAddress
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated IP address record. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPAddress updateLinodeIP(Integer linodeId, String address, UpdateLinodeIPRequest updateLinodeIPRequest) throws ApiException {
        ApiResponse<IPAddress> localVarResp = updateLinodeIPWithHttpInfo(linodeId, address, updateLinodeIPRequest);
        return localVarResp.getData();
    }

    /**
     * IP Address Update
     * Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to &#x60;null&#x60; for a public IPv4 address, resets it to the default \&quot;ip.linodeusercontent.com\&quot; RDNS value. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param updateLinodeIPRequest The information to update for the IP address. (optional)
     * @return ApiResponse&lt;IPAddress&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated IP address record. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPAddress> updateLinodeIPWithHttpInfo(Integer linodeId, String address, UpdateLinodeIPRequest updateLinodeIPRequest) throws ApiException {
        okhttp3.Call localVarCall = updateLinodeIPValidateBeforeCall(linodeId, address, updateLinodeIPRequest, null);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Address Update (asynchronously)
     * Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to &#x60;null&#x60; for a public IPv4 address, resets it to the default \&quot;ip.linodeusercontent.com\&quot; RDNS value. 
     * @param linodeId The ID of the Linode to look up. (required)
     * @param address The IP address to look up. (required)
     * @param updateLinodeIPRequest The information to update for the IP address. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated IP address record. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLinodeIPAsync(Integer linodeId, String address, UpdateLinodeIPRequest updateLinodeIPRequest, final ApiCallback<IPAddress> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateLinodeIPValidateBeforeCall(linodeId, address, updateLinodeIPRequest, _callback);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateLinodeInstance
     * @param linodeId ID of the Linode to look up (required)
     * @param linode Any field that is not marked as &#x60;readOnly&#x60; may be updated. Fields that are marked &#x60;readOnly&#x60; will be ignored. If any updated field fails to pass validation, the Linode will not be updated.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLinodeInstanceCall(Integer linodeId, Linode linode, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = linode;

        // create path and map variables
        String localVarPath = "/linode/instances/{linodeId}"
            .replace("{" + "linodeId" + "}", localVarApiClient.escapeString(linodeId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "personalAccessToken", "oauth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateLinodeInstanceValidateBeforeCall(Integer linodeId, Linode linode, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'linodeId' is set
        if (linodeId == null) {
            throw new ApiException("Missing the required parameter 'linodeId' when calling updateLinodeInstance(Async)");
        }

        // verify the required parameter 'linode' is set
        if (linode == null) {
            throw new ApiException("Missing the required parameter 'linode' when calling updateLinodeInstance(Async)");
        }

        return updateLinodeInstanceCall(linodeId, linode, _callback);

    }

    /**
     * Linode Update
     * Updates a Linode that you have permission to &#x60;read_write&#x60;.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param linodeId ID of the Linode to look up (required)
     * @param linode Any field that is not marked as &#x60;readOnly&#x60; may be updated. Fields that are marked &#x60;readOnly&#x60; will be ignored. If any updated field fails to pass validation, the Linode will not be updated.  (required)
     * @return Linode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Linode updateLinodeInstance(Integer linodeId, Linode linode) throws ApiException {
        ApiResponse<Linode> localVarResp = updateLinodeInstanceWithHttpInfo(linodeId, linode);
        return localVarResp.getData();
    }

    /**
     * Linode Update
     * Updates a Linode that you have permission to &#x60;read_write&#x60;.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param linodeId ID of the Linode to look up (required)
     * @param linode Any field that is not marked as &#x60;readOnly&#x60; may be updated. Fields that are marked &#x60;readOnly&#x60; will be ignored. If any updated field fails to pass validation, the Linode will not be updated.  (required)
     * @return ApiResponse&lt;Linode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Linode> updateLinodeInstanceWithHttpInfo(Integer linodeId, Linode linode) throws ApiException {
        okhttp3.Call localVarCall = updateLinodeInstanceValidateBeforeCall(linodeId, linode, null);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linode Update (asynchronously)
     * Updates a Linode that you have permission to &#x60;read_write&#x60;.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 
     * @param linodeId ID of the Linode to look up (required)
     * @param linode Any field that is not marked as &#x60;readOnly&#x60; may be updated. Fields that are marked &#x60;readOnly&#x60; will be ignored. If any updated field fails to pass validation, the Linode will not be updated.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The updated Linode. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLinodeInstanceAsync(Integer linodeId, Linode linode, final ApiCallback<Linode> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateLinodeInstanceValidateBeforeCall(linodeId, linode, _callback);
        Type localVarReturnType = new TypeToken<Linode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
