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
import CreateSuccessResponse from '../model/CreateSuccessResponse';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import IntegrationsProductsSyncGet200Response from '../model/IntegrationsProductsSyncGet200Response';
import InvoicesGet200Response from '../model/InvoicesGet200Response';
import InvoicesInvoiceIdGet200Response from '../model/InvoicesInvoiceIdGet200Response';
import InvoicesInvoiceIdPutRequest from '../model/InvoicesInvoiceIdPutRequest';
import InvoicesPostRequest from '../model/InvoicesPostRequest';

/**
* Invoices service.
* @module api/InvoicesApi
* @version 0.0.42
*/
export default class InvoicesApi {

    /**
    * Constructs a new InvoicesApi. 
    * @alias module:api/InvoicesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the bulkDeleteInvoices operation.
     * @callback module:api/InvoicesApi~bulkDeleteInvoicesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Bulk delete invoices
     * @param {module:model/BulkActionRequestBody} bulkActionRequestBody Invoices ids
     * @param {module:api/InvoicesApi~bulkDeleteInvoicesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    bulkDeleteInvoices(bulkActionRequestBody, callback) {
      let postBody = bulkActionRequestBody;
      // verify the required parameter 'bulkActionRequestBody' is set
      if (bulkActionRequestBody === undefined || bulkActionRequestBody === null) {
        throw new Error("Missing the required parameter 'bulkActionRequestBody' when calling bulkDeleteInvoices");
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
        '/invoices/bulkDelete', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesGet operation.
     * @callback module:api/InvoicesApi~invoicesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoicesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View list of invoices
     * @param {Object} opts Optional parameters
     * @param {String} [contactId] Used to filter on the `contact_id` of the invoices
     * @param {String} [projectId] Used to filter on the `project_id` of the invoices
     * @param {String} [invoiceNumber] Used to filter on the `invoice_number` of the invoices
     * @param {String} [offerNumber] 
     * @param {module:model/Number} [isDraft] 
     * @param {module:model/Number} [isOffer] 
     * @param {module:model/Number} [isLocked] 
     * @param {module:model/Number} [isFixedPrice] 
     * @param {Date} [dateFrom] 
     * @param {Date} [dateTo] 
     * @param {Date} [issuedDate] 
     * @param {Number} [sentAsDraft] Used to filter invoices which are sent as draft to integration
     * @param {module:api/InvoicesApi~invoicesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoicesGet200Response}
     */
    invoicesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'contact_id': opts['contactId'],
        'project_id': opts['projectId'],
        'invoice_number': opts['invoiceNumber'],
        'offer_number': opts['offerNumber'],
        'is_draft': opts['isDraft'],
        'is_offer': opts['isOffer'],
        'is_locked': opts['isLocked'],
        'is_fixed_price': opts['isFixedPrice'],
        'date_from': opts['dateFrom'],
        'date_to': opts['dateTo'],
        'issued_date': opts['issuedDate'],
        'sent_as_draft': opts['sentAsDraft']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = InvoicesGet200Response;
      return this.apiClient.callApi(
        '/invoices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesInvoiceIdCopyPost operation.
     * @callback module:api/InvoicesApi~invoicesInvoiceIdCopyPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a copy of an invoice
     * @param {String} invoiceId 
     * @param {Object} opts Optional parameters
     * @param {String} [projectId] 
     * @param {String} [contactId] 
     * @param {module:api/InvoicesApi~invoicesInvoiceIdCopyPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    invoicesInvoiceIdCopyPost(invoiceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoicesInvoiceIdCopyPost");
      }

      let pathParams = {
        'invoice_id': invoiceId
      };
      let queryParams = {
        'project_id': opts['projectId'],
        'contact_id': opts['contactId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CreateSuccessResponse;
      return this.apiClient.callApi(
        '/invoices/{invoice_id}/copy', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesInvoiceIdDelete operation.
     * @callback module:api/InvoicesApi~invoicesInvoiceIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete invoice
     * @param {String} invoiceId 
     * @param {module:api/InvoicesApi~invoicesInvoiceIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    invoicesInvoiceIdDelete(invoiceId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoicesInvoiceIdDelete");
      }

      let pathParams = {
        'invoice_id': invoiceId
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
        '/invoices/{invoice_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesInvoiceIdGet operation.
     * @callback module:api/InvoicesApi~invoicesInvoiceIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoicesInvoiceIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View invoice
     * @param {String} invoiceId 
     * @param {module:api/InvoicesApi~invoicesInvoiceIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoicesInvoiceIdGet200Response}
     */
    invoicesInvoiceIdGet(invoiceId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoicesInvoiceIdGet");
      }

      let pathParams = {
        'invoice_id': invoiceId
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
      let returnType = InvoicesInvoiceIdGet200Response;
      return this.apiClient.callApi(
        '/invoices/{invoice_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesInvoiceIdLinkProjectPdfPost operation.
     * @callback module:api/InvoicesApi~invoicesInvoiceIdLinkProjectPdfPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates an invoice file containing the project's pdf overview
     * @param {String} invoiceId 
     * @param {module:api/InvoicesApi~invoicesInvoiceIdLinkProjectPdfPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    invoicesInvoiceIdLinkProjectPdfPost(invoiceId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoicesInvoiceIdLinkProjectPdfPost");
      }

      let pathParams = {
        'invoice_id': invoiceId
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
        '/invoices/{invoice_id}/linkProjectPdf', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesInvoiceIdPut operation.
     * @callback module:api/InvoicesApi~invoicesInvoiceIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit invoice
     * @param {String} invoiceId 
     * @param {Object} opts Optional parameters
     * @param {module:model/InvoicesInvoiceIdPutRequest} [invoicesInvoiceIdPutRequest] 
     * @param {module:api/InvoicesApi~invoicesInvoiceIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    invoicesInvoiceIdPut(invoiceId, opts, callback) {
      opts = opts || {};
      let postBody = opts['invoicesInvoiceIdPutRequest'];
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoicesInvoiceIdPut");
      }

      let pathParams = {
        'invoice_id': invoiceId
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
        '/invoices/{invoice_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesInvoiceIdUnlinkProjectPdfPost operation.
     * @callback module:api/InvoicesApi~invoicesInvoiceIdUnlinkProjectPdfPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the linked project overview pdf
     * @param {String} invoiceId 
     * @param {module:api/InvoicesApi~invoicesInvoiceIdUnlinkProjectPdfPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    invoicesInvoiceIdUnlinkProjectPdfPost(invoiceId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoicesInvoiceIdUnlinkProjectPdfPost");
      }

      let pathParams = {
        'invoice_id': invoiceId
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
        '/invoices/{invoice_id}/unlinkProjectPdf', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesPost operation.
     * @callback module:api/InvoicesApi~invoicesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add invoice
     * @param {Object} opts Optional parameters
     * @param {module:model/InvoicesPostRequest} [invoicesPostRequest] 
     * @param {module:api/InvoicesApi~invoicesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    invoicesPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['invoicesPostRequest'];

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
        '/invoices', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoicesVatOptionsGet operation.
     * @callback module:api/InvoicesApi~invoicesVatOptionsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IntegrationsProductsSyncGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List VAT options
     * @param {module:api/InvoicesApi~invoicesVatOptionsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IntegrationsProductsSyncGet200Response}
     */
    invoicesVatOptionsGet(callback) {
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
      let returnType = IntegrationsProductsSyncGet200Response;
      return this.apiClient.callApi(
        '/invoices/vatOptions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
