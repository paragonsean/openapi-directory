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


import org.openapitools.client.model.CreateDataSource200Response;
import org.openapitools.client.model.Datasource;
import org.openapitools.client.model.DeleteDataSource200Response;
import org.openapitools.client.model.GetAllDataSources200Response;
import org.openapitools.client.model.GetDataSource200Response;
import org.openapitools.client.model.ReloadAllDatasourcesAllNodes200Response;
import org.openapitools.client.model.ReloadAllDatasourcesOneNode200Response;
import org.openapitools.client.model.ReloadOneDatasourceAllNodes200Response;
import org.openapitools.client.model.ReloadOneDatasourceOneNode200Response;
import org.openapitools.client.model.UpdateDataSource200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DataSourcesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DataSourcesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DataSourcesApi(ApiClient apiClient) {
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
     * Build call for createDataSource
     * @param datasource  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDataSourceCall(Datasource datasource, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = datasource;

        // create path and map variables
        String localVarPath = "/datasources";

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
    private okhttp3.Call createDataSourceValidateBeforeCall(Datasource datasource, final ApiCallback _callback) throws ApiException {
        return createDataSourceCall(datasource, _callback);

    }

    /**
     * Create a data source
     * Create a new data source
     * @param datasource  (optional)
     * @return CreateDataSource200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public CreateDataSource200Response createDataSource(Datasource datasource) throws ApiException {
        ApiResponse<CreateDataSource200Response> localVarResp = createDataSourceWithHttpInfo(datasource);
        return localVarResp.getData();
    }

    /**
     * Create a data source
     * Create a new data source
     * @param datasource  (optional)
     * @return ApiResponse&lt;CreateDataSource200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateDataSource200Response> createDataSourceWithHttpInfo(Datasource datasource) throws ApiException {
        okhttp3.Call localVarCall = createDataSourceValidateBeforeCall(datasource, null);
        Type localVarReturnType = new TypeToken<CreateDataSource200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a data source (asynchronously)
     * Create a new data source
     * @param datasource  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Created </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createDataSourceAsync(Datasource datasource, final ApiCallback<CreateDataSource200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = createDataSourceValidateBeforeCall(datasource, _callback);
        Type localVarReturnType = new TypeToken<CreateDataSource200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDataSource
     * @param datasourceId Id of the data source (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDataSourceCall(String datasourceId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datasources/{datasourceId}"
            .replace("{" + "datasourceId" + "}", localVarApiClient.escapeString(datasourceId.toString()));

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
    private okhttp3.Call deleteDataSourceValidateBeforeCall(String datasourceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datasourceId' is set
        if (datasourceId == null) {
            throw new ApiException("Missing the required parameter 'datasourceId' when calling deleteDataSource(Async)");
        }

        return deleteDataSourceCall(datasourceId, _callback);

    }

    /**
     * Delete a data source
     * Delete a data source configuration
     * @param datasourceId Id of the data source (required)
     * @return DeleteDataSource200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public DeleteDataSource200Response deleteDataSource(String datasourceId) throws ApiException {
        ApiResponse<DeleteDataSource200Response> localVarResp = deleteDataSourceWithHttpInfo(datasourceId);
        return localVarResp.getData();
    }

    /**
     * Delete a data source
     * Delete a data source configuration
     * @param datasourceId Id of the data source (required)
     * @return ApiResponse&lt;DeleteDataSource200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteDataSource200Response> deleteDataSourceWithHttpInfo(String datasourceId) throws ApiException {
        okhttp3.Call localVarCall = deleteDataSourceValidateBeforeCall(datasourceId, null);
        Type localVarReturnType = new TypeToken<DeleteDataSource200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a data source (asynchronously)
     * Delete a data source configuration
     * @param datasourceId Id of the data source (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDataSourceAsync(String datasourceId, final ApiCallback<DeleteDataSource200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDataSourceValidateBeforeCall(datasourceId, _callback);
        Type localVarReturnType = new TypeToken<DeleteDataSource200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllDataSources
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllDataSourcesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datasources";

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
    private okhttp3.Call getAllDataSourcesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getAllDataSourcesCall(_callback);

    }

    /**
     * List all data sources
     * Get the configuration of all present data sources
     * @return GetAllDataSources200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources information </td><td>  -  </td></tr>
     </table>
     */
    public GetAllDataSources200Response getAllDataSources() throws ApiException {
        ApiResponse<GetAllDataSources200Response> localVarResp = getAllDataSourcesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * List all data sources
     * Get the configuration of all present data sources
     * @return ApiResponse&lt;GetAllDataSources200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetAllDataSources200Response> getAllDataSourcesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getAllDataSourcesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetAllDataSources200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List all data sources (asynchronously)
     * Get the configuration of all present data sources
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllDataSourcesAsync(final ApiCallback<GetAllDataSources200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllDataSourcesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetAllDataSources200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDataSource
     * @param datasourceId Id of the data source (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDataSourceCall(String datasourceId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datasources/{datasourceId}"
            .replace("{" + "datasourceId" + "}", localVarApiClient.escapeString(datasourceId.toString()));

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
    private okhttp3.Call getDataSourceValidateBeforeCall(String datasourceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datasourceId' is set
        if (datasourceId == null) {
            throw new ApiException("Missing the required parameter 'datasourceId' when calling getDataSource(Async)");
        }

        return getDataSourceCall(datasourceId, _callback);

    }

    /**
     * Get data source configuration
     * Get the configuration of a data source
     * @param datasourceId Id of the data source (required)
     * @return GetDataSource200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public GetDataSource200Response getDataSource(String datasourceId) throws ApiException {
        ApiResponse<GetDataSource200Response> localVarResp = getDataSourceWithHttpInfo(datasourceId);
        return localVarResp.getData();
    }

    /**
     * Get data source configuration
     * Get the configuration of a data source
     * @param datasourceId Id of the data source (required)
     * @return ApiResponse&lt;GetDataSource200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetDataSource200Response> getDataSourceWithHttpInfo(String datasourceId) throws ApiException {
        okhttp3.Call localVarCall = getDataSourceValidateBeforeCall(datasourceId, null);
        Type localVarReturnType = new TypeToken<GetDataSource200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get data source configuration (asynchronously)
     * Get the configuration of a data source
     * @param datasourceId Id of the data source (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDataSourceAsync(String datasourceId, final ApiCallback<GetDataSource200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDataSourceValidateBeforeCall(datasourceId, _callback);
        Type localVarReturnType = new TypeToken<GetDataSource200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reloadAllDatasourcesAllNodes
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadAllDatasourcesAllNodesCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datasources/reload";

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
    private okhttp3.Call reloadAllDatasourcesAllNodesValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return reloadAllDatasourcesAllNodesCall(_callback);

    }

    /**
     * Update properties from data sources
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @return ReloadAllDatasourcesAllNodes200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ReloadAllDatasourcesAllNodes200Response reloadAllDatasourcesAllNodes() throws ApiException {
        ApiResponse<ReloadAllDatasourcesAllNodes200Response> localVarResp = reloadAllDatasourcesAllNodesWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Update properties from data sources
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @return ApiResponse&lt;ReloadAllDatasourcesAllNodes200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReloadAllDatasourcesAllNodes200Response> reloadAllDatasourcesAllNodesWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = reloadAllDatasourcesAllNodesValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ReloadAllDatasourcesAllNodes200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update properties from data sources (asynchronously)
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadAllDatasourcesAllNodesAsync(final ApiCallback<ReloadAllDatasourcesAllNodes200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = reloadAllDatasourcesAllNodesValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ReloadAllDatasourcesAllNodes200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reloadAllDatasourcesOneNode
     * @param nodeId Id of the target node (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadAllDatasourcesOneNodeCall(String nodeId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodes/{nodeId}/fetchData"
            .replace("{" + "nodeId" + "}", localVarApiClient.escapeString(nodeId.toString()));

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
    private okhttp3.Call reloadAllDatasourcesOneNodeValidateBeforeCall(String nodeId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling reloadAllDatasourcesOneNode(Async)");
        }

        return reloadAllDatasourcesOneNodeCall(nodeId, _callback);

    }

    /**
     * Update properties for one node from all data sources
     * Update properties from all data sources on one nodes. The call is asynchronous.
     * @param nodeId Id of the target node (required)
     * @return ReloadAllDatasourcesOneNode200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ReloadAllDatasourcesOneNode200Response reloadAllDatasourcesOneNode(String nodeId) throws ApiException {
        ApiResponse<ReloadAllDatasourcesOneNode200Response> localVarResp = reloadAllDatasourcesOneNodeWithHttpInfo(nodeId);
        return localVarResp.getData();
    }

    /**
     * Update properties for one node from all data sources
     * Update properties from all data sources on one nodes. The call is asynchronous.
     * @param nodeId Id of the target node (required)
     * @return ApiResponse&lt;ReloadAllDatasourcesOneNode200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReloadAllDatasourcesOneNode200Response> reloadAllDatasourcesOneNodeWithHttpInfo(String nodeId) throws ApiException {
        okhttp3.Call localVarCall = reloadAllDatasourcesOneNodeValidateBeforeCall(nodeId, null);
        Type localVarReturnType = new TypeToken<ReloadAllDatasourcesOneNode200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update properties for one node from all data sources (asynchronously)
     * Update properties from all data sources on one nodes. The call is asynchronous.
     * @param nodeId Id of the target node (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadAllDatasourcesOneNodeAsync(String nodeId, final ApiCallback<ReloadAllDatasourcesOneNode200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = reloadAllDatasourcesOneNodeValidateBeforeCall(nodeId, _callback);
        Type localVarReturnType = new TypeToken<ReloadAllDatasourcesOneNode200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reloadOneDatasourceAllNodes
     * @param datasourceId Id of the data source (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadOneDatasourceAllNodesCall(String datasourceId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/datasources/reload/{datasourceId}"
            .replace("{" + "datasourceId" + "}", localVarApiClient.escapeString(datasourceId.toString()));

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
    private okhttp3.Call reloadOneDatasourceAllNodesValidateBeforeCall(String datasourceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datasourceId' is set
        if (datasourceId == null) {
            throw new ApiException("Missing the required parameter 'datasourceId' when calling reloadOneDatasourceAllNodes(Async)");
        }

        return reloadOneDatasourceAllNodesCall(datasourceId, _callback);

    }

    /**
     * Update properties from data sources
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @param datasourceId Id of the data source (required)
     * @return ReloadOneDatasourceAllNodes200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ReloadOneDatasourceAllNodes200Response reloadOneDatasourceAllNodes(String datasourceId) throws ApiException {
        ApiResponse<ReloadOneDatasourceAllNodes200Response> localVarResp = reloadOneDatasourceAllNodesWithHttpInfo(datasourceId);
        return localVarResp.getData();
    }

    /**
     * Update properties from data sources
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @param datasourceId Id of the data source (required)
     * @return ApiResponse&lt;ReloadOneDatasourceAllNodes200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReloadOneDatasourceAllNodes200Response> reloadOneDatasourceAllNodesWithHttpInfo(String datasourceId) throws ApiException {
        okhttp3.Call localVarCall = reloadOneDatasourceAllNodesValidateBeforeCall(datasourceId, null);
        Type localVarReturnType = new TypeToken<ReloadOneDatasourceAllNodes200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update properties from data sources (asynchronously)
     * Update properties from all data source on all nodes. The call is asynchronous.
     * @param datasourceId Id of the data source (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadOneDatasourceAllNodesAsync(String datasourceId, final ApiCallback<ReloadOneDatasourceAllNodes200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = reloadOneDatasourceAllNodesValidateBeforeCall(datasourceId, _callback);
        Type localVarReturnType = new TypeToken<ReloadOneDatasourceAllNodes200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for reloadOneDatasourceOneNode
     * @param nodeId Id of the target node (required)
     * @param datasourceId Id of the data source (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadOneDatasourceOneNodeCall(String nodeId, String datasourceId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/nodes/{nodeId}/fetchData/{datasourceId}"
            .replace("{" + "nodeId" + "}", localVarApiClient.escapeString(nodeId.toString()))
            .replace("{" + "datasourceId" + "}", localVarApiClient.escapeString(datasourceId.toString()));

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
    private okhttp3.Call reloadOneDatasourceOneNodeValidateBeforeCall(String nodeId, String datasourceId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'nodeId' is set
        if (nodeId == null) {
            throw new ApiException("Missing the required parameter 'nodeId' when calling reloadOneDatasourceOneNode(Async)");
        }

        // verify the required parameter 'datasourceId' is set
        if (datasourceId == null) {
            throw new ApiException("Missing the required parameter 'datasourceId' when calling reloadOneDatasourceOneNode(Async)");
        }

        return reloadOneDatasourceOneNodeCall(nodeId, datasourceId, _callback);

    }

    /**
     * Update properties for one node from a data source
     * Update properties from a data source on one nodes. The call is asynchronous.
     * @param nodeId Id of the target node (required)
     * @param datasourceId Id of the data source (required)
     * @return ReloadOneDatasourceOneNode200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ReloadOneDatasourceOneNode200Response reloadOneDatasourceOneNode(String nodeId, String datasourceId) throws ApiException {
        ApiResponse<ReloadOneDatasourceOneNode200Response> localVarResp = reloadOneDatasourceOneNodeWithHttpInfo(nodeId, datasourceId);
        return localVarResp.getData();
    }

    /**
     * Update properties for one node from a data source
     * Update properties from a data source on one nodes. The call is asynchronous.
     * @param nodeId Id of the target node (required)
     * @param datasourceId Id of the data source (required)
     * @return ApiResponse&lt;ReloadOneDatasourceOneNode200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ReloadOneDatasourceOneNode200Response> reloadOneDatasourceOneNodeWithHttpInfo(String nodeId, String datasourceId) throws ApiException {
        okhttp3.Call localVarCall = reloadOneDatasourceOneNodeValidateBeforeCall(nodeId, datasourceId, null);
        Type localVarReturnType = new TypeToken<ReloadOneDatasourceOneNode200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update properties for one node from a data source (asynchronously)
     * Update properties from a data source on one nodes. The call is asynchronous.
     * @param nodeId Id of the target node (required)
     * @param datasourceId Id of the data source (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data sources reloaded </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call reloadOneDatasourceOneNodeAsync(String nodeId, String datasourceId, final ApiCallback<ReloadOneDatasourceOneNode200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = reloadOneDatasourceOneNodeValidateBeforeCall(nodeId, datasourceId, _callback);
        Type localVarReturnType = new TypeToken<ReloadOneDatasourceOneNode200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateDataSource
     * @param datasourceId Id of the data source (required)
     * @param datasource  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDataSourceCall(String datasourceId, Datasource datasource, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = datasource;

        // create path and map variables
        String localVarPath = "/datasources/{datasourceId}"
            .replace("{" + "datasourceId" + "}", localVarApiClient.escapeString(datasourceId.toString()));

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
    private okhttp3.Call updateDataSourceValidateBeforeCall(String datasourceId, Datasource datasource, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'datasourceId' is set
        if (datasourceId == null) {
            throw new ApiException("Missing the required parameter 'datasourceId' when calling updateDataSource(Async)");
        }

        return updateDataSourceCall(datasourceId, datasource, _callback);

    }

    /**
     * Update a data source configuration
     * Update the configuration of a data source
     * @param datasourceId Id of the data source (required)
     * @param datasource  (optional)
     * @return UpdateDataSource200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public UpdateDataSource200Response updateDataSource(String datasourceId, Datasource datasource) throws ApiException {
        ApiResponse<UpdateDataSource200Response> localVarResp = updateDataSourceWithHttpInfo(datasourceId, datasource);
        return localVarResp.getData();
    }

    /**
     * Update a data source configuration
     * Update the configuration of a data source
     * @param datasourceId Id of the data source (required)
     * @param datasource  (optional)
     * @return ApiResponse&lt;UpdateDataSource200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateDataSource200Response> updateDataSourceWithHttpInfo(String datasourceId, Datasource datasource) throws ApiException {
        okhttp3.Call localVarCall = updateDataSourceValidateBeforeCall(datasourceId, datasource, null);
        Type localVarReturnType = new TypeToken<UpdateDataSource200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a data source configuration (asynchronously)
     * Update the configuration of a data source
     * @param datasourceId Id of the data source (required)
     * @param datasource  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Data source information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateDataSourceAsync(String datasourceId, Datasource datasource, final ApiCallback<UpdateDataSource200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateDataSourceValidateBeforeCall(datasourceId, datasource, _callback);
        Type localVarReturnType = new TypeToken<UpdateDataSource200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
