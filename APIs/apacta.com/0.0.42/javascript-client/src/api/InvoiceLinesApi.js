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
import ClockingRecordsClockingRecordIdPut200Response from '../model/ClockingRecordsClockingRecordIdPut200Response';
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import CreateSuccessResponse from '../model/CreateSuccessResponse';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import InvoiceLinesGet200Response from '../model/InvoiceLinesGet200Response';
import InvoiceLinesInvoiceLineIdGet200Response from '../model/InvoiceLinesInvoiceLineIdGet200Response';
import InvoiceLinesInvoiceLineIdPutRequest from '../model/InvoiceLinesInvoiceLineIdPutRequest';
import InvoiceLinesPostRequest from '../model/InvoiceLinesPostRequest';

/**
* InvoiceLines service.
* @module api/InvoiceLinesApi
* @version 0.0.42
*/
export default class InvoiceLinesApi {

    /**
    * Constructs a new InvoiceLinesApi. 
    * @alias module:api/InvoiceLinesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the invoiceLineTextsInvoiceLineTextIdPost operation.
     * @callback module:api/InvoiceLinesApi~invoiceLineTextsInvoiceLineTextIdPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit invoice line text
     * @param {String} invoiceLineTextId Automatically added
     * @param {String} html 
     * @param {Object} opts Optional parameters
     * @param {File} [image] 
     * @param {module:api/InvoiceLinesApi~invoiceLineTextsInvoiceLineTextIdPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    invoiceLineTextsInvoiceLineTextIdPost(invoiceLineTextId, html, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'invoiceLineTextId' is set
      if (invoiceLineTextId === undefined || invoiceLineTextId === null) {
        throw new Error("Missing the required parameter 'invoiceLineTextId' when calling invoiceLineTextsInvoiceLineTextIdPost");
      }
      // verify the required parameter 'html' is set
      if (html === undefined || html === null) {
        throw new Error("Missing the required parameter 'html' when calling invoiceLineTextsInvoiceLineTextIdPost");
      }

      let pathParams = {
        'invoice_line_text_id': invoiceLineTextId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'html': html,
        'image': opts['image']
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = EmptySuccessResponse;
      return this.apiClient.callApi(
        '/invoice_line_texts/{invoice_line_text_id}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoiceLineTextsPost operation.
     * @callback module:api/InvoiceLinesApi~invoiceLineTextsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add invoice line text
     * @param {String} html 
     * @param {String} invoiceId 
     * @param {Object} opts Optional parameters
     * @param {File} [image] 
     * @param {Number} [placement] 
     * @param {module:api/InvoiceLinesApi~invoiceLineTextsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    invoiceLineTextsPost(html, invoiceId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'html' is set
      if (html === undefined || html === null) {
        throw new Error("Missing the required parameter 'html' when calling invoiceLineTextsPost");
      }
      // verify the required parameter 'invoiceId' is set
      if (invoiceId === undefined || invoiceId === null) {
        throw new Error("Missing the required parameter 'invoiceId' when calling invoiceLineTextsPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'html': html,
        'image': opts['image'],
        'invoice_id': invoiceId,
        'placement': opts['placement']
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = CreateSuccessResponse;
      return this.apiClient.callApi(
        '/invoice_line_texts/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoiceLinesGet operation.
     * @callback module:api/InvoiceLinesApi~invoiceLinesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoiceLinesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View list of invoice lines
     * @param {Object} opts Optional parameters
     * @param {String} [invoiceId] 
     * @param {String} [productId] 
     * @param {String} [userId] 
     * @param {String} [name] 
     * @param {String} [discountText] 
     * @param {module:api/InvoiceLinesApi~invoiceLinesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoiceLinesGet200Response}
     */
    invoiceLinesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'invoice_id': opts['invoiceId'],
        'product_id': opts['productId'],
        'user_id': opts['userId'],
        'name': opts['name'],
        'discount_text': opts['discountText']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = InvoiceLinesGet200Response;
      return this.apiClient.callApi(
        '/invoice_lines', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoiceLinesInvoiceLineIdDelete operation.
     * @callback module:api/InvoiceLinesApi~invoiceLinesInvoiceLineIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete invoice line
     * @param {String} invoiceLineId 
     * @param {module:api/InvoiceLinesApi~invoiceLinesInvoiceLineIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    invoiceLinesInvoiceLineIdDelete(invoiceLineId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceLineId' is set
      if (invoiceLineId === undefined || invoiceLineId === null) {
        throw new Error("Missing the required parameter 'invoiceLineId' when calling invoiceLinesInvoiceLineIdDelete");
      }

      let pathParams = {
        'invoice_line_id': invoiceLineId
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
        '/invoice_lines/{invoice_line_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoiceLinesInvoiceLineIdGet operation.
     * @callback module:api/InvoiceLinesApi~invoiceLinesInvoiceLineIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InvoiceLinesInvoiceLineIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View invoice line
     * @param {String} invoiceLineId 
     * @param {module:api/InvoiceLinesApi~invoiceLinesInvoiceLineIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InvoiceLinesInvoiceLineIdGet200Response}
     */
    invoiceLinesInvoiceLineIdGet(invoiceLineId, callback) {
      let postBody = null;
      // verify the required parameter 'invoiceLineId' is set
      if (invoiceLineId === undefined || invoiceLineId === null) {
        throw new Error("Missing the required parameter 'invoiceLineId' when calling invoiceLinesInvoiceLineIdGet");
      }

      let pathParams = {
        'invoice_line_id': invoiceLineId
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
      let returnType = InvoiceLinesInvoiceLineIdGet200Response;
      return this.apiClient.callApi(
        '/invoice_lines/{invoice_line_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoiceLinesInvoiceLineIdPut operation.
     * @callback module:api/InvoiceLinesApi~invoiceLinesInvoiceLineIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsClockingRecordIdPut200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit invoice line
     * @param {String} invoiceLineId 
     * @param {Object} opts Optional parameters
     * @param {module:model/InvoiceLinesInvoiceLineIdPutRequest} [invoiceLinesInvoiceLineIdPutRequest] 
     * @param {module:api/InvoiceLinesApi~invoiceLinesInvoiceLineIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsClockingRecordIdPut200Response}
     */
    invoiceLinesInvoiceLineIdPut(invoiceLineId, opts, callback) {
      opts = opts || {};
      let postBody = opts['invoiceLinesInvoiceLineIdPutRequest'];
      // verify the required parameter 'invoiceLineId' is set
      if (invoiceLineId === undefined || invoiceLineId === null) {
        throw new Error("Missing the required parameter 'invoiceLineId' when calling invoiceLinesInvoiceLineIdPut");
      }

      let pathParams = {
        'invoice_line_id': invoiceLineId
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
        '/invoice_lines/{invoice_line_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the invoiceLinesPost operation.
     * @callback module:api/InvoiceLinesApi~invoiceLinesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add invoice line
     * @param {Object} opts Optional parameters
     * @param {module:model/InvoiceLinesPostRequest} [invoiceLinesPostRequest] 
     * @param {module:api/InvoiceLinesApi~invoiceLinesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    invoiceLinesPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['invoiceLinesPostRequest'];

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
        '/invoice_lines', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
