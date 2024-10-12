/**
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ClockingRecordsClockingRecordIdDelete200Response from '../model/ClockingRecordsClockingRecordIdDelete200Response';
import ClockingRecordsClockingRecordIdPut200Response from '../model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import ExpenseFilesExpenseFileIdPut200Response from '../model/ExpenseFilesExpenseFileIdPut200Response';
import ProjectsGet200Response from '../model/ProjectsGet200Response';
import ProjectsHasProjectsWithCustomStatusesGet200Response from '../model/ProjectsHasProjectsWithCustomStatusesGet200Response';
import ProjectsPostRequest from '../model/ProjectsPostRequest';
import ProjectsProjectIdAllFilesGet200Response from '../model/ProjectsProjectIdAllFilesGet200Response';
import ProjectsProjectIdGet200Response from '../model/ProjectsProjectIdGet200Response';
import ProjectsProjectIdPutRequest from '../model/ProjectsProjectIdPutRequest';
import ProjectsProjectIdSendBulkPdfPostRequest from '../model/ProjectsProjectIdSendBulkPdfPostRequest';
import ProjectsProjectIdUsersGet200Response from '../model/ProjectsProjectIdUsersGet200Response';
import ProjectsProjectIdUsersPostRequest from '../model/ProjectsProjectIdUsersPostRequest';
import ProjectsProjectIdUsersUserIdGet200Response from '../model/ProjectsProjectIdUsersUserIdGet200Response';

/**
* Projects service.
* @module api/ProjectsApi
* @version 0.0.42
*/
export default class ProjectsApi {

    /**
    * Constructs a new ProjectsApi. 
    * @alias module:api/ProjectsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the projectsGet operation.
     * @callback module:api/ProjectsApi~projectsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View list of projects
     * @param {Object} opts Optional parameters
     * @param {Boolean} [showAll = false)] Unless this is set to `true` only open projects will be shown
     * @param {String} [sort] Sort projects by `not_invoiced_amount`
     * @param {String} [direction] 
     * @param {String} [contactId] Used to filter on the `contact_id` of the projects
     * @param {String} [companyId] Used to filter on the `company_id` of the projects
     * @param {String} [projectStatusId] Used to filter on the `project_status_id` of the projects
     * @param {Array.<String>} [projectStatusIds] Used to filter on the `project_status_id` of the projects (match any of the provided values)
     * @param {String} [name] Used to search on the `name` of the projects
     * @param {String} [erpProjectId] Used to search on the `erp_project_id` of the projects
     * @param {String} [erpTaskId] Used to search on the `erp_task_id` of the projects
     * @param {String} [startTimeGte] Show projects with start time after than this value
     * @param {String} [startTimeLte] Show projects with start time before this value
     * @param {String} [startTimeEq] Show only projects with start time on specific date
     * @param {String} [eventStartGt] 
     * @param {String} [eventStartLt] 
     * @param {String} [eventStartEq] 
     * @param {String} [eventEndGt] 
     * @param {String} [eventEndLt] 
     * @param {String} [eventEndEq] 
     * @param {module:api/ProjectsApi~projectsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsGet200Response}
     */
    projectsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'show_all': opts['showAll'],
        'sort': opts['sort'],
        'direction': opts['direction'],
        'contact_id': opts['contactId'],
        'company_id': opts['companyId'],
        'project_status_id': opts['projectStatusId'],
        'project_status_ids': this.apiClient.buildCollectionParam(opts['projectStatusIds'], 'csv'),
        'name': opts['name'],
        'erp_project_id': opts['erpProjectId'],
        'erp_task_id': opts['erpTaskId'],
        'start_time_gte': opts['startTimeGte'],
        'start_time_lte': opts['startTimeLte'],
        'start_time_eq': opts['startTimeEq'],
        'event_start[][gt]': opts['eventStartGt'],
        'event_start[][lt]': opts['eventStartLt'],
        'event_start[][eq]': opts['eventStartEq'],
        'event_end[][gt]': opts['eventEndGt'],
        'event_end[][lt]': opts['eventEndLt'],
        'event_end[][eq]': opts['eventEndEq']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsGet200Response;
      return this.apiClient.callApi(
        '/projects', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsHasProjectsWithCustomStatusesGet_0 operation.
     * @callback module:api/ProjectsApi~projectsHasProjectsWithCustomStatusesGet_0Callback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsHasProjectsWithCustomStatusesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Check if the company has projects with custom statuses
     * @param {module:api/ProjectsApi~projectsHasProjectsWithCustomStatusesGet_0Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsHasProjectsWithCustomStatusesGet200Response}
     */
    projectsHasProjectsWithCustomStatusesGet_0(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsHasProjectsWithCustomStatusesGet200Response;
      return this.apiClient.callApi(
        '/projects/has_projects_with_custom_statuses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsPost operation.
     * @callback module:api/ProjectsApi~projectsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a project
     * @param {Object} opts Optional parameters
     * @param {module:model/ProjectsPostRequest} [projectsPostRequest] 
     * @param {module:api/ProjectsApi~projectsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    projectsPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['projectsPostRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ClockingRecordsPost201Response;
      return this.apiClient.callApi(
        '/projects', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdAllFilesGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdAllFilesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdAllFilesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show list of all files uploaded to project
     * Used to show files uploaded to a project from form, expense and project
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdAllFilesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdAllFilesGet200Response}
     */
    projectsProjectIdAllFilesGet(projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdAllFilesGet");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsProjectIdAllFilesGet200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/all_files', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdDelete operation.
     * @callback module:api/ProjectsApi~projectsProjectIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdDelete200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a project
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdDelete200Response}
     */
    projectsProjectIdDelete(projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdDelete");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClockingRecordsClockingRecordIdDelete200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdFilesFileIdDelete operation.
     * @callback module:api/ProjectsApi~projectsProjectIdFilesFileIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseFilesExpenseFileIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete file
     * Delete file uploaded to a project from wall post or form
     * @param {String} projectId 
     * @param {String} fileId 
     * @param {module:api/ProjectsApi~projectsProjectIdFilesFileIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    projectsProjectIdFilesFileIdDelete(projectId, fileId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdFilesFileIdDelete");
      }
      // verify the required parameter 'fileId' is set
      if (fileId === undefined || fileId === null) {
        throw new Error("Missing the required parameter 'fileId' when calling projectsProjectIdFilesFileIdDelete");
      }

      let pathParams = {
        'project_id': projectId,
        'file_id': fileId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpenseFilesExpenseFileIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/files/{file_id}/', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdFilesFileIdGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdFilesFileIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseFilesExpenseFileIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show file
     * Show file uploaded to a project from wall post or form
     * @param {String} projectId 
     * @param {String} fileId 
     * @param {module:api/ProjectsApi~projectsProjectIdFilesFileIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    projectsProjectIdFilesFileIdGet(projectId, fileId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdFilesFileIdGet");
      }
      // verify the required parameter 'fileId' is set
      if (fileId === undefined || fileId === null) {
        throw new Error("Missing the required parameter 'fileId' when calling projectsProjectIdFilesFileIdGet");
      }

      let pathParams = {
        'project_id': projectId,
        'file_id': fileId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpenseFilesExpenseFileIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/files/{file_id}/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdFilesFileIdPut operation.
     * @callback module:api/ProjectsApi~projectsProjectIdFilesFileIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseFilesExpenseFileIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit file
     * Edit file uploaded to a project from wall post or form
     * @param {String} projectId 
     * @param {String} fileId 
     * @param {module:api/ProjectsApi~projectsProjectIdFilesFileIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    projectsProjectIdFilesFileIdPut(projectId, fileId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdFilesFileIdPut");
      }
      // verify the required parameter 'fileId' is set
      if (fileId === undefined || fileId === null) {
        throw new Error("Missing the required parameter 'fileId' when calling projectsProjectIdFilesFileIdPut");
      }

      let pathParams = {
        'project_id': projectId,
        'file_id': fileId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpenseFilesExpenseFileIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/files/{file_id}/', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdFilesGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdFilesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdAllFilesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show list of files uploaded to project
     * Used to show files uploaded to a project from wall post or form
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdFilesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdAllFilesGet200Response}
     */
    projectsProjectIdFilesGet(projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdFilesGet");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsProjectIdAllFilesGet200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/files', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View specific project
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdGet200Response}
     */
    projectsProjectIdGet(projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdGet");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsProjectIdGet200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdProjectFilesGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdProjectFilesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdAllFilesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show list of project files uploaded to project
     * Returns files belonging to the project, not uploaded from wall post or form
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdProjectFilesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdAllFilesGet200Response}
     */
    projectsProjectIdProjectFilesGet(projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesGet");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsProjectIdAllFilesGet200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/project_files', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdProjectFilesPost operation.
     * @callback module:api/ProjectsApi~projectsProjectIdProjectFilesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add project file to projects
     * @param {String} projectId 
     * @param {File} file 
     * @param {module:api/ProjectsApi~projectsProjectIdProjectFilesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    projectsProjectIdProjectFilesPost(projectId, file, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesPost");
      }
      // verify the required parameter 'file' is set
      if (file === undefined || file === null) {
        throw new Error("Missing the required parameter 'file' when calling projectsProjectIdProjectFilesPost");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'file': file
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = ClockingRecordsPost201Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/project_files', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdProjectFilesProjectFileIdDelete operation.
     * @callback module:api/ProjectsApi~projectsProjectIdProjectFilesProjectFileIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseFilesExpenseFileIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete project file
     * @param {String} projectFileId 
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdProjectFilesProjectFileIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    projectsProjectIdProjectFilesProjectFileIdDelete(projectFileId, projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectFileId' is set
      if (projectFileId === undefined || projectFileId === null) {
        throw new Error("Missing the required parameter 'projectFileId' when calling projectsProjectIdProjectFilesProjectFileIdDelete");
      }
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesProjectFileIdDelete");
      }

      let pathParams = {
        'project_file_id': projectFileId,
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpenseFilesExpenseFileIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/project_files/{project_file_id}/', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdProjectFilesProjectFileIdGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdProjectFilesProjectFileIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseFilesExpenseFileIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show project file
     * @param {String} projectId 
     * @param {String} projectFileId 
     * @param {module:api/ProjectsApi~projectsProjectIdProjectFilesProjectFileIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    projectsProjectIdProjectFilesProjectFileIdGet(projectId, projectFileId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesProjectFileIdGet");
      }
      // verify the required parameter 'projectFileId' is set
      if (projectFileId === undefined || projectFileId === null) {
        throw new Error("Missing the required parameter 'projectFileId' when calling projectsProjectIdProjectFilesProjectFileIdGet");
      }

      let pathParams = {
        'project_id': projectId,
        'project_file_id': projectFileId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpenseFilesExpenseFileIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/project_files/{project_file_id}/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdProjectFilesProjectFileIdPut operation.
     * @callback module:api/ProjectsApi~projectsProjectIdProjectFilesProjectFileIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpenseFilesExpenseFileIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit project file
     * @param {String} projectId 
     * @param {String} projectFileId 
     * @param {module:api/ProjectsApi~projectsProjectIdProjectFilesProjectFileIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpenseFilesExpenseFileIdPut200Response}
     */
    projectsProjectIdProjectFilesProjectFileIdPut(projectId, projectFileId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdProjectFilesProjectFileIdPut");
      }
      // verify the required parameter 'projectFileId' is set
      if (projectFileId === undefined || projectFileId === null) {
        throw new Error("Missing the required parameter 'projectFileId' when calling projectsProjectIdProjectFilesProjectFileIdPut");
      }

      let pathParams = {
        'project_id': projectId,
        'project_file_id': projectFileId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpenseFilesExpenseFileIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/project_files/{project_file_id}/', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdPut operation.
     * @callback module:api/ProjectsApi~projectsProjectIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a project
     * @param {String} projectId 
     * @param {Object} opts Optional parameters
     * @param {module:model/ProjectsProjectIdPutRequest} [projectsProjectIdPutRequest] 
     * @param {module:api/ProjectsApi~projectsProjectIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    projectsProjectIdPut(projectId, opts, callback) {
      opts = opts || {};
      let postBody = opts['projectsProjectIdPutRequest'];
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdPut");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ClockingRecordsClockingRecordIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdSendBulkPdfPost operation.
     * @callback module:api/ProjectsApi~projectsProjectIdSendBulkPdfPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Send bulk forms pdf by email
     * @param {String} projectId 
     * @param {module:model/ProjectsProjectIdSendBulkPdfPostRequest} projectsProjectIdSendBulkPdfPostRequest 
     * @param {module:api/ProjectsApi~projectsProjectIdSendBulkPdfPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    projectsProjectIdSendBulkPdfPost(projectId, projectsProjectIdSendBulkPdfPostRequest, callback) {
      let postBody = projectsProjectIdSendBulkPdfPostRequest;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdSendBulkPdfPost");
      }
      // verify the required parameter 'projectsProjectIdSendBulkPdfPostRequest' is set
      if (projectsProjectIdSendBulkPdfPostRequest === undefined || projectsProjectIdSendBulkPdfPostRequest === null) {
        throw new Error("Missing the required parameter 'projectsProjectIdSendBulkPdfPostRequest' when calling projectsProjectIdSendBulkPdfPost");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/projects/{project_id}/send_bulk_pdf', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdUsersGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdUsersGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdUsersGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show list of users added to project
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdUsersGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdUsersGet200Response}
     */
    projectsProjectIdUsersGet(projectId, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdUsersGet");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsProjectIdUsersGet200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/users/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdUsersPost operation.
     * @callback module:api/ProjectsApi~projectsProjectIdUsersPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add user to project
     * @param {String} projectId 
     * @param {Object} opts Optional parameters
     * @param {module:model/ProjectsProjectIdUsersPostRequest} [projectsProjectIdUsersPostRequest] 
     * @param {module:api/ProjectsApi~projectsProjectIdUsersPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    projectsProjectIdUsersPost(projectId, opts, callback) {
      opts = opts || {};
      let postBody = opts['projectsProjectIdUsersPostRequest'];
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdUsersPost");
      }

      let pathParams = {
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ClockingRecordsPost201Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/users/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdUsersUserIdDelete operation.
     * @callback module:api/ProjectsApi~projectsProjectIdUsersUserIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete user from project
     * @param {String} userId 
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdUsersUserIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    projectsProjectIdUsersUserIdDelete(userId, projectId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling projectsProjectIdUsersUserIdDelete");
      }
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdUsersUserIdDelete");
      }

      let pathParams = {
        'user_id': userId,
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClockingRecordsClockingRecordIdPut200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/users/{user_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectsProjectIdUsersUserIdGet operation.
     * @callback module:api/ProjectsApi~projectsProjectIdUsersUserIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdUsersUserIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View specific user assigned to project
     * @param {String} userId 
     * @param {String} projectId 
     * @param {module:api/ProjectsApi~projectsProjectIdUsersUserIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdUsersUserIdGet200Response}
     */
    projectsProjectIdUsersUserIdGet(userId, projectId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling projectsProjectIdUsersUserIdGet");
      }
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling projectsProjectIdUsersUserIdGet");
      }

      let pathParams = {
        'user_id': userId,
        'project_id': projectId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ProjectsProjectIdUsersUserIdGet200Response;
      return this.apiClient.callApi(
        '/projects/{project_id}/users/{user_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
