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


import org.openapitools.client.model.AddContactPersonRequest;
import org.openapitools.client.model.ClockingRecordsClockingRecordIdDelete200Response;
import org.openapitools.client.model.ClockingRecordsClockingRecordIdPut200Response;
import org.openapitools.client.model.ClockingRecordsPost201Response;
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.GetContactPerson200Response;
import org.openapitools.client.model.GetContactPersonsList200Response;
import java.time.LocalDate;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ContactPersonsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ContactPersonsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ContactPersonsApi(ApiClient apiClient) {
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
     * Build call for addContactPerson
     * @param contactId  (required)
     * @param addContactPersonRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added contact person </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addContactPersonCall(String contactId, AddContactPersonRequest addContactPersonRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addContactPersonRequest;

        // create path and map variables
        String localVarPath = "/contacts/{contact_id}/contact_persons"
            .replace("{" + "contact_id" + "}", localVarApiClient.escapeString(contactId.toString()));

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
    private okhttp3.Call addContactPersonValidateBeforeCall(String contactId, AddContactPersonRequest addContactPersonRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contactId' is set
        if (contactId == null) {
            throw new ApiException("Missing the required parameter 'contactId' when calling addContactPerson(Async)");
        }

        return addContactPersonCall(contactId, addContactPersonRequest, _callback);

    }

    /**
     * Add a new contact person to a contact
     * 
     * @param contactId  (required)
     * @param addContactPersonRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added contact person </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response addContactPerson(String contactId, AddContactPersonRequest addContactPersonRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = addContactPersonWithHttpInfo(contactId, addContactPersonRequest);
        return localVarResp.getData();
    }

    /**
     * Add a new contact person to a contact
     * 
     * @param contactId  (required)
     * @param addContactPersonRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added contact person </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> addContactPersonWithHttpInfo(String contactId, AddContactPersonRequest addContactPersonRequest) throws ApiException {
        okhttp3.Call localVarCall = addContactPersonValidateBeforeCall(contactId, addContactPersonRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a new contact person to a contact (asynchronously)
     * 
     * @param contactId  (required)
     * @param addContactPersonRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added contact person </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addContactPersonAsync(String contactId, AddContactPersonRequest addContactPersonRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = addContactPersonValidateBeforeCall(contactId, addContactPersonRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for contactsContactIdContactPersonsContactPersonIdDelete
     * @param contactId  (required)
     * @param contactPersonId  (required)
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
    public okhttp3.Call contactsContactIdContactPersonsContactPersonIdDeleteCall(String contactId, String contactPersonId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/contacts/{contact_id}/contact_persons/{contact_person_id}"
            .replace("{" + "contact_id" + "}", localVarApiClient.escapeString(contactId.toString()))
            .replace("{" + "contact_person_id" + "}", localVarApiClient.escapeString(contactPersonId.toString()));

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
    private okhttp3.Call contactsContactIdContactPersonsContactPersonIdDeleteValidateBeforeCall(String contactId, String contactPersonId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contactId' is set
        if (contactId == null) {
            throw new ApiException("Missing the required parameter 'contactId' when calling contactsContactIdContactPersonsContactPersonIdDelete(Async)");
        }

        // verify the required parameter 'contactPersonId' is set
        if (contactPersonId == null) {
            throw new ApiException("Missing the required parameter 'contactPersonId' when calling contactsContactIdContactPersonsContactPersonIdDelete(Async)");
        }

        return contactsContactIdContactPersonsContactPersonIdDeleteCall(contactId, contactPersonId, _callback);

    }

    /**
     * Delete a contact person
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @return ClockingRecordsClockingRecordIdDelete200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdDelete200Response contactsContactIdContactPersonsContactPersonIdDelete(String contactId, String contactPersonId) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdDelete200Response> localVarResp = contactsContactIdContactPersonsContactPersonIdDeleteWithHttpInfo(contactId, contactPersonId);
        return localVarResp.getData();
    }

    /**
     * Delete a contact person
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdDelete200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdDelete200Response> contactsContactIdContactPersonsContactPersonIdDeleteWithHttpInfo(String contactId, String contactPersonId) throws ApiException {
        okhttp3.Call localVarCall = contactsContactIdContactPersonsContactPersonIdDeleteValidateBeforeCall(contactId, contactPersonId, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdDelete200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a contact person (asynchronously)
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
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
    public okhttp3.Call contactsContactIdContactPersonsContactPersonIdDeleteAsync(String contactId, String contactPersonId, final ApiCallback<ClockingRecordsClockingRecordIdDelete200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = contactsContactIdContactPersonsContactPersonIdDeleteValidateBeforeCall(contactId, contactPersonId, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdDelete200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for editContactPerson
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @param addContactPersonRequest  (optional)
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
    public okhttp3.Call editContactPersonCall(String contactId, String contactPersonId, AddContactPersonRequest addContactPersonRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addContactPersonRequest;

        // create path and map variables
        String localVarPath = "/contacts/{contact_id}/contact_persons/{contact_person_id}"
            .replace("{" + "contact_id" + "}", localVarApiClient.escapeString(contactId.toString()))
            .replace("{" + "contact_person_id" + "}", localVarApiClient.escapeString(contactPersonId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call editContactPersonValidateBeforeCall(String contactId, String contactPersonId, AddContactPersonRequest addContactPersonRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contactId' is set
        if (contactId == null) {
            throw new ApiException("Missing the required parameter 'contactId' when calling editContactPerson(Async)");
        }

        // verify the required parameter 'contactPersonId' is set
        if (contactPersonId == null) {
            throw new ApiException("Missing the required parameter 'contactPersonId' when calling editContactPerson(Async)");
        }

        return editContactPersonCall(contactId, contactPersonId, addContactPersonRequest, _callback);

    }

    /**
     * Edit a contact person
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @param addContactPersonRequest  (optional)
     * @return ClockingRecordsClockingRecordIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdPut200Response editContactPerson(String contactId, String contactPersonId, AddContactPersonRequest addContactPersonRequest) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdPut200Response> localVarResp = editContactPersonWithHttpInfo(contactId, contactPersonId, addContactPersonRequest);
        return localVarResp.getData();
    }

    /**
     * Edit a contact person
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @param addContactPersonRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdPut200Response> editContactPersonWithHttpInfo(String contactId, String contactPersonId, AddContactPersonRequest addContactPersonRequest) throws ApiException {
        okhttp3.Call localVarCall = editContactPersonValidateBeforeCall(contactId, contactPersonId, addContactPersonRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit a contact person (asynchronously)
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @param addContactPersonRequest  (optional)
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
    public okhttp3.Call editContactPersonAsync(String contactId, String contactPersonId, AddContactPersonRequest addContactPersonRequest, final ApiCallback<ClockingRecordsClockingRecordIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = editContactPersonValidateBeforeCall(contactId, contactPersonId, addContactPersonRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getContactPerson
     * @param contactId  (required)
     * @param contactPersonId  (required)
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
    public okhttp3.Call getContactPersonCall(String contactId, String contactPersonId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/contacts/{contact_id}/contact_persons/{contact_person_id}"
            .replace("{" + "contact_id" + "}", localVarApiClient.escapeString(contactId.toString()))
            .replace("{" + "contact_person_id" + "}", localVarApiClient.escapeString(contactPersonId.toString()));

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
    private okhttp3.Call getContactPersonValidateBeforeCall(String contactId, String contactPersonId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contactId' is set
        if (contactId == null) {
            throw new ApiException("Missing the required parameter 'contactId' when calling getContactPerson(Async)");
        }

        // verify the required parameter 'contactPersonId' is set
        if (contactPersonId == null) {
            throw new ApiException("Missing the required parameter 'contactPersonId' when calling getContactPerson(Async)");
        }

        return getContactPersonCall(contactId, contactPersonId, _callback);

    }

    /**
     * Get a contact person
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @return GetContactPerson200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public GetContactPerson200Response getContactPerson(String contactId, String contactPersonId) throws ApiException {
        ApiResponse<GetContactPerson200Response> localVarResp = getContactPersonWithHttpInfo(contactId, contactPersonId);
        return localVarResp.getData();
    }

    /**
     * Get a contact person
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
     * @return ApiResponse&lt;GetContactPerson200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetContactPerson200Response> getContactPersonWithHttpInfo(String contactId, String contactPersonId) throws ApiException {
        okhttp3.Call localVarCall = getContactPersonValidateBeforeCall(contactId, contactPersonId, null);
        Type localVarReturnType = new TypeToken<GetContactPerson200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a contact person (asynchronously)
     * 
     * @param contactId  (required)
     * @param contactPersonId  (required)
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
    public okhttp3.Call getContactPersonAsync(String contactId, String contactPersonId, final ApiCallback<GetContactPerson200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getContactPersonValidateBeforeCall(contactId, contactPersonId, _callback);
        Type localVarReturnType = new TypeToken<GetContactPerson200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getContactPersonsList
     * @param contactId  (required)
     * @param q  (optional)
     * @param createdGte  (optional)
     * @param createdLte  (optional)
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
    public okhttp3.Call getContactPersonsListCall(String contactId, String q, LocalDate createdGte, LocalDate createdLte, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/contacts/{contact_id}/contact_persons"
            .replace("{" + "contact_id" + "}", localVarApiClient.escapeString(contactId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (q != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("q", q));
        }

        if (createdGte != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("created_gte", createdGte));
        }

        if (createdLte != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("created_lte", createdLte));
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
    private okhttp3.Call getContactPersonsListValidateBeforeCall(String contactId, String q, LocalDate createdGte, LocalDate createdLte, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contactId' is set
        if (contactId == null) {
            throw new ApiException("Missing the required parameter 'contactId' when calling getContactPersonsList(Async)");
        }

        return getContactPersonsListCall(contactId, q, createdGte, createdLte, _callback);

    }

    /**
     * Get a list of contact people
     * Get a list of contact people associated with a contact
     * @param contactId  (required)
     * @param q  (optional)
     * @param createdGte  (optional)
     * @param createdLte  (optional)
     * @return GetContactPersonsList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public GetContactPersonsList200Response getContactPersonsList(String contactId, String q, LocalDate createdGte, LocalDate createdLte) throws ApiException {
        ApiResponse<GetContactPersonsList200Response> localVarResp = getContactPersonsListWithHttpInfo(contactId, q, createdGte, createdLte);
        return localVarResp.getData();
    }

    /**
     * Get a list of contact people
     * Get a list of contact people associated with a contact
     * @param contactId  (required)
     * @param q  (optional)
     * @param createdGte  (optional)
     * @param createdLte  (optional)
     * @return ApiResponse&lt;GetContactPersonsList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetContactPersonsList200Response> getContactPersonsListWithHttpInfo(String contactId, String q, LocalDate createdGte, LocalDate createdLte) throws ApiException {
        okhttp3.Call localVarCall = getContactPersonsListValidateBeforeCall(contactId, q, createdGte, createdLte, null);
        Type localVarReturnType = new TypeToken<GetContactPersonsList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of contact people (asynchronously)
     * Get a list of contact people associated with a contact
     * @param contactId  (required)
     * @param q  (optional)
     * @param createdGte  (optional)
     * @param createdLte  (optional)
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
    public okhttp3.Call getContactPersonsListAsync(String contactId, String q, LocalDate createdGte, LocalDate createdLte, final ApiCallback<GetContactPersonsList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getContactPersonsListValidateBeforeCall(contactId, q, createdGte, createdLte, _callback);
        Type localVarReturnType = new TypeToken<GetContactPersonsList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
