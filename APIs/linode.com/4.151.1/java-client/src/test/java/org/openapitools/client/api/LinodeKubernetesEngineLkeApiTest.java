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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LinodeKubernetesEngineLkeApi
 */
@Disabled
public class LinodeKubernetesEngineLkeApiTest {

    private final LinodeKubernetesEngineLkeApi api = new LinodeKubernetesEngineLkeApi();

    /**
     * Kubernetes Cluster Create
     *
     * Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API server endpoint](/docs/api/linode-kubernetes-engine-lke/#kubernetes-api-endpoints-list) and the [Kubeconfig file](/docs/api/linode-kubernetes-engine-lke/#kubeconfig-view) for the new cluster are ready. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createLKEClusterTest() throws ApiException {
        CreateLKEClusterRequest createLKEClusterRequest = null;
        LKECluster response = api.createLKECluster(createLKEClusterRequest);
        // TODO: test validations
    }

    /**
     * Kubernetes Cluster Delete
     *
     * Deletes a Cluster you have permission to &#x60;read_write&#x60;.  **Deleting a Cluster is a destructive action and cannot be undone.**  Deleting a Cluster:   - Deletes all Linodes in all pools within this Kubernetes cluster   - Deletes all supporting Kubernetes services for this Kubernetes     cluster (API server, etcd, etc)   - Deletes all NodeBalancers created by this Kubernetes cluster   - Does not delete any of the volumes created by this Kubernetes     cluster 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLKEClusterTest() throws ApiException {
        Integer clusterId = null;
        Object response = api.deleteLKECluster(clusterId);
        // TODO: test validations
    }

    /**
     * Kubeconfig Delete
     *
     * Delete and regenerate the Kubeconfig file for a Cluster. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLKEClusterKubeconfigTest() throws ApiException {
        Integer clusterId = null;
        Object response = api.deleteLKEClusterKubeconfig(clusterId);
        // TODO: test validations
    }

    /**
     * Node Delete
     *
     * Deletes a specific Node from a Node Pool.  **Deleting a Node is a destructive action and cannot be undone.**  Deleting a Node will reduce the size of the Node Pool it belongs to. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLKEClusterNodeTest() throws ApiException {
        Integer clusterId = null;
        String nodeId = null;
        Object response = api.deleteLKEClusterNode(clusterId, nodeId);
        // TODO: test validations
    }

    /**
     * Node Pool Delete
     *
     * Delete a specific Node Pool from a Kubernetes cluster.  **Deleting a Node Pool is a destructive action and cannot be undone.**  Deleting a Node Pool will delete all Linodes within that Pool. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLKENodePoolTest() throws ApiException {
        Integer clusterId = null;
        Integer poolId = null;
        Object response = api.deleteLKENodePool(clusterId, poolId);
        // TODO: test validations
    }

    /**
     * Kubernetes Cluster View
     *
     * Get a specific Cluster by ID. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClusterTest() throws ApiException {
        Integer clusterId = null;
        LKECluster response = api.getLKECluster(clusterId);
        // TODO: test validations
    }

    /**
     * Kubernetes API Endpoints List
     *
     * List the Kubernetes API server endpoints for this cluster. Please note that it often takes 2-5 minutes before the endpoint is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClusterAPIEndpointsTest() throws ApiException {
        Integer clusterId = null;
        GetLKEClusterAPIEndpoints200Response response = api.getLKEClusterAPIEndpoints(clusterId);
        // TODO: test validations
    }

    /**
     * Kubernetes Cluster Dashboard URL View
     *
     * Get a [Kubernetes Dashboard](https://github.com/kubernetes/dashboard) access URL for this Cluster, which enables performance of administrative tasks through a web interface.  Dashboards are installed for Clusters by default.  To access the Cluster Dashboard login prompt, enter the URL in a web browser. Select either **Token** or **Kubeconfig** authentication, then select **Sign in**.  For additional guidance on using the Cluster Dashboard, see the [Navigating the Cluster Dashboard](/docs/guides/using-the-kubernetes-dashboard-on-lke/#navigating-the-cluster-dashboard) section of our guide on [Using the Kubernetes Dashboard on LKE](/docs/guides/using-the-kubernetes-dashboard-on-lke/). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClusterDashboardTest() throws ApiException {
        Integer clusterId = null;
        GetLKEClusterDashboard200Response response = api.getLKEClusterDashboard(clusterId);
        // TODO: test validations
    }

    /**
     * Kubeconfig View
     *
     * Get the Kubeconfig file for a Cluster. Please note that it often takes 2-5 minutes before the Kubeconfig file is ready after first [creating a new cluster](/docs/api/linode-kubernetes-engine-lke/#kubernetes-cluster-create). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClusterKubeconfigTest() throws ApiException {
        Integer clusterId = null;
        GetLKEClusterKubeconfig200Response response = api.getLKEClusterKubeconfig(clusterId);
        // TODO: test validations
    }

    /**
     * Node View
     *
     * Returns the values for a specified node object. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClusterNodeTest() throws ApiException {
        Integer clusterId = null;
        String nodeId = null;
        GetLKEClusterNode200Response response = api.getLKEClusterNode(clusterId, nodeId);
        // TODO: test validations
    }

    /**
     * Node Pools List
     *
     * Returns all active Node Pools on a Kubernetes cluster. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClusterPoolsTest() throws ApiException {
        Integer clusterId = null;
        GetLKEClusterPools200Response response = api.getLKEClusterPools(clusterId);
        // TODO: test validations
    }

    /**
     * Kubernetes Clusters List
     *
     * Lists current Kubernetes clusters available on your account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEClustersTest() throws ApiException {
        GetLKEClusters200Response response = api.getLKEClusters();
        // TODO: test validations
    }

    /**
     * Node Pool View
     *
     * Get a specific Node Pool by ID. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKENodePoolTest() throws ApiException {
        Integer clusterId = null;
        Integer poolId = null;
        LKENodePool response = api.getLKENodePool(clusterId, poolId);
        // TODO: test validations
    }

    /**
     * Kubernetes Version View
     *
     * View a Kubernetes version available for deployment to a Kubernetes cluster. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEVersionTest() throws ApiException {
        String version = null;
        LKEVersion response = api.getLKEVersion(version);
        // TODO: test validations
    }

    /**
     * Kubernetes Versions List
     *
     * List the Kubernetes versions available for deployment to a Kubernetes cluster. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLKEVersionsTest() throws ApiException {
        GetLKEVersions200Response response = api.getLKEVersions();
        // TODO: test validations
    }

    /**
     * Service Token Delete
     *
     * Delete and regenerate the service account token for a Cluster.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postLKECServiceTokenDeleteTest() throws ApiException {
        Integer clusterId = null;
        Object response = api.postLKECServiceTokenDelete(clusterId);
        // TODO: test validations
    }

    /**
     * Node Recycle
     *
     * Recycles an individual Node in the designated Kubernetes Cluster. The Node will be deleted and replaced with a new Linode, which may take a few minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postLKEClusterNodeRecycleTest() throws ApiException {
        Integer clusterId = null;
        String nodeId = null;
        Object response = api.postLKEClusterNodeRecycle(clusterId, nodeId);
        // TODO: test validations
    }

    /**
     * Node Pool Recycle
     *
     * Recycles a Node Pool for the designated Kubernetes Cluster. All Linodes within the Node Pool will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch for the Cluster&#39;s Kubernetes Version.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postLKEClusterPoolRecycleTest() throws ApiException {
        Integer clusterId = null;
        Integer poolId = null;
        Object response = api.postLKEClusterPoolRecycle(clusterId, poolId);
        // TODO: test validations
    }

    /**
     * Node Pool Create
     *
     * Creates a new Node Pool for the designated Kubernetes cluster. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postLKEClusterPoolsTest() throws ApiException {
        Integer clusterId = null;
        UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = null;
        LKENodePool response = api.postLKEClusterPools(clusterId, UNKNOWN_BASE_TYPE);
        // TODO: test validations
    }

    /**
     * Cluster Nodes Recycle
     *
     * Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available [patch version](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#kubernetes-release-versioning) for the Cluster&#39;s current Kubernetes minor release.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postLKEClusterRecycleTest() throws ApiException {
        Integer clusterId = null;
        Object response = api.postLKEClusterRecycle(clusterId);
        // TODO: test validations
    }

    /**
     * Kubernetes Cluster Regenerate
     *
     * Regenerate the Kubeconfig file and/or the service account token for a Cluster.  This is a helper command that allows performing both the [Kubeconfig Delete](#kubeconfig-delete) and the [Service Token Delete](#service-token-delete) actions with a single request.  When using this command, at least one of &#x60;kubeconfig&#x60; or &#x60;servicetoken&#x60; is required.  **Note**: When regenerating a service account token, the Cluster&#39;s control plane components and Linode CSI drivers are also restarted and configured with the new token. High Availability Clusters should not experience any disruption, while standard Clusters may experience brief control plane downtime while components are restarted. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postLKEClusterRegenerateTest() throws ApiException {
        Integer clusterId = null;
        PostLKEClusterRegenerateRequest postLKEClusterRegenerateRequest = null;
        Object response = api.postLKEClusterRegenerate(clusterId, postLKEClusterRegenerateRequest);
        // TODO: test validations
    }

    /**
     * Kubernetes Cluster Update
     *
     * Updates a Kubernetes cluster. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putLKEClusterTest() throws ApiException {
        Integer clusterId = null;
        PutLKEClusterRequest putLKEClusterRequest = null;
        PutLKECluster200Response response = api.putLKECluster(clusterId, putLKEClusterRequest);
        // TODO: test validations
    }

    /**
     * Node Pool Update
     *
     * Updates a Node Pool&#39;s count and autoscaler configuration.  Linodes will be created or deleted to match changes to the Node Pool&#39;s count.  **Any local storage on deleted Linodes (such as \&quot;hostPath\&quot; and \&quot;emptyDir\&quot; volumes, or \&quot;local\&quot; PersistentVolumes) will be erased.** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putLKENodePoolTest() throws ApiException {
        Integer clusterId = null;
        Integer poolId = null;
        PutLKENodePoolRequest putLKENodePoolRequest = null;
        LKENodePool response = api.putLKENodePool(clusterId, poolId, putLKENodePoolRequest);
        // TODO: test validations
    }

}
