/*
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
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


import org.openapitools.client.model.BadRequestResponse;
import org.openapitools.client.model.BulkActionRequestBody;
import org.openapitools.client.model.ClockingRecordsClockingRecordIdPut200Response;
import org.openapitools.client.model.ClockingRecordsPost201Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsPostRequest;
import org.openapitools.client.model.CreateSuccessResponse;
import org.openapitools.client.model.EmptySuccessResponse;
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import java.io.File;
import org.openapitools.client.model.ForbiddenError;
import org.openapitools.client.model.ProjectsProjectIdUsersGet200Response;
import org.openapitools.client.model.ProjectsProjectIdUsersUserIdGet200Response;
import org.openapitools.client.model.UsersPostRequest;
import org.openapitools.client.model.UsersResendWelcomeSmsGet200Response;
import org.openapitools.client.model.UsersUserIdIntegrationSettingsGet200Response;
import org.openapitools.client.model.UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UsersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public UsersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public UsersApi(ApiClient apiClient) {
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
     * Build call for usersBulkActivate
     * @param bulkActionRequestBody User ids (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersBulkActivateCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = bulkActionRequestBody;

        // create path and map variables
        String localVarPath = "/users/bulkActivate";

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersBulkActivateValidateBeforeCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
        return usersBulkActivateCall(bulkActionRequestBody, _callback);

    }

    /**
     * Activate multiple users
     * 
     * @param bulkActionRequestBody User ids (optional)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse usersBulkActivate(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = usersBulkActivateWithHttpInfo(bulkActionRequestBody);
        return localVarResp.getData();
    }

    /**
     * Activate multiple users
     * 
     * @param bulkActionRequestBody User ids (optional)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> usersBulkActivateWithHttpInfo(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        okhttp3.Call localVarCall = usersBulkActivateValidateBeforeCall(bulkActionRequestBody, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Activate multiple users (asynchronously)
     * 
     * @param bulkActionRequestBody User ids (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersBulkActivateAsync(BulkActionRequestBody bulkActionRequestBody, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersBulkActivateValidateBeforeCall(bulkActionRequestBody, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersBulkDeactivate
     * @param bulkActionRequestBody User ids (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersBulkDeactivateCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = bulkActionRequestBody;

        // create path and map variables
        String localVarPath = "/users/bulkDeactivate";

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersBulkDeactivateValidateBeforeCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
        return usersBulkDeactivateCall(bulkActionRequestBody, _callback);

    }

    /**
     * Deactivate multiple users
     * 
     * @param bulkActionRequestBody User ids (optional)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse usersBulkDeactivate(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = usersBulkDeactivateWithHttpInfo(bulkActionRequestBody);
        return localVarResp.getData();
    }

    /**
     * Deactivate multiple users
     * 
     * @param bulkActionRequestBody User ids (optional)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> usersBulkDeactivateWithHttpInfo(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        okhttp3.Call localVarCall = usersBulkDeactivateValidateBeforeCall(bulkActionRequestBody, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Deactivate multiple users (asynchronously)
     * 
     * @param bulkActionRequestBody User ids (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersBulkDeactivateAsync(BulkActionRequestBody bulkActionRequestBody, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersBulkDeactivateValidateBeforeCall(bulkActionRequestBody, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersGet
     * @param firstName Used to filter on the &#x60;first_name&#x60; of the users (optional)
     * @param lastName Used to filter on the &#x60;last_name&#x60; of the users (optional)
     * @param email Used to filter on the &#x60;email&#x60; of the users (optional)
     * @param stockLocationId Used to filter on the &#x60;stock_location_id&#x60; of the users (optional)
     * @param isActive Filters active/inactive users (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersGetCall(String firstName, String lastName, String email, String stockLocationId, Boolean isActive, final ApiCallback _callback) throws ApiException {
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

        if (firstName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("first_name", firstName));
        }

        if (lastName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("last_name", lastName));
        }

        if (email != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email", email));
        }

        if (stockLocationId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("stock_location_id", stockLocationId));
        }

        if (isActive != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("is_active", isActive));
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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersGetValidateBeforeCall(String firstName, String lastName, String email, String stockLocationId, Boolean isActive, final ApiCallback _callback) throws ApiException {
        return usersGetCall(firstName, lastName, email, stockLocationId, isActive, _callback);

    }

    /**
     * Get list of users in company
     * 
     * @param firstName Used to filter on the &#x60;first_name&#x60; of the users (optional)
     * @param lastName Used to filter on the &#x60;last_name&#x60; of the users (optional)
     * @param email Used to filter on the &#x60;email&#x60; of the users (optional)
     * @param stockLocationId Used to filter on the &#x60;stock_location_id&#x60; of the users (optional)
     * @param isActive Filters active/inactive users (optional)
     * @return ProjectsProjectIdUsersGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdUsersGet200Response usersGet(String firstName, String lastName, String email, String stockLocationId, Boolean isActive) throws ApiException {
        ApiResponse<ProjectsProjectIdUsersGet200Response> localVarResp = usersGetWithHttpInfo(firstName, lastName, email, stockLocationId, isActive);
        return localVarResp.getData();
    }

    /**
     * Get list of users in company
     * 
     * @param firstName Used to filter on the &#x60;first_name&#x60; of the users (optional)
     * @param lastName Used to filter on the &#x60;last_name&#x60; of the users (optional)
     * @param email Used to filter on the &#x60;email&#x60; of the users (optional)
     * @param stockLocationId Used to filter on the &#x60;stock_location_id&#x60; of the users (optional)
     * @param isActive Filters active/inactive users (optional)
     * @return ApiResponse&lt;ProjectsProjectIdUsersGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdUsersGet200Response> usersGetWithHttpInfo(String firstName, String lastName, String email, String stockLocationId, Boolean isActive) throws ApiException {
        okhttp3.Call localVarCall = usersGetValidateBeforeCall(firstName, lastName, email, stockLocationId, isActive, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get list of users in company (asynchronously)
     * 
     * @param firstName Used to filter on the &#x60;first_name&#x60; of the users (optional)
     * @param lastName Used to filter on the &#x60;last_name&#x60; of the users (optional)
     * @param email Used to filter on the &#x60;email&#x60; of the users (optional)
     * @param stockLocationId Used to filter on the &#x60;stock_location_id&#x60; of the users (optional)
     * @param isActive Filters active/inactive users (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersGetAsync(String firstName, String lastName, String email, String stockLocationId, Boolean isActive, final ApiCallback<ProjectsProjectIdUsersGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersGetValidateBeforeCall(firstName, lastName, email, stockLocationId, isActive, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersPost
     * @param usersPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersPostCall(UsersPostRequest usersPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = usersPostRequest;

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersPostValidateBeforeCall(UsersPostRequest usersPostRequest, final ApiCallback _callback) throws ApiException {
        return usersPostCall(usersPostRequest, _callback);

    }

    /**
     * Add user to company
     * 
     * @param usersPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response usersPost(UsersPostRequest usersPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = usersPostWithHttpInfo(usersPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add user to company
     * 
     * @param usersPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> usersPostWithHttpInfo(UsersPostRequest usersPostRequest) throws ApiException {
        okhttp3.Call localVarCall = usersPostValidateBeforeCall(usersPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add user to company (asynchronously)
     * 
     * @param usersPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersPostAsync(UsersPostRequest usersPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersPostValidateBeforeCall(usersPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersResendWelcomeSmsGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersResendWelcomeSmsGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/resendWelcomeSms";

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersResendWelcomeSmsGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return usersResendWelcomeSmsGetCall(_callback);

    }

    /**
     * Resend Welcome SMS to the user
     * 
     * @return UsersResendWelcomeSmsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public UsersResendWelcomeSmsGet200Response usersResendWelcomeSmsGet() throws ApiException {
        ApiResponse<UsersResendWelcomeSmsGet200Response> localVarResp = usersResendWelcomeSmsGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Resend Welcome SMS to the user
     * 
     * @return ApiResponse&lt;UsersResendWelcomeSmsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UsersResendWelcomeSmsGet200Response> usersResendWelcomeSmsGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = usersResendWelcomeSmsGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<UsersResendWelcomeSmsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Resend Welcome SMS to the user (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersResendWelcomeSmsGetAsync(final ApiCallback<UsersResendWelcomeSmsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersResendWelcomeSmsGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<UsersResendWelcomeSmsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdDelete
     * @param userId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdDeleteCall(String userId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdDeleteValidateBeforeCall(String userId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdDelete(Async)");
        }

        return usersUserIdDeleteCall(userId, _callback);

    }

    /**
     * Delete user
     * 
     * @param userId  (required)
     * @return ClockingRecordsClockingRecordIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdPut200Response usersUserIdDelete(String userId) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdPut200Response> localVarResp = usersUserIdDeleteWithHttpInfo(userId);
        return localVarResp.getData();
    }

    /**
     * Delete user
     * 
     * @param userId  (required)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdPut200Response> usersUserIdDeleteWithHttpInfo(String userId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdDeleteValidateBeforeCall(userId, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete user (asynchronously)
     * 
     * @param userId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdDeleteAsync(String userId, final ApiCallback<ClockingRecordsClockingRecordIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdDeleteValidateBeforeCall(userId, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdGet
     * @param userId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdGetCall(String userId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdGetValidateBeforeCall(String userId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdGet(Async)");
        }

        return usersUserIdGetCall(userId, _callback);

    }

    /**
     * View user
     * 
     * @param userId  (required)
     * @return ProjectsProjectIdUsersUserIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdUsersUserIdGet200Response usersUserIdGet(String userId) throws ApiException {
        ApiResponse<ProjectsProjectIdUsersUserIdGet200Response> localVarResp = usersUserIdGetWithHttpInfo(userId);
        return localVarResp.getData();
    }

    /**
     * View user
     * 
     * @param userId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdUsersUserIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdUsersUserIdGet200Response> usersUserIdGetWithHttpInfo(String userId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdGetValidateBeforeCall(userId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersUserIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * View user (asynchronously)
     * 
     * @param userId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdGetAsync(String userId, final ApiCallback<ProjectsProjectIdUsersUserIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdGetValidateBeforeCall(userId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersUserIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdIntegrationSettingsGet
     * @param userId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsGetCall(String userId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}/integration_settings"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdIntegrationSettingsGetValidateBeforeCall(String userId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsGet(Async)");
        }

        return usersUserIdIntegrationSettingsGetCall(userId, _callback);

    }

    /**
     * Get a list of user integration settings
     * 
     * @param userId  (required)
     * @return UsersUserIdIntegrationSettingsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public UsersUserIdIntegrationSettingsGet200Response usersUserIdIntegrationSettingsGet(String userId) throws ApiException {
        ApiResponse<UsersUserIdIntegrationSettingsGet200Response> localVarResp = usersUserIdIntegrationSettingsGetWithHttpInfo(userId);
        return localVarResp.getData();
    }

    /**
     * Get a list of user integration settings
     * 
     * @param userId  (required)
     * @return ApiResponse&lt;UsersUserIdIntegrationSettingsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UsersUserIdIntegrationSettingsGet200Response> usersUserIdIntegrationSettingsGetWithHttpInfo(String userId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsGetValidateBeforeCall(userId, null);
        Type localVarReturnType = new TypeToken<UsersUserIdIntegrationSettingsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of user integration settings (asynchronously)
     * 
     * @param userId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsGetAsync(String userId, final ApiCallback<UsersUserIdIntegrationSettingsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsGetValidateBeforeCall(userId, _callback);
        Type localVarReturnType = new TypeToken<UsersUserIdIntegrationSettingsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCall(String userId, String integrationSettingsUserId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}/integration_settings/{integration_settings_user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()))
            .replace("{" + "integration_settings_user_id" + "}", localVarApiClient.escapeString(integrationSettingsUserId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteValidateBeforeCall(String userId, String integrationSettingsUserId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(Async)");
        }

        // verify the required parameter 'integrationSettingsUserId' is set
        if (integrationSettingsUserId == null) {
            throw new ApiException("Missing the required parameter 'integrationSettingsUserId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(Async)");
        }

        return usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCall(userId, integrationSettingsUserId, _callback);

    }

    /**
     * Delete a user integration setting
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(String userId, String integrationSettingsUserId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteWithHttpInfo(userId, integrationSettingsUserId);
        return localVarResp.getData();
    }

    /**
     * Delete a user integration setting
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteWithHttpInfo(String userId, String integrationSettingsUserId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteValidateBeforeCall(userId, integrationSettingsUserId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a user integration setting (asynchronously)
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteAsync(String userId, String integrationSettingsUserId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteValidateBeforeCall(userId, integrationSettingsUserId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCall(String userId, String integrationSettingsUserId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}/integration_settings/{integration_settings_user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()))
            .replace("{" + "integration_settings_user_id" + "}", localVarApiClient.escapeString(integrationSettingsUserId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetValidateBeforeCall(String userId, String integrationSettingsUserId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(Async)");
        }

        // verify the required parameter 'integrationSettingsUserId' is set
        if (integrationSettingsUserId == null) {
            throw new ApiException("Missing the required parameter 'integrationSettingsUserId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(Async)");
        }

        return usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCall(userId, integrationSettingsUserId, _callback);

    }

    /**
     * Get a user integration setting
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @return UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(String userId, String integrationSettingsUserId) throws ApiException {
        ApiResponse<UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response> localVarResp = usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetWithHttpInfo(userId, integrationSettingsUserId);
        return localVarResp.getData();
    }

    /**
     * Get a user integration setting
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @return ApiResponse&lt;UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response> usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetWithHttpInfo(String userId, String integrationSettingsUserId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetValidateBeforeCall(userId, integrationSettingsUserId, null);
        Type localVarReturnType = new TypeToken<UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a user integration setting (asynchronously)
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetAsync(String userId, String integrationSettingsUserId, final ApiCallback<UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetValidateBeforeCall(userId, integrationSettingsUserId, _callback);
        Type localVarReturnType = new TypeToken<UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCall(String userId, String integrationSettingsUserId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}/integration_settings/{integration_settings_user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()))
            .replace("{" + "integration_settings_user_id" + "}", localVarApiClient.escapeString(integrationSettingsUserId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutValidateBeforeCall(String userId, String integrationSettingsUserId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(Async)");
        }

        // verify the required parameter 'integrationSettingsUserId' is set
        if (integrationSettingsUserId == null) {
            throw new ApiException("Missing the required parameter 'integrationSettingsUserId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(Async)");
        }

        return usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCall(userId, integrationSettingsUserId, _callback);

    }

    /**
     * Edit a user integration setting
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(String userId, String integrationSettingsUserId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutWithHttpInfo(userId, integrationSettingsUserId);
        return localVarResp.getData();
    }

    /**
     * Edit a user integration setting
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutWithHttpInfo(String userId, String integrationSettingsUserId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutValidateBeforeCall(userId, integrationSettingsUserId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit a user integration setting (asynchronously)
     * 
     * @param userId  (required)
     * @param integrationSettingsUserId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Users integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutAsync(String userId, String integrationSettingsUserId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutValidateBeforeCall(userId, integrationSettingsUserId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdIntegrationSettingsPost
     * @param userId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsPostCall(String userId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = companiesCompanyIdIntegrationSettingsPostRequest;

        // create path and map variables
        String localVarPath = "/users/{user_id}/integration_settings"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdIntegrationSettingsPostValidateBeforeCall(String userId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsPost(Async)");
        }

        return usersUserIdIntegrationSettingsPostCall(userId, companiesCompanyIdIntegrationSettingsPostRequest, _callback);

    }

    /**
     * Add a user integration setting
     * 
     * @param userId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @return CreateSuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public CreateSuccessResponse usersUserIdIntegrationSettingsPost(String userId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest) throws ApiException {
        ApiResponse<CreateSuccessResponse> localVarResp = usersUserIdIntegrationSettingsPostWithHttpInfo(userId, companiesCompanyIdIntegrationSettingsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add a user integration setting
     * 
     * @param userId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @return ApiResponse&lt;CreateSuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateSuccessResponse> usersUserIdIntegrationSettingsPostWithHttpInfo(String userId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsPostValidateBeforeCall(userId, companiesCompanyIdIntegrationSettingsPostRequest, null);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a user integration setting (asynchronously)
     * 
     * @param userId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdIntegrationSettingsPostAsync(String userId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest, final ApiCallback<CreateSuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdIntegrationSettingsPostValidateBeforeCall(userId, companiesCompanyIdIntegrationSettingsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdPut
     * @param userId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdPutCall(String userId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdPutValidateBeforeCall(String userId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdPut(Async)");
        }

        return usersUserIdPutCall(userId, _callback);

    }

    /**
     * Edit user
     * 
     * @param userId  (required)
     * @return ClockingRecordsClockingRecordIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdPut200Response usersUserIdPut(String userId) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdPut200Response> localVarResp = usersUserIdPutWithHttpInfo(userId);
        return localVarResp.getData();
    }

    /**
     * Edit user
     * 
     * @param userId  (required)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdPut200Response> usersUserIdPutWithHttpInfo(String userId) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdPutValidateBeforeCall(userId, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit user (asynchronously)
     * 
     * @param userId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdPutAsync(String userId, final ApiCallback<ClockingRecordsClockingRecordIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdPutValidateBeforeCall(userId, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for usersUserIdUploadImagePost
     * @param userId  (required)
     * @param image  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdUploadImagePostCall(String userId, File image, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/{user_id}/uploadImage"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (image != null) {
            localVarFormParams.put("image", image);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api_key", "X-Auth-Token" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call usersUserIdUploadImagePostValidateBeforeCall(String userId, File image, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling usersUserIdUploadImagePost(Async)");
        }

        return usersUserIdUploadImagePostCall(userId, image, _callback);

    }

    /**
     * Upload a new image to a user
     * 
     * @param userId  (required)
     * @param image  (optional)
     * @return CreateSuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public CreateSuccessResponse usersUserIdUploadImagePost(String userId, File image) throws ApiException {
        ApiResponse<CreateSuccessResponse> localVarResp = usersUserIdUploadImagePostWithHttpInfo(userId, image);
        return localVarResp.getData();
    }

    /**
     * Upload a new image to a user
     * 
     * @param userId  (required)
     * @param image  (optional)
     * @return ApiResponse&lt;CreateSuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateSuccessResponse> usersUserIdUploadImagePostWithHttpInfo(String userId, File image) throws ApiException {
        okhttp3.Call localVarCall = usersUserIdUploadImagePostValidateBeforeCall(userId, image, null);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Upload a new image to a user (asynchronously)
     * 
     * @param userId  (required)
     * @param image  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> User not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call usersUserIdUploadImagePostAsync(String userId, File image, final ApiCallback<CreateSuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = usersUserIdUploadImagePostValidateBeforeCall(userId, image, _callback);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
