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
import BulkActionRequestBody from '../model/BulkActionRequestBody';
import ClockingRecordsClockingRecordIdDelete200Response from '../model/ClockingRecordsClockingRecordIdDelete200Response';
import ClockingRecordsClockingRecordIdPut200Response from '../model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import ContactsContactIdGet200Response from '../model/ContactsContactIdGet200Response';
import ContactsGet200Response from '../model/ContactsGet200Response';
import ContactsPostRequest from '../model/ContactsPostRequest';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';

/**
* Contacts service.
* @module api/ContactsApi
* @version 0.0.42
*/
export default class ContactsApi {

    /**
    * Constructs a new ContactsApi. 
    * @alias module:api/ContactsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the bulkDeleteContacts operation.
     * @callback module:api/ContactsApi~bulkDeleteContactsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Bulk delete contacts
     * @param {module:model/BulkActionRequestBody} bulkActionRequestBody Contact ids
     * @param {module:api/ContactsApi~bulkDeleteContactsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    bulkDeleteContacts(bulkActionRequestBody, callback) {
      let postBody = bulkActionRequestBody;
      // verify the required parameter 'bulkActionRequestBody' is set
      if (bulkActionRequestBody === undefined || bulkActionRequestBody === null) {
        throw new Error("Missing the required parameter 'bulkActionRequestBody' when calling bulkDeleteContacts");
      }

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
        '/contacts/bulkDelete', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsContactIdDelete operation.
     * @callback module:api/ContactsApi~contactsContactIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdDelete200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a contact
     * @param {String} contactId 
     * @param {module:api/ContactsApi~contactsContactIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdDelete200Response}
     */
    contactsContactIdDelete(contactId, callback) {
      let postBody = null;
      // verify the required parameter 'contactId' is set
      if (contactId === undefined || contactId === null) {
        throw new Error("Missing the required parameter 'contactId' when calling contactsContactIdDelete");
      }

      let pathParams = {
        'contact_id': contactId
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
        '/contacts/{contact_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsContactIdGet operation.
     * @callback module:api/ContactsApi~contactsContactIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContactsContactIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Details of 1 contact
     * @param {String} contactId 
     * @param {module:api/ContactsApi~contactsContactIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContactsContactIdGet200Response}
     */
    contactsContactIdGet(contactId, callback) {
      let postBody = null;
      // verify the required parameter 'contactId' is set
      if (contactId === undefined || contactId === null) {
        throw new Error("Missing the required parameter 'contactId' when calling contactsContactIdGet");
      }

      let pathParams = {
        'contact_id': contactId
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
      let returnType = ContactsContactIdGet200Response;
      return this.apiClient.callApi(
        '/contacts/{contact_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsContactIdPut operation.
     * @callback module:api/ContactsApi~contactsContactIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a contact
     * @param {String} contactId 
     * @param {Object} opts Optional parameters
     * @param {module:model/ContactsPostRequest} [contactsPostRequest] 
     * @param {module:api/ContactsApi~contactsContactIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    contactsContactIdPut(contactId, opts, callback) {
      opts = opts || {};
      let postBody = opts['contactsPostRequest'];
      // verify the required parameter 'contactId' is set
      if (contactId === undefined || contactId === null) {
        throw new Error("Missing the required parameter 'contactId' when calling contactsContactIdPut");
      }

      let pathParams = {
        'contact_id': contactId
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
        '/contacts/{contact_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsGet operation.
     * @callback module:api/ContactsApi~contactsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContactsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of contacts
     * @param {Object} opts Optional parameters
     * @param {String} [name] Used to search for a contact with a specific name
     * @param {String} [cvr] Search for values in CVR field
     * @param {String} [ean] Search for values in EAN field
     * @param {String} [erpId] Search for values in ERP id field
     * @param {String} [contactType] Used to show only contacts with with one specific `ContactType`
     * @param {String} [city] Used to show only contacts with with one specific `City`
     * @param {String} [modifiedGte] 
     * @param {module:api/ContactsApi~contactsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContactsGet200Response}
     */
    contactsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'name': opts['name'],
        'cvr': opts['cvr'],
        'ean': opts['ean'],
        'erp_id': opts['erpId'],
        'contact_type': opts['contactType'],
        'city': opts['city'],
        'modified_gte': opts['modifiedGte']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ContactsGet200Response;
      return this.apiClient.callApi(
        '/contacts', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contactsPost operation.
     * @callback module:api/ContactsApi~contactsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a new contact
     * @param {Object} opts Optional parameters
     * @param {module:model/ContactsPostRequest} [contactsPostRequest] 
     * @param {module:api/ContactsApi~contactsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    contactsPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['contactsPostRequest'];

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
        '/contacts', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
