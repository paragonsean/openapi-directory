/*
 * Rudder API
 * Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like `/api/version/function`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) => 404 not found curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules ```  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules # Wrong => Error response indicating which versions are available curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules ```  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   <h4>Existing versions</h4> <table>   <thead>     <tr>       <th style=\"width: 20%\">Version</th>       <th style=\"width: 20%\">Rudder versions it appeared in</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">1</td>       <td class=\"code\">Never released (for internal use only)</td>       <td>Experimental version</td>     </tr>     <tr>       <td class=\"code\">2 to 10 (deprecated)</td>       <td class=\"code\">4.3 and before</td>       <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>     </tr>     <tr>       <td class=\"code\">11</td>       <td class=\"code\">5.0</td>       <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>     </tr>     <tr>       <td class=\"code\">12</td>       <td class=\"code\">6.0 and 6.1</td>       <td>Node key management</td>     </tr>     <tr>       <td class=\"code\">13</td>       <td class=\"code\">6.2</td>       <td><ul>         <li>Node status endpoint</li>         <li>System health check</li>         <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">14</td>       <td class=\"code\">7.0</td>       <td><ul>         <li>Secret management</li>         <li>Directive tree</li>         <li>Improve techniques management</li>         <li>Demote a relay</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">15</td>       <td class=\"code\">7.1</td>       <td><ul>         <li>Package updates in nodes</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">16</td>       <td class=\"code\">7.2</td>       <td><ul>         <li>Create node API included from plugin</li>         <li>Configuration archive import/export</li>       </ul></td>     </tr>   </tbody> </table>   ## Response format  All responses from the API are in the JSON format.  ```json {   \"action\": \"The name of the called function\",   \"id\": \"The ID of the element you want, if relevant\",   \"result\": \"The result of your action: success or error\",   \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",   \"errorDetails\": \"Only present if this is an error, it contains the error message\" } ```   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can't be submitted in a JSON form.  #### Available for all requests  <table>   <thead>     <tr>       <th style=\"width: 30%\">Field</th>       <th style=\"width: 10%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">prettify</td>       <td><b>boolean</b><br><i>optional</i></td>       <td>         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         <p class=\"default-value\">Default value: <code>false</code></p>       </td>     </tr>   </tbody> </table>   #### Available for modification requests (PUT/POST/DELETE)  <table>   <thead>     <tr>       <th style=\"width: 25%\">Field</th>       <th style=\"width: 12%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">reason</td>       <td><b>string</b><br><i>optional</i> or <i>required</i></td>       <td>         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestName</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         <p class=\"default-value\">Default value: <code>A default string for each function</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestDescription</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request description, is used only if workflows are enabled.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>   </tbody> </table>   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  ```bash # Get the Rule of ID \"id\" curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id ```    CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a `curl` `POST` request, that header can be provided with the `-H` parameter:  ```bash curl -X POST -H \"Content-Type: application/json\" ... ```  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.  The (human readable) format is:  ```json {   \"key1\": \"value1\",   \"key2\": false,   \"key3\": 42 } ```   Here is an example with inlined data:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id}   -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}' ```  You can also pass a supply the JSON in a file:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam ```  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\" curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\" ```  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  ``` key=value ```  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\" ```  * As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json ``` 
 *
 * The version of the OpenAPI document: 17
 * Contact: dev@rudder.io
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


import org.openapitools.client.model.AcceptChangeRequest200Response;
import org.openapitools.client.model.AcceptChangeRequestRequest;
import org.openapitools.client.model.ChangeRequestDetails200Response;
import org.openapitools.client.model.DeclineChangeRequest200Response;
import org.openapitools.client.model.ListChangeRequests200Response;
import org.openapitools.client.model.ListUsers200Response;
import org.openapitools.client.model.RemoveValidatedUser200Response;
import org.openapitools.client.model.SaveWorkflowUser200Response;
import org.openapitools.client.model.SaveWorkflowUserRequest;
import org.openapitools.client.model.UpdateChangeRequest200Response;
import org.openapitools.client.model.UpdateChangeRequestRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ChangeRequestsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ChangeRequestsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ChangeRequestsApi(ApiClient apiClient) {
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
     * Build call for acceptChangeRequest
     * @param changeRequestId  (required)
     * @param acceptChangeRequestRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acceptChangeRequestCall(Integer changeRequestId, AcceptChangeRequestRequest acceptChangeRequestRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = acceptChangeRequestRequest;

        // create path and map variables
        String localVarPath = "/changeRequests/{changeRequestId}/accept"
            .replace("{" + "changeRequestId" + "}", localVarApiClient.escapeString(changeRequestId.toString()));

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call acceptChangeRequestValidateBeforeCall(Integer changeRequestId, AcceptChangeRequestRequest acceptChangeRequestRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'changeRequestId' is set
        if (changeRequestId == null) {
            throw new ApiException("Missing the required parameter 'changeRequestId' when calling acceptChangeRequest(Async)");
        }

        // verify the required parameter 'acceptChangeRequestRequest' is set
        if (acceptChangeRequestRequest == null) {
            throw new ApiException("Missing the required parameter 'acceptChangeRequestRequest' when calling acceptChangeRequest(Async)");
        }

        return acceptChangeRequestCall(changeRequestId, acceptChangeRequestRequest, _callback);

    }

    /**
     * Accept a request details
     * Accept a change request
     * @param changeRequestId  (required)
     * @param acceptChangeRequestRequest  (required)
     * @return AcceptChangeRequest200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public AcceptChangeRequest200Response acceptChangeRequest(Integer changeRequestId, AcceptChangeRequestRequest acceptChangeRequestRequest) throws ApiException {
        ApiResponse<AcceptChangeRequest200Response> localVarResp = acceptChangeRequestWithHttpInfo(changeRequestId, acceptChangeRequestRequest);
        return localVarResp.getData();
    }

    /**
     * Accept a request details
     * Accept a change request
     * @param changeRequestId  (required)
     * @param acceptChangeRequestRequest  (required)
     * @return ApiResponse&lt;AcceptChangeRequest200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AcceptChangeRequest200Response> acceptChangeRequestWithHttpInfo(Integer changeRequestId, AcceptChangeRequestRequest acceptChangeRequestRequest) throws ApiException {
        okhttp3.Call localVarCall = acceptChangeRequestValidateBeforeCall(changeRequestId, acceptChangeRequestRequest, null);
        Type localVarReturnType = new TypeToken<AcceptChangeRequest200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Accept a request details (asynchronously)
     * Accept a change request
     * @param changeRequestId  (required)
     * @param acceptChangeRequestRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acceptChangeRequestAsync(Integer changeRequestId, AcceptChangeRequestRequest acceptChangeRequestRequest, final ApiCallback<AcceptChangeRequest200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = acceptChangeRequestValidateBeforeCall(changeRequestId, acceptChangeRequestRequest, _callback);
        Type localVarReturnType = new TypeToken<AcceptChangeRequest200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for changeRequestDetails
     * @param changeRequestId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeRequestDetailsCall(Integer changeRequestId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/changeRequests/{changeRequestId}"
            .replace("{" + "changeRequestId" + "}", localVarApiClient.escapeString(changeRequestId.toString()));

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call changeRequestDetailsValidateBeforeCall(Integer changeRequestId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'changeRequestId' is set
        if (changeRequestId == null) {
            throw new ApiException("Missing the required parameter 'changeRequestId' when calling changeRequestDetails(Async)");
        }

        return changeRequestDetailsCall(changeRequestId, _callback);

    }

    /**
     * Get a change request details
     * Get a change request details
     * @param changeRequestId  (required)
     * @return ChangeRequestDetails200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ChangeRequestDetails200Response changeRequestDetails(Integer changeRequestId) throws ApiException {
        ApiResponse<ChangeRequestDetails200Response> localVarResp = changeRequestDetailsWithHttpInfo(changeRequestId);
        return localVarResp.getData();
    }

    /**
     * Get a change request details
     * Get a change request details
     * @param changeRequestId  (required)
     * @return ApiResponse&lt;ChangeRequestDetails200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ChangeRequestDetails200Response> changeRequestDetailsWithHttpInfo(Integer changeRequestId) throws ApiException {
        okhttp3.Call localVarCall = changeRequestDetailsValidateBeforeCall(changeRequestId, null);
        Type localVarReturnType = new TypeToken<ChangeRequestDetails200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a change request details (asynchronously)
     * Get a change request details
     * @param changeRequestId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeRequestDetailsAsync(Integer changeRequestId, final ApiCallback<ChangeRequestDetails200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeRequestDetailsValidateBeforeCall(changeRequestId, _callback);
        Type localVarReturnType = new TypeToken<ChangeRequestDetails200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for declineChangeRequest
     * @param changeRequestId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call declineChangeRequestCall(Integer changeRequestId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/changeRequests/{changeRequestId}"
            .replace("{" + "changeRequestId" + "}", localVarApiClient.escapeString(changeRequestId.toString()));

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call declineChangeRequestValidateBeforeCall(Integer changeRequestId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'changeRequestId' is set
        if (changeRequestId == null) {
            throw new ApiException("Missing the required parameter 'changeRequestId' when calling declineChangeRequest(Async)");
        }

        return declineChangeRequestCall(changeRequestId, _callback);

    }

    /**
     * Decline a request details
     * Refuse a change request
     * @param changeRequestId  (required)
     * @return DeclineChangeRequest200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public DeclineChangeRequest200Response declineChangeRequest(Integer changeRequestId) throws ApiException {
        ApiResponse<DeclineChangeRequest200Response> localVarResp = declineChangeRequestWithHttpInfo(changeRequestId);
        return localVarResp.getData();
    }

    /**
     * Decline a request details
     * Refuse a change request
     * @param changeRequestId  (required)
     * @return ApiResponse&lt;DeclineChangeRequest200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeclineChangeRequest200Response> declineChangeRequestWithHttpInfo(Integer changeRequestId) throws ApiException {
        okhttp3.Call localVarCall = declineChangeRequestValidateBeforeCall(changeRequestId, null);
        Type localVarReturnType = new TypeToken<DeclineChangeRequest200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Decline a request details (asynchronously)
     * Refuse a change request
     * @param changeRequestId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call declineChangeRequestAsync(Integer changeRequestId, final ApiCallback<DeclineChangeRequest200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = declineChangeRequestValidateBeforeCall(changeRequestId, _callback);
        Type localVarReturnType = new TypeToken<DeclineChangeRequest200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listChangeRequests
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listChangeRequestsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/changeRequests";

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listChangeRequestsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listChangeRequestsCall(_callback);

    }

    /**
     * List all change requests
     * List all change requests
     * @return ListChangeRequests200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ListChangeRequests200Response listChangeRequests() throws ApiException {
        ApiResponse<ListChangeRequests200Response> localVarResp = listChangeRequestsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List all change requests
     * List all change requests
     * @return ApiResponse&lt;ListChangeRequests200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListChangeRequests200Response> listChangeRequestsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listChangeRequestsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListChangeRequests200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all change requests (asynchronously)
     * List all change requests
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listChangeRequestsAsync(final ApiCallback<ListChangeRequests200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listChangeRequestsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListChangeRequests200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listUsers
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List users </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listUsersCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users";

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listUsersValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listUsersCall(_callback);

    }

    /**
     * List user
     * List all validated and unvalidated users
     * @return ListUsers200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List users </td><td>  -  </td></tr>
     </table>
     */
    public ListUsers200Response listUsers() throws ApiException {
        ApiResponse<ListUsers200Response> localVarResp = listUsersWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List user
     * List all validated and unvalidated users
     * @return ApiResponse&lt;ListUsers200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List users </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListUsers200Response> listUsersWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listUsersValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListUsers200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List user (asynchronously)
     * List all validated and unvalidated users
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List users </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listUsersAsync(final ApiCallback<ListUsers200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listUsersValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListUsers200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for removeValidatedUser
     * @param username Username of an user (unique) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Removed user </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeValidatedUserCall(String username, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/validatedUsers/{username}"
            .replace("{" + "username" + "}", localVarApiClient.escapeString(username.toString()));

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call removeValidatedUserValidateBeforeCall(String username, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'username' is set
        if (username == null) {
            throw new ApiException("Missing the required parameter 'username' when calling removeValidatedUser(Async)");
        }

        return removeValidatedUserCall(username, _callback);

    }

    /**
     * Remove an user from validated user list
     * The user is again subject to workflow validation
     * @param username Username of an user (unique) (required)
     * @return RemoveValidatedUser200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Removed user </td><td>  -  </td></tr>
     </table>
     */
    public RemoveValidatedUser200Response removeValidatedUser(String username) throws ApiException {
        ApiResponse<RemoveValidatedUser200Response> localVarResp = removeValidatedUserWithHttpInfo(username);
        return localVarResp.getData();
    }

    /**
     * Remove an user from validated user list
     * The user is again subject to workflow validation
     * @param username Username of an user (unique) (required)
     * @return ApiResponse&lt;RemoveValidatedUser200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Removed user </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<RemoveValidatedUser200Response> removeValidatedUserWithHttpInfo(String username) throws ApiException {
        okhttp3.Call localVarCall = removeValidatedUserValidateBeforeCall(username, null);
        Type localVarReturnType = new TypeToken<RemoveValidatedUser200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Remove an user from validated user list (asynchronously)
     * The user is again subject to workflow validation
     * @param username Username of an user (unique) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Removed user </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call removeValidatedUserAsync(String username, final ApiCallback<RemoveValidatedUser200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = removeValidatedUserValidateBeforeCall(username, _callback);
        Type localVarReturnType = new TypeToken<RemoveValidatedUser200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for saveWorkflowUser
     * @param saveWorkflowUserRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Updated </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call saveWorkflowUserCall(SaveWorkflowUserRequest saveWorkflowUserRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = saveWorkflowUserRequest;

        // create path and map variables
        String localVarPath = "/validatedUsers";

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call saveWorkflowUserValidateBeforeCall(SaveWorkflowUserRequest saveWorkflowUserRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'saveWorkflowUserRequest' is set
        if (saveWorkflowUserRequest == null) {
            throw new ApiException("Missing the required parameter 'saveWorkflowUserRequest' when calling saveWorkflowUser(Async)");
        }

        return saveWorkflowUserCall(saveWorkflowUserRequest, _callback);

    }

    /**
     * Update validated user list
     * Add and remove user from validated users
     * @param saveWorkflowUserRequest  (required)
     * @return SaveWorkflowUser200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Updated </td><td>  -  </td></tr>
     </table>
     */
    public SaveWorkflowUser200Response saveWorkflowUser(SaveWorkflowUserRequest saveWorkflowUserRequest) throws ApiException {
        ApiResponse<SaveWorkflowUser200Response> localVarResp = saveWorkflowUserWithHttpInfo(saveWorkflowUserRequest);
        return localVarResp.getData();
    }

    /**
     * Update validated user list
     * Add and remove user from validated users
     * @param saveWorkflowUserRequest  (required)
     * @return ApiResponse&lt;SaveWorkflowUser200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Updated </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SaveWorkflowUser200Response> saveWorkflowUserWithHttpInfo(SaveWorkflowUserRequest saveWorkflowUserRequest) throws ApiException {
        okhttp3.Call localVarCall = saveWorkflowUserValidateBeforeCall(saveWorkflowUserRequest, null);
        Type localVarReturnType = new TypeToken<SaveWorkflowUser200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update validated user list (asynchronously)
     * Add and remove user from validated users
     * @param saveWorkflowUserRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Updated </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call saveWorkflowUserAsync(SaveWorkflowUserRequest saveWorkflowUserRequest, final ApiCallback<SaveWorkflowUser200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = saveWorkflowUserValidateBeforeCall(saveWorkflowUserRequest, _callback);
        Type localVarReturnType = new TypeToken<SaveWorkflowUser200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateChangeRequest
     * @param changeRequestId  (required)
     * @param updateChangeRequestRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateChangeRequestCall(Integer changeRequestId, UpdateChangeRequestRequest updateChangeRequestRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateChangeRequestRequest;

        // create path and map variables
        String localVarPath = "/changeRequests/{changeRequestId}"
            .replace("{" + "changeRequestId" + "}", localVarApiClient.escapeString(changeRequestId.toString()));

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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateChangeRequestValidateBeforeCall(Integer changeRequestId, UpdateChangeRequestRequest updateChangeRequestRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'changeRequestId' is set
        if (changeRequestId == null) {
            throw new ApiException("Missing the required parameter 'changeRequestId' when calling updateChangeRequest(Async)");
        }

        // verify the required parameter 'updateChangeRequestRequest' is set
        if (updateChangeRequestRequest == null) {
            throw new ApiException("Missing the required parameter 'updateChangeRequestRequest' when calling updateChangeRequest(Async)");
        }

        return updateChangeRequestCall(changeRequestId, updateChangeRequestRequest, _callback);

    }

    /**
     * Update a request details
     * Update a change request
     * @param changeRequestId  (required)
     * @param updateChangeRequestRequest  (required)
     * @return UpdateChangeRequest200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public UpdateChangeRequest200Response updateChangeRequest(Integer changeRequestId, UpdateChangeRequestRequest updateChangeRequestRequest) throws ApiException {
        ApiResponse<UpdateChangeRequest200Response> localVarResp = updateChangeRequestWithHttpInfo(changeRequestId, updateChangeRequestRequest);
        return localVarResp.getData();
    }

    /**
     * Update a request details
     * Update a change request
     * @param changeRequestId  (required)
     * @param updateChangeRequestRequest  (required)
     * @return ApiResponse&lt;UpdateChangeRequest200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateChangeRequest200Response> updateChangeRequestWithHttpInfo(Integer changeRequestId, UpdateChangeRequestRequest updateChangeRequestRequest) throws ApiException {
        okhttp3.Call localVarCall = updateChangeRequestValidateBeforeCall(changeRequestId, updateChangeRequestRequest, null);
        Type localVarReturnType = new TypeToken<UpdateChangeRequest200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a request details (asynchronously)
     * Update a change request
     * @param changeRequestId  (required)
     * @param updateChangeRequestRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Change requests information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateChangeRequestAsync(Integer changeRequestId, UpdateChangeRequestRequest updateChangeRequestRequest, final ApiCallback<UpdateChangeRequest200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateChangeRequestValidateBeforeCall(changeRequestId, updateChangeRequestRequest, _callback);
        Type localVarReturnType = new TypeToken<UpdateChangeRequest200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
