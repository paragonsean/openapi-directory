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


import org.openapitools.client.model.CreateTechnique200Response;
import org.openapitools.client.model.DeleteTechnique200Response;
import org.openapitools.client.model.EditorTechnique;
import org.openapitools.client.model.GetTechniqueAllVersion200Response;
import org.openapitools.client.model.GetTechniquesResources200Response;
import org.openapitools.client.model.ListTechniqueVersionDirectives200Response;
import org.openapitools.client.model.ListTechniques200Response;
import org.openapitools.client.model.ListTechniquesDirectives200Response;
import org.openapitools.client.model.ListTechniquesVersions200Response;
import org.openapitools.client.model.Methods200Response;
import org.openapitools.client.model.TechniqueCategories200Response;
import org.openapitools.client.model.TechniqueRevisions200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TechniquesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TechniquesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TechniquesApi(ApiClient apiClient) {
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
     * Build call for createTechnique
     * @param editorTechnique  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createTechniqueCall(List<EditorTechnique> editorTechnique, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = editorTechnique;

        // create path and map variables
        String localVarPath = "/techniques";

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
    private okhttp3.Call createTechniqueValidateBeforeCall(List<EditorTechnique> editorTechnique, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'editorTechnique' is set
        if (editorTechnique == null) {
            throw new ApiException("Missing the required parameter 'editorTechnique' when calling createTechnique(Async)");
        }

        return createTechniqueCall(editorTechnique, _callback);

    }

    /**
     * Create technique
     * Create a new technique in Rudder from a technique in the technique editor
     * @param editorTechnique  (required)
     * @return CreateTechnique200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public CreateTechnique200Response createTechnique(List<EditorTechnique> editorTechnique) throws ApiException {
        ApiResponse<CreateTechnique200Response> localVarResp = createTechniqueWithHttpInfo(editorTechnique);
        return localVarResp.getData();
    }

    /**
     * Create technique
     * Create a new technique in Rudder from a technique in the technique editor
     * @param editorTechnique  (required)
     * @return ApiResponse&lt;CreateTechnique200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateTechnique200Response> createTechniqueWithHttpInfo(List<EditorTechnique> editorTechnique) throws ApiException {
        okhttp3.Call localVarCall = createTechniqueValidateBeforeCall(editorTechnique, null);
        Type localVarReturnType = new TypeToken<CreateTechnique200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create technique (asynchronously)
     * Create a new technique in Rudder from a technique in the technique editor
     * @param editorTechnique  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createTechniqueAsync(List<EditorTechnique> editorTechnique, final ApiCallback<CreateTechnique200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createTechniqueValidateBeforeCall(editorTechnique, _callback);
        Type localVarReturnType = new TypeToken<CreateTechnique200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteTechnique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteTechniqueCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}/{techniqueVersion}"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()))
            .replace("{" + "techniqueVersion" + "}", localVarApiClient.escapeString(techniqueVersion.toString()));

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
    private okhttp3.Call deleteTechniqueValidateBeforeCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling deleteTechnique(Async)");
        }

        // verify the required parameter 'techniqueVersion' is set
        if (techniqueVersion == null) {
            throw new ApiException("Missing the required parameter 'techniqueVersion' when calling deleteTechnique(Async)");
        }

        return deleteTechniqueCall(techniqueId, techniqueVersion, _callback);

    }

    /**
     * Delete technique
     * Delete a technique from technique editor
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return DeleteTechnique200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion information </td><td>  -  </td></tr>
     </table>
     */
    public DeleteTechnique200Response deleteTechnique(String techniqueId, String techniqueVersion) throws ApiException {
        ApiResponse<DeleteTechnique200Response> localVarResp = deleteTechniqueWithHttpInfo(techniqueId, techniqueVersion);
        return localVarResp.getData();
    }

    /**
     * Delete technique
     * Delete a technique from technique editor
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return ApiResponse&lt;DeleteTechnique200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteTechnique200Response> deleteTechniqueWithHttpInfo(String techniqueId, String techniqueVersion) throws ApiException {
        okhttp3.Call localVarCall = deleteTechniqueValidateBeforeCall(techniqueId, techniqueVersion, null);
        Type localVarReturnType = new TypeToken<DeleteTechnique200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete technique (asynchronously)
     * Delete a technique from technique editor
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Deletion information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteTechniqueAsync(String techniqueId, String techniqueVersion, final ApiCallback<DeleteTechnique200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteTechniqueValidateBeforeCall(techniqueId, techniqueVersion, _callback);
        Type localVarReturnType = new TypeToken<DeleteTechnique200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTechniqueAllVersion
     * @param techniqueId Technique ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTechniqueAllVersionCall(String techniqueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()));

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
    private okhttp3.Call getTechniqueAllVersionValidateBeforeCall(String techniqueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling getTechniqueAllVersion(Async)");
        }

        return getTechniqueAllVersionCall(techniqueId, _callback);

    }

    /**
     * Technique metadata by ID
     * Get each Technique&#39;s versions with their metadata by ID
     * @param techniqueId Technique ID (required)
     * @return GetTechniqueAllVersion200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public GetTechniqueAllVersion200Response getTechniqueAllVersion(String techniqueId) throws ApiException {
        ApiResponse<GetTechniqueAllVersion200Response> localVarResp = getTechniqueAllVersionWithHttpInfo(techniqueId);
        return localVarResp.getData();
    }

    /**
     * Technique metadata by ID
     * Get each Technique&#39;s versions with their metadata by ID
     * @param techniqueId Technique ID (required)
     * @return ApiResponse&lt;GetTechniqueAllVersion200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetTechniqueAllVersion200Response> getTechniqueAllVersionWithHttpInfo(String techniqueId) throws ApiException {
        okhttp3.Call localVarCall = getTechniqueAllVersionValidateBeforeCall(techniqueId, null);
        Type localVarReturnType = new TypeToken<GetTechniqueAllVersion200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Technique metadata by ID (asynchronously)
     * Get each Technique&#39;s versions with their metadata by ID
     * @param techniqueId Technique ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTechniqueAllVersionAsync(String techniqueId, final ApiCallback<GetTechniqueAllVersion200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTechniqueAllVersionValidateBeforeCall(techniqueId, _callback);
        Type localVarReturnType = new TypeToken<GetTechniqueAllVersion200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTechniqueAllVersionId
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTechniqueAllVersionIdCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}/{techniqueVersion}"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()))
            .replace("{" + "techniqueVersion" + "}", localVarApiClient.escapeString(techniqueVersion.toString()));

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
    private okhttp3.Call getTechniqueAllVersionIdValidateBeforeCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling getTechniqueAllVersionId(Async)");
        }

        // verify the required parameter 'techniqueVersion' is set
        if (techniqueVersion == null) {
            throw new ApiException("Missing the required parameter 'techniqueVersion' when calling getTechniqueAllVersionId(Async)");
        }

        return getTechniqueAllVersionIdCall(techniqueId, techniqueVersion, _callback);

    }

    /**
     * Technique metadata by version and ID
     * Get Technique metadata
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return GetTechniqueAllVersion200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public GetTechniqueAllVersion200Response getTechniqueAllVersionId(String techniqueId, String techniqueVersion) throws ApiException {
        ApiResponse<GetTechniqueAllVersion200Response> localVarResp = getTechniqueAllVersionIdWithHttpInfo(techniqueId, techniqueVersion);
        return localVarResp.getData();
    }

    /**
     * Technique metadata by version and ID
     * Get Technique metadata
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return ApiResponse&lt;GetTechniqueAllVersion200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetTechniqueAllVersion200Response> getTechniqueAllVersionIdWithHttpInfo(String techniqueId, String techniqueVersion) throws ApiException {
        okhttp3.Call localVarCall = getTechniqueAllVersionIdValidateBeforeCall(techniqueId, techniqueVersion, null);
        Type localVarReturnType = new TypeToken<GetTechniqueAllVersion200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Technique metadata by version and ID (asynchronously)
     * Get Technique metadata
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTechniqueAllVersionIdAsync(String techniqueId, String techniqueVersion, final ApiCallback<GetTechniqueAllVersion200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTechniqueAllVersionIdValidateBeforeCall(techniqueId, techniqueVersion, _callback);
        Type localVarReturnType = new TypeToken<GetTechniqueAllVersion200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTechniquesResources
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resources information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTechniquesResourcesCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}/{techniqueVersion}/resources"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()))
            .replace("{" + "techniqueVersion" + "}", localVarApiClient.escapeString(techniqueVersion.toString()));

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
    private okhttp3.Call getTechniquesResourcesValidateBeforeCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling getTechniquesResources(Async)");
        }

        // verify the required parameter 'techniqueVersion' is set
        if (techniqueVersion == null) {
            throw new ApiException("Missing the required parameter 'techniqueVersion' when calling getTechniquesResources(Async)");
        }

        return getTechniquesResourcesCall(techniqueId, techniqueVersion, _callback);

    }

    /**
     * Technique&#39;s resources
     * Get currently deployed resources of a technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return GetTechniquesResources200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resources information </td><td>  -  </td></tr>
     </table>
     */
    public GetTechniquesResources200Response getTechniquesResources(String techniqueId, String techniqueVersion) throws ApiException {
        ApiResponse<GetTechniquesResources200Response> localVarResp = getTechniquesResourcesWithHttpInfo(techniqueId, techniqueVersion);
        return localVarResp.getData();
    }

    /**
     * Technique&#39;s resources
     * Get currently deployed resources of a technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return ApiResponse&lt;GetTechniquesResources200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resources information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetTechniquesResources200Response> getTechniquesResourcesWithHttpInfo(String techniqueId, String techniqueVersion) throws ApiException {
        okhttp3.Call localVarCall = getTechniquesResourcesValidateBeforeCall(techniqueId, techniqueVersion, null);
        Type localVarReturnType = new TypeToken<GetTechniquesResources200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Technique&#39;s resources (asynchronously)
     * Get currently deployed resources of a technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Resources information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTechniquesResourcesAsync(String techniqueId, String techniqueVersion, final ApiCallback<GetTechniquesResources200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTechniquesResourcesValidateBeforeCall(techniqueId, techniqueVersion, _callback);
        Type localVarReturnType = new TypeToken<GetTechniquesResources200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTechniqueVersionDirectives
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniqueVersionDirectivesCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}/{techniqueVersion}/directives"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()))
            .replace("{" + "techniqueVersion" + "}", localVarApiClient.escapeString(techniqueVersion.toString()));

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
    private okhttp3.Call listTechniqueVersionDirectivesValidateBeforeCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling listTechniqueVersionDirectives(Async)");
        }

        // verify the required parameter 'techniqueVersion' is set
        if (techniqueVersion == null) {
            throw new ApiException("Missing the required parameter 'techniqueVersion' when calling listTechniqueVersionDirectives(Async)");
        }

        return listTechniqueVersionDirectivesCall(techniqueId, techniqueVersion, _callback);

    }

    /**
     * List all directives based on a version of a technique
     * List all directives based on a version of a technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return ListTechniqueVersionDirectives200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ListTechniqueVersionDirectives200Response listTechniqueVersionDirectives(String techniqueId, String techniqueVersion) throws ApiException {
        ApiResponse<ListTechniqueVersionDirectives200Response> localVarResp = listTechniqueVersionDirectivesWithHttpInfo(techniqueId, techniqueVersion);
        return localVarResp.getData();
    }

    /**
     * List all directives based on a version of a technique
     * List all directives based on a version of a technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return ApiResponse&lt;ListTechniqueVersionDirectives200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTechniqueVersionDirectives200Response> listTechniqueVersionDirectivesWithHttpInfo(String techniqueId, String techniqueVersion) throws ApiException {
        okhttp3.Call localVarCall = listTechniqueVersionDirectivesValidateBeforeCall(techniqueId, techniqueVersion, null);
        Type localVarReturnType = new TypeToken<ListTechniqueVersionDirectives200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all directives based on a version of a technique (asynchronously)
     * List all directives based on a version of a technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniqueVersionDirectivesAsync(String techniqueId, String techniqueVersion, final ApiCallback<ListTechniqueVersionDirectives200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTechniqueVersionDirectivesValidateBeforeCall(techniqueId, techniqueVersion, _callback);
        Type localVarReturnType = new TypeToken<ListTechniqueVersionDirectives200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTechniques
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniquesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques";

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
    private okhttp3.Call listTechniquesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listTechniquesCall(_callback);

    }

    /**
     * List all techniques
     * List all technique with their versions
     * @return ListTechniques200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ListTechniques200Response listTechniques() throws ApiException {
        ApiResponse<ListTechniques200Response> localVarResp = listTechniquesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List all techniques
     * List all technique with their versions
     * @return ApiResponse&lt;ListTechniques200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTechniques200Response> listTechniquesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listTechniquesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListTechniques200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all techniques (asynchronously)
     * List all technique with their versions
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniquesAsync(final ApiCallback<ListTechniques200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTechniquesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListTechniques200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTechniquesDirectives
     * @param techniqueId Technique ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniquesDirectivesCall(String techniqueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}/directives"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()));

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
    private okhttp3.Call listTechniquesDirectivesValidateBeforeCall(String techniqueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling listTechniquesDirectives(Async)");
        }

        return listTechniquesDirectivesCall(techniqueId, _callback);

    }

    /**
     * List all directives based on a technique
     * List all directives based on all version of a technique
     * @param techniqueId Technique ID (required)
     * @return ListTechniquesDirectives200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ListTechniquesDirectives200Response listTechniquesDirectives(String techniqueId) throws ApiException {
        ApiResponse<ListTechniquesDirectives200Response> localVarResp = listTechniquesDirectivesWithHttpInfo(techniqueId);
        return localVarResp.getData();
    }

    /**
     * List all directives based on a technique
     * List all directives based on all version of a technique
     * @param techniqueId Technique ID (required)
     * @return ApiResponse&lt;ListTechniquesDirectives200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTechniquesDirectives200Response> listTechniquesDirectivesWithHttpInfo(String techniqueId) throws ApiException {
        okhttp3.Call localVarCall = listTechniquesDirectivesValidateBeforeCall(techniqueId, null);
        Type localVarReturnType = new TypeToken<ListTechniquesDirectives200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all directives based on a technique (asynchronously)
     * List all directives based on all version of a technique
     * @param techniqueId Technique ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniquesDirectivesAsync(String techniqueId, final ApiCallback<ListTechniquesDirectives200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTechniquesDirectivesValidateBeforeCall(techniqueId, _callback);
        Type localVarReturnType = new TypeToken<ListTechniquesDirectives200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTechniquesVersions
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniquesVersionsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/versions";

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
    private okhttp3.Call listTechniquesVersionsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listTechniquesVersionsCall(_callback);

    }

    /**
     * List versions
     * List all techniques version
     * @return ListTechniquesVersions200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public ListTechniquesVersions200Response listTechniquesVersions() throws ApiException {
        ApiResponse<ListTechniquesVersions200Response> localVarResp = listTechniquesVersionsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List versions
     * List all techniques version
     * @return ApiResponse&lt;ListTechniquesVersions200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTechniquesVersions200Response> listTechniquesVersionsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listTechniquesVersionsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListTechniquesVersions200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List versions (asynchronously)
     * List all techniques version
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTechniquesVersionsAsync(final ApiCallback<ListTechniquesVersions200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTechniquesVersionsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListTechniquesVersions200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for methods
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call methodsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/methods";

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
    private okhttp3.Call methodsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return methodsCall(_callback);

    }

    /**
     * List methods
     * Get all generic methods metadata
     * @return Methods200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public Methods200Response methods() throws ApiException {
        ApiResponse<Methods200Response> localVarResp = methodsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List methods
     * Get all generic methods metadata
     * @return ApiResponse&lt;Methods200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Methods200Response> methodsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = methodsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Methods200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List methods (asynchronously)
     * Get all generic methods metadata
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call methodsAsync(final ApiCallback<Methods200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = methodsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Methods200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reloadMethods
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadMethodsCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/methods/reload";

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
    private okhttp3.Call reloadMethodsValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return reloadMethodsCall(_callback);

    }

    /**
     * Reload methods
     * Reload methods metadata from file system
     * @return Methods200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public Methods200Response reloadMethods() throws ApiException {
        ApiResponse<Methods200Response> localVarResp = reloadMethodsWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Reload methods
     * Reload methods metadata from file system
     * @return ApiResponse&lt;Methods200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Methods200Response> reloadMethodsWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = reloadMethodsValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Methods200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reload methods (asynchronously)
     * Reload methods metadata from file system
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Methods information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadMethodsAsync(final ApiCallback<Methods200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = reloadMethodsValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Methods200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for techniqueCategories
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Categories information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call techniqueCategoriesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/categories";

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
    private okhttp3.Call techniqueCategoriesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return techniqueCategoriesCall(_callback);

    }

    /**
     * List categories
     * Get all technique categories
     * @return TechniqueCategories200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Categories information </td><td>  -  </td></tr>
     </table>
     */
    public TechniqueCategories200Response techniqueCategories() throws ApiException {
        ApiResponse<TechniqueCategories200Response> localVarResp = techniqueCategoriesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List categories
     * Get all technique categories
     * @return ApiResponse&lt;TechniqueCategories200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Categories information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TechniqueCategories200Response> techniqueCategoriesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = techniqueCategoriesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<TechniqueCategories200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List categories (asynchronously)
     * Get all technique categories
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Categories information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call techniqueCategoriesAsync(final ApiCallback<TechniqueCategories200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = techniqueCategoriesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<TechniqueCategories200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for techniqueRevisions
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call techniqueRevisionsCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/{techniqueId}/{techniqueVersion}/revisions"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()))
            .replace("{" + "techniqueVersion" + "}", localVarApiClient.escapeString(techniqueVersion.toString()));

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
    private okhttp3.Call techniqueRevisionsValidateBeforeCall(String techniqueId, String techniqueVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling techniqueRevisions(Async)");
        }

        // verify the required parameter 'techniqueVersion' is set
        if (techniqueVersion == null) {
            throw new ApiException("Missing the required parameter 'techniqueVersion' when calling techniqueRevisions(Async)");
        }

        return techniqueRevisionsCall(techniqueId, techniqueVersion, _callback);

    }

    /**
     * Technique&#39;s revisions
     * Get revisions for given technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return TechniqueRevisions200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public TechniqueRevisions200Response techniqueRevisions(String techniqueId, String techniqueVersion) throws ApiException {
        ApiResponse<TechniqueRevisions200Response> localVarResp = techniqueRevisionsWithHttpInfo(techniqueId, techniqueVersion);
        return localVarResp.getData();
    }

    /**
     * Technique&#39;s revisions
     * Get revisions for given technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @return ApiResponse&lt;TechniqueRevisions200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TechniqueRevisions200Response> techniqueRevisionsWithHttpInfo(String techniqueId, String techniqueVersion) throws ApiException {
        okhttp3.Call localVarCall = techniqueRevisionsValidateBeforeCall(techniqueId, techniqueVersion, null);
        Type localVarReturnType = new TypeToken<TechniqueRevisions200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Technique&#39;s revisions (asynchronously)
     * Get revisions for given technique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call techniqueRevisionsAsync(String techniqueId, String techniqueVersion, final ApiCallback<TechniqueRevisions200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = techniqueRevisionsValidateBeforeCall(techniqueId, techniqueVersion, _callback);
        Type localVarReturnType = new TypeToken<TechniqueRevisions200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for techniques
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call techniquesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/techniques/reload";

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
    private okhttp3.Call techniquesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return techniquesCall(_callback);

    }

    /**
     * Reload techniques
     * Reload all techniques metadata from file system
     * @return ListTechniques200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ListTechniques200Response techniques() throws ApiException {
        ApiResponse<ListTechniques200Response> localVarResp = techniquesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Reload techniques
     * Reload all techniques metadata from file system
     * @return ApiResponse&lt;ListTechniques200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTechniques200Response> techniquesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = techniquesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ListTechniques200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reload techniques (asynchronously)
     * Reload all techniques metadata from file system
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Techniques information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call techniquesAsync(final ApiCallback<ListTechniques200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = techniquesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ListTechniques200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateTechnique
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param editorTechnique  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateTechniqueCall(String techniqueId, String techniqueVersion, List<EditorTechnique> editorTechnique, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = editorTechnique;

        // create path and map variables
        String localVarPath = "/techniques/{techniqueId}/{techniqueVersion}"
            .replace("{" + "techniqueId" + "}", localVarApiClient.escapeString(techniqueId.toString()))
            .replace("{" + "techniqueVersion" + "}", localVarApiClient.escapeString(techniqueVersion.toString()));

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
    private okhttp3.Call updateTechniqueValidateBeforeCall(String techniqueId, String techniqueVersion, List<EditorTechnique> editorTechnique, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'techniqueId' is set
        if (techniqueId == null) {
            throw new ApiException("Missing the required parameter 'techniqueId' when calling updateTechnique(Async)");
        }

        // verify the required parameter 'techniqueVersion' is set
        if (techniqueVersion == null) {
            throw new ApiException("Missing the required parameter 'techniqueVersion' when calling updateTechnique(Async)");
        }

        // verify the required parameter 'editorTechnique' is set
        if (editorTechnique == null) {
            throw new ApiException("Missing the required parameter 'editorTechnique' when calling updateTechnique(Async)");
        }

        return updateTechniqueCall(techniqueId, techniqueVersion, editorTechnique, _callback);

    }

    /**
     * Update technique
     * Update technique created with technique editor
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param editorTechnique  (required)
     * @return CreateTechnique200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public CreateTechnique200Response updateTechnique(String techniqueId, String techniqueVersion, List<EditorTechnique> editorTechnique) throws ApiException {
        ApiResponse<CreateTechnique200Response> localVarResp = updateTechniqueWithHttpInfo(techniqueId, techniqueVersion, editorTechnique);
        return localVarResp.getData();
    }

    /**
     * Update technique
     * Update technique created with technique editor
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param editorTechnique  (required)
     * @return ApiResponse&lt;CreateTechnique200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateTechnique200Response> updateTechniqueWithHttpInfo(String techniqueId, String techniqueVersion, List<EditorTechnique> editorTechnique) throws ApiException {
        okhttp3.Call localVarCall = updateTechniqueValidateBeforeCall(techniqueId, techniqueVersion, editorTechnique, null);
        Type localVarReturnType = new TypeToken<CreateTechnique200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update technique (asynchronously)
     * Update technique created with technique editor
     * @param techniqueId Technique ID (required)
     * @param techniqueVersion Technique version (required)
     * @param editorTechnique  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Versions information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateTechniqueAsync(String techniqueId, String techniqueVersion, List<EditorTechnique> editorTechnique, final ApiCallback<CreateTechnique200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateTechniqueValidateBeforeCall(techniqueId, techniqueVersion, editorTechnique, _callback);
        Type localVarReturnType = new TypeToken<CreateTechnique200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
