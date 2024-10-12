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
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.ExpenseFilesExpenseFileIdPut200Response;
import org.openapitools.client.model.MaterialsMaterialIdRentalsCheckoutPostRequest;
import org.openapitools.client.model.MaterialsMaterialIdRentalsGet200Response;
import org.openapitools.client.model.MaterialsMaterialIdRentalsMaterialRentalIdGet200Response;
import org.openapitools.client.model.MaterialsMaterialIdRentalsPostRequest;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MaterialRentalsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MaterialRentalsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MaterialRentalsApi(ApiClient apiClient) {
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
     * Build call for materialsMaterialIdRentalsCheckoutPost
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsCheckoutPostRequest  (optional)
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
    public okhttp3.Call materialsMaterialIdRentalsCheckoutPostCall(String materialId, MaterialsMaterialIdRentalsCheckoutPostRequest materialsMaterialIdRentalsCheckoutPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = materialsMaterialIdRentalsCheckoutPostRequest;

        // create path and map variables
        String localVarPath = "/materials/{material_id}/rentals/checkout/"
            .replace("{" + "material_id" + "}", localVarApiClient.escapeString(materialId.toString()));

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
    private okhttp3.Call materialsMaterialIdRentalsCheckoutPostValidateBeforeCall(String materialId, MaterialsMaterialIdRentalsCheckoutPostRequest materialsMaterialIdRentalsCheckoutPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'materialId' is set
        if (materialId == null) {
            throw new ApiException("Missing the required parameter 'materialId' when calling materialsMaterialIdRentalsCheckoutPost(Async)");
        }

        return materialsMaterialIdRentalsCheckoutPostCall(materialId, materialsMaterialIdRentalsCheckoutPostRequest, _callback);

    }

    /**
     * Checkout material rental
     * 
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsCheckoutPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response materialsMaterialIdRentalsCheckoutPost(String materialId, MaterialsMaterialIdRentalsCheckoutPostRequest materialsMaterialIdRentalsCheckoutPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = materialsMaterialIdRentalsCheckoutPostWithHttpInfo(materialId, materialsMaterialIdRentalsCheckoutPostRequest);
        return localVarResp.getData();
    }

    /**
     * Checkout material rental
     * 
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsCheckoutPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> materialsMaterialIdRentalsCheckoutPostWithHttpInfo(String materialId, MaterialsMaterialIdRentalsCheckoutPostRequest materialsMaterialIdRentalsCheckoutPostRequest) throws ApiException {
        okhttp3.Call localVarCall = materialsMaterialIdRentalsCheckoutPostValidateBeforeCall(materialId, materialsMaterialIdRentalsCheckoutPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Checkout material rental (asynchronously)
     * 
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsCheckoutPostRequest  (optional)
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
    public okhttp3.Call materialsMaterialIdRentalsCheckoutPostAsync(String materialId, MaterialsMaterialIdRentalsCheckoutPostRequest materialsMaterialIdRentalsCheckoutPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = materialsMaterialIdRentalsCheckoutPostValidateBeforeCall(materialId, materialsMaterialIdRentalsCheckoutPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for materialsMaterialIdRentalsGet
     * @param materialId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call materialsMaterialIdRentalsGetCall(String materialId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/materials/{material_id}/rentals/"
            .replace("{" + "material_id" + "}", localVarApiClient.escapeString(materialId.toString()));

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
    private okhttp3.Call materialsMaterialIdRentalsGetValidateBeforeCall(String materialId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'materialId' is set
        if (materialId == null) {
            throw new ApiException("Missing the required parameter 'materialId' when calling materialsMaterialIdRentalsGet(Async)");
        }

        return materialsMaterialIdRentalsGetCall(materialId, _callback);

    }

    /**
     * Show list of rentals for specific material
     * 
     * @param materialId  (required)
     * @return MaterialsMaterialIdRentalsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public MaterialsMaterialIdRentalsGet200Response materialsMaterialIdRentalsGet(String materialId) throws ApiException {
        ApiResponse<MaterialsMaterialIdRentalsGet200Response> localVarResp = materialsMaterialIdRentalsGetWithHttpInfo(materialId);
        return localVarResp.getData();
    }

    /**
     * Show list of rentals for specific material
     * 
     * @param materialId  (required)
     * @return ApiResponse&lt;MaterialsMaterialIdRentalsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MaterialsMaterialIdRentalsGet200Response> materialsMaterialIdRentalsGetWithHttpInfo(String materialId) throws ApiException {
        okhttp3.Call localVarCall = materialsMaterialIdRentalsGetValidateBeforeCall(materialId, null);
        Type localVarReturnType = new TypeToken<MaterialsMaterialIdRentalsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show list of rentals for specific material (asynchronously)
     * 
     * @param materialId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call materialsMaterialIdRentalsGetAsync(String materialId, final ApiCallback<MaterialsMaterialIdRentalsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = materialsMaterialIdRentalsGetValidateBeforeCall(materialId, _callback);
        Type localVarReturnType = new TypeToken<MaterialsMaterialIdRentalsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for materialsMaterialIdRentalsMaterialRentalIdDelete
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdDeleteCall(UUID materialId, UUID materialRentalId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/materials/{material_id}/rentals/{material_rental_id}/"
            .replace("{" + "material_id" + "}", localVarApiClient.escapeString(materialId.toString()))
            .replace("{" + "material_rental_id" + "}", localVarApiClient.escapeString(materialRentalId.toString()));

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
    private okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdDeleteValidateBeforeCall(UUID materialId, UUID materialRentalId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'materialId' is set
        if (materialId == null) {
            throw new ApiException("Missing the required parameter 'materialId' when calling materialsMaterialIdRentalsMaterialRentalIdDelete(Async)");
        }

        // verify the required parameter 'materialRentalId' is set
        if (materialRentalId == null) {
            throw new ApiException("Missing the required parameter 'materialRentalId' when calling materialsMaterialIdRentalsMaterialRentalIdDelete(Async)");
        }

        return materialsMaterialIdRentalsMaterialRentalIdDeleteCall(materialId, materialRentalId, _callback);

    }

    /**
     * Delete material rental
     * Delete rental for material
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response materialsMaterialIdRentalsMaterialRentalIdDelete(UUID materialId, UUID materialRentalId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = materialsMaterialIdRentalsMaterialRentalIdDeleteWithHttpInfo(materialId, materialRentalId);
        return localVarResp.getData();
    }

    /**
     * Delete material rental
     * Delete rental for material
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> materialsMaterialIdRentalsMaterialRentalIdDeleteWithHttpInfo(UUID materialId, UUID materialRentalId) throws ApiException {
        okhttp3.Call localVarCall = materialsMaterialIdRentalsMaterialRentalIdDeleteValidateBeforeCall(materialId, materialRentalId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete material rental (asynchronously)
     * Delete rental for material
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdDeleteAsync(UUID materialId, UUID materialRentalId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = materialsMaterialIdRentalsMaterialRentalIdDeleteValidateBeforeCall(materialId, materialRentalId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for materialsMaterialIdRentalsMaterialRentalIdGet
     * @param materialId  (required)
     * @param materialRentalId  (required)
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
    public okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdGetCall(String materialId, String materialRentalId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/materials/{material_id}/rentals/{material_rental_id}/"
            .replace("{" + "material_id" + "}", localVarApiClient.escapeString(materialId.toString()))
            .replace("{" + "material_rental_id" + "}", localVarApiClient.escapeString(materialRentalId.toString()));

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
    private okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdGetValidateBeforeCall(String materialId, String materialRentalId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'materialId' is set
        if (materialId == null) {
            throw new ApiException("Missing the required parameter 'materialId' when calling materialsMaterialIdRentalsMaterialRentalIdGet(Async)");
        }

        // verify the required parameter 'materialRentalId' is set
        if (materialRentalId == null) {
            throw new ApiException("Missing the required parameter 'materialRentalId' when calling materialsMaterialIdRentalsMaterialRentalIdGet(Async)");
        }

        return materialsMaterialIdRentalsMaterialRentalIdGetCall(materialId, materialRentalId, _callback);

    }

    /**
     * Show rental foor materi
     * 
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @return MaterialsMaterialIdRentalsMaterialRentalIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public MaterialsMaterialIdRentalsMaterialRentalIdGet200Response materialsMaterialIdRentalsMaterialRentalIdGet(String materialId, String materialRentalId) throws ApiException {
        ApiResponse<MaterialsMaterialIdRentalsMaterialRentalIdGet200Response> localVarResp = materialsMaterialIdRentalsMaterialRentalIdGetWithHttpInfo(materialId, materialRentalId);
        return localVarResp.getData();
    }

    /**
     * Show rental foor materi
     * 
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @return ApiResponse&lt;MaterialsMaterialIdRentalsMaterialRentalIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MaterialsMaterialIdRentalsMaterialRentalIdGet200Response> materialsMaterialIdRentalsMaterialRentalIdGetWithHttpInfo(String materialId, String materialRentalId) throws ApiException {
        okhttp3.Call localVarCall = materialsMaterialIdRentalsMaterialRentalIdGetValidateBeforeCall(materialId, materialRentalId, null);
        Type localVarReturnType = new TypeToken<MaterialsMaterialIdRentalsMaterialRentalIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show rental foor materi (asynchronously)
     * 
     * @param materialId  (required)
     * @param materialRentalId  (required)
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
    public okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdGetAsync(String materialId, String materialRentalId, final ApiCallback<MaterialsMaterialIdRentalsMaterialRentalIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = materialsMaterialIdRentalsMaterialRentalIdGetValidateBeforeCall(materialId, materialRentalId, _callback);
        Type localVarReturnType = new TypeToken<MaterialsMaterialIdRentalsMaterialRentalIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for materialsMaterialIdRentalsMaterialRentalIdPut
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdPutCall(UUID materialId, UUID materialRentalId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/materials/{material_id}/rentals/{material_rental_id}/"
            .replace("{" + "material_id" + "}", localVarApiClient.escapeString(materialId.toString()))
            .replace("{" + "material_rental_id" + "}", localVarApiClient.escapeString(materialRentalId.toString()));

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
    private okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdPutValidateBeforeCall(UUID materialId, UUID materialRentalId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'materialId' is set
        if (materialId == null) {
            throw new ApiException("Missing the required parameter 'materialId' when calling materialsMaterialIdRentalsMaterialRentalIdPut(Async)");
        }

        // verify the required parameter 'materialRentalId' is set
        if (materialRentalId == null) {
            throw new ApiException("Missing the required parameter 'materialRentalId' when calling materialsMaterialIdRentalsMaterialRentalIdPut(Async)");
        }

        return materialsMaterialIdRentalsMaterialRentalIdPutCall(materialId, materialRentalId, _callback);

    }

    /**
     * Edit material rental
     * Edit material rental
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response materialsMaterialIdRentalsMaterialRentalIdPut(UUID materialId, UUID materialRentalId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = materialsMaterialIdRentalsMaterialRentalIdPutWithHttpInfo(materialId, materialRentalId);
        return localVarResp.getData();
    }

    /**
     * Edit material rental
     * Edit material rental
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> materialsMaterialIdRentalsMaterialRentalIdPutWithHttpInfo(UUID materialId, UUID materialRentalId) throws ApiException {
        okhttp3.Call localVarCall = materialsMaterialIdRentalsMaterialRentalIdPutValidateBeforeCall(materialId, materialRentalId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit material rental (asynchronously)
     * Edit material rental
     * @param materialId  (required)
     * @param materialRentalId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call materialsMaterialIdRentalsMaterialRentalIdPutAsync(UUID materialId, UUID materialRentalId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = materialsMaterialIdRentalsMaterialRentalIdPutValidateBeforeCall(materialId, materialRentalId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for materialsMaterialIdRentalsPost
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsPostRequest  (optional)
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
    public okhttp3.Call materialsMaterialIdRentalsPostCall(String materialId, MaterialsMaterialIdRentalsPostRequest materialsMaterialIdRentalsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = materialsMaterialIdRentalsPostRequest;

        // create path and map variables
        String localVarPath = "/materials/{material_id}/rentals/"
            .replace("{" + "material_id" + "}", localVarApiClient.escapeString(materialId.toString()));

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
    private okhttp3.Call materialsMaterialIdRentalsPostValidateBeforeCall(String materialId, MaterialsMaterialIdRentalsPostRequest materialsMaterialIdRentalsPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'materialId' is set
        if (materialId == null) {
            throw new ApiException("Missing the required parameter 'materialId' when calling materialsMaterialIdRentalsPost(Async)");
        }

        return materialsMaterialIdRentalsPostCall(materialId, materialsMaterialIdRentalsPostRequest, _callback);

    }

    /**
     * Add material rental
     * 
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response materialsMaterialIdRentalsPost(String materialId, MaterialsMaterialIdRentalsPostRequest materialsMaterialIdRentalsPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = materialsMaterialIdRentalsPostWithHttpInfo(materialId, materialsMaterialIdRentalsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add material rental
     * 
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> materialsMaterialIdRentalsPostWithHttpInfo(String materialId, MaterialsMaterialIdRentalsPostRequest materialsMaterialIdRentalsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = materialsMaterialIdRentalsPostValidateBeforeCall(materialId, materialsMaterialIdRentalsPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add material rental (asynchronously)
     * 
     * @param materialId  (required)
     * @param materialsMaterialIdRentalsPostRequest  (optional)
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
    public okhttp3.Call materialsMaterialIdRentalsPostAsync(String materialId, MaterialsMaterialIdRentalsPostRequest materialsMaterialIdRentalsPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = materialsMaterialIdRentalsPostValidateBeforeCall(materialId, materialsMaterialIdRentalsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
