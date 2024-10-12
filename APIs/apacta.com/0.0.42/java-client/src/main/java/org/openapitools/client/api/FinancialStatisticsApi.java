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


import org.openapitools.client.model.FinancialStatisticsWorkingHoursGet200Response;
import org.openapitools.client.model.GetExpensesSalesPrice200Response;
import org.openapitools.client.model.GetFinancialStatistics200Response;
import org.openapitools.client.model.GetFinancialStatisticsOverview200Response;
import org.openapitools.client.model.GetInvoicedAmount200Response;
import org.openapitools.client.model.GetMargin200Response;
import org.openapitools.client.model.GetMaterialRentalsCostPrice200Response;
import org.openapitools.client.model.GetProductsCostPrice200Response;
import java.time.LocalDate;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FinancialStatisticsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public FinancialStatisticsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public FinancialStatisticsApi(ApiClient apiClient) {
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
     * Build call for financialStatisticsWorkingHoursGet
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call financialStatisticsWorkingHoursGetCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/workingHours";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call financialStatisticsWorkingHoursGetValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return financialStatisticsWorkingHoursGetCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get Total working hours grouped by time entry type
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return FinancialStatisticsWorkingHoursGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public FinancialStatisticsWorkingHoursGet200Response financialStatisticsWorkingHoursGet(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<FinancialStatisticsWorkingHoursGet200Response> localVarResp = financialStatisticsWorkingHoursGetWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get Total working hours grouped by time entry type
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;FinancialStatisticsWorkingHoursGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<FinancialStatisticsWorkingHoursGet200Response> financialStatisticsWorkingHoursGetWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = financialStatisticsWorkingHoursGetValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<FinancialStatisticsWorkingHoursGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Total working hours grouped by time entry type (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call financialStatisticsWorkingHoursGetAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<FinancialStatisticsWorkingHoursGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = financialStatisticsWorkingHoursGetValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<FinancialStatisticsWorkingHoursGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getExpensesSalesPrice
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getExpensesSalesPriceCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/expensesSalesPrice";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call getExpensesSalesPriceValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return getExpensesSalesPriceCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get expenses sales price
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return GetExpensesSalesPrice200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetExpensesSalesPrice200Response getExpensesSalesPrice(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<GetExpensesSalesPrice200Response> localVarResp = getExpensesSalesPriceWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get expenses sales price
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;GetExpensesSalesPrice200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetExpensesSalesPrice200Response> getExpensesSalesPriceWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = getExpensesSalesPriceValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<GetExpensesSalesPrice200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get expenses sales price (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getExpensesSalesPriceAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<GetExpensesSalesPrice200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getExpensesSalesPriceValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetExpensesSalesPrice200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFinancialStatistics
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param projectStatusIds  (optional)
     * @param onlyNotInvoiced  (optional)
     * @param details  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFinancialStatisticsCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, UUID projectStatusIds, Boolean onlyNotInvoiced, Boolean details, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
        }

        if (projectStatusIds != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_status_ids[]", projectStatusIds));
        }

        if (onlyNotInvoiced != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("only_not_invoiced", onlyNotInvoiced));
        }

        if (details != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("details", details));
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
    private okhttp3.Call getFinancialStatisticsValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, UUID projectStatusIds, Boolean onlyNotInvoiced, Boolean details, final ApiCallback _callback) throws ApiException {
        return getFinancialStatisticsCall(dateFrom, dateTo, projectId, projectStatusIds, onlyNotInvoiced, details, _callback);

    }

    /**
     * Get general statistics
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param projectStatusIds  (optional)
     * @param onlyNotInvoiced  (optional)
     * @param details  (optional)
     * @return GetFinancialStatistics200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetFinancialStatistics200Response getFinancialStatistics(LocalDate dateFrom, LocalDate dateTo, UUID projectId, UUID projectStatusIds, Boolean onlyNotInvoiced, Boolean details) throws ApiException {
        ApiResponse<GetFinancialStatistics200Response> localVarResp = getFinancialStatisticsWithHttpInfo(dateFrom, dateTo, projectId, projectStatusIds, onlyNotInvoiced, details);
        return localVarResp.getData();
    }

    /**
     * Get general statistics
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param projectStatusIds  (optional)
     * @param onlyNotInvoiced  (optional)
     * @param details  (optional)
     * @return ApiResponse&lt;GetFinancialStatistics200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetFinancialStatistics200Response> getFinancialStatisticsWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId, UUID projectStatusIds, Boolean onlyNotInvoiced, Boolean details) throws ApiException {
        okhttp3.Call localVarCall = getFinancialStatisticsValidateBeforeCall(dateFrom, dateTo, projectId, projectStatusIds, onlyNotInvoiced, details, null);
        Type localVarReturnType = new TypeToken<GetFinancialStatistics200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get general statistics (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param projectStatusIds  (optional)
     * @param onlyNotInvoiced  (optional)
     * @param details  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFinancialStatisticsAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, UUID projectStatusIds, Boolean onlyNotInvoiced, Boolean details, final ApiCallback<GetFinancialStatistics200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFinancialStatisticsValidateBeforeCall(dateFrom, dateTo, projectId, projectStatusIds, onlyNotInvoiced, details, _callback);
        Type localVarReturnType = new TypeToken<GetFinancialStatistics200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getFinancialStatisticsOverview
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFinancialStatisticsOverviewCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/overview";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call getFinancialStatisticsOverviewValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return getFinancialStatisticsOverviewCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get statistics overview
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return GetFinancialStatisticsOverview200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetFinancialStatisticsOverview200Response getFinancialStatisticsOverview(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<GetFinancialStatisticsOverview200Response> localVarResp = getFinancialStatisticsOverviewWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get statistics overview
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;GetFinancialStatisticsOverview200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetFinancialStatisticsOverview200Response> getFinancialStatisticsOverviewWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = getFinancialStatisticsOverviewValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<GetFinancialStatisticsOverview200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get statistics overview (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getFinancialStatisticsOverviewAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<GetFinancialStatisticsOverview200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getFinancialStatisticsOverviewValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetFinancialStatisticsOverview200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoicedAmount
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoicedAmountCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/invoicedAmount";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call getInvoicedAmountValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return getInvoicedAmountCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get invoiced amount
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return GetInvoicedAmount200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetInvoicedAmount200Response getInvoicedAmount(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<GetInvoicedAmount200Response> localVarResp = getInvoicedAmountWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get invoiced amount
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;GetInvoicedAmount200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetInvoicedAmount200Response> getInvoicedAmountWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = getInvoicedAmountValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<GetInvoicedAmount200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get invoiced amount (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoicedAmountAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<GetInvoicedAmount200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoicedAmountValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetInvoicedAmount200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMargin
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMarginCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/margin";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call getMarginValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return getMarginCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get margin
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return GetMargin200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetMargin200Response getMargin(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<GetMargin200Response> localVarResp = getMarginWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get margin
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;GetMargin200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetMargin200Response> getMarginWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = getMarginValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<GetMargin200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get margin (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMarginAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<GetMargin200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMarginValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetMargin200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMaterialRentalsCostPrice
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMaterialRentalsCostPriceCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/materialRentalsCostPrice";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call getMaterialRentalsCostPriceValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return getMaterialRentalsCostPriceCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get products material rentals cost price
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return GetMaterialRentalsCostPrice200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetMaterialRentalsCostPrice200Response getMaterialRentalsCostPrice(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<GetMaterialRentalsCostPrice200Response> localVarResp = getMaterialRentalsCostPriceWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get products material rentals cost price
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;GetMaterialRentalsCostPrice200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetMaterialRentalsCostPrice200Response> getMaterialRentalsCostPriceWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = getMaterialRentalsCostPriceValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<GetMaterialRentalsCostPrice200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get products material rentals cost price (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMaterialRentalsCostPriceAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<GetMaterialRentalsCostPrice200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMaterialRentalsCostPriceValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetMaterialRentalsCostPrice200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProductsCostPrice
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProductsCostPriceCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/financial_statistics/productsCostPrice";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_from", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_to", dateTo));
        }

        if (projectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_id", projectId));
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
    private okhttp3.Call getProductsCostPriceValidateBeforeCall(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback _callback) throws ApiException {
        return getProductsCostPriceCall(dateFrom, dateTo, projectId, _callback);

    }

    /**
     * Get products cost price
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return GetProductsCostPrice200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetProductsCostPrice200Response getProductsCostPrice(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        ApiResponse<GetProductsCostPrice200Response> localVarResp = getProductsCostPriceWithHttpInfo(dateFrom, dateTo, projectId);
        return localVarResp.getData();
    }

    /**
     * Get products cost price
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @return ApiResponse&lt;GetProductsCostPrice200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetProductsCostPrice200Response> getProductsCostPriceWithHttpInfo(LocalDate dateFrom, LocalDate dateTo, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = getProductsCostPriceValidateBeforeCall(dateFrom, dateTo, projectId, null);
        Type localVarReturnType = new TypeToken<GetProductsCostPrice200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get products cost price (asynchronously)
     * 
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param projectId  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProductsCostPriceAsync(LocalDate dateFrom, LocalDate dateTo, UUID projectId, final ApiCallback<GetProductsCostPrice200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProductsCostPriceValidateBeforeCall(dateFrom, dateTo, projectId, _callback);
        Type localVarReturnType = new TypeToken<GetProductsCostPrice200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
