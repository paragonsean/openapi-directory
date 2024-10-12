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
import org.openapitools.client.model.ClockingRecordsPost201Response;
import org.openapitools.client.model.EmptySuccessResponse;
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.ExpensesExpenseIdGet200Response;
import org.openapitools.client.model.ExpensesGet200Response;
import org.openapitools.client.model.ExpensesHighestAmountGet200Response;
import org.openapitools.client.model.ExpensesPostRequest;
import java.time.LocalDate;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ExpensesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ExpensesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ExpensesApi(ApiClient apiClient) {
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
     * Build call for bulkDeleteExpenses
     * @param bulkActionRequestBody expense ids (required)
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
    public okhttp3.Call bulkDeleteExpensesCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses/bulkDelete";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call bulkDeleteExpensesValidateBeforeCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'bulkActionRequestBody' is set
        if (bulkActionRequestBody == null) {
            throw new ApiException("Missing the required parameter 'bulkActionRequestBody' when calling bulkDeleteExpenses(Async)");
        }

        return bulkDeleteExpensesCall(bulkActionRequestBody, _callback);

    }

    /**
     * Bulk delete expenses
     * 
     * @param bulkActionRequestBody expense ids (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse bulkDeleteExpenses(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = bulkDeleteExpensesWithHttpInfo(bulkActionRequestBody);
        return localVarResp.getData();
    }

    /**
     * Bulk delete expenses
     * 
     * @param bulkActionRequestBody expense ids (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> bulkDeleteExpensesWithHttpInfo(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        okhttp3.Call localVarCall = bulkDeleteExpensesValidateBeforeCall(bulkActionRequestBody, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Bulk delete expenses (asynchronously)
     * 
     * @param bulkActionRequestBody expense ids (required)
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
    public okhttp3.Call bulkDeleteExpensesAsync(BulkActionRequestBody bulkActionRequestBody, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = bulkDeleteExpensesValidateBeforeCall(bulkActionRequestBody, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for expensesExpenseIdDelete
     * @param expenseId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesExpenseIdDeleteCall(String expenseId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses/{expense_id}"
            .replace("{" + "expense_id" + "}", localVarApiClient.escapeString(expenseId.toString()));

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
    private okhttp3.Call expensesExpenseIdDeleteValidateBeforeCall(String expenseId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'expenseId' is set
        if (expenseId == null) {
            throw new ApiException("Missing the required parameter 'expenseId' when calling expensesExpenseIdDelete(Async)");
        }

        return expensesExpenseIdDeleteCall(expenseId, _callback);

    }

    /**
     * Delete expense
     * 
     * @param expenseId  (required)
     * @return ExpensesExpenseIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpensesExpenseIdGet200Response expensesExpenseIdDelete(String expenseId) throws ApiException {
        ApiResponse<ExpensesExpenseIdGet200Response> localVarResp = expensesExpenseIdDeleteWithHttpInfo(expenseId);
        return localVarResp.getData();
    }

    /**
     * Delete expense
     * 
     * @param expenseId  (required)
     * @return ApiResponse&lt;ExpensesExpenseIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpensesExpenseIdGet200Response> expensesExpenseIdDeleteWithHttpInfo(String expenseId) throws ApiException {
        okhttp3.Call localVarCall = expensesExpenseIdDeleteValidateBeforeCall(expenseId, null);
        Type localVarReturnType = new TypeToken<ExpensesExpenseIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete expense (asynchronously)
     * 
     * @param expenseId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesExpenseIdDeleteAsync(String expenseId, final ApiCallback<ExpensesExpenseIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = expensesExpenseIdDeleteValidateBeforeCall(expenseId, _callback);
        Type localVarReturnType = new TypeToken<ExpensesExpenseIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for expensesExpenseIdGet
     * @param expenseId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesExpenseIdGetCall(String expenseId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses/{expense_id}"
            .replace("{" + "expense_id" + "}", localVarApiClient.escapeString(expenseId.toString()));

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
    private okhttp3.Call expensesExpenseIdGetValidateBeforeCall(String expenseId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'expenseId' is set
        if (expenseId == null) {
            throw new ApiException("Missing the required parameter 'expenseId' when calling expensesExpenseIdGet(Async)");
        }

        return expensesExpenseIdGetCall(expenseId, _callback);

    }

    /**
     * Show expense
     * 
     * @param expenseId  (required)
     * @return ExpensesExpenseIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ExpensesExpenseIdGet200Response expensesExpenseIdGet(String expenseId) throws ApiException {
        ApiResponse<ExpensesExpenseIdGet200Response> localVarResp = expensesExpenseIdGetWithHttpInfo(expenseId);
        return localVarResp.getData();
    }

    /**
     * Show expense
     * 
     * @param expenseId  (required)
     * @return ApiResponse&lt;ExpensesExpenseIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpensesExpenseIdGet200Response> expensesExpenseIdGetWithHttpInfo(String expenseId) throws ApiException {
        okhttp3.Call localVarCall = expensesExpenseIdGetValidateBeforeCall(expenseId, null);
        Type localVarReturnType = new TypeToken<ExpensesExpenseIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show expense (asynchronously)
     * 
     * @param expenseId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesExpenseIdGetAsync(String expenseId, final ApiCallback<ExpensesExpenseIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = expensesExpenseIdGetValidateBeforeCall(expenseId, _callback);
        Type localVarReturnType = new TypeToken<ExpensesExpenseIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for expensesExpenseIdPut
     * @param expenseId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesExpenseIdPutCall(String expenseId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses/{expense_id}"
            .replace("{" + "expense_id" + "}", localVarApiClient.escapeString(expenseId.toString()));

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
    private okhttp3.Call expensesExpenseIdPutValidateBeforeCall(String expenseId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'expenseId' is set
        if (expenseId == null) {
            throw new ApiException("Missing the required parameter 'expenseId' when calling expensesExpenseIdPut(Async)");
        }

        return expensesExpenseIdPutCall(expenseId, _callback);

    }

    /**
     * Edit expense
     * 
     * @param expenseId  (required)
     * @return ExpensesExpenseIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpensesExpenseIdGet200Response expensesExpenseIdPut(String expenseId) throws ApiException {
        ApiResponse<ExpensesExpenseIdGet200Response> localVarResp = expensesExpenseIdPutWithHttpInfo(expenseId);
        return localVarResp.getData();
    }

    /**
     * Edit expense
     * 
     * @param expenseId  (required)
     * @return ApiResponse&lt;ExpensesExpenseIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpensesExpenseIdGet200Response> expensesExpenseIdPutWithHttpInfo(String expenseId) throws ApiException {
        okhttp3.Call localVarCall = expensesExpenseIdPutValidateBeforeCall(expenseId, null);
        Type localVarReturnType = new TypeToken<ExpensesExpenseIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit expense (asynchronously)
     * 
     * @param expenseId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesExpenseIdPutAsync(String expenseId, final ApiCallback<ExpensesExpenseIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = expensesExpenseIdPutValidateBeforeCall(expenseId, _callback);
        Type localVarReturnType = new TypeToken<ExpensesExpenseIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for expensesGet
     * @param createdById  (optional)
     * @param companyId  (optional)
     * @param contactId  (optional)
     * @param projectId  (optional)
     * @param dueDate Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records] (optional)
     * @param gtCreated Created after date (optional)
     * @param ltCreated Created before date (optional)
     * @param status Filter by status identifier. [null&#x3D;all records] (optional)
     * @param isImported  (optional, default to true)
     * @param minAmount Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60; (optional)
     * @param maxAmount Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60; (optional)
     * @param projects You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60; (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesGetCall(UUID createdById, UUID companyId, UUID contactId, UUID projectId, String dueDate, LocalDate gtCreated, LocalDate ltCreated, String status, Boolean isImported, Float minAmount, Float maxAmount, String projects, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (createdById != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("created_by_id", createdById));
        }

        if (companyId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("company_id", companyId));
        }

        if (contactId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("contact_id", contactId));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
        }

        if (dueDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("due_date", dueDate));
        }

        if (gtCreated != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("gt_created", gtCreated));
        }

        if (ltCreated != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lt_created", ltCreated));
        }

        if (status != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("status", status));
        }

        if (isImported != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("is_imported", isImported));
        }

        if (minAmount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("min_amount", minAmount));
        }

        if (maxAmount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("max_amount", maxAmount));
        }

        if (projects != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("projects", projects));
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
    private okhttp3.Call expensesGetValidateBeforeCall(UUID createdById, UUID companyId, UUID contactId, UUID projectId, String dueDate, LocalDate gtCreated, LocalDate ltCreated, String status, Boolean isImported, Float minAmount, Float maxAmount, String projects, final ApiCallback _callback) throws ApiException {
        return expensesGetCall(createdById, companyId, contactId, projectId, dueDate, gtCreated, ltCreated, status, isImported, minAmount, maxAmount, projects, _callback);

    }

    /**
     * Show list of expenses
     * 
     * @param createdById  (optional)
     * @param companyId  (optional)
     * @param contactId  (optional)
     * @param projectId  (optional)
     * @param dueDate Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records] (optional)
     * @param gtCreated Created after date (optional)
     * @param ltCreated Created before date (optional)
     * @param status Filter by status identifier. [null&#x3D;all records] (optional)
     * @param isImported  (optional, default to true)
     * @param minAmount Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60; (optional)
     * @param maxAmount Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60; (optional)
     * @param projects You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60; (optional)
     * @return ExpensesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpensesGet200Response expensesGet(UUID createdById, UUID companyId, UUID contactId, UUID projectId, String dueDate, LocalDate gtCreated, LocalDate ltCreated, String status, Boolean isImported, Float minAmount, Float maxAmount, String projects) throws ApiException {
        ApiResponse<ExpensesGet200Response> localVarResp = expensesGetWithHttpInfo(createdById, companyId, contactId, projectId, dueDate, gtCreated, ltCreated, status, isImported, minAmount, maxAmount, projects);
        return localVarResp.getData();
    }

    /**
     * Show list of expenses
     * 
     * @param createdById  (optional)
     * @param companyId  (optional)
     * @param contactId  (optional)
     * @param projectId  (optional)
     * @param dueDate Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records] (optional)
     * @param gtCreated Created after date (optional)
     * @param ltCreated Created before date (optional)
     * @param status Filter by status identifier. [null&#x3D;all records] (optional)
     * @param isImported  (optional, default to true)
     * @param minAmount Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60; (optional)
     * @param maxAmount Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60; (optional)
     * @param projects You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60; (optional)
     * @return ApiResponse&lt;ExpensesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpensesGet200Response> expensesGetWithHttpInfo(UUID createdById, UUID companyId, UUID contactId, UUID projectId, String dueDate, LocalDate gtCreated, LocalDate ltCreated, String status, Boolean isImported, Float minAmount, Float maxAmount, String projects) throws ApiException {
        okhttp3.Call localVarCall = expensesGetValidateBeforeCall(createdById, companyId, contactId, projectId, dueDate, gtCreated, ltCreated, status, isImported, minAmount, maxAmount, projects, null);
        Type localVarReturnType = new TypeToken<ExpensesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show list of expenses (asynchronously)
     * 
     * @param createdById  (optional)
     * @param companyId  (optional)
     * @param contactId  (optional)
     * @param projectId  (optional)
     * @param dueDate Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records] (optional)
     * @param gtCreated Created after date (optional)
     * @param ltCreated Created before date (optional)
     * @param status Filter by status identifier. [null&#x3D;all records] (optional)
     * @param isImported  (optional, default to true)
     * @param minAmount Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60; (optional)
     * @param maxAmount Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60; (optional)
     * @param projects You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60; (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesGetAsync(UUID createdById, UUID companyId, UUID contactId, UUID projectId, String dueDate, LocalDate gtCreated, LocalDate ltCreated, String status, Boolean isImported, Float minAmount, Float maxAmount, String projects, final ApiCallback<ExpensesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = expensesGetValidateBeforeCall(createdById, companyId, contactId, projectId, dueDate, gtCreated, ltCreated, status, isImported, minAmount, maxAmount, projects, _callback);
        Type localVarReturnType = new TypeToken<ExpensesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for expensesHighestAmountGet
     * @param gtCreated Used to filter time range (required)
     * @param ltCreated Used to filter time range (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesHighestAmountGetCall(LocalDate gtCreated, LocalDate ltCreated, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses/highest_amount";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (gtCreated != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("gt_created", gtCreated));
        }

        if (ltCreated != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("lt_created", ltCreated));
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
    private okhttp3.Call expensesHighestAmountGetValidateBeforeCall(LocalDate gtCreated, LocalDate ltCreated, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'gtCreated' is set
        if (gtCreated == null) {
            throw new ApiException("Missing the required parameter 'gtCreated' when calling expensesHighestAmountGet(Async)");
        }

        // verify the required parameter 'ltCreated' is set
        if (ltCreated == null) {
            throw new ApiException("Missing the required parameter 'ltCreated' when calling expensesHighestAmountGet(Async)");
        }

        return expensesHighestAmountGetCall(gtCreated, ltCreated, _callback);

    }

    /**
     * Show highest Expense amount(&#x60;total_selling_price&#x60;)
     * 
     * @param gtCreated Used to filter time range (required)
     * @param ltCreated Used to filter time range (required)
     * @return ExpensesHighestAmountGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpensesHighestAmountGet200Response expensesHighestAmountGet(LocalDate gtCreated, LocalDate ltCreated) throws ApiException {
        ApiResponse<ExpensesHighestAmountGet200Response> localVarResp = expensesHighestAmountGetWithHttpInfo(gtCreated, ltCreated);
        return localVarResp.getData();
    }

    /**
     * Show highest Expense amount(&#x60;total_selling_price&#x60;)
     * 
     * @param gtCreated Used to filter time range (required)
     * @param ltCreated Used to filter time range (required)
     * @return ApiResponse&lt;ExpensesHighestAmountGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpensesHighestAmountGet200Response> expensesHighestAmountGetWithHttpInfo(LocalDate gtCreated, LocalDate ltCreated) throws ApiException {
        okhttp3.Call localVarCall = expensesHighestAmountGetValidateBeforeCall(gtCreated, ltCreated, null);
        Type localVarReturnType = new TypeToken<ExpensesHighestAmountGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show highest Expense amount(&#x60;total_selling_price&#x60;) (asynchronously)
     * 
     * @param gtCreated Used to filter time range (required)
     * @param ltCreated Used to filter time range (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call expensesHighestAmountGetAsync(LocalDate gtCreated, LocalDate ltCreated, final ApiCallback<ExpensesHighestAmountGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = expensesHighestAmountGetValidateBeforeCall(gtCreated, ltCreated, _callback);
        Type localVarReturnType = new TypeToken<ExpensesHighestAmountGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for expensesPost
     * @param expensesPostRequest  (optional)
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
    public okhttp3.Call expensesPostCall(ExpensesPostRequest expensesPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = expensesPostRequest;

        // create path and map variables
        String localVarPath = "/expenses";

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
    private okhttp3.Call expensesPostValidateBeforeCall(ExpensesPostRequest expensesPostRequest, final ApiCallback _callback) throws ApiException {
        return expensesPostCall(expensesPostRequest, _callback);

    }

    /**
     * Add line to expense
     * 
     * @param expensesPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response expensesPost(ExpensesPostRequest expensesPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = expensesPostWithHttpInfo(expensesPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add line to expense
     * 
     * @param expensesPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> expensesPostWithHttpInfo(ExpensesPostRequest expensesPostRequest) throws ApiException {
        okhttp3.Call localVarCall = expensesPostValidateBeforeCall(expensesPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add line to expense (asynchronously)
     * 
     * @param expensesPostRequest  (optional)
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
    public okhttp3.Call expensesPostAsync(ExpensesPostRequest expensesPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = expensesPostValidateBeforeCall(expensesPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for sendEmailsExpenses
     * @param bulkActionRequestBody expense ids (required)
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
    public okhttp3.Call sendEmailsExpensesCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/expenses/sendEmails";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call sendEmailsExpensesValidateBeforeCall(BulkActionRequestBody bulkActionRequestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'bulkActionRequestBody' is set
        if (bulkActionRequestBody == null) {
            throw new ApiException("Missing the required parameter 'bulkActionRequestBody' when calling sendEmailsExpenses(Async)");
        }

        return sendEmailsExpensesCall(bulkActionRequestBody, _callback);

    }

    /**
     * Bulk delete expenses
     * 
     * @param bulkActionRequestBody expense ids (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse sendEmailsExpenses(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = sendEmailsExpensesWithHttpInfo(bulkActionRequestBody);
        return localVarResp.getData();
    }

    /**
     * Bulk delete expenses
     * 
     * @param bulkActionRequestBody expense ids (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> sendEmailsExpensesWithHttpInfo(BulkActionRequestBody bulkActionRequestBody) throws ApiException {
        okhttp3.Call localVarCall = sendEmailsExpensesValidateBeforeCall(bulkActionRequestBody, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Bulk delete expenses (asynchronously)
     * 
     * @param bulkActionRequestBody expense ids (required)
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
    public okhttp3.Call sendEmailsExpensesAsync(BulkActionRequestBody bulkActionRequestBody, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = sendEmailsExpensesValidateBeforeCall(bulkActionRequestBody, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
