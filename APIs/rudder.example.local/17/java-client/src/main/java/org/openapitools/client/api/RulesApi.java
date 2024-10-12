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


import org.openapitools.client.model.CreateRule200Response;
import org.openapitools.client.model.CreateRuleCategory200Response;
import org.openapitools.client.model.DeleteRule200Response;
import org.openapitools.client.model.DeleteRuleCategory200Response;
import org.openapitools.client.model.GetRuleCategoryDetails200Response;
import org.openapitools.client.model.GetRuleTree200Response;
import org.openapitools.client.model.ListRules200Response;
import org.openapitools.client.model.RuleCategory;
import org.openapitools.client.model.RuleCategoryUpdate;
import org.openapitools.client.model.RuleDetails200Response;
import org.openapitools.client.model.RuleNew;
import org.openapitools.client.model.RuleWithCategory;
import java.util.UUID;
import org.openapitools.client.model.UpdateRule200Response;
import org.openapitools.client.model.UpdateRuleCategory200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RulesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RulesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RulesApi(ApiClient apiClient) {
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
     * Build call for createRule
     * @param ruleNew  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRuleCall(RuleNew ruleNew, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ruleNew;

        // create path and map variables
        String localVarPath = "/rules";

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
    private okhttp3.Call createRuleValidateBeforeCall(RuleNew ruleNew, final ApiCallback _callback) throws ApiException {
        return createRuleCall(ruleNew, _callback);

    }

    /**
     * Create a rule
     * Create a new rule. You can specify a source rule to clone it.
     * @param ruleNew  (optional)
     * @return CreateRule200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public CreateRule200Response createRule(RuleNew ruleNew) throws ApiException {
        ApiResponse<CreateRule200Response> localVarResp = createRuleWithHttpInfo(ruleNew);
        return localVarResp.getData();
    }

    /**
     * Create a rule
     * Create a new rule. You can specify a source rule to clone it.
     * @param ruleNew  (optional)
     * @return ApiResponse&lt;CreateRule200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateRule200Response> createRuleWithHttpInfo(RuleNew ruleNew) throws ApiException {
        okhttp3.Call localVarCall = createRuleValidateBeforeCall(ruleNew, null);
        Type localVarReturnType = new TypeToken<CreateRule200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a rule (asynchronously)
     * Create a new rule. You can specify a source rule to clone it.
     * @param ruleNew  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRuleAsync(RuleNew ruleNew, final ApiCallback<CreateRule200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createRuleValidateBeforeCall(ruleNew, _callback);
        Type localVarReturnType = new TypeToken<CreateRule200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createRuleCategory
     * @param ruleCategory  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRuleCategoryCall(RuleCategory ruleCategory, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ruleCategory;

        // create path and map variables
        String localVarPath = "/rules/categories";

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
    private okhttp3.Call createRuleCategoryValidateBeforeCall(RuleCategory ruleCategory, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleCategory' is set
        if (ruleCategory == null) {
            throw new ApiException("Missing the required parameter 'ruleCategory' when calling createRuleCategory(Async)");
        }

        return createRuleCategoryCall(ruleCategory, _callback);

    }

    /**
     * Create a rule category
     * Create a new rule category
     * @param ruleCategory  (required)
     * @return CreateRuleCategory200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public CreateRuleCategory200Response createRuleCategory(RuleCategory ruleCategory) throws ApiException {
        ApiResponse<CreateRuleCategory200Response> localVarResp = createRuleCategoryWithHttpInfo(ruleCategory);
        return localVarResp.getData();
    }

    /**
     * Create a rule category
     * Create a new rule category
     * @param ruleCategory  (required)
     * @return ApiResponse&lt;CreateRuleCategory200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateRuleCategory200Response> createRuleCategoryWithHttpInfo(RuleCategory ruleCategory) throws ApiException {
        okhttp3.Call localVarCall = createRuleCategoryValidateBeforeCall(ruleCategory, null);
        Type localVarReturnType = new TypeToken<CreateRuleCategory200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a rule category (asynchronously)
     * Create a new rule category
     * @param ruleCategory  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRuleCategoryAsync(RuleCategory ruleCategory, final ApiCallback<CreateRuleCategory200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createRuleCategoryValidateBeforeCall(ruleCategory, _callback);
        Type localVarReturnType = new TypeToken<CreateRuleCategory200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRule
     * @param ruleId Id of the target rule (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRuleCall(UUID ruleId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/rules/{ruleId}"
            .replace("{" + "ruleId" + "}", localVarApiClient.escapeString(ruleId.toString()));

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
    private okhttp3.Call deleteRuleValidateBeforeCall(UUID ruleId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleId' is set
        if (ruleId == null) {
            throw new ApiException("Missing the required parameter 'ruleId' when calling deleteRule(Async)");
        }

        return deleteRuleCall(ruleId, _callback);

    }

    /**
     * Delete a rule
     * Delete a rule.
     * @param ruleId Id of the target rule (required)
     * @return DeleteRule200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public DeleteRule200Response deleteRule(UUID ruleId) throws ApiException {
        ApiResponse<DeleteRule200Response> localVarResp = deleteRuleWithHttpInfo(ruleId);
        return localVarResp.getData();
    }

    /**
     * Delete a rule
     * Delete a rule.
     * @param ruleId Id of the target rule (required)
     * @return ApiResponse&lt;DeleteRule200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteRule200Response> deleteRuleWithHttpInfo(UUID ruleId) throws ApiException {
        okhttp3.Call localVarCall = deleteRuleValidateBeforeCall(ruleId, null);
        Type localVarReturnType = new TypeToken<DeleteRule200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a rule (asynchronously)
     * Delete a rule.
     * @param ruleId Id of the target rule (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRuleAsync(UUID ruleId, final ApiCallback<DeleteRule200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRuleValidateBeforeCall(ruleId, _callback);
        Type localVarReturnType = new TypeToken<DeleteRule200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRuleCategory
     * @param ruleCategoryId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRuleCategoryCall(UUID ruleCategoryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/rules/categories/{ruleCategoryId}"
            .replace("{" + "ruleCategoryId" + "}", localVarApiClient.escapeString(ruleCategoryId.toString()));

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
    private okhttp3.Call deleteRuleCategoryValidateBeforeCall(UUID ruleCategoryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleCategoryId' is set
        if (ruleCategoryId == null) {
            throw new ApiException("Missing the required parameter 'ruleCategoryId' when calling deleteRuleCategory(Async)");
        }

        return deleteRuleCategoryCall(ruleCategoryId, _callback);

    }

    /**
     * Delete group category
     * Delete a group category. It must have no child groups and no children categories.
     * @param ruleCategoryId  (required)
     * @return DeleteRuleCategory200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public DeleteRuleCategory200Response deleteRuleCategory(UUID ruleCategoryId) throws ApiException {
        ApiResponse<DeleteRuleCategory200Response> localVarResp = deleteRuleCategoryWithHttpInfo(ruleCategoryId);
        return localVarResp.getData();
    }

    /**
     * Delete group category
     * Delete a group category. It must have no child groups and no children categories.
     * @param ruleCategoryId  (required)
     * @return ApiResponse&lt;DeleteRuleCategory200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteRuleCategory200Response> deleteRuleCategoryWithHttpInfo(UUID ruleCategoryId) throws ApiException {
        okhttp3.Call localVarCall = deleteRuleCategoryValidateBeforeCall(ruleCategoryId, null);
        Type localVarReturnType = new TypeToken<DeleteRuleCategory200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete group category (asynchronously)
     * Delete a group category. It must have no child groups and no children categories.
     * @param ruleCategoryId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Groups category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRuleCategoryAsync(UUID ruleCategoryId, final ApiCallback<DeleteRuleCategory200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRuleCategoryValidateBeforeCall(ruleCategoryId, _callback);
        Type localVarReturnType = new TypeToken<DeleteRuleCategory200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRuleCategoryDetails
     * @param ruleCategoryId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRuleCategoryDetailsCall(UUID ruleCategoryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/rules/categories/{ruleCategoryId}"
            .replace("{" + "ruleCategoryId" + "}", localVarApiClient.escapeString(ruleCategoryId.toString()));

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
    private okhttp3.Call getRuleCategoryDetailsValidateBeforeCall(UUID ruleCategoryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleCategoryId' is set
        if (ruleCategoryId == null) {
            throw new ApiException("Missing the required parameter 'ruleCategoryId' when calling getRuleCategoryDetails(Async)");
        }

        return getRuleCategoryDetailsCall(ruleCategoryId, _callback);

    }

    /**
     * Get rule category details
     * Get detailed information about a rule category
     * @param ruleCategoryId  (required)
     * @return GetRuleCategoryDetails200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public GetRuleCategoryDetails200Response getRuleCategoryDetails(UUID ruleCategoryId) throws ApiException {
        ApiResponse<GetRuleCategoryDetails200Response> localVarResp = getRuleCategoryDetailsWithHttpInfo(ruleCategoryId);
        return localVarResp.getData();
    }

    /**
     * Get rule category details
     * Get detailed information about a rule category
     * @param ruleCategoryId  (required)
     * @return ApiResponse&lt;GetRuleCategoryDetails200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRuleCategoryDetails200Response> getRuleCategoryDetailsWithHttpInfo(UUID ruleCategoryId) throws ApiException {
        okhttp3.Call localVarCall = getRuleCategoryDetailsValidateBeforeCall(ruleCategoryId, null);
        Type localVarReturnType = new TypeToken<GetRuleCategoryDetails200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get rule category details (asynchronously)
     * Get detailed information about a rule category
     * @param ruleCategoryId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRuleCategoryDetailsAsync(UUID ruleCategoryId, final ApiCallback<GetRuleCategoryDetails200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRuleCategoryDetailsValidateBeforeCall(ruleCategoryId, _callback);
        Type localVarReturnType = new TypeToken<GetRuleCategoryDetails200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRuleTree
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRuleTreeCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/rules/tree";

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
    private okhttp3.Call getRuleTreeValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getRuleTreeCall(_callback);

    }

    /**
     * Get rules tree
     * Get all available rules and their categories in a tree
     * @return GetRuleTree200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public GetRuleTree200Response getRuleTree() throws ApiException {
        ApiResponse<GetRuleTree200Response> localVarResp = getRuleTreeWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get rules tree
     * Get all available rules and their categories in a tree
     * @return ApiResponse&lt;GetRuleTree200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRuleTree200Response> getRuleTreeWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getRuleTreeValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetRuleTree200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get rules tree (asynchronously)
     * Get all available rules and their categories in a tree
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRuleTreeAsync(final ApiCallback<GetRuleTree200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRuleTreeValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetRuleTree200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listRules
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRulesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/rules";

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
    private okhttp3.Call listRulesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listRulesCall(_callback);

    }

    /**
     * List all rules
     * List all rules
     * @return ListRules200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ListRules200Response listRules() throws ApiException {
        ApiResponse<ListRules200Response> localVarResp = listRulesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List all rules
     * List all rules
     * @return ApiResponse&lt;ListRules200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListRules200Response> listRulesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listRulesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListRules200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all rules (asynchronously)
     * List all rules
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRulesAsync(final ApiCallback<ListRules200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listRulesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListRules200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for ruleDetails
     * @param ruleId Id of the target rule (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call ruleDetailsCall(UUID ruleId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/rules/{ruleId}"
            .replace("{" + "ruleId" + "}", localVarApiClient.escapeString(ruleId.toString()));

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
    private okhttp3.Call ruleDetailsValidateBeforeCall(UUID ruleId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleId' is set
        if (ruleId == null) {
            throw new ApiException("Missing the required parameter 'ruleId' when calling ruleDetails(Async)");
        }

        return ruleDetailsCall(ruleId, _callback);

    }

    /**
     * Get a rule details
     * Get the details of a rule
     * @param ruleId Id of the target rule (required)
     * @return RuleDetails200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public RuleDetails200Response ruleDetails(UUID ruleId) throws ApiException {
        ApiResponse<RuleDetails200Response> localVarResp = ruleDetailsWithHttpInfo(ruleId);
        return localVarResp.getData();
    }

    /**
     * Get a rule details
     * Get the details of a rule
     * @param ruleId Id of the target rule (required)
     * @return ApiResponse&lt;RuleDetails200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<RuleDetails200Response> ruleDetailsWithHttpInfo(UUID ruleId) throws ApiException {
        okhttp3.Call localVarCall = ruleDetailsValidateBeforeCall(ruleId, null);
        Type localVarReturnType = new TypeToken<RuleDetails200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a rule details (asynchronously)
     * Get the details of a rule
     * @param ruleId Id of the target rule (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call ruleDetailsAsync(UUID ruleId, final ApiCallback<RuleDetails200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = ruleDetailsValidateBeforeCall(ruleId, _callback);
        Type localVarReturnType = new TypeToken<RuleDetails200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateRule
     * @param ruleId Id of the target rule (required)
     * @param ruleWithCategory  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRuleCall(UUID ruleId, RuleWithCategory ruleWithCategory, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ruleWithCategory;

        // create path and map variables
        String localVarPath = "/rules/{ruleId}"
            .replace("{" + "ruleId" + "}", localVarApiClient.escapeString(ruleId.toString()));

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
    private okhttp3.Call updateRuleValidateBeforeCall(UUID ruleId, RuleWithCategory ruleWithCategory, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleId' is set
        if (ruleId == null) {
            throw new ApiException("Missing the required parameter 'ruleId' when calling updateRule(Async)");
        }

        // verify the required parameter 'ruleWithCategory' is set
        if (ruleWithCategory == null) {
            throw new ApiException("Missing the required parameter 'ruleWithCategory' when calling updateRule(Async)");
        }

        return updateRuleCall(ruleId, ruleWithCategory, _callback);

    }

    /**
     * Update a rule details
     * Update the details of a rule
     * @param ruleId Id of the target rule (required)
     * @param ruleWithCategory  (required)
     * @return UpdateRule200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public UpdateRule200Response updateRule(UUID ruleId, RuleWithCategory ruleWithCategory) throws ApiException {
        ApiResponse<UpdateRule200Response> localVarResp = updateRuleWithHttpInfo(ruleId, ruleWithCategory);
        return localVarResp.getData();
    }

    /**
     * Update a rule details
     * Update the details of a rule
     * @param ruleId Id of the target rule (required)
     * @param ruleWithCategory  (required)
     * @return ApiResponse&lt;UpdateRule200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateRule200Response> updateRuleWithHttpInfo(UUID ruleId, RuleWithCategory ruleWithCategory) throws ApiException {
        okhttp3.Call localVarCall = updateRuleValidateBeforeCall(ruleId, ruleWithCategory, null);
        Type localVarReturnType = new TypeToken<UpdateRule200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a rule details (asynchronously)
     * Update the details of a rule
     * @param ruleId Id of the target rule (required)
     * @param ruleWithCategory  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRuleAsync(UUID ruleId, RuleWithCategory ruleWithCategory, final ApiCallback<UpdateRule200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateRuleValidateBeforeCall(ruleId, ruleWithCategory, _callback);
        Type localVarReturnType = new TypeToken<UpdateRule200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateRuleCategory
     * @param ruleCategoryId  (required)
     * @param ruleCategoryUpdate  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRuleCategoryCall(UUID ruleCategoryId, RuleCategoryUpdate ruleCategoryUpdate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ruleCategoryUpdate;

        // create path and map variables
        String localVarPath = "/rules/categories/{ruleCategoryId}"
            .replace("{" + "ruleCategoryId" + "}", localVarApiClient.escapeString(ruleCategoryId.toString()));

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
    private okhttp3.Call updateRuleCategoryValidateBeforeCall(UUID ruleCategoryId, RuleCategoryUpdate ruleCategoryUpdate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ruleCategoryId' is set
        if (ruleCategoryId == null) {
            throw new ApiException("Missing the required parameter 'ruleCategoryId' when calling updateRuleCategory(Async)");
        }

        // verify the required parameter 'ruleCategoryUpdate' is set
        if (ruleCategoryUpdate == null) {
            throw new ApiException("Missing the required parameter 'ruleCategoryUpdate' when calling updateRuleCategory(Async)");
        }

        return updateRuleCategoryCall(ruleCategoryId, ruleCategoryUpdate, _callback);

    }

    /**
     * Update rule category details
     * Update detailed information about a rule category
     * @param ruleCategoryId  (required)
     * @param ruleCategoryUpdate  (required)
     * @return UpdateRuleCategory200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public UpdateRuleCategory200Response updateRuleCategory(UUID ruleCategoryId, RuleCategoryUpdate ruleCategoryUpdate) throws ApiException {
        ApiResponse<UpdateRuleCategory200Response> localVarResp = updateRuleCategoryWithHttpInfo(ruleCategoryId, ruleCategoryUpdate);
        return localVarResp.getData();
    }

    /**
     * Update rule category details
     * Update detailed information about a rule category
     * @param ruleCategoryId  (required)
     * @param ruleCategoryUpdate  (required)
     * @return ApiResponse&lt;UpdateRuleCategory200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateRuleCategory200Response> updateRuleCategoryWithHttpInfo(UUID ruleCategoryId, RuleCategoryUpdate ruleCategoryUpdate) throws ApiException {
        okhttp3.Call localVarCall = updateRuleCategoryValidateBeforeCall(ruleCategoryId, ruleCategoryUpdate, null);
        Type localVarReturnType = new TypeToken<UpdateRuleCategory200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update rule category details (asynchronously)
     * Update detailed information about a rule category
     * @param ruleCategoryId  (required)
     * @param ruleCategoryUpdate  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Rules category information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRuleCategoryAsync(UUID ruleCategoryId, RuleCategoryUpdate ruleCategoryUpdate, final ApiCallback<UpdateRuleCategory200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateRuleCategoryValidateBeforeCall(ruleCategoryId, ruleCategoryUpdate, _callback);
        Type localVarReturnType = new TypeToken<UpdateRuleCategory200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
