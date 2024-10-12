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
import AddCompaniesVendorRequest from '../model/AddCompaniesVendorRequest';
import BulkActionRequestBody from '../model/BulkActionRequestBody';
import ClockingRecordsClockingRecordIdDelete200Response from '../model/ClockingRecordsClockingRecordIdDelete200Response';
import ClockingRecordsClockingRecordIdPut200Response from '../model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import GetCompaiesVendorsList200Response from '../model/GetCompaiesVendorsList200Response';
import GetCompaniesVendor200Response from '../model/GetCompaniesVendor200Response';
import GetCompaniesVendorsExpenseStatistics200Response from '../model/GetCompaniesVendorsExpenseStatistics200Response';

/**
* CompaniesVendors service.
* @module api/CompaniesVendorsApi
* @version 0.0.42
*/
export default class CompaniesVendorsApi {

    /**
    * Constructs a new CompaniesVendorsApi. 
    * @alias module:api/CompaniesVendorsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addCompaniesVendor operation.
     * @callback module:api/CompaniesVendorsApi~addCompaniesVendorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a new companies vendor
     * @param {Object} opts Optional parameters
     * @param {module:model/AddCompaniesVendorRequest} [addCompaniesVendorRequest] 
     * @param {module:api/CompaniesVendorsApi~addCompaniesVendorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    addCompaniesVendor(opts, callback) {
      opts = opts || {};
      let postBody = opts['addCompaniesVendorRequest'];

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
        '/companies_vendors', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the bulkCompaniesVendors operation.
     * @callback module:api/CompaniesVendorsApi~bulkCompaniesVendorsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Bulk delete companies vendors
     * @param {module:model/BulkActionRequestBody} bulkActionRequestBody Companies vendors ids
     * @param {module:api/CompaniesVendorsApi~bulkCompaniesVendorsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    bulkCompaniesVendors(bulkActionRequestBody, callback) {
      let postBody = bulkActionRequestBody;
      // verify the required parameter 'bulkActionRequestBody' is set
      if (bulkActionRequestBody === undefined || bulkActionRequestBody === null) {
        throw new Error("Missing the required parameter 'bulkActionRequestBody' when calling bulkCompaniesVendors");
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
        '/companies_vendors/bulkDelete', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesVendorsCompaniesVendorIdDelete operation.
     * @callback module:api/CompaniesVendorsApi~companiesVendorsCompaniesVendorIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdDelete200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a companies vendor
     * @param {String} companiesVendorId 
     * @param {module:api/CompaniesVendorsApi~companiesVendorsCompaniesVendorIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdDelete200Response}
     */
    companiesVendorsCompaniesVendorIdDelete(companiesVendorId, callback) {
      let postBody = null;
      // verify the required parameter 'companiesVendorId' is set
      if (companiesVendorId === undefined || companiesVendorId === null) {
        throw new Error("Missing the required parameter 'companiesVendorId' when calling companiesVendorsCompaniesVendorIdDelete");
      }

      let pathParams = {
        'companies_vendor_id': companiesVendorId
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
        '/companies_vendors/{companies_vendor_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the editCompaniesVendor operation.
     * @callback module:api/CompaniesVendorsApi~editCompaniesVendorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a companies vendor
     * @param {String} companiesVendorId 
     * @param {Object} opts Optional parameters
     * @param {module:model/AddCompaniesVendorRequest} [addCompaniesVendorRequest] 
     * @param {module:api/CompaniesVendorsApi~editCompaniesVendorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    editCompaniesVendor(companiesVendorId, opts, callback) {
      opts = opts || {};
      let postBody = opts['addCompaniesVendorRequest'];
      // verify the required parameter 'companiesVendorId' is set
      if (companiesVendorId === undefined || companiesVendorId === null) {
        throw new Error("Missing the required parameter 'companiesVendorId' when calling editCompaniesVendor");
      }

      let pathParams = {
        'companies_vendor_id': companiesVendorId
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
        '/companies_vendors/{companies_vendor_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCompaiesVendorsList operation.
     * @callback module:api/CompaniesVendorsApi~getCompaiesVendorsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCompaiesVendorsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of companies vendors
     * @param {module:api/CompaniesVendorsApi~getCompaiesVendorsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCompaiesVendorsList200Response}
     */
    getCompaiesVendorsList(callback) {
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
      let returnType = GetCompaiesVendorsList200Response;
      return this.apiClient.callApi(
        '/companies_vendors', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCompaniesVendor operation.
     * @callback module:api/CompaniesVendorsApi~getCompaniesVendorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCompaniesVendor200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a companies vendor
     * @param {String} companiesVendorId 
     * @param {module:api/CompaniesVendorsApi~getCompaniesVendorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCompaniesVendor200Response}
     */
    getCompaniesVendor(companiesVendorId, callback) {
      let postBody = null;
      // verify the required parameter 'companiesVendorId' is set
      if (companiesVendorId === undefined || companiesVendorId === null) {
        throw new Error("Missing the required parameter 'companiesVendorId' when calling getCompaniesVendor");
      }

      let pathParams = {
        'companies_vendor_id': companiesVendorId
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
      let returnType = GetCompaniesVendor200Response;
      return this.apiClient.callApi(
        '/companies_vendors/{companies_vendor_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCompaniesVendorsExpenseStatistics operation.
     * @callback module:api/CompaniesVendorsApi~getCompaniesVendorsExpenseStatisticsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetCompaniesVendorsExpenseStatistics200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get companies vendor expense statistics
     * @param {String} companiesVendorId 
     * @param {module:api/CompaniesVendorsApi~getCompaniesVendorsExpenseStatisticsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetCompaniesVendorsExpenseStatistics200Response}
     */
    getCompaniesVendorsExpenseStatistics(companiesVendorId, callback) {
      let postBody = null;
      // verify the required parameter 'companiesVendorId' is set
      if (companiesVendorId === undefined || companiesVendorId === null) {
        throw new Error("Missing the required parameter 'companiesVendorId' when calling getCompaniesVendorsExpenseStatistics");
      }

      let pathParams = {
        'companies_vendor_id': companiesVendorId
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
      let returnType = GetCompaniesVendorsExpenseStatistics200Response;
      return this.apiClient.callApi(
        '/companies_vendors/{companies_vendor_id}/expense_statistics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
