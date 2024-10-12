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


import org.openapitools.client.model.CreateLKEClusterRequest;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetLKEClusterAPIEndpoints200Response;
import org.openapitools.client.model.GetLKEClusterDashboard200Response;
import org.openapitools.client.model.GetLKEClusterKubeconfig200Response;
import org.openapitools.client.model.GetLKEClusterNode200Response;
import org.openapitools.client.model.GetLKEClusterPools200Response;
import org.openapitools.client.model.GetLKEClusters200Response;
import org.openapitools.client.model.GetLKEVersions200Response;
import org.openapitools.client.model.LKECluster;
import org.openapitools.client.model.LKENodePool;
import org.openapitools.client.model.LKENodePoolRequestBody;
import org.openapitools.client.model.LKEVersion;
import org.openapitools.client.model.PostLKEClusterRegenerateRequest;
import org.openapitools.client.model.PutLKECluster200Response;
import org.openapitools.client.model.PutLKEClusterRequest;
import org.openapitools.client.model.PutLKENodePoolRequest;
import org.openapitools.client.model.UNKNOWN_BASE_TYPE;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LinodeKubernetesEngineLkeApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LinodeKubernetesEngineLkeApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LinodeKubernetesEngineLkeApi(ApiClient apiClient) {
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
     * Build call for createLKECluster
     * @param createLKEClusterRequest Configuration for the Kubernetes cluster (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubernetes cluster creation has started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createLKEClusterCall(CreateLKEClusterRequest createLKEClusterRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createLKEClusterRequest;

        // create path and map variables
        String localVarPath = "/lke/clusters";

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
    private okhttp3.Call createLKEClusterValidateBeforeCall(CreateLKEClusterRequest createLKEClusterRequest, final ApiCallback _callback) throws ApiException {
        return createLKEClusterCall(createLKEClusterRequest, _callback);

    }

    /**
     * Kubernetes Cluster Create
     * Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster are ready. 
     * @param createLKEClusterRequest Configuration for the Kubernetes cluster (optional)
     * @return LKECluster
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubernetes cluster creation has started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LKECluster createLKECluster(CreateLKEClusterRequest createLKEClusterRequest) throws ApiException {
        ApiResponse<LKECluster> localVarResp = createLKEClusterWithHttpInfo(createLKEClusterRequest);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Cluster Create
     * Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster are ready. 
     * @param createLKEClusterRequest Configuration for the Kubernetes cluster (optional)
     * @return ApiResponse&lt;LKECluster&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubernetes cluster creation has started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LKECluster> createLKEClusterWithHttpInfo(CreateLKEClusterRequest createLKEClusterRequest) throws ApiException {
        okhttp3.Call localVarCall = createLKEClusterValidateBeforeCall(createLKEClusterRequest, null);
        Type localVarReturnType = new TypeToken<LKECluster>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Cluster Create (asynchronously)
     * Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster are ready. 
     * @param createLKEClusterRequest Configuration for the Kubernetes cluster (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubernetes cluster creation has started. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createLKEClusterAsync(CreateLKEClusterRequest createLKEClusterRequest, final ApiCallback<LKECluster> _callback) throws ApiException {

        okhttp3.Call localVarCall = createLKEClusterValidateBeforeCall(createLKEClusterRequest, _callback);
        Type localVarReturnType = new TypeToken<LKECluster>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLKECluster
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
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
    public okhttp3.Call deleteLKEClusterCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteLKEClusterValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling deleteLKECluster(Async)");
        }

        return deleteLKEClusterCall(clusterId, _callback);

    }

    /**
     * Kubernetes Cluster Delete
     * Deletes a Cluster you have permission to &#x60;read_write&#x60;.  **Deleting a Cluster is a destructive action and cannot be undone.**  Deleting a Cluster:   - Deletes all Linodes in all pools within this Kubernetes cluster   - Deletes all supporting Kubernetes services for this Kubernetes     cluster (API server, etcd, etc)   - Deletes all NodeBalancers created by this Kubernetes cluster   - Does not delete any of the volumes created by this Kubernetes     cluster 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteLKECluster(Integer clusterId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteLKEClusterWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Cluster Delete
     * Deletes a Cluster you have permission to &#x60;read_write&#x60;.  **Deleting a Cluster is a destructive action and cannot be undone.**  Deleting a Cluster:   - Deletes all Linodes in all pools within this Kubernetes cluster   - Deletes all supporting Kubernetes services for this Kubernetes     cluster (API server, etcd, etc)   - Deletes all NodeBalancers created by this Kubernetes cluster   - Does not delete any of the volumes created by this Kubernetes     cluster 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteLKEClusterWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = deleteLKEClusterValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Cluster Delete (asynchronously)
     * Deletes a Cluster you have permission to &#x60;read_write&#x60;.  **Deleting a Cluster is a destructive action and cannot be undone.**  Deleting a Cluster:   - Deletes all Linodes in all pools within this Kubernetes cluster   - Deletes all supporting Kubernetes services for this Kubernetes     cluster (API server, etcd, etc)   - Deletes all NodeBalancers created by this Kubernetes cluster   - Does not delete any of the volumes created by this Kubernetes     cluster 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
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
    public okhttp3.Call deleteLKEClusterAsync(Integer clusterId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLKEClusterValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLKEClusterKubeconfig
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubeconfig file deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLKEClusterKubeconfigCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/kubeconfig"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteLKEClusterKubeconfigValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling deleteLKEClusterKubeconfig(Async)");
        }

        return deleteLKEClusterKubeconfigCall(clusterId, _callback);

    }

    /**
     * Kubeconfig Delete
     * Delete and regenerate the Kubeconfig file for a Cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubeconfig file deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteLKEClusterKubeconfig(Integer clusterId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteLKEClusterKubeconfigWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Kubeconfig Delete
     * Delete and regenerate the Kubeconfig file for a Cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubeconfig file deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteLKEClusterKubeconfigWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = deleteLKEClusterKubeconfigValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubeconfig Delete (asynchronously)
     * Delete and regenerate the Kubeconfig file for a Cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Kubeconfig file deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLKEClusterKubeconfigAsync(Integer clusterId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLKEClusterKubeconfigValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLKEClusterNode
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
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
    public okhttp3.Call deleteLKEClusterNodeCall(Integer clusterId, String nodeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/nodes/{nodeId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
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
    private okhttp3.Call deleteLKEClusterNodeValidateBeforeCall(Integer clusterId, String nodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling deleteLKEClusterNode(Async)");
        }

        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling deleteLKEClusterNode(Async)");
        }

        return deleteLKEClusterNodeCall(clusterId, nodeId, _callback);

    }

    /**
     * Node Delete
     * Deletes a specific Node from a Node Pool.  **Deleting a Node is a destructive action and cannot be undone.**  Deleting a Node will reduce the size of the Node Pool it belongs to. 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteLKEClusterNode(Integer clusterId, String nodeId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteLKEClusterNodeWithHttpInfo(clusterId, nodeId);
        return localVarResp.getData();
    }

    /**
     * Node Delete
     * Deletes a specific Node from a Node Pool.  **Deleting a Node is a destructive action and cannot be undone.**  Deleting a Node will reduce the size of the Node Pool it belongs to. 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteLKEClusterNodeWithHttpInfo(Integer clusterId, String nodeId) throws ApiException {
        okhttp3.Call localVarCall = deleteLKEClusterNodeValidateBeforeCall(clusterId, nodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Delete (asynchronously)
     * Deletes a specific Node from a Node Pool.  **Deleting a Node is a destructive action and cannot be undone.**  Deleting a Node will reduce the size of the Node Pool it belongs to. 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
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
    public okhttp3.Call deleteLKEClusterNodeAsync(Integer clusterId, String nodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLKEClusterNodeValidateBeforeCall(clusterId, nodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLKENodePool
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
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
    public okhttp3.Call deleteLKENodePoolCall(Integer clusterId, Integer poolId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/pools/{poolId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "poolId" + "}", localVarApiClient.escapeString(poolId.toString()));

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
    private okhttp3.Call deleteLKENodePoolValidateBeforeCall(Integer clusterId, Integer poolId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling deleteLKENodePool(Async)");
        }

        // verify the required parameter 'poolId' is set
        if (poolId == null) {
            throw new ApiException("Missing the required parameter 'poolId' when calling deleteLKENodePool(Async)");
        }

        return deleteLKENodePoolCall(clusterId, poolId, _callback);

    }

    /**
     * Node Pool Delete
     * Delete a specific Node Pool from a Kubernetes cluster.  **Deleting a Node Pool is a destructive action and cannot be undone.**  Deleting a Node Pool will delete all Linodes within that Pool. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteLKENodePool(Integer clusterId, Integer poolId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteLKENodePoolWithHttpInfo(clusterId, poolId);
        return localVarResp.getData();
    }

    /**
     * Node Pool Delete
     * Delete a specific Node Pool from a Kubernetes cluster.  **Deleting a Node Pool is a destructive action and cannot be undone.**  Deleting a Node Pool will delete all Linodes within that Pool. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Delete successful </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteLKENodePoolWithHttpInfo(Integer clusterId, Integer poolId) throws ApiException {
        okhttp3.Call localVarCall = deleteLKENodePoolValidateBeforeCall(clusterId, poolId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Pool Delete (asynchronously)
     * Delete a specific Node Pool from a Kubernetes cluster.  **Deleting a Node Pool is a destructive action and cannot be undone.**  Deleting a Node Pool will delete all Linodes within that Pool. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
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
    public okhttp3.Call deleteLKENodePoolAsync(Integer clusterId, Integer poolId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLKENodePoolValidateBeforeCall(clusterId, poolId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKECluster
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}"
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
    private okhttp3.Call getLKEClusterValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKECluster(Async)");
        }

        return getLKEClusterCall(clusterId, _callback);

    }

    /**
     * Kubernetes Cluster View
     * Get a specific Cluster by ID. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return LKECluster
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LKECluster getLKECluster(Integer clusterId) throws ApiException {
        ApiResponse<LKECluster> localVarResp = getLKEClusterWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Cluster View
     * Get a specific Cluster by ID. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;LKECluster&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LKECluster> getLKEClusterWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = getLKEClusterValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<LKECluster>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Cluster View (asynchronously)
     * Get a specific Cluster by ID. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterAsync(Integer clusterId, final ApiCallback<LKECluster> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClusterValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<LKECluster>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEClusterAPIEndpoints
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Kubernetes API server endpoints for this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterAPIEndpointsCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/api-endpoints"
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
    private okhttp3.Call getLKEClusterAPIEndpointsValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKEClusterAPIEndpoints(Async)");
        }

        return getLKEClusterAPIEndpointsCall(clusterId, _callback);

    }

    /**
     * Kubernetes API Endpoints List
     * List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return GetLKEClusterAPIEndpoints200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Kubernetes API server endpoints for this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEClusterAPIEndpoints200Response getLKEClusterAPIEndpoints(Integer clusterId) throws ApiException {
        ApiResponse<GetLKEClusterAPIEndpoints200Response> localVarResp = getLKEClusterAPIEndpointsWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Kubernetes API Endpoints List
     * List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;GetLKEClusterAPIEndpoints200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Kubernetes API server endpoints for this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEClusterAPIEndpoints200Response> getLKEClusterAPIEndpointsWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = getLKEClusterAPIEndpointsValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<GetLKEClusterAPIEndpoints200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes API Endpoints List (asynchronously)
     * List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Kubernetes API server endpoints for this cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterAPIEndpointsAsync(Integer clusterId, final ApiCallback<GetLKEClusterAPIEndpoints200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClusterAPIEndpointsValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<GetLKEClusterAPIEndpoints200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEClusterDashboard
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes Cluster Dashboard URL. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterDashboardCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/dashboard"
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
    private okhttp3.Call getLKEClusterDashboardValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKEClusterDashboard(Async)");
        }

        return getLKEClusterDashboardCall(clusterId, _callback);

    }

    /**
     * Kubernetes Cluster Dashboard URL View
     * Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either **Token** or **Kubeconfig** authentication, then select **Sign in**.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](/docs/guides/using-the-kubernetes-dashboard-on-lke/). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return GetLKEClusterDashboard200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes Cluster Dashboard URL. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEClusterDashboard200Response getLKEClusterDashboard(Integer clusterId) throws ApiException {
        ApiResponse<GetLKEClusterDashboard200Response> localVarResp = getLKEClusterDashboardWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Cluster Dashboard URL View
     * Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either **Token** or **Kubeconfig** authentication, then select **Sign in**.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](/docs/guides/using-the-kubernetes-dashboard-on-lke/). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;GetLKEClusterDashboard200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes Cluster Dashboard URL. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEClusterDashboard200Response> getLKEClusterDashboardWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = getLKEClusterDashboardValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<GetLKEClusterDashboard200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Cluster Dashboard URL View (asynchronously)
     * Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either **Token** or **Kubeconfig** authentication, then select **Sign in**.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](/docs/guides/using-the-kubernetes-dashboard-on-lke/). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes Cluster Dashboard URL. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterDashboardAsync(Integer clusterId, final ApiCallback<GetLKEClusterDashboard200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClusterDashboardValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<GetLKEClusterDashboard200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEClusterKubeconfig
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Base64-encoded Kubeconfig file for this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterKubeconfigCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/kubeconfig"
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
    private okhttp3.Call getLKEClusterKubeconfigValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKEClusterKubeconfig(Async)");
        }

        return getLKEClusterKubeconfigCall(clusterId, _callback);

    }

    /**
     * Kubeconfig View
     * Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return GetLKEClusterKubeconfig200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Base64-encoded Kubeconfig file for this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEClusterKubeconfig200Response getLKEClusterKubeconfig(Integer clusterId) throws ApiException {
        ApiResponse<GetLKEClusterKubeconfig200Response> localVarResp = getLKEClusterKubeconfigWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Kubeconfig View
     * Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;GetLKEClusterKubeconfig200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Base64-encoded Kubeconfig file for this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEClusterKubeconfig200Response> getLKEClusterKubeconfigWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = getLKEClusterKubeconfigValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<GetLKEClusterKubeconfig200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubeconfig View (asynchronously)
     * Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the Base64-encoded Kubeconfig file for this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterKubeconfigAsync(Integer clusterId, final ApiCallback<GetLKEClusterKubeconfig200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClusterKubeconfigValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<GetLKEClusterKubeconfig200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEClusterNode
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the values of a node object in the form that it appears currently in the node pool array. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterNodeCall(Integer clusterId, String nodeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/nodes/{nodeId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
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
    private okhttp3.Call getLKEClusterNodeValidateBeforeCall(Integer clusterId, String nodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKEClusterNode(Async)");
        }

        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling getLKEClusterNode(Async)");
        }

        return getLKEClusterNodeCall(clusterId, nodeId, _callback);

    }

    /**
     * Node View
     * Returns the values for a specified node object. 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
     * @return GetLKEClusterNode200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the values of a node object in the form that it appears currently in the node pool array. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEClusterNode200Response getLKEClusterNode(Integer clusterId, String nodeId) throws ApiException {
        ApiResponse<GetLKEClusterNode200Response> localVarResp = getLKEClusterNodeWithHttpInfo(clusterId, nodeId);
        return localVarResp.getData();
    }

    /**
     * Node View
     * Returns the values for a specified node object. 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
     * @return ApiResponse&lt;GetLKEClusterNode200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the values of a node object in the form that it appears currently in the node pool array. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEClusterNode200Response> getLKEClusterNodeWithHttpInfo(Integer clusterId, String nodeId) throws ApiException {
        okhttp3.Call localVarCall = getLKEClusterNodeValidateBeforeCall(clusterId, nodeId, null);
        Type localVarReturnType = new TypeToken<GetLKEClusterNode200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node View (asynchronously)
     * Returns the values for a specified node object. 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the values of a node object in the form that it appears currently in the node pool array. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterNodeAsync(Integer clusterId, String nodeId, final ApiCallback<GetLKEClusterNode200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClusterNodeValidateBeforeCall(clusterId, nodeId, _callback);
        Type localVarReturnType = new TypeToken<GetLKEClusterNode200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEClusterPools
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Pools in this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterPoolsCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/pools"
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
    private okhttp3.Call getLKEClusterPoolsValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKEClusterPools(Async)");
        }

        return getLKEClusterPoolsCall(clusterId, _callback);

    }

    /**
     * Node Pools List
     * Returns all active Node Pools on a Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return GetLKEClusterPools200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Pools in this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEClusterPools200Response getLKEClusterPools(Integer clusterId) throws ApiException {
        ApiResponse<GetLKEClusterPools200Response> localVarResp = getLKEClusterPoolsWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Node Pools List
     * Returns all active Node Pools on a Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @return ApiResponse&lt;GetLKEClusterPools200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Pools in this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEClusterPools200Response> getLKEClusterPoolsWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = getLKEClusterPoolsValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<GetLKEClusterPools200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Pools List (asynchronously)
     * Returns all active Node Pools on a Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Pools in this Kubernetes cluster. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClusterPoolsAsync(Integer clusterId, final ApiCallback<GetLKEClusterPools200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClusterPoolsValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<GetLKEClusterPools200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEClusters
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Kubernetes clusters on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClustersCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters";

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
    private okhttp3.Call getLKEClustersValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getLKEClustersCall(_callback);

    }

    /**
     * Kubernetes Clusters List
     * Lists current Kubernetes clusters available on your account. 
     * @return GetLKEClusters200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Kubernetes clusters on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEClusters200Response getLKEClusters() throws ApiException {
        ApiResponse<GetLKEClusters200Response> localVarResp = getLKEClustersWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Kubernetes Clusters List
     * Lists current Kubernetes clusters available on your account. 
     * @return ApiResponse&lt;GetLKEClusters200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Kubernetes clusters on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEClusters200Response> getLKEClustersWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getLKEClustersValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetLKEClusters200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Clusters List (asynchronously)
     * Lists current Kubernetes clusters available on your account. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns an array of all Kubernetes clusters on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEClustersAsync(final ApiCallback<GetLKEClusters200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEClustersValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetLKEClusters200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKENodePool
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Node Pool. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKENodePoolCall(Integer clusterId, Integer poolId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/pools/{poolId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "poolId" + "}", localVarApiClient.escapeString(poolId.toString()));

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
    private okhttp3.Call getLKENodePoolValidateBeforeCall(Integer clusterId, Integer poolId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling getLKENodePool(Async)");
        }

        // verify the required parameter 'poolId' is set
        if (poolId == null) {
            throw new ApiException("Missing the required parameter 'poolId' when calling getLKENodePool(Async)");
        }

        return getLKENodePoolCall(clusterId, poolId, _callback);

    }

    /**
     * Node Pool View
     * Get a specific Node Pool by ID. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @return LKENodePool
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Node Pool. </td><td>  -  </td></tr>
     </table>
     */
    public LKENodePool getLKENodePool(Integer clusterId, Integer poolId) throws ApiException {
        ApiResponse<LKENodePool> localVarResp = getLKENodePoolWithHttpInfo(clusterId, poolId);
        return localVarResp.getData();
    }

    /**
     * Node Pool View
     * Get a specific Node Pool by ID. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @return ApiResponse&lt;LKENodePool&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Node Pool. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LKENodePool> getLKENodePoolWithHttpInfo(Integer clusterId, Integer poolId) throws ApiException {
        okhttp3.Call localVarCall = getLKENodePoolValidateBeforeCall(clusterId, poolId, null);
        Type localVarReturnType = new TypeToken<LKENodePool>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Pool View (asynchronously)
     * Get a specific Node Pool by ID. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Node Pool. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKENodePoolAsync(Integer clusterId, Integer poolId, final ApiCallback<LKENodePool> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKENodePoolValidateBeforeCall(clusterId, poolId, _callback);
        Type localVarReturnType = new TypeToken<LKENodePool>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEVersion
     * @param version The LKE version to view. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes version object that is available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEVersionCall(String version, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/versions/{version}"
            .replace("{" + "version" + "}", localVarApiClient.escapeString(version.toString()));

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
    private okhttp3.Call getLKEVersionValidateBeforeCall(String version, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'version' is set
        if (version == null) {
            throw new ApiException("Missing the required parameter 'version' when calling getLKEVersion(Async)");
        }

        return getLKEVersionCall(version, _callback);

    }

    /**
     * Kubernetes Version View
     * View a Kubernetes version available for deployment to a Kubernetes cluster. 
     * @param version The LKE version to view. (required)
     * @return LKEVersion
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes version object that is available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LKEVersion getLKEVersion(String version) throws ApiException {
        ApiResponse<LKEVersion> localVarResp = getLKEVersionWithHttpInfo(version);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Version View
     * View a Kubernetes version available for deployment to a Kubernetes cluster. 
     * @param version The LKE version to view. (required)
     * @return ApiResponse&lt;LKEVersion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes version object that is available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LKEVersion> getLKEVersionWithHttpInfo(String version) throws ApiException {
        okhttp3.Call localVarCall = getLKEVersionValidateBeforeCall(version, null);
        Type localVarReturnType = new TypeToken<LKEVersion>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Version View (asynchronously)
     * View a Kubernetes version available for deployment to a Kubernetes cluster. 
     * @param version The LKE version to view. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a Kubernetes version object that is available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEVersionAsync(String version, final ApiCallback<LKEVersion> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEVersionValidateBeforeCall(version, _callback);
        Type localVarReturnType = new TypeToken<LKEVersion>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLKEVersions
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a list of Kubernetes versions available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEVersionsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/versions";

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
    private okhttp3.Call getLKEVersionsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getLKEVersionsCall(_callback);

    }

    /**
     * Kubernetes Versions List
     * List the Kubernetes versions available for deployment to a Kubernetes cluster. 
     * @return GetLKEVersions200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a list of Kubernetes versions available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetLKEVersions200Response getLKEVersions() throws ApiException {
        ApiResponse<GetLKEVersions200Response> localVarResp = getLKEVersionsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Kubernetes Versions List
     * List the Kubernetes versions available for deployment to a Kubernetes cluster. 
     * @return ApiResponse&lt;GetLKEVersions200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a list of Kubernetes versions available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLKEVersions200Response> getLKEVersionsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getLKEVersionsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetLKEVersions200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Versions List (asynchronously)
     * List the Kubernetes versions available for deployment to a Kubernetes cluster. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a list of Kubernetes versions available for deployment to a Kubernetes cluster.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLKEVersionsAsync(final ApiCallback<GetLKEVersions200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLKEVersionsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetLKEVersions200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postLKECServiceTokenDelete
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Service token deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKECServiceTokenDeleteCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/servicetoken"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postLKECServiceTokenDeleteValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling postLKECServiceTokenDelete(Async)");
        }

        return postLKECServiceTokenDeleteCall(clusterId, _callback);

    }

    /**
     * Service Token Delete
     * Delete and regenerate the service account token for a Cluster.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Service token deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postLKECServiceTokenDelete(Integer clusterId) throws ApiException {
        ApiResponse<Object> localVarResp = postLKECServiceTokenDeleteWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Service Token Delete
     * Delete and regenerate the service account token for a Cluster.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Service token deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postLKECServiceTokenDeleteWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = postLKECServiceTokenDeleteValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Service Token Delete (asynchronously)
     * Delete and regenerate the service account token for a Cluster.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Service token deleted and regenerated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKECServiceTokenDeleteAsync(Integer clusterId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postLKECServiceTokenDeleteValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postLKEClusterNodeRecycle
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to be recycled. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterNodeRecycleCall(Integer clusterId, String nodeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/nodes/{nodeId}/recycle"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postLKEClusterNodeRecycleValidateBeforeCall(Integer clusterId, String nodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling postLKEClusterNodeRecycle(Async)");
        }

        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling postLKEClusterNodeRecycle(Async)");
        }

        return postLKEClusterNodeRecycleCall(clusterId, nodeId, _callback);

    }

    /**
     * Node Recycle
     * Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to be recycled. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postLKEClusterNodeRecycle(Integer clusterId, String nodeId) throws ApiException {
        ApiResponse<Object> localVarResp = postLKEClusterNodeRecycleWithHttpInfo(clusterId, nodeId);
        return localVarResp.getData();
    }

    /**
     * Node Recycle
     * Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to be recycled. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postLKEClusterNodeRecycleWithHttpInfo(Integer clusterId, String nodeId) throws ApiException {
        okhttp3.Call localVarCall = postLKEClusterNodeRecycleValidateBeforeCall(clusterId, nodeId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Recycle (asynchronously)
     * Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster containing the Node. (required)
     * @param nodeId ID of the Node to be recycled. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterNodeRecycleAsync(Integer clusterId, String nodeId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postLKEClusterNodeRecycleValidateBeforeCall(clusterId, nodeId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postLKEClusterPoolRecycle
     * @param clusterId ID of the Kubernetes cluster this Node Pool is attached to. (required)
     * @param poolId ID of the Node Pool to be recycled. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterPoolRecycleCall(Integer clusterId, Integer poolId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/pools/{poolId}/recycle"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "poolId" + "}", localVarApiClient.escapeString(poolId.toString()));

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
    private okhttp3.Call postLKEClusterPoolRecycleValidateBeforeCall(Integer clusterId, Integer poolId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling postLKEClusterPoolRecycle(Async)");
        }

        // verify the required parameter 'poolId' is set
        if (poolId == null) {
            throw new ApiException("Missing the required parameter 'poolId' when calling postLKEClusterPoolRecycle(Async)");
        }

        return postLKEClusterPoolRecycleCall(clusterId, poolId, _callback);

    }

    /**
     * Node Pool Recycle
     * Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster this Node Pool is attached to. (required)
     * @param poolId ID of the Node Pool to be recycled. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postLKEClusterPoolRecycle(Integer clusterId, Integer poolId) throws ApiException {
        ApiResponse<Object> localVarResp = postLKEClusterPoolRecycleWithHttpInfo(clusterId, poolId);
        return localVarResp.getData();
    }

    /**
     * Node Pool Recycle
     * Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster this Node Pool is attached to. (required)
     * @param poolId ID of the Node Pool to be recycled. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postLKEClusterPoolRecycleWithHttpInfo(Integer clusterId, Integer poolId) throws ApiException {
        okhttp3.Call localVarCall = postLKEClusterPoolRecycleValidateBeforeCall(clusterId, poolId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Pool Recycle (asynchronously)
     * Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster this Node Pool is attached to. (required)
     * @param poolId ID of the Node Pool to be recycled. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterPoolRecycleAsync(Integer clusterId, Integer poolId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postLKEClusterPoolRecycleValidateBeforeCall(clusterId, poolId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postLKEClusterPools
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param UNKNOWN_BASE_TYPE Configuration for the Node Pool (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool has been created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterPoolsCall(Integer clusterId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/pools"
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
    private okhttp3.Call postLKEClusterPoolsValidateBeforeCall(Integer clusterId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling postLKEClusterPools(Async)");
        }

        // verify the required parameter 'UNKNOWN_BASE_TYPE' is set
        if (UNKNOWN_BASE_TYPE == null) {
            throw new ApiException("Missing the required parameter 'UNKNOWN_BASE_TYPE' when calling postLKEClusterPools(Async)");
        }

        return postLKEClusterPoolsCall(clusterId, UNKNOWN_BASE_TYPE, _callback);

    }

    /**
     * Node Pool Create
     * Creates a new Node Pool for the designated Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param UNKNOWN_BASE_TYPE Configuration for the Node Pool (required)
     * @return LKENodePool
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool has been created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public LKENodePool postLKEClusterPools(Integer clusterId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) throws ApiException {
        ApiResponse<LKENodePool> localVarResp = postLKEClusterPoolsWithHttpInfo(clusterId, UNKNOWN_BASE_TYPE);
        return localVarResp.getData();
    }

    /**
     * Node Pool Create
     * Creates a new Node Pool for the designated Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param UNKNOWN_BASE_TYPE Configuration for the Node Pool (required)
     * @return ApiResponse&lt;LKENodePool&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool has been created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LKENodePool> postLKEClusterPoolsWithHttpInfo(Integer clusterId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) throws ApiException {
        okhttp3.Call localVarCall = postLKEClusterPoolsValidateBeforeCall(clusterId, UNKNOWN_BASE_TYPE, null);
        Type localVarReturnType = new TypeToken<LKENodePool>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Pool Create (asynchronously)
     * Creates a new Node Pool for the designated Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param UNKNOWN_BASE_TYPE Configuration for the Node Pool (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool has been created. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterPoolsAsync(Integer clusterId, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE, final ApiCallback<LKENodePool> _callback) throws ApiException {

        okhttp3.Call localVarCall = postLKEClusterPoolsValidateBeforeCall(clusterId, UNKNOWN_BASE_TYPE, _callback);
        Type localVarReturnType = new TypeToken<LKENodePool>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postLKEClusterRecycle
     * @param clusterId ID of the Kubernetes cluster which contains nodes to be recycled. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterRecycleCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/lke/clusters/{clusterId}/recycle"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postLKEClusterRecycleValidateBeforeCall(Integer clusterId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling postLKEClusterRecycle(Async)");
        }

        return postLKEClusterRecycleCall(clusterId, _callback);

    }

    /**
     * Cluster Nodes Recycle
     * Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster&#39;s current Kubernetes minor release.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster which contains nodes to be recycled. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postLKEClusterRecycle(Integer clusterId) throws ApiException {
        ApiResponse<Object> localVarResp = postLKEClusterRecycleWithHttpInfo(clusterId);
        return localVarResp.getData();
    }

    /**
     * Cluster Nodes Recycle
     * Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster&#39;s current Kubernetes minor release.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster which contains nodes to be recycled. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postLKEClusterRecycleWithHttpInfo(Integer clusterId) throws ApiException {
        okhttp3.Call localVarCall = postLKEClusterRecycleValidateBeforeCall(clusterId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Cluster Nodes Recycle (asynchronously)
     * Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster&#39;s current Kubernetes minor release.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster which contains nodes to be recycled. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Recycle request succeeded and is in progress. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterRecycleAsync(Integer clusterId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postLKEClusterRecycleValidateBeforeCall(clusterId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postLKEClusterRegenerate
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @param postLKEClusterRegenerateRequest The Kubernetes Cluster Regenerate request object. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Regenerate request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterRegenerateCall(Integer clusterId, PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postLKEClusterRegenerateRequest;

        // create path and map variables
        String localVarPath = "/lke/clusters/{clusterId}/regenerate"
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
    private okhttp3.Call postLKEClusterRegenerateValidateBeforeCall(Integer clusterId, PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling postLKEClusterRegenerate(Async)");
        }

        return postLKEClusterRegenerateCall(clusterId, postLKEClusterRegenerateRequest, _callback);

    }

    /**
     * Kubernetes Cluster Regenerate
     * Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.  When using this command, at least one of &#x60;kubeconfig&#x60; or &#x60;servicetoken&#x60; is required.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @param postLKEClusterRegenerateRequest The Kubernetes Cluster Regenerate request object. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Regenerate request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postLKEClusterRegenerate(Integer clusterId, PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest) throws ApiException {
        ApiResponse<Object> localVarResp = postLKEClusterRegenerateWithHttpInfo(clusterId, postLKEClusterRegenerateRequest);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Cluster Regenerate
     * Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.  When using this command, at least one of &#x60;kubeconfig&#x60; or &#x60;servicetoken&#x60; is required.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @param postLKEClusterRegenerateRequest The Kubernetes Cluster Regenerate request object. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Regenerate request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postLKEClusterRegenerateWithHttpInfo(Integer clusterId, PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest) throws ApiException {
        okhttp3.Call localVarCall = postLKEClusterRegenerateValidateBeforeCall(clusterId, postLKEClusterRegenerateRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Cluster Regenerate (asynchronously)
     * Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.  When using this command, at least one of &#x60;kubeconfig&#x60; or &#x60;servicetoken&#x60; is required.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     * @param clusterId ID of the target Kubernetes cluster. (required)
     * @param postLKEClusterRegenerateRequest The Kubernetes Cluster Regenerate request object. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Regenerate request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postLKEClusterRegenerateAsync(Integer clusterId, PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postLKEClusterRegenerateValidateBeforeCall(clusterId, postLKEClusterRegenerateRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putLKECluster
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param putLKEClusterRequest The fields to update the Kubernetes cluster. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putLKEClusterCall(Integer clusterId, PutLKEClusterRequest putLKEClusterRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = putLKEClusterRequest;

        // create path and map variables
        String localVarPath = "/lke/clusters/{clusterId}"
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
    private okhttp3.Call putLKEClusterValidateBeforeCall(Integer clusterId, PutLKEClusterRequest putLKEClusterRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling putLKECluster(Async)");
        }

        return putLKEClusterCall(clusterId, putLKEClusterRequest, _callback);

    }

    /**
     * Kubernetes Cluster Update
     * Updates a Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param putLKEClusterRequest The fields to update the Kubernetes cluster. (optional)
     * @return PutLKECluster200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
     </table>
     */
    public PutLKECluster200Response putLKECluster(Integer clusterId, PutLKEClusterRequest putLKEClusterRequest) throws ApiException {
        ApiResponse<PutLKECluster200Response> localVarResp = putLKEClusterWithHttpInfo(clusterId, putLKEClusterRequest);
        return localVarResp.getData();
    }

    /**
     * Kubernetes Cluster Update
     * Updates a Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param putLKEClusterRequest The fields to update the Kubernetes cluster. (optional)
     * @return ApiResponse&lt;PutLKECluster200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PutLKECluster200Response> putLKEClusterWithHttpInfo(Integer clusterId, PutLKEClusterRequest putLKEClusterRequest) throws ApiException {
        okhttp3.Call localVarCall = putLKEClusterValidateBeforeCall(clusterId, putLKEClusterRequest, null);
        Type localVarReturnType = new TypeToken<PutLKECluster200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Kubernetes Cluster Update (asynchronously)
     * Updates a Kubernetes cluster. 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param putLKEClusterRequest The fields to update the Kubernetes cluster. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Kubernetes cluster. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putLKEClusterAsync(Integer clusterId, PutLKEClusterRequest putLKEClusterRequest, final ApiCallback<PutLKECluster200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = putLKEClusterValidateBeforeCall(clusterId, putLKEClusterRequest, _callback);
        Type localVarReturnType = new TypeToken<PutLKECluster200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putLKENodePool
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @param putLKENodePoolRequest The fields to update (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool was successfully modified. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putLKENodePoolCall(Integer clusterId, Integer poolId, PutLKENodePoolRequest putLKENodePoolRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = putLKENodePoolRequest;

        // create path and map variables
        String localVarPath = "/lke/clusters/{clusterId}/pools/{poolId}"
            .replace("{" + "clusterId" + "}", localVarApiClient.escapeString(clusterId.toString()))
            .replace("{" + "poolId" + "}", localVarApiClient.escapeString(poolId.toString()));

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
    private okhttp3.Call putLKENodePoolValidateBeforeCall(Integer clusterId, Integer poolId, PutLKENodePoolRequest putLKENodePoolRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterId' is set
        if (clusterId == null) {
            throw new ApiException("Missing the required parameter 'clusterId' when calling putLKENodePool(Async)");
        }

        // verify the required parameter 'poolId' is set
        if (poolId == null) {
            throw new ApiException("Missing the required parameter 'poolId' when calling putLKENodePool(Async)");
        }

        return putLKENodePoolCall(clusterId, poolId, putLKENodePoolRequest, _callback);

    }

    /**
     * Node Pool Update
     * Updates a Node Pool&#39;s count and autoscaler configuration.  Linodes will be created or deleted to match changes to the Node Pool&#39;s count.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @param putLKENodePoolRequest The fields to update (optional)
     * @return LKENodePool
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool was successfully modified. </td><td>  -  </td></tr>
     </table>
     */
    public LKENodePool putLKENodePool(Integer clusterId, Integer poolId, PutLKENodePoolRequest putLKENodePoolRequest) throws ApiException {
        ApiResponse<LKENodePool> localVarResp = putLKENodePoolWithHttpInfo(clusterId, poolId, putLKENodePoolRequest);
        return localVarResp.getData();
    }

    /**
     * Node Pool Update
     * Updates a Node Pool&#39;s count and autoscaler configuration.  Linodes will be created or deleted to match changes to the Node Pool&#39;s count.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @param putLKENodePoolRequest The fields to update (optional)
     * @return ApiResponse&lt;LKENodePool&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool was successfully modified. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LKENodePool> putLKENodePoolWithHttpInfo(Integer clusterId, Integer poolId, PutLKENodePoolRequest putLKENodePoolRequest) throws ApiException {
        okhttp3.Call localVarCall = putLKENodePoolValidateBeforeCall(clusterId, poolId, putLKENodePoolRequest, null);
        Type localVarReturnType = new TypeToken<LKENodePool>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Node Pool Update (asynchronously)
     * Updates a Node Pool&#39;s count and autoscaler configuration.  Linodes will be created or deleted to match changes to the Node Pool&#39;s count.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     * @param clusterId ID of the Kubernetes cluster to look up. (required)
     * @param poolId ID of the Pool to look up (required)
     * @param putLKENodePoolRequest The fields to update (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Node Pool was successfully modified. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putLKENodePoolAsync(Integer clusterId, Integer poolId, PutLKENodePoolRequest putLKENodePoolRequest, final ApiCallback<LKENodePool> _callback) throws ApiException {

        okhttp3.Call localVarCall = putLKENodePoolValidateBeforeCall(clusterId, poolId, putLKENodePoolRequest, _callback);
        Type localVarReturnType = new TypeToken<LKENodePool>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
