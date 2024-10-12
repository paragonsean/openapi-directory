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
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import ExpensesExpenseIdGet200Response from '../model/ExpensesExpenseIdGet200Response';
import ExpensesGet200Response from '../model/ExpensesGet200Response';
import ExpensesHighestAmountGet200Response from '../model/ExpensesHighestAmountGet200Response';
import ExpensesPostRequest from '../model/ExpensesPostRequest';

/**
* Expenses service.
* @module api/ExpensesApi
* @version 0.0.42
*/
export default class ExpensesApi {

    /**
    * Constructs a new ExpensesApi. 
    * @alias module:api/ExpensesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the bulkDeleteExpenses operation.
     * @callback module:api/ExpensesApi~bulkDeleteExpensesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Bulk delete expenses
     * @param {module:model/BulkActionRequestBody} bulkActionRequestBody expense ids
     * @param {module:api/ExpensesApi~bulkDeleteExpensesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    bulkDeleteExpenses(bulkActionRequestBody, callback) {
      let postBody = bulkActionRequestBody;
      // verify the required parameter 'bulkActionRequestBody' is set
      if (bulkActionRequestBody === undefined || bulkActionRequestBody === null) {
        throw new Error("Missing the required parameter 'bulkActionRequestBody' when calling bulkDeleteExpenses");
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
        '/expenses/bulkDelete', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expensesExpenseIdDelete operation.
     * @callback module:api/ExpensesApi~expensesExpenseIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpensesExpenseIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete expense
     * @param {String} expenseId 
     * @param {module:api/ExpensesApi~expensesExpenseIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpensesExpenseIdGet200Response}
     */
    expensesExpenseIdDelete(expenseId, callback) {
      let postBody = null;
      // verify the required parameter 'expenseId' is set
      if (expenseId === undefined || expenseId === null) {
        throw new Error("Missing the required parameter 'expenseId' when calling expensesExpenseIdDelete");
      }

      let pathParams = {
        'expense_id': expenseId
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
      let returnType = ExpensesExpenseIdGet200Response;
      return this.apiClient.callApi(
        '/expenses/{expense_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expensesExpenseIdGet operation.
     * @callback module:api/ExpensesApi~expensesExpenseIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpensesExpenseIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show expense
     * @param {String} expenseId 
     * @param {module:api/ExpensesApi~expensesExpenseIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpensesExpenseIdGet200Response}
     */
    expensesExpenseIdGet(expenseId, callback) {
      let postBody = null;
      // verify the required parameter 'expenseId' is set
      if (expenseId === undefined || expenseId === null) {
        throw new Error("Missing the required parameter 'expenseId' when calling expensesExpenseIdGet");
      }

      let pathParams = {
        'expense_id': expenseId
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
      let returnType = ExpensesExpenseIdGet200Response;
      return this.apiClient.callApi(
        '/expenses/{expense_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expensesExpenseIdPut operation.
     * @callback module:api/ExpensesApi~expensesExpenseIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpensesExpenseIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit expense
     * @param {String} expenseId 
     * @param {module:api/ExpensesApi~expensesExpenseIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpensesExpenseIdGet200Response}
     */
    expensesExpenseIdPut(expenseId, callback) {
      let postBody = null;
      // verify the required parameter 'expenseId' is set
      if (expenseId === undefined || expenseId === null) {
        throw new Error("Missing the required parameter 'expenseId' when calling expensesExpenseIdPut");
      }

      let pathParams = {
        'expense_id': expenseId
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
      let returnType = ExpensesExpenseIdGet200Response;
      return this.apiClient.callApi(
        '/expenses/{expense_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expensesGet operation.
     * @callback module:api/ExpensesApi~expensesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpensesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show list of expenses
     * @param {Object} opts Optional parameters
     * @param {String} [createdById] 
     * @param {String} [companyId] 
     * @param {String} [contactId] 
     * @param {String} [projectId] 
     * @param {module:model/String} [dueDate] Filter by [valid=records in future including today], [exceeded=records in past] or [null=all records]
     * @param {Date} [gtCreated] Created after date
     * @param {Date} [ltCreated] Created before date
     * @param {module:model/String} [status] Filter by status identifier. [null=all records]
     * @param {Boolean} [isImported = true)] 
     * @param {Number} [minAmount] Expenses `total_selling_price` > `min_amount`
     * @param {Number} [maxAmount] Expenses `total_selling_price` < `max_amount`
     * @param {module:model/String} [projects] You can select `all projects`, `no projects` or select `multiple projects`
     * @param {module:api/ExpensesApi~expensesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpensesGet200Response}
     */
    expensesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'created_by_id': opts['createdById'],
        'company_id': opts['companyId'],
        'contact_id': opts['contactId'],
        'project_id': opts['projectId'],
        'due_date': opts['dueDate'],
        'gt_created': opts['gtCreated'],
        'lt_created': opts['ltCreated'],
        'status': opts['status'],
        'is_imported': opts['isImported'],
        'min_amount': opts['minAmount'],
        'max_amount': opts['maxAmount'],
        'projects': opts['projects']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpensesGet200Response;
      return this.apiClient.callApi(
        '/expenses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expensesHighestAmountGet operation.
     * @callback module:api/ExpensesApi~expensesHighestAmountGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpensesHighestAmountGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show highest Expense amount(`total_selling_price`)
     * @param {Date} gtCreated Used to filter time range
     * @param {Date} ltCreated Used to filter time range
     * @param {module:api/ExpensesApi~expensesHighestAmountGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpensesHighestAmountGet200Response}
     */
    expensesHighestAmountGet(gtCreated, ltCreated, callback) {
      let postBody = null;
      // verify the required parameter 'gtCreated' is set
      if (gtCreated === undefined || gtCreated === null) {
        throw new Error("Missing the required parameter 'gtCreated' when calling expensesHighestAmountGet");
      }
      // verify the required parameter 'ltCreated' is set
      if (ltCreated === undefined || ltCreated === null) {
        throw new Error("Missing the required parameter 'ltCreated' when calling expensesHighestAmountGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'gt_created': gtCreated,
        'lt_created': ltCreated
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExpensesHighestAmountGet200Response;
      return this.apiClient.callApi(
        '/expenses/highest_amount', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expensesPost operation.
     * @callback module:api/ExpensesApi~expensesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add line to expense
     * @param {Object} opts Optional parameters
     * @param {module:model/ExpensesPostRequest} [expensesPostRequest] 
     * @param {module:api/ExpensesApi~expensesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    expensesPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['expensesPostRequest'];

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
        '/expenses', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sendEmailsExpenses operation.
     * @callback module:api/ExpensesApi~sendEmailsExpensesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Bulk delete expenses
     * @param {module:model/BulkActionRequestBody} bulkActionRequestBody expense ids
     * @param {module:api/ExpensesApi~sendEmailsExpensesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    sendEmailsExpenses(bulkActionRequestBody, callback) {
      let postBody = bulkActionRequestBody;
      // verify the required parameter 'bulkActionRequestBody' is set
      if (bulkActionRequestBody === undefined || bulkActionRequestBody === null) {
        throw new Error("Missing the required parameter 'bulkActionRequestBody' when calling sendEmailsExpenses");
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
        '/expenses/sendEmails', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
