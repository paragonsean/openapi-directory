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
import BulkActionRequestBody from '../model/BulkActionRequestBody';
import ClockingRecordsClockingRecordIdPut200Response from '../model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import CompaniesCompanyIdIntegrationSettingsPostRequest from '../model/CompaniesCompanyIdIntegrationSettingsPostRequest';
import CreateSuccessResponse from '../model/CreateSuccessResponse';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import ForbiddenError from '../model/ForbiddenError';
import ProjectsProjectIdUsersGet200Response from '../model/ProjectsProjectIdUsersGet200Response';
import ProjectsProjectIdUsersUserIdGet200Response from '../model/ProjectsProjectIdUsersUserIdGet200Response';
import UsersPostRequest from '../model/UsersPostRequest';
import UsersResendWelcomeSmsGet200Response from '../model/UsersResendWelcomeSmsGet200Response';
import UsersUserIdIntegrationSettingsGet200Response from '../model/UsersUserIdIntegrationSettingsGet200Response';
import UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response from '../model/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response';

/**
* Users service.
* @module api/UsersApi
* @version 0.0.42
*/
export default class UsersApi {

    /**
    * Constructs a new UsersApi. 
    * @alias module:api/UsersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the usersBulkActivate operation.
     * @callback module:api/UsersApi~usersBulkActivateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Activate multiple users
     * @param {Object} opts Optional parameters
     * @param {module:model/BulkActionRequestBody} [bulkActionRequestBody] User ids
     * @param {module:api/UsersApi~usersBulkActivateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    usersBulkActivate(opts, callback) {
      opts = opts || {};
      let postBody = opts['bulkActionRequestBody'];

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
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/users/bulkActivate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersBulkDeactivate operation.
     * @callback module:api/UsersApi~usersBulkDeactivateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deactivate multiple users
     * @param {Object} opts Optional parameters
     * @param {module:model/BulkActionRequestBody} [bulkActionRequestBody] User ids
     * @param {module:api/UsersApi~usersBulkDeactivateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    usersBulkDeactivate(opts, callback) {
      opts = opts || {};
      let postBody = opts['bulkActionRequestBody'];

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
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/users/bulkDeactivate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersGet operation.
     * @callback module:api/UsersApi~usersGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdUsersGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get list of users in company
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] Used to filter on the `first_name` of the users
     * @param {String} [lastName] Used to filter on the `last_name` of the users
     * @param {String} [email] Used to filter on the `email` of the users
     * @param {String} [stockLocationId] Used to filter on the `stock_location_id` of the users
     * @param {Boolean} [isActive] Filters active/inactive users
     * @param {module:api/UsersApi~usersGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdUsersGet200Response}
     */
    usersGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'email': opts['email'],
        'stock_location_id': opts['stockLocationId'],
        'is_active': opts['isActive']
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
        '/users', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersPost operation.
     * @callback module:api/UsersApi~usersPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add user to company
     * @param {Object} opts Optional parameters
     * @param {module:model/UsersPostRequest} [usersPostRequest] 
     * @param {module:api/UsersApi~usersPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    usersPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['usersPostRequest'];

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
        '/users', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersResendWelcomeSmsGet operation.
     * @callback module:api/UsersApi~usersResendWelcomeSmsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UsersResendWelcomeSmsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Resend Welcome SMS to the user
     * @param {module:api/UsersApi~usersResendWelcomeSmsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UsersResendWelcomeSmsGet200Response}
     */
    usersResendWelcomeSmsGet(callback) {
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
      let returnType = UsersResendWelcomeSmsGet200Response;
      return this.apiClient.callApi(
        '/users/resendWelcomeSms', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdDelete operation.
     * @callback module:api/UsersApi~usersUserIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete user
     * @param {String} userId 
     * @param {module:api/UsersApi~usersUserIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    usersUserIdDelete(userId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdDelete");
      }

      let pathParams = {
        'user_id': userId
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
        '/users/{user_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdGet operation.
     * @callback module:api/UsersApi~usersUserIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProjectsProjectIdUsersUserIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View user
     * @param {String} userId 
     * @param {module:api/UsersApi~usersUserIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProjectsProjectIdUsersUserIdGet200Response}
     */
    usersUserIdGet(userId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdGet");
      }

      let pathParams = {
        'user_id': userId
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
        '/users/{user_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdIntegrationSettingsGet operation.
     * @callback module:api/UsersApi~usersUserIdIntegrationSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UsersUserIdIntegrationSettingsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of user integration settings
     * @param {String} userId 
     * @param {module:api/UsersApi~usersUserIdIntegrationSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UsersUserIdIntegrationSettingsGet200Response}
     */
    usersUserIdIntegrationSettingsGet(userId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsGet");
      }

      let pathParams = {
        'user_id': userId
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
      let returnType = UsersUserIdIntegrationSettingsGet200Response;
      return this.apiClient.callApi(
        '/users/{user_id}/integration_settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete operation.
     * @callback module:api/UsersApi~usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a user integration setting
     * @param {String} userId 
     * @param {String} integrationSettingsUserId 
     * @param {module:api/UsersApi~usersUserIdIntegrationSettingsIntegrationSettingsUserIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete(userId, integrationSettingsUserId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete");
      }
      // verify the required parameter 'integrationSettingsUserId' is set
      if (integrationSettingsUserId === undefined || integrationSettingsUserId === null) {
        throw new Error("Missing the required parameter 'integrationSettingsUserId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdDelete");
      }

      let pathParams = {
        'user_id': userId,
        'integration_settings_user_id': integrationSettingsUserId
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
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/users/{user_id}/integration_settings/{integration_settings_user_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet operation.
     * @callback module:api/UsersApi~usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a user integration setting
     * @param {String} userId 
     * @param {String} integrationSettingsUserId 
     * @param {module:api/UsersApi~usersUserIdIntegrationSettingsIntegrationSettingsUserIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response}
     */
    usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet(userId, integrationSettingsUserId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet");
      }
      // verify the required parameter 'integrationSettingsUserId' is set
      if (integrationSettingsUserId === undefined || integrationSettingsUserId === null) {
        throw new Error("Missing the required parameter 'integrationSettingsUserId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdGet");
      }

      let pathParams = {
        'user_id': userId,
        'integration_settings_user_id': integrationSettingsUserId
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
      let returnType = UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response;
      return this.apiClient.callApi(
        '/users/{user_id}/integration_settings/{integration_settings_user_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut operation.
     * @callback module:api/UsersApi~usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a user integration setting
     * @param {String} userId 
     * @param {String} integrationSettingsUserId 
     * @param {module:api/UsersApi~usersUserIdIntegrationSettingsIntegrationSettingsUserIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut(userId, integrationSettingsUserId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut");
      }
      // verify the required parameter 'integrationSettingsUserId' is set
      if (integrationSettingsUserId === undefined || integrationSettingsUserId === null) {
        throw new Error("Missing the required parameter 'integrationSettingsUserId' when calling usersUserIdIntegrationSettingsIntegrationSettingsUserIdPut");
      }

      let pathParams = {
        'user_id': userId,
        'integration_settings_user_id': integrationSettingsUserId
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
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/users/{user_id}/integration_settings/{integration_settings_user_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdIntegrationSettingsPost operation.
     * @callback module:api/UsersApi~usersUserIdIntegrationSettingsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a user integration setting
     * @param {String} userId 
     * @param {Object} opts Optional parameters
     * @param {module:model/CompaniesCompanyIdIntegrationSettingsPostRequest} [companiesCompanyIdIntegrationSettingsPostRequest] 
     * @param {module:api/UsersApi~usersUserIdIntegrationSettingsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    usersUserIdIntegrationSettingsPost(userId, opts, callback) {
      opts = opts || {};
      let postBody = opts['companiesCompanyIdIntegrationSettingsPostRequest'];
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdIntegrationSettingsPost");
      }

      let pathParams = {
        'user_id': userId
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
      let returnType = CreateSuccessResponse;
      return this.apiClient.callApi(
        '/users/{user_id}/integration_settings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdPut operation.
     * @callback module:api/UsersApi~usersUserIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit user
     * @param {String} userId 
     * @param {module:api/UsersApi~usersUserIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    usersUserIdPut(userId, callback) {
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdPut");
      }

      let pathParams = {
        'user_id': userId
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
        '/users/{user_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the usersUserIdUploadImagePost operation.
     * @callback module:api/UsersApi~usersUserIdUploadImagePostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upload a new image to a user
     * @param {String} userId 
     * @param {Object} opts Optional parameters
     * @param {File} [image] 
     * @param {module:api/UsersApi~usersUserIdUploadImagePostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    usersUserIdUploadImagePost(userId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'userId' is set
      if (userId === undefined || userId === null) {
        throw new Error("Missing the required parameter 'userId' when calling usersUserIdUploadImagePost");
      }

      let pathParams = {
        'user_id': userId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'image': opts['image']
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = CreateSuccessResponse;
      return this.apiClient.callApi(
        '/users/{user_id}/uploadImage', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
