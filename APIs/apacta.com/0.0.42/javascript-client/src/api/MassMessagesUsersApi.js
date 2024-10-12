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
import MassMessagesUsersGet200Response from '../model/MassMessagesUsersGet200Response';
import MassMessagesUsersMassMessagesUserIdGet200Response from '../model/MassMessagesUsersMassMessagesUserIdGet200Response';

/**
* MassMessagesUsers service.
* @module api/MassMessagesUsersApi
* @version 0.0.42
*/
export default class MassMessagesUsersApi {

    /**
    * Constructs a new MassMessagesUsersApi. 
    * @alias module:api/MassMessagesUsersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the massMessagesUsersGet operation.
     * @callback module:api/MassMessagesUsersApi~massMessagesUsersGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MassMessagesUsersGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View list of mass messages for specific user
     * @param {Object} opts Optional parameters
     * @param {Boolean} [isRead] Used to filter on the `is_read` of the mass messages
     * @param {module:api/MassMessagesUsersApi~massMessagesUsersGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MassMessagesUsersGet200Response}
     */
    massMessagesUsersGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'is_read': opts['isRead']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MassMessagesUsersGet200Response;
      return this.apiClient.callApi(
        '/mass_messages_users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the massMessagesUsersMassMessagesUserIdGet operation.
     * @callback module:api/MassMessagesUsersApi~massMessagesUsersMassMessagesUserIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MassMessagesUsersMassMessagesUserIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View mass message
     * @param {String} massMessagesUserId 
     * @param {module:api/MassMessagesUsersApi~massMessagesUsersMassMessagesUserIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MassMessagesUsersMassMessagesUserIdGet200Response}
     */
    massMessagesUsersMassMessagesUserIdGet(massMessagesUserId, callback) {
      let postBody = null;
      // verify the required parameter 'massMessagesUserId' is set
      if (massMessagesUserId === undefined || massMessagesUserId === null) {
        throw new Error("Missing the required parameter 'massMessagesUserId' when calling massMessagesUsersMassMessagesUserIdGet");
      }

      let pathParams = {
        'mass_messages_user_id': massMessagesUserId
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
      let returnType = MassMessagesUsersMassMessagesUserIdGet200Response;
      return this.apiClient.callApi(
        '/mass_messages_users/{mass_messages_user_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the massMessagesUsersMassMessagesUserIdPut operation.
     * @callback module:api/MassMessagesUsersApi~massMessagesUsersMassMessagesUserIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit mass message
     * @param {String} massMessagesUserId 
     * @param {module:api/MassMessagesUsersApi~massMessagesUsersMassMessagesUserIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    massMessagesUsersMassMessagesUserIdPut(massMessagesUserId, callback) {
      let postBody = null;
      // verify the required parameter 'massMessagesUserId' is set
      if (massMessagesUserId === undefined || massMessagesUserId === null) {
        throw new Error("Missing the required parameter 'massMessagesUserId' when calling massMessagesUsersMassMessagesUserIdPut");
      }

      let pathParams = {
        'mass_messages_user_id': massMessagesUserId
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
        '/mass_messages_users/{mass_messages_user_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
