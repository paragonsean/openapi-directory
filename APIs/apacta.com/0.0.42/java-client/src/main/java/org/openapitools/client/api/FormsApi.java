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


import org.openapitools.client.model.ClockingRecordsPost201Response;
import org.openapitools.client.model.EmptySuccessResponse;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.FormsFormIdGet200Response;
import org.openapitools.client.model.FormsGet200Response;
import org.openapitools.client.model.FormsPostRequest;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FormsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public FormsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public FormsApi(ApiClient apiClient) {
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
     * Build call for formsFormIdDelete
     * @param formId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsFormIdDeleteCall(String formId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forms/{form_id}"
            .replace("{" + "form_id" + "}", localVarApiClient.escapeString(formId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
    private okhttp3.Call formsFormIdDeleteValidateBeforeCall(String formId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'formId' is set
        if (formId == null) {
            throw new ApiException("Missing the required parameter 'formId' when calling formsFormIdDelete(Async)");
        }

        return formsFormIdDeleteCall(formId, _callback);

    }

    /**
     * Delete a form
     * You can only delete the forms that you&#39;ve submitted yourself
     * @param formId  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void formsFormIdDelete(String formId) throws ApiException {
        formsFormIdDeleteWithHttpInfo(formId);
    }

    /**
     * Delete a form
     * You can only delete the forms that you&#39;ve submitted yourself
     * @param formId  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> formsFormIdDeleteWithHttpInfo(String formId) throws ApiException {
        okhttp3.Call localVarCall = formsFormIdDeleteValidateBeforeCall(formId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a form (asynchronously)
     * You can only delete the forms that you&#39;ve submitted yourself
     * @param formId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsFormIdDeleteAsync(String formId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsFormIdDeleteValidateBeforeCall(formId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for formsFormIdGet
     * @param formId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsFormIdGetCall(String formId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forms/{form_id}"
            .replace("{" + "form_id" + "}", localVarApiClient.escapeString(formId.toString()));

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
    private okhttp3.Call formsFormIdGetValidateBeforeCall(String formId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'formId' is set
        if (formId == null) {
            throw new ApiException("Missing the required parameter 'formId' when calling formsFormIdGet(Async)");
        }

        return formsFormIdGetCall(formId, _callback);

    }

    /**
     * View form
     * 
     * @param formId  (required)
     * @return FormsFormIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public FormsFormIdGet200Response formsFormIdGet(String formId) throws ApiException {
        ApiResponse<FormsFormIdGet200Response> localVarResp = formsFormIdGetWithHttpInfo(formId);
        return localVarResp.getData();
    }

    /**
     * View form
     * 
     * @param formId  (required)
     * @return ApiResponse&lt;FormsFormIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FormsFormIdGet200Response> formsFormIdGetWithHttpInfo(String formId) throws ApiException {
        okhttp3.Call localVarCall = formsFormIdGetValidateBeforeCall(formId, null);
        Type localVarReturnType = new TypeToken<FormsFormIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * View form (asynchronously)
     * 
     * @param formId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsFormIdGetAsync(String formId, final ApiCallback<FormsFormIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsFormIdGetValidateBeforeCall(formId, _callback);
        Type localVarReturnType = new TypeToken<FormsFormIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for formsFormIdPut
     * @param formId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsFormIdPutCall(String formId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forms/{form_id}"
            .replace("{" + "form_id" + "}", localVarApiClient.escapeString(formId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
    private okhttp3.Call formsFormIdPutValidateBeforeCall(String formId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'formId' is set
        if (formId == null) {
            throw new ApiException("Missing the required parameter 'formId' when calling formsFormIdPut(Async)");
        }

        return formsFormIdPutCall(formId, _callback);

    }

    /**
     * Edit a form
     * 
     * @param formId  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void formsFormIdPut(String formId) throws ApiException {
        formsFormIdPutWithHttpInfo(formId);
    }

    /**
     * Edit a form
     * 
     * @param formId  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> formsFormIdPutWithHttpInfo(String formId) throws ApiException {
        okhttp3.Call localVarCall = formsFormIdPutValidateBeforeCall(formId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Edit a form (asynchronously)
     * 
     * @param formId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsFormIdPutAsync(String formId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsFormIdPutValidateBeforeCall(formId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for formsGet
     * @param extended Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60; (optional)
     * @param dateFrom Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60; (optional)
     * @param dateTo Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60; (optional)
     * @param show Used to show forms with trashed (optional)
     * @param projectId Used to filter on the &#x60;project_id&#x60; of the forms (optional)
     * @param createdById Used to filter on the &#x60;created_by_id&#x60; of the forms (optional)
     * @param formTemplateId Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array. (optional)
     * @param formTemplateType Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;] (optional)
     * @param employeeName Used to filter forms by user&#39;s first or last name (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsGetCall(String extended, String dateFrom, String dateTo, String show, UUID projectId, String createdById, List<UUID> formTemplateId, String formTemplateType, String employeeName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forms";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (extended != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("extended", extended));
        }

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (show != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("show", show));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
        }

        if (createdById != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("created_by_id", createdById));
        }

        if (formTemplateId != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "form_template_id", formTemplateId));
        }

        if (formTemplateType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("form_template_type", formTemplateType));
        }

        if (employeeName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("employee_name", employeeName));
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
    private okhttp3.Call formsGetValidateBeforeCall(String extended, String dateFrom, String dateTo, String show, UUID projectId, String createdById, List<UUID> formTemplateId, String formTemplateType, String employeeName, final ApiCallback _callback) throws ApiException {
        return formsGetCall(extended, dateFrom, dateTo, show, projectId, createdById, formTemplateId, formTemplateType, employeeName, _callback);

    }

    /**
     * Retrieve array of forms
     * 
     * @param extended Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60; (optional)
     * @param dateFrom Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60; (optional)
     * @param dateTo Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60; (optional)
     * @param show Used to show forms with trashed (optional)
     * @param projectId Used to filter on the &#x60;project_id&#x60; of the forms (optional)
     * @param createdById Used to filter on the &#x60;created_by_id&#x60; of the forms (optional)
     * @param formTemplateId Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array. (optional)
     * @param formTemplateType Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;] (optional)
     * @param employeeName Used to filter forms by user&#39;s first or last name (optional)
     * @return FormsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public FormsGet200Response formsGet(String extended, String dateFrom, String dateTo, String show, UUID projectId, String createdById, List<UUID> formTemplateId, String formTemplateType, String employeeName) throws ApiException {
        ApiResponse<FormsGet200Response> localVarResp = formsGetWithHttpInfo(extended, dateFrom, dateTo, show, projectId, createdById, formTemplateId, formTemplateType, employeeName);
        return localVarResp.getData();
    }

    /**
     * Retrieve array of forms
     * 
     * @param extended Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60; (optional)
     * @param dateFrom Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60; (optional)
     * @param dateTo Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60; (optional)
     * @param show Used to show forms with trashed (optional)
     * @param projectId Used to filter on the &#x60;project_id&#x60; of the forms (optional)
     * @param createdById Used to filter on the &#x60;created_by_id&#x60; of the forms (optional)
     * @param formTemplateId Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array. (optional)
     * @param formTemplateType Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;] (optional)
     * @param employeeName Used to filter forms by user&#39;s first or last name (optional)
     * @return ApiResponse&lt;FormsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FormsGet200Response> formsGetWithHttpInfo(String extended, String dateFrom, String dateTo, String show, UUID projectId, String createdById, List<UUID> formTemplateId, String formTemplateType, String employeeName) throws ApiException {
        okhttp3.Call localVarCall = formsGetValidateBeforeCall(extended, dateFrom, dateTo, show, projectId, createdById, formTemplateId, formTemplateType, employeeName, null);
        Type localVarReturnType = new TypeToken<FormsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve array of forms (asynchronously)
     * 
     * @param extended Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60; (optional)
     * @param dateFrom Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60; (optional)
     * @param dateTo Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60; (optional)
     * @param show Used to show forms with trashed (optional)
     * @param projectId Used to filter on the &#x60;project_id&#x60; of the forms (optional)
     * @param createdById Used to filter on the &#x60;created_by_id&#x60; of the forms (optional)
     * @param formTemplateId Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array. (optional)
     * @param formTemplateType Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;] (optional)
     * @param employeeName Used to filter forms by user&#39;s first or last name (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsGetAsync(String extended, String dateFrom, String dateTo, String show, UUID projectId, String createdById, List<UUID> formTemplateId, String formTemplateType, String employeeName, final ApiCallback<FormsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsGetValidateBeforeCall(extended, dateFrom, dateTo, show, projectId, createdById, formTemplateId, formTemplateType, employeeName, _callback);
        Type localVarReturnType = new TypeToken<FormsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for formsPost
     * @param formsPostRequest  (optional)
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
    public okhttp3.Call formsPostCall(FormsPostRequest formsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = formsPostRequest;

        // create path and map variables
        String localVarPath = "/forms";

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
    private okhttp3.Call formsPostValidateBeforeCall(FormsPostRequest formsPostRequest, final ApiCallback _callback) throws ApiException {
        return formsPostCall(formsPostRequest, _callback);

    }

    /**
     * Add new form
     * Used to add a form into the system
     * @param formsPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response formsPost(FormsPostRequest formsPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = formsPostWithHttpInfo(formsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add new form
     * Used to add a form into the system
     * @param formsPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> formsPostWithHttpInfo(FormsPostRequest formsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = formsPostValidateBeforeCall(formsPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add new form (asynchronously)
     * Used to add a form into the system
     * @param formsPostRequest  (optional)
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
    public okhttp3.Call formsPostAsync(FormsPostRequest formsPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsPostValidateBeforeCall(formsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for formsUndeleteFormIdGet
     * @param formId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsUndeleteFormIdGetCall(String formId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forms/undelete/{form_id}"
            .replace("{" + "form_id" + "}", localVarApiClient.escapeString(formId.toString()));

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
    private okhttp3.Call formsUndeleteFormIdGetValidateBeforeCall(String formId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'formId' is set
        if (formId == null) {
            throw new ApiException("Missing the required parameter 'formId' when calling formsUndeleteFormIdGet(Async)");
        }

        return formsUndeleteFormIdGetCall(formId, _callback);

    }

    /**
     * Undelete form and related entities to it
     * 
     * @param formId  (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse formsUndeleteFormIdGet(String formId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = formsUndeleteFormIdGetWithHttpInfo(formId);
        return localVarResp.getData();
    }

    /**
     * Undelete form and related entities to it
     * 
     * @param formId  (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> formsUndeleteFormIdGetWithHttpInfo(String formId) throws ApiException {
        okhttp3.Call localVarCall = formsUndeleteFormIdGetValidateBeforeCall(formId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Undelete form and related entities to it (asynchronously)
     * 
     * @param formId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsUndeleteFormIdGetAsync(String formId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsUndeleteFormIdGetValidateBeforeCall(formId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for formsViewTimeFormPdfFormIdGet
     * @param formId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsViewTimeFormPdfFormIdGetCall(String formId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/forms/view_time_form_pdf/{form_id}"
            .replace("{" + "form_id" + "}", localVarApiClient.escapeString(formId.toString()));

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
    private okhttp3.Call formsViewTimeFormPdfFormIdGetValidateBeforeCall(String formId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'formId' is set
        if (formId == null) {
            throw new ApiException("Missing the required parameter 'formId' when calling formsViewTimeFormPdfFormIdGet(Async)");
        }

        return formsViewTimeFormPdfFormIdGetCall(formId, _callback);

    }

    /**
     * Generate time form pdf
     * 
     * @param formId  (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse formsViewTimeFormPdfFormIdGet(String formId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = formsViewTimeFormPdfFormIdGetWithHttpInfo(formId);
        return localVarResp.getData();
    }

    /**
     * Generate time form pdf
     * 
     * @param formId  (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> formsViewTimeFormPdfFormIdGetWithHttpInfo(String formId) throws ApiException {
        okhttp3.Call localVarCall = formsViewTimeFormPdfFormIdGetValidateBeforeCall(formId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Generate time form pdf (asynchronously)
     * 
     * @param formId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call formsViewTimeFormPdfFormIdGetAsync(String formId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = formsViewTimeFormPdfFormIdGetValidateBeforeCall(formId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
