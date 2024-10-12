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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DatabasesApi
 */
@Disabled
public class DatabasesApiTest {

    private final DatabasesApi api = new DatabasesApi();

    /**
     * Managed MongoDB Database Backup Delete
     *
     * Delete a single backup for an accessible Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatabaseMongoDBInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        Object response = api.deleteDatabaseMongoDBInstanceBackup(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Backup Delete
     *
     * Delete a single backup for an accessible Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatabaseMySQLInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        Object response = api.deleteDatabaseMySQLInstanceBackup(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Backup Delete
     *
     * Delete a single backup for an accessible Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatabasePostgreSQLInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        Object response = api.deleteDatabasePostgreSQLInstanceBackup(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Delete
     *
     * Remove a Managed MongoDB Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatabasesMongoDBInstanceTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.deleteDatabasesMongoDBInstance(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Delete
     *
     * Remove a Managed MySQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatabasesMySQLInstanceTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.deleteDatabasesMySQLInstance(instanceId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Delete
     *
     * Remove a Managed PostgreSQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDatabasesPostgreSQLInstanceTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.deleteDatabasesPostgreSQLInstance(instanceId);
        // TODO: test validations
    }

    /**
     * Managed Database Engine View
     *
     * Display information for a single Managed Database engine type and version. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesEngineTest() throws ApiException {
        String engineId = null;
        Integer page = null;
        Integer pageSize = null;
        DatabaseEngine response = api.getDatabasesEngine(engineId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed Database Engines List
     *
     * Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesEnginesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesEngines200Response response = api.getDatabasesEngines(page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed Databases List All
     *
     * Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its &#x60;instance_uri&#x60;. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesInstancesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesInstances200Response response = api.getDatabasesInstances(page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database View
     *
     * Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMongoDBInstanceTest() throws ApiException {
        Integer instanceId = null;
        DatabaseMongoDB response = api.getDatabasesMongoDBInstance(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Backup View
     *
     * Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMongoDBInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        DatabaseBackup response = api.getDatabasesMongoDBInstanceBackup(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Backups List
     *
     * Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMongoDBInstanceBackupsTest() throws ApiException {
        Integer instanceId = null;
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesMongoDBInstanceBackups200Response response = api.getDatabasesMongoDBInstanceBackups(instanceId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Credentials View
     *
     * Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMongoDBInstanceCredentialsTest() throws ApiException {
        Integer instanceId = null;
        DatabaseCredentials response = api.getDatabasesMongoDBInstanceCredentials(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database SSL Certificate View
     *
     * Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMongoDBInstanceSSLTest() throws ApiException {
        Integer instanceId = null;
        DatabaseSSL response = api.getDatabasesMongoDBInstanceSSL(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Databases List
     *
     * Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMongoDBInstancesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesMongoDBInstances200Response response = api.getDatabasesMongoDBInstances(page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database View
     *
     * Display information for a single, accessible Managed MySQL Database. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMySQLInstanceTest() throws ApiException {
        Integer instanceId = null;
        DatabaseMySQL response = api.getDatabasesMySQLInstance(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Backup View
     *
     * Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMySQLInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        DatabaseBackup response = api.getDatabasesMySQLInstanceBackup(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Backups List
     *
     * Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMySQLInstanceBackupsTest() throws ApiException {
        Integer instanceId = null;
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesMongoDBInstanceBackups200Response response = api.getDatabasesMySQLInstanceBackups(instanceId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Credentials View
     *
     * Display the root username and password for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMySQLInstanceCredentialsTest() throws ApiException {
        Integer instanceId = null;
        DatabaseCredentials response = api.getDatabasesMySQLInstanceCredentials(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database SSL Certificate View
     *
     * Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMySQLInstanceSSLTest() throws ApiException {
        Integer instanceId = null;
        DatabaseSSL response = api.getDatabasesMySQLInstanceSSL(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Databases List
     *
     * Display all accessible Managed MySQL Databases. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesMySQLInstancesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesMySQLInstances200Response response = api.getDatabasesMySQLInstances(page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database View
     *
     * Display information for a single, accessible Managed PostgreSQL Database. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesPostgreSQLInstanceTest() throws ApiException {
        Integer instanceId = null;
        DatabasePostgreSQL response = api.getDatabasesPostgreSQLInstance(instanceId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Backup View
     *
     * Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesPostgreSQLInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        DatabaseBackup response = api.getDatabasesPostgreSQLInstanceBackup(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Backups List
     *
     * Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesPostgreSQLInstanceBackupsTest() throws ApiException {
        Integer instanceId = null;
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesMongoDBInstanceBackups200Response response = api.getDatabasesPostgreSQLInstanceBackups(instanceId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Credentials View
     *
     * Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesPostgreSQLInstanceCredentialsTest() throws ApiException {
        Integer instanceId = null;
        DatabaseCredentials response = api.getDatabasesPostgreSQLInstanceCredentials(instanceId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database SSL Certificate View
     *
     * Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesPostgreSQLInstanceSSLTest() throws ApiException {
        Integer instanceId = null;
        DatabaseSSL response = api.getDatabasesPostgreSQLInstanceSSL(instanceId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Databases List
     *
     * Display all accessible Managed PostgreSQL Databases. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesPostgreSQLInstancesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesPostgreSQLInstances200Response response = api.getDatabasesPostgreSQLInstances(page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed Database Type View
     *
     * Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesTypeTest() throws ApiException {
        String typeId = null;
        Integer page = null;
        Integer pageSize = null;
        DatabaseType response = api.getDatabasesType(typeId, page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed Database Types List
     *
     * Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDatabasesTypesTest() throws ApiException {
        Integer page = null;
        Integer pageSize = null;
        GetDatabasesTypes200Response response = api.getDatabasesTypes(page, pageSize);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Backup Snapshot Create
     *
     * Creates a snapshot backup of a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMongoDBInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        DatabaseBackupSnapshot databaseBackupSnapshot = null;
        Object response = api.postDatabasesMongoDBInstanceBackup(instanceId, databaseBackupSnapshot);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Backup Restore
     *
     * Restore a backup to a Managed MongoDB Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMongoDBInstanceBackupRestoreTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        Object response = api.postDatabasesMongoDBInstanceBackupRestore(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Credentials Reset
     *
     * Reset the root password for a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMongoDBInstanceCredentialsResetTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.postDatabasesMongoDBInstanceCredentialsReset(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Patch
     *
     * Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMongoDBInstancePatchTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.postDatabasesMongoDBInstancePatch(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Backup Snapshot Create
     *
     * Creates a snapshot backup of a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMySQLInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        DatabaseBackupSnapshot databaseBackupSnapshot = null;
        Object response = api.postDatabasesMySQLInstanceBackup(instanceId, databaseBackupSnapshot);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Backup Restore
     *
     * Restore a backup to a Managed MySQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMySQLInstanceBackupRestoreTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        Object response = api.postDatabasesMySQLInstanceBackupRestore(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Credentials Reset
     *
     * Reset the root password for a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMySQLInstanceCredentialsResetTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.postDatabasesMySQLInstanceCredentialsReset(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Patch
     *
     * Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMySQLInstancePatchTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.postDatabasesMySQLInstancePatch(instanceId);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Create
     *
     * Provision a Managed MySQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesMySQLInstancesTest() throws ApiException {
        DatabaseMySQLRequest databaseMySQLRequest = null;
        DatabaseMySQL response = api.postDatabasesMySQLInstances(databaseMySQLRequest);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Backup Snapshot Create
     *
     * Creates a snapshot backup of a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesPostgreSQLInstanceBackupTest() throws ApiException {
        Integer instanceId = null;
        DatabaseBackupSnapshot databaseBackupSnapshot = null;
        Object response = api.postDatabasesPostgreSQLInstanceBackup(instanceId, databaseBackupSnapshot);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Backup Restore
     *
     * Restore a backup to a Managed PostgreSQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesPostgreSQLInstanceBackupRestoreTest() throws ApiException {
        Integer instanceId = null;
        Integer backupId = null;
        Object response = api.postDatabasesPostgreSQLInstanceBackupRestore(instanceId, backupId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Credentials Reset
     *
     * Reset the root password for a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesPostgreSQLInstanceCredentialsResetTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.postDatabasesPostgreSQLInstanceCredentialsReset(instanceId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Patch
     *
     * Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesPostgreSQLInstancePatchTest() throws ApiException {
        Integer instanceId = null;
        Object response = api.postDatabasesPostgreSQLInstancePatch(instanceId);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Create
     *
     * Provision a Managed PostgreSQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postDatabasesPostgreSQLInstancesTest() throws ApiException {
        DatabasePostgreSQLRequest databasePostgreSQLRequest = null;
        DatabasePostgreSQL response = api.postDatabasesPostgreSQLInstances(databasePostgreSQLRequest);
        // TODO: test validations
    }

    /**
     * Managed MongoDB Database Update
     *
     * Update a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putDatabasesMongoDBInstanceTest() throws ApiException {
        Integer instanceId = null;
        PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest = null;
        DatabaseMongoDB response = api.putDatabasesMongoDBInstance(instanceId, putDatabasesMongoDBInstanceRequest);
        // TODO: test validations
    }

    /**
     * Managed MySQL Database Update
     *
     * Update a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putDatabasesMySQLInstanceTest() throws ApiException {
        Integer instanceId = null;
        PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest = null;
        DatabaseMySQL response = api.putDatabasesMySQLInstance(instanceId, putDatabasesMySQLInstanceRequest);
        // TODO: test validations
    }

    /**
     * Managed PostgreSQL Database Update
     *
     * Update a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putDatabasesPostgreSQLInstanceTest() throws ApiException {
        Integer instanceId = null;
        PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest = null;
        DatabasePostgreSQL response = api.putDatabasesPostgreSQLInstance(instanceId, putDatabasesPostgreSQLInstanceRequest);
        // TODO: test validations
    }

}
