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


import org.openapitools.client.model.AllocateIPRequest;
import org.openapitools.client.model.CreateFirewallsRequest;
import org.openapitools.client.model.Firewall;
import org.openapitools.client.model.FirewallDevices;
import org.openapitools.client.model.FirewallDevicesEntity;
import org.openapitools.client.model.FirewallRules;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetFirewallDevices200Response;
import org.openapitools.client.model.GetIPs200Response;
import org.openapitools.client.model.GetIPv6Pools200Response;
import org.openapitools.client.model.GetIPv6Ranges200Response;
import org.openapitools.client.model.GetLinodeFirewalls200Response;
import org.openapitools.client.model.GetVLANs200Response;
import org.openapitools.client.model.IPAddress;
import org.openapitools.client.model.IPAddressesAssignRequest;
import org.openapitools.client.model.IPAddressesShareRequest;
import org.openapitools.client.model.IPv6RangeBGP;
import org.openapitools.client.model.PostIPv6Range200Response;
import org.openapitools.client.model.PostIPv6RangeRequest;
import org.openapitools.client.model.UNKNOWN_BASE_TYPE;
import org.openapitools.client.model.UpdateFirewallRequest;
import org.openapitools.client.model.UpdateFirewallRulesRequest;
import org.openapitools.client.model.UpdateIPRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NetworkingApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public NetworkingApi() {
        this(Configuration.getDefaultApiClient());
    }

    public NetworkingApi(ApiClient apiClient) {
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
     * Build call for allocateIP
     * @param allocateIPRequest Information about the address you are creating. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address allocated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call allocateIPCall(AllocateIPRequest allocateIPRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = allocateIPRequest;

        // create path and map variables
        String localVarPath = "/networking/ips";

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
    private okhttp3.Call allocateIPValidateBeforeCall(AllocateIPRequest allocateIPRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'allocateIPRequest' is set
        if (allocateIPRequest == null) {
            throw new ApiException("Missing the required parameter 'allocateIPRequest' when calling allocateIP(Async)");
        }

        return allocateIPCall(allocateIPRequest, _callback);

    }

    /**
     * IP Address Allocate
     * Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [open a support ticket](/docs/api/support/#support-ticket-open) requesting additional addresses before attempting allocation. 
     * @param allocateIPRequest Information about the address you are creating. (required)
     * @return IPAddress
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address allocated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPAddress allocateIP(AllocateIPRequest allocateIPRequest) throws ApiException {
        ApiResponse<IPAddress> localVarResp = allocateIPWithHttpInfo(allocateIPRequest);
        return localVarResp.getData();
    }

    /**
     * IP Address Allocate
     * Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [open a support ticket](/docs/api/support/#support-ticket-open) requesting additional addresses before attempting allocation. 
     * @param allocateIPRequest Information about the address you are creating. (required)
     * @return ApiResponse&lt;IPAddress&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address allocated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPAddress> allocateIPWithHttpInfo(AllocateIPRequest allocateIPRequest) throws ApiException {
        okhttp3.Call localVarCall = allocateIPValidateBeforeCall(allocateIPRequest, null);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Address Allocate (asynchronously)
     * Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [open a support ticket](/docs/api/support/#support-ticket-open) requesting additional addresses before attempting allocation. 
     * @param allocateIPRequest Information about the address you are creating. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address allocated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call allocateIPAsync(AllocateIPRequest allocateIPRequest, final ApiCallback<IPAddress> _callback) throws ApiException {

        okhttp3.Call localVarCall = allocateIPValidateBeforeCall(allocateIPRequest, _callback);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for assignIPs
     * @param ipAddressesAssignRequest Information about what IPv4 address or IPv6 range to assign, and to which Linode.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call assignIPsCall(IPAddressesAssignRequest ipAddressesAssignRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ipAddressesAssignRequest;

        // create path and map variables
        String localVarPath = "/networking/ips/assign";

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
    private okhttp3.Call assignIPsValidateBeforeCall(IPAddressesAssignRequest ipAddressesAssignRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ipAddressesAssignRequest' is set
        if (ipAddressesAssignRequest == null) {
            throw new ApiException("Missing the required parameter 'ipAddressesAssignRequest' when calling assignIPs(Async)");
        }

        return assignIPsCall(ipAddressesAssignRequest, _callback);

    }

    /**
     * IP Addresses Assign
     * Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 
     * @param ipAddressesAssignRequest Information about what IPv4 address or IPv6 range to assign, and to which Linode.  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object assignIPs(IPAddressesAssignRequest ipAddressesAssignRequest) throws ApiException {
        ApiResponse<Object> localVarResp = assignIPsWithHttpInfo(ipAddressesAssignRequest);
        return localVarResp.getData();
    }

    /**
     * IP Addresses Assign
     * Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 
     * @param ipAddressesAssignRequest Information about what IPv4 address or IPv6 range to assign, and to which Linode.  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> assignIPsWithHttpInfo(IPAddressesAssignRequest ipAddressesAssignRequest) throws ApiException {
        okhttp3.Call localVarCall = assignIPsValidateBeforeCall(ipAddressesAssignRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Addresses Assign (asynchronously)
     * Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 
     * @param ipAddressesAssignRequest Information about what IPv4 address or IPv6 range to assign, and to which Linode.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call assignIPsAsync(IPAddressesAssignRequest ipAddressesAssignRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = assignIPsValidateBeforeCall(ipAddressesAssignRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for assignIPv4s
     * @param ipAddressesAssignRequest Information about what IPv4 address to assign, and to which Linode.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call assignIPv4sCall(IPAddressesAssignRequest ipAddressesAssignRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ipAddressesAssignRequest;

        // create path and map variables
        String localVarPath = "/networking/ipv4/assign";

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
    private okhttp3.Call assignIPv4sValidateBeforeCall(IPAddressesAssignRequest ipAddressesAssignRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ipAddressesAssignRequest' is set
        if (ipAddressesAssignRequest == null) {
            throw new ApiException("Missing the required parameter 'ipAddressesAssignRequest' when calling assignIPv4s(Async)");
        }

        return assignIPv4sCall(ipAddressesAssignRequest, _callback);

    }

    /**
     * Linodes Assign IPv4s
     * This command is equivalent to **IP Addresses Assign** ([POST /networking/ips/assign](#ip-addresses-assign)).  Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 
     * @param ipAddressesAssignRequest Information about what IPv4 address to assign, and to which Linode.  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object assignIPv4s(IPAddressesAssignRequest ipAddressesAssignRequest) throws ApiException {
        ApiResponse<Object> localVarResp = assignIPv4sWithHttpInfo(ipAddressesAssignRequest);
        return localVarResp.getData();
    }

    /**
     * Linodes Assign IPv4s
     * This command is equivalent to **IP Addresses Assign** ([POST /networking/ips/assign](#ip-addresses-assign)).  Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 
     * @param ipAddressesAssignRequest Information about what IPv4 address to assign, and to which Linode.  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> assignIPv4sWithHttpInfo(IPAddressesAssignRequest ipAddressesAssignRequest) throws ApiException {
        okhttp3.Call localVarCall = assignIPv4sValidateBeforeCall(ipAddressesAssignRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linodes Assign IPv4s (asynchronously)
     * This command is equivalent to **IP Addresses Assign** ([POST /networking/ips/assign](#ip-addresses-assign)).  Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 
     * @param ipAddressesAssignRequest Information about what IPv4 address to assign, and to which Linode.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> All assignments completed successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call assignIPv4sAsync(IPAddressesAssignRequest ipAddressesAssignRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = assignIPv4sValidateBeforeCall(ipAddressesAssignRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createFirewallDevice
     * @param firewallId ID of the Firewall to access.  (required)
     * @param UNKNOWN_BASE_TYPE  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createFirewallDeviceCall(Integer firewallId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}/devices"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call createFirewallDeviceValidateBeforeCall(Integer firewallId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling createFirewallDevice(Async)");
        }

        return createFirewallDeviceCall(firewallId, UNKNOWN_BASE_TYPE, _callback);

    }

    /**
     * Firewall Device Create
     * Creates a Firewall Device, which assigns a Firewall to a service (referred to as the Device&#39;s &#x60;entity&#x60;) and applies the Firewall&#39;s Rules to the device.  * Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_device_add&#x60; Event is generated when the Firewall Device is added successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param UNKNOWN_BASE_TYPE  (optional)
     * @return FirewallDevices
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public FirewallDevices createFirewallDevice(Integer firewallId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) throws ApiException {
        ApiResponse<FirewallDevices> localVarResp = createFirewallDeviceWithHttpInfo(firewallId, UNKNOWN_BASE_TYPE);
        return localVarResp.getData();
    }

    /**
     * Firewall Device Create
     * Creates a Firewall Device, which assigns a Firewall to a service (referred to as the Device&#39;s &#x60;entity&#x60;) and applies the Firewall&#39;s Rules to the device.  * Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_device_add&#x60; Event is generated when the Firewall Device is added successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param UNKNOWN_BASE_TYPE  (optional)
     * @return ApiResponse&lt;FirewallDevices&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FirewallDevices> createFirewallDeviceWithHttpInfo(Integer firewallId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) throws ApiException {
        okhttp3.Call localVarCall = createFirewallDeviceValidateBeforeCall(firewallId, UNKNOWN_BASE_TYPE, null);
        Type localVarReturnType = new TypeToken<FirewallDevices>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Device Create (asynchronously)
     * Creates a Firewall Device, which assigns a Firewall to a service (referred to as the Device&#39;s &#x60;entity&#x60;) and applies the Firewall&#39;s Rules to the device.  * Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_device_add&#x60; Event is generated when the Firewall Device is added successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param UNKNOWN_BASE_TYPE  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createFirewallDeviceAsync(Integer firewallId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback<FirewallDevices> _callback) throws ApiException {

        okhttp3.Call localVarCall = createFirewallDeviceValidateBeforeCall(firewallId, UNKNOWN_BASE_TYPE, _callback);
        Type localVarReturnType = new TypeToken<FirewallDevices>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createFirewalls
     * @param createFirewallsRequest Creates a Firewall object that can be applied to a Linode service to filter the service&#39;s network traffic. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createFirewallsCall(CreateFirewallsRequest createFirewallsRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createFirewallsRequest;

        // create path and map variables
        String localVarPath = "/networking/firewalls";

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
    private okhttp3.Call createFirewallsValidateBeforeCall(CreateFirewallsRequest createFirewallsRequest, final ApiCallback _callback) throws ApiException {
        return createFirewallsCall(createFirewallsRequest, _callback);

    }

    /**
     * Firewall Create
     * Creates a Firewall to filter network traffic.  * Use the &#x60;rules&#x60; property to create inbound and outbound access rules.  * Use the &#x60;devices&#x60; property to assign the Firewall to a service and apply its Rules to the device. Requires &#x60;read_write&#x60; [User&#39;s Grants](/docs/api/account/#users-grants-view) to the device. Currently, Firewalls can only be assigned to Linode instances.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_create&#x60; Event is generated when this endpoint returns successfully. 
     * @param createFirewallsRequest Creates a Firewall object that can be applied to a Linode service to filter the service&#39;s network traffic. (optional)
     * @return Firewall
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Firewall createFirewalls(CreateFirewallsRequest createFirewallsRequest) throws ApiException {
        ApiResponse<Firewall> localVarResp = createFirewallsWithHttpInfo(createFirewallsRequest);
        return localVarResp.getData();
    }

    /**
     * Firewall Create
     * Creates a Firewall to filter network traffic.  * Use the &#x60;rules&#x60; property to create inbound and outbound access rules.  * Use the &#x60;devices&#x60; property to assign the Firewall to a service and apply its Rules to the device. Requires &#x60;read_write&#x60; [User&#39;s Grants](/docs/api/account/#users-grants-view) to the device. Currently, Firewalls can only be assigned to Linode instances.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_create&#x60; Event is generated when this endpoint returns successfully. 
     * @param createFirewallsRequest Creates a Firewall object that can be applied to a Linode service to filter the service&#39;s network traffic. (optional)
     * @return ApiResponse&lt;Firewall&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Firewall> createFirewallsWithHttpInfo(CreateFirewallsRequest createFirewallsRequest) throws ApiException {
        okhttp3.Call localVarCall = createFirewallsValidateBeforeCall(createFirewallsRequest, null);
        Type localVarReturnType = new TypeToken<Firewall>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Create (asynchronously)
     * Creates a Firewall to filter network traffic.  * Use the &#x60;rules&#x60; property to create inbound and outbound access rules.  * Use the &#x60;devices&#x60; property to assign the Firewall to a service and apply its Rules to the device. Requires &#x60;read_write&#x60; [User&#39;s Grants](/docs/api/account/#users-grants-view) to the device. Currently, Firewalls can only be assigned to Linode instances.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_create&#x60; Event is generated when this endpoint returns successfully. 
     * @param createFirewallsRequest Creates a Firewall object that can be applied to a Linode service to filter the service&#39;s network traffic. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about the created Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createFirewallsAsync(CreateFirewallsRequest createFirewallsRequest, final ApiCallback<Firewall> _callback) throws ApiException {

        okhttp3.Call localVarCall = createFirewallsValidateBeforeCall(createFirewallsRequest, _callback);
        Type localVarReturnType = new TypeToken<Firewall>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteFirewall
     * @param firewallId ID of the Firewall to access.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteFirewallCall(Integer firewallId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call deleteFirewallValidateBeforeCall(Integer firewallId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling deleteFirewall(Async)");
        }

        return deleteFirewallCall(firewallId, _callback);

    }

    /**
     * Firewall Delete
     * Delete a Firewall resource by its ID. This will remove all of the Firewall&#39;s Rules from any Linode services that the Firewall was assigned to.  A &#x60;firewall_delete&#x60; Event is generated when this endpoint returns successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteFirewall(Integer firewallId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteFirewallWithHttpInfo(firewallId);
        return localVarResp.getData();
    }

    /**
     * Firewall Delete
     * Delete a Firewall resource by its ID. This will remove all of the Firewall&#39;s Rules from any Linode services that the Firewall was assigned to.  A &#x60;firewall_delete&#x60; Event is generated when this endpoint returns successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteFirewallWithHttpInfo(Integer firewallId) throws ApiException {
        okhttp3.Call localVarCall = deleteFirewallValidateBeforeCall(firewallId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Delete (asynchronously)
     * Delete a Firewall resource by its ID. This will remove all of the Firewall&#39;s Rules from any Linode services that the Firewall was assigned to.  A &#x60;firewall_delete&#x60; Event is generated when this endpoint returns successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteFirewallAsync(Integer firewallId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteFirewallValidateBeforeCall(firewallId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteFirewallDevice
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteFirewallDeviceCall(Integer firewallId, Integer deviceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}/devices/{deviceId}"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()))
            .replace("{" + "deviceId" + "}", localVarApiClient.escapeString(deviceId.toString()));

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
    private okhttp3.Call deleteFirewallDeviceValidateBeforeCall(Integer firewallId, Integer deviceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling deleteFirewallDevice(Async)");
        }

        // verify the required parameter 'deviceId' is set
        if (deviceId == null) {
            throw new ApiException("Missing the required parameter 'deviceId' when calling deleteFirewallDevice(Async)");
        }

        return deleteFirewallDeviceCall(firewallId, deviceId, _callback);

    }

    /**
     * Firewall Device Delete
     * Removes a Firewall Device, which removes a Firewall from the Linode service it was assigned to by the Device. This will remove all of the Firewall&#39;s Rules from the Linode service. If any other Firewalls have been assigned to the Linode service, then those Rules will remain in effect.  A &#x60;firewall_device_remove&#x60; Event is generated when the Firewall Device is removed successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteFirewallDevice(Integer firewallId, Integer deviceId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteFirewallDeviceWithHttpInfo(firewallId, deviceId);
        return localVarResp.getData();
    }

    /**
     * Firewall Device Delete
     * Removes a Firewall Device, which removes a Firewall from the Linode service it was assigned to by the Device. This will remove all of the Firewall&#39;s Rules from the Linode service. If any other Firewalls have been assigned to the Linode service, then those Rules will remain in effect.  A &#x60;firewall_device_remove&#x60; Event is generated when the Firewall Device is removed successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteFirewallDeviceWithHttpInfo(Integer firewallId, Integer deviceId) throws ApiException {
        okhttp3.Call localVarCall = deleteFirewallDeviceValidateBeforeCall(firewallId, deviceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Device Delete (asynchronously)
     * Removes a Firewall Device, which removes a Firewall from the Linode service it was assigned to by the Device. This will remove all of the Firewall&#39;s Rules from the Linode service. If any other Firewalls have been assigned to the Linode service, then those Rules will remain in effect.  A &#x60;firewall_device_remove&#x60; Event is generated when the Firewall Device is removed successfully. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete Successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteFirewallDeviceAsync(Integer firewallId, Integer deviceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteFirewallDeviceValidateBeforeCall(firewallId, deviceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteIPv6Range
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 Range deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteIPv6RangeCall(String range, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networking/ipv6/ranges/{range}"
            .replace("{" + "range" + "}", localVarApiClient.escapeString(range.toString()));

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
    private okhttp3.Call deleteIPv6RangeValidateBeforeCall(String range, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'range' is set
        if (range == null) {
            throw new ApiException("Missing the required parameter 'range' when calling deleteIPv6Range(Async)");
        }

        return deleteIPv6RangeCall(range, _callback);

    }

    /**
     * IPv6 Range Delete
     * Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.  **Note:** Shared IPv6 ranges cannot be deleted at this time. Please contact Customer Support for assistance. 
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 Range deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteIPv6Range(String range) throws ApiException {
        ApiResponse<Object> localVarResp = deleteIPv6RangeWithHttpInfo(range);
        return localVarResp.getData();
    }

    /**
     * IPv6 Range Delete
     * Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.  **Note:** Shared IPv6 ranges cannot be deleted at this time. Please contact Customer Support for assistance. 
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 Range deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteIPv6RangeWithHttpInfo(String range) throws ApiException {
        okhttp3.Call localVarCall = deleteIPv6RangeValidateBeforeCall(range, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv6 Range Delete (asynchronously)
     * Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.  **Note:** Shared IPv6 ranges cannot be deleted at this time. Please contact Customer Support for assistance. 
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 Range deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteIPv6RangeAsync(String range, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteIPv6RangeValidateBeforeCall(range, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFirewall
     * @param firewallId ID of the Firewall to access.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about this Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallCall(Integer firewallId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call getFirewallValidateBeforeCall(Integer firewallId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling getFirewall(Async)");
        }

        return getFirewallCall(firewallId, _callback);

    }

    /**
     * Firewall View
     * Get a specific Firewall resource by its ID. The Firewall&#39;s Devices will not be returned in the response. Instead, use the [List Firewall Devices](/docs/api/networking/#firewall-devices-list) endpoint to review them. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @return Firewall
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about this Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Firewall getFirewall(Integer firewallId) throws ApiException {
        ApiResponse<Firewall> localVarResp = getFirewallWithHttpInfo(firewallId);
        return localVarResp.getData();
    }

    /**
     * Firewall View
     * Get a specific Firewall resource by its ID. The Firewall&#39;s Devices will not be returned in the response. Instead, use the [List Firewall Devices](/docs/api/networking/#firewall-devices-list) endpoint to review them. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @return ApiResponse&lt;Firewall&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about this Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Firewall> getFirewallWithHttpInfo(Integer firewallId) throws ApiException {
        okhttp3.Call localVarCall = getFirewallValidateBeforeCall(firewallId, null);
        Type localVarReturnType = new TypeToken<Firewall>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall View (asynchronously)
     * Get a specific Firewall resource by its ID. The Firewall&#39;s Devices will not be returned in the response. Instead, use the [List Firewall Devices](/docs/api/networking/#firewall-devices-list) endpoint to review them. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information about this Firewall. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallAsync(Integer firewallId, final ApiCallback<Firewall> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFirewallValidateBeforeCall(firewallId, _callback);
        Type localVarReturnType = new TypeToken<Firewall>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFirewallDevice
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallDeviceCall(Integer firewallId, Integer deviceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}/devices/{deviceId}"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()))
            .replace("{" + "deviceId" + "}", localVarApiClient.escapeString(deviceId.toString()));

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
    private okhttp3.Call getFirewallDeviceValidateBeforeCall(Integer firewallId, Integer deviceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling getFirewallDevice(Async)");
        }

        // verify the required parameter 'deviceId' is set
        if (deviceId == null) {
            throw new ApiException("Missing the required parameter 'deviceId' when calling getFirewallDevice(Async)");
        }

        return getFirewallDeviceCall(firewallId, deviceId, _callback);

    }

    /**
     * Firewall Device View
     * Returns information for a Firewall Device, which assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @return FirewallDevices
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public FirewallDevices getFirewallDevice(Integer firewallId, Integer deviceId) throws ApiException {
        ApiResponse<FirewallDevices> localVarResp = getFirewallDeviceWithHttpInfo(firewallId, deviceId);
        return localVarResp.getData();
    }

    /**
     * Firewall Device View
     * Returns information for a Firewall Device, which assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @return ApiResponse&lt;FirewallDevices&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FirewallDevices> getFirewallDeviceWithHttpInfo(Integer firewallId, Integer deviceId) throws ApiException {
        okhttp3.Call localVarCall = getFirewallDeviceValidateBeforeCall(firewallId, deviceId, null);
        Type localVarReturnType = new TypeToken<FirewallDevices>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Device View (asynchronously)
     * Returns information for a Firewall Device, which assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param deviceId ID of the Firewall Device to access.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Device. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallDeviceAsync(Integer firewallId, Integer deviceId, final ApiCallback<FirewallDevices> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFirewallDeviceValidateBeforeCall(firewallId, deviceId, _callback);
        Type localVarReturnType = new TypeToken<FirewallDevices>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFirewallDevices
     * @param firewallId ID of the Firewall to access.  (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Firewall Devices </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallDevicesCall(Integer firewallId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}/devices"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call getFirewallDevicesValidateBeforeCall(Integer firewallId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling getFirewallDevices(Async)");
        }

        return getFirewallDevicesCall(firewallId, page, pageSize, _callback);

    }

    /**
     * Firewall Devices List
     * Returns a paginated list of a Firewall&#39;s Devices. A Firewall Device assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetFirewallDevices200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Firewall Devices </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetFirewallDevices200Response getFirewallDevices(Integer firewallId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetFirewallDevices200Response> localVarResp = getFirewallDevicesWithHttpInfo(firewallId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Firewall Devices List
     * Returns a paginated list of a Firewall&#39;s Devices. A Firewall Device assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetFirewallDevices200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Firewall Devices </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetFirewallDevices200Response> getFirewallDevicesWithHttpInfo(Integer firewallId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getFirewallDevicesValidateBeforeCall(firewallId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetFirewallDevices200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Devices List (asynchronously)
     * Returns a paginated list of a Firewall&#39;s Devices. A Firewall Device assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Firewall Devices </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallDevicesAsync(Integer firewallId, Integer page, Integer pageSize, final ApiCallback<GetFirewallDevices200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFirewallDevicesValidateBeforeCall(firewallId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetFirewallDevices200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFirewallRules
     * @param firewallId ID of the Firewall to access.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Rules. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallRulesCall(Integer firewallId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls/{firewallId}/rules"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call getFirewallRulesValidateBeforeCall(Integer firewallId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling getFirewallRules(Async)");
        }

        return getFirewallRulesCall(firewallId, _callback);

    }

    /**
     * Firewall Rules List
     * Returns the inbound and outbound Rules for a Firewall. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @return FirewallRules
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Rules. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public FirewallRules getFirewallRules(Integer firewallId) throws ApiException {
        ApiResponse<FirewallRules> localVarResp = getFirewallRulesWithHttpInfo(firewallId);
        return localVarResp.getData();
    }

    /**
     * Firewall Rules List
     * Returns the inbound and outbound Rules for a Firewall. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @return ApiResponse&lt;FirewallRules&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Rules. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FirewallRules> getFirewallRulesWithHttpInfo(Integer firewallId) throws ApiException {
        okhttp3.Call localVarCall = getFirewallRulesValidateBeforeCall(firewallId, null);
        Type localVarReturnType = new TypeToken<FirewallRules>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Rules List (asynchronously)
     * Returns the inbound and outbound Rules for a Firewall. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Firewall Rules. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallRulesAsync(Integer firewallId, final ApiCallback<FirewallRules> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFirewallRulesValidateBeforeCall(firewallId, _callback);
        Type localVarReturnType = new TypeToken<FirewallRules>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFirewalls
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Firewalls. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallsCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

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
        String localVarPath = "/networking/firewalls";

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
    private okhttp3.Call getFirewallsValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getFirewallsCall(page, pageSize, _callback);

    }

    /**
     * Firewalls List
     * Returns a paginated list of accessible Firewalls. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeFirewalls200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Firewalls. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeFirewalls200Response getFirewalls(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeFirewalls200Response> localVarResp = getFirewallsWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Firewalls List
     * Returns a paginated list of accessible Firewalls. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeFirewalls200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Firewalls. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeFirewalls200Response> getFirewallsWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getFirewallsValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeFirewalls200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewalls List (asynchronously)
     * Returns a paginated list of accessible Firewalls. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of Firewalls. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFirewallsAsync(Integer page, Integer pageSize, final ApiCallback<GetLinodeFirewalls200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFirewallsValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeFirewalls200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getIP
     * @param address The address to operate on. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested IP Address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPCall(String address, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networking/ips/{address}"
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
    private okhttp3.Call getIPValidateBeforeCall(String address, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling getIP(Async)");
        }

        return getIPCall(address, _callback);

    }

    /**
     * IP Address View
     * Returns information about a single IP Address on your Account. 
     * @param address The address to operate on. (required)
     * @return IPAddress
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested IP Address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPAddress getIP(String address) throws ApiException {
        ApiResponse<IPAddress> localVarResp = getIPWithHttpInfo(address);
        return localVarResp.getData();
    }

    /**
     * IP Address View
     * Returns information about a single IP Address on your Account. 
     * @param address The address to operate on. (required)
     * @return ApiResponse&lt;IPAddress&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested IP Address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPAddress> getIPWithHttpInfo(String address) throws ApiException {
        okhttp3.Call localVarCall = getIPValidateBeforeCall(address, null);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Address View (asynchronously)
     * Returns information about a single IP Address on your Account. 
     * @param address The address to operate on. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested IP Address. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPAsync(String address, final ApiCallback<IPAddress> _callback) throws ApiException {

        okhttp3.Call localVarCall = getIPValidateBeforeCall(address, _callback);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getIPs
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of IP Addresses. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networking/ips";

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
    private okhttp3.Call getIPsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getIPsCall(_callback);

    }

    /**
     * IP Addresses List
     * Returns a paginated list of IP Addresses on your Account, excluding private addresses. 
     * @return GetIPs200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of IP Addresses. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetIPs200Response getIPs() throws ApiException {
        ApiResponse<GetIPs200Response> localVarResp = getIPsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * IP Addresses List
     * Returns a paginated list of IP Addresses on your Account, excluding private addresses. 
     * @return ApiResponse&lt;GetIPs200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of IP Addresses. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetIPs200Response> getIPsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getIPsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetIPs200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Addresses List (asynchronously)
     * Returns a paginated list of IP Addresses on your Account, excluding private addresses. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of IP Addresses. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPsAsync(final ApiCallback<GetIPs200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getIPsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetIPs200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getIPv6Pools
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 pools on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPv6PoolsCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networking/ipv6/pools";

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
    private okhttp3.Call getIPv6PoolsValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getIPv6PoolsCall(page, pageSize, _callback);

    }

    /**
     * IPv6 Pools List
     * Displays the IPv6 pools on your Account. A pool of IPv6 addresses are routed to all of your Linodes in a single [Region](/docs/api/regions/#regions-list). Any Linode on your Account may bring up any address in this pool at any time, with no external configuration required. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetIPv6Pools200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 pools on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetIPv6Pools200Response getIPv6Pools(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetIPv6Pools200Response> localVarResp = getIPv6PoolsWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * IPv6 Pools List
     * Displays the IPv6 pools on your Account. A pool of IPv6 addresses are routed to all of your Linodes in a single [Region](/docs/api/regions/#regions-list). Any Linode on your Account may bring up any address in this pool at any time, with no external configuration required. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetIPv6Pools200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 pools on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetIPv6Pools200Response> getIPv6PoolsWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getIPv6PoolsValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetIPv6Pools200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv6 Pools List (asynchronously)
     * Displays the IPv6 pools on your Account. A pool of IPv6 addresses are routed to all of your Linodes in a single [Region](/docs/api/regions/#regions-list). Any Linode on your Account may bring up any address in this pool at any time, with no external configuration required. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 pools on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPv6PoolsAsync(Integer page, Integer pageSize, final ApiCallback<GetIPv6Pools200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getIPv6PoolsValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetIPv6Pools200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getIPv6Range
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns IPv6 range information. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPv6RangeCall(String range, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networking/ipv6/ranges/{range}"
            .replace("{" + "range" + "}", localVarApiClient.escapeString(range.toString()));

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
    private okhttp3.Call getIPv6RangeValidateBeforeCall(String range, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'range' is set
        if (range == null) {
            throw new ApiException("Missing the required parameter 'range' when calling getIPv6Range(Async)");
        }

        return getIPv6RangeCall(range, _callback);

    }

    /**
     * IPv6 Range View
     * View IPv6 range information. 
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @return IPv6RangeBGP
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns IPv6 range information. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPv6RangeBGP getIPv6Range(String range) throws ApiException {
        ApiResponse<IPv6RangeBGP> localVarResp = getIPv6RangeWithHttpInfo(range);
        return localVarResp.getData();
    }

    /**
     * IPv6 Range View
     * View IPv6 range information. 
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @return ApiResponse&lt;IPv6RangeBGP&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns IPv6 range information. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPv6RangeBGP> getIPv6RangeWithHttpInfo(String range) throws ApiException {
        okhttp3.Call localVarCall = getIPv6RangeValidateBeforeCall(range, null);
        Type localVarReturnType = new TypeToken<IPv6RangeBGP>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv6 Range View (asynchronously)
     * View IPv6 range information. 
     * @param range The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns IPv6 range information. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPv6RangeAsync(String range, final ApiCallback<IPv6RangeBGP> _callback) throws ApiException {

        okhttp3.Call localVarCall = getIPv6RangeValidateBeforeCall(range, _callback);
        Type localVarReturnType = new TypeToken<IPv6RangeBGP>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getIPv6Ranges
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 ranges on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPv6RangesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networking/ipv6/ranges";

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
    private okhttp3.Call getIPv6RangesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getIPv6RangesCall(page, pageSize, _callback);

    }

    /**
     * IPv6 Ranges List
     * Displays the IPv6 ranges on your Account.     * An IPv6 range is a &#x60;/64&#x60; or &#x60;/54&#x60; block of IPv6 addresses routed to a single Linode in a given [Region](/docs/api/regions/#regions-list).    * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.    * Access the IPv6 Range Create ([POST /networking/ipv6/ranges](/docs/api/networking/#ipv6-range-create)) endpoint to add a &#x60;/64&#x60; or &#x60;/56&#x60; block of IPv6 addresses to your account. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetIPv6Ranges200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 ranges on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetIPv6Ranges200Response getIPv6Ranges(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetIPv6Ranges200Response> localVarResp = getIPv6RangesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * IPv6 Ranges List
     * Displays the IPv6 ranges on your Account.     * An IPv6 range is a &#x60;/64&#x60; or &#x60;/54&#x60; block of IPv6 addresses routed to a single Linode in a given [Region](/docs/api/regions/#regions-list).    * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.    * Access the IPv6 Range Create ([POST /networking/ipv6/ranges](/docs/api/networking/#ipv6-range-create)) endpoint to add a &#x60;/64&#x60; or &#x60;/56&#x60; block of IPv6 addresses to your account. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetIPv6Ranges200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 ranges on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetIPv6Ranges200Response> getIPv6RangesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getIPv6RangesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetIPv6Ranges200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv6 Ranges List (asynchronously)
     * Displays the IPv6 ranges on your Account.     * An IPv6 range is a &#x60;/64&#x60; or &#x60;/54&#x60; block of IPv6 addresses routed to a single Linode in a given [Region](/docs/api/regions/#regions-list).    * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.    * Access the IPv6 Range Create ([POST /networking/ipv6/ranges](/docs/api/networking/#ipv6-range-create)) endpoint to add a &#x60;/64&#x60; or &#x60;/56&#x60; block of IPv6 addresses to your account. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The IPv6 ranges on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getIPv6RangesAsync(Integer page, Integer pageSize, final ApiCallback<GetIPv6Ranges200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getIPv6RangesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetIPv6Ranges200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVLANs
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The VLANs available on this Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVLANsCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4beta" };

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
        String localVarPath = "/networking/vlans";

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
    private okhttp3.Call getVLANsValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getVLANsCall(page, pageSize, _callback);

    }

    /**
     * VLANs List
     * Returns a list of all Virtual Local Area Networks (VLANs) on your Account. VLANs provide a mechanism for secure communication between two or more Linodes that are assigned to the same VLAN and are both within the same Layer 2 broadcast domain.  VLANs are created and attached to Linodes by using the &#x60;interfaces&#x60; property for the following endpoints:  - Linode Create ([POST /linode/instances](/docs/api/linode-instances/#linode-create)) - Configuration Profile Create ([POST /linode/instances/{linodeId}/configs](/docs/api/linode-instances/#configuration-profile-create)) - Configuration Profile Update ([PUT /linode/instances/{linodeId}/configs/{configId}](/docs/api/linode-instances/#configuration-profile-update))  There are several ways to detach a VLAN from a Linode:  - [Update](/docs/api/linode-instances/#configuration-profile-update) the active Configuration Profile to remove the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode. - [Create](/docs/api/linode-instances/#configuration-profile-create) a new Configuration Profile without the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode into the new Configuration Profile. - [Delete](/docs/api/linode-instances/#linode-delete) the Linode.  **Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  **Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) to view additional specifications and limitations. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetVLANs200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The VLANs available on this Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetVLANs200Response getVLANs(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetVLANs200Response> localVarResp = getVLANsWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * VLANs List
     * Returns a list of all Virtual Local Area Networks (VLANs) on your Account. VLANs provide a mechanism for secure communication between two or more Linodes that are assigned to the same VLAN and are both within the same Layer 2 broadcast domain.  VLANs are created and attached to Linodes by using the &#x60;interfaces&#x60; property for the following endpoints:  - Linode Create ([POST /linode/instances](/docs/api/linode-instances/#linode-create)) - Configuration Profile Create ([POST /linode/instances/{linodeId}/configs](/docs/api/linode-instances/#configuration-profile-create)) - Configuration Profile Update ([PUT /linode/instances/{linodeId}/configs/{configId}](/docs/api/linode-instances/#configuration-profile-update))  There are several ways to detach a VLAN from a Linode:  - [Update](/docs/api/linode-instances/#configuration-profile-update) the active Configuration Profile to remove the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode. - [Create](/docs/api/linode-instances/#configuration-profile-create) a new Configuration Profile without the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode into the new Configuration Profile. - [Delete](/docs/api/linode-instances/#linode-delete) the Linode.  **Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  **Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) to view additional specifications and limitations. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetVLANs200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The VLANs available on this Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetVLANs200Response> getVLANsWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getVLANsValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetVLANs200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * VLANs List (asynchronously)
     * Returns a list of all Virtual Local Area Networks (VLANs) on your Account. VLANs provide a mechanism for secure communication between two or more Linodes that are assigned to the same VLAN and are both within the same Layer 2 broadcast domain.  VLANs are created and attached to Linodes by using the &#x60;interfaces&#x60; property for the following endpoints:  - Linode Create ([POST /linode/instances](/docs/api/linode-instances/#linode-create)) - Configuration Profile Create ([POST /linode/instances/{linodeId}/configs](/docs/api/linode-instances/#configuration-profile-create)) - Configuration Profile Update ([PUT /linode/instances/{linodeId}/configs/{configId}](/docs/api/linode-instances/#configuration-profile-update))  There are several ways to detach a VLAN from a Linode:  - [Update](/docs/api/linode-instances/#configuration-profile-update) the active Configuration Profile to remove the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode. - [Create](/docs/api/linode-instances/#configuration-profile-create) a new Configuration Profile without the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode into the new Configuration Profile. - [Delete](/docs/api/linode-instances/#linode-delete) the Linode.  **Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  **Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) to view additional specifications and limitations. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The VLANs available on this Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVLANsAsync(Integer page, Integer pageSize, final ApiCallback<GetVLANs200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVLANsValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetVLANs200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postIPv6Range
     * @param postIPv6RangeRequest Information about the IPv6 range to create.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 range created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postIPv6RangeCall(PostIPv6RangeRequest postIPv6RangeRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postIPv6RangeRequest;

        // create path and map variables
        String localVarPath = "/networking/ipv6/ranges";

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
    private okhttp3.Call postIPv6RangeValidateBeforeCall(PostIPv6RangeRequest postIPv6RangeRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'postIPv6RangeRequest' is set
        if (postIPv6RangeRequest == null) {
            throw new ApiException("Missing the required parameter 'postIPv6RangeRequest' when calling postIPv6Range(Async)");
        }

        return postIPv6RangeCall(postIPv6RangeRequest, _callback);

    }

    /**
     * IPv6 Range Create
     * Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the &#x60;ipv6&#x60; property when accessing the Linode View ([GET /linode/instances/{linodeId}](/docs/api/linode-instances/#linode-view)) endpoint to view a Linode&#39;s IPv6 SLAAC address.   * Either &#x60;linode_id&#x60; or &#x60;route_target&#x60; is required in a request.   * &#x60;linode_id&#x60; and &#x60;route_target&#x60; are mutually exclusive. Submitting values for both properties in a request results in an error.   * Upon a successful request, an IPv6 range is created in the [Region](/docs/api/regions/#regions-list) that corresponds to the provided &#x60;linode_id&#x60; or &#x60;route_target&#x60;.   * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.   * Access the IP Addresses Assign ([POST /networking/ips/assign](/docs/api/networking/#ip-addresses-assign)) endpoint to re-assign IPv6 Ranges to your Linodes.  **Note**: The following restrictions apply:   * A Linode can only have one IPv6 range targeting its SLAAC address.   * An account can only have one IPv6 range in each [Region](/docs/api/regions/#regions-list).   * [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request expansion of these restrictions. 
     * @param postIPv6RangeRequest Information about the IPv6 range to create.  (required)
     * @return PostIPv6Range200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 range created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public PostIPv6Range200Response postIPv6Range(PostIPv6RangeRequest postIPv6RangeRequest) throws ApiException {
        ApiResponse<PostIPv6Range200Response> localVarResp = postIPv6RangeWithHttpInfo(postIPv6RangeRequest);
        return localVarResp.getData();
    }

    /**
     * IPv6 Range Create
     * Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the &#x60;ipv6&#x60; property when accessing the Linode View ([GET /linode/instances/{linodeId}](/docs/api/linode-instances/#linode-view)) endpoint to view a Linode&#39;s IPv6 SLAAC address.   * Either &#x60;linode_id&#x60; or &#x60;route_target&#x60; is required in a request.   * &#x60;linode_id&#x60; and &#x60;route_target&#x60; are mutually exclusive. Submitting values for both properties in a request results in an error.   * Upon a successful request, an IPv6 range is created in the [Region](/docs/api/regions/#regions-list) that corresponds to the provided &#x60;linode_id&#x60; or &#x60;route_target&#x60;.   * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.   * Access the IP Addresses Assign ([POST /networking/ips/assign](/docs/api/networking/#ip-addresses-assign)) endpoint to re-assign IPv6 Ranges to your Linodes.  **Note**: The following restrictions apply:   * A Linode can only have one IPv6 range targeting its SLAAC address.   * An account can only have one IPv6 range in each [Region](/docs/api/regions/#regions-list).   * [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request expansion of these restrictions. 
     * @param postIPv6RangeRequest Information about the IPv6 range to create.  (required)
     * @return ApiResponse&lt;PostIPv6Range200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 range created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PostIPv6Range200Response> postIPv6RangeWithHttpInfo(PostIPv6RangeRequest postIPv6RangeRequest) throws ApiException {
        okhttp3.Call localVarCall = postIPv6RangeValidateBeforeCall(postIPv6RangeRequest, null);
        Type localVarReturnType = new TypeToken<PostIPv6Range200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv6 Range Create (asynchronously)
     * Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the &#x60;ipv6&#x60; property when accessing the Linode View ([GET /linode/instances/{linodeId}](/docs/api/linode-instances/#linode-view)) endpoint to view a Linode&#39;s IPv6 SLAAC address.   * Either &#x60;linode_id&#x60; or &#x60;route_target&#x60; is required in a request.   * &#x60;linode_id&#x60; and &#x60;route_target&#x60; are mutually exclusive. Submitting values for both properties in a request results in an error.   * Upon a successful request, an IPv6 range is created in the [Region](/docs/api/regions/#regions-list) that corresponds to the provided &#x60;linode_id&#x60; or &#x60;route_target&#x60;.   * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.   * Access the IP Addresses Assign ([POST /networking/ips/assign](/docs/api/networking/#ip-addresses-assign)) endpoint to re-assign IPv6 Ranges to your Linodes.  **Note**: The following restrictions apply:   * A Linode can only have one IPv6 range targeting its SLAAC address.   * An account can only have one IPv6 range in each [Region](/docs/api/regions/#regions-list).   * [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request expansion of these restrictions. 
     * @param postIPv6RangeRequest Information about the IPv6 range to create.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IPv6 range created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postIPv6RangeAsync(PostIPv6RangeRequest postIPv6RangeRequest, final ApiCallback<PostIPv6Range200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = postIPv6RangeValidateBeforeCall(postIPv6RangeRequest, _callback);
        Type localVarReturnType = new TypeToken<PostIPv6Range200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for shareIPs
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address sharing successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call shareIPsCall(IPAddressesShareRequest ipAddressesShareRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = ipAddressesShareRequest;

        // create path and map variables
        String localVarPath = "/networking/ips/share";

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
    private okhttp3.Call shareIPsValidateBeforeCall(IPAddressesShareRequest ipAddressesShareRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ipAddressesShareRequest' is set
        if (ipAddressesShareRequest == null) {
            throw new ApiException("Missing the required parameter 'ipAddressesShareRequest' when calling shareIPs(Async)");
        }

        return shareIPsCall(ipAddressesShareRequest, _callback);

    }

    /**
     * IP Addresses Share
     * Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address sharing successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object shareIPs(IPAddressesShareRequest ipAddressesShareRequest) throws ApiException {
        ApiResponse<Object> localVarResp = shareIPsWithHttpInfo(ipAddressesShareRequest);
        return localVarResp.getData();
    }

    /**
     * IP Addresses Share
     * Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address sharing successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> shareIPsWithHttpInfo(IPAddressesShareRequest ipAddressesShareRequest) throws ApiException {
        okhttp3.Call localVarCall = shareIPsValidateBeforeCall(ipAddressesShareRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Addresses Share (asynchronously)
     * Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> IP Address sharing successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call shareIPsAsync(IPAddressesShareRequest ipAddressesShareRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = shareIPsValidateBeforeCall(ipAddressesShareRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for shareIPv4s
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Sharing configured successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call shareIPv4sCall(IPAddressesShareRequest ipAddressesShareRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ipAddressesShareRequest;

        // create path and map variables
        String localVarPath = "/networking/ipv4/share";

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
    private okhttp3.Call shareIPv4sValidateBeforeCall(IPAddressesShareRequest ipAddressesShareRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ipAddressesShareRequest' is set
        if (ipAddressesShareRequest == null) {
            throw new ApiException("Missing the required parameter 'ipAddressesShareRequest' when calling shareIPv4s(Async)");
        }

        return shareIPv4sCall(ipAddressesShareRequest, _callback);

    }

    /**
     * IPv4 Sharing Configure
     * This command is equivalent to **IP Addresses Share** ([POST /networking/ips/share](#ip-addresses-share)).  Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Sharing configured successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object shareIPv4s(IPAddressesShareRequest ipAddressesShareRequest) throws ApiException {
        ApiResponse<Object> localVarResp = shareIPv4sWithHttpInfo(ipAddressesShareRequest);
        return localVarResp.getData();
    }

    /**
     * IPv4 Sharing Configure
     * This command is equivalent to **IP Addresses Share** ([POST /networking/ips/share](#ip-addresses-share)).  Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Sharing configured successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> shareIPv4sWithHttpInfo(IPAddressesShareRequest ipAddressesShareRequest) throws ApiException {
        okhttp3.Call localVarCall = shareIPv4sValidateBeforeCall(ipAddressesShareRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IPv4 Sharing Configure (asynchronously)
     * This command is equivalent to **IP Addresses Share** ([POST /networking/ips/share](#ip-addresses-share)).  Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 
     * @param ipAddressesShareRequest Information about what IPs to share with which Linode. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Sharing configured successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call shareIPv4sAsync(IPAddressesShareRequest ipAddressesShareRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = shareIPv4sValidateBeforeCall(ipAddressesShareRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateFirewall
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRequest The Firewall information to update. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateFirewallCall(Integer firewallId, UpdateFirewallRequest updateFirewallRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateFirewallRequest;

        // create path and map variables
        String localVarPath = "/networking/firewalls/{firewallId}"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call updateFirewallValidateBeforeCall(Integer firewallId, UpdateFirewallRequest updateFirewallRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling updateFirewall(Async)");
        }

        return updateFirewallCall(firewallId, updateFirewallRequest, _callback);

    }

    /**
     * Firewall Update
     * Updates information for a Firewall. Some parts of a Firewall&#39;s configuration cannot be manipulated by this endpoint:  - A Firewall&#39;s Devices cannot be set with this endpoint. Instead, use the [Create Firewall Device](/docs/api/networking/#firewall-device-create) and [Delete Firewall Device](/docs/api/networking/#firewall-device-delete) endpoints to assign and remove this Firewall from Linode services.  - A Firewall&#39;s Rules cannot be changed with this endpoint. Instead, use the [Update Firewall Rules](/docs/api/networking/#firewall-rules-update) endpoint to update your Rules.  - A Firewall&#39;s status can be set to &#x60;enabled&#x60; or &#x60;disabled&#x60; by this endpoint, but it cannot be set to &#x60;deleted&#x60;. Instead, use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.  If a Firewall&#39;s status is changed with this endpoint, a corresponding &#x60;firewall_enable&#x60; or &#x60;firewall_disable&#x60; Event will be generated. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRequest The Firewall information to update. (optional)
     * @return Firewall
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Firewall updateFirewall(Integer firewallId, UpdateFirewallRequest updateFirewallRequest) throws ApiException {
        ApiResponse<Firewall> localVarResp = updateFirewallWithHttpInfo(firewallId, updateFirewallRequest);
        return localVarResp.getData();
    }

    /**
     * Firewall Update
     * Updates information for a Firewall. Some parts of a Firewall&#39;s configuration cannot be manipulated by this endpoint:  - A Firewall&#39;s Devices cannot be set with this endpoint. Instead, use the [Create Firewall Device](/docs/api/networking/#firewall-device-create) and [Delete Firewall Device](/docs/api/networking/#firewall-device-delete) endpoints to assign and remove this Firewall from Linode services.  - A Firewall&#39;s Rules cannot be changed with this endpoint. Instead, use the [Update Firewall Rules](/docs/api/networking/#firewall-rules-update) endpoint to update your Rules.  - A Firewall&#39;s status can be set to &#x60;enabled&#x60; or &#x60;disabled&#x60; by this endpoint, but it cannot be set to &#x60;deleted&#x60;. Instead, use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.  If a Firewall&#39;s status is changed with this endpoint, a corresponding &#x60;firewall_enable&#x60; or &#x60;firewall_disable&#x60; Event will be generated. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRequest The Firewall information to update. (optional)
     * @return ApiResponse&lt;Firewall&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Firewall> updateFirewallWithHttpInfo(Integer firewallId, UpdateFirewallRequest updateFirewallRequest) throws ApiException {
        okhttp3.Call localVarCall = updateFirewallValidateBeforeCall(firewallId, updateFirewallRequest, null);
        Type localVarReturnType = new TypeToken<Firewall>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Update (asynchronously)
     * Updates information for a Firewall. Some parts of a Firewall&#39;s configuration cannot be manipulated by this endpoint:  - A Firewall&#39;s Devices cannot be set with this endpoint. Instead, use the [Create Firewall Device](/docs/api/networking/#firewall-device-create) and [Delete Firewall Device](/docs/api/networking/#firewall-device-delete) endpoints to assign and remove this Firewall from Linode services.  - A Firewall&#39;s Rules cannot be changed with this endpoint. Instead, use the [Update Firewall Rules](/docs/api/networking/#firewall-rules-update) endpoint to update your Rules.  - A Firewall&#39;s status can be set to &#x60;enabled&#x60; or &#x60;disabled&#x60; by this endpoint, but it cannot be set to &#x60;deleted&#x60;. Instead, use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.  If a Firewall&#39;s status is changed with this endpoint, a corresponding &#x60;firewall_enable&#x60; or &#x60;firewall_disable&#x60; Event will be generated. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRequest The Firewall information to update. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateFirewallAsync(Integer firewallId, UpdateFirewallRequest updateFirewallRequest, final ApiCallback<Firewall> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateFirewallValidateBeforeCall(firewallId, updateFirewallRequest, _callback);
        Type localVarReturnType = new TypeToken<Firewall>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateFirewallRules
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRulesRequest The Firewall Rules information to update. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall Rules updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateFirewallRulesCall(Integer firewallId, UpdateFirewallRulesRequest updateFirewallRulesRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateFirewallRulesRequest;

        // create path and map variables
        String localVarPath = "/networking/firewalls/{firewallId}/rules"
            .replace("{" + "firewallId" + "}", localVarApiClient.escapeString(firewallId.toString()));

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
    private okhttp3.Call updateFirewallRulesValidateBeforeCall(Integer firewallId, UpdateFirewallRulesRequest updateFirewallRulesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'firewallId' is set
        if (firewallId == null) {
            throw new ApiException("Missing the required parameter 'firewallId' when calling updateFirewallRules(Async)");
        }

        return updateFirewallRulesCall(firewallId, updateFirewallRulesRequest, _callback);

    }

    /**
     * Firewall Rules Update
     * Updates the inbound and outbound Rules for a Firewall.  **Note:** This command replaces all of a Firewall&#39;s &#x60;inbound&#x60; and/or &#x60;outbound&#x60; rulesets with the values specified in your request. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRulesRequest The Firewall Rules information to update. (optional)
     * @return FirewallRules
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall Rules updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public FirewallRules updateFirewallRules(Integer firewallId, UpdateFirewallRulesRequest updateFirewallRulesRequest) throws ApiException {
        ApiResponse<FirewallRules> localVarResp = updateFirewallRulesWithHttpInfo(firewallId, updateFirewallRulesRequest);
        return localVarResp.getData();
    }

    /**
     * Firewall Rules Update
     * Updates the inbound and outbound Rules for a Firewall.  **Note:** This command replaces all of a Firewall&#39;s &#x60;inbound&#x60; and/or &#x60;outbound&#x60; rulesets with the values specified in your request. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRulesRequest The Firewall Rules information to update. (optional)
     * @return ApiResponse&lt;FirewallRules&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall Rules updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FirewallRules> updateFirewallRulesWithHttpInfo(Integer firewallId, UpdateFirewallRulesRequest updateFirewallRulesRequest) throws ApiException {
        okhttp3.Call localVarCall = updateFirewallRulesValidateBeforeCall(firewallId, updateFirewallRulesRequest, null);
        Type localVarReturnType = new TypeToken<FirewallRules>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Firewall Rules Update (asynchronously)
     * Updates the inbound and outbound Rules for a Firewall.  **Note:** This command replaces all of a Firewall&#39;s &#x60;inbound&#x60; and/or &#x60;outbound&#x60; rulesets with the values specified in your request. 
     * @param firewallId ID of the Firewall to access.  (required)
     * @param updateFirewallRulesRequest The Firewall Rules information to update. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Firewall Rules updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateFirewallRulesAsync(Integer firewallId, UpdateFirewallRulesRequest updateFirewallRulesRequest, final ApiCallback<FirewallRules> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateFirewallRulesValidateBeforeCall(firewallId, updateFirewallRulesRequest, _callback);
        Type localVarReturnType = new TypeToken<FirewallRules>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateIP
     * @param address The address to operate on. (required)
     * @param updateIPRequest The information to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> RDNS set successfully </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateIPCall(String address, UpdateIPRequest updateIPRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateIPRequest;

        // create path and map variables
        String localVarPath = "/networking/ips/{address}"
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
    private okhttp3.Call updateIPValidateBeforeCall(String address, UpdateIPRequest updateIPRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'address' is set
        if (address == null) {
            throw new ApiException("Missing the required parameter 'address' when calling updateIP(Async)");
        }

        // verify the required parameter 'updateIPRequest' is set
        if (updateIPRequest == null) {
            throw new ApiException("Missing the required parameter 'updateIPRequest' when calling updateIP(Async)");
        }

        return updateIPCall(address, updateIPRequest, _callback);

    }

    /**
     * IP Address RDNS Update
     * Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to &#x60;null&#x60; for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value. 
     * @param address The address to operate on. (required)
     * @param updateIPRequest The information to update. (required)
     * @return IPAddress
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> RDNS set successfully </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public IPAddress updateIP(String address, UpdateIPRequest updateIPRequest) throws ApiException {
        ApiResponse<IPAddress> localVarResp = updateIPWithHttpInfo(address, updateIPRequest);
        return localVarResp.getData();
    }

    /**
     * IP Address RDNS Update
     * Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to &#x60;null&#x60; for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value. 
     * @param address The address to operate on. (required)
     * @param updateIPRequest The information to update. (required)
     * @return ApiResponse&lt;IPAddress&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> RDNS set successfully </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IPAddress> updateIPWithHttpInfo(String address, UpdateIPRequest updateIPRequest) throws ApiException {
        okhttp3.Call localVarCall = updateIPValidateBeforeCall(address, updateIPRequest, null);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * IP Address RDNS Update (asynchronously)
     * Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to &#x60;null&#x60; for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value. 
     * @param address The address to operate on. (required)
     * @param updateIPRequest The information to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> RDNS set successfully </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateIPAsync(String address, UpdateIPRequest updateIPRequest, final ApiCallback<IPAddress> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateIPValidateBeforeCall(address, updateIPRequest, _callback);
        Type localVarReturnType = new TypeToken<IPAddress>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
