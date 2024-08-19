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


import org.openapitools.client.model.CreateGroup200Response;
import org.openapitools.client.model.CreateGroupCategory200Response;
import org.openapitools.client.model.DeleteGroup200Response;
import org.openapitools.client.model.DeleteGroupCategory200Response;
import org.openapitools.client.model.GetGroupCategoryDetails200Response;
import org.openapitools.client.model.GetGroupTree200Response;
import org.openapitools.client.model.GroupCategory;
import org.openapitools.client.model.GroupCategoryUpdate;
import org.openapitools.client.model.GroupDetails200Response;
import org.openapitools.client.model.GroupNew;
import org.openapitools.client.model.GroupUpdate;
import org.openapitools.client.model.ListGroups200Response;
import org.openapitools.client.model.ReloadGroup200Response;
import java.util.UUID;
import org.openapitools.client.model.UpdateGroup200Response;
import org.openapitools.client.model.UpdateGroupCategory200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public GroupsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public GroupsApi(ApiClient apiClient) {
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
     * Build call for createGroup
     * @param groupNew  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Group information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createGroupCall(GroupNew groupNew, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = groupNew;

        // create path and map variables
        String localVarPath = "/groups";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createGroupValidateBeforeCall(GroupNew groupNew, final ApiCallback _callback) throws ApiException {
        return createGroupCall(groupNew, _callback);

    }

    /**
     * Create a group
     * Create a new group based in provided parameters
     * @param groupNew  (optional)
     * @return CreateGroup200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Group information </td><td>  -  </td></tr>
     </table>
     */
    public CreateGroup200Response createGroup(GroupNew groupNew) throws ApiException {
        ApiResponse<CreateGroup200Response> localVarResp = createGroupWithHttpInfo(groupNew);
        return localVarResp.getData();
    }

    /**
     * Create a group
     * Create a new group based in provided parameters
     * @param groupNew  (optional)
     * @return ApiResponse&lt;CreateGroup200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Group information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateGroup200Response> createGroupWithHttpInfo(GroupNew groupNew) throws ApiException {
        okhttp3.Call localVarCall = createGroupValidateBeforeCall(groupNew, null);
        Type localVarReturnType = new TypeToken<CreateGroup200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a group (asynchronously)
     * Create a new group based in provided parameters
     * @param groupNew  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Group information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createGroupAsync(GroupNew groupNew, final ApiCallback<CreateGroup200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createGroupValidateBeforeCall(groupNew, _callback);
        Type localVarReturnType = new TypeToken<CreateGroup200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createGroupCategory
     * @param groupCategory  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createGroupCategoryCall(GroupCategory groupCategory, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = groupCategory;

        // create path and map variables
        String localVarPath = "/groups/categories";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createGroupCategoryValidateBeforeCall(GroupCategory groupCategory, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupCategory' is set
        if (groupCategory == null) {
            throw new ApiException("Missing the required parameter 'groupCategory' when calling createGroupCategory(Async)");
        }

        return createGroupCategoryCall(groupCategory, _callback);

    }

    /**
     * Create a group category
     * Create a new group category
     * @param groupCategory  (required)
     * @return CreateGroupCategory200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public CreateGroupCategory200Response createGroupCategory(GroupCategory groupCategory) throws ApiException {
        ApiResponse<CreateGroupCategory200Response> localVarResp = createGroupCategoryWithHttpInfo(groupCategory);
        return localVarResp.getData();
    }

    /**
     * Create a group category
     * Create a new group category
     * @param groupCategory  (required)
     * @return ApiResponse&lt;CreateGroupCategory200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateGroupCategory200Response> createGroupCategoryWithHttpInfo(GroupCategory groupCategory) throws ApiException {
        okhttp3.Call localVarCall = createGroupCategoryValidateBeforeCall(groupCategory, null);
        Type localVarReturnType = new TypeToken<CreateGroupCategory200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a group category (asynchronously)
     * Create a new group category
     * @param groupCategory  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createGroupCategoryAsync(GroupCategory groupCategory, final ApiCallback<CreateGroupCategory200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createGroupCategoryValidateBeforeCall(groupCategory, _callback);
        Type localVarReturnType = new TypeToken<CreateGroupCategory200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteGroup
     * @param groupId Id of the group (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteGroupCall(UUID groupId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups/{groupId}"
            .replace("{" + "groupId" + "}", localVarApiClient.escapeString(groupId.toString()));

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
    private okhttp3.Call deleteGroupValidateBeforeCall(UUID groupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupId' is set
        if (groupId == null) {
            throw new ApiException("Missing the required parameter 'groupId' when calling deleteGroup(Async)");
        }

        return deleteGroupCall(groupId, _callback);

    }

    /**
     * Delete a group
     * Update detailed information about a group
     * @param groupId Id of the group (required)
     * @return DeleteGroup200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public DeleteGroup200Response deleteGroup(UUID groupId) throws ApiException {
        ApiResponse<DeleteGroup200Response> localVarResp = deleteGroupWithHttpInfo(groupId);
        return localVarResp.getData();
    }

    /**
     * Delete a group
     * Update detailed information about a group
     * @param groupId Id of the group (required)
     * @return ApiResponse&lt;DeleteGroup200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteGroup200Response> deleteGroupWithHttpInfo(UUID groupId) throws ApiException {
        okhttp3.Call localVarCall = deleteGroupValidateBeforeCall(groupId, null);
        Type localVarReturnType = new TypeToken<DeleteGroup200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a group (asynchronously)
     * Update detailed information about a group
     * @param groupId Id of the group (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteGroupAsync(UUID groupId, final ApiCallback<DeleteGroup200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteGroupValidateBeforeCall(groupId, _callback);
        Type localVarReturnType = new TypeToken<DeleteGroup200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteGroupCategory
     * @param groupCategoryId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteGroupCategoryCall(UUID groupCategoryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups/categories/{groupCategoryId}"
            .replace("{" + "groupCategoryId" + "}", localVarApiClient.escapeString(groupCategoryId.toString()));

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
    private okhttp3.Call deleteGroupCategoryValidateBeforeCall(UUID groupCategoryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupCategoryId' is set
        if (groupCategoryId == null) {
            throw new ApiException("Missing the required parameter 'groupCategoryId' when calling deleteGroupCategory(Async)");
        }

        return deleteGroupCategoryCall(groupCategoryId, _callback);

    }

    /**
     * Delete group category
     * Delete a group category. It must have no child groups and no children categories.
     * @param groupCategoryId  (required)
     * @return DeleteGroupCategory200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public DeleteGroupCategory200Response deleteGroupCategory(UUID groupCategoryId) throws ApiException {
        ApiResponse<DeleteGroupCategory200Response> localVarResp = deleteGroupCategoryWithHttpInfo(groupCategoryId);
        return localVarResp.getData();
    }

    /**
     * Delete group category
     * Delete a group category. It must have no child groups and no children categories.
     * @param groupCategoryId  (required)
     * @return ApiResponse&lt;DeleteGroupCategory200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteGroupCategory200Response> deleteGroupCategoryWithHttpInfo(UUID groupCategoryId) throws ApiException {
        okhttp3.Call localVarCall = deleteGroupCategoryValidateBeforeCall(groupCategoryId, null);
        Type localVarReturnType = new TypeToken<DeleteGroupCategory200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete group category (asynchronously)
     * Delete a group category. It must have no child groups and no children categories.
     * @param groupCategoryId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteGroupCategoryAsync(UUID groupCategoryId, final ApiCallback<DeleteGroupCategory200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteGroupCategoryValidateBeforeCall(groupCategoryId, _callback);
        Type localVarReturnType = new TypeToken<DeleteGroupCategory200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getGroupCategoryDetails
     * @param groupCategoryId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getGroupCategoryDetailsCall(UUID groupCategoryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups/categories/{groupCategoryId}"
            .replace("{" + "groupCategoryId" + "}", localVarApiClient.escapeString(groupCategoryId.toString()));

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
    private okhttp3.Call getGroupCategoryDetailsValidateBeforeCall(UUID groupCategoryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupCategoryId' is set
        if (groupCategoryId == null) {
            throw new ApiException("Missing the required parameter 'groupCategoryId' when calling getGroupCategoryDetails(Async)");
        }

        return getGroupCategoryDetailsCall(groupCategoryId, _callback);

    }

    /**
     * Get group category details
     * Get detailed information about a group category
     * @param groupCategoryId  (required)
     * @return GetGroupCategoryDetails200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public GetGroupCategoryDetails200Response getGroupCategoryDetails(UUID groupCategoryId) throws ApiException {
        ApiResponse<GetGroupCategoryDetails200Response> localVarResp = getGroupCategoryDetailsWithHttpInfo(groupCategoryId);
        return localVarResp.getData();
    }

    /**
     * Get group category details
     * Get detailed information about a group category
     * @param groupCategoryId  (required)
     * @return ApiResponse&lt;GetGroupCategoryDetails200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetGroupCategoryDetails200Response> getGroupCategoryDetailsWithHttpInfo(UUID groupCategoryId) throws ApiException {
        okhttp3.Call localVarCall = getGroupCategoryDetailsValidateBeforeCall(groupCategoryId, null);
        Type localVarReturnType = new TypeToken<GetGroupCategoryDetails200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get group category details (asynchronously)
     * Get detailed information about a group category
     * @param groupCategoryId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getGroupCategoryDetailsAsync(UUID groupCategoryId, final ApiCallback<GetGroupCategoryDetails200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getGroupCategoryDetailsValidateBeforeCall(groupCategoryId, _callback);
        Type localVarReturnType = new TypeToken<GetGroupCategoryDetails200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getGroupTree
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getGroupTreeCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups/tree";

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
    private okhttp3.Call getGroupTreeValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getGroupTreeCall(_callback);

    }

    /**
     * Get groups tree
     * Get all available groups and their categories in a tree
     * @return GetGroupTree200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public GetGroupTree200Response getGroupTree() throws ApiException {
        ApiResponse<GetGroupTree200Response> localVarResp = getGroupTreeWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get groups tree
     * Get all available groups and their categories in a tree
     * @return ApiResponse&lt;GetGroupTree200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetGroupTree200Response> getGroupTreeWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getGroupTreeValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetGroupTree200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get groups tree (asynchronously)
     * Get all available groups and their categories in a tree
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getGroupTreeAsync(final ApiCallback<GetGroupTree200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getGroupTreeValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetGroupTree200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for groupDetails
     * @param groupId Id of the group (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call groupDetailsCall(UUID groupId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups/{groupId}"
            .replace("{" + "groupId" + "}", localVarApiClient.escapeString(groupId.toString()));

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
    private okhttp3.Call groupDetailsValidateBeforeCall(UUID groupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupId' is set
        if (groupId == null) {
            throw new ApiException("Missing the required parameter 'groupId' when calling groupDetails(Async)");
        }

        return groupDetailsCall(groupId, _callback);

    }

    /**
     * Get group details
     * Get detailed information about a group
     * @param groupId Id of the group (required)
     * @return GroupDetails200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public GroupDetails200Response groupDetails(UUID groupId) throws ApiException {
        ApiResponse<GroupDetails200Response> localVarResp = groupDetailsWithHttpInfo(groupId);
        return localVarResp.getData();
    }

    /**
     * Get group details
     * Get detailed information about a group
     * @param groupId Id of the group (required)
     * @return ApiResponse&lt;GroupDetails200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GroupDetails200Response> groupDetailsWithHttpInfo(UUID groupId) throws ApiException {
        okhttp3.Call localVarCall = groupDetailsValidateBeforeCall(groupId, null);
        Type localVarReturnType = new TypeToken<GroupDetails200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get group details (asynchronously)
     * Get detailed information about a group
     * @param groupId Id of the group (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call groupDetailsAsync(UUID groupId, final ApiCallback<GroupDetails200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = groupDetailsValidateBeforeCall(groupId, _callback);
        Type localVarReturnType = new TypeToken<GroupDetails200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listGroups
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listGroupsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups";

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
    private okhttp3.Call listGroupsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listGroupsCall(_callback);

    }

    /**
     * List all groups
     * List all groups
     * @return ListGroups200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ListGroups200Response listGroups() throws ApiException {
        ApiResponse<ListGroups200Response> localVarResp = listGroupsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List all groups
     * List all groups
     * @return ApiResponse&lt;ListGroups200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListGroups200Response> listGroupsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listGroupsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListGroups200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all groups (asynchronously)
     * List all groups
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listGroupsAsync(final ApiCallback<ListGroups200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listGroupsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListGroups200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reloadGroup
     * @param groupId Id of the group (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadGroupCall(UUID groupId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/groups/{groupId}/reload"
            .replace("{" + "groupId" + "}", localVarApiClient.escapeString(groupId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call reloadGroupValidateBeforeCall(UUID groupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupId' is set
        if (groupId == null) {
            throw new ApiException("Missing the required parameter 'groupId' when calling reloadGroup(Async)");
        }

        return reloadGroupCall(groupId, _callback);

    }

    /**
     * Reload a group
     * Recompute the content of a group
     * @param groupId Id of the group (required)
     * @return ReloadGroup200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ReloadGroup200Response reloadGroup(UUID groupId) throws ApiException {
        ApiResponse<ReloadGroup200Response> localVarResp = reloadGroupWithHttpInfo(groupId);
        return localVarResp.getData();
    }

    /**
     * Reload a group
     * Recompute the content of a group
     * @param groupId Id of the group (required)
     * @return ApiResponse&lt;ReloadGroup200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReloadGroup200Response> reloadGroupWithHttpInfo(UUID groupId) throws ApiException {
        okhttp3.Call localVarCall = reloadGroupValidateBeforeCall(groupId, null);
        Type localVarReturnType = new TypeToken<ReloadGroup200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reload a group (asynchronously)
     * Recompute the content of a group
     * @param groupId Id of the group (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadGroupAsync(UUID groupId, final ApiCallback<ReloadGroup200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = reloadGroupValidateBeforeCall(groupId, _callback);
        Type localVarReturnType = new TypeToken<ReloadGroup200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateGroup
     * @param groupId Id of the group (required)
     * @param groupUpdate  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateGroupCall(UUID groupId, GroupUpdate groupUpdate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = groupUpdate;

        // create path and map variables
        String localVarPath = "/groups/{groupId}"
            .replace("{" + "groupId" + "}", localVarApiClient.escapeString(groupId.toString()));

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
    private okhttp3.Call updateGroupValidateBeforeCall(UUID groupId, GroupUpdate groupUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupId' is set
        if (groupId == null) {
            throw new ApiException("Missing the required parameter 'groupId' when calling updateGroup(Async)");
        }

        // verify the required parameter 'groupUpdate' is set
        if (groupUpdate == null) {
            throw new ApiException("Missing the required parameter 'groupUpdate' when calling updateGroup(Async)");
        }

        return updateGroupCall(groupId, groupUpdate, _callback);

    }

    /**
     * Update group details
     * Update detailed information about a group
     * @param groupId Id of the group (required)
     * @param groupUpdate  (required)
     * @return UpdateGroup200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public UpdateGroup200Response updateGroup(UUID groupId, GroupUpdate groupUpdate) throws ApiException {
        ApiResponse<UpdateGroup200Response> localVarResp = updateGroupWithHttpInfo(groupId, groupUpdate);
        return localVarResp.getData();
    }

    /**
     * Update group details
     * Update detailed information about a group
     * @param groupId Id of the group (required)
     * @param groupUpdate  (required)
     * @return ApiResponse&lt;UpdateGroup200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateGroup200Response> updateGroupWithHttpInfo(UUID groupId, GroupUpdate groupUpdate) throws ApiException {
        okhttp3.Call localVarCall = updateGroupValidateBeforeCall(groupId, groupUpdate, null);
        Type localVarReturnType = new TypeToken<UpdateGroup200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update group details (asynchronously)
     * Update detailed information about a group
     * @param groupId Id of the group (required)
     * @param groupUpdate  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateGroupAsync(UUID groupId, GroupUpdate groupUpdate, final ApiCallback<UpdateGroup200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateGroupValidateBeforeCall(groupId, groupUpdate, _callback);
        Type localVarReturnType = new TypeToken<UpdateGroup200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateGroupCategory
     * @param groupCategoryId  (required)
     * @param groupCategoryUpdate  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateGroupCategoryCall(UUID groupCategoryId, GroupCategoryUpdate groupCategoryUpdate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = groupCategoryUpdate;

        // create path and map variables
        String localVarPath = "/groups/categories/{groupCategoryId}"
            .replace("{" + "groupCategoryId" + "}", localVarApiClient.escapeString(groupCategoryId.toString()));

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
    private okhttp3.Call updateGroupCategoryValidateBeforeCall(UUID groupCategoryId, GroupCategoryUpdate groupCategoryUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'groupCategoryId' is set
        if (groupCategoryId == null) {
            throw new ApiException("Missing the required parameter 'groupCategoryId' when calling updateGroupCategory(Async)");
        }

        // verify the required parameter 'groupCategoryUpdate' is set
        if (groupCategoryUpdate == null) {
            throw new ApiException("Missing the required parameter 'groupCategoryUpdate' when calling updateGroupCategory(Async)");
        }

        return updateGroupCategoryCall(groupCategoryId, groupCategoryUpdate, _callback);

    }

    /**
     * Update group category details
     * Update detailed information about a group category
     * @param groupCategoryId  (required)
     * @param groupCategoryUpdate  (required)
     * @return UpdateGroupCategory200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public UpdateGroupCategory200Response updateGroupCategory(UUID groupCategoryId, GroupCategoryUpdate groupCategoryUpdate) throws ApiException {
        ApiResponse<UpdateGroupCategory200Response> localVarResp = updateGroupCategoryWithHttpInfo(groupCategoryId, groupCategoryUpdate);
        return localVarResp.getData();
    }

    /**
     * Update group category details
     * Update detailed information about a group category
     * @param groupCategoryId  (required)
     * @param groupCategoryUpdate  (required)
     * @return ApiResponse&lt;UpdateGroupCategory200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateGroupCategory200Response> updateGroupCategoryWithHttpInfo(UUID groupCategoryId, GroupCategoryUpdate groupCategoryUpdate) throws ApiException {
        okhttp3.Call localVarCall = updateGroupCategoryValidateBeforeCall(groupCategoryId, groupCategoryUpdate, null);
        Type localVarReturnType = new TypeToken<UpdateGroupCategory200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update group category details (asynchronously)
     * Update detailed information about a group category
     * @param groupCategoryId  (required)
     * @param groupCategoryUpdate  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateGroupCategoryAsync(UUID groupCategoryId, GroupCategoryUpdate groupCategoryUpdate, final ApiCallback<UpdateGroupCategory200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateGroupCategoryValidateBeforeCall(groupCategoryId, groupCategoryUpdate, _callback);
        Type localVarReturnType = new TypeToken<UpdateGroupCategory200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
