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


import org.openapitools.client.model.CreateObjectStorageBucketRequest;
import org.openapitools.client.model.CreateObjectStorageObjectURL200Response;
import org.openapitools.client.model.CreateObjectStorageObjectURLRequest;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetObjectStorageBucketContent200Response;
import org.openapitools.client.model.GetObjectStorageBuckets200Response;
import org.openapitools.client.model.GetObjectStorageClusters200Response;
import org.openapitools.client.model.GetObjectStorageKeys200Response;
import org.openapitools.client.model.GetObjectStorageTransfer200Response;
import org.openapitools.client.model.ObjectStorageBucket;
import org.openapitools.client.model.ObjectStorageCluster;
import org.openapitools.client.model.ObjectStorageKey;
import org.openapitools.client.model.ObjectStorageSSL;
import org.openapitools.client.model.ObjectStorageSSLResponse;
import org.openapitools.client.model.UpdateObjectStorageBucketACLRequest;
import org.openapitools.client.model.UpdateObjectStorageBucketAccessRequest;
import org.openapitools.client.model.UpdateObjectStorageKeyRequest;
import org.openapitools.client.model.ViewObjectStorageBucketACL200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ObjectStorageApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ObjectStorageApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ObjectStorageApi(ApiClient apiClient) {
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
     * Build call for cancelObjectStorage
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Object Storage cancellation successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cancelObjectStorageCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/cancel";

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
    private okhttp3.Call cancelObjectStorageValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return cancelObjectStorageCall(_callback);

    }

    /**
     * Object Storage Cancel
     * Cancel Object Storage on an Account.  **Warning**: Removes all buckets and their contents from your Account. This data is irretrievable once removed. 
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Object Storage cancellation successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object cancelObjectStorage() throws ApiException {
        ApiResponse<Object> localVarResp = cancelObjectStorageWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Object Storage Cancel
     * Cancel Object Storage on an Account.  **Warning**: Removes all buckets and their contents from your Account. This data is irretrievable once removed. 
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Object Storage cancellation successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> cancelObjectStorageWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = cancelObjectStorageValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Cancel (asynchronously)
     * Cancel Object Storage on an Account.  **Warning**: Removes all buckets and their contents from your Account. This data is irretrievable once removed. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Object Storage cancellation successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cancelObjectStorageAsync(final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = cancelObjectStorageValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createObjectStorageBucket
     * @param createObjectStorageBucketRequest Information about the bucket you want to create.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The bucket created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageBucketCall(CreateObjectStorageBucketRequest createObjectStorageBucketRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createObjectStorageBucketRequest;

        // create path and map variables
        String localVarPath = "/object-storage/buckets";

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
    private okhttp3.Call createObjectStorageBucketValidateBeforeCall(CreateObjectStorageBucketRequest createObjectStorageBucketRequest, final ApiCallback _callback) throws ApiException {
        return createObjectStorageBucketCall(createObjectStorageBucketRequest, _callback);

    }

    /**
     * Object Storage Bucket Create
     * Creates an Object Storage Bucket in the specified cluster.  Accounts with negative balances cannot access this command.  If the bucket already exists and is owned by you, this endpoint returns a &#x60;200&#x60; response with that bucket as if it had just been created.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly. 
     * @param createObjectStorageBucketRequest Information about the bucket you want to create.  (optional)
     * @return ObjectStorageBucket
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The bucket created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageBucket createObjectStorageBucket(CreateObjectStorageBucketRequest createObjectStorageBucketRequest) throws ApiException {
        ApiResponse<ObjectStorageBucket> localVarResp = createObjectStorageBucketWithHttpInfo(createObjectStorageBucketRequest);
        return localVarResp.getData();
    }

    /**
     * Object Storage Bucket Create
     * Creates an Object Storage Bucket in the specified cluster.  Accounts with negative balances cannot access this command.  If the bucket already exists and is owned by you, this endpoint returns a &#x60;200&#x60; response with that bucket as if it had just been created.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly. 
     * @param createObjectStorageBucketRequest Information about the bucket you want to create.  (optional)
     * @return ApiResponse&lt;ObjectStorageBucket&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The bucket created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageBucket> createObjectStorageBucketWithHttpInfo(CreateObjectStorageBucketRequest createObjectStorageBucketRequest) throws ApiException {
        okhttp3.Call localVarCall = createObjectStorageBucketValidateBeforeCall(createObjectStorageBucketRequest, null);
        Type localVarReturnType = new TypeToken<ObjectStorageBucket>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Bucket Create (asynchronously)
     * Creates an Object Storage Bucket in the specified cluster.  Accounts with negative balances cannot access this command.  If the bucket already exists and is owned by you, this endpoint returns a &#x60;200&#x60; response with that bucket as if it had just been created.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly. 
     * @param createObjectStorageBucketRequest Information about the bucket you want to create.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The bucket created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageBucketAsync(CreateObjectStorageBucketRequest createObjectStorageBucketRequest, final ApiCallback<ObjectStorageBucket> _callback) throws ApiException {

        okhttp3.Call localVarCall = createObjectStorageBucketValidateBeforeCall(createObjectStorageBucketRequest, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageBucket>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createObjectStorageKeys
     * @param objectStorageKey The label of the key to create. This is used to identify the created key.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The new keypair.  **This is the only time** the secret key is returned. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageKeysCall(ObjectStorageKey objectStorageKey, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = objectStorageKey;

        // create path and map variables
        String localVarPath = "/object-storage/keys";

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
    private okhttp3.Call createObjectStorageKeysValidateBeforeCall(ObjectStorageKey objectStorageKey, final ApiCallback _callback) throws ApiException {
        return createObjectStorageKeysCall(objectStorageKey, _callback);

    }

    /**
     * Object Storage Key Create
     * Provisions a new Object Storage Key on your account.  Accounts with negative balances cannot access this command.  * To create a Limited Access Key with specific permissions, send a &#x60;bucket_access&#x60; array.  * To create a Limited Access Key without access to any buckets, send an empty &#x60;bucket_access&#x60; array.  * To create an Access Key with unlimited access to all clusters and all buckets, omit the &#x60;bucket_access&#x60; array. 
     * @param objectStorageKey The label of the key to create. This is used to identify the created key.  (optional)
     * @return ObjectStorageKey
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The new keypair.  **This is the only time** the secret key is returned. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageKey createObjectStorageKeys(ObjectStorageKey objectStorageKey) throws ApiException {
        ApiResponse<ObjectStorageKey> localVarResp = createObjectStorageKeysWithHttpInfo(objectStorageKey);
        return localVarResp.getData();
    }

    /**
     * Object Storage Key Create
     * Provisions a new Object Storage Key on your account.  Accounts with negative balances cannot access this command.  * To create a Limited Access Key with specific permissions, send a &#x60;bucket_access&#x60; array.  * To create a Limited Access Key without access to any buckets, send an empty &#x60;bucket_access&#x60; array.  * To create an Access Key with unlimited access to all clusters and all buckets, omit the &#x60;bucket_access&#x60; array. 
     * @param objectStorageKey The label of the key to create. This is used to identify the created key.  (optional)
     * @return ApiResponse&lt;ObjectStorageKey&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The new keypair.  **This is the only time** the secret key is returned. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageKey> createObjectStorageKeysWithHttpInfo(ObjectStorageKey objectStorageKey) throws ApiException {
        okhttp3.Call localVarCall = createObjectStorageKeysValidateBeforeCall(objectStorageKey, null);
        Type localVarReturnType = new TypeToken<ObjectStorageKey>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Key Create (asynchronously)
     * Provisions a new Object Storage Key on your account.  Accounts with negative balances cannot access this command.  * To create a Limited Access Key with specific permissions, send a &#x60;bucket_access&#x60; array.  * To create a Limited Access Key without access to any buckets, send an empty &#x60;bucket_access&#x60; array.  * To create an Access Key with unlimited access to all clusters and all buckets, omit the &#x60;bucket_access&#x60; array. 
     * @param objectStorageKey The label of the key to create. This is used to identify the created key.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The new keypair.  **This is the only time** the secret key is returned. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageKeysAsync(ObjectStorageKey objectStorageKey, final ApiCallback<ObjectStorageKey> _callback) throws ApiException {

        okhttp3.Call localVarCall = createObjectStorageKeysValidateBeforeCall(objectStorageKey, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageKey>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createObjectStorageObjectURL
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param createObjectStorageObjectURLRequest Information about the request to sign. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The URL with which to access your object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageObjectURLCall(String clusterId, String bucket, CreateObjectStorageObjectURLRequest createObjectStorageObjectURLRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createObjectStorageObjectURLRequest;

        // create path and map variables
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/object-url"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call createObjectStorageObjectURLValidateBeforeCall(String clusterId, String bucket, CreateObjectStorageObjectURLRequest createObjectStorageObjectURLRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling createObjectStorageObjectURL(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling createObjectStorageObjectURL(Async)");
        }

        return createObjectStorageObjectURLCall(clusterId, bucket, createObjectStorageObjectURLRequest, _callback);

    }

    /**
     * Object Storage Object URL Create
     * Creates a pre-signed URL to access a single Object in a bucket. This can be used to share objects, and also to create/delete objects by using the appropriate HTTP method in your request body&#39;s &#x60;method&#x60; parameter.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param createObjectStorageObjectURLRequest Information about the request to sign. (optional)
     * @return CreateObjectStorageObjectURL200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The URL with which to access your object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public CreateObjectStorageObjectURL200Response createObjectStorageObjectURL(String clusterId, String bucket, CreateObjectStorageObjectURLRequest createObjectStorageObjectURLRequest) throws ApiException {
        ApiResponse<CreateObjectStorageObjectURL200Response> localVarResp = createObjectStorageObjectURLWithHttpInfo(clusterId, bucket, createObjectStorageObjectURLRequest);
        return localVarResp.getData();
    }

    /**
     * Object Storage Object URL Create
     * Creates a pre-signed URL to access a single Object in a bucket. This can be used to share objects, and also to create/delete objects by using the appropriate HTTP method in your request body&#39;s &#x60;method&#x60; parameter.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param createObjectStorageObjectURLRequest Information about the request to sign. (optional)
     * @return ApiResponse&lt;CreateObjectStorageObjectURL200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The URL with which to access your object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateObjectStorageObjectURL200Response> createObjectStorageObjectURLWithHttpInfo(String clusterId, String bucket, CreateObjectStorageObjectURLRequest createObjectStorageObjectURLRequest) throws ApiException {
        okhttp3.Call localVarCall = createObjectStorageObjectURLValidateBeforeCall(clusterId, bucket, createObjectStorageObjectURLRequest, null);
        Type localVarReturnType = new TypeToken<CreateObjectStorageObjectURL200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Object URL Create (asynchronously)
     * Creates a pre-signed URL to access a single Object in a bucket. This can be used to share objects, and also to create/delete objects by using the appropriate HTTP method in your request body&#39;s &#x60;method&#x60; parameter.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param createObjectStorageObjectURLRequest Information about the request to sign. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The URL with which to access your object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageObjectURLAsync(String clusterId, String bucket, CreateObjectStorageObjectURLRequest createObjectStorageObjectURLRequest, final ApiCallback<CreateObjectStorageObjectURL200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createObjectStorageObjectURLValidateBeforeCall(clusterId, bucket, createObjectStorageObjectURLRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateObjectStorageObjectURL200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createObjectStorageSSL
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param objectStorageSSL Upload this TLS/SSL certificate with its corresponding secret key. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns whether this bucket has a corresponding TLS/SSL certificate that was uploaded by a user. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageSSLCall(String clusterId, String bucket, ObjectStorageSSL objectStorageSSL, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = objectStorageSSL;

        // create path and map variables
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/ssl"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call createObjectStorageSSLValidateBeforeCall(String clusterId, String bucket, ObjectStorageSSL objectStorageSSL, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling createObjectStorageSSL(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling createObjectStorageSSL(Async)");
        }

        return createObjectStorageSSLCall(clusterId, bucket, objectStorageSSL, _callback);

    }

    /**
     * Object Storage TLS/SSL Cert Upload
     * Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.   To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete) and upload a new one. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param objectStorageSSL Upload this TLS/SSL certificate with its corresponding secret key. (optional)
     * @return ObjectStorageSSLResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns whether this bucket has a corresponding TLS/SSL certificate that was uploaded by a user. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageSSLResponse createObjectStorageSSL(String clusterId, String bucket, ObjectStorageSSL objectStorageSSL) throws ApiException {
        ApiResponse<ObjectStorageSSLResponse> localVarResp = createObjectStorageSSLWithHttpInfo(clusterId, bucket, objectStorageSSL);
        return localVarResp.getData();
    }

    /**
     * Object Storage TLS/SSL Cert Upload
     * Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.   To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete) and upload a new one. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param objectStorageSSL Upload this TLS/SSL certificate with its corresponding secret key. (optional)
     * @return ApiResponse&lt;ObjectStorageSSLResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns whether this bucket has a corresponding TLS/SSL certificate that was uploaded by a user. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageSSLResponse> createObjectStorageSSLWithHttpInfo(String clusterId, String bucket, ObjectStorageSSL objectStorageSSL) throws ApiException {
        okhttp3.Call localVarCall = createObjectStorageSSLValidateBeforeCall(clusterId, bucket, objectStorageSSL, null);
        Type localVarReturnType = new TypeToken<ObjectStorageSSLResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage TLS/SSL Cert Upload (asynchronously)
     * Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.   To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete) and upload a new one. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param objectStorageSSL Upload this TLS/SSL certificate with its corresponding secret key. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns whether this bucket has a corresponding TLS/SSL certificate that was uploaded by a user. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createObjectStorageSSLAsync(String clusterId, String bucket, ObjectStorageSSL objectStorageSSL, final ApiCallback<ObjectStorageSSLResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createObjectStorageSSLValidateBeforeCall(clusterId, bucket, objectStorageSSL, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageSSLResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteObjectStorageBucket
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Bucket deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteObjectStorageBucketCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call deleteObjectStorageBucketValidateBeforeCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling deleteObjectStorageBucket(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling deleteObjectStorageBucket(Async)");
        }

        return deleteObjectStorageBucketCall(clusterId, bucket, _callback);

    }

    /**
     * Object Storage Bucket Remove
     * Removes a single bucket.  Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations can fail if the bucket contains too many objects. The recommended way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that remove all objects, then delete the bucket.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Bucket deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteObjectStorageBucket(String clusterId, String bucket) throws ApiException {
        ApiResponse<Object> localVarResp = deleteObjectStorageBucketWithHttpInfo(clusterId, bucket);
        return localVarResp.getData();
    }

    /**
     * Object Storage Bucket Remove
     * Removes a single bucket.  Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations can fail if the bucket contains too many objects. The recommended way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that remove all objects, then delete the bucket.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Bucket deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteObjectStorageBucketWithHttpInfo(String clusterId, String bucket) throws ApiException {
        okhttp3.Call localVarCall = deleteObjectStorageBucketValidateBeforeCall(clusterId, bucket, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Bucket Remove (asynchronously)
     * Removes a single bucket.  Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations can fail if the bucket contains too many objects. The recommended way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that remove all objects, then delete the bucket.  This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Bucket deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteObjectStorageBucketAsync(String clusterId, String bucket, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteObjectStorageBucketValidateBeforeCall(clusterId, bucket, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteObjectStorageKey
     * @param keyId The key to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteObjectStorageKeyCall(Integer keyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/keys/{keyId}"
            .replace("{" + "keyId" + "}", localVarApiClient.escapeString(keyId.toString()));

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
    private okhttp3.Call deleteObjectStorageKeyValidateBeforeCall(Integer keyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'keyId' is set
        if (keyId == null) {
            throw new ApiException("Missing the required parameter 'keyId' when calling deleteObjectStorageKey(Async)");
        }

        return deleteObjectStorageKeyCall(keyId, _callback);

    }

    /**
     * Object Storage Key Revoke
     * Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients. 
     * @param keyId The key to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteObjectStorageKey(Integer keyId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteObjectStorageKeyWithHttpInfo(keyId);
        return localVarResp.getData();
    }

    /**
     * Object Storage Key Revoke
     * Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients. 
     * @param keyId The key to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteObjectStorageKeyWithHttpInfo(Integer keyId) throws ApiException {
        okhttp3.Call localVarCall = deleteObjectStorageKeyValidateBeforeCall(keyId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Key Revoke (asynchronously)
     * Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients. 
     * @param keyId The key to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteObjectStorageKeyAsync(Integer keyId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteObjectStorageKeyValidateBeforeCall(keyId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteObjectStorageSSL
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteObjectStorageSSLCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/ssl"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call deleteObjectStorageSSLValidateBeforeCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling deleteObjectStorageSSL(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling deleteObjectStorageSSL(Async)");
        }

        return deleteObjectStorageSSLCall(clusterId, bucket, _callback);

    }

    /**
     * Object Storage TLS/SSL Cert Delete
     * Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteObjectStorageSSL(String clusterId, String bucket) throws ApiException {
        ApiResponse<Object> localVarResp = deleteObjectStorageSSLWithHttpInfo(clusterId, bucket);
        return localVarResp.getData();
    }

    /**
     * Object Storage TLS/SSL Cert Delete
     * Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteObjectStorageSSLWithHttpInfo(String clusterId, String bucket) throws ApiException {
        okhttp3.Call localVarCall = deleteObjectStorageSSLValidateBeforeCall(clusterId, bucket, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage TLS/SSL Cert Delete (asynchronously)
     * Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletes this Object Storage bucket&#39;s user uploaded TLS/SSL certificate and private key. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteObjectStorageSSLAsync(String clusterId, String bucket, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteObjectStorageSSLValidateBeforeCall(clusterId, bucket, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageBucket
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested bucket. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call getObjectStorageBucketValidateBeforeCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getObjectStorageBucket(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling getObjectStorageBucket(Async)");
        }

        return getObjectStorageBucketCall(clusterId, bucket, _callback);

    }

    /**
     * Object Storage Bucket View
     * Returns a single Object Storage Bucket.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return ObjectStorageBucket
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested bucket. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageBucket getObjectStorageBucket(String clusterId, String bucket) throws ApiException {
        ApiResponse<ObjectStorageBucket> localVarResp = getObjectStorageBucketWithHttpInfo(clusterId, bucket);
        return localVarResp.getData();
    }

    /**
     * Object Storage Bucket View
     * Returns a single Object Storage Bucket.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return ApiResponse&lt;ObjectStorageBucket&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested bucket. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageBucket> getObjectStorageBucketWithHttpInfo(String clusterId, String bucket) throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageBucketValidateBeforeCall(clusterId, bucket, null);
        Type localVarReturnType = new TypeToken<ObjectStorageBucket>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Bucket View (asynchronously)
     * Returns a single Object Storage Bucket.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested bucket. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketAsync(String clusterId, String bucket, final ApiCallback<ObjectStorageBucket> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageBucketValidateBeforeCall(clusterId, bucket, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageBucket>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageBucketContent
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param marker The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details.  (optional)
     * @param delimiter The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter.  (optional)
     * @param prefix Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem.  (optional)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> One page of the requested bucket&#39;s contents. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketContentCall(String clusterId, String bucket, String marker, String delimiter, String prefix, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/object-list"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (marker != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("marker", marker));
        }

        if (delimiter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("delimiter", delimiter));
        }

        if (prefix != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("prefix", prefix));
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
    private okhttp3.Call getObjectStorageBucketContentValidateBeforeCall(String clusterId, String bucket, String marker, String delimiter, String prefix, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getObjectStorageBucketContent(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling getObjectStorageBucketContent(Async)");
        }

        return getObjectStorageBucketContentCall(clusterId, bucket, marker, delimiter, prefix, pageSize, _callback);

    }

    /**
     * Object Storage Bucket Contents List
     * Returns the contents of a bucket. The contents are paginated using a &#x60;marker&#x60;, which is the name of the last object on the previous page.  Objects may be filtered by &#x60;prefix&#x60; and &#x60;delimiter&#x60; as well; see Query Parameters for more information.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param marker The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details.  (optional)
     * @param delimiter The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter.  (optional)
     * @param prefix Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem.  (optional)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetObjectStorageBucketContent200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> One page of the requested bucket&#39;s contents. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetObjectStorageBucketContent200Response getObjectStorageBucketContent(String clusterId, String bucket, String marker, String delimiter, String prefix, Integer pageSize) throws ApiException {
        ApiResponse<GetObjectStorageBucketContent200Response> localVarResp = getObjectStorageBucketContentWithHttpInfo(clusterId, bucket, marker, delimiter, prefix, pageSize);
        return localVarResp.getData();
    }

    /**
     * Object Storage Bucket Contents List
     * Returns the contents of a bucket. The contents are paginated using a &#x60;marker&#x60;, which is the name of the last object on the previous page.  Objects may be filtered by &#x60;prefix&#x60; and &#x60;delimiter&#x60; as well; see Query Parameters for more information.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param marker The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details.  (optional)
     * @param delimiter The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter.  (optional)
     * @param prefix Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem.  (optional)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetObjectStorageBucketContent200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> One page of the requested bucket&#39;s contents. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetObjectStorageBucketContent200Response> getObjectStorageBucketContentWithHttpInfo(String clusterId, String bucket, String marker, String delimiter, String prefix, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageBucketContentValidateBeforeCall(clusterId, bucket, marker, delimiter, prefix, pageSize, null);
        Type localVarReturnType = new TypeToken<GetObjectStorageBucketContent200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Bucket Contents List (asynchronously)
     * Returns the contents of a bucket. The contents are paginated using a &#x60;marker&#x60;, which is the name of the last object on the previous page.  Objects may be filtered by &#x60;prefix&#x60; and &#x60;delimiter&#x60; as well; see Query Parameters for more information.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param marker The \&quot;marker\&quot; for this request, which can be used to paginate through large buckets. Its value should be the value of the &#x60;next_marker&#x60; property returned with the last page. Listing bucket contents *does not* support arbitrary page access. See the &#x60;next_marker&#x60; property in the responses section for more details.  (optional)
     * @param delimiter The delimiter for object names; if given, object names will be returned up to the first occurrence of this character. This is most commonly used with the &#x60;/&#x60; character to allow bucket transversal in a manner similar to a filesystem, however any delimiter may be used. Use in conjunction with &#x60;prefix&#x60; to see object names past the first occurrence of the delimiter.  (optional)
     * @param prefix Filters objects returned to only those whose name start with the given prefix. Commonly used in conjunction with &#x60;delimiter&#x60; to allow transversal of bucket contents in a manner similar to a filesystem.  (optional)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> One page of the requested bucket&#39;s contents. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketContentAsync(String clusterId, String bucket, String marker, String delimiter, String prefix, Integer pageSize, final ApiCallback<GetObjectStorageBucketContent200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageBucketContentValidateBeforeCall(clusterId, bucket, marker, delimiter, prefix, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetObjectStorageBucketContent200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageBucketinCluster
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own in this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketinClusterCall(String clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()));

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
    private okhttp3.Call getObjectStorageBucketinClusterValidateBeforeCall(String clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getObjectStorageBucketinCluster(Async)");
        }

        return getObjectStorageBucketinClusterCall(clusterId, _callback);

    }

    /**
     * Object Storage Buckets in Cluster List
     * Returns a list of Buckets in this cluster belonging to this Account.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @return GetObjectStorageBuckets200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own in this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetObjectStorageBuckets200Response getObjectStorageBucketinCluster(String clusterId) throws ApiException {
        ApiResponse<GetObjectStorageBuckets200Response> localVarResp = getObjectStorageBucketinClusterWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Object Storage Buckets in Cluster List
     * Returns a list of Buckets in this cluster belonging to this Account.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @return ApiResponse&lt;GetObjectStorageBuckets200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own in this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetObjectStorageBuckets200Response> getObjectStorageBucketinClusterWithHttpInfo(String clusterId) throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageBucketinClusterValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<GetObjectStorageBuckets200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Buckets in Cluster List (asynchronously)
     * Returns a list of Buckets in this cluster belonging to this Account.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own in this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketinClusterAsync(String clusterId, final ApiCallback<GetObjectStorageBuckets200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageBucketinClusterValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<GetObjectStorageBuckets200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageBuckets
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets";

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
    private okhttp3.Call getObjectStorageBucketsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getObjectStorageBucketsCall(_callback);

    }

    /**
     * Object Storage Buckets List
     * Returns a paginated list of all Object Storage Buckets that you own.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly. 
     * @return GetObjectStorageBuckets200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetObjectStorageBuckets200Response getObjectStorageBuckets() throws ApiException {
        ApiResponse<GetObjectStorageBuckets200Response> localVarResp = getObjectStorageBucketsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Object Storage Buckets List
     * Returns a paginated list of all Object Storage Buckets that you own.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly. 
     * @return ApiResponse&lt;GetObjectStorageBuckets200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetObjectStorageBuckets200Response> getObjectStorageBucketsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageBucketsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetObjectStorageBuckets200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Buckets List (asynchronously)
     * Returns a paginated list of all Object Storage Buckets that you own.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of buckets you own. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageBucketsAsync(final ApiCallback<GetObjectStorageBuckets200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageBucketsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetObjectStorageBuckets200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageCluster
     * @param clusterId The ID of the Cluster. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Cluster </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageClusterCall(String clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/clusters/{clusterId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()));

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
    private okhttp3.Call getObjectStorageClusterValidateBeforeCall(String clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getObjectStorageCluster(Async)");
        }

        return getObjectStorageClusterCall(clusterId, _callback);

    }

    /**
     * Cluster View
     * Returns a single Object Storage Cluster. 
     * @param clusterId The ID of the Cluster. (required)
     * @return ObjectStorageCluster
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Cluster </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageCluster getObjectStorageCluster(String clusterId) throws ApiException {
        ApiResponse<ObjectStorageCluster> localVarResp = getObjectStorageClusterWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Cluster View
     * Returns a single Object Storage Cluster. 
     * @param clusterId The ID of the Cluster. (required)
     * @return ApiResponse&lt;ObjectStorageCluster&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Cluster </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageCluster> getObjectStorageClusterWithHttpInfo(String clusterId) throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageClusterValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<ObjectStorageCluster>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Cluster View (asynchronously)
     * Returns a single Object Storage Cluster. 
     * @param clusterId The ID of the Cluster. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The requested Cluster </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageClusterAsync(String clusterId, final ApiCallback<ObjectStorageCluster> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageClusterValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageCluster>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageClusters
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of available clusters. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageClustersCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/clusters";

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
    private okhttp3.Call getObjectStorageClustersValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getObjectStorageClustersCall(_callback);

    }

    /**
     * Clusters List
     * Returns a paginated list of Object Storage Clusters that are available for use.  Users can connect to the clusters with third party clients to create buckets and upload objects. 
     * @return GetObjectStorageClusters200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of available clusters. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetObjectStorageClusters200Response getObjectStorageClusters() throws ApiException {
        ApiResponse<GetObjectStorageClusters200Response> localVarResp = getObjectStorageClustersWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Clusters List
     * Returns a paginated list of Object Storage Clusters that are available for use.  Users can connect to the clusters with third party clients to create buckets and upload objects. 
     * @return ApiResponse&lt;GetObjectStorageClusters200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of available clusters. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetObjectStorageClusters200Response> getObjectStorageClustersWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageClustersValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetObjectStorageClusters200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Clusters List (asynchronously)
     * Returns a paginated list of Object Storage Clusters that are available for use.  Users can connect to the clusters with third party clients to create buckets and upload objects. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of available clusters. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageClustersAsync(final ApiCallback<GetObjectStorageClusters200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageClustersValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetObjectStorageClusters200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageKey
     * @param keyId The key to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The keypair </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageKeyCall(Integer keyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/keys/{keyId}"
            .replace("{" + "keyId" + "}", localVarApiClient.escapeString(keyId.toString()));

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
    private okhttp3.Call getObjectStorageKeyValidateBeforeCall(Integer keyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'keyId' is set
        if (keyId == null) {
            throw new ApiException("Missing the required parameter 'keyId' when calling getObjectStorageKey(Async)");
        }

        return getObjectStorageKeyCall(keyId, _callback);

    }

    /**
     * Object Storage Key View
     * Returns a single Object Storage Key provisioned for your account. 
     * @param keyId The key to look up. (required)
     * @return ObjectStorageKey
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The keypair </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageKey getObjectStorageKey(Integer keyId) throws ApiException {
        ApiResponse<ObjectStorageKey> localVarResp = getObjectStorageKeyWithHttpInfo(keyId);
        return localVarResp.getData();
    }

    /**
     * Object Storage Key View
     * Returns a single Object Storage Key provisioned for your account. 
     * @param keyId The key to look up. (required)
     * @return ApiResponse&lt;ObjectStorageKey&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The keypair </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageKey> getObjectStorageKeyWithHttpInfo(Integer keyId) throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageKeyValidateBeforeCall(keyId, null);
        Type localVarReturnType = new TypeToken<ObjectStorageKey>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Key View (asynchronously)
     * Returns a single Object Storage Key provisioned for your account. 
     * @param keyId The key to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The keypair </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageKeyAsync(Integer keyId, final ApiCallback<ObjectStorageKey> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageKeyValidateBeforeCall(keyId, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageKey>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageKeys
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Object Storage Keys </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageKeysCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/keys";

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
    private okhttp3.Call getObjectStorageKeysValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getObjectStorageKeysCall(_callback);

    }

    /**
     * Object Storage Keys List
     * Returns a paginated list of Object Storage Keys for authenticating to the Object Storage S3 API. 
     * @return GetObjectStorageKeys200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Object Storage Keys </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetObjectStorageKeys200Response getObjectStorageKeys() throws ApiException {
        ApiResponse<GetObjectStorageKeys200Response> localVarResp = getObjectStorageKeysWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Object Storage Keys List
     * Returns a paginated list of Object Storage Keys for authenticating to the Object Storage S3 API. 
     * @return ApiResponse&lt;GetObjectStorageKeys200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Object Storage Keys </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetObjectStorageKeys200Response> getObjectStorageKeysWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageKeysValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetObjectStorageKeys200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Keys List (asynchronously)
     * Returns a paginated list of Object Storage Keys for authenticating to the Object Storage S3 API. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Object Storage Keys </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageKeysAsync(final ApiCallback<GetObjectStorageKeys200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageKeysValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetObjectStorageKeys200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageSSL
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageSSLCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/ssl"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call getObjectStorageSSLValidateBeforeCall(String clusterId, String bucket, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getObjectStorageSSL(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling getObjectStorageSSL(Async)");
        }

        return getObjectStorageSSLCall(clusterId, bucket, _callback);

    }

    /**
     * Object Storage TLS/SSL Cert View
     * Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return ObjectStorageSSLResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageSSLResponse getObjectStorageSSL(String clusterId, String bucket) throws ApiException {
        ApiResponse<ObjectStorageSSLResponse> localVarResp = getObjectStorageSSLWithHttpInfo(clusterId, bucket);
        return localVarResp.getData();
    }

    /**
     * Object Storage TLS/SSL Cert View
     * Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @return ApiResponse&lt;ObjectStorageSSLResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageSSLResponse> getObjectStorageSSLWithHttpInfo(String clusterId, String bucket) throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageSSLValidateBeforeCall(clusterId, bucket, null);
        Type localVarReturnType = new TypeToken<ObjectStorageSSLResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage TLS/SSL Cert View (asynchronously)
     * Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageSSLAsync(String clusterId, String bucket, final ApiCallback<ObjectStorageSSLResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageSSLValidateBeforeCall(clusterId, bucket, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageSSLResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getObjectStorageTransfer
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the amount of outbound data transfer used by your account&#39;s Object Storage buckets.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageTransferCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/transfer";

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
    private okhttp3.Call getObjectStorageTransferValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getObjectStorageTransferCall(_callback);

    }

    /**
     * Object Storage Transfer View
     * The amount of outbound data transfer used by your account&#39;s Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas. 
     * @return GetObjectStorageTransfer200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the amount of outbound data transfer used by your account&#39;s Object Storage buckets.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetObjectStorageTransfer200Response getObjectStorageTransfer() throws ApiException {
        ApiResponse<GetObjectStorageTransfer200Response> localVarResp = getObjectStorageTransferWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Object Storage Transfer View
     * The amount of outbound data transfer used by your account&#39;s Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas. 
     * @return ApiResponse&lt;GetObjectStorageTransfer200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the amount of outbound data transfer used by your account&#39;s Object Storage buckets.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetObjectStorageTransfer200Response> getObjectStorageTransferWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getObjectStorageTransferValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetObjectStorageTransfer200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Transfer View (asynchronously)
     * The amount of outbound data transfer used by your account&#39;s Object Storage buckets. Object Storage adds 1 terabyte of outbound data transfer to your data transfer pool. See the [Object Storage Overview](/docs/products/storage/object-storage/#pricing) guide for details on Object Storage transfer quotas. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the amount of outbound data transfer used by your account&#39;s Object Storage buckets.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getObjectStorageTransferAsync(final ApiCallback<GetObjectStorageTransfer200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getObjectStorageTransferValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetObjectStorageTransfer200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for modifyObjectStorageBucketAccess
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call modifyObjectStorageBucketAccessCall(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateObjectStorageBucketAccessRequest;

        // create path and map variables
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/access"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call modifyObjectStorageBucketAccessValidateBeforeCall(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling modifyObjectStorageBucketAccess(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling modifyObjectStorageBucketAccess(Async)");
        }

        return modifyObjectStorageBucketAccessCall(clusterId, bucket, updateObjectStorageBucketAccessRequest, _callback);

    }

    /**
     * Object Storage Bucket Access Modify
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object modifyObjectStorageBucketAccess(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest) throws ApiException {
        ApiResponse<Object> localVarResp = modifyObjectStorageBucketAccessWithHttpInfo(clusterId, bucket, updateObjectStorageBucketAccessRequest);
        return localVarResp.getData();
    }

    /**
     * Object Storage Bucket Access Modify
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> modifyObjectStorageBucketAccessWithHttpInfo(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest) throws ApiException {
        okhttp3.Call localVarCall = modifyObjectStorageBucketAccessValidateBeforeCall(clusterId, bucket, updateObjectStorageBucketAccessRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Bucket Access Modify (asynchronously)
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call modifyObjectStorageBucketAccessAsync(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = modifyObjectStorageBucketAccessValidateBeforeCall(clusterId, bucket, updateObjectStorageBucketAccessRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateObjectStorageBucketACL
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketACLRequest The changes to make to this Object&#39;s access controls. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateObjectStorageBucketACLCall(String clusterId, String bucket, UpdateObjectStorageBucketACLRequest updateObjectStorageBucketACLRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateObjectStorageBucketACLRequest;

        // create path and map variables
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/object-acl"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call updateObjectStorageBucketACLValidateBeforeCall(String clusterId, String bucket, UpdateObjectStorageBucketACLRequest updateObjectStorageBucketACLRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling updateObjectStorageBucketACL(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling updateObjectStorageBucketACL(Async)");
        }

        return updateObjectStorageBucketACLCall(clusterId, bucket, updateObjectStorageBucketACLRequest, _callback);

    }

    /**
     * Object Storage Object ACL Config Update
     * Update an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketACLRequest The changes to make to this Object&#39;s access controls. (optional)
     * @return ViewObjectStorageBucketACL200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ViewObjectStorageBucketACL200Response updateObjectStorageBucketACL(String clusterId, String bucket, UpdateObjectStorageBucketACLRequest updateObjectStorageBucketACLRequest) throws ApiException {
        ApiResponse<ViewObjectStorageBucketACL200Response> localVarResp = updateObjectStorageBucketACLWithHttpInfo(clusterId, bucket, updateObjectStorageBucketACLRequest);
        return localVarResp.getData();
    }

    /**
     * Object Storage Object ACL Config Update
     * Update an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketACLRequest The changes to make to this Object&#39;s access controls. (optional)
     * @return ApiResponse&lt;ViewObjectStorageBucketACL200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ViewObjectStorageBucketACL200Response> updateObjectStorageBucketACLWithHttpInfo(String clusterId, String bucket, UpdateObjectStorageBucketACLRequest updateObjectStorageBucketACLRequest) throws ApiException {
        okhttp3.Call localVarCall = updateObjectStorageBucketACLValidateBeforeCall(clusterId, bucket, updateObjectStorageBucketACLRequest, null);
        Type localVarReturnType = new TypeToken<ViewObjectStorageBucketACL200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Object ACL Config Update (asynchronously)
     * Update an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketACLRequest The changes to make to this Object&#39;s access controls. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateObjectStorageBucketACLAsync(String clusterId, String bucket, UpdateObjectStorageBucketACLRequest updateObjectStorageBucketACLRequest, final ApiCallback<ViewObjectStorageBucketACL200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateObjectStorageBucketACLValidateBeforeCall(clusterId, bucket, updateObjectStorageBucketACLRequest, _callback);
        Type localVarReturnType = new TypeToken<ViewObjectStorageBucketACL200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateObjectStorageBucketAccess
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateObjectStorageBucketAccessCall(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateObjectStorageBucketAccessRequest;

        // create path and map variables
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/access"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

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
    private okhttp3.Call updateObjectStorageBucketAccessValidateBeforeCall(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling updateObjectStorageBucketAccess(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling updateObjectStorageBucketAccess(Async)");
        }

        return updateObjectStorageBucketAccessCall(clusterId, bucket, updateObjectStorageBucketAccessRequest, _callback);

    }

    /**
     * Object Storage Bucket Access Update
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object updateObjectStorageBucketAccess(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateObjectStorageBucketAccessWithHttpInfo(clusterId, bucket, updateObjectStorageBucketAccessRequest);
        return localVarResp.getData();
    }

    /**
     * Object Storage Bucket Access Update
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateObjectStorageBucketAccessWithHttpInfo(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest) throws ApiException {
        okhttp3.Call localVarCall = updateObjectStorageBucketAccessValidateBeforeCall(clusterId, bucket, updateObjectStorageBucketAccessRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Bucket Access Update (asynchronously)
     * Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings. Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.   For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param updateObjectStorageBucketAccessRequest The changes to make to the bucket&#39;s access controls. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Access controls updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateObjectStorageBucketAccessAsync(String clusterId, String bucket, UpdateObjectStorageBucketAccessRequest updateObjectStorageBucketAccessRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateObjectStorageBucketAccessValidateBeforeCall(clusterId, bucket, updateObjectStorageBucketAccessRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateObjectStorageKey
     * @param keyId The key to look up. (required)
     * @param updateObjectStorageKeyRequest The fields to update. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Update Successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateObjectStorageKeyCall(Integer keyId, UpdateObjectStorageKeyRequest updateObjectStorageKeyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateObjectStorageKeyRequest;

        // create path and map variables
        String localVarPath = "/object-storage/keys/{keyId}"
            .replace("{" + "keyId" + "}", localVarApiClient.escapeString(keyId.toString()));

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
    private okhttp3.Call updateObjectStorageKeyValidateBeforeCall(Integer keyId, UpdateObjectStorageKeyRequest updateObjectStorageKeyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'keyId' is set
        if (keyId == null) {
            throw new ApiException("Missing the required parameter 'keyId' when calling updateObjectStorageKey(Async)");
        }

        return updateObjectStorageKeyCall(keyId, updateObjectStorageKeyRequest, _callback);

    }

    /**
     * Object Storage Key Update
     * Updates an Object Storage Key on your account. 
     * @param keyId The key to look up. (required)
     * @param updateObjectStorageKeyRequest The fields to update. (optional)
     * @return ObjectStorageKey
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Update Successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ObjectStorageKey updateObjectStorageKey(Integer keyId, UpdateObjectStorageKeyRequest updateObjectStorageKeyRequest) throws ApiException {
        ApiResponse<ObjectStorageKey> localVarResp = updateObjectStorageKeyWithHttpInfo(keyId, updateObjectStorageKeyRequest);
        return localVarResp.getData();
    }

    /**
     * Object Storage Key Update
     * Updates an Object Storage Key on your account. 
     * @param keyId The key to look up. (required)
     * @param updateObjectStorageKeyRequest The fields to update. (optional)
     * @return ApiResponse&lt;ObjectStorageKey&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Update Successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ObjectStorageKey> updateObjectStorageKeyWithHttpInfo(Integer keyId, UpdateObjectStorageKeyRequest updateObjectStorageKeyRequest) throws ApiException {
        okhttp3.Call localVarCall = updateObjectStorageKeyValidateBeforeCall(keyId, updateObjectStorageKeyRequest, null);
        Type localVarReturnType = new TypeToken<ObjectStorageKey>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Key Update (asynchronously)
     * Updates an Object Storage Key on your account. 
     * @param keyId The key to look up. (required)
     * @param updateObjectStorageKeyRequest The fields to update. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Update Successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateObjectStorageKeyAsync(Integer keyId, UpdateObjectStorageKeyRequest updateObjectStorageKeyRequest, final ApiCallback<ObjectStorageKey> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateObjectStorageKeyValidateBeforeCall(keyId, updateObjectStorageKeyRequest, _callback);
        Type localVarReturnType = new TypeToken<ObjectStorageKey>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for viewObjectStorageBucketACL
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param name The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call viewObjectStorageBucketACLCall(String clusterId, String bucket, String name, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/object-storage/buckets/{clusterId}/{bucket}/object-acl"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "bucket" + "}", localVarApiClient.escapeString(bucket.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (name != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("name", name));
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
    private okhttp3.Call viewObjectStorageBucketACLValidateBeforeCall(String clusterId, String bucket, String name, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling viewObjectStorageBucketACL(Async)");
        }

        // verify the required parameter 'bucket' is set
        if (bucket == null) {
            throw new ApiException("Missing the required parameter 'bucket' when calling viewObjectStorageBucketACL(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling viewObjectStorageBucketACL(Async)");
        }

        return viewObjectStorageBucketACLCall(clusterId, bucket, name, _callback);

    }

    /**
     * Object Storage Object ACL Config View
     * View an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param name The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  (required)
     * @return ViewObjectStorageBucketACL200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ViewObjectStorageBucketACL200Response viewObjectStorageBucketACL(String clusterId, String bucket, String name) throws ApiException {
        ApiResponse<ViewObjectStorageBucketACL200Response> localVarResp = viewObjectStorageBucketACLWithHttpInfo(clusterId, bucket, name);
        return localVarResp.getData();
    }

    /**
     * Object Storage Object ACL Config View
     * View an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param name The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  (required)
     * @return ApiResponse&lt;ViewObjectStorageBucketACL200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ViewObjectStorageBucketACL200Response> viewObjectStorageBucketACLWithHttpInfo(String clusterId, String bucket, String name) throws ApiException {
        okhttp3.Call localVarCall = viewObjectStorageBucketACLValidateBeforeCall(clusterId, bucket, name, null);
        Type localVarReturnType = new TypeToken<ViewObjectStorageBucketACL200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Object Storage Object ACL Config View (asynchronously)
     * View an Object&#39;s configured Access Control List (ACL) in this Object Storage bucket. ACLs define who can access your buckets and objects and specify the level of access granted to those users.   This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly. 
     * @param clusterId The ID of the cluster this bucket exists in. (required)
     * @param bucket The bucket name. (required)
     * @param name The &#x60;name&#x60; of the object for which to retrieve its Access Control List (ACL). Use the [Object Storage Bucket Contents List](/docs/api/object-storage/#object-storage-bucket-contents-list) endpoint to access all object names in a bucket.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The Object&#39;s canned ACL and policy. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call viewObjectStorageBucketACLAsync(String clusterId, String bucket, String name, final ApiCallback<ViewObjectStorageBucketACL200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = viewObjectStorageBucketACLValidateBeforeCall(clusterId, bucket, name, _callback);
        Type localVarReturnType = new TypeToken<ViewObjectStorageBucketACL200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
