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


import org.openapitools.client.model.CheckCVE200Response;
import org.openapitools.client.model.GetAllCve200Response;
import org.openapitools.client.model.GetCVECheckConfiguration200Response;
import org.openapitools.client.model.GetCVEList200Response;
import org.openapitools.client.model.GetCVEListRequest;
import org.openapitools.client.model.GetCve200Response;
import org.openapitools.client.model.GetLastCVECheck200Response;
import org.openapitools.client.model.ReadCVEfromFS200Response;
import java.util.UUID;
import org.openapitools.client.model.UpdateCVE200Response;
import org.openapitools.client.model.UpdateCVECheckConfiguration200Response;
import org.openapitools.client.model.UpdateCVECheckConfigurationRequest;
import org.openapitools.client.model.UpdateCVERequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CveApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CveApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CveApi(ApiClient apiClient) {
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
     * Build call for checkCVE
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check result </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call checkCVECall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cve/check";

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
    private okhttp3.Call checkCVEValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return checkCVECall(_callback);

    }

    /**
     * Trigger a CVE check
     * Trigger a CVE check
     * @return CheckCVE200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check result </td><td>  -  </td></tr>
     </table>
     */
    public CheckCVE200Response checkCVE() throws ApiException {
        ApiResponse<CheckCVE200Response> localVarResp = checkCVEWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Trigger a CVE check
     * Trigger a CVE check
     * @return ApiResponse&lt;CheckCVE200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check result </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CheckCVE200Response> checkCVEWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = checkCVEValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<CheckCVE200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Trigger a CVE check (asynchronously)
     * Trigger a CVE check
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check result </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call checkCVEAsync(final ApiCallback<CheckCVE200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = checkCVEValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<CheckCVE200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllCve
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllCveCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cve";

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
    private okhttp3.Call getAllCveValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getAllCveCall(_callback);

    }

    /**
     * Get all CVE details
     * Get all CVE details
     * @return GetAllCve200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public GetAllCve200Response getAllCve() throws ApiException {
        ApiResponse<GetAllCve200Response> localVarResp = getAllCveWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get all CVE details
     * Get all CVE details
     * @return ApiResponse&lt;GetAllCve200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAllCve200Response> getAllCveWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getAllCveValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetAllCve200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get all CVE details (asynchronously)
     * Get all CVE details
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllCveAsync(final ApiCallback<GetAllCve200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllCveValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetAllCve200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCVECheckConfiguration
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCVECheckConfigurationCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cve/check/config";

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
    private okhttp3.Call getCVECheckConfigurationValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getCVECheckConfigurationCall(_callback);

    }

    /**
     * Get CVE check config
     * Get CVE check config
     * @return GetCVECheckConfiguration200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public GetCVECheckConfiguration200Response getCVECheckConfiguration() throws ApiException {
        ApiResponse<GetCVECheckConfiguration200Response> localVarResp = getCVECheckConfigurationWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get CVE check config
     * Get CVE check config
     * @return ApiResponse&lt;GetCVECheckConfiguration200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetCVECheckConfiguration200Response> getCVECheckConfigurationWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getCVECheckConfigurationValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetCVECheckConfiguration200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get CVE check config (asynchronously)
     * Get CVE check config
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCVECheckConfigurationAsync(final ApiCallback<GetCVECheckConfiguration200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCVECheckConfigurationValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetCVECheckConfiguration200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCVEList
     * @param getCVEListRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE list </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCVEListCall(GetCVEListRequest getCVEListRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = getCVEListRequest;

        // create path and map variables
        String localVarPath = "/cve/list";

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
    private okhttp3.Call getCVEListValidateBeforeCall(GetCVEListRequest getCVEListRequest, final ApiCallback _callback) throws ApiException {
        return getCVEListCall(getCVEListRequest, _callback);

    }

    /**
     * Get a list of CVE details
     * Get CVE details, from a list passed as parameter
     * @param getCVEListRequest  (optional)
     * @return GetCVEList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE list </td><td>  -  </td></tr>
     </table>
     */
    public GetCVEList200Response getCVEList(GetCVEListRequest getCVEListRequest) throws ApiException {
        ApiResponse<GetCVEList200Response> localVarResp = getCVEListWithHttpInfo(getCVEListRequest);
        return localVarResp.getData();
    }

    /**
     * Get a list of CVE details
     * Get CVE details, from a list passed as parameter
     * @param getCVEListRequest  (optional)
     * @return ApiResponse&lt;GetCVEList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE list </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetCVEList200Response> getCVEListWithHttpInfo(GetCVEListRequest getCVEListRequest) throws ApiException {
        okhttp3.Call localVarCall = getCVEListValidateBeforeCall(getCVEListRequest, null);
        Type localVarReturnType = new TypeToken<GetCVEList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of CVE details (asynchronously)
     * Get CVE details, from a list passed as parameter
     * @param getCVEListRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE list </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCVEListAsync(GetCVEListRequest getCVEListRequest, final ApiCallback<GetCVEList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCVEListValidateBeforeCall(getCVEListRequest, _callback);
        Type localVarReturnType = new TypeToken<GetCVEList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCve
     * @param cveId Id of the CVE (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCveCall(UUID cveId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cve/{cveId}"
            .replace("{" + "cveId" + "}", localVarApiClient.escapeString(cveId.toString()));

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
    private okhttp3.Call getCveValidateBeforeCall(UUID cveId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'cveId' is set
        if (cveId == null) {
            throw new ApiException("Missing the required parameter 'cveId' when calling getCve(Async)");
        }

        return getCveCall(cveId, _callback);

    }

    /**
     * Get a CVE details
     * Get a CVE details
     * @param cveId Id of the CVE (required)
     * @return GetCve200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public GetCve200Response getCve(UUID cveId) throws ApiException {
        ApiResponse<GetCve200Response> localVarResp = getCveWithHttpInfo(cveId);
        return localVarResp.getData();
    }

    /**
     * Get a CVE details
     * Get a CVE details
     * @param cveId Id of the CVE (required)
     * @return ApiResponse&lt;GetCve200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetCve200Response> getCveWithHttpInfo(UUID cveId) throws ApiException {
        okhttp3.Call localVarCall = getCveValidateBeforeCall(cveId, null);
        Type localVarReturnType = new TypeToken<GetCve200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a CVE details (asynchronously)
     * Get a CVE details
     * @param cveId Id of the CVE (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> CVE details result </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCveAsync(UUID cveId, final ApiCallback<GetCve200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCveValidateBeforeCall(cveId, _callback);
        Type localVarReturnType = new TypeToken<GetCve200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLastCVECheck
     * @param groupId Id of node groups you want to get from last CVE check (optional)
     * @param nodeId Id of nodes you want to get from last CVE check (optional)
     * @param cveId Id of CVE you want to get from last CVE check (optional)
     * @param _package Name of packages you want to get from last CVE check (optional)
     * @param severity Severity of the CVE you want to get from last CVE check (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Last CVE check </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLastCVECheckCall(String groupId, String nodeId, String cveId, String _package, String severity, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cve/check/last";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (groupId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("groupId", groupId));
        }

        if (nodeId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nodeId", nodeId));
        }

        if (cveId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cveId", cveId));
        }

        if (_package != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("package", _package));
        }

        if (severity != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("severity", severity));
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

        String[] localVarAuthNames = new String[] { "API-Tokens" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getLastCVECheckValidateBeforeCall(String groupId, String nodeId, String cveId, String _package, String severity, final ApiCallback _callback) throws ApiException {
        return getLastCVECheckCall(groupId, nodeId, cveId, _package, severity, _callback);

    }

    /**
     * Get last CVE check result
     * Get last CVE check result
     * @param groupId Id of node groups you want to get from last CVE check (optional)
     * @param nodeId Id of nodes you want to get from last CVE check (optional)
     * @param cveId Id of CVE you want to get from last CVE check (optional)
     * @param _package Name of packages you want to get from last CVE check (optional)
     * @param severity Severity of the CVE you want to get from last CVE check (optional)
     * @return GetLastCVECheck200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Last CVE check </td><td>  -  </td></tr>
     </table>
     */
    public GetLastCVECheck200Response getLastCVECheck(String groupId, String nodeId, String cveId, String _package, String severity) throws ApiException {
        ApiResponse<GetLastCVECheck200Response> localVarResp = getLastCVECheckWithHttpInfo(groupId, nodeId, cveId, _package, severity);
        return localVarResp.getData();
    }

    /**
     * Get last CVE check result
     * Get last CVE check result
     * @param groupId Id of node groups you want to get from last CVE check (optional)
     * @param nodeId Id of nodes you want to get from last CVE check (optional)
     * @param cveId Id of CVE you want to get from last CVE check (optional)
     * @param _package Name of packages you want to get from last CVE check (optional)
     * @param severity Severity of the CVE you want to get from last CVE check (optional)
     * @return ApiResponse&lt;GetLastCVECheck200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Last CVE check </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLastCVECheck200Response> getLastCVECheckWithHttpInfo(String groupId, String nodeId, String cveId, String _package, String severity) throws ApiException {
        okhttp3.Call localVarCall = getLastCVECheckValidateBeforeCall(groupId, nodeId, cveId, _package, severity, null);
        Type localVarReturnType = new TypeToken<GetLastCVECheck200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get last CVE check result (asynchronously)
     * Get last CVE check result
     * @param groupId Id of node groups you want to get from last CVE check (optional)
     * @param nodeId Id of nodes you want to get from last CVE check (optional)
     * @param cveId Id of CVE you want to get from last CVE check (optional)
     * @param _package Name of packages you want to get from last CVE check (optional)
     * @param severity Severity of the CVE you want to get from last CVE check (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Last CVE check </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLastCVECheckAsync(String groupId, String nodeId, String cveId, String _package, String severity, final ApiCallback<GetLastCVECheck200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLastCVECheckValidateBeforeCall(groupId, nodeId, cveId, _package, severity, _callback);
        Type localVarReturnType = new TypeToken<GetLastCVECheck200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for readCVEfromFS
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call readCVEfromFSCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cve/update/fs";

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
    private okhttp3.Call readCVEfromFSValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return readCVEfromFSCall(_callback);

    }

    /**
     * Update CVE database from file system
     * Update CVE database from file system
     * @return ReadCVEfromFS200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public ReadCVEfromFS200Response readCVEfromFS() throws ApiException {
        ApiResponse<ReadCVEfromFS200Response> localVarResp = readCVEfromFSWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Update CVE database from file system
     * Update CVE database from file system
     * @return ApiResponse&lt;ReadCVEfromFS200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReadCVEfromFS200Response> readCVEfromFSWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = readCVEfromFSValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ReadCVEfromFS200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update CVE database from file system (asynchronously)
     * Update CVE database from file system
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call readCVEfromFSAsync(final ApiCallback<ReadCVEfromFS200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = readCVEfromFSValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ReadCVEfromFS200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateCVE
     * @param updateCVERequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateCVECall(UpdateCVERequest updateCVERequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateCVERequest;

        // create path and map variables
        String localVarPath = "/cve/update";

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
    private okhttp3.Call updateCVEValidateBeforeCall(UpdateCVERequest updateCVERequest, final ApiCallback _callback) throws ApiException {
        return updateCVECall(updateCVERequest, _callback);

    }

    /**
     * Update CVE database from remote source
     * Update CVE database from remote source
     * @param updateCVERequest  (optional)
     * @return UpdateCVE200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public UpdateCVE200Response updateCVE(UpdateCVERequest updateCVERequest) throws ApiException {
        ApiResponse<UpdateCVE200Response> localVarResp = updateCVEWithHttpInfo(updateCVERequest);
        return localVarResp.getData();
    }

    /**
     * Update CVE database from remote source
     * Update CVE database from remote source
     * @param updateCVERequest  (optional)
     * @return ApiResponse&lt;UpdateCVE200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateCVE200Response> updateCVEWithHttpInfo(UpdateCVERequest updateCVERequest) throws ApiException {
        okhttp3.Call localVarCall = updateCVEValidateBeforeCall(updateCVERequest, null);
        Type localVarReturnType = new TypeToken<UpdateCVE200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update CVE database from remote source (asynchronously)
     * Update CVE database from remote source
     * @param updateCVERequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> updated CVE count </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateCVEAsync(UpdateCVERequest updateCVERequest, final ApiCallback<UpdateCVE200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateCVEValidateBeforeCall(updateCVERequest, _callback);
        Type localVarReturnType = new TypeToken<UpdateCVE200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateCVECheckConfiguration
     * @param updateCVECheckConfigurationRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> new CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateCVECheckConfigurationCall(UpdateCVECheckConfigurationRequest updateCVECheckConfigurationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateCVECheckConfigurationRequest;

        // create path and map variables
        String localVarPath = "/cve/check/config";

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
    private okhttp3.Call updateCVECheckConfigurationValidateBeforeCall(UpdateCVECheckConfigurationRequest updateCVECheckConfigurationRequest, final ApiCallback _callback) throws ApiException {
        return updateCVECheckConfigurationCall(updateCVECheckConfigurationRequest, _callback);

    }

    /**
     * Update cve check config
     * Update cve check config
     * @param updateCVECheckConfigurationRequest  (optional)
     * @return UpdateCVECheckConfiguration200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> new CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public UpdateCVECheckConfiguration200Response updateCVECheckConfiguration(UpdateCVECheckConfigurationRequest updateCVECheckConfigurationRequest) throws ApiException {
        ApiResponse<UpdateCVECheckConfiguration200Response> localVarResp = updateCVECheckConfigurationWithHttpInfo(updateCVECheckConfigurationRequest);
        return localVarResp.getData();
    }

    /**
     * Update cve check config
     * Update cve check config
     * @param updateCVECheckConfigurationRequest  (optional)
     * @return ApiResponse&lt;UpdateCVECheckConfiguration200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> new CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateCVECheckConfiguration200Response> updateCVECheckConfigurationWithHttpInfo(UpdateCVECheckConfigurationRequest updateCVECheckConfigurationRequest) throws ApiException {
        okhttp3.Call localVarCall = updateCVECheckConfigurationValidateBeforeCall(updateCVECheckConfigurationRequest, null);
        Type localVarReturnType = new TypeToken<UpdateCVECheckConfiguration200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update cve check config (asynchronously)
     * Update cve check config
     * @param updateCVECheckConfigurationRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> new CVE check config </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateCVECheckConfigurationAsync(UpdateCVECheckConfigurationRequest updateCVECheckConfigurationRequest, final ApiCallback<UpdateCVECheckConfiguration200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateCVECheckConfigurationValidateBeforeCall(updateCVECheckConfigurationRequest, _callback);
        Type localVarReturnType = new TypeToken<UpdateCVECheckConfiguration200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
