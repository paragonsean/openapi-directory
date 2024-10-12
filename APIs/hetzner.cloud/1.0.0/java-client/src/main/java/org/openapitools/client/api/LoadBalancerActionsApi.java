/*
 * Hetzner Cloud API
 * This is the official API documentation for the Public Hetzner Cloud.  ## Introduction  The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests and responses.  As an alternative to working directly with our API you may also consider to use: * Our CLI program [hcloud](https://github.com/hetznercloud/cli) * Our [library for Go](https://github.com/hetznercloud/hcloud-go) * Our [library for Python](https://github.com/hetznercloud/hcloud-python)  Also you can find a [list of libraries, tools, and integrations on GitHub](https://github.com/hetznercloud/awesome-hcloud).  If you are developing integrations based on our API and your product is Open Source you may be eligible for a free one time €50 (excl. VAT) credit on your account. Please contact us via the the support page on your Cloud Console and let us know the following: * The type of integration you would like to develop * Link to the GitHub repo you will use for the Project * Link to some other Open Source work you have already done (if you have done so)  ## Getting Started To get started using the API you first need an API token. Sign in into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token. Make sure to copy the token because it won’t be shown to you again. A token is bound to a Project, to interact with the API of another Project you have to create a new token inside the Project. Let’s say your new token is `jEheVytlAoFl7F8MqUQ7jAo2hOXASztX`.  You’re now ready to do your first request against the API. To get a list of all Servers in your Project, issue the example request on the right side using [curl](https://curl.haxx.se/).  Make sure to replace the token in the example command with the token you have just created. Since your Project probably does not contain any Servers yet, the example response will look like the response on the right side. We will almost always provide a resource root like `servers` inside the example response. A response can also contain a `meta` object with information like [Pagination](https://docs.hetzner.cloud/#overview-pagination).  **Example Request** ```bash curl -H \"Authorization: Bearer jEheVytlAoFl7F8MqUQ7jAo2hOXASztX\" \\     https://api.hetzner.cloud/v1/servers ```  **Example Response** ```json {     \"servers\": [],     \"meta\": {         \"pagination\": {             \"page\": 1,             \"per_page\": 25,             \"previous_page\": null,             \"next_page\": null,             \"last_page\": 1,             \"total_entries\": 0         }     } } ```  ## Authentication All requests to the Hetzner Cloud API must be authenticated via a API token. Include your secret API token in every request you send to the API with the `Authorization` HTTP header.  To create a new API token for your Project, switch into the [Hetzner Cloud Console](https://console.hetzner.cloud/) choose a Project, go to `Security` → `API Tokens`, and generate a new token.  **Example Authorization header** ```html Authorization: Bearer LRK9DAWQ1ZAEFSrCNEEzLCUwhYX1U3g7wMg4dTlkkDC96fyDuyJ39nVbVjCKSDfj ```  ## Errors Errors are indicated by HTTP status codes. Further, the response of the request which generated the error contains an error code, an error message, and, optionally, error details. The schema of the error details object depends on the error code.  The error response contains the following keys:  | Keys      | Meaning                                                               | |-----------|-----------------------------------------------------------------------| | `code`    | Short string indicating the type of error (machine-parsable)          | | `message` | Textual description on what has gone wrong                            | | `details` | An object providing for details on the error (schema depends on code) |  **Example response** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  ### Error Codes  | Code                      | Description                                                                      | |---------------------------|----------------------------------------------------------------------------------| | `forbidden`               | Insufficient permissions for this request                                        | | `invalid_input`           | Error while parsing or processing the input                                      | | `json_error`              | Invalid JSON input in your request                                               | | `locked`                  | The item you are trying to access is locked (there is already an Action running) | | `not_found`               | Entity not found                                                                 | | `rate_limit_exceeded`     | Error when sending too many requests                                             | | `resource_limit_exceeded` | Error when exceeding the maximum quantity of a resource for an account           | | `resource_unavailable`    | The requested resource is currently unavailable                                  | | `service_error`           | Error within a service                                                           | | `uniqueness_error`        | One or more of the objects fields must be unique                                 | | `protected`               | The Action you are trying to start is protected for this resource                | | `maintenance`             | Cannot perform operation due to maintenance                                      | | `conflict`                | The resource has changed during the request, please retry                        | | `unsupported_error`       | The corresponding resource does not support the Action                           | | `token_readonly`          | The token is only allowed to perform GET requests                                | | `unavailable`             | A service or product is currently not available                                  |  **invalid_input** ```json {   \"error\": {     \"code\": \"invalid_input\",     \"message\": \"invalid input in field 'broken_field': is too long\",     \"details\": {       \"fields\": [         {           \"name\": \"broken_field\",           \"messages\": [\"is too long\"]         }       ]     }   } } ```  **uniqueness_error** ```json {   \"error\": {     \"code\": \"uniqueness_error\",     \"message\": \"SSH key with the same fingerprint already exists\",     \"details\": {       \"fields\": [         {           \"name\": \"public_key\"         }       ]     }   } } ```  **resource_limit_exceeded** ```json {   \"error\": {     \"code\": \"resource_limit_exceeded\",     \"message\": \"project limit exceeded\",     \"details\": {       \"limits\": [         {           \"name\": \"project_limit\"         }       ]     }   } } ```  ## Labels Labels are `key/value` pairs that can be attached to all resources.  Valid label keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be a string of 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).  Valid label values must be a string of 63 characters or less and must be empty or begin and end with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.  The `hetzner.cloud/` prefix is reserved and cannot be used.  **Example Labels** ```json {   \"labels\": {     \"environment\":\"development\",     \"service\":\"backend\",     \"example.com/my\":\"label\",     \"just-a-key\":\"\"   } } ```  ## Label Selector For resources with labels, you can filter resources by their labels using the label selector query language.  | Expression           | Meaning                                                             | |----------------------|---------------------------------------------------------------------| | `k==v` / `k=v`       | Value of key `k` does equal value `v`                               | | `k!=v`               | Value of key `k` does not equal value `v`                           | | `k`                  | Key `k` is present                                                  | | `!k`                 | Key `k` is not present                                              | | `k in (v1,v2,v3)`    | Value of key `k` is `v1`, `v2`, or `v3`                             | | `k notin (v1,v2,v3)` | Value of key `k` is neither `v1`, nor `v2`, nor `v3`                | | `k1==v,!k2`          | Value of key `k1` is `v` and key `k2` is not present                |  ### Examples * Returns all resources that have a `env=production` label and that don't have a `type=database` label:    `env=production,type!=database` * Returns all resources that have a `env=testing` or `env=staging` label:      `env in (testing,staging)` * Returns all resources that don't have a `type` label:      `!type`  ## Pagination Responses which return multiple items support pagination. If they do support pagination, it can be controlled with following query string parameters:  * A `page` parameter specifies the page to fetch. The number of the first page is 1. * A `per_page` parameter specifies the number of items returned per page. The default value is 25, the maximum value is 50 except otherwise specified in the documentation.  Responses contain a `Link` header with pagination information.  Additionally, if the response body is JSON and the root object is an object, that object has a `pagination` object inside the `meta` object with pagination information:  **Example Pagination** ```json {     \"servers\": [...],     \"meta\": {         \"pagination\": {             \"page\": 2,             \"per_page\": 25,             \"previous_page\": 1,             \"next_page\": 3,             \"last_page\": 4,             \"total_entries\": 100         }     } } ```  The keys `previous_page`, `next_page`, `last_page`, and `total_entries` may be `null` when on the first page, last page, or when the total number of entries is unknown.  **Example Pagination Link header** ```bash Link: <https://api.hetzner.cloud/v1/actions?page=2&per_page=5>; rel=\"prev\",       <https://api.hetzner.cloud/v1/actions?page=4&per_page=5>; rel=\"next\",       <https://api.hetzner.cloud/v1/actions?page=6&per_page=5>; rel=\"last\" ```  Line breaks have been added for display purposes only and responses may only contain some of the above `rel` values.  ## Rate Limiting All requests, whether they are authenticated or not, are subject to rate limiting. If you have reached your limit, your requests will be handled with a `429 Too Many Requests` error. Burst requests are allowed. Responses contain serveral headers which provide information about your current rate limit status.  * The `RateLimit-Limit` header contains the total number of requests you can perform per hour. * The `RateLimit-Remaining` header contains the number of requests remaining in the current rate limit time frame. * The `RateLimit-Reset` header contains a UNIX timestamp of the point in time when your rate limit will have recovered and you will have the full number of requests available again.  The default limit is 3600 requests per hour and per Project. The number of remaining requests increases gradually. For example, when your limit is 3600 requests per hour, the number of remaining requests will increase by 1 every second.  ## Server Metadata Your Server can discover metadata about itself by doing a HTTP request to specific URLs. The following data is available:  | Data              | Format | Contents                                                     | |-------------------|--------|--------------------------------------------------------------| | hostname          | text   | Name of the Server as set in the api                         | | instance-id       | number | ID of the server                                             | | public-ipv4       | text   | Primary public IPv4 address                                  | | private-networks  | yaml   | Details about the private networks the Server is attached to | | availability-zone | text   | Name of the availability zone that Server runs in            | | region            | text   | Network zone, e.g. eu-central                                |  **Example: Summary** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata ```  ```yaml availability-zone: hel1-dc2 hostname: my-server instance-id: 42 public-ipv4: 1.2.3.4 region: eu-central ```  **Example: Hostname** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/hostname my-server ```  **Example: Instance ID** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/instance-id 42 ```  **Example: Public IPv4** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/public-ipv4 1.2.3.4 ```  **Example: Private Networks** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/private-networks ```  ```json - ip: 10.0.0.2   alias_ips: [10.0.0.3, 10.0.0.4]   interface_num: 1   mac_address: 86:00:00:2a:7d:e0   network_id: 1234   network_name: nw-test1   network: 10.0.0.0/8   subnet: 10.0.0.0/24   gateway: 10.0.0.1 - ip: 192.168.0.2   alias_ips: []   interface_num: 2   mac_address: 86:00:00:2a:7d:e1   network_id: 4321   network_name: nw-test2   network: 192.168.0.0/16   subnet: 192.168.0.0/24   gateway: 192.168.0.1 ```  **Example: Availability Zone** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/availability-zone hel1-dc2 ```  **Example: Region** ```bash $ curl http://169.254.169.254/hetzner/v1/metadata/region eu-central ```  ## Sorting Some responses which return multiple items support sorting. If they do support sorting the documentation states which fields can be used for sorting. You specify sorting with the `sort` query string parameter. You can sort by multiple fields. You can set the sort direction by appending `:asc` or `:desc` to the field name. By default, ascending sorting is used.  **Example: Sorting** ```bash https://api.hetzner.cloud/v1/actions?sort=status https://api.hetzner.cloud/v1/actions?sort=status:asc https://api.hetzner.cloud/v1/actions?sort=status:desc https://api.hetzner.cloud/v1/actions?sort=status:asc&sort=command:desc ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
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


import org.openapitools.client.model.ActionResponse;
import org.openapitools.client.model.ActionsResponse;
import org.openapitools.client.model.AddTargetRequest;
import org.openapitools.client.model.ChangeLoadbalancerDnsPtrRequest;
import org.openapitools.client.model.ChangeTypeRequest;
import org.openapitools.client.model.LoadBalancerService;
import org.openapitools.client.model.LoadBalancersIdActionsAttachToNetworkPostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsChangeAlgorithmPostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsChangeProtectionPostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsDeleteServicePostRequest;
import org.openapitools.client.model.LoadBalancersIdActionsDetachFromNetworkPostRequest;
import org.openapitools.client.model.RemoveTargetRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LoadBalancerActionsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LoadBalancerActionsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LoadBalancerActionsApi(ApiClient apiClient) {
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
     * Build call for loadBalancersIdActionsActionIdGet
     * @param id ID of the Load Balancer (required)
     * @param actionId ID of the Action (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;action&#x60; key contains the Load Balancer Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsActionIdGetCall(Integer id, Integer actionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/load_balancers/{id}/actions/{action_id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "action_id" + "}", localVarApiClient.escapeString(actionId.toString()));

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
    private okhttp3.Call loadBalancersIdActionsActionIdGetValidateBeforeCall(Integer id, Integer actionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsActionIdGet(Async)");
        }

        // verify the required parameter 'actionId' is set
        if (actionId == null) {
            throw new ApiException("Missing the required parameter 'actionId' when calling loadBalancersIdActionsActionIdGet(Async)");
        }

        return loadBalancersIdActionsActionIdGetCall(id, actionId, _callback);

    }

    /**
     * Get an Action for a Load Balancer
     * Returns a specific Action for a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param actionId ID of the Action (required)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;action&#x60; key contains the Load Balancer Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsActionIdGet(Integer id, Integer actionId) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsActionIdGetWithHttpInfo(id, actionId);
        return localVarResp.getData();
    }

    /**
     * Get an Action for a Load Balancer
     * Returns a specific Action for a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param actionId ID of the Action (required)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;action&#x60; key contains the Load Balancer Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsActionIdGetWithHttpInfo(Integer id, Integer actionId) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsActionIdGetValidateBeforeCall(id, actionId, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get an Action for a Load Balancer (asynchronously)
     * Returns a specific Action for a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param actionId ID of the Action (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;action&#x60; key contains the Load Balancer Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsActionIdGetAsync(Integer id, Integer actionId, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsActionIdGetValidateBeforeCall(id, actionId, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsAddServicePost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsAddServicePostCall(Integer id, LoadBalancerService loadBalancerService, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancerService;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/add_service"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsAddServicePostValidateBeforeCall(Integer id, LoadBalancerService loadBalancerService, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsAddServicePost(Async)");
        }

        return loadBalancersIdActionsAddServicePostCall(id, loadBalancerService, _callback);

    }

    /**
     * Add Service
     * Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsAddServicePost(Integer id, LoadBalancerService loadBalancerService) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsAddServicePostWithHttpInfo(id, loadBalancerService);
        return localVarResp.getData();
    }

    /**
     * Add Service
     * Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsAddServicePostWithHttpInfo(Integer id, LoadBalancerService loadBalancerService) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsAddServicePostValidateBeforeCall(id, loadBalancerService, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add Service (asynchronously)
     * Adds a service to a Load Balancer.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsAddServicePostAsync(Integer id, LoadBalancerService loadBalancerService, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsAddServicePostValidateBeforeCall(id, loadBalancerService, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsAddTargetPost
     * @param id ID of the Load Balancer (required)
     * @param addTargetRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsAddTargetPostCall(Integer id, AddTargetRequest addTargetRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addTargetRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/add_target"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsAddTargetPostValidateBeforeCall(Integer id, AddTargetRequest addTargetRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsAddTargetPost(Async)");
        }

        return loadBalancersIdActionsAddTargetPostCall(id, addTargetRequest, _callback);

    }

    /**
     * Add Target
     * Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 
     * @param id ID of the Load Balancer (required)
     * @param addTargetRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsAddTargetPost(Integer id, AddTargetRequest addTargetRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsAddTargetPostWithHttpInfo(id, addTargetRequest);
        return localVarResp.getData();
    }

    /**
     * Add Target
     * Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 
     * @param id ID of the Load Balancer (required)
     * @param addTargetRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsAddTargetPostWithHttpInfo(Integer id, AddTargetRequest addTargetRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsAddTargetPostValidateBeforeCall(id, addTargetRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add Target (asynchronously)
     * Adds a target to a Load Balancer.  #### Call specific error codes  | Code                                    | Description                                                                                           | |-----------------------------------------|-------------------------------------------------------------------------------------------------------| | &#x60;cloud_resource_ip_not_allowed&#x60;         | The IP you are trying to add as a target belongs to a Hetzner Cloud resource                          | | &#x60;ip_not_owned&#x60;                          | The IP you are trying to add as a target is not owned by the Project owner                            | | &#x60;load_balancer_not_attached_to_network&#x60; | The Load Balancer is not attached to a network                                                        | | &#x60;robot_unavailable&#x60;                     | Robot was not available. The caller may retry the operation after a short delay.                      | | &#x60;server_not_attached_to_network&#x60;        | The server you are trying to add as a target is not attached to the same network as the Load Balancer | | &#x60;target_already_defined&#x60;                | The Load Balancer target you are trying to define is already defined                                  | 
     * @param id ID of the Load Balancer (required)
     * @param addTargetRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;add_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsAddTargetPostAsync(Integer id, AddTargetRequest addTargetRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsAddTargetPostValidateBeforeCall(id, addTargetRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsAttachToNetworkPost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsAttachToNetworkPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;attach_to_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsAttachToNetworkPostCall(Integer id, LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancersIdActionsAttachToNetworkPostRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/attach_to_network"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsAttachToNetworkPostValidateBeforeCall(Integer id, LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsAttachToNetworkPost(Async)");
        }

        return loadBalancersIdActionsAttachToNetworkPostCall(id, loadBalancersIdActionsAttachToNetworkPostRequest, _callback);

    }

    /**
     * Attach a Load Balancer to a Network
     * Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsAttachToNetworkPostRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;attach_to_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsAttachToNetworkPost(Integer id, LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsAttachToNetworkPostWithHttpInfo(id, loadBalancersIdActionsAttachToNetworkPostRequest);
        return localVarResp.getData();
    }

    /**
     * Attach a Load Balancer to a Network
     * Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsAttachToNetworkPostRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;attach_to_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsAttachToNetworkPostWithHttpInfo(Integer id, LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsAttachToNetworkPostValidateBeforeCall(id, loadBalancersIdActionsAttachToNetworkPostRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Attach a Load Balancer to a Network (asynchronously)
     * Attach a Load Balancer to a Network.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;load_balancer_already_attached&#x60; | The Load Balancer is already attached to a network                    | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Load Balancer within the network | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsAttachToNetworkPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;attach_to_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsAttachToNetworkPostAsync(Integer id, LoadBalancersIdActionsAttachToNetworkPostRequest loadBalancersIdActionsAttachToNetworkPostRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsAttachToNetworkPostValidateBeforeCall(id, loadBalancersIdActionsAttachToNetworkPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsChangeAlgorithmPost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeAlgorithmPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_algorithm&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeAlgorithmPostCall(Integer id, LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancersIdActionsChangeAlgorithmPostRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/change_algorithm"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsChangeAlgorithmPostValidateBeforeCall(Integer id, LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsChangeAlgorithmPost(Async)");
        }

        return loadBalancersIdActionsChangeAlgorithmPostCall(id, loadBalancersIdActionsChangeAlgorithmPostRequest, _callback);

    }

    /**
     * Change Algorithm
     * Change the algorithm that determines to which target new requests are sent.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeAlgorithmPostRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_algorithm&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsChangeAlgorithmPost(Integer id, LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsChangeAlgorithmPostWithHttpInfo(id, loadBalancersIdActionsChangeAlgorithmPostRequest);
        return localVarResp.getData();
    }

    /**
     * Change Algorithm
     * Change the algorithm that determines to which target new requests are sent.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeAlgorithmPostRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_algorithm&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsChangeAlgorithmPostWithHttpInfo(Integer id, LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsChangeAlgorithmPostValidateBeforeCall(id, loadBalancersIdActionsChangeAlgorithmPostRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Change Algorithm (asynchronously)
     * Change the algorithm that determines to which target new requests are sent.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeAlgorithmPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_algorithm&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeAlgorithmPostAsync(Integer id, LoadBalancersIdActionsChangeAlgorithmPostRequest loadBalancersIdActionsChangeAlgorithmPostRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsChangeAlgorithmPostValidateBeforeCall(id, loadBalancersIdActionsChangeAlgorithmPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsChangeDnsPtrPost
     * @param id ID of the Load Balancer (required)
     * @param changeLoadbalancerDnsPtrRequest Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key in the reply contains an Action object with this structure </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeDnsPtrPostCall(Integer id, ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = changeLoadbalancerDnsPtrRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/change_dns_ptr"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsChangeDnsPtrPostValidateBeforeCall(Integer id, ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsChangeDnsPtrPost(Async)");
        }

        return loadBalancersIdActionsChangeDnsPtrPostCall(id, changeLoadbalancerDnsPtrRequest, _callback);

    }

    /**
     * Change reverse DNS entry for this Load Balancer
     * Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 
     * @param id ID of the Load Balancer (required)
     * @param changeLoadbalancerDnsPtrRequest Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key in the reply contains an Action object with this structure </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsChangeDnsPtrPost(Integer id, ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsChangeDnsPtrPostWithHttpInfo(id, changeLoadbalancerDnsPtrRequest);
        return localVarResp.getData();
    }

    /**
     * Change reverse DNS entry for this Load Balancer
     * Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 
     * @param id ID of the Load Balancer (required)
     * @param changeLoadbalancerDnsPtrRequest Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key in the reply contains an Action object with this structure </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsChangeDnsPtrPostWithHttpInfo(Integer id, ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsChangeDnsPtrPostValidateBeforeCall(id, changeLoadbalancerDnsPtrRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Change reverse DNS entry for this Load Balancer (asynchronously)
     * Changes the hostname that will appear when getting the hostname belonging to the public IPs (IPv4 and IPv6) of this Load Balancer.  Floating IPs assigned to the Server are not affected by this. 
     * @param id ID of the Load Balancer (required)
     * @param changeLoadbalancerDnsPtrRequest Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key in the reply contains an Action object with this structure </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeDnsPtrPostAsync(Integer id, ChangeLoadbalancerDnsPtrRequest changeLoadbalancerDnsPtrRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsChangeDnsPtrPostValidateBeforeCall(id, changeLoadbalancerDnsPtrRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsChangeProtectionPost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeProtectionPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeProtectionPostCall(Integer id, LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancersIdActionsChangeProtectionPostRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/change_protection"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsChangeProtectionPostValidateBeforeCall(Integer id, LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsChangeProtectionPost(Async)");
        }

        return loadBalancersIdActionsChangeProtectionPostCall(id, loadBalancersIdActionsChangeProtectionPostRequest, _callback);

    }

    /**
     * Change Load Balancer Protection
     * Changes the protection configuration of a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeProtectionPostRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsChangeProtectionPost(Integer id, LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsChangeProtectionPostWithHttpInfo(id, loadBalancersIdActionsChangeProtectionPostRequest);
        return localVarResp.getData();
    }

    /**
     * Change Load Balancer Protection
     * Changes the protection configuration of a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeProtectionPostRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsChangeProtectionPostWithHttpInfo(Integer id, LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsChangeProtectionPostValidateBeforeCall(id, loadBalancersIdActionsChangeProtectionPostRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Change Load Balancer Protection (asynchronously)
     * Changes the protection configuration of a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsChangeProtectionPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeProtectionPostAsync(Integer id, LoadBalancersIdActionsChangeProtectionPostRequest loadBalancersIdActionsChangeProtectionPostRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsChangeProtectionPostValidateBeforeCall(id, loadBalancersIdActionsChangeProtectionPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsChangeTypePost
     * @param id ID of the Load Balancer (required)
     * @param changeTypeRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_load_balancer_type&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeTypePostCall(Integer id, ChangeTypeRequest changeTypeRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = changeTypeRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/change_type"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsChangeTypePostValidateBeforeCall(Integer id, ChangeTypeRequest changeTypeRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsChangeTypePost(Async)");
        }

        return loadBalancersIdActionsChangeTypePostCall(id, changeTypeRequest, _callback);

    }

    /**
     * Change the Type of a Load Balancer
     * Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 
     * @param id ID of the Load Balancer (required)
     * @param changeTypeRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_load_balancer_type&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsChangeTypePost(Integer id, ChangeTypeRequest changeTypeRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsChangeTypePostWithHttpInfo(id, changeTypeRequest);
        return localVarResp.getData();
    }

    /**
     * Change the Type of a Load Balancer
     * Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 
     * @param id ID of the Load Balancer (required)
     * @param changeTypeRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_load_balancer_type&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsChangeTypePostWithHttpInfo(Integer id, ChangeTypeRequest changeTypeRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsChangeTypePostValidateBeforeCall(id, changeTypeRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Change the Type of a Load Balancer (asynchronously)
     * Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.  **Call specific error codes**  | Code                         | Description                                                     | |------------------------------|-----------------------------------------------------------------| | &#x60;invalid_load_balancer_type&#x60; | The Load Balancer type does not fit for the given Load Balancer | 
     * @param id ID of the Load Balancer (required)
     * @param changeTypeRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;change_load_balancer_type&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsChangeTypePostAsync(Integer id, ChangeTypeRequest changeTypeRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsChangeTypePostValidateBeforeCall(id, changeTypeRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsDeleteServicePost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDeleteServicePostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;delete_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsDeleteServicePostCall(Integer id, LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancersIdActionsDeleteServicePostRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/delete_service"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsDeleteServicePostValidateBeforeCall(Integer id, LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsDeleteServicePost(Async)");
        }

        return loadBalancersIdActionsDeleteServicePostCall(id, loadBalancersIdActionsDeleteServicePostRequest, _callback);

    }

    /**
     * Delete Service
     * Delete a service of a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDeleteServicePostRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;delete_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsDeleteServicePost(Integer id, LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsDeleteServicePostWithHttpInfo(id, loadBalancersIdActionsDeleteServicePostRequest);
        return localVarResp.getData();
    }

    /**
     * Delete Service
     * Delete a service of a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDeleteServicePostRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;delete_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsDeleteServicePostWithHttpInfo(Integer id, LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsDeleteServicePostValidateBeforeCall(id, loadBalancersIdActionsDeleteServicePostRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete Service (asynchronously)
     * Delete a service of a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDeleteServicePostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;delete_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsDeleteServicePostAsync(Integer id, LoadBalancersIdActionsDeleteServicePostRequest loadBalancersIdActionsDeleteServicePostRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsDeleteServicePostValidateBeforeCall(id, loadBalancersIdActionsDeleteServicePostRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsDetachFromNetworkPost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDetachFromNetworkPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;detach_from_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsDetachFromNetworkPostCall(Integer id, LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancersIdActionsDetachFromNetworkPostRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/detach_from_network"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsDetachFromNetworkPostValidateBeforeCall(Integer id, LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsDetachFromNetworkPost(Async)");
        }

        return loadBalancersIdActionsDetachFromNetworkPostCall(id, loadBalancersIdActionsDetachFromNetworkPostRequest, _callback);

    }

    /**
     * Detach a Load Balancer from a Network
     * Detaches a Load Balancer from a network.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDetachFromNetworkPostRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;detach_from_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsDetachFromNetworkPost(Integer id, LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsDetachFromNetworkPostWithHttpInfo(id, loadBalancersIdActionsDetachFromNetworkPostRequest);
        return localVarResp.getData();
    }

    /**
     * Detach a Load Balancer from a Network
     * Detaches a Load Balancer from a network.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDetachFromNetworkPostRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;detach_from_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsDetachFromNetworkPostWithHttpInfo(Integer id, LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsDetachFromNetworkPostValidateBeforeCall(id, loadBalancersIdActionsDetachFromNetworkPostRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Detach a Load Balancer from a Network (asynchronously)
     * Detaches a Load Balancer from a network.
     * @param id ID of the Load Balancer (required)
     * @param loadBalancersIdActionsDetachFromNetworkPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;detach_from_network&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsDetachFromNetworkPostAsync(Integer id, LoadBalancersIdActionsDetachFromNetworkPostRequest loadBalancersIdActionsDetachFromNetworkPostRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsDetachFromNetworkPostValidateBeforeCall(id, loadBalancersIdActionsDetachFromNetworkPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsDisablePublicInterfacePost
     * @param id ID of the Load Balancer (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;disable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsDisablePublicInterfacePostCall(Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/load_balancers/{id}/actions/disable_public_interface"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsDisablePublicInterfacePostValidateBeforeCall(Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsDisablePublicInterfacePost(Async)");
        }

        return loadBalancersIdActionsDisablePublicInterfacePostCall(id, _callback);

    }

    /**
     * Disable the public interface of a Load Balancer
     * Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 
     * @param id ID of the Load Balancer (required)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;disable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsDisablePublicInterfacePost(Integer id) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsDisablePublicInterfacePostWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Disable the public interface of a Load Balancer
     * Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 
     * @param id ID of the Load Balancer (required)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;disable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsDisablePublicInterfacePostWithHttpInfo(Integer id) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsDisablePublicInterfacePostValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Disable the public interface of a Load Balancer (asynchronously)
     * Disable the public interface of a Load Balancer. The Load Balancer will be not accessible from the internet via its public IPs.  #### Call specific error codes  | Code                                      | Description                                                                    | |-------------------------------------------|--------------------------------------------------------------------------------| | &#x60;load_balancer_not_attached_to_network&#x60;   |  The Load Balancer is not attached to a network                                | | &#x60;targets_without_use_private_ip&#x60;          | The Load Balancer has targets that use the public IP instead of the private IP | 
     * @param id ID of the Load Balancer (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;disable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsDisablePublicInterfacePostAsync(Integer id, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsDisablePublicInterfacePostValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsEnablePublicInterfacePost
     * @param id ID of the Load Balancer (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;enable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsEnablePublicInterfacePostCall(Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/load_balancers/{id}/actions/enable_public_interface"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsEnablePublicInterfacePostValidateBeforeCall(Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsEnablePublicInterfacePost(Async)");
        }

        return loadBalancersIdActionsEnablePublicInterfacePostCall(id, _callback);

    }

    /**
     * Enable the public interface of a Load Balancer
     * Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.
     * @param id ID of the Load Balancer (required)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;enable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsEnablePublicInterfacePost(Integer id) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsEnablePublicInterfacePostWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Enable the public interface of a Load Balancer
     * Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.
     * @param id ID of the Load Balancer (required)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;enable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsEnablePublicInterfacePostWithHttpInfo(Integer id) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsEnablePublicInterfacePostValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Enable the public interface of a Load Balancer (asynchronously)
     * Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the internet via its public IPs.
     * @param id ID of the Load Balancer (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;enable_public_interface&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsEnablePublicInterfacePostAsync(Integer id, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsEnablePublicInterfacePostValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsGet
     * @param id ID of the Load Balancer (required)
     * @param sort Can be used multiple times. (optional)
     * @param status Can be used multiple times, the response will contain only Actions with specified statuses (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;actions&#x60; key contains a list of Actions </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsGetCall(Integer id, String sort, String status, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/load_balancers/{id}/actions"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (status != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("status", status));
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
    private okhttp3.Call loadBalancersIdActionsGetValidateBeforeCall(Integer id, String sort, String status, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsGet(Async)");
        }

        return loadBalancersIdActionsGetCall(id, sort, status, _callback);

    }

    /**
     * Get all Actions for a Load Balancer
     * Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.
     * @param id ID of the Load Balancer (required)
     * @param sort Can be used multiple times. (optional)
     * @param status Can be used multiple times, the response will contain only Actions with specified statuses (optional)
     * @return ActionsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;actions&#x60; key contains a list of Actions </td><td>  -  </td></tr>
     </table>
     */
    public ActionsResponse loadBalancersIdActionsGet(Integer id, String sort, String status) throws ApiException {
        ApiResponse<ActionsResponse> localVarResp = loadBalancersIdActionsGetWithHttpInfo(id, sort, status);
        return localVarResp.getData();
    }

    /**
     * Get all Actions for a Load Balancer
     * Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.
     * @param id ID of the Load Balancer (required)
     * @param sort Can be used multiple times. (optional)
     * @param status Can be used multiple times, the response will contain only Actions with specified statuses (optional)
     * @return ApiResponse&lt;ActionsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;actions&#x60; key contains a list of Actions </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionsResponse> loadBalancersIdActionsGetWithHttpInfo(Integer id, String sort, String status) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsGetValidateBeforeCall(id, sort, status, null);
        Type localVarReturnType = new TypeToken<ActionsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get all Actions for a Load Balancer (asynchronously)
     * Returns all Action objects for a Load Balancer. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.
     * @param id ID of the Load Balancer (required)
     * @param sort Can be used multiple times. (optional)
     * @param status Can be used multiple times, the response will contain only Actions with specified statuses (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The &#x60;actions&#x60; key contains a list of Actions </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsGetAsync(Integer id, String sort, String status, final ApiCallback<ActionsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsGetValidateBeforeCall(id, sort, status, _callback);
        Type localVarReturnType = new TypeToken<ActionsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsRemoveTargetPost
     * @param id ID of the Load Balancer (required)
     * @param removeTargetRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;remove_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsRemoveTargetPostCall(Integer id, RemoveTargetRequest removeTargetRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = removeTargetRequest;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/remove_target"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsRemoveTargetPostValidateBeforeCall(Integer id, RemoveTargetRequest removeTargetRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsRemoveTargetPost(Async)");
        }

        return loadBalancersIdActionsRemoveTargetPostCall(id, removeTargetRequest, _callback);

    }

    /**
     * Remove Target
     * Removes a target from a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param removeTargetRequest  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;remove_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsRemoveTargetPost(Integer id, RemoveTargetRequest removeTargetRequest) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsRemoveTargetPostWithHttpInfo(id, removeTargetRequest);
        return localVarResp.getData();
    }

    /**
     * Remove Target
     * Removes a target from a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param removeTargetRequest  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;remove_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsRemoveTargetPostWithHttpInfo(Integer id, RemoveTargetRequest removeTargetRequest) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsRemoveTargetPostValidateBeforeCall(id, removeTargetRequest, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Remove Target (asynchronously)
     * Removes a target from a Load Balancer.
     * @param id ID of the Load Balancer (required)
     * @param removeTargetRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;remove_target&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsRemoveTargetPostAsync(Integer id, RemoveTargetRequest removeTargetRequest, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsRemoveTargetPostValidateBeforeCall(id, removeTargetRequest, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for loadBalancersIdActionsUpdateServicePost
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;update_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsUpdateServicePostCall(Integer id, LoadBalancerService loadBalancerService, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = loadBalancerService;

        // create path and map variables
        String localVarPath = "/load_balancers/{id}/actions/update_service"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loadBalancersIdActionsUpdateServicePostValidateBeforeCall(Integer id, LoadBalancerService loadBalancerService, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling loadBalancersIdActionsUpdateServicePost(Async)");
        }

        return loadBalancersIdActionsUpdateServicePostCall(id, loadBalancerService, _callback);

    }

    /**
     * Update Service
     * Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @return ActionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;update_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ActionResponse loadBalancersIdActionsUpdateServicePost(Integer id, LoadBalancerService loadBalancerService) throws ApiException {
        ApiResponse<ActionResponse> localVarResp = loadBalancersIdActionsUpdateServicePostWithHttpInfo(id, loadBalancerService);
        return localVarResp.getData();
    }

    /**
     * Update Service
     * Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @return ApiResponse&lt;ActionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;update_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ActionResponse> loadBalancersIdActionsUpdateServicePostWithHttpInfo(Integer id, LoadBalancerService loadBalancerService) throws ApiException {
        okhttp3.Call localVarCall = loadBalancersIdActionsUpdateServicePostValidateBeforeCall(id, loadBalancerService, null);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Service (asynchronously)
     * Updates a Load Balancer Service.  #### Call specific error codes  | Code                       | Description                                             | |----------------------------|---------------------------------------------------------| | &#x60;source_port_already_used&#x60; | The source port you are trying to add is already in use | 
     * @param id ID of the Load Balancer (required)
     * @param loadBalancerService  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> The &#x60;action&#x60; key contains the &#x60;update_service&#x60; Action </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loadBalancersIdActionsUpdateServicePostAsync(Integer id, LoadBalancerService loadBalancerService, final ApiCallback<ActionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = loadBalancersIdActionsUpdateServicePostValidateBeforeCall(id, loadBalancerService, _callback);
        Type localVarReturnType = new TypeToken<ActionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
