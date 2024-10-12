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


import org.openapitools.client.model.CloneDomainRequest;
import org.openapitools.client.model.Domain;
import org.openapitools.client.model.DomainRecord;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetDomainRecords200Response;
import org.openapitools.client.model.GetDomainZone200Response;
import org.openapitools.client.model.GetDomains200Response;
import org.openapitools.client.model.ImportDomainRequest;
import org.openapitools.client.model.UpdateDomainRecordRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DomainsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DomainsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DomainsApi(ApiClient apiClient) {
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
     * Build call for cloneDomain
     * @param domainId ID of the Domain to clone. (required)
     * @param cloneDomainRequest Information about the Domain to clone. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Domain in Linode&#39;s DNS Manager, based on a cloned Domain.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloneDomainCall(String domainId, CloneDomainRequest cloneDomainRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = cloneDomainRequest;

        // create path and map variables
        String localVarPath = "/domains/{domainId}/clone"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call cloneDomainValidateBeforeCall(String domainId, CloneDomainRequest cloneDomainRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling cloneDomain(Async)");
        }

        // verify the required parameter 'cloneDomainRequest' is set
        if (cloneDomainRequest == null) {
            throw new ApiException("Missing the required parameter 'cloneDomainRequest' when calling cloneDomain(Async)");
        }

        return cloneDomainCall(domainId, cloneDomainRequest, _callback);

    }

    /**
     * Domain Clone
     * Clones a Domain and all associated DNS records from a Domain that is registered in Linode&#39;s DNS manager. 
     * @param domainId ID of the Domain to clone. (required)
     * @param cloneDomainRequest Information about the Domain to clone. (required)
     * @return Domain
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Domain in Linode&#39;s DNS Manager, based on a cloned Domain.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Domain cloneDomain(String domainId, CloneDomainRequest cloneDomainRequest) throws ApiException {
        ApiResponse<Domain> localVarResp = cloneDomainWithHttpInfo(domainId, cloneDomainRequest);
        return localVarResp.getData();
    }

    /**
     * Domain Clone
     * Clones a Domain and all associated DNS records from a Domain that is registered in Linode&#39;s DNS manager. 
     * @param domainId ID of the Domain to clone. (required)
     * @param cloneDomainRequest Information about the Domain to clone. (required)
     * @return ApiResponse&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Domain in Linode&#39;s DNS Manager, based on a cloned Domain.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Domain> cloneDomainWithHttpInfo(String domainId, CloneDomainRequest cloneDomainRequest) throws ApiException {
        okhttp3.Call localVarCall = cloneDomainValidateBeforeCall(domainId, cloneDomainRequest, null);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Clone (asynchronously)
     * Clones a Domain and all associated DNS records from a Domain that is registered in Linode&#39;s DNS manager. 
     * @param domainId ID of the Domain to clone. (required)
     * @param cloneDomainRequest Information about the Domain to clone. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Domain in Linode&#39;s DNS Manager, based on a cloned Domain.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloneDomainAsync(String domainId, CloneDomainRequest cloneDomainRequest, final ApiCallback<Domain> _callback) throws ApiException {

        okhttp3.Call localVarCall = cloneDomainValidateBeforeCall(domainId, cloneDomainRequest, _callback);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createDomain
     * @param domain Information about the domain you are registering. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain added successfully.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDomainCall(Domain domain, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = domain;

        // create path and map variables
        String localVarPath = "/domains";

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
    private okhttp3.Call createDomainValidateBeforeCall(Domain domain, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling createDomain(Async)");
        }

        return createDomainCall(domain, _callback);

    }

    /**
     * Domain Create
     * Adds a new Domain to Linode&#39;s DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode&#39;s nameservers so that the records hosted here are used. 
     * @param domain Information about the domain you are registering. (required)
     * @return Domain
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain added successfully.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Domain createDomain(Domain domain) throws ApiException {
        ApiResponse<Domain> localVarResp = createDomainWithHttpInfo(domain);
        return localVarResp.getData();
    }

    /**
     * Domain Create
     * Adds a new Domain to Linode&#39;s DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode&#39;s nameservers so that the records hosted here are used. 
     * @param domain Information about the domain you are registering. (required)
     * @return ApiResponse&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain added successfully.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Domain> createDomainWithHttpInfo(Domain domain) throws ApiException {
        okhttp3.Call localVarCall = createDomainValidateBeforeCall(domain, null);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Create (asynchronously)
     * Adds a new Domain to Linode&#39;s DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode&#39;s nameservers so that the records hosted here are used. 
     * @param domain Information about the domain you are registering. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain added successfully.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDomainAsync(Domain domain, final ApiCallback<Domain> _callback) throws ApiException {

        okhttp3.Call localVarCall = createDomainValidateBeforeCall(domain, _callback);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createDomainRecord
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param domainRecord Information about the new Record to add.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDomainRecordCall(Integer domainId, DomainRecord domainRecord, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = domainRecord;

        // create path and map variables
        String localVarPath = "/domains/{domainId}/records"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call createDomainRecordValidateBeforeCall(Integer domainId, DomainRecord domainRecord, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling createDomainRecord(Async)");
        }

        // verify the required parameter 'domainRecord' is set
        if (domainRecord == null) {
            throw new ApiException("Missing the required parameter 'domainRecord' when calling createDomainRecord(Async)");
        }

        return createDomainRecordCall(domainId, domainRecord, _callback);

    }

    /**
     * Domain Record Create
     * Adds a new Domain Record to the zonefile this Domain represents.  Each domain can have up to 12,000 active records. 
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param domainRecord Information about the new Record to add.  (required)
     * @return DomainRecord
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DomainRecord createDomainRecord(Integer domainId, DomainRecord domainRecord) throws ApiException {
        ApiResponse<DomainRecord> localVarResp = createDomainRecordWithHttpInfo(domainId, domainRecord);
        return localVarResp.getData();
    }

    /**
     * Domain Record Create
     * Adds a new Domain Record to the zonefile this Domain represents.  Each domain can have up to 12,000 active records. 
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param domainRecord Information about the new Record to add.  (required)
     * @return ApiResponse&lt;DomainRecord&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DomainRecord> createDomainRecordWithHttpInfo(Integer domainId, DomainRecord domainRecord) throws ApiException {
        okhttp3.Call localVarCall = createDomainRecordValidateBeforeCall(domainId, domainRecord, null);
        Type localVarReturnType = new TypeToken<DomainRecord>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Record Create (asynchronously)
     * Adds a new Domain Record to the zonefile this Domain represents.  Each domain can have up to 12,000 active records. 
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param domainRecord Information about the new Record to add.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record created successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDomainRecordAsync(Integer domainId, DomainRecord domainRecord, final ApiCallback<DomainRecord> _callback) throws ApiException {

        okhttp3.Call localVarCall = createDomainRecordValidateBeforeCall(domainId, domainRecord, _callback);
        Type localVarReturnType = new TypeToken<DomainRecord>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDomain
     * @param domainId The ID of the Domain to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainCall(Integer domainId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call deleteDomainValidateBeforeCall(Integer domainId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling deleteDomain(Async)");
        }

        return deleteDomainCall(domainId, _callback);

    }

    /**
     * Domain Delete
     * Deletes a Domain from Linode&#39;s DNS Manager. The Domain will be removed from Linode&#39;s nameservers shortly after this operation completes. This also deletes all associated Domain Records. 
     * @param domainId The ID of the Domain to access. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDomain(Integer domainId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDomainWithHttpInfo(domainId);
        return localVarResp.getData();
    }

    /**
     * Domain Delete
     * Deletes a Domain from Linode&#39;s DNS Manager. The Domain will be removed from Linode&#39;s nameservers shortly after this operation completes. This also deletes all associated Domain Records. 
     * @param domainId The ID of the Domain to access. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDomainWithHttpInfo(Integer domainId) throws ApiException {
        okhttp3.Call localVarCall = deleteDomainValidateBeforeCall(domainId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Delete (asynchronously)
     * Deletes a Domain from Linode&#39;s DNS Manager. The Domain will be removed from Linode&#39;s nameservers shortly after this operation completes. This also deletes all associated Domain Records. 
     * @param domainId The ID of the Domain to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainAsync(Integer domainId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDomainValidateBeforeCall(domainId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDomainRecord
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Record deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainRecordCall(Integer domainId, Integer recordId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}/records/{recordId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()))
            .replace("{" + "recordId" + "}", localVarApiClient.escapeString(recordId.toString()));

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
    private okhttp3.Call deleteDomainRecordValidateBeforeCall(Integer domainId, Integer recordId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling deleteDomainRecord(Async)");
        }

        // verify the required parameter 'recordId' is set
        if (recordId == null) {
            throw new ApiException("Missing the required parameter 'recordId' when calling deleteDomainRecord(Async)");
        }

        return deleteDomainRecordCall(domainId, recordId, _callback);

    }

    /**
     * Domain Record Delete
     * Deletes a Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Record deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDomainRecord(Integer domainId, Integer recordId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDomainRecordWithHttpInfo(domainId, recordId);
        return localVarResp.getData();
    }

    /**
     * Domain Record Delete
     * Deletes a Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Record deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDomainRecordWithHttpInfo(Integer domainId, Integer recordId) throws ApiException {
        okhttp3.Call localVarCall = deleteDomainRecordValidateBeforeCall(domainId, recordId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Record Delete (asynchronously)
     * Deletes a Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Record deleted successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDomainRecordAsync(Integer domainId, Integer recordId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDomainRecordValidateBeforeCall(domainId, recordId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomain
     * @param domainId The ID of the Domain to access. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainCall(Integer domainId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call getDomainValidateBeforeCall(Integer domainId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling getDomain(Async)");
        }

        return getDomainCall(domainId, _callback);

    }

    /**
     * Domain View
     * This is a single Domain that you have registered in Linode&#39;s DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode&#39;s nameservers. 
     * @param domainId The ID of the Domain to access. (required)
     * @return Domain
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Domain getDomain(Integer domainId) throws ApiException {
        ApiResponse<Domain> localVarResp = getDomainWithHttpInfo(domainId);
        return localVarResp.getData();
    }

    /**
     * Domain View
     * This is a single Domain that you have registered in Linode&#39;s DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode&#39;s nameservers. 
     * @param domainId The ID of the Domain to access. (required)
     * @return ApiResponse&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Domain> getDomainWithHttpInfo(Integer domainId) throws ApiException {
        okhttp3.Call localVarCall = getDomainValidateBeforeCall(domainId, null);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain View (asynchronously)
     * This is a single Domain that you have registered in Linode&#39;s DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode&#39;s nameservers. 
     * @param domainId The ID of the Domain to access. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainAsync(Integer domainId, final ApiCallback<Domain> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainValidateBeforeCall(domainId, _callback);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomainRecord
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Domain Record object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainRecordCall(Integer domainId, Integer recordId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}/records/{recordId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()))
            .replace("{" + "recordId" + "}", localVarApiClient.escapeString(recordId.toString()));

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
    private okhttp3.Call getDomainRecordValidateBeforeCall(Integer domainId, Integer recordId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling getDomainRecord(Async)");
        }

        // verify the required parameter 'recordId' is set
        if (recordId == null) {
            throw new ApiException("Missing the required parameter 'recordId' when calling getDomainRecord(Async)");
        }

        return getDomainRecordCall(domainId, recordId, _callback);

    }

    /**
     * Domain Record View
     * View a single Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @return DomainRecord
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Domain Record object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DomainRecord getDomainRecord(Integer domainId, Integer recordId) throws ApiException {
        ApiResponse<DomainRecord> localVarResp = getDomainRecordWithHttpInfo(domainId, recordId);
        return localVarResp.getData();
    }

    /**
     * Domain Record View
     * View a single Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @return ApiResponse&lt;DomainRecord&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Domain Record object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DomainRecord> getDomainRecordWithHttpInfo(Integer domainId, Integer recordId) throws ApiException {
        okhttp3.Call localVarCall = getDomainRecordValidateBeforeCall(domainId, recordId, null);
        Type localVarReturnType = new TypeToken<DomainRecord>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Record View (asynchronously)
     * View a single Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Domain Record object. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainRecordAsync(Integer domainId, Integer recordId, final ApiCallback<DomainRecord> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainRecordValidateBeforeCall(domainId, recordId, _callback);
        Type localVarReturnType = new TypeToken<DomainRecord>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomainRecords
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Domain Records. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainRecordsCall(Integer domainId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}/records"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call getDomainRecordsValidateBeforeCall(Integer domainId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling getDomainRecords(Async)");
        }

        return getDomainRecordsCall(domainId, page, pageSize, _callback);

    }

    /**
     * Domain Records List
     * Returns a paginated list of Records configured on a Domain in Linode&#39;s DNS Manager. 
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDomainRecords200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Domain Records. </td><td>  -  </td></tr>
     </table>
     */
    public GetDomainRecords200Response getDomainRecords(Integer domainId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDomainRecords200Response> localVarResp = getDomainRecordsWithHttpInfo(domainId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Domain Records List
     * Returns a paginated list of Records configured on a Domain in Linode&#39;s DNS Manager. 
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDomainRecords200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Domain Records. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDomainRecords200Response> getDomainRecordsWithHttpInfo(Integer domainId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDomainRecordsValidateBeforeCall(domainId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDomainRecords200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Records List (asynchronously)
     * Returns a paginated list of Records configured on a Domain in Linode&#39;s DNS Manager. 
     * @param domainId The ID of the Domain we are accessing Records for. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Domain Records. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainRecordsAsync(Integer domainId, Integer page, Integer pageSize, final ApiCallback<GetDomainRecords200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainRecordsValidateBeforeCall(domainId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDomainRecords200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomainZone
     * @param domainId ID of the Domain. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array containing the lines of the domain zone file.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainZoneCall(String domainId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}/zone-file"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call getDomainZoneValidateBeforeCall(String domainId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling getDomainZone(Async)");
        }

        return getDomainZoneCall(domainId, _callback);

    }

    /**
     * Domain Zone File View
     * Returns the zone file for the last rendered zone for the specified domain. 
     * @param domainId ID of the Domain. (required)
     * @return GetDomainZone200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array containing the lines of the domain zone file.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDomainZone200Response getDomainZone(String domainId) throws ApiException {
        ApiResponse<GetDomainZone200Response> localVarResp = getDomainZoneWithHttpInfo(domainId);
        return localVarResp.getData();
    }

    /**
     * Domain Zone File View
     * Returns the zone file for the last rendered zone for the specified domain. 
     * @param domainId ID of the Domain. (required)
     * @return ApiResponse&lt;GetDomainZone200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array containing the lines of the domain zone file.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDomainZone200Response> getDomainZoneWithHttpInfo(String domainId) throws ApiException {
        okhttp3.Call localVarCall = getDomainZoneValidateBeforeCall(domainId, null);
        Type localVarReturnType = new TypeToken<GetDomainZone200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Zone File View (asynchronously)
     * Returns the zone file for the last rendered zone for the specified domain. 
     * @param domainId ID of the Domain. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array containing the lines of the domain zone file.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainZoneAsync(String domainId, final ApiCallback<GetDomainZone200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainZoneValidateBeforeCall(domainId, _callback);
        Type localVarReturnType = new TypeToken<GetDomainZone200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomains
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Domains you have registered. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainsCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains";

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
    private okhttp3.Call getDomainsValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDomainsCall(page, pageSize, _callback);

    }

    /**
     * Domains List
     * This is a collection of Domains that you have registered in Linode&#39;s DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode&#39;s nameservers. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDomains200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Domains you have registered. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDomains200Response getDomains(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDomains200Response> localVarResp = getDomainsWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Domains List
     * This is a collection of Domains that you have registered in Linode&#39;s DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode&#39;s nameservers. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDomains200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Domains you have registered. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDomains200Response> getDomainsWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDomainsValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDomains200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domains List (asynchronously)
     * This is a collection of Domains that you have registered in Linode&#39;s DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode&#39;s nameservers. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A paginated list of Domains you have registered. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainsAsync(Integer page, Integer pageSize, final ApiCallback<GetDomains200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainsValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDomains200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for importDomain
     * @param importDomainRequest Information about the Domain to import. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call importDomainCall(ImportDomainRequest importDomainRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = importDomainRequest;

        // create path and map variables
        String localVarPath = "/domains/import";

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
    private okhttp3.Call importDomainValidateBeforeCall(ImportDomainRequest importDomainRequest, final ApiCallback _callback) throws ApiException {
        return importDomainCall(importDomainRequest, _callback);

    }

    /**
     * Domain Import
     * Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:    - 96.126.114.97   - 96.126.114.98   - 2600:3c00::5e   - 2600:3c00::5f 
     * @param importDomainRequest Information about the Domain to import. (optional)
     * @return Domain
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Domain importDomain(ImportDomainRequest importDomainRequest) throws ApiException {
        ApiResponse<Domain> localVarResp = importDomainWithHttpInfo(importDomainRequest);
        return localVarResp.getData();
    }

    /**
     * Domain Import
     * Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:    - 96.126.114.97   - 96.126.114.98   - 2600:3c00::5e   - 2600:3c00::5f 
     * @param importDomainRequest Information about the Domain to import. (optional)
     * @return ApiResponse&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Domain> importDomainWithHttpInfo(ImportDomainRequest importDomainRequest) throws ApiException {
        okhttp3.Call localVarCall = importDomainValidateBeforeCall(importDomainRequest, null);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Import (asynchronously)
     * Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:    - 96.126.114.97   - 96.126.114.98   - 2600:3c00::5e   - 2600:3c00::5f 
     * @param importDomainRequest Information about the Domain to import. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A single Domain in Linode&#39;s DNS Manager.  </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call importDomainAsync(ImportDomainRequest importDomainRequest, final ApiCallback<Domain> _callback) throws ApiException {

        okhttp3.Call localVarCall = importDomainValidateBeforeCall(importDomainRequest, _callback);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateDomain
     * @param domainId The ID of the Domain to access. (required)
     * @param domain The Domain information to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain update successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDomainCall(Integer domainId, Domain domain, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = domain;

        // create path and map variables
        String localVarPath = "/domains/{domainId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

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
    private okhttp3.Call updateDomainValidateBeforeCall(Integer domainId, Domain domain, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling updateDomain(Async)");
        }

        // verify the required parameter 'domain' is set
        if (domain == null) {
            throw new ApiException("Missing the required parameter 'domain' when calling updateDomain(Async)");
        }

        return updateDomainCall(domainId, domain, _callback);

    }

    /**
     * Domain Update
     * Update information about a Domain in Linode&#39;s DNS Manager. 
     * @param domainId The ID of the Domain to access. (required)
     * @param domain The Domain information to update. (required)
     * @return Domain
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain update successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Domain updateDomain(Integer domainId, Domain domain) throws ApiException {
        ApiResponse<Domain> localVarResp = updateDomainWithHttpInfo(domainId, domain);
        return localVarResp.getData();
    }

    /**
     * Domain Update
     * Update information about a Domain in Linode&#39;s DNS Manager. 
     * @param domainId The ID of the Domain to access. (required)
     * @param domain The Domain information to update. (required)
     * @return ApiResponse&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain update successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Domain> updateDomainWithHttpInfo(Integer domainId, Domain domain) throws ApiException {
        okhttp3.Call localVarCall = updateDomainValidateBeforeCall(domainId, domain, null);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Update (asynchronously)
     * Update information about a Domain in Linode&#39;s DNS Manager. 
     * @param domainId The ID of the Domain to access. (required)
     * @param domain The Domain information to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain update successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDomainAsync(Integer domainId, Domain domain, final ApiCallback<Domain> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateDomainValidateBeforeCall(domainId, domain, _callback);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateDomainRecord
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param updateDomainRecordRequest The values to change. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDomainRecordCall(Integer domainId, Integer recordId, UpdateDomainRecordRequest updateDomainRecordRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateDomainRecordRequest;

        // create path and map variables
        String localVarPath = "/domains/{domainId}/records/{recordId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()))
            .replace("{" + "recordId" + "}", localVarApiClient.escapeString(recordId.toString()));

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
    private okhttp3.Call updateDomainRecordValidateBeforeCall(Integer domainId, Integer recordId, UpdateDomainRecordRequest updateDomainRecordRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling updateDomainRecord(Async)");
        }

        // verify the required parameter 'recordId' is set
        if (recordId == null) {
            throw new ApiException("Missing the required parameter 'recordId' when calling updateDomainRecord(Async)");
        }

        // verify the required parameter 'updateDomainRecordRequest' is set
        if (updateDomainRecordRequest == null) {
            throw new ApiException("Missing the required parameter 'updateDomainRecordRequest' when calling updateDomainRecord(Async)");
        }

        return updateDomainRecordCall(domainId, recordId, updateDomainRecordRequest, _callback);

    }

    /**
     * Domain Record Update
     * Updates a single Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param updateDomainRecordRequest The values to change. (required)
     * @return DomainRecord
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DomainRecord updateDomainRecord(Integer domainId, Integer recordId, UpdateDomainRecordRequest updateDomainRecordRequest) throws ApiException {
        ApiResponse<DomainRecord> localVarResp = updateDomainRecordWithHttpInfo(domainId, recordId, updateDomainRecordRequest);
        return localVarResp.getData();
    }

    /**
     * Domain Record Update
     * Updates a single Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param updateDomainRecordRequest The values to change. (required)
     * @return ApiResponse&lt;DomainRecord&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DomainRecord> updateDomainRecordWithHttpInfo(Integer domainId, Integer recordId, UpdateDomainRecordRequest updateDomainRecordRequest) throws ApiException {
        okhttp3.Call localVarCall = updateDomainRecordValidateBeforeCall(domainId, recordId, updateDomainRecordRequest, null);
        Type localVarReturnType = new TypeToken<DomainRecord>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Domain Record Update (asynchronously)
     * Updates a single Record on this Domain. 
     * @param domainId The ID of the Domain whose Record you are accessing. (required)
     * @param recordId The ID of the Record you are accessing. (required)
     * @param updateDomainRecordRequest The values to change. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Domain Record updated. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDomainRecordAsync(Integer domainId, Integer recordId, UpdateDomainRecordRequest updateDomainRecordRequest, final ApiCallback<DomainRecord> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateDomainRecordValidateBeforeCall(domainId, recordId, updateDomainRecordRequest, _callback);
        Type localVarReturnType = new TypeToken<DomainRecord>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
