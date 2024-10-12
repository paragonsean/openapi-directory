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


import org.openapitools.client.model.CreateNodeBalancerRequest;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetLinodeNodeBalancers200Response;
import org.openapitools.client.model.GetNodeBalancerConfigNodes200Response;
import org.openapitools.client.model.GetNodeBalancerConfigs200Response;
import org.openapitools.client.model.NodeBalancer;
import org.openapitools.client.model.NodeBalancerConfig;
import org.openapitools.client.model.NodeBalancerNode;
import org.openapitools.client.model.NodeBalancerStats;
import org.openapitools.client.model.RebuildNodeBalancerConfigRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NodeBalancersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public NodeBalancersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public NodeBalancersApi(ApiClient apiClient) {
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
     * Build call for createNodeBalancer
     * @param createNodeBalancerRequest Information about the NodeBalancer to create. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNodeBalancerCall(CreateNodeBalancerRequest createNodeBalancerRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createNodeBalancerRequest;

        // create path and map variables
        String localVarPath = "/nodebalancers";

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
    private okhttp3.Call createNodeBalancerValidateBeforeCall(CreateNodeBalancerRequest createNodeBalancerRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createNodeBalancerRequest' is set
        if (createNodeBalancerRequest == null) {
            throw new ApiException("Missing the required parameter 'createNodeBalancerRequest' when calling createNodeBalancer(Async)");
        }

        return createNodeBalancerCall(createNodeBalancerRequest, _callback);

    }

    /**
     * NodeBalancer Create
     * Creates a NodeBalancer in the requested Region.  NodeBalancers require a port Config with at least one backend Node to start serving requests.  When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Config Create](/docs/api/nodebalancers/#config-create) and [Node Create](/docs/api/nodebalancers/#node-create) commands. 
     * @param createNodeBalancerRequest Information about the NodeBalancer to create. (required)
     * @return NodeBalancer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancer createNodeBalancer(CreateNodeBalancerRequest createNodeBalancerRequest) throws ApiException {
        ApiResponse<NodeBalancer> localVarResp = createNodeBalancerWithHttpInfo(createNodeBalancerRequest);
        return localVarResp.getData();
    }

    /**
     * NodeBalancer Create
     * Creates a NodeBalancer in the requested Region.  NodeBalancers require a port Config with at least one backend Node to start serving requests.  When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Config Create](/docs/api/nodebalancers/#config-create) and [Node Create](/docs/api/nodebalancers/#node-create) commands. 
     * @param createNodeBalancerRequest Information about the NodeBalancer to create. (required)
     * @return ApiResponse&lt;NodeBalancer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancer> createNodeBalancerWithHttpInfo(CreateNodeBalancerRequest createNodeBalancerRequest) throws ApiException {
        okhttp3.Call localVarCall = createNodeBalancerValidateBeforeCall(createNodeBalancerRequest, null);
        Type localVarReturnType = new TypeToken<NodeBalancer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * NodeBalancer Create (asynchronously)
     * Creates a NodeBalancer in the requested Region.  NodeBalancers require a port Config with at least one backend Node to start serving requests.  When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Config Create](/docs/api/nodebalancers/#config-create) and [Node Create](/docs/api/nodebalancers/#node-create) commands. 
     * @param createNodeBalancerRequest Information about the NodeBalancer to create. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNodeBalancerAsync(CreateNodeBalancerRequest createNodeBalancerRequest, final ApiCallback<NodeBalancer> _callback) throws ApiException {

        okhttp3.Call localVarCall = createNodeBalancerValidateBeforeCall(createNodeBalancerRequest, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createNodeBalancerConfig
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancerConfig Information about the port to configure. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNodeBalancerConfigCall(Integer nodeBalancerId, NodeBalancerConfig nodeBalancerConfig, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = nodeBalancerConfig;

        // create path and map variables
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()));

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
    private okhttp3.Call createNodeBalancerConfigValidateBeforeCall(Integer nodeBalancerId, NodeBalancerConfig nodeBalancerConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling createNodeBalancerConfig(Async)");
        }

        return createNodeBalancerConfigCall(nodeBalancerId, nodeBalancerConfig, _callback);

    }

    /**
     * Config Create
     * Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancerConfig Information about the port to configure. (optional)
     * @return NodeBalancerConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerConfig createNodeBalancerConfig(Integer nodeBalancerId, NodeBalancerConfig nodeBalancerConfig) throws ApiException {
        ApiResponse<NodeBalancerConfig> localVarResp = createNodeBalancerConfigWithHttpInfo(nodeBalancerId, nodeBalancerConfig);
        return localVarResp.getData();
    }

    /**
     * Config Create
     * Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancerConfig Information about the port to configure. (optional)
     * @return ApiResponse&lt;NodeBalancerConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerConfig> createNodeBalancerConfigWithHttpInfo(Integer nodeBalancerId, NodeBalancerConfig nodeBalancerConfig) throws ApiException {
        okhttp3.Call localVarCall = createNodeBalancerConfigValidateBeforeCall(nodeBalancerId, nodeBalancerConfig, null);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Config Create (asynchronously)
     * Creates a NodeBalancer Config, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer Nodes to the new Config before it can actually serve requests. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancerConfig Information about the port to configure. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNodeBalancerConfigAsync(Integer nodeBalancerId, NodeBalancerConfig nodeBalancerConfig, final ApiCallback<NodeBalancerConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = createNodeBalancerConfigValidateBeforeCall(nodeBalancerId, nodeBalancerConfig, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createNodeBalancerNode
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param nodeBalancerNode Information about the Node to create. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNodeBalancerNodeCall(Integer nodeBalancerId, Integer configId, NodeBalancerNode nodeBalancerNode, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = nodeBalancerNode;

        // create path and map variables
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createNodeBalancerNodeValidateBeforeCall(Integer nodeBalancerId, Integer configId, NodeBalancerNode nodeBalancerNode, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling createNodeBalancerNode(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling createNodeBalancerNode(Async)");
        }

        // verify the required parameter 'nodeBalancerNode' is set
        if (nodeBalancerNode == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerNode' when calling createNodeBalancerNode(Async)");
        }

        return createNodeBalancerNodeCall(nodeBalancerId, configId, nodeBalancerNode, _callback);

    }

    /**
     * Node Create
     * Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param nodeBalancerNode Information about the Node to create. (required)
     * @return NodeBalancerNode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerNode createNodeBalancerNode(Integer nodeBalancerId, Integer configId, NodeBalancerNode nodeBalancerNode) throws ApiException {
        ApiResponse<NodeBalancerNode> localVarResp = createNodeBalancerNodeWithHttpInfo(nodeBalancerId, configId, nodeBalancerNode);
        return localVarResp.getData();
    }

    /**
     * Node Create
     * Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param nodeBalancerNode Information about the Node to create. (required)
     * @return ApiResponse&lt;NodeBalancerNode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerNode> createNodeBalancerNodeWithHttpInfo(Integer nodeBalancerId, Integer configId, NodeBalancerNode nodeBalancerNode) throws ApiException {
        okhttp3.Call localVarCall = createNodeBalancerNodeValidateBeforeCall(nodeBalancerId, configId, nodeBalancerNode, null);
        Type localVarReturnType = new TypeToken<NodeBalancerNode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Create (asynchronously)
     * Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param nodeBalancerNode Information about the Node to create. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNodeBalancerNodeAsync(Integer nodeBalancerId, Integer configId, NodeBalancerNode nodeBalancerNode, final ApiCallback<NodeBalancerNode> _callback) throws ApiException {

        okhttp3.Call localVarCall = createNodeBalancerNodeValidateBeforeCall(nodeBalancerId, configId, nodeBalancerNode, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerNode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteNodeBalancer
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNodeBalancerCall(Integer nodeBalancerId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()));

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
    private okhttp3.Call deleteNodeBalancerValidateBeforeCall(Integer nodeBalancerId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling deleteNodeBalancer(Async)");
        }

        return deleteNodeBalancerCall(nodeBalancerId, _callback);

    }

    /**
     * NodeBalancer Delete
     * Deletes a NodeBalancer.  **This is a destructive action and cannot be undone.**  Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteNodeBalancer(Integer nodeBalancerId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteNodeBalancerWithHttpInfo(nodeBalancerId);
        return localVarResp.getData();
    }

    /**
     * NodeBalancer Delete
     * Deletes a NodeBalancer.  **This is a destructive action and cannot be undone.**  Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteNodeBalancerWithHttpInfo(Integer nodeBalancerId) throws ApiException {
        okhttp3.Call localVarCall = deleteNodeBalancerValidateBeforeCall(nodeBalancerId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * NodeBalancer Delete (asynchronously)
     * Deletes a NodeBalancer.  **This is a destructive action and cannot be undone.**  Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNodeBalancerAsync(Integer nodeBalancerId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteNodeBalancerValidateBeforeCall(nodeBalancerId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteNodeBalancerConfig
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer Config deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNodeBalancerConfigCall(Integer nodeBalancerId, Integer configId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
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
    private okhttp3.Call deleteNodeBalancerConfigValidateBeforeCall(Integer nodeBalancerId, Integer configId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling deleteNodeBalancerConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling deleteNodeBalancerConfig(Async)");
        }

        return deleteNodeBalancerConfigCall(nodeBalancerId, configId, _callback);

    }

    /**
     * Config Delete
     * Deletes the Config for a port of this NodeBalancer.  **This cannot be undone.**  Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer Config deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteNodeBalancerConfig(Integer nodeBalancerId, Integer configId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteNodeBalancerConfigWithHttpInfo(nodeBalancerId, configId);
        return localVarResp.getData();
    }

    /**
     * Config Delete
     * Deletes the Config for a port of this NodeBalancer.  **This cannot be undone.**  Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer Config deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteNodeBalancerConfigWithHttpInfo(Integer nodeBalancerId, Integer configId) throws ApiException {
        okhttp3.Call localVarCall = deleteNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Config Delete (asynchronously)
     * Deletes the Config for a port of this NodeBalancer.  **This cannot be undone.**  Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer Config deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNodeBalancerConfigAsync(Integer nodeBalancerId, Integer configId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteNodeBalancerConfigNode
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNodeBalancerConfigNodeCall(Integer nodeBalancerId, Integer configId, Integer nodeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()))
            .replace("{" + "nodeId" + "}", localVarApiClient.escapeString(nodeId.toString()));

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
    private okhttp3.Call deleteNodeBalancerConfigNodeValidateBeforeCall(Integer nodeBalancerId, Integer configId, Integer nodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling deleteNodeBalancerConfigNode(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling deleteNodeBalancerConfigNode(Async)");
        }

        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling deleteNodeBalancerConfigNode(Async)");
        }

        return deleteNodeBalancerConfigNodeCall(nodeBalancerId, configId, nodeId, _callback);

    }

    /**
     * Node Delete
     * Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.  This does not change or remove the Linode whose address was used in the creation of this Node. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteNodeBalancerConfigNode(Integer nodeBalancerId, Integer configId, Integer nodeId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteNodeBalancerConfigNodeWithHttpInfo(nodeBalancerId, configId, nodeId);
        return localVarResp.getData();
    }

    /**
     * Node Delete
     * Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.  This does not change or remove the Linode whose address was used in the creation of this Node. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteNodeBalancerConfigNodeWithHttpInfo(Integer nodeBalancerId, Integer configId, Integer nodeId) throws ApiException {
        okhttp3.Call localVarCall = deleteNodeBalancerConfigNodeValidateBeforeCall(nodeBalancerId, configId, nodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Delete (asynchronously)
     * Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.  This does not change or remove the Linode whose address was used in the creation of this Node. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNodeBalancerConfigNodeAsync(Integer nodeBalancerId, Integer configId, Integer nodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteNodeBalancerConfigNodeValidateBeforeCall(nodeBalancerId, configId, nodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNodeBalancer
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerCall(Integer nodeBalancerId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()));

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
    private okhttp3.Call getNodeBalancerValidateBeforeCall(Integer nodeBalancerId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling getNodeBalancer(Async)");
        }

        return getNodeBalancerCall(nodeBalancerId, _callback);

    }

    /**
     * NodeBalancer View
     * Returns a single NodeBalancer you can access. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @return NodeBalancer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancer getNodeBalancer(Integer nodeBalancerId) throws ApiException {
        ApiResponse<NodeBalancer> localVarResp = getNodeBalancerWithHttpInfo(nodeBalancerId);
        return localVarResp.getData();
    }

    /**
     * NodeBalancer View
     * Returns a single NodeBalancer you can access. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @return ApiResponse&lt;NodeBalancer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancer> getNodeBalancerWithHttpInfo(Integer nodeBalancerId) throws ApiException {
        okhttp3.Call localVarCall = getNodeBalancerValidateBeforeCall(nodeBalancerId, null);
        Type localVarReturnType = new TypeToken<NodeBalancer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * NodeBalancer View (asynchronously)
     * Returns a single NodeBalancer you can access. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerAsync(Integer nodeBalancerId, final ApiCallback<NodeBalancer> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNodeBalancerValidateBeforeCall(nodeBalancerId, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNodeBalancerConfig
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer config. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerConfigCall(Integer nodeBalancerId, Integer configId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
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
    private okhttp3.Call getNodeBalancerConfigValidateBeforeCall(Integer nodeBalancerId, Integer configId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling getNodeBalancerConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling getNodeBalancerConfig(Async)");
        }

        return getNodeBalancerConfigCall(nodeBalancerId, configId, _callback);

    }

    /**
     * Config View
     * Returns configuration information for a single port of this NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @return NodeBalancerConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer config. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerConfig getNodeBalancerConfig(Integer nodeBalancerId, Integer configId) throws ApiException {
        ApiResponse<NodeBalancerConfig> localVarResp = getNodeBalancerConfigWithHttpInfo(nodeBalancerId, configId);
        return localVarResp.getData();
    }

    /**
     * Config View
     * Returns configuration information for a single port of this NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @return ApiResponse&lt;NodeBalancerConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer config. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerConfig> getNodeBalancerConfigWithHttpInfo(Integer nodeBalancerId, Integer configId) throws ApiException {
        okhttp3.Call localVarCall = getNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, null);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Config View (asynchronously)
     * Returns configuration information for a single port of this NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested NodeBalancer config. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerConfigAsync(Integer nodeBalancerId, Integer configId, final ApiCallback<NodeBalancerConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNodeBalancerConfigNodes
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerConfigNodesCall(Integer nodeBalancerId, Integer configId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()));

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
    private okhttp3.Call getNodeBalancerConfigNodesValidateBeforeCall(Integer nodeBalancerId, Integer configId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling getNodeBalancerConfigNodes(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling getNodeBalancerConfigNodes(Async)");
        }

        return getNodeBalancerConfigNodesCall(nodeBalancerId, configId, page, pageSize, _callback);

    }

    /**
     * Nodes List
     * Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetNodeBalancerConfigNodes200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetNodeBalancerConfigNodes200Response getNodeBalancerConfigNodes(Integer nodeBalancerId, Integer configId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetNodeBalancerConfigNodes200Response> localVarResp = getNodeBalancerConfigNodesWithHttpInfo(nodeBalancerId, configId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Nodes List
     * Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetNodeBalancerConfigNodes200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNodeBalancerConfigNodes200Response> getNodeBalancerConfigNodesWithHttpInfo(Integer nodeBalancerId, Integer configId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getNodeBalancerConfigNodesValidateBeforeCall(nodeBalancerId, configId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetNodeBalancerConfigNodes200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Nodes List (asynchronously)
     * Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the NodeBalancer config to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerConfigNodesAsync(Integer nodeBalancerId, Integer configId, Integer page, Integer pageSize, final ApiCallback<GetNodeBalancerConfigNodes200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNodeBalancerConfigNodesValidateBeforeCall(nodeBalancerId, configId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetNodeBalancerConfigNodes200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNodeBalancerConfigs
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginted list of NodeBalancer Configs </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerConfigsCall(Integer nodeBalancerId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()));

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
    private okhttp3.Call getNodeBalancerConfigsValidateBeforeCall(Integer nodeBalancerId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling getNodeBalancerConfigs(Async)");
        }

        return getNodeBalancerConfigsCall(nodeBalancerId, page, pageSize, _callback);

    }

    /**
     * Configs List
     * Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.  For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetNodeBalancerConfigs200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginted list of NodeBalancer Configs </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetNodeBalancerConfigs200Response getNodeBalancerConfigs(Integer nodeBalancerId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetNodeBalancerConfigs200Response> localVarResp = getNodeBalancerConfigsWithHttpInfo(nodeBalancerId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Configs List
     * Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.  For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetNodeBalancerConfigs200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginted list of NodeBalancer Configs </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNodeBalancerConfigs200Response> getNodeBalancerConfigsWithHttpInfo(Integer nodeBalancerId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getNodeBalancerConfigsValidateBeforeCall(nodeBalancerId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetNodeBalancerConfigs200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Configs List (asynchronously)
     * Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.  For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginted list of NodeBalancer Configs </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerConfigsAsync(Integer nodeBalancerId, Integer page, Integer pageSize, final ApiCallback<GetNodeBalancerConfigs200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNodeBalancerConfigsValidateBeforeCall(nodeBalancerId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetNodeBalancerConfigs200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNodeBalancerNode
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerNodeCall(Integer nodeBalancerId, Integer configId, Integer nodeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()))
            .replace("{" + "nodeId" + "}", localVarApiClient.escapeString(nodeId.toString()));

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
    private okhttp3.Call getNodeBalancerNodeValidateBeforeCall(Integer nodeBalancerId, Integer configId, Integer nodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling getNodeBalancerNode(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling getNodeBalancerNode(Async)");
        }

        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling getNodeBalancerNode(Async)");
        }

        return getNodeBalancerNodeCall(nodeBalancerId, configId, nodeId, _callback);

    }

    /**
     * Node View
     * Returns information about a single Node, a backend for this NodeBalancer&#39;s configured port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @return NodeBalancerNode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerNode getNodeBalancerNode(Integer nodeBalancerId, Integer configId, Integer nodeId) throws ApiException {
        ApiResponse<NodeBalancerNode> localVarResp = getNodeBalancerNodeWithHttpInfo(nodeBalancerId, configId, nodeId);
        return localVarResp.getData();
    }

    /**
     * Node View
     * Returns information about a single Node, a backend for this NodeBalancer&#39;s configured port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @return ApiResponse&lt;NodeBalancerNode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerNode> getNodeBalancerNodeWithHttpInfo(Integer nodeBalancerId, Integer configId, Integer nodeId) throws ApiException {
        okhttp3.Call localVarCall = getNodeBalancerNodeValidateBeforeCall(nodeBalancerId, configId, nodeId, null);
        Type localVarReturnType = new TypeToken<NodeBalancerNode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node View (asynchronously)
     * Returns information about a single Node, a backend for this NodeBalancer&#39;s configured port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancer nodes. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancerNodeAsync(Integer nodeBalancerId, Integer configId, Integer nodeId, final ApiCallback<NodeBalancerNode> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNodeBalancerNodeValidateBeforeCall(nodeBalancerId, configId, nodeId, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerNode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNodeBalancers
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancers. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancersCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers";

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
    private okhttp3.Call getNodeBalancersValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getNodeBalancersCall(page, pageSize, _callback);

    }

    /**
     * NodeBalancers List
     * Returns a paginated list of NodeBalancers you have access to. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetLinodeNodeBalancers200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancers. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLinodeNodeBalancers200Response getNodeBalancers(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetLinodeNodeBalancers200Response> localVarResp = getNodeBalancersWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * NodeBalancers List
     * Returns a paginated list of NodeBalancers you have access to. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetLinodeNodeBalancers200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancers. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLinodeNodeBalancers200Response> getNodeBalancersWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getNodeBalancersValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetLinodeNodeBalancers200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * NodeBalancers List (asynchronously)
     * Returns a paginated list of NodeBalancers you have access to. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of NodeBalancers. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNodeBalancersAsync(Integer page, Integer pageSize, final ApiCallback<GetLinodeNodeBalancers200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNodeBalancersValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetLinodeNodeBalancers200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for nodebalancersNodeBalancerIdStatsGet
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested stats. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call nodebalancersNodeBalancerIdStatsGetCall(Integer nodeBalancerId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodebalancers/{nodeBalancerId}/stats"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()));

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
    private okhttp3.Call nodebalancersNodeBalancerIdStatsGetValidateBeforeCall(Integer nodeBalancerId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling nodebalancersNodeBalancerIdStatsGet(Async)");
        }

        return nodebalancersNodeBalancerIdStatsGetCall(nodeBalancerId, _callback);

    }

    /**
     * NodeBalancer Statistics View
     * Returns detailed statistics about the requested NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @return NodeBalancerStats
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested stats. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerStats nodebalancersNodeBalancerIdStatsGet(Integer nodeBalancerId) throws ApiException {
        ApiResponse<NodeBalancerStats> localVarResp = nodebalancersNodeBalancerIdStatsGetWithHttpInfo(nodeBalancerId);
        return localVarResp.getData();
    }

    /**
     * NodeBalancer Statistics View
     * Returns detailed statistics about the requested NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @return ApiResponse&lt;NodeBalancerStats&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested stats. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerStats> nodebalancersNodeBalancerIdStatsGetWithHttpInfo(Integer nodeBalancerId) throws ApiException {
        okhttp3.Call localVarCall = nodebalancersNodeBalancerIdStatsGetValidateBeforeCall(nodeBalancerId, null);
        Type localVarReturnType = new TypeToken<NodeBalancerStats>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * NodeBalancer Statistics View (asynchronously)
     * Returns detailed statistics about the requested NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested stats. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call nodebalancersNodeBalancerIdStatsGetAsync(Integer nodeBalancerId, final ApiCallback<NodeBalancerStats> _callback) throws ApiException {

        okhttp3.Call localVarCall = nodebalancersNodeBalancerIdStatsGetValidateBeforeCall(nodeBalancerId, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerStats>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for rebuildNodeBalancerConfig
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access. (required)
     * @param rebuildNodeBalancerConfigRequest Information about the NodeBalancer Config to rebuild.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rebuildNodeBalancerConfigCall(Integer nodeBalancerId, Integer configId, RebuildNodeBalancerConfigRequest rebuildNodeBalancerConfigRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = rebuildNodeBalancerConfigRequest;

        // create path and map variables
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}/rebuild"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call rebuildNodeBalancerConfigValidateBeforeCall(Integer nodeBalancerId, Integer configId, RebuildNodeBalancerConfigRequest rebuildNodeBalancerConfigRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling rebuildNodeBalancerConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling rebuildNodeBalancerConfig(Async)");
        }

        // verify the required parameter 'rebuildNodeBalancerConfigRequest' is set
        if (rebuildNodeBalancerConfigRequest == null) {
            throw new ApiException("Missing the required parameter 'rebuildNodeBalancerConfigRequest' when calling rebuildNodeBalancerConfig(Async)");
        }

        return rebuildNodeBalancerConfigCall(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest, _callback);

    }

    /**
     * Config Rebuild
     * Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.  Use this command to update a NodeBalancer&#39;s Config and Nodes with a single request. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access. (required)
     * @param rebuildNodeBalancerConfigRequest Information about the NodeBalancer Config to rebuild.  (required)
     * @return NodeBalancerConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerConfig rebuildNodeBalancerConfig(Integer nodeBalancerId, Integer configId, RebuildNodeBalancerConfigRequest rebuildNodeBalancerConfigRequest) throws ApiException {
        ApiResponse<NodeBalancerConfig> localVarResp = rebuildNodeBalancerConfigWithHttpInfo(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest);
        return localVarResp.getData();
    }

    /**
     * Config Rebuild
     * Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.  Use this command to update a NodeBalancer&#39;s Config and Nodes with a single request. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access. (required)
     * @param rebuildNodeBalancerConfigRequest Information about the NodeBalancer Config to rebuild.  (required)
     * @return ApiResponse&lt;NodeBalancerConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerConfig> rebuildNodeBalancerConfigWithHttpInfo(Integer nodeBalancerId, Integer configId, RebuildNodeBalancerConfigRequest rebuildNodeBalancerConfigRequest) throws ApiException {
        okhttp3.Call localVarCall = rebuildNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest, null);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Config Rebuild (asynchronously)
     * Rebuilds a NodeBalancer Config and its Nodes that you have permission to modify.  Use this command to update a NodeBalancer&#39;s Config and Nodes with a single request. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access. (required)
     * @param rebuildNodeBalancerConfigRequest Information about the NodeBalancer Config to rebuild.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rebuildNodeBalancerConfigAsync(Integer nodeBalancerId, Integer configId, RebuildNodeBalancerConfigRequest rebuildNodeBalancerConfigRequest, final ApiCallback<NodeBalancerConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = rebuildNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, rebuildNodeBalancerConfigRequest, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNodeBalancer
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancer The information to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNodeBalancerCall(Integer nodeBalancerId, NodeBalancer nodeBalancer, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = nodeBalancer;

        // create path and map variables
        String localVarPath = "/nodebalancers/{nodeBalancerId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()));

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
    private okhttp3.Call updateNodeBalancerValidateBeforeCall(Integer nodeBalancerId, NodeBalancer nodeBalancer, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling updateNodeBalancer(Async)");
        }

        // verify the required parameter 'nodeBalancer' is set
        if (nodeBalancer == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancer' when calling updateNodeBalancer(Async)");
        }

        return updateNodeBalancerCall(nodeBalancerId, nodeBalancer, _callback);

    }

    /**
     * NodeBalancer Update
     * Updates information about a NodeBalancer you can access. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancer The information to update. (required)
     * @return NodeBalancer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancer updateNodeBalancer(Integer nodeBalancerId, NodeBalancer nodeBalancer) throws ApiException {
        ApiResponse<NodeBalancer> localVarResp = updateNodeBalancerWithHttpInfo(nodeBalancerId, nodeBalancer);
        return localVarResp.getData();
    }

    /**
     * NodeBalancer Update
     * Updates information about a NodeBalancer you can access. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancer The information to update. (required)
     * @return ApiResponse&lt;NodeBalancer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancer> updateNodeBalancerWithHttpInfo(Integer nodeBalancerId, NodeBalancer nodeBalancer) throws ApiException {
        okhttp3.Call localVarCall = updateNodeBalancerValidateBeforeCall(nodeBalancerId, nodeBalancer, null);
        Type localVarReturnType = new TypeToken<NodeBalancer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * NodeBalancer Update (asynchronously)
     * Updates information about a NodeBalancer you can access. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param nodeBalancer The information to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> NodeBalancer updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNodeBalancerAsync(Integer nodeBalancerId, NodeBalancer nodeBalancer, final ApiCallback<NodeBalancer> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNodeBalancerValidateBeforeCall(nodeBalancerId, nodeBalancer, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNodeBalancerConfig
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param nodeBalancerConfig The fields to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNodeBalancerConfigCall(Integer nodeBalancerId, Integer configId, NodeBalancerConfig nodeBalancerConfig, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = nodeBalancerConfig;

        // create path and map variables
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
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
    private okhttp3.Call updateNodeBalancerConfigValidateBeforeCall(Integer nodeBalancerId, Integer configId, NodeBalancerConfig nodeBalancerConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling updateNodeBalancerConfig(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling updateNodeBalancerConfig(Async)");
        }

        // verify the required parameter 'nodeBalancerConfig' is set
        if (nodeBalancerConfig == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerConfig' when calling updateNodeBalancerConfig(Async)");
        }

        return updateNodeBalancerConfigCall(nodeBalancerId, configId, nodeBalancerConfig, _callback);

    }

    /**
     * Config Update
     * Updates the configuration for a single port on a NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param nodeBalancerConfig The fields to update. (required)
     * @return NodeBalancerConfig
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerConfig updateNodeBalancerConfig(Integer nodeBalancerId, Integer configId, NodeBalancerConfig nodeBalancerConfig) throws ApiException {
        ApiResponse<NodeBalancerConfig> localVarResp = updateNodeBalancerConfigWithHttpInfo(nodeBalancerId, configId, nodeBalancerConfig);
        return localVarResp.getData();
    }

    /**
     * Config Update
     * Updates the configuration for a single port on a NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param nodeBalancerConfig The fields to update. (required)
     * @return ApiResponse&lt;NodeBalancerConfig&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerConfig> updateNodeBalancerConfigWithHttpInfo(Integer nodeBalancerId, Integer configId, NodeBalancerConfig nodeBalancerConfig) throws ApiException {
        okhttp3.Call localVarCall = updateNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, nodeBalancerConfig, null);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Config Update (asynchronously)
     * Updates the configuration for a single port on a NodeBalancer. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the config to access. (required)
     * @param nodeBalancerConfig The fields to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Config updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNodeBalancerConfigAsync(Integer nodeBalancerId, Integer configId, NodeBalancerConfig nodeBalancerConfig, final ApiCallback<NodeBalancerConfig> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNodeBalancerConfigValidateBeforeCall(nodeBalancerId, configId, nodeBalancerConfig, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerConfig>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNodeBalancerNode
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param nodeBalancerNode The fields to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNodeBalancerNodeCall(Integer nodeBalancerId, Integer configId, Integer nodeId, NodeBalancerNode nodeBalancerNode, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = nodeBalancerNode;

        // create path and map variables
        String localVarPath = "/nodebalancers/{nodeBalancerId}/configs/{configId}/nodes/{nodeId}"
            .replace("{" + "nodeBalancerId" + "}", localVarApiClient.escapeString(nodeBalancerId.toString()))
            .replace("{" + "configId" + "}", localVarApiClient.escapeString(configId.toString()))
            .replace("{" + "nodeId" + "}", localVarApiClient.escapeString(nodeId.toString()));

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
    private okhttp3.Call updateNodeBalancerNodeValidateBeforeCall(Integer nodeBalancerId, Integer configId, Integer nodeId, NodeBalancerNode nodeBalancerNode, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeBalancerId' is set
        if (nodeBalancerId == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerId' when calling updateNodeBalancerNode(Async)");
        }

        // verify the required parameter 'configId' is set
        if (configId == null) {
            throw new ApiException("Missing the required parameter 'configId' when calling updateNodeBalancerNode(Async)");
        }

        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling updateNodeBalancerNode(Async)");
        }

        // verify the required parameter 'nodeBalancerNode' is set
        if (nodeBalancerNode == null) {
            throw new ApiException("Missing the required parameter 'nodeBalancerNode' when calling updateNodeBalancerNode(Async)");
        }

        return updateNodeBalancerNodeCall(nodeBalancerId, configId, nodeId, nodeBalancerNode, _callback);

    }

    /**
     * Node Update
     * Updates information about a Node, a backend for this NodeBalancer&#39;s configured port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param nodeBalancerNode The fields to update. (required)
     * @return NodeBalancerNode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public NodeBalancerNode updateNodeBalancerNode(Integer nodeBalancerId, Integer configId, Integer nodeId, NodeBalancerNode nodeBalancerNode) throws ApiException {
        ApiResponse<NodeBalancerNode> localVarResp = updateNodeBalancerNodeWithHttpInfo(nodeBalancerId, configId, nodeId, nodeBalancerNode);
        return localVarResp.getData();
    }

    /**
     * Node Update
     * Updates information about a Node, a backend for this NodeBalancer&#39;s configured port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param nodeBalancerNode The fields to update. (required)
     * @return ApiResponse&lt;NodeBalancerNode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<NodeBalancerNode> updateNodeBalancerNodeWithHttpInfo(Integer nodeBalancerId, Integer configId, Integer nodeId, NodeBalancerNode nodeBalancerNode) throws ApiException {
        okhttp3.Call localVarCall = updateNodeBalancerNodeValidateBeforeCall(nodeBalancerId, configId, nodeId, nodeBalancerNode, null);
        Type localVarReturnType = new TypeToken<NodeBalancerNode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Update (asynchronously)
     * Updates information about a Node, a backend for this NodeBalancer&#39;s configured port. 
     * @param nodeBalancerId The ID of the NodeBalancer to access. (required)
     * @param configId The ID of the Config to access (required)
     * @param nodeId The ID of the Node to access (required)
     * @param nodeBalancerNode The fields to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNodeBalancerNodeAsync(Integer nodeBalancerId, Integer configId, Integer nodeId, NodeBalancerNode nodeBalancerNode, final ApiCallback<NodeBalancerNode> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNodeBalancerNodeValidateBeforeCall(nodeBalancerId, configId, nodeId, nodeBalancerNode, _callback);
        Type localVarReturnType = new TypeToken<NodeBalancerNode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
