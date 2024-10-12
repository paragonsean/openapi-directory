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


import org.openapitools.client.model.DatabaseBackup;
import org.openapitools.client.model.DatabaseBackupSnapshot;
import org.openapitools.client.model.DatabaseCredentials;
import org.openapitools.client.model.DatabaseEngine;
import org.openapitools.client.model.DatabaseMongoDB;
import org.openapitools.client.model.DatabaseMySQL;
import org.openapitools.client.model.DatabaseMySQLRequest;
import org.openapitools.client.model.DatabasePostgreSQL;
import org.openapitools.client.model.DatabasePostgreSQLRequest;
import org.openapitools.client.model.DatabaseSSL;
import org.openapitools.client.model.DatabaseType;
import org.openapitools.client.model.GetAccountDefaultResponse;
import org.openapitools.client.model.GetDatabasesEngines200Response;
import org.openapitools.client.model.GetDatabasesInstances200Response;
import org.openapitools.client.model.GetDatabasesMongoDBInstanceBackups200Response;
import org.openapitools.client.model.GetDatabasesMongoDBInstances200Response;
import org.openapitools.client.model.GetDatabasesMySQLInstances200Response;
import org.openapitools.client.model.GetDatabasesPostgreSQLInstances200Response;
import org.openapitools.client.model.GetDatabasesTypes200Response;
import org.openapitools.client.model.PutDatabasesMongoDBInstanceRequest;
import org.openapitools.client.model.PutDatabasesMySQLInstanceRequest;
import org.openapitools.client.model.PutDatabasesPostgreSQLInstanceRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DatabasesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DatabasesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DatabasesApi(ApiClient apiClient) {
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
     * Build call for deleteDatabaseMongoDBInstanceBackup
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseMongoDBInstanceBackupCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/backups/{backupId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDatabaseMongoDBInstanceBackupValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling deleteDatabaseMongoDBInstanceBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling deleteDatabaseMongoDBInstanceBackup(Async)");
        }

        return deleteDatabaseMongoDBInstanceBackupCall(instanceId, backupId, _callback);

    }

    /**
     * Managed MongoDB Database Backup Delete
     * Delete a single backup for an accessible Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDatabaseMongoDBInstanceBackup(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDatabaseMongoDBInstanceBackupWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Backup Delete
     * Delete a single backup for an accessible Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDatabaseMongoDBInstanceBackupWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabaseMongoDBInstanceBackupValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Backup Delete (asynchronously)
     * Delete a single backup for an accessible Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseMongoDBInstanceBackupAsync(Integer instanceId, Integer backupId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabaseMongoDBInstanceBackupValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabaseMySQLInstanceBackup
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseMySQLInstanceBackupCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/backups/{backupId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDatabaseMySQLInstanceBackupValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling deleteDatabaseMySQLInstanceBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling deleteDatabaseMySQLInstanceBackup(Async)");
        }

        return deleteDatabaseMySQLInstanceBackupCall(instanceId, backupId, _callback);

    }

    /**
     * Managed MySQL Database Backup Delete
     * Delete a single backup for an accessible Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDatabaseMySQLInstanceBackup(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDatabaseMySQLInstanceBackupWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Backup Delete
     * Delete a single backup for an accessible Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDatabaseMySQLInstanceBackupWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabaseMySQLInstanceBackupValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Backup Delete (asynchronously)
     * Delete a single backup for an accessible Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseMySQLInstanceBackupAsync(Integer instanceId, Integer backupId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabaseMySQLInstanceBackupValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabasePostgreSQLInstanceBackup
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasePostgreSQLInstanceBackupCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/backups/{backupId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDatabasePostgreSQLInstanceBackupValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling deleteDatabasePostgreSQLInstanceBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling deleteDatabasePostgreSQLInstanceBackup(Async)");
        }

        return deleteDatabasePostgreSQLInstanceBackupCall(instanceId, backupId, _callback);

    }

    /**
     * Managed PostgreSQL Database Backup Delete
     * Delete a single backup for an accessible Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDatabasePostgreSQLInstanceBackup(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDatabasePostgreSQLInstanceBackupWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Backup Delete
     * Delete a single backup for an accessible Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDatabasePostgreSQLInstanceBackupWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabasePostgreSQLInstanceBackupValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Backup Delete (asynchronously)
     * Delete a single backup for an accessible Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to delete Database backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasePostgreSQLInstanceBackupAsync(Integer instanceId, Integer backupId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabasePostgreSQLInstanceBackupValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabasesMongoDBInstance
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MongoDB Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasesMongoDBInstanceCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call deleteDatabasesMongoDBInstanceValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling deleteDatabasesMongoDBInstance(Async)");
        }

        return deleteDatabasesMongoDBInstanceCall(instanceId, _callback);

    }

    /**
     * Managed MongoDB Database Delete
     * Remove a Managed MongoDB Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MongoDB Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDatabasesMongoDBInstance(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDatabasesMongoDBInstanceWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Delete
     * Remove a Managed MongoDB Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MongoDB Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDatabasesMongoDBInstanceWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabasesMongoDBInstanceValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Delete (asynchronously)
     * Remove a Managed MongoDB Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MongoDB Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasesMongoDBInstanceAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabasesMongoDBInstanceValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabasesMySQLInstance
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MySQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasesMySQLInstanceCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call deleteDatabasesMySQLInstanceValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling deleteDatabasesMySQLInstance(Async)");
        }

        return deleteDatabasesMySQLInstanceCall(instanceId, _callback);

    }

    /**
     * Managed MySQL Database Delete
     * Remove a Managed MySQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MySQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDatabasesMySQLInstance(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDatabasesMySQLInstanceWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Delete
     * Remove a Managed MySQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MySQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDatabasesMySQLInstanceWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabasesMySQLInstanceValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Delete (asynchronously)
     * Remove a Managed MySQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed MySQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasesMySQLInstanceAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabasesMySQLInstanceValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabasesPostgreSQLInstance
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed PostgreSQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasesPostgreSQLInstanceCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call deleteDatabasesPostgreSQLInstanceValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling deleteDatabasesPostgreSQLInstance(Async)");
        }

        return deleteDatabasesPostgreSQLInstanceCall(instanceId, _callback);

    }

    /**
     * Managed PostgreSQL Database Delete
     * Remove a Managed PostgreSQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed PostgreSQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object deleteDatabasesPostgreSQLInstance(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = deleteDatabasesPostgreSQLInstanceWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Delete
     * Remove a Managed PostgreSQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed PostgreSQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteDatabasesPostgreSQLInstanceWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabasesPostgreSQLInstanceValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Delete (asynchronously)
     * Remove a Managed PostgreSQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed PostgreSQL Database successfully deleted. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabasesPostgreSQLInstanceAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabasesPostgreSQLInstanceValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesEngine
     * @param engineId The ID of the Managed Database engine. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed Database engine type and version. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesEngineCall(String engineId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/engines/{engineId}"
            .replace("{" + "engineId" + "}", localVarApiClient.escapeString(engineId.toString()));

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
    private okhttp3.Call getDatabasesEngineValidateBeforeCall(String engineId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'engineId' is set
        if (engineId == null) {
            throw new ApiException("Missing the required parameter 'engineId' when calling getDatabasesEngine(Async)");
        }

        return getDatabasesEngineCall(engineId, page, pageSize, _callback);

    }

    /**
     * Managed Database Engine View
     * Display information for a single Managed Database engine type and version. 
     * @param engineId The ID of the Managed Database engine. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return DatabaseEngine
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed Database engine type and version. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseEngine getDatabasesEngine(String engineId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<DatabaseEngine> localVarResp = getDatabasesEngineWithHttpInfo(engineId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed Database Engine View
     * Display information for a single Managed Database engine type and version. 
     * @param engineId The ID of the Managed Database engine. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;DatabaseEngine&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed Database engine type and version. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseEngine> getDatabasesEngineWithHttpInfo(String engineId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesEngineValidateBeforeCall(engineId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<DatabaseEngine>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed Database Engine View (asynchronously)
     * Display information for a single Managed Database engine type and version. 
     * @param engineId The ID of the Managed Database engine. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed Database engine type and version. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesEngineAsync(String engineId, Integer page, Integer pageSize, final ApiCallback<DatabaseEngine> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesEngineValidateBeforeCall(engineId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<DatabaseEngine>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesEngines
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all available Managed Database engines and versions. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesEnginesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/engines";

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
    private okhttp3.Call getDatabasesEnginesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDatabasesEnginesCall(page, pageSize, _callback);

    }

    /**
     * Managed Database Engines List
     * Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesEngines200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all available Managed Database engines and versions. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesEngines200Response getDatabasesEngines(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesEngines200Response> localVarResp = getDatabasesEnginesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed Database Engines List
     * Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesEngines200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all available Managed Database engines and versions. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesEngines200Response> getDatabasesEnginesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesEnginesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesEngines200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed Database Engines List (asynchronously)
     * Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all available Managed Database engines and versions. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesEnginesAsync(Integer page, Integer pageSize, final ApiCallback<GetDatabasesEngines200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesEnginesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesEngines200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesInstances
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesInstancesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/instances";

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
    private okhttp3.Call getDatabasesInstancesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDatabasesInstancesCall(page, pageSize, _callback);

    }

    /**
     * Managed Databases List All
     * Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its &#x60;instance_uri&#x60;. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesInstances200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesInstances200Response getDatabasesInstances(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesInstances200Response> localVarResp = getDatabasesInstancesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed Databases List All
     * Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its &#x60;instance_uri&#x60;. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesInstances200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesInstances200Response> getDatabasesInstancesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesInstancesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesInstances200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed Databases List All (asynchronously)
     * Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its &#x60;instance_uri&#x60;. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesInstancesAsync(Integer page, Integer pageSize, final ApiCallback<GetDatabasesInstances200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesInstancesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesInstances200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMongoDBInstance
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMongoDBInstanceValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstance(Async)");
        }

        return getDatabasesMongoDBInstanceCall(instanceId, _callback);

    }

    /**
     * Managed MongoDB Database View
     * Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return DatabaseMongoDB
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseMongoDB getDatabasesMongoDBInstance(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseMongoDB> localVarResp = getDatabasesMongoDBInstanceWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database View
     * Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;DatabaseMongoDB&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseMongoDB> getDatabasesMongoDBInstanceWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseMongoDB>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database View (asynchronously)
     * Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceAsync(Integer instanceId, final ApiCallback<DatabaseMongoDB> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseMongoDB>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMongoDBInstanceBackup
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceBackupCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/backups/{backupId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
    private okhttp3.Call getDatabasesMongoDBInstanceBackupValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling getDatabasesMongoDBInstanceBackup(Async)");
        }

        return getDatabasesMongoDBInstanceBackupCall(instanceId, backupId, _callback);

    }

    /**
     * Managed MongoDB Database Backup View
     * Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @return DatabaseBackup
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseBackup getDatabasesMongoDBInstanceBackup(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<DatabaseBackup> localVarResp = getDatabasesMongoDBInstanceBackupWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Backup View
     * Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @return ApiResponse&lt;DatabaseBackup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseBackup> getDatabasesMongoDBInstanceBackupWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceBackupValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<DatabaseBackup>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Backup View (asynchronously)
     * Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceBackupAsync(Integer instanceId, Integer backupId, final ApiCallback<DatabaseBackup> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceBackupValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseBackup>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMongoDBInstanceBackups
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceBackupsCall(Integer instanceId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/backups"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMongoDBInstanceBackupsValidateBeforeCall(Integer instanceId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceBackups(Async)");
        }

        return getDatabasesMongoDBInstanceBackupsCall(instanceId, page, pageSize, _callback);

    }

    /**
     * Managed MongoDB Database Backups List
     * Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesMongoDBInstanceBackups200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesMongoDBInstanceBackups200Response getDatabasesMongoDBInstanceBackups(Integer instanceId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesMongoDBInstanceBackups200Response> localVarResp = getDatabasesMongoDBInstanceBackupsWithHttpInfo(instanceId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Backups List
     * Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesMongoDBInstanceBackups200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesMongoDBInstanceBackups200Response> getDatabasesMongoDBInstanceBackupsWithHttpInfo(Integer instanceId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceBackupsValidateBeforeCall(instanceId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstanceBackups200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Backups List (asynchronously)
     * Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceBackupsAsync(Integer instanceId, Integer page, Integer pageSize, final ApiCallback<GetDatabasesMongoDBInstanceBackups200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceBackupsValidateBeforeCall(instanceId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstanceBackups200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMongoDBInstanceCredentials
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceCredentialsCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/credentials"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMongoDBInstanceCredentialsValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceCredentials(Async)");
        }

        return getDatabasesMongoDBInstanceCredentialsCall(instanceId, _callback);

    }

    /**
     * Managed MongoDB Database Credentials View
     * Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return DatabaseCredentials
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseCredentials getDatabasesMongoDBInstanceCredentials(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseCredentials> localVarResp = getDatabasesMongoDBInstanceCredentialsWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Credentials View
     * Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;DatabaseCredentials&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseCredentials> getDatabasesMongoDBInstanceCredentialsWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceCredentialsValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseCredentials>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Credentials View (asynchronously)
     * Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceCredentialsAsync(Integer instanceId, final ApiCallback<DatabaseCredentials> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceCredentialsValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseCredentials>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMongoDBInstanceSSL
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceSSLCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/ssl"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMongoDBInstanceSSLValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMongoDBInstanceSSL(Async)");
        }

        return getDatabasesMongoDBInstanceSSLCall(instanceId, _callback);

    }

    /**
     * Managed MongoDB Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return DatabaseSSL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseSSL getDatabasesMongoDBInstanceSSL(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseSSL> localVarResp = getDatabasesMongoDBInstanceSSLWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;DatabaseSSL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseSSL> getDatabasesMongoDBInstanceSSLWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceSSLValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseSSL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database SSL Certificate View (asynchronously)
     * Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MongoDB Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstanceSSLAsync(Integer instanceId, final ApiCallback<DatabaseSSL> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMongoDBInstanceSSLValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseSSL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMongoDBInstances
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MongoDB Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstancesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances";

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
    private okhttp3.Call getDatabasesMongoDBInstancesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDatabasesMongoDBInstancesCall(page, pageSize, _callback);

    }

    /**
     * Managed MongoDB Databases List
     * Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesMongoDBInstances200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MongoDB Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesMongoDBInstances200Response getDatabasesMongoDBInstances(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesMongoDBInstances200Response> localVarResp = getDatabasesMongoDBInstancesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Databases List
     * Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesMongoDBInstances200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MongoDB Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesMongoDBInstances200Response> getDatabasesMongoDBInstancesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMongoDBInstancesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstances200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Databases List (asynchronously)
     * Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MongoDB Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMongoDBInstancesAsync(Integer page, Integer pageSize, final ApiCallback<GetDatabasesMongoDBInstances200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMongoDBInstancesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstances200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMySQLInstance
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMySQLInstanceValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstance(Async)");
        }

        return getDatabasesMySQLInstanceCall(instanceId, _callback);

    }

    /**
     * Managed MySQL Database View
     * Display information for a single, accessible Managed MySQL Database. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return DatabaseMySQL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseMySQL getDatabasesMySQLInstance(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseMySQL> localVarResp = getDatabasesMySQLInstanceWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database View
     * Display information for a single, accessible Managed MySQL Database. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return ApiResponse&lt;DatabaseMySQL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseMySQL> getDatabasesMySQLInstanceWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMySQLInstanceValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseMySQL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database View (asynchronously)
     * Display information for a single, accessible Managed MySQL Database. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceAsync(Integer instanceId, final ApiCallback<DatabaseMySQL> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMySQLInstanceValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseMySQL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMySQLInstanceBackup
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceBackupCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/backups/{backupId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
    private okhttp3.Call getDatabasesMySQLInstanceBackupValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling getDatabasesMySQLInstanceBackup(Async)");
        }

        return getDatabasesMySQLInstanceBackupCall(instanceId, backupId, _callback);

    }

    /**
     * Managed MySQL Database Backup View
     * Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @return DatabaseBackup
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseBackup getDatabasesMySQLInstanceBackup(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<DatabaseBackup> localVarResp = getDatabasesMySQLInstanceBackupWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Backup View
     * Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @return ApiResponse&lt;DatabaseBackup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseBackup> getDatabasesMySQLInstanceBackupWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMySQLInstanceBackupValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<DatabaseBackup>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Backup View (asynchronously)
     * Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceBackupAsync(Integer instanceId, Integer backupId, final ApiCallback<DatabaseBackup> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMySQLInstanceBackupValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseBackup>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMySQLInstanceBackups
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceBackupsCall(Integer instanceId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/backups"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMySQLInstanceBackupsValidateBeforeCall(Integer instanceId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceBackups(Async)");
        }

        return getDatabasesMySQLInstanceBackupsCall(instanceId, page, pageSize, _callback);

    }

    /**
     * Managed MySQL Database Backups List
     * Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesMongoDBInstanceBackups200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesMongoDBInstanceBackups200Response getDatabasesMySQLInstanceBackups(Integer instanceId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesMongoDBInstanceBackups200Response> localVarResp = getDatabasesMySQLInstanceBackupsWithHttpInfo(instanceId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Backups List
     * Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesMongoDBInstanceBackups200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesMongoDBInstanceBackups200Response> getDatabasesMySQLInstanceBackupsWithHttpInfo(Integer instanceId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMySQLInstanceBackupsValidateBeforeCall(instanceId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstanceBackups200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Backups List (asynchronously)
     * Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceBackupsAsync(Integer instanceId, Integer page, Integer pageSize, final ApiCallback<GetDatabasesMongoDBInstanceBackups200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMySQLInstanceBackupsValidateBeforeCall(instanceId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstanceBackups200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMySQLInstanceCredentials
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceCredentialsCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/credentials"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMySQLInstanceCredentialsValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceCredentials(Async)");
        }

        return getDatabasesMySQLInstanceCredentialsCall(instanceId, _callback);

    }

    /**
     * Managed MySQL Database Credentials View
     * Display the root username and password for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return DatabaseCredentials
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseCredentials getDatabasesMySQLInstanceCredentials(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseCredentials> localVarResp = getDatabasesMySQLInstanceCredentialsWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Credentials View
     * Display the root username and password for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return ApiResponse&lt;DatabaseCredentials&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseCredentials> getDatabasesMySQLInstanceCredentialsWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMySQLInstanceCredentialsValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseCredentials>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Credentials View (asynchronously)
     * Display the root username and password for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceCredentialsAsync(Integer instanceId, final ApiCallback<DatabaseCredentials> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMySQLInstanceCredentialsValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseCredentials>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMySQLInstanceSSL
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceSSLCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/ssl"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesMySQLInstanceSSLValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesMySQLInstanceSSL(Async)");
        }

        return getDatabasesMySQLInstanceSSLCall(instanceId, _callback);

    }

    /**
     * Managed MySQL Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return DatabaseSSL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseSSL getDatabasesMySQLInstanceSSL(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseSSL> localVarResp = getDatabasesMySQLInstanceSSLWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return ApiResponse&lt;DatabaseSSL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseSSL> getDatabasesMySQLInstanceSSLWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMySQLInstanceSSLValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseSSL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database SSL Certificate View (asynchronously)
     * Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed MySQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstanceSSLAsync(Integer instanceId, final ApiCallback<DatabaseSSL> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMySQLInstanceSSLValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseSSL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesMySQLInstances
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MySQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstancesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances";

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
    private okhttp3.Call getDatabasesMySQLInstancesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDatabasesMySQLInstancesCall(page, pageSize, _callback);

    }

    /**
     * Managed MySQL Databases List
     * Display all accessible Managed MySQL Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesMySQLInstances200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MySQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesMySQLInstances200Response getDatabasesMySQLInstances(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesMySQLInstances200Response> localVarResp = getDatabasesMySQLInstancesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Databases List
     * Display all accessible Managed MySQL Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesMySQLInstances200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MySQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesMySQLInstances200Response> getDatabasesMySQLInstancesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesMySQLInstancesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesMySQLInstances200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Databases List (asynchronously)
     * Display all accessible Managed MySQL Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed MySQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesMySQLInstancesAsync(Integer page, Integer pageSize, final ApiCallback<GetDatabasesMySQLInstances200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesMySQLInstancesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesMySQLInstances200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesPostgreSQLInstance
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesPostgreSQLInstanceValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstance(Async)");
        }

        return getDatabasesPostgreSQLInstanceCall(instanceId, _callback);

    }

    /**
     * Managed PostgreSQL Database View
     * Display information for a single, accessible Managed PostgreSQL Database. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return DatabasePostgreSQL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabasePostgreSQL getDatabasesPostgreSQLInstance(Integer instanceId) throws ApiException {
        ApiResponse<DatabasePostgreSQL> localVarResp = getDatabasesPostgreSQLInstanceWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database View
     * Display information for a single, accessible Managed PostgreSQL Database. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;DatabasePostgreSQL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabasePostgreSQL> getDatabasesPostgreSQLInstanceWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabasePostgreSQL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database View (asynchronously)
     * Display information for a single, accessible Managed PostgreSQL Database. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns information for a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceAsync(Integer instanceId, final ApiCallback<DatabasePostgreSQL> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabasePostgreSQL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesPostgreSQLInstanceBackup
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceBackupCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/backups/{backupId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
    private okhttp3.Call getDatabasesPostgreSQLInstanceBackupValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceBackup(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling getDatabasesPostgreSQLInstanceBackup(Async)");
        }

        return getDatabasesPostgreSQLInstanceBackupCall(instanceId, backupId, _callback);

    }

    /**
     * Managed PostgreSQL Database Backup View
     * Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @return DatabaseBackup
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseBackup getDatabasesPostgreSQLInstanceBackup(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<DatabaseBackup> localVarResp = getDatabasesPostgreSQLInstanceBackupWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Backup View
     * Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @return ApiResponse&lt;DatabaseBackup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseBackup> getDatabasesPostgreSQLInstanceBackupWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceBackupValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<DatabaseBackup>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Backup View (asynchronously)
     * Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single backup for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceBackupAsync(Integer instanceId, Integer backupId, final ApiCallback<DatabaseBackup> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceBackupValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseBackup>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesPostgreSQLInstanceBackups
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceBackupsCall(Integer instanceId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/backups"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesPostgreSQLInstanceBackupsValidateBeforeCall(Integer instanceId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceBackups(Async)");
        }

        return getDatabasesPostgreSQLInstanceBackupsCall(instanceId, page, pageSize, _callback);

    }

    /**
     * Managed PostgreSQL Database Backups List
     * Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesMongoDBInstanceBackups200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesMongoDBInstanceBackups200Response getDatabasesPostgreSQLInstanceBackups(Integer instanceId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesMongoDBInstanceBackups200Response> localVarResp = getDatabasesPostgreSQLInstanceBackupsWithHttpInfo(instanceId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Backups List
     * Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesMongoDBInstanceBackups200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesMongoDBInstanceBackups200Response> getDatabasesPostgreSQLInstanceBackupsWithHttpInfo(Integer instanceId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceBackupsValidateBeforeCall(instanceId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstanceBackups200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Backups List (asynchronously)
     * Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of backups for the Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceBackupsAsync(Integer instanceId, Integer page, Integer pageSize, final ApiCallback<GetDatabasesMongoDBInstanceBackups200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceBackupsValidateBeforeCall(instanceId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesMongoDBInstanceBackups200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesPostgreSQLInstanceCredentials
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceCredentialsCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/credentials"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesPostgreSQLInstanceCredentialsValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceCredentials(Async)");
        }

        return getDatabasesPostgreSQLInstanceCredentialsCall(instanceId, _callback);

    }

    /**
     * Managed PostgreSQL Database Credentials View
     * Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return DatabaseCredentials
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseCredentials getDatabasesPostgreSQLInstanceCredentials(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseCredentials> localVarResp = getDatabasesPostgreSQLInstanceCredentialsWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Credentials View
     * Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;DatabaseCredentials&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseCredentials> getDatabasesPostgreSQLInstanceCredentialsWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceCredentialsValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseCredentials>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Credentials View (asynchronously)
     * Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database root username and password. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceCredentialsAsync(Integer instanceId, final ApiCallback<DatabaseCredentials> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceCredentialsValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseCredentials>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesPostgreSQLInstanceSSL
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceSSLCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/ssl"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call getDatabasesPostgreSQLInstanceSSLValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling getDatabasesPostgreSQLInstanceSSL(Async)");
        }

        return getDatabasesPostgreSQLInstanceSSLCall(instanceId, _callback);

    }

    /**
     * Managed PostgreSQL Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return DatabaseSSL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseSSL getDatabasesPostgreSQLInstanceSSL(Integer instanceId) throws ApiException {
        ApiResponse<DatabaseSSL> localVarResp = getDatabasesPostgreSQLInstanceSSLWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database SSL Certificate View
     * Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;DatabaseSSL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseSSL> getDatabasesPostgreSQLInstanceSSLWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceSSLValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<DatabaseSSL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database SSL Certificate View (asynchronously)
     * Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the SSL CA certificate of a single Managed PostgreSQL Database. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstanceSSLAsync(Integer instanceId, final ApiCallback<DatabaseSSL> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstanceSSLValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<DatabaseSSL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesPostgreSQLInstances
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed PostgreSQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstancesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances";

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
    private okhttp3.Call getDatabasesPostgreSQLInstancesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDatabasesPostgreSQLInstancesCall(page, pageSize, _callback);

    }

    /**
     * Managed PostgreSQL Databases List
     * Display all accessible Managed PostgreSQL Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesPostgreSQLInstances200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed PostgreSQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesPostgreSQLInstances200Response getDatabasesPostgreSQLInstances(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesPostgreSQLInstances200Response> localVarResp = getDatabasesPostgreSQLInstancesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Databases List
     * Display all accessible Managed PostgreSQL Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesPostgreSQLInstances200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed PostgreSQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesPostgreSQLInstances200Response> getDatabasesPostgreSQLInstancesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstancesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesPostgreSQLInstances200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Databases List (asynchronously)
     * Display all accessible Managed PostgreSQL Databases. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all accessible Managed PostgreSQL Databases on your Account. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesPostgreSQLInstancesAsync(Integer page, Integer pageSize, final ApiCallback<GetDatabasesPostgreSQLInstances200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesPostgreSQLInstancesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesPostgreSQLInstances200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesType
     * @param typeId The ID of the Managed Database type. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Managed Database type. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesTypeCall(String typeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/types/{typeId}"
            .replace("{" + "typeId" + "}", localVarApiClient.escapeString(typeId.toString()));

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
    private okhttp3.Call getDatabasesTypeValidateBeforeCall(String typeId, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'typeId' is set
        if (typeId == null) {
            throw new ApiException("Missing the required parameter 'typeId' when calling getDatabasesType(Async)");
        }

        return getDatabasesTypeCall(typeId, page, pageSize, _callback);

    }

    /**
     * Managed Database Type View
     * Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 
     * @param typeId The ID of the Managed Database type. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return DatabaseType
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Managed Database type. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseType getDatabasesType(String typeId, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<DatabaseType> localVarResp = getDatabasesTypeWithHttpInfo(typeId, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed Database Type View
     * Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 
     * @param typeId The ID of the Managed Database type. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;DatabaseType&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Managed Database type. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseType> getDatabasesTypeWithHttpInfo(String typeId, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesTypeValidateBeforeCall(typeId, page, pageSize, null);
        Type localVarReturnType = new TypeToken<DatabaseType>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed Database Type View (asynchronously)
     * Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 
     * @param typeId The ID of the Managed Database type. (required)
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a single Managed Database type. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesTypeAsync(String typeId, Integer page, Integer pageSize, final ApiCallback<DatabaseType> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesTypeValidateBeforeCall(typeId, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<DatabaseType>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabasesTypes
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all Managed Database types. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesTypesCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/types";

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
    private okhttp3.Call getDatabasesTypesValidateBeforeCall(Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        return getDatabasesTypesCall(page, pageSize, _callback);

    }

    /**
     * Managed Database Types List
     * Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return GetDatabasesTypes200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all Managed Database types. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public GetDatabasesTypes200Response getDatabasesTypes(Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetDatabasesTypes200Response> localVarResp = getDatabasesTypesWithHttpInfo(page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Managed Database Types List
     * Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @return ApiResponse&lt;GetDatabasesTypes200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all Managed Database types. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDatabasesTypes200Response> getDatabasesTypesWithHttpInfo(Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getDatabasesTypesValidateBeforeCall(page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetDatabasesTypes200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed Database Types List (asynchronously)
     * Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 
     * @param page The page of a collection to return. (optional, default to 1)
     * @param pageSize The number of items to return per page. (optional, default to 100)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns a paginated list of all Managed Database types. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabasesTypesAsync(Integer page, Integer pageSize, final ApiCallback<GetDatabasesTypes200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabasesTypesValidateBeforeCall(page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetDatabasesTypes200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMongoDBInstanceBackup
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstanceBackupCall(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = databaseBackupSnapshot;

        // create path and map variables
        String localVarPath = "/databases/mongodb/instances/{instanceId}/backups"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesMongoDBInstanceBackupValidateBeforeCall(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstanceBackup(Async)");
        }

        return postDatabasesMongoDBInstanceBackupCall(instanceId, databaseBackupSnapshot, _callback);

    }

    /**
     * Managed MongoDB Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMongoDBInstanceBackup(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMongoDBInstanceBackupWithHttpInfo(instanceId, databaseBackupSnapshot);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMongoDBInstanceBackupWithHttpInfo(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMongoDBInstanceBackupValidateBeforeCall(instanceId, databaseBackupSnapshot, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Backup Snapshot Create (asynchronously)
     * Creates a snapshot backup of a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstanceBackupAsync(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMongoDBInstanceBackupValidateBeforeCall(instanceId, databaseBackupSnapshot, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMongoDBInstanceBackupRestore
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstanceBackupRestoreCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/backups/{backupId}/restore"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postDatabasesMongoDBInstanceBackupRestoreValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstanceBackupRestore(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling postDatabasesMongoDBInstanceBackupRestore(Async)");
        }

        return postDatabasesMongoDBInstanceBackupRestoreCall(instanceId, backupId, _callback);

    }

    /**
     * Managed MongoDB Database Backup Restore
     * Restore a backup to a Managed MongoDB Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMongoDBInstanceBackupRestore(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMongoDBInstanceBackupRestoreWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Backup Restore
     * Restore a backup to a Managed MongoDB Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMongoDBInstanceBackupRestoreWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMongoDBInstanceBackupRestoreValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Backup Restore (asynchronously)
     * Restore a backup to a Managed MongoDB Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param backupId The ID of the Managed MongoDB Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstanceBackupRestoreAsync(Integer instanceId, Integer backupId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMongoDBInstanceBackupRestoreValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMongoDBInstanceCredentialsReset
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstanceCredentialsResetCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/credentials/reset"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesMongoDBInstanceCredentialsResetValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstanceCredentialsReset(Async)");
        }

        return postDatabasesMongoDBInstanceCredentialsResetCall(instanceId, _callback);

    }

    /**
     * Managed MongoDB Database Credentials Reset
     * Reset the root password for a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMongoDBInstanceCredentialsReset(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMongoDBInstanceCredentialsResetWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Credentials Reset
     * Reset the root password for a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMongoDBInstanceCredentialsResetWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMongoDBInstanceCredentialsResetValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Credentials Reset (asynchronously)
     * Reset the root password for a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstanceCredentialsResetAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMongoDBInstanceCredentialsResetValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMongoDBInstancePatch
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstancePatchCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mongodb/instances/{instanceId}/patch"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesMongoDBInstancePatchValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMongoDBInstancePatch(Async)");
        }

        return postDatabasesMongoDBInstancePatchCall(instanceId, _callback);

    }

    /**
     * Managed MongoDB Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMongoDBInstancePatch(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMongoDBInstancePatchWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMongoDBInstancePatchWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMongoDBInstancePatchValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Patch (asynchronously)
     * Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMongoDBInstancePatchAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMongoDBInstancePatchValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMySQLInstanceBackup
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstanceBackupCall(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = databaseBackupSnapshot;

        // create path and map variables
        String localVarPath = "/databases/mysql/instances/{instanceId}/backups"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesMySQLInstanceBackupValidateBeforeCall(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstanceBackup(Async)");
        }

        return postDatabasesMySQLInstanceBackupCall(instanceId, databaseBackupSnapshot, _callback);

    }

    /**
     * Managed MySQL Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMySQLInstanceBackup(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMySQLInstanceBackupWithHttpInfo(instanceId, databaseBackupSnapshot);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMySQLInstanceBackupWithHttpInfo(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMySQLInstanceBackupValidateBeforeCall(instanceId, databaseBackupSnapshot, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Backup Snapshot Create (asynchronously)
     * Creates a snapshot backup of a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstanceBackupAsync(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMySQLInstanceBackupValidateBeforeCall(instanceId, databaseBackupSnapshot, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMySQLInstanceBackupRestore
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstanceBackupRestoreCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/backups/{backupId}/restore"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postDatabasesMySQLInstanceBackupRestoreValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstanceBackupRestore(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling postDatabasesMySQLInstanceBackupRestore(Async)");
        }

        return postDatabasesMySQLInstanceBackupRestoreCall(instanceId, backupId, _callback);

    }

    /**
     * Managed MySQL Database Backup Restore
     * Restore a backup to a Managed MySQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMySQLInstanceBackupRestore(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMySQLInstanceBackupRestoreWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Backup Restore
     * Restore a backup to a Managed MySQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMySQLInstanceBackupRestoreWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMySQLInstanceBackupRestoreValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Backup Restore (asynchronously)
     * Restore a backup to a Managed MySQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param backupId The ID of the Managed MySQL Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstanceBackupRestoreAsync(Integer instanceId, Integer backupId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMySQLInstanceBackupRestoreValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMySQLInstanceCredentialsReset
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstanceCredentialsResetCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/credentials/reset"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesMySQLInstanceCredentialsResetValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstanceCredentialsReset(Async)");
        }

        return postDatabasesMySQLInstanceCredentialsResetCall(instanceId, _callback);

    }

    /**
     * Managed MySQL Database Credentials Reset
     * Reset the root password for a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMySQLInstanceCredentialsReset(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMySQLInstanceCredentialsResetWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Credentials Reset
     * Reset the root password for a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMySQLInstanceCredentialsResetWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMySQLInstanceCredentialsResetValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Credentials Reset (asynchronously)
     * Reset the root password for a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstanceCredentialsResetAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMySQLInstanceCredentialsResetValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMySQLInstancePatch
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstancePatchCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/mysql/instances/{instanceId}/patch"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesMySQLInstancePatchValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesMySQLInstancePatch(Async)");
        }

        return postDatabasesMySQLInstancePatchCall(instanceId, _callback);

    }

    /**
     * Managed MySQL Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesMySQLInstancePatch(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesMySQLInstancePatchWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesMySQLInstancePatchWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMySQLInstancePatchValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Patch (asynchronously)
     * Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstancePatchAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMySQLInstancePatchValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesMySQLInstances
     * @param databaseMySQLRequest Information about the Managed MySQL Database you are creating. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed MySQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstancesCall(DatabaseMySQLRequest databaseMySQLRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = databaseMySQLRequest;

        // create path and map variables
        String localVarPath = "/databases/mysql/instances";

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
    private okhttp3.Call postDatabasesMySQLInstancesValidateBeforeCall(DatabaseMySQLRequest databaseMySQLRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseMySQLRequest' is set
        if (databaseMySQLRequest == null) {
            throw new ApiException("Missing the required parameter 'databaseMySQLRequest' when calling postDatabasesMySQLInstances(Async)");
        }

        return postDatabasesMySQLInstancesCall(databaseMySQLRequest, _callback);

    }

    /**
     * Managed MySQL Database Create
     * Provision a Managed MySQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 
     * @param databaseMySQLRequest Information about the Managed MySQL Database you are creating. (required)
     * @return DatabaseMySQL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed MySQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseMySQL postDatabasesMySQLInstances(DatabaseMySQLRequest databaseMySQLRequest) throws ApiException {
        ApiResponse<DatabaseMySQL> localVarResp = postDatabasesMySQLInstancesWithHttpInfo(databaseMySQLRequest);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Create
     * Provision a Managed MySQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 
     * @param databaseMySQLRequest Information about the Managed MySQL Database you are creating. (required)
     * @return ApiResponse&lt;DatabaseMySQL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed MySQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseMySQL> postDatabasesMySQLInstancesWithHttpInfo(DatabaseMySQLRequest databaseMySQLRequest) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesMySQLInstancesValidateBeforeCall(databaseMySQLRequest, null);
        Type localVarReturnType = new TypeToken<DatabaseMySQL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Create (asynchronously)
     * Provision a Managed MySQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 
     * @param databaseMySQLRequest Information about the Managed MySQL Database you are creating. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed MySQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesMySQLInstancesAsync(DatabaseMySQLRequest databaseMySQLRequest, final ApiCallback<DatabaseMySQL> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesMySQLInstancesValidateBeforeCall(databaseMySQLRequest, _callback);
        Type localVarReturnType = new TypeToken<DatabaseMySQL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesPostgreSQLInstanceBackup
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstanceBackupCall(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = databaseBackupSnapshot;

        // create path and map variables
        String localVarPath = "/databases/postgresql/instances/{instanceId}/backups"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesPostgreSQLInstanceBackupValidateBeforeCall(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstanceBackup(Async)");
        }

        return postDatabasesPostgreSQLInstanceBackupCall(instanceId, databaseBackupSnapshot, _callback);

    }

    /**
     * Managed PostgreSQL Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesPostgreSQLInstanceBackup(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesPostgreSQLInstanceBackupWithHttpInfo(instanceId, databaseBackupSnapshot);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Backup Snapshot Create
     * Creates a snapshot backup of a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesPostgreSQLInstanceBackupWithHttpInfo(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstanceBackupValidateBeforeCall(instanceId, databaseBackupSnapshot, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Backup Snapshot Create (asynchronously)
     * Creates a snapshot backup of a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param databaseBackupSnapshot Information about the snapshot backup to create. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Database snapshot backup request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstanceBackupAsync(Integer instanceId, DatabaseBackupSnapshot databaseBackupSnapshot, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstanceBackupValidateBeforeCall(instanceId, databaseBackupSnapshot, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesPostgreSQLInstanceBackupRestore
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstanceBackupRestoreCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/backups/{backupId}/restore"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postDatabasesPostgreSQLInstanceBackupRestoreValidateBeforeCall(Integer instanceId, Integer backupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstanceBackupRestore(Async)");
        }

        // verify the required parameter 'backupId' is set
        if (backupId == null) {
            throw new ApiException("Missing the required parameter 'backupId' when calling postDatabasesPostgreSQLInstanceBackupRestore(Async)");
        }

        return postDatabasesPostgreSQLInstanceBackupRestoreCall(instanceId, backupId, _callback);

    }

    /**
     * Managed PostgreSQL Database Backup Restore
     * Restore a backup to a Managed PostgreSQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesPostgreSQLInstanceBackupRestore(Integer instanceId, Integer backupId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesPostgreSQLInstanceBackupRestoreWithHttpInfo(instanceId, backupId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Backup Restore
     * Restore a backup to a Managed PostgreSQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesPostgreSQLInstanceBackupRestoreWithHttpInfo(Integer instanceId, Integer backupId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstanceBackupRestoreValidateBeforeCall(instanceId, backupId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Backup Restore (asynchronously)
     * Restore a backup to a Managed PostgreSQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param backupId The ID of the Managed PostgreSQL Database backup. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Request to restore backup successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstanceBackupRestoreAsync(Integer instanceId, Integer backupId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstanceBackupRestoreValidateBeforeCall(instanceId, backupId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesPostgreSQLInstanceCredentialsReset
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstanceCredentialsResetCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/credentials/reset"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesPostgreSQLInstanceCredentialsResetValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstanceCredentialsReset(Async)");
        }

        return postDatabasesPostgreSQLInstanceCredentialsResetCall(instanceId, _callback);

    }

    /**
     * Managed PostgreSQL Database Credentials Reset
     * Reset the root password for a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesPostgreSQLInstanceCredentialsReset(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesPostgreSQLInstanceCredentialsResetWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Credentials Reset
     * Reset the root password for a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesPostgreSQLInstanceCredentialsResetWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstanceCredentialsResetValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Credentials Reset (asynchronously)
     * Reset the root password for a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance credentials successfully reset. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstanceCredentialsResetAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstanceCredentialsResetValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesPostgreSQLInstancePatch
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstancePatchCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

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
        String localVarPath = "/databases/postgresql/instances/{instanceId}/patch"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call postDatabasesPostgreSQLInstancePatchValidateBeforeCall(Integer instanceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling postDatabasesPostgreSQLInstancePatch(Async)");
        }

        return postDatabasesPostgreSQLInstancePatchCall(instanceId, _callback);

    }

    /**
     * Managed PostgreSQL Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public Object postDatabasesPostgreSQLInstancePatch(Integer instanceId) throws ApiException {
        ApiResponse<Object> localVarResp = postDatabasesPostgreSQLInstancePatchWithHttpInfo(instanceId);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Patch
     * Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postDatabasesPostgreSQLInstancePatchWithHttpInfo(Integer instanceId) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstancePatchValidateBeforeCall(instanceId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Patch (asynchronously)
     * Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database instance patch request successful. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstancePatchAsync(Integer instanceId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstancePatchValidateBeforeCall(instanceId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postDatabasesPostgreSQLInstances
     * @param databasePostgreSQLRequest Information about the Managed PostgreSQL Database you are creating. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed PostgreSQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstancesCall(DatabasePostgreSQLRequest databasePostgreSQLRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = databasePostgreSQLRequest;

        // create path and map variables
        String localVarPath = "/databases/postgresql/instances";

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
    private okhttp3.Call postDatabasesPostgreSQLInstancesValidateBeforeCall(DatabasePostgreSQLRequest databasePostgreSQLRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databasePostgreSQLRequest' is set
        if (databasePostgreSQLRequest == null) {
            throw new ApiException("Missing the required parameter 'databasePostgreSQLRequest' when calling postDatabasesPostgreSQLInstances(Async)");
        }

        return postDatabasesPostgreSQLInstancesCall(databasePostgreSQLRequest, _callback);

    }

    /**
     * Managed PostgreSQL Database Create
     * Provision a Managed PostgreSQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 
     * @param databasePostgreSQLRequest Information about the Managed PostgreSQL Database you are creating. (required)
     * @return DatabasePostgreSQL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed PostgreSQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabasePostgreSQL postDatabasesPostgreSQLInstances(DatabasePostgreSQLRequest databasePostgreSQLRequest) throws ApiException {
        ApiResponse<DatabasePostgreSQL> localVarResp = postDatabasesPostgreSQLInstancesWithHttpInfo(databasePostgreSQLRequest);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Create
     * Provision a Managed PostgreSQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 
     * @param databasePostgreSQLRequest Information about the Managed PostgreSQL Database you are creating. (required)
     * @return ApiResponse&lt;DatabasePostgreSQL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed PostgreSQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabasePostgreSQL> postDatabasesPostgreSQLInstancesWithHttpInfo(DatabasePostgreSQLRequest databasePostgreSQLRequest) throws ApiException {
        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstancesValidateBeforeCall(databasePostgreSQLRequest, null);
        Type localVarReturnType = new TypeToken<DatabasePostgreSQL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Create (asynchronously)
     * Provision a Managed PostgreSQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 
     * @param databasePostgreSQLRequest Information about the Managed PostgreSQL Database you are creating. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A new Managed PostgreSQL Database is provisioning. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postDatabasesPostgreSQLInstancesAsync(DatabasePostgreSQLRequest databasePostgreSQLRequest, final ApiCallback<DatabasePostgreSQL> _callback) throws ApiException {

        okhttp3.Call localVarCall = postDatabasesPostgreSQLInstancesValidateBeforeCall(databasePostgreSQLRequest, _callback);
        Type localVarReturnType = new TypeToken<DatabasePostgreSQL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putDatabasesMongoDBInstance
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param putDatabasesMongoDBInstanceRequest Updated information for the Managed MongoDB Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDatabasesMongoDBInstanceCall(Integer instanceId, PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putDatabasesMongoDBInstanceRequest;

        // create path and map variables
        String localVarPath = "/databases/mongodb/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call putDatabasesMongoDBInstanceValidateBeforeCall(Integer instanceId, PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling putDatabasesMongoDBInstance(Async)");
        }

        // verify the required parameter 'putDatabasesMongoDBInstanceRequest' is set
        if (putDatabasesMongoDBInstanceRequest == null) {
            throw new ApiException("Missing the required parameter 'putDatabasesMongoDBInstanceRequest' when calling putDatabasesMongoDBInstance(Async)");
        }

        return putDatabasesMongoDBInstanceCall(instanceId, putDatabasesMongoDBInstanceRequest, _callback);

    }

    /**
     * Managed MongoDB Database Update
     * Update a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param putDatabasesMongoDBInstanceRequest Updated information for the Managed MongoDB Database. (required)
     * @return DatabaseMongoDB
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseMongoDB putDatabasesMongoDBInstance(Integer instanceId, PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest) throws ApiException {
        ApiResponse<DatabaseMongoDB> localVarResp = putDatabasesMongoDBInstanceWithHttpInfo(instanceId, putDatabasesMongoDBInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Managed MongoDB Database Update
     * Update a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param putDatabasesMongoDBInstanceRequest Updated information for the Managed MongoDB Database. (required)
     * @return ApiResponse&lt;DatabaseMongoDB&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseMongoDB> putDatabasesMongoDBInstanceWithHttpInfo(Integer instanceId, PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = putDatabasesMongoDBInstanceValidateBeforeCall(instanceId, putDatabasesMongoDBInstanceRequest, null);
        Type localVarReturnType = new TypeToken<DatabaseMongoDB>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MongoDB Database Update (asynchronously)
     * Update a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     * @param instanceId The ID of the Managed MongoDB Database. (required)
     * @param putDatabasesMongoDBInstanceRequest Updated information for the Managed MongoDB Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDatabasesMongoDBInstanceAsync(Integer instanceId, PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest, final ApiCallback<DatabaseMongoDB> _callback) throws ApiException {

        okhttp3.Call localVarCall = putDatabasesMongoDBInstanceValidateBeforeCall(instanceId, putDatabasesMongoDBInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<DatabaseMongoDB>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putDatabasesMySQLInstance
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param putDatabasesMySQLInstanceRequest Updated information for the Managed MySQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDatabasesMySQLInstanceCall(Integer instanceId, PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putDatabasesMySQLInstanceRequest;

        // create path and map variables
        String localVarPath = "/databases/mysql/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call putDatabasesMySQLInstanceValidateBeforeCall(Integer instanceId, PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling putDatabasesMySQLInstance(Async)");
        }

        // verify the required parameter 'putDatabasesMySQLInstanceRequest' is set
        if (putDatabasesMySQLInstanceRequest == null) {
            throw new ApiException("Missing the required parameter 'putDatabasesMySQLInstanceRequest' when calling putDatabasesMySQLInstance(Async)");
        }

        return putDatabasesMySQLInstanceCall(instanceId, putDatabasesMySQLInstanceRequest, _callback);

    }

    /**
     * Managed MySQL Database Update
     * Update a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param putDatabasesMySQLInstanceRequest Updated information for the Managed MySQL Database. (required)
     * @return DatabaseMySQL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabaseMySQL putDatabasesMySQLInstance(Integer instanceId, PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest) throws ApiException {
        ApiResponse<DatabaseMySQL> localVarResp = putDatabasesMySQLInstanceWithHttpInfo(instanceId, putDatabasesMySQLInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Managed MySQL Database Update
     * Update a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param putDatabasesMySQLInstanceRequest Updated information for the Managed MySQL Database. (required)
     * @return ApiResponse&lt;DatabaseMySQL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabaseMySQL> putDatabasesMySQLInstanceWithHttpInfo(Integer instanceId, PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = putDatabasesMySQLInstanceValidateBeforeCall(instanceId, putDatabasesMySQLInstanceRequest, null);
        Type localVarReturnType = new TypeToken<DatabaseMySQL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed MySQL Database Update (asynchronously)
     * Update a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed MySQL Database. (required)
     * @param putDatabasesMySQLInstanceRequest Updated information for the Managed MySQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDatabasesMySQLInstanceAsync(Integer instanceId, PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest, final ApiCallback<DatabaseMySQL> _callback) throws ApiException {

        okhttp3.Call localVarCall = putDatabasesMySQLInstanceValidateBeforeCall(instanceId, putDatabasesMySQLInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<DatabaseMySQL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putDatabasesPostgreSQLInstance
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param putDatabasesPostgreSQLInstanceRequest Updated information for the Managed PostgreSQL Database. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDatabasesPostgreSQLInstanceCall(Integer instanceId, PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] { "https://api.linode.com/v4", "https://api.linode.com/v4beta" };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putDatabasesPostgreSQLInstanceRequest;

        // create path and map variables
        String localVarPath = "/databases/postgresql/instances/{instanceId}"
            .replace("{" + "instanceId" + "}", localVarApiClient.escapeString(instanceId.toString()));

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
    private okhttp3.Call putDatabasesPostgreSQLInstanceValidateBeforeCall(Integer instanceId, PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'instanceId' is set
        if (instanceId == null) {
            throw new ApiException("Missing the required parameter 'instanceId' when calling putDatabasesPostgreSQLInstance(Async)");
        }

        // verify the required parameter 'putDatabasesPostgreSQLInstanceRequest' is set
        if (putDatabasesPostgreSQLInstanceRequest == null) {
            throw new ApiException("Missing the required parameter 'putDatabasesPostgreSQLInstanceRequest' when calling putDatabasesPostgreSQLInstance(Async)");
        }

        return putDatabasesPostgreSQLInstanceCall(instanceId, putDatabasesPostgreSQLInstanceRequest, _callback);

    }

    /**
     * Managed PostgreSQL Database Update
     * Update a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param putDatabasesPostgreSQLInstanceRequest Updated information for the Managed PostgreSQL Database. (required)
     * @return DatabasePostgreSQL
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public DatabasePostgreSQL putDatabasesPostgreSQLInstance(Integer instanceId, PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest) throws ApiException {
        ApiResponse<DatabasePostgreSQL> localVarResp = putDatabasesPostgreSQLInstanceWithHttpInfo(instanceId, putDatabasesPostgreSQLInstanceRequest);
        return localVarResp.getData();
    }

    /**
     * Managed PostgreSQL Database Update
     * Update a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param putDatabasesPostgreSQLInstanceRequest Updated information for the Managed PostgreSQL Database. (required)
     * @return ApiResponse&lt;DatabasePostgreSQL&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DatabasePostgreSQL> putDatabasesPostgreSQLInstanceWithHttpInfo(Integer instanceId, PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest) throws ApiException {
        okhttp3.Call localVarCall = putDatabasesPostgreSQLInstanceValidateBeforeCall(instanceId, putDatabasesPostgreSQLInstanceRequest, null);
        Type localVarReturnType = new TypeToken<DatabasePostgreSQL>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Managed PostgreSQL Database Update (asynchronously)
     * Update a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     * @param instanceId The ID of the Managed PostgreSQL Database. (required)
     * @param putDatabasesPostgreSQLInstanceRequest Updated information for the Managed PostgreSQL Database. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Managed Database updated successfully. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putDatabasesPostgreSQLInstanceAsync(Integer instanceId, PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest, final ApiCallback<DatabasePostgreSQL> _callback) throws ApiException {

        okhttp3.Call localVarCall = putDatabasesPostgreSQLInstanceValidateBeforeCall(instanceId, putDatabasesPostgreSQLInstanceRequest, _callback);
        Type localVarReturnType = new TypeToken<DatabasePostgreSQL>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
