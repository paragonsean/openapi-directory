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
import ClockingRecordsClockingRecordIdPut200Response from '../model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import ErrorValidation from '../model/ErrorValidation';
import TimeEntriesGet200Response from '../model/TimeEntriesGet200Response';
import TimeEntriesPostRequest from '../model/TimeEntriesPostRequest';
import TimeEntriesTimeEntryIdGet200Response from '../model/TimeEntriesTimeEntryIdGet200Response';

/**
* TimeEntries service.
* @module api/TimeEntriesApi
* @version 0.0.42
*/
export default class TimeEntriesApi {

    /**
    * Constructs a new TimeEntriesApi. 
    * @alias module:api/TimeEntriesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the timeEntriesGet operation.
     * @callback module:api/TimeEntriesApi~timeEntriesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimeEntriesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List time entries
     * @param {Object} opts Optional parameters
     * @param {String} [userId] 
     * @param {String} [formId] 
     * @param {String} [projectId] 
     * @param {String} [gtFromTime] 
     * @param {String} [ltFromTime] 
     * @param {String} [gtToTime] 
     * @param {String} [ltToTime] 
     * @param {String} [ltSum] 
     * @param {String} [gtSum] 
     * @param {module:api/TimeEntriesApi~timeEntriesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimeEntriesGet200Response}
     */
    timeEntriesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'user_id': opts['userId'],
        'form_id': opts['formId'],
        'project_id': opts['projectId'],
        'gt_from_time': opts['gtFromTime'],
        'lt_from_time': opts['ltFromTime'],
        'gt_to_time': opts['gtToTime'],
        'lt_to_time': opts['ltToTime'],
        'lt_sum': opts['ltSum'],
        'gt_sum': opts['gtSum']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TimeEntriesGet200Response;
      return this.apiClient.callApi(
        '/time_entries', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timeEntriesPost operation.
     * @callback module:api/TimeEntriesApi~timeEntriesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add new time entry
     * @param {Object} opts Optional parameters
     * @param {module:model/TimeEntriesPostRequest} [timeEntriesPostRequest] 
     * @param {module:api/TimeEntriesApi~timeEntriesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    timeEntriesPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['timeEntriesPostRequest'];

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
        '/time_entries', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timeEntriesTimeEntryIdDelete operation.
     * @callback module:api/TimeEntriesApi~timeEntriesTimeEntryIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete time entry
     * @param {String} timeEntryId 
     * @param {module:api/TimeEntriesApi~timeEntriesTimeEntryIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    timeEntriesTimeEntryIdDelete(timeEntryId, callback) {
      let postBody = null;
      // verify the required parameter 'timeEntryId' is set
      if (timeEntryId === undefined || timeEntryId === null) {
        throw new Error("Missing the required parameter 'timeEntryId' when calling timeEntriesTimeEntryIdDelete");
      }

      let pathParams = {
        'time_entry_id': timeEntryId
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
        '/time_entries/{time_entry_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timeEntriesTimeEntryIdGet operation.
     * @callback module:api/TimeEntriesApi~timeEntriesTimeEntryIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TimeEntriesTimeEntryIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View time entry
     * @param {String} timeEntryId 
     * @param {module:api/TimeEntriesApi~timeEntriesTimeEntryIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TimeEntriesTimeEntryIdGet200Response}
     */
    timeEntriesTimeEntryIdGet(timeEntryId, callback) {
      let postBody = null;
      // verify the required parameter 'timeEntryId' is set
      if (timeEntryId === undefined || timeEntryId === null) {
        throw new Error("Missing the required parameter 'timeEntryId' when calling timeEntriesTimeEntryIdGet");
      }

      let pathParams = {
        'time_entry_id': timeEntryId
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
      let returnType = TimeEntriesTimeEntryIdGet200Response;
      return this.apiClient.callApi(
        '/time_entries/{time_entry_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timeEntriesTimeEntryIdPut operation.
     * @callback module:api/TimeEntriesApi~timeEntriesTimeEntryIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit time entry
     * @param {String} timeEntryId 
     * @param {module:api/TimeEntriesApi~timeEntriesTimeEntryIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    timeEntriesTimeEntryIdPut(timeEntryId, callback) {
      let postBody = null;
      // verify the required parameter 'timeEntryId' is set
      if (timeEntryId === undefined || timeEntryId === null) {
        throw new Error("Missing the required parameter 'timeEntryId' when calling timeEntriesTimeEntryIdPut");
      }

      let pathParams = {
        'time_entry_id': timeEntryId
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
        '/time_entries/{time_entry_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
