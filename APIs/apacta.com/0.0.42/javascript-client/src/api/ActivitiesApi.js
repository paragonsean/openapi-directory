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
import ActivitiesGet200Response from '../model/ActivitiesGet200Response';
import ActivitiesPostRequest from '../model/ActivitiesPostRequest';
import BadRequestResponse from '../model/BadRequestResponse';
import BulkActionRequestBody from '../model/BulkActionRequestBody';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import ForbiddenError from '../model/ForbiddenError';

/**
* Activities service.
* @module api/ActivitiesApi
* @version 0.0.42
*/
export default class ActivitiesApi {

    /**
    * Constructs a new ActivitiesApi. 
    * @alias module:api/ActivitiesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the activitiesActivityIdDelete operation.
     * @callback module:api/ActivitiesApi~activitiesActivityIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an activity
     * @param {String} activityId 
     * @param {module:api/ActivitiesApi~activitiesActivityIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    activitiesActivityIdDelete(activityId, callback) {
      let postBody = null;
      // verify the required parameter 'activityId' is set
      if (activityId === undefined || activityId === null) {
        throw new Error("Missing the required parameter 'activityId' when calling activitiesActivityIdDelete");
      }

      let pathParams = {
        'activity_id': activityId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/activities/{activity_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the activitiesActivityIdPut operation.
     * @callback module:api/ActivitiesApi~activitiesActivityIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit an activity
     * @param {String} activityId 
     * @param {module:model/ActivitiesPostRequest} activitiesPostRequest 
     * @param {module:api/ActivitiesApi~activitiesActivityIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    activitiesActivityIdPut(activityId, activitiesPostRequest, callback) {
      let postBody = activitiesPostRequest;
      // verify the required parameter 'activityId' is set
      if (activityId === undefined || activityId === null) {
        throw new Error("Missing the required parameter 'activityId' when calling activitiesActivityIdPut");
      }
      // verify the required parameter 'activitiesPostRequest' is set
      if (activitiesPostRequest === undefined || activitiesPostRequest === null) {
        throw new Error("Missing the required parameter 'activitiesPostRequest' when calling activitiesActivityIdPut");
      }

      let pathParams = {
        'activity_id': activityId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/activities/{activity_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the activitiesBulkDeleteDelete operation.
     * @callback module:api/ActivitiesApi~activitiesBulkDeleteDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Bulk delete activities
     * @param {module:model/BulkActionRequestBody} bulkActionRequestBody Activities ids
     * @param {module:api/ActivitiesApi~activitiesBulkDeleteDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    activitiesBulkDeleteDelete(bulkActionRequestBody, callback) {
      let postBody = bulkActionRequestBody;
      // verify the required parameter 'bulkActionRequestBody' is set
      if (bulkActionRequestBody === undefined || bulkActionRequestBody === null) {
        throw new Error("Missing the required parameter 'bulkActionRequestBody' when calling activitiesBulkDeleteDelete");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/activities/bulkDelete', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the activitiesGet operation.
     * @callback module:api/ActivitiesApi~activitiesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ActivitiesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of activities
     * @param {module:api/ActivitiesApi~activitiesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ActivitiesGet200Response}
     */
    activitiesGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ActivitiesGet200Response;
      return this.apiClient.callApi(
        '/activities', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the activitiesPost operation.
     * @callback module:api/ActivitiesApi~activitiesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create an activity
     * @param {module:model/ActivitiesPostRequest} activitiesPostRequest 
     * @param {module:api/ActivitiesApi~activitiesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    activitiesPost(activitiesPostRequest, callback) {
      let postBody = activitiesPostRequest;
      // verify the required parameter 'activitiesPostRequest' is set
      if (activitiesPostRequest === undefined || activitiesPostRequest === null) {
        throw new Error("Missing the required parameter 'activitiesPostRequest' when calling activitiesPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/activities', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
