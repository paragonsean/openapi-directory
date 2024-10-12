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
import BadRequestResponse from '../model/BadRequestResponse';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import EventsEventIdGet200Response from '../model/EventsEventIdGet200Response';
import EventsGet200Response from '../model/EventsGet200Response';
import EventsIsUserFreeGet200Response from '../model/EventsIsUserFreeGet200Response';
import EventsPostRequest from '../model/EventsPostRequest';

/**
* Events service.
* @module api/EventsApi
* @version 0.0.42
*/
export default class EventsApi {

    /**
    * Constructs a new EventsApi. 
    * @alias module:api/EventsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the eventsEventIdDelete operation.
     * @callback module:api/EventsApi~eventsEventIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventsEventIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete event
     * @param {String} eventId 
     * @param {module:api/EventsApi~eventsEventIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventsEventIdGet200Response}
     */
    eventsEventIdDelete(eventId, callback) {
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling eventsEventIdDelete");
      }

      let pathParams = {
        'event_id': eventId
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
      let returnType = EventsEventIdGet200Response;
      return this.apiClient.callApi(
        '/events/{event_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventsEventIdGet operation.
     * @callback module:api/EventsApi~eventsEventIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventsEventIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show event
     * @param {String} eventId 
     * @param {module:api/EventsApi~eventsEventIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventsEventIdGet200Response}
     */
    eventsEventIdGet(eventId, callback) {
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling eventsEventIdGet");
      }

      let pathParams = {
        'event_id': eventId
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
      let returnType = EventsEventIdGet200Response;
      return this.apiClient.callApi(
        '/events/{event_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventsEventIdPut operation.
     * @callback module:api/EventsApi~eventsEventIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventsEventIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit event
     * @param {String} eventId 
     * @param {module:api/EventsApi~eventsEventIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventsEventIdGet200Response}
     */
    eventsEventIdPut(eventId, callback) {
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling eventsEventIdPut");
      }

      let pathParams = {
        'event_id': eventId
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
      let returnType = EventsEventIdGet200Response;
      return this.apiClient.callApi(
        '/events/{event_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventsGet operation.
     * @callback module:api/EventsApi~eventsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show list of events
     * @param {Object} opts Optional parameters
     * @param {String} [userId] 
     * @param {String} [projectId] 
     * @param {String} [startGt] 
     * @param {String} [startLt] 
     * @param {String} [startEq] 
     * @param {String} [endGt] 
     * @param {String} [endLt] 
     * @param {String} [endEq] 
     * @param {String} [tags] List events with given tag ids separated by comma. Example tags=0377d6ce-db5e-4b1e-ac3a-8ca39ea3142e,8cec327e-a559-4b40-9ed6-316b9de46743
     * @param {Boolean} [withoutUsers] List events without attached user
     * @param {module:api/EventsApi~eventsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventsGet200Response}
     */
    eventsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'user_id': opts['userId'],
        'project_id': opts['projectId'],
        'start[][gt]': opts['startGt'],
        'start[][lt]': opts['startLt'],
        'start[][eq]': opts['startEq'],
        'end[][gt]': opts['endGt'],
        'end[][lt]': opts['endLt'],
        'end[][eq]': opts['endEq'],
        'tags': opts['tags'],
        'without_users': opts['withoutUsers']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EventsGet200Response;
      return this.apiClient.callApi(
        '/events', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventsIsUserFreeGet operation.
     * @callback module:api/EventsApi~eventsIsUserFreeGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventsIsUserFreeGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Check if user is available at given datetime range
     * @param {String} userId 
     * @param {String} start 
     * @param {String} end 
     * @param {module:api/EventsApi~eventsIsUserFreeGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventsIsUserFreeGet200Response}
     */
    eventsIsUserFreeGet(userId, start, end, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling eventsIsUserFreeGet");
      }
      // verify the required parameter 'start' is set
      if (start === undefined || start === null) {
        throw new Error("Missing the required parameter 'start' when calling eventsIsUserFreeGet");
      }
      // verify the required parameter 'end' is set
      if (end === undefined || end === null) {
        throw new Error("Missing the required parameter 'end' when calling eventsIsUserFreeGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'user_id': userId,
        'start': start,
        'end': end
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EventsIsUserFreeGet200Response;
      return this.apiClient.callApi(
        '/events/is_user_free', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eventsPost operation.
     * @callback module:api/EventsApi~eventsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create event
     * @param {Object} opts Optional parameters
     * @param {module:model/EventsPostRequest} [eventsPostRequest] 
     * @param {module:api/EventsApi~eventsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    eventsPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['eventsPostRequest'];

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
        '/events', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
