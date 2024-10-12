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


import org.openapitools.client.model.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest;
import org.openapitools.client.model.CompaniesCompanyIdFormTemplatesGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationFeatureSettingsGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdIntegrationSettingsPostRequest;
import org.openapitools.client.model.CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response;
import org.openapitools.client.model.CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest;
import org.openapitools.client.model.CompaniesGet200Response;
import org.openapitools.client.model.CompaniesSubscriptionSelfServiceGet200Response;
import org.openapitools.client.model.CreateSuccessResponse;
import org.openapitools.client.model.EmptySuccessResponse;
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.ForbiddenError;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CompaniesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CompaniesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CompaniesApi(ApiClient apiClient) {
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
     * Build call for companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCall(String companyId, String cIntegrationFeatureSettingId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "c_integration_feature_setting_id" + "}", localVarApiClient.escapeString(cIntegrationFeatureSettingId.toString()));

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
    private okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetValidateBeforeCall(String companyId, String cIntegrationFeatureSettingId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(Async)");
        }

        // verify the required parameter 'cIntegrationFeatureSettingId' is set
        if (cIntegrationFeatureSettingId == null) {
            throw new ApiException("Missing the required parameter 'cIntegrationFeatureSettingId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(Async)");
        }

        return companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCall(companyId, cIntegrationFeatureSettingId, _callback);

    }

    /**
     * View a company integration feature setting
     * 
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @return CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(String companyId, String cIntegrationFeatureSettingId) throws ApiException {
        ApiResponse<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> localVarResp = companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetWithHttpInfo(companyId, cIntegrationFeatureSettingId);
        return localVarResp.getData();
    }

    /**
     * View a company integration feature setting
     * 
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetWithHttpInfo(String companyId, String cIntegrationFeatureSettingId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetValidateBeforeCall(companyId, cIntegrationFeatureSettingId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * View a company integration feature setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetAsync(String companyId, String cIntegrationFeatureSettingId, final ApiCallback<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetValidateBeforeCall(companyId, cIntegrationFeatureSettingId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCall(String companyId, String cIntegrationFeatureSettingId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "c_integration_feature_setting_id" + "}", localVarApiClient.escapeString(cIntegrationFeatureSettingId.toString()));

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
    private okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutValidateBeforeCall(String companyId, String cIntegrationFeatureSettingId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(Async)");
        }

        // verify the required parameter 'cIntegrationFeatureSettingId' is set
        if (cIntegrationFeatureSettingId == null) {
            throw new ApiException("Missing the required parameter 'cIntegrationFeatureSettingId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(Async)");
        }

        return companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCall(companyId, cIntegrationFeatureSettingId, _callback);

    }

    /**
     * Edit a company integration feature setting
     * 
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @return CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(String companyId, String cIntegrationFeatureSettingId) throws ApiException {
        ApiResponse<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> localVarResp = companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutWithHttpInfo(companyId, cIntegrationFeatureSettingId);
        return localVarResp.getData();
    }

    /**
     * Edit a company integration feature setting
     * 
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutWithHttpInfo(String companyId, String cIntegrationFeatureSettingId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutValidateBeforeCall(companyId, cIntegrationFeatureSettingId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit a company integration feature setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param cIntegrationFeatureSettingId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutAsync(String companyId, String cIntegrationFeatureSettingId, final ApiCallback<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutValidateBeforeCall(companyId, cIntegrationFeatureSettingId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdCompaniesIntegrationFeatureSettingsGet
     * @param companyId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCall(String companyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/companies_integration_feature_settings"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

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
    private okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsGetValidateBeforeCall(String companyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(Async)");
        }

        return companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCall(companyId, _callback);

    }

    /**
     * List a company integration feature settings
     * 
     * @param companyId  (required)
     * @return CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(String companyId) throws ApiException {
        ApiResponse<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> localVarResp = companiesCompanyIdCompaniesIntegrationFeatureSettingsGetWithHttpInfo(companyId);
        return localVarResp.getData();
    }

    /**
     * List a company integration feature settings
     * 
     * @param companyId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> companiesCompanyIdCompaniesIntegrationFeatureSettingsGetWithHttpInfo(String companyId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsGetValidateBeforeCall(companyId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List a company integration feature settings (asynchronously)
     * 
     * @param companyId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsGetAsync(String companyId, final ApiCallback<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsGetValidateBeforeCall(companyId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdCompaniesIntegrationFeatureSettingsPost
     * @param companyId  (required)
     * @param companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCall(String companyId, CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest;

        // create path and map variables
        String localVarPath = "/companies/{company_id}/companies_integration_feature_settings"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

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
    private okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsPostValidateBeforeCall(String companyId, CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(Async)");
        }

        return companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCall(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest, _callback);

    }

    /**
     * Add a company integration feature setting
     * 
     * @param companyId  (required)
     * @param companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest  (optional)
     * @return CreateSuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public CreateSuccessResponse companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(String companyId, CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest) throws ApiException {
        ApiResponse<CreateSuccessResponse> localVarResp = companiesCompanyIdCompaniesIntegrationFeatureSettingsPostWithHttpInfo(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add a company integration feature setting
     * 
     * @param companyId  (required)
     * @param companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest  (optional)
     * @return ApiResponse&lt;CreateSuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateSuccessResponse> companiesCompanyIdCompaniesIntegrationFeatureSettingsPostWithHttpInfo(String companyId, CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsPostValidateBeforeCall(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest, null);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a company integration feature setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdCompaniesIntegrationFeatureSettingsPostAsync(String companyId, CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest, final ApiCallback<CreateSuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdCompaniesIntegrationFeatureSettingsPostValidateBeforeCall(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdFormTemplatesFormTemplateIdDelete
     * @param companyId  (required)
     * @param formTemplateId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies form template not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdFormTemplatesFormTemplateIdDeleteCall(String companyId, String formTemplateId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/form_templates/{form_template_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "form_template_id" + "}", localVarApiClient.escapeString(formTemplateId.toString()));

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
    private okhttp3.Call companiesCompanyIdFormTemplatesFormTemplateIdDeleteValidateBeforeCall(String companyId, String formTemplateId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdFormTemplatesFormTemplateIdDelete(Async)");
        }

        // verify the required parameter 'formTemplateId' is set
        if (formTemplateId == null) {
            throw new ApiException("Missing the required parameter 'formTemplateId' when calling companiesCompanyIdFormTemplatesFormTemplateIdDelete(Async)");
        }

        return companiesCompanyIdFormTemplatesFormTemplateIdDeleteCall(companyId, formTemplateId, _callback);

    }

    /**
     * Delete a form template company
     * 
     * @param companyId  (required)
     * @param formTemplateId Automatically added (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies form template not found </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse companiesCompanyIdFormTemplatesFormTemplateIdDelete(String companyId, String formTemplateId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = companiesCompanyIdFormTemplatesFormTemplateIdDeleteWithHttpInfo(companyId, formTemplateId);
        return localVarResp.getData();
    }

    /**
     * Delete a form template company
     * 
     * @param companyId  (required)
     * @param formTemplateId Automatically added (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies form template not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> companiesCompanyIdFormTemplatesFormTemplateIdDeleteWithHttpInfo(String companyId, String formTemplateId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdFormTemplatesFormTemplateIdDeleteValidateBeforeCall(companyId, formTemplateId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a form template company (asynchronously)
     * 
     * @param companyId  (required)
     * @param formTemplateId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies form template not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdFormTemplatesFormTemplateIdDeleteAsync(String companyId, String formTemplateId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdFormTemplatesFormTemplateIdDeleteValidateBeforeCall(companyId, formTemplateId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdFormTemplatesFormTemplateIdGet
     * @param companyId  (required)
     * @param id  (required)
     * @param formTemplateId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Form template company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdFormTemplatesFormTemplateIdGetCall(String companyId, String id, String formTemplateId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/form_templates/{form_template_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "form_template_id" + "}", localVarApiClient.escapeString(formTemplateId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (id != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("id", id));
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
    private okhttp3.Call companiesCompanyIdFormTemplatesFormTemplateIdGetValidateBeforeCall(String companyId, String id, String formTemplateId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdFormTemplatesFormTemplateIdGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling companiesCompanyIdFormTemplatesFormTemplateIdGet(Async)");
        }

        // verify the required parameter 'formTemplateId' is set
        if (formTemplateId == null) {
            throw new ApiException("Missing the required parameter 'formTemplateId' when calling companiesCompanyIdFormTemplatesFormTemplateIdGet(Async)");
        }

        return companiesCompanyIdFormTemplatesFormTemplateIdGetCall(companyId, id, formTemplateId, _callback);

    }

    /**
     * Get a company form template
     * 
     * @param companyId  (required)
     * @param id  (required)
     * @param formTemplateId Automatically added (required)
     * @return CompaniesCompanyIdFormTemplatesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Form template company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdFormTemplatesGet200Response companiesCompanyIdFormTemplatesFormTemplateIdGet(String companyId, String id, String formTemplateId) throws ApiException {
        ApiResponse<CompaniesCompanyIdFormTemplatesGet200Response> localVarResp = companiesCompanyIdFormTemplatesFormTemplateIdGetWithHttpInfo(companyId, id, formTemplateId);
        return localVarResp.getData();
    }

    /**
     * Get a company form template
     * 
     * @param companyId  (required)
     * @param id  (required)
     * @param formTemplateId Automatically added (required)
     * @return ApiResponse&lt;CompaniesCompanyIdFormTemplatesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Form template company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdFormTemplatesGet200Response> companiesCompanyIdFormTemplatesFormTemplateIdGetWithHttpInfo(String companyId, String id, String formTemplateId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdFormTemplatesFormTemplateIdGetValidateBeforeCall(companyId, id, formTemplateId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdFormTemplatesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a company form template (asynchronously)
     * 
     * @param companyId  (required)
     * @param id  (required)
     * @param formTemplateId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Form template company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdFormTemplatesFormTemplateIdGetAsync(String companyId, String id, String formTemplateId, final ApiCallback<CompaniesCompanyIdFormTemplatesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdFormTemplatesFormTemplateIdGetValidateBeforeCall(companyId, id, formTemplateId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdFormTemplatesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdFormTemplatesGet
     * @param companyId  (required)
     * @param formTemplateId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdFormTemplatesGetCall(String companyId, String formTemplateId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/form_templates/"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (formTemplateId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("form_template_id", formTemplateId));
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
    private okhttp3.Call companiesCompanyIdFormTemplatesGetValidateBeforeCall(String companyId, String formTemplateId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdFormTemplatesGet(Async)");
        }

        // verify the required parameter 'formTemplateId' is set
        if (formTemplateId == null) {
            throw new ApiException("Missing the required parameter 'formTemplateId' when calling companiesCompanyIdFormTemplatesGet(Async)");
        }

        return companiesCompanyIdFormTemplatesGetCall(companyId, formTemplateId, _callback);

    }

    /**
     * Get a list of company form templates
     * 
     * @param companyId  (required)
     * @param formTemplateId  (required)
     * @return CompaniesCompanyIdFormTemplatesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdFormTemplatesGet200Response companiesCompanyIdFormTemplatesGet(String companyId, String formTemplateId) throws ApiException {
        ApiResponse<CompaniesCompanyIdFormTemplatesGet200Response> localVarResp = companiesCompanyIdFormTemplatesGetWithHttpInfo(companyId, formTemplateId);
        return localVarResp.getData();
    }

    /**
     * Get a list of company form templates
     * 
     * @param companyId  (required)
     * @param formTemplateId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdFormTemplatesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdFormTemplatesGet200Response> companiesCompanyIdFormTemplatesGetWithHttpInfo(String companyId, String formTemplateId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdFormTemplatesGetValidateBeforeCall(companyId, formTemplateId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdFormTemplatesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of company form templates (asynchronously)
     * 
     * @param companyId  (required)
     * @param formTemplateId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdFormTemplatesGetAsync(String companyId, String formTemplateId, final ApiCallback<CompaniesCompanyIdFormTemplatesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdFormTemplatesGetValidateBeforeCall(companyId, formTemplateId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdFormTemplatesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdGet
     * @param companyId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Company object </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdGetCall(String companyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

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
    private okhttp3.Call companiesCompanyIdGetValidateBeforeCall(String companyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdGet(Async)");
        }

        return companiesCompanyIdGetCall(companyId, _callback);

    }

    /**
     * Details of 1 company
     * 
     * @param companyId  (required)
     * @return CompaniesCompanyIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Company object </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdGet200Response companiesCompanyIdGet(String companyId) throws ApiException {
        ApiResponse<CompaniesCompanyIdGet200Response> localVarResp = companiesCompanyIdGetWithHttpInfo(companyId);
        return localVarResp.getData();
    }

    /**
     * Details of 1 company
     * 
     * @param companyId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Company object </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdGet200Response> companiesCompanyIdGetWithHttpInfo(String companyId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdGetValidateBeforeCall(companyId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Details of 1 company (asynchronously)
     * 
     * @param companyId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Company object </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdGetAsync(String companyId, final ApiCallback<CompaniesCompanyIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdGetValidateBeforeCall(companyId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationFeatureSettingsGet
     * @param companyId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationFeatureSettingsGetCall(String companyId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_feature_settings"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

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
    private okhttp3.Call companiesCompanyIdIntegrationFeatureSettingsGetValidateBeforeCall(String companyId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationFeatureSettingsGet(Async)");
        }

        return companiesCompanyIdIntegrationFeatureSettingsGetCall(companyId, _callback);

    }

    /**
     * Get a list of integration feature settings
     * 
     * @param companyId  (required)
     * @return CompaniesCompanyIdIntegrationFeatureSettingsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdIntegrationFeatureSettingsGet200Response companiesCompanyIdIntegrationFeatureSettingsGet(String companyId) throws ApiException {
        ApiResponse<CompaniesCompanyIdIntegrationFeatureSettingsGet200Response> localVarResp = companiesCompanyIdIntegrationFeatureSettingsGetWithHttpInfo(companyId);
        return localVarResp.getData();
    }

    /**
     * Get a list of integration feature settings
     * 
     * @param companyId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdIntegrationFeatureSettingsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdIntegrationFeatureSettingsGet200Response> companiesCompanyIdIntegrationFeatureSettingsGetWithHttpInfo(String companyId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationFeatureSettingsGetValidateBeforeCall(companyId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationFeatureSettingsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of integration feature settings (asynchronously)
     * 
     * @param companyId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationFeatureSettingsGetAsync(String companyId, final ApiCallback<CompaniesCompanyIdIntegrationFeatureSettingsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationFeatureSettingsGetValidateBeforeCall(companyId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationFeatureSettingsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet
     * @param companyId  (required)
     * @param integrationFeatureSettingId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCall(String companyId, String integrationFeatureSettingId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_feature_settings/{integration_feature_setting_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "integration_feature_setting_id" + "}", localVarApiClient.escapeString(integrationFeatureSettingId.toString()));

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
    private okhttp3.Call companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetValidateBeforeCall(String companyId, String integrationFeatureSettingId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(Async)");
        }

        // verify the required parameter 'integrationFeatureSettingId' is set
        if (integrationFeatureSettingId == null) {
            throw new ApiException("Missing the required parameter 'integrationFeatureSettingId' when calling companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(Async)");
        }

        return companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCall(companyId, integrationFeatureSettingId, _callback);

    }

    /**
     * Show details of 1 integration feature setting
     * 
     * @param companyId  (required)
     * @param integrationFeatureSettingId  (required)
     * @return CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(String companyId, String integrationFeatureSettingId) throws ApiException {
        ApiResponse<CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response> localVarResp = companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetWithHttpInfo(companyId, integrationFeatureSettingId);
        return localVarResp.getData();
    }

    /**
     * Show details of 1 integration feature setting
     * 
     * @param companyId  (required)
     * @param integrationFeatureSettingId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response> companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetWithHttpInfo(String companyId, String integrationFeatureSettingId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetValidateBeforeCall(companyId, integrationFeatureSettingId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show details of 1 integration feature setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param integrationFeatureSettingId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> IntegrationFeatureSetting not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetAsync(String companyId, String integrationFeatureSettingId, final ApiCallback<CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetValidateBeforeCall(companyId, integrationFeatureSettingId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
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
    public okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCall(String companyId, String companiesIntegrationSettingId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_settings/{companies_integration_setting_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "companies_integration_setting_id" + "}", localVarApiClient.escapeString(companiesIntegrationSettingId.toString()));

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
    private okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteValidateBeforeCall(String companyId, String companiesIntegrationSettingId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(Async)");
        }

        // verify the required parameter 'companiesIntegrationSettingId' is set
        if (companiesIntegrationSettingId == null) {
            throw new ApiException("Missing the required parameter 'companiesIntegrationSettingId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(Async)");
        }

        return companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCall(companyId, companiesIntegrationSettingId, _callback);

    }

    /**
     * Delete a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
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
    public EmptySuccessResponse companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(String companyId, String companiesIntegrationSettingId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteWithHttpInfo(companyId, companiesIntegrationSettingId);
        return localVarResp.getData();
    }

    /**
     * Delete a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
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
    public ApiResponse<EmptySuccessResponse> companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteWithHttpInfo(String companyId, String companiesIntegrationSettingId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteValidateBeforeCall(companyId, companiesIntegrationSettingId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a company integration setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
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
    public okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteAsync(String companyId, String companiesIntegrationSettingId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteValidateBeforeCall(companyId, companiesIntegrationSettingId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
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
    public okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCall(String companyId, String companiesIntegrationSettingId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_settings/{companies_integration_setting_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "companies_integration_setting_id" + "}", localVarApiClient.escapeString(companiesIntegrationSettingId.toString()));

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
    private okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetValidateBeforeCall(String companyId, String companiesIntegrationSettingId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(Async)");
        }

        // verify the required parameter 'companiesIntegrationSettingId' is set
        if (companiesIntegrationSettingId == null) {
            throw new ApiException("Missing the required parameter 'companiesIntegrationSettingId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(Async)");
        }

        return companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCall(companyId, companiesIntegrationSettingId, _callback);

    }

    /**
     * Get a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
     * @return CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(String companyId, String companiesIntegrationSettingId) throws ApiException {
        ApiResponse<CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response> localVarResp = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetWithHttpInfo(companyId, companiesIntegrationSettingId);
        return localVarResp.getData();
    }

    /**
     * Get a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
     * @return ApiResponse&lt;CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response> companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetWithHttpInfo(String companyId, String companiesIntegrationSettingId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetValidateBeforeCall(companyId, companiesIntegrationSettingId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a company integration setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
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
    public okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetAsync(String companyId, String companiesIntegrationSettingId, final ApiCallback<CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetValidateBeforeCall(companyId, companiesIntegrationSettingId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCall(String companyId, String companiesIntegrationSettingId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_settings/{companies_integration_setting_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "companies_integration_setting_id" + "}", localVarApiClient.escapeString(companiesIntegrationSettingId.toString()));

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
    private okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutValidateBeforeCall(String companyId, String companiesIntegrationSettingId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(Async)");
        }

        // verify the required parameter 'companiesIntegrationSettingId' is set
        if (companiesIntegrationSettingId == null) {
            throw new ApiException("Missing the required parameter 'companiesIntegrationSettingId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(Async)");
        }

        return companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCall(companyId, companiesIntegrationSettingId, _callback);

    }

    /**
     * Edit a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(String companyId, String companiesIntegrationSettingId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutWithHttpInfo(companyId, companiesIntegrationSettingId);
        return localVarResp.getData();
    }

    /**
     * Edit a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutWithHttpInfo(String companyId, String companiesIntegrationSettingId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutValidateBeforeCall(companyId, companiesIntegrationSettingId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit a company integration setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param companiesIntegrationSettingId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Companies integration setting not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutAsync(String companyId, String companiesIntegrationSettingId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutValidateBeforeCall(companyId, companiesIntegrationSettingId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationSettingsGet
     * @param companyId  (required)
     * @param identifier The identifier of an ERP integration (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationSettingsGetCall(String companyId, String identifier, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_settings"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (identifier != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("identifier", identifier));
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
    private okhttp3.Call companiesCompanyIdIntegrationSettingsGetValidateBeforeCall(String companyId, String identifier, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsGet(Async)");
        }

        return companiesCompanyIdIntegrationSettingsGetCall(companyId, identifier, _callback);

    }

    /**
     * Get a list of company integration settings
     * 
     * @param companyId  (required)
     * @param identifier The identifier of an ERP integration (optional)
     * @return CompaniesCompanyIdIntegrationSettingsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdIntegrationSettingsGet200Response companiesCompanyIdIntegrationSettingsGet(String companyId, String identifier) throws ApiException {
        ApiResponse<CompaniesCompanyIdIntegrationSettingsGet200Response> localVarResp = companiesCompanyIdIntegrationSettingsGetWithHttpInfo(companyId, identifier);
        return localVarResp.getData();
    }

    /**
     * Get a list of company integration settings
     * 
     * @param companyId  (required)
     * @param identifier The identifier of an ERP integration (optional)
     * @return ApiResponse&lt;CompaniesCompanyIdIntegrationSettingsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdIntegrationSettingsGet200Response> companiesCompanyIdIntegrationSettingsGetWithHttpInfo(String companyId, String identifier) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsGetValidateBeforeCall(companyId, identifier, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationSettingsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of company integration settings (asynchronously)
     * 
     * @param companyId  (required)
     * @param identifier The identifier of an ERP integration (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationSettingsGetAsync(String companyId, String identifier, final ApiCallback<CompaniesCompanyIdIntegrationSettingsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsGetValidateBeforeCall(companyId, identifier, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdIntegrationSettingsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdIntegrationSettingsPost
     * @param companyId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationSettingsPostCall(String companyId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/integration_settings"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()));

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
    private okhttp3.Call companiesCompanyIdIntegrationSettingsPostValidateBeforeCall(String companyId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsPost(Async)");
        }

        return companiesCompanyIdIntegrationSettingsPostCall(companyId, companiesCompanyIdIntegrationSettingsPostRequest, _callback);

    }

    /**
     * Add a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @return CreateSuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public CreateSuccessResponse companiesCompanyIdIntegrationSettingsPost(String companyId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest) throws ApiException {
        ApiResponse<CreateSuccessResponse> localVarResp = companiesCompanyIdIntegrationSettingsPostWithHttpInfo(companyId, companiesCompanyIdIntegrationSettingsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add a company integration setting
     * 
     * @param companyId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @return ApiResponse&lt;CreateSuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateSuccessResponse> companiesCompanyIdIntegrationSettingsPostWithHttpInfo(String companyId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsPostValidateBeforeCall(companyId, companiesCompanyIdIntegrationSettingsPostRequest, null);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a company integration setting (asynchronously)
     * 
     * @param companyId  (required)
     * @param companiesCompanyIdIntegrationSettingsPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdIntegrationSettingsPostAsync(String companyId, CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest, final ApiCallback<CreateSuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdIntegrationSettingsPostValidateBeforeCall(companyId, companiesCompanyIdIntegrationSettingsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdPriceMarginsPriceMarginsIdDelete
     * @param companyId  (required)
     * @param priceMarginId  (required)
     * @param priceMarginsId Automatically added (required)
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
    public okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCall(String companyId, String priceMarginId, String priceMarginsId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/price_margins/{price_margins_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "price_margins_id" + "}", localVarApiClient.escapeString(priceMarginsId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (priceMarginId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("price_margin_id", priceMarginId));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdDeleteValidateBeforeCall(String companyId, String priceMarginId, String priceMarginsId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdDelete(Async)");
        }

        // verify the required parameter 'priceMarginId' is set
        if (priceMarginId == null) {
            throw new ApiException("Missing the required parameter 'priceMarginId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdDelete(Async)");
        }

        // verify the required parameter 'priceMarginsId' is set
        if (priceMarginsId == null) {
            throw new ApiException("Missing the required parameter 'priceMarginsId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdDelete(Async)");
        }

        return companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCall(companyId, priceMarginId, priceMarginsId, _callback);

    }

    /**
     * Delete a company price margin
     * 
     * @param companyId  (required)
     * @param priceMarginId  (required)
     * @param priceMarginsId Automatically added (required)
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
    public EmptySuccessResponse companiesCompanyIdPriceMarginsPriceMarginsIdDelete(String companyId, String priceMarginId, String priceMarginsId) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = companiesCompanyIdPriceMarginsPriceMarginsIdDeleteWithHttpInfo(companyId, priceMarginId, priceMarginsId);
        return localVarResp.getData();
    }

    /**
     * Delete a company price margin
     * 
     * @param companyId  (required)
     * @param priceMarginId  (required)
     * @param priceMarginsId Automatically added (required)
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
    public ApiResponse<EmptySuccessResponse> companiesCompanyIdPriceMarginsPriceMarginsIdDeleteWithHttpInfo(String companyId, String priceMarginId, String priceMarginsId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdPriceMarginsPriceMarginsIdDeleteValidateBeforeCall(companyId, priceMarginId, priceMarginsId, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a company price margin (asynchronously)
     * 
     * @param companyId  (required)
     * @param priceMarginId  (required)
     * @param priceMarginsId Automatically added (required)
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
    public okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdDeleteAsync(String companyId, String priceMarginId, String priceMarginsId, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdPriceMarginsPriceMarginsIdDeleteValidateBeforeCall(companyId, priceMarginId, priceMarginsId, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdPriceMarginsPriceMarginsIdGet
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdGetCall(String companyId, String priceMarginsId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/{company_id}/price_margins/{price_margins_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "price_margins_id" + "}", localVarApiClient.escapeString(priceMarginsId.toString()));

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
    private okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdGetValidateBeforeCall(String companyId, String priceMarginsId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdGet(Async)");
        }

        // verify the required parameter 'priceMarginsId' is set
        if (priceMarginsId == null) {
            throw new ApiException("Missing the required parameter 'priceMarginsId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdGet(Async)");
        }

        return companiesCompanyIdPriceMarginsPriceMarginsIdGetCall(companyId, priceMarginsId, _callback);

    }

    /**
     * Get a list of company price margins
     * 
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @return CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response companiesCompanyIdPriceMarginsPriceMarginsIdGet(String companyId, String priceMarginsId) throws ApiException {
        ApiResponse<CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response> localVarResp = companiesCompanyIdPriceMarginsPriceMarginsIdGetWithHttpInfo(companyId, priceMarginsId);
        return localVarResp.getData();
    }

    /**
     * Get a list of company price margins
     * 
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @return ApiResponse&lt;CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response> companiesCompanyIdPriceMarginsPriceMarginsIdGetWithHttpInfo(String companyId, String priceMarginsId) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdPriceMarginsPriceMarginsIdGetValidateBeforeCall(companyId, priceMarginsId, null);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of company price margins (asynchronously)
     * 
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdGetAsync(String companyId, String priceMarginsId, final ApiCallback<CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdPriceMarginsPriceMarginsIdGetValidateBeforeCall(companyId, priceMarginsId, _callback);
        Type localVarReturnType = new TypeToken<CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesCompanyIdPriceMarginsPriceMarginsIdPost
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @param companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdPostCall(String companyId, String priceMarginsId, CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest;

        // create path and map variables
        String localVarPath = "/companies/{company_id}/price_margins/{price_margins_id}"
            .replace("{" + "company_id" + "}", localVarApiClient.escapeString(companyId.toString()))
            .replace("{" + "price_margins_id" + "}", localVarApiClient.escapeString(priceMarginsId.toString()));

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
    private okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdPostValidateBeforeCall(String companyId, String priceMarginsId, CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'companyId' is set
        if (companyId == null) {
            throw new ApiException("Missing the required parameter 'companyId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdPost(Async)");
        }

        // verify the required parameter 'priceMarginsId' is set
        if (priceMarginsId == null) {
            throw new ApiException("Missing the required parameter 'priceMarginsId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdPost(Async)");
        }

        return companiesCompanyIdPriceMarginsPriceMarginsIdPostCall(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest, _callback);

    }

    /**
     * Add a company price margin
     * 
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @param companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest  (optional)
     * @return CreateSuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public CreateSuccessResponse companiesCompanyIdPriceMarginsPriceMarginsIdPost(String companyId, String priceMarginsId, CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest) throws ApiException {
        ApiResponse<CreateSuccessResponse> localVarResp = companiesCompanyIdPriceMarginsPriceMarginsIdPostWithHttpInfo(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add a company price margin
     * 
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @param companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest  (optional)
     * @return ApiResponse&lt;CreateSuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateSuccessResponse> companiesCompanyIdPriceMarginsPriceMarginsIdPostWithHttpInfo(String companyId, String priceMarginsId, CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest) throws ApiException {
        okhttp3.Call localVarCall = companiesCompanyIdPriceMarginsPriceMarginsIdPostValidateBeforeCall(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest, null);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a company price margin (asynchronously)
     * 
     * @param companyId  (required)
     * @param priceMarginsId Automatically added (required)
     * @param companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesCompanyIdPriceMarginsPriceMarginsIdPostAsync(String companyId, String priceMarginsId, CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest, final ApiCallback<CreateSuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesCompanyIdPriceMarginsPriceMarginsIdPostValidateBeforeCall(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateSuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies";

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
    private okhttp3.Call companiesGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return companiesGetCall(_callback);

    }

    /**
     * Get a list of companies
     * 
     * @return CompaniesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesGet200Response companiesGet() throws ApiException {
        ApiResponse<CompaniesGet200Response> localVarResp = companiesGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get a list of companies
     * 
     * @return ApiResponse&lt;CompaniesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesGet200Response> companiesGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = companiesGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<CompaniesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of companies (asynchronously)
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
    public okhttp3.Call companiesGetAsync(final ApiCallback<CompaniesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<CompaniesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for companiesSubscriptionSelfServiceGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Self service url </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesSubscriptionSelfServiceGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/companies/subscription_self_service";

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
    private okhttp3.Call companiesSubscriptionSelfServiceGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return companiesSubscriptionSelfServiceGetCall(_callback);

    }

    /**
     * URL for subscription selfservice
     * 
     * @return CompaniesSubscriptionSelfServiceGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Self service url </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public CompaniesSubscriptionSelfServiceGet200Response companiesSubscriptionSelfServiceGet() throws ApiException {
        ApiResponse<CompaniesSubscriptionSelfServiceGet200Response> localVarResp = companiesSubscriptionSelfServiceGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * URL for subscription selfservice
     * 
     * @return ApiResponse&lt;CompaniesSubscriptionSelfServiceGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Self service url </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CompaniesSubscriptionSelfServiceGet200Response> companiesSubscriptionSelfServiceGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = companiesSubscriptionSelfServiceGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<CompaniesSubscriptionSelfServiceGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * URL for subscription selfservice (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Self service url </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Company not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call companiesSubscriptionSelfServiceGetAsync(final ApiCallback<CompaniesSubscriptionSelfServiceGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = companiesSubscriptionSelfServiceGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<CompaniesSubscriptionSelfServiceGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
