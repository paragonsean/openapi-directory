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


import org.openapitools.client.model.ClockingRecordsClockingRecordIdDelete200Response;
import org.openapitools.client.model.ClockingRecordsClockingRecordIdPut200Response;
import org.openapitools.client.model.ClockingRecordsPost201Response;
import org.openapitools.client.model.EmptySuccessResponse;
import org.openapitools.client.model.ErrorNotFound;
import org.openapitools.client.model.ErrorValidation;
import org.openapitools.client.model.ExpenseFilesExpenseFileIdPut200Response;
import java.io.File;
import org.openapitools.client.model.ProjectsGet200Response;
import org.openapitools.client.model.ProjectsHasProjectsWithCustomStatusesGet200Response;
import org.openapitools.client.model.ProjectsPostRequest;
import org.openapitools.client.model.ProjectsProjectIdAllFilesGet200Response;
import org.openapitools.client.model.ProjectsProjectIdGet200Response;
import org.openapitools.client.model.ProjectsProjectIdPutRequest;
import org.openapitools.client.model.ProjectsProjectIdSendBulkPdfPostRequest;
import org.openapitools.client.model.ProjectsProjectIdUsersGet200Response;
import org.openapitools.client.model.ProjectsProjectIdUsersPostRequest;
import org.openapitools.client.model.ProjectsProjectIdUsersUserIdGet200Response;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProjectsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProjectsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProjectsApi(ApiClient apiClient) {
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
     * Build call for projectsGet
     * @param showAll Unless this is set to &#x60;true&#x60; only open projects will be shown (optional, default to false)
     * @param sort Sort projects by &#x60;not_invoiced_amount&#x60; (optional)
     * @param direction  (optional)
     * @param contactId Used to filter on the &#x60;contact_id&#x60; of the projects (optional)
     * @param companyId Used to filter on the &#x60;company_id&#x60; of the projects (optional)
     * @param projectStatusId Used to filter on the &#x60;project_status_id&#x60; of the projects (optional)
     * @param projectStatusIds Used to filter on the &#x60;project_status_id&#x60; of the projects (match any of the provided values) (optional)
     * @param name Used to search on the &#x60;name&#x60; of the projects (optional)
     * @param erpProjectId Used to search on the &#x60;erp_project_id&#x60; of the projects (optional)
     * @param erpTaskId Used to search on the &#x60;erp_task_id&#x60; of the projects (optional)
     * @param startTimeGte Show projects with start time after than this value (optional)
     * @param startTimeLte Show projects with start time before this value (optional)
     * @param startTimeEq Show only projects with start time on specific date (optional)
     * @param eventStartGt  (optional)
     * @param eventStartLt  (optional)
     * @param eventStartEq  (optional)
     * @param eventEndGt  (optional)
     * @param eventEndLt  (optional)
     * @param eventEndEq  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsGetCall(Boolean showAll, String sort, String direction, UUID contactId, UUID companyId, UUID projectStatusId, List<UUID> projectStatusIds, String name, String erpProjectId, String erpTaskId, String startTimeGte, String startTimeLte, String startTimeEq, String eventStartGt, String eventStartLt, String eventStartEq, String eventEndGt, String eventEndLt, String eventEndEq, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (showAll != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("show_all", showAll));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (direction != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("direction", direction));
        }

        if (contactId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("contact_id", contactId));
        }

        if (companyId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("company_id", companyId));
        }

        if (projectStatusId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("project_status_id", projectStatusId));
        }

        if (projectStatusIds != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "project_status_ids", projectStatusIds));
        }

        if (name != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("name", name));
        }

        if (erpProjectId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("erp_project_id", erpProjectId));
        }

        if (erpTaskId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("erp_task_id", erpTaskId));
        }

        if (startTimeGte != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start_time_gte", startTimeGte));
        }

        if (startTimeLte != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start_time_lte", startTimeLte));
        }

        if (startTimeEq != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start_time_eq", startTimeEq));
        }

        if (eventStartGt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event_start[][gt]", eventStartGt));
        }

        if (eventStartLt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event_start[][lt]", eventStartLt));
        }

        if (eventStartEq != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event_start[][eq]", eventStartEq));
        }

        if (eventEndGt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event_end[][gt]", eventEndGt));
        }

        if (eventEndLt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event_end[][lt]", eventEndLt));
        }

        if (eventEndEq != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event_end[][eq]", eventEndEq));
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
    private okhttp3.Call projectsGetValidateBeforeCall(Boolean showAll, String sort, String direction, UUID contactId, UUID companyId, UUID projectStatusId, List<UUID> projectStatusIds, String name, String erpProjectId, String erpTaskId, String startTimeGte, String startTimeLte, String startTimeEq, String eventStartGt, String eventStartLt, String eventStartEq, String eventEndGt, String eventEndLt, String eventEndEq, final ApiCallback _callback) throws ApiException {
        return projectsGetCall(showAll, sort, direction, contactId, companyId, projectStatusId, projectStatusIds, name, erpProjectId, erpTaskId, startTimeGte, startTimeLte, startTimeEq, eventStartGt, eventStartLt, eventStartEq, eventEndGt, eventEndLt, eventEndEq, _callback);

    }

    /**
     * View list of projects
     * 
     * @param showAll Unless this is set to &#x60;true&#x60; only open projects will be shown (optional, default to false)
     * @param sort Sort projects by &#x60;not_invoiced_amount&#x60; (optional)
     * @param direction  (optional)
     * @param contactId Used to filter on the &#x60;contact_id&#x60; of the projects (optional)
     * @param companyId Used to filter on the &#x60;company_id&#x60; of the projects (optional)
     * @param projectStatusId Used to filter on the &#x60;project_status_id&#x60; of the projects (optional)
     * @param projectStatusIds Used to filter on the &#x60;project_status_id&#x60; of the projects (match any of the provided values) (optional)
     * @param name Used to search on the &#x60;name&#x60; of the projects (optional)
     * @param erpProjectId Used to search on the &#x60;erp_project_id&#x60; of the projects (optional)
     * @param erpTaskId Used to search on the &#x60;erp_task_id&#x60; of the projects (optional)
     * @param startTimeGte Show projects with start time after than this value (optional)
     * @param startTimeLte Show projects with start time before this value (optional)
     * @param startTimeEq Show only projects with start time on specific date (optional)
     * @param eventStartGt  (optional)
     * @param eventStartLt  (optional)
     * @param eventStartEq  (optional)
     * @param eventEndGt  (optional)
     * @param eventEndLt  (optional)
     * @param eventEndEq  (optional)
     * @return ProjectsGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsGet200Response projectsGet(Boolean showAll, String sort, String direction, UUID contactId, UUID companyId, UUID projectStatusId, List<UUID> projectStatusIds, String name, String erpProjectId, String erpTaskId, String startTimeGte, String startTimeLte, String startTimeEq, String eventStartGt, String eventStartLt, String eventStartEq, String eventEndGt, String eventEndLt, String eventEndEq) throws ApiException {
        ApiResponse<ProjectsGet200Response> localVarResp = projectsGetWithHttpInfo(showAll, sort, direction, contactId, companyId, projectStatusId, projectStatusIds, name, erpProjectId, erpTaskId, startTimeGte, startTimeLte, startTimeEq, eventStartGt, eventStartLt, eventStartEq, eventEndGt, eventEndLt, eventEndEq);
        return localVarResp.getData();
    }

    /**
     * View list of projects
     * 
     * @param showAll Unless this is set to &#x60;true&#x60; only open projects will be shown (optional, default to false)
     * @param sort Sort projects by &#x60;not_invoiced_amount&#x60; (optional)
     * @param direction  (optional)
     * @param contactId Used to filter on the &#x60;contact_id&#x60; of the projects (optional)
     * @param companyId Used to filter on the &#x60;company_id&#x60; of the projects (optional)
     * @param projectStatusId Used to filter on the &#x60;project_status_id&#x60; of the projects (optional)
     * @param projectStatusIds Used to filter on the &#x60;project_status_id&#x60; of the projects (match any of the provided values) (optional)
     * @param name Used to search on the &#x60;name&#x60; of the projects (optional)
     * @param erpProjectId Used to search on the &#x60;erp_project_id&#x60; of the projects (optional)
     * @param erpTaskId Used to search on the &#x60;erp_task_id&#x60; of the projects (optional)
     * @param startTimeGte Show projects with start time after than this value (optional)
     * @param startTimeLte Show projects with start time before this value (optional)
     * @param startTimeEq Show only projects with start time on specific date (optional)
     * @param eventStartGt  (optional)
     * @param eventStartLt  (optional)
     * @param eventStartEq  (optional)
     * @param eventEndGt  (optional)
     * @param eventEndLt  (optional)
     * @param eventEndEq  (optional)
     * @return ApiResponse&lt;ProjectsGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsGet200Response> projectsGetWithHttpInfo(Boolean showAll, String sort, String direction, UUID contactId, UUID companyId, UUID projectStatusId, List<UUID> projectStatusIds, String name, String erpProjectId, String erpTaskId, String startTimeGte, String startTimeLte, String startTimeEq, String eventStartGt, String eventStartLt, String eventStartEq, String eventEndGt, String eventEndLt, String eventEndEq) throws ApiException {
        okhttp3.Call localVarCall = projectsGetValidateBeforeCall(showAll, sort, direction, contactId, companyId, projectStatusId, projectStatusIds, name, erpProjectId, erpTaskId, startTimeGte, startTimeLte, startTimeEq, eventStartGt, eventStartLt, eventStartEq, eventEndGt, eventEndLt, eventEndEq, null);
        Type localVarReturnType = new TypeToken<ProjectsGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * View list of projects (asynchronously)
     * 
     * @param showAll Unless this is set to &#x60;true&#x60; only open projects will be shown (optional, default to false)
     * @param sort Sort projects by &#x60;not_invoiced_amount&#x60; (optional)
     * @param direction  (optional)
     * @param contactId Used to filter on the &#x60;contact_id&#x60; of the projects (optional)
     * @param companyId Used to filter on the &#x60;company_id&#x60; of the projects (optional)
     * @param projectStatusId Used to filter on the &#x60;project_status_id&#x60; of the projects (optional)
     * @param projectStatusIds Used to filter on the &#x60;project_status_id&#x60; of the projects (match any of the provided values) (optional)
     * @param name Used to search on the &#x60;name&#x60; of the projects (optional)
     * @param erpProjectId Used to search on the &#x60;erp_project_id&#x60; of the projects (optional)
     * @param erpTaskId Used to search on the &#x60;erp_task_id&#x60; of the projects (optional)
     * @param startTimeGte Show projects with start time after than this value (optional)
     * @param startTimeLte Show projects with start time before this value (optional)
     * @param startTimeEq Show only projects with start time on specific date (optional)
     * @param eventStartGt  (optional)
     * @param eventStartLt  (optional)
     * @param eventStartEq  (optional)
     * @param eventEndGt  (optional)
     * @param eventEndLt  (optional)
     * @param eventEndEq  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsGetAsync(Boolean showAll, String sort, String direction, UUID contactId, UUID companyId, UUID projectStatusId, List<UUID> projectStatusIds, String name, String erpProjectId, String erpTaskId, String startTimeGte, String startTimeLte, String startTimeEq, String eventStartGt, String eventStartLt, String eventStartEq, String eventEndGt, String eventEndLt, String eventEndEq, final ApiCallback<ProjectsGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsGetValidateBeforeCall(showAll, sort, direction, contactId, companyId, projectStatusId, projectStatusIds, name, erpProjectId, erpTaskId, startTimeGte, startTimeLte, startTimeEq, eventStartGt, eventStartLt, eventStartEq, eventEndGt, eventEndLt, eventEndEq, _callback);
        Type localVarReturnType = new TypeToken<ProjectsGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsHasProjectsWithCustomStatusesGet_0
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsHasProjectsWithCustomStatusesGet_0Call(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/has_projects_with_custom_statuses";

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
    private okhttp3.Call projectsHasProjectsWithCustomStatusesGet_0ValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return projectsHasProjectsWithCustomStatusesGet_0Call(_callback);

    }

    /**
     * Check if the company has projects with custom statuses
     * 
     * @return ProjectsHasProjectsWithCustomStatusesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsHasProjectsWithCustomStatusesGet200Response projectsHasProjectsWithCustomStatusesGet_0() throws ApiException {
        ApiResponse<ProjectsHasProjectsWithCustomStatusesGet200Response> localVarResp = projectsHasProjectsWithCustomStatusesGet_0WithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Check if the company has projects with custom statuses
     * 
     * @return ApiResponse&lt;ProjectsHasProjectsWithCustomStatusesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsHasProjectsWithCustomStatusesGet200Response> projectsHasProjectsWithCustomStatusesGet_0WithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = projectsHasProjectsWithCustomStatusesGet_0ValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<ProjectsHasProjectsWithCustomStatusesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Check if the company has projects with custom statuses (asynchronously)
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
    public okhttp3.Call projectsHasProjectsWithCustomStatusesGet_0Async(final ApiCallback<ProjectsHasProjectsWithCustomStatusesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsHasProjectsWithCustomStatusesGet_0ValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<ProjectsHasProjectsWithCustomStatusesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsPost
     * @param projectsPostRequest  (optional)
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
    public okhttp3.Call projectsPostCall(ProjectsPostRequest projectsPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = projectsPostRequest;

        // create path and map variables
        String localVarPath = "/projects";

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
    private okhttp3.Call projectsPostValidateBeforeCall(ProjectsPostRequest projectsPostRequest, final ApiCallback _callback) throws ApiException {
        return projectsPostCall(projectsPostRequest, _callback);

    }

    /**
     * Add a project
     * 
     * @param projectsPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response projectsPost(ProjectsPostRequest projectsPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = projectsPostWithHttpInfo(projectsPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add a project
     * 
     * @param projectsPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> projectsPostWithHttpInfo(ProjectsPostRequest projectsPostRequest) throws ApiException {
        okhttp3.Call localVarCall = projectsPostValidateBeforeCall(projectsPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a project (asynchronously)
     * 
     * @param projectsPostRequest  (optional)
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
    public okhttp3.Call projectsPostAsync(ProjectsPostRequest projectsPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsPostValidateBeforeCall(projectsPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdAllFilesGet
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdAllFilesGetCall(String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/all_files"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdAllFilesGetValidateBeforeCall(String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdAllFilesGet(Async)");
        }

        return projectsProjectIdAllFilesGetCall(projectId, _callback);

    }

    /**
     * Show list of all files uploaded to project
     * Used to show files uploaded to a project from form, expense and project
     * @param projectId  (required)
     * @return ProjectsProjectIdAllFilesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdAllFilesGet200Response projectsProjectIdAllFilesGet(String projectId) throws ApiException {
        ApiResponse<ProjectsProjectIdAllFilesGet200Response> localVarResp = projectsProjectIdAllFilesGetWithHttpInfo(projectId);
        return localVarResp.getData();
    }

    /**
     * Show list of all files uploaded to project
     * Used to show files uploaded to a project from form, expense and project
     * @param projectId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdAllFilesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdAllFilesGet200Response> projectsProjectIdAllFilesGetWithHttpInfo(String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdAllFilesGetValidateBeforeCall(projectId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdAllFilesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show list of all files uploaded to project (asynchronously)
     * Used to show files uploaded to a project from form, expense and project
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdAllFilesGetAsync(String projectId, final ApiCallback<ProjectsProjectIdAllFilesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdAllFilesGetValidateBeforeCall(projectId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdAllFilesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdDelete
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdDeleteCall(String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdDeleteValidateBeforeCall(String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdDelete(Async)");
        }

        return projectsProjectIdDeleteCall(projectId, _callback);

    }

    /**
     * Delete a project
     * 
     * @param projectId  (required)
     * @return ClockingRecordsClockingRecordIdDelete200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdDelete200Response projectsProjectIdDelete(String projectId) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdDelete200Response> localVarResp = projectsProjectIdDeleteWithHttpInfo(projectId);
        return localVarResp.getData();
    }

    /**
     * Delete a project
     * 
     * @param projectId  (required)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdDelete200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdDelete200Response> projectsProjectIdDeleteWithHttpInfo(String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdDeleteValidateBeforeCall(projectId, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdDelete200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a project (asynchronously)
     * 
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdDeleteAsync(String projectId, final ApiCallback<ClockingRecordsClockingRecordIdDelete200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdDeleteValidateBeforeCall(projectId, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdDelete200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdFilesFileIdDelete
     * @param projectId  (required)
     * @param fileId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdFilesFileIdDeleteCall(UUID projectId, UUID fileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/files/{file_id}/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "file_id" + "}", localVarApiClient.escapeString(fileId.toString()));

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
    private okhttp3.Call projectsProjectIdFilesFileIdDeleteValidateBeforeCall(UUID projectId, UUID fileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdFilesFileIdDelete(Async)");
        }

        // verify the required parameter 'fileId' is set
        if (fileId == null) {
            throw new ApiException("Missing the required parameter 'fileId' when calling projectsProjectIdFilesFileIdDelete(Async)");
        }

        return projectsProjectIdFilesFileIdDeleteCall(projectId, fileId, _callback);

    }

    /**
     * Delete file
     * Delete file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response projectsProjectIdFilesFileIdDelete(UUID projectId, UUID fileId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = projectsProjectIdFilesFileIdDeleteWithHttpInfo(projectId, fileId);
        return localVarResp.getData();
    }

    /**
     * Delete file
     * Delete file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> projectsProjectIdFilesFileIdDeleteWithHttpInfo(UUID projectId, UUID fileId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdFilesFileIdDeleteValidateBeforeCall(projectId, fileId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete file (asynchronously)
     * Delete file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdFilesFileIdDeleteAsync(UUID projectId, UUID fileId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdFilesFileIdDeleteValidateBeforeCall(projectId, fileId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdFilesFileIdGet
     * @param projectId  (required)
     * @param fileId  (required)
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
    public okhttp3.Call projectsProjectIdFilesFileIdGetCall(String projectId, String fileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/files/{file_id}/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "file_id" + "}", localVarApiClient.escapeString(fileId.toString()));

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
    private okhttp3.Call projectsProjectIdFilesFileIdGetValidateBeforeCall(String projectId, String fileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdFilesFileIdGet(Async)");
        }

        // verify the required parameter 'fileId' is set
        if (fileId == null) {
            throw new ApiException("Missing the required parameter 'fileId' when calling projectsProjectIdFilesFileIdGet(Async)");
        }

        return projectsProjectIdFilesFileIdGetCall(projectId, fileId, _callback);

    }

    /**
     * Show file
     * Show file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response projectsProjectIdFilesFileIdGet(String projectId, String fileId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = projectsProjectIdFilesFileIdGetWithHttpInfo(projectId, fileId);
        return localVarResp.getData();
    }

    /**
     * Show file
     * Show file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> projectsProjectIdFilesFileIdGetWithHttpInfo(String projectId, String fileId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdFilesFileIdGetValidateBeforeCall(projectId, fileId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show file (asynchronously)
     * Show file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
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
    public okhttp3.Call projectsProjectIdFilesFileIdGetAsync(String projectId, String fileId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdFilesFileIdGetValidateBeforeCall(projectId, fileId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdFilesFileIdPut
     * @param projectId  (required)
     * @param fileId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdFilesFileIdPutCall(UUID projectId, UUID fileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/files/{file_id}/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "file_id" + "}", localVarApiClient.escapeString(fileId.toString()));

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
    private okhttp3.Call projectsProjectIdFilesFileIdPutValidateBeforeCall(UUID projectId, UUID fileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdFilesFileIdPut(Async)");
        }

        // verify the required parameter 'fileId' is set
        if (fileId == null) {
            throw new ApiException("Missing the required parameter 'fileId' when calling projectsProjectIdFilesFileIdPut(Async)");
        }

        return projectsProjectIdFilesFileIdPutCall(projectId, fileId, _callback);

    }

    /**
     * Edit file
     * Edit file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response projectsProjectIdFilesFileIdPut(UUID projectId, UUID fileId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = projectsProjectIdFilesFileIdPutWithHttpInfo(projectId, fileId);
        return localVarResp.getData();
    }

    /**
     * Edit file
     * Edit file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> projectsProjectIdFilesFileIdPutWithHttpInfo(UUID projectId, UUID fileId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdFilesFileIdPutValidateBeforeCall(projectId, fileId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit file (asynchronously)
     * Edit file uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param fileId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdFilesFileIdPutAsync(UUID projectId, UUID fileId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdFilesFileIdPutValidateBeforeCall(projectId, fileId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdFilesGet
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdFilesGetCall(String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/files"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdFilesGetValidateBeforeCall(String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdFilesGet(Async)");
        }

        return projectsProjectIdFilesGetCall(projectId, _callback);

    }

    /**
     * Show list of files uploaded to project
     * Used to show files uploaded to a project from wall post or form
     * @param projectId  (required)
     * @return ProjectsProjectIdAllFilesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdAllFilesGet200Response projectsProjectIdFilesGet(String projectId) throws ApiException {
        ApiResponse<ProjectsProjectIdAllFilesGet200Response> localVarResp = projectsProjectIdFilesGetWithHttpInfo(projectId);
        return localVarResp.getData();
    }

    /**
     * Show list of files uploaded to project
     * Used to show files uploaded to a project from wall post or form
     * @param projectId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdAllFilesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdAllFilesGet200Response> projectsProjectIdFilesGetWithHttpInfo(String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdFilesGetValidateBeforeCall(projectId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdAllFilesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show list of files uploaded to project (asynchronously)
     * Used to show files uploaded to a project from wall post or form
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdFilesGetAsync(String projectId, final ApiCallback<ProjectsProjectIdAllFilesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdFilesGetValidateBeforeCall(projectId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdAllFilesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdGet
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdGetCall(String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdGetValidateBeforeCall(String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdGet(Async)");
        }

        return projectsProjectIdGetCall(projectId, _callback);

    }

    /**
     * View specific project
     * 
     * @param projectId  (required)
     * @return ProjectsProjectIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdGet200Response projectsProjectIdGet(String projectId) throws ApiException {
        ApiResponse<ProjectsProjectIdGet200Response> localVarResp = projectsProjectIdGetWithHttpInfo(projectId);
        return localVarResp.getData();
    }

    /**
     * View specific project
     * 
     * @param projectId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdGet200Response> projectsProjectIdGetWithHttpInfo(String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdGetValidateBeforeCall(projectId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * View specific project (asynchronously)
     * 
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdGetAsync(String projectId, final ApiCallback<ProjectsProjectIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdGetValidateBeforeCall(projectId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdProjectFilesGet
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesGetCall(String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/project_files"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdProjectFilesGetValidateBeforeCall(String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesGet(Async)");
        }

        return projectsProjectIdProjectFilesGetCall(projectId, _callback);

    }

    /**
     * Show list of project files uploaded to project
     * Returns files belonging to the project, not uploaded from wall post or form
     * @param projectId  (required)
     * @return ProjectsProjectIdAllFilesGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdAllFilesGet200Response projectsProjectIdProjectFilesGet(String projectId) throws ApiException {
        ApiResponse<ProjectsProjectIdAllFilesGet200Response> localVarResp = projectsProjectIdProjectFilesGetWithHttpInfo(projectId);
        return localVarResp.getData();
    }

    /**
     * Show list of project files uploaded to project
     * Returns files belonging to the project, not uploaded from wall post or form
     * @param projectId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdAllFilesGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdAllFilesGet200Response> projectsProjectIdProjectFilesGetWithHttpInfo(String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdProjectFilesGetValidateBeforeCall(projectId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdAllFilesGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show list of project files uploaded to project (asynchronously)
     * Returns files belonging to the project, not uploaded from wall post or form
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesGetAsync(String projectId, final ApiCallback<ProjectsProjectIdAllFilesGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdProjectFilesGetValidateBeforeCall(projectId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdAllFilesGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdProjectFilesPost
     * @param projectId  (required)
     * @param _file  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added project file </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesPostCall(String projectId, File _file, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/project_files"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (_file != null) {
            localVarFormParams.put("file", _file);
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
    private okhttp3.Call projectsProjectIdProjectFilesPostValidateBeforeCall(String projectId, File _file, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesPost(Async)");
        }

        // verify the required parameter '_file' is set
        if (_file == null) {
            throw new ApiException("Missing the required parameter '_file' when calling projectsProjectIdProjectFilesPost(Async)");
        }

        return projectsProjectIdProjectFilesPostCall(projectId, _file, _callback);

    }

    /**
     * Add project file to projects
     * 
     * @param projectId  (required)
     * @param _file  (required)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added project file </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response projectsProjectIdProjectFilesPost(String projectId, File _file) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = projectsProjectIdProjectFilesPostWithHttpInfo(projectId, _file);
        return localVarResp.getData();
    }

    /**
     * Add project file to projects
     * 
     * @param projectId  (required)
     * @param _file  (required)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added project file </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> projectsProjectIdProjectFilesPostWithHttpInfo(String projectId, File _file) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdProjectFilesPostValidateBeforeCall(projectId, _file, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add project file to projects (asynchronously)
     * 
     * @param projectId  (required)
     * @param _file  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successfully added project file </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesPostAsync(String projectId, File _file, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdProjectFilesPostValidateBeforeCall(projectId, _file, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdProjectFilesProjectFileIdDelete
     * @param projectFileId  (required)
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesProjectFileIdDeleteCall(UUID projectFileId, UUID projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/project_files/{project_file_id}/"
            .replace("{" + "project_file_id" + "}", localVarApiClient.escapeString(projectFileId.toString()))
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdProjectFilesProjectFileIdDeleteValidateBeforeCall(UUID projectFileId, UUID projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectFileId' is set
        if (projectFileId == null) {
            throw new ApiException("Missing the required parameter 'projectFileId' when calling projectsProjectIdProjectFilesProjectFileIdDelete(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesProjectFileIdDelete(Async)");
        }

        return projectsProjectIdProjectFilesProjectFileIdDeleteCall(projectFileId, projectId, _callback);

    }

    /**
     * Delete project file
     * 
     * @param projectFileId  (required)
     * @param projectId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response projectsProjectIdProjectFilesProjectFileIdDelete(UUID projectFileId, UUID projectId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = projectsProjectIdProjectFilesProjectFileIdDeleteWithHttpInfo(projectFileId, projectId);
        return localVarResp.getData();
    }

    /**
     * Delete project file
     * 
     * @param projectFileId  (required)
     * @param projectId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> projectsProjectIdProjectFilesProjectFileIdDeleteWithHttpInfo(UUID projectFileId, UUID projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdProjectFilesProjectFileIdDeleteValidateBeforeCall(projectFileId, projectId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete project file (asynchronously)
     * 
     * @param projectFileId  (required)
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesProjectFileIdDeleteAsync(UUID projectFileId, UUID projectId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdProjectFilesProjectFileIdDeleteValidateBeforeCall(projectFileId, projectId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdProjectFilesProjectFileIdGet
     * @param projectId  (required)
     * @param projectFileId  (required)
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
    public okhttp3.Call projectsProjectIdProjectFilesProjectFileIdGetCall(String projectId, String projectFileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/project_files/{project_file_id}/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "project_file_id" + "}", localVarApiClient.escapeString(projectFileId.toString()));

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
    private okhttp3.Call projectsProjectIdProjectFilesProjectFileIdGetValidateBeforeCall(String projectId, String projectFileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesProjectFileIdGet(Async)");
        }

        // verify the required parameter 'projectFileId' is set
        if (projectFileId == null) {
            throw new ApiException("Missing the required parameter 'projectFileId' when calling projectsProjectIdProjectFilesProjectFileIdGet(Async)");
        }

        return projectsProjectIdProjectFilesProjectFileIdGetCall(projectId, projectFileId, _callback);

    }

    /**
     * Show project file
     * 
     * @param projectId  (required)
     * @param projectFileId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response projectsProjectIdProjectFilesProjectFileIdGet(String projectId, String projectFileId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = projectsProjectIdProjectFilesProjectFileIdGetWithHttpInfo(projectId, projectFileId);
        return localVarResp.getData();
    }

    /**
     * Show project file
     * 
     * @param projectId  (required)
     * @param projectFileId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> projectsProjectIdProjectFilesProjectFileIdGetWithHttpInfo(String projectId, String projectFileId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdProjectFilesProjectFileIdGetValidateBeforeCall(projectId, projectFileId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show project file (asynchronously)
     * 
     * @param projectId  (required)
     * @param projectFileId  (required)
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
    public okhttp3.Call projectsProjectIdProjectFilesProjectFileIdGetAsync(String projectId, String projectFileId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdProjectFilesProjectFileIdGetValidateBeforeCall(projectId, projectFileId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdProjectFilesProjectFileIdPut
     * @param projectId  (required)
     * @param projectFileId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesProjectFileIdPutCall(UUID projectId, UUID projectFileId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/project_files/{project_file_id}/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()))
            .replace("{" + "project_file_id" + "}", localVarApiClient.escapeString(projectFileId.toString()));

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
    private okhttp3.Call projectsProjectIdProjectFilesProjectFileIdPutValidateBeforeCall(UUID projectId, UUID projectFileId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesProjectFileIdPut(Async)");
        }

        // verify the required parameter 'projectFileId' is set
        if (projectFileId == null) {
            throw new ApiException("Missing the required parameter 'projectFileId' when calling projectsProjectIdProjectFilesProjectFileIdPut(Async)");
        }

        return projectsProjectIdProjectFilesProjectFileIdPutCall(projectId, projectFileId, _callback);

    }

    /**
     * Edit project file
     * 
     * @param projectId  (required)
     * @param projectFileId  (required)
     * @return ExpenseFilesExpenseFileIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ExpenseFilesExpenseFileIdPut200Response projectsProjectIdProjectFilesProjectFileIdPut(UUID projectId, UUID projectFileId) throws ApiException {
        ApiResponse<ExpenseFilesExpenseFileIdPut200Response> localVarResp = projectsProjectIdProjectFilesProjectFileIdPutWithHttpInfo(projectId, projectFileId);
        return localVarResp.getData();
    }

    /**
     * Edit project file
     * 
     * @param projectId  (required)
     * @param projectFileId  (required)
     * @return ApiResponse&lt;ExpenseFilesExpenseFileIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ExpenseFilesExpenseFileIdPut200Response> projectsProjectIdProjectFilesProjectFileIdPutWithHttpInfo(UUID projectId, UUID projectFileId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdProjectFilesProjectFileIdPutValidateBeforeCall(projectId, projectFileId, null);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit project file (asynchronously)
     * 
     * @param projectId  (required)
     * @param projectFileId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdProjectFilesProjectFileIdPutAsync(UUID projectId, UUID projectFileId, final ApiCallback<ExpenseFilesExpenseFileIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdProjectFilesProjectFileIdPutValidateBeforeCall(projectId, projectFileId, _callback);
        Type localVarReturnType = new TypeToken<ExpenseFilesExpenseFileIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdPut
     * @param projectId  (required)
     * @param projectsProjectIdPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdPutCall(String projectId, ProjectsProjectIdPutRequest projectsProjectIdPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = projectsProjectIdPutRequest;

        // create path and map variables
        String localVarPath = "/projects/{project_id}"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdPutValidateBeforeCall(String projectId, ProjectsProjectIdPutRequest projectsProjectIdPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdPut(Async)");
        }

        return projectsProjectIdPutCall(projectId, projectsProjectIdPutRequest, _callback);

    }

    /**
     * Edit a project
     * 
     * @param projectId  (required)
     * @param projectsProjectIdPutRequest  (optional)
     * @return ClockingRecordsClockingRecordIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdPut200Response projectsProjectIdPut(String projectId, ProjectsProjectIdPutRequest projectsProjectIdPutRequest) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdPut200Response> localVarResp = projectsProjectIdPutWithHttpInfo(projectId, projectsProjectIdPutRequest);
        return localVarResp.getData();
    }

    /**
     * Edit a project
     * 
     * @param projectId  (required)
     * @param projectsProjectIdPutRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdPut200Response> projectsProjectIdPutWithHttpInfo(String projectId, ProjectsProjectIdPutRequest projectsProjectIdPutRequest) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdPutValidateBeforeCall(projectId, projectsProjectIdPutRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Edit a project (asynchronously)
     * 
     * @param projectId  (required)
     * @param projectsProjectIdPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdPutAsync(String projectId, ProjectsProjectIdPutRequest projectsProjectIdPutRequest, final ApiCallback<ClockingRecordsClockingRecordIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdPutValidateBeforeCall(projectId, projectsProjectIdPutRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdSendBulkPdfPost
     * @param projectId  (required)
     * @param projectsProjectIdSendBulkPdfPostRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdSendBulkPdfPostCall(String projectId, ProjectsProjectIdSendBulkPdfPostRequest projectsProjectIdSendBulkPdfPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = projectsProjectIdSendBulkPdfPostRequest;

        // create path and map variables
        String localVarPath = "/projects/{project_id}/send_bulk_pdf"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdSendBulkPdfPostValidateBeforeCall(String projectId, ProjectsProjectIdSendBulkPdfPostRequest projectsProjectIdSendBulkPdfPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdSendBulkPdfPost(Async)");
        }

        // verify the required parameter 'projectsProjectIdSendBulkPdfPostRequest' is set
        if (projectsProjectIdSendBulkPdfPostRequest == null) {
            throw new ApiException("Missing the required parameter 'projectsProjectIdSendBulkPdfPostRequest' when calling projectsProjectIdSendBulkPdfPost(Async)");
        }

        return projectsProjectIdSendBulkPdfPostCall(projectId, projectsProjectIdSendBulkPdfPostRequest, _callback);

    }

    /**
     * Send bulk forms pdf by email
     * 
     * @param projectId  (required)
     * @param projectsProjectIdSendBulkPdfPostRequest  (required)
     * @return EmptySuccessResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public EmptySuccessResponse projectsProjectIdSendBulkPdfPost(String projectId, ProjectsProjectIdSendBulkPdfPostRequest projectsProjectIdSendBulkPdfPostRequest) throws ApiException {
        ApiResponse<EmptySuccessResponse> localVarResp = projectsProjectIdSendBulkPdfPostWithHttpInfo(projectId, projectsProjectIdSendBulkPdfPostRequest);
        return localVarResp.getData();
    }

    /**
     * Send bulk forms pdf by email
     * 
     * @param projectId  (required)
     * @param projectsProjectIdSendBulkPdfPostRequest  (required)
     * @return ApiResponse&lt;EmptySuccessResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptySuccessResponse> projectsProjectIdSendBulkPdfPostWithHttpInfo(String projectId, ProjectsProjectIdSendBulkPdfPostRequest projectsProjectIdSendBulkPdfPostRequest) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdSendBulkPdfPostValidateBeforeCall(projectId, projectsProjectIdSendBulkPdfPostRequest, null);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Send bulk forms pdf by email (asynchronously)
     * 
     * @param projectId  (required)
     * @param projectsProjectIdSendBulkPdfPostRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdSendBulkPdfPostAsync(String projectId, ProjectsProjectIdSendBulkPdfPostRequest projectsProjectIdSendBulkPdfPostRequest, final ApiCallback<EmptySuccessResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdSendBulkPdfPostValidateBeforeCall(projectId, projectsProjectIdSendBulkPdfPostRequest, _callback);
        Type localVarReturnType = new TypeToken<EmptySuccessResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdUsersGet
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdUsersGetCall(String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/users/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdUsersGetValidateBeforeCall(String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdUsersGet(Async)");
        }

        return projectsProjectIdUsersGetCall(projectId, _callback);

    }

    /**
     * Show list of users added to project
     * 
     * @param projectId  (required)
     * @return ProjectsProjectIdUsersGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdUsersGet200Response projectsProjectIdUsersGet(String projectId) throws ApiException {
        ApiResponse<ProjectsProjectIdUsersGet200Response> localVarResp = projectsProjectIdUsersGetWithHttpInfo(projectId);
        return localVarResp.getData();
    }

    /**
     * Show list of users added to project
     * 
     * @param projectId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdUsersGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdUsersGet200Response> projectsProjectIdUsersGetWithHttpInfo(String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdUsersGetValidateBeforeCall(projectId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Show list of users added to project (asynchronously)
     * 
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdUsersGetAsync(String projectId, final ApiCallback<ProjectsProjectIdUsersGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdUsersGetValidateBeforeCall(projectId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdUsersPost
     * @param projectId  (required)
     * @param projectsProjectIdUsersPostRequest  (optional)
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
    public okhttp3.Call projectsProjectIdUsersPostCall(String projectId, ProjectsProjectIdUsersPostRequest projectsProjectIdUsersPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = projectsProjectIdUsersPostRequest;

        // create path and map variables
        String localVarPath = "/projects/{project_id}/users/"
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdUsersPostValidateBeforeCall(String projectId, ProjectsProjectIdUsersPostRequest projectsProjectIdUsersPostRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdUsersPost(Async)");
        }

        return projectsProjectIdUsersPostCall(projectId, projectsProjectIdUsersPostRequest, _callback);

    }

    /**
     * Add user to project
     * 
     * @param projectId  (required)
     * @param projectsProjectIdUsersPostRequest  (optional)
     * @return ClockingRecordsPost201Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsPost201Response projectsProjectIdUsersPost(String projectId, ProjectsProjectIdUsersPostRequest projectsProjectIdUsersPostRequest) throws ApiException {
        ApiResponse<ClockingRecordsPost201Response> localVarResp = projectsProjectIdUsersPostWithHttpInfo(projectId, projectsProjectIdUsersPostRequest);
        return localVarResp.getData();
    }

    /**
     * Add user to project
     * 
     * @param projectId  (required)
     * @param projectsProjectIdUsersPostRequest  (optional)
     * @return ApiResponse&lt;ClockingRecordsPost201Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Validation error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsPost201Response> projectsProjectIdUsersPostWithHttpInfo(String projectId, ProjectsProjectIdUsersPostRequest projectsProjectIdUsersPostRequest) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdUsersPostValidateBeforeCall(projectId, projectsProjectIdUsersPostRequest, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add user to project (asynchronously)
     * 
     * @param projectId  (required)
     * @param projectsProjectIdUsersPostRequest  (optional)
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
    public okhttp3.Call projectsProjectIdUsersPostAsync(String projectId, ProjectsProjectIdUsersPostRequest projectsProjectIdUsersPostRequest, final ApiCallback<ClockingRecordsPost201Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdUsersPostValidateBeforeCall(projectId, projectsProjectIdUsersPostRequest, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsPost201Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdUsersUserIdDelete
     * @param userId  (required)
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdUsersUserIdDeleteCall(String userId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/users/{user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()))
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdUsersUserIdDeleteValidateBeforeCall(String userId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling projectsProjectIdUsersUserIdDelete(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdUsersUserIdDelete(Async)");
        }

        return projectsProjectIdUsersUserIdDeleteCall(userId, projectId, _callback);

    }

    /**
     * Delete user from project
     * 
     * @param userId  (required)
     * @param projectId  (required)
     * @return ClockingRecordsClockingRecordIdPut200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ClockingRecordsClockingRecordIdPut200Response projectsProjectIdUsersUserIdDelete(String userId, String projectId) throws ApiException {
        ApiResponse<ClockingRecordsClockingRecordIdPut200Response> localVarResp = projectsProjectIdUsersUserIdDeleteWithHttpInfo(userId, projectId);
        return localVarResp.getData();
    }

    /**
     * Delete user from project
     * 
     * @param userId  (required)
     * @param projectId  (required)
     * @return ApiResponse&lt;ClockingRecordsClockingRecordIdPut200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClockingRecordsClockingRecordIdPut200Response> projectsProjectIdUsersUserIdDeleteWithHttpInfo(String userId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdUsersUserIdDeleteValidateBeforeCall(userId, projectId, null);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete user from project (asynchronously)
     * 
     * @param userId  (required)
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdUsersUserIdDeleteAsync(String userId, String projectId, final ApiCallback<ClockingRecordsClockingRecordIdPut200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdUsersUserIdDeleteValidateBeforeCall(userId, projectId, _callback);
        Type localVarReturnType = new TypeToken<ClockingRecordsClockingRecordIdPut200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for projectsProjectIdUsersUserIdGet
     * @param userId  (required)
     * @param projectId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdUsersUserIdGetCall(String userId, String projectId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/projects/{project_id}/users/{user_id}"
            .replace("{" + "user_id" + "}", localVarApiClient.escapeString(userId.toString()))
            .replace("{" + "project_id" + "}", localVarApiClient.escapeString(projectId.toString()));

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
    private okhttp3.Call projectsProjectIdUsersUserIdGetValidateBeforeCall(String userId, String projectId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'userId' is set
        if (userId == null) {
            throw new ApiException("Missing the required parameter 'userId' when calling projectsProjectIdUsersUserIdGet(Async)");
        }

        // verify the required parameter 'projectId' is set
        if (projectId == null) {
            throw new ApiException("Missing the required parameter 'projectId' when calling projectsProjectIdUsersUserIdGet(Async)");
        }

        return projectsProjectIdUsersUserIdGetCall(userId, projectId, _callback);

    }

    /**
     * View specific user assigned to project
     * 
     * @param userId  (required)
     * @param projectId  (required)
     * @return ProjectsProjectIdUsersUserIdGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProjectsProjectIdUsersUserIdGet200Response projectsProjectIdUsersUserIdGet(String userId, String projectId) throws ApiException {
        ApiResponse<ProjectsProjectIdUsersUserIdGet200Response> localVarResp = projectsProjectIdUsersUserIdGetWithHttpInfo(userId, projectId);
        return localVarResp.getData();
    }

    /**
     * View specific user assigned to project
     * 
     * @param userId  (required)
     * @param projectId  (required)
     * @return ApiResponse&lt;ProjectsProjectIdUsersUserIdGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectsProjectIdUsersUserIdGet200Response> projectsProjectIdUsersUserIdGetWithHttpInfo(String userId, String projectId) throws ApiException {
        okhttp3.Call localVarCall = projectsProjectIdUsersUserIdGetValidateBeforeCall(userId, projectId, null);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersUserIdGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * View specific user assigned to project (asynchronously)
     * 
     * @param userId  (required)
     * @param projectId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call projectsProjectIdUsersUserIdGetAsync(String userId, String projectId, final ApiCallback<ProjectsProjectIdUsersUserIdGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = projectsProjectIdUsersUserIdGetValidateBeforeCall(userId, projectId, _callback);
        Type localVarReturnType = new TypeToken<ProjectsProjectIdUsersUserIdGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
