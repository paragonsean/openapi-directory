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
import ClockingRecordsPost201Response from '../model/ClockingRecordsPost201Response';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorValidation from '../model/ErrorValidation';
import FormsFormIdGet200Response from '../model/FormsFormIdGet200Response';
import FormsGet200Response from '../model/FormsGet200Response';
import FormsPostRequest from '../model/FormsPostRequest';

/**
* Forms service.
* @module api/FormsApi
* @version 0.0.42
*/
export default class FormsApi {

    /**
    * Constructs a new FormsApi. 
    * @alias module:api/FormsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the formsFormIdDelete operation.
     * @callback module:api/FormsApi~formsFormIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a form
     * You can only delete the forms that you've submitted yourself
     * @param {String} formId 
     * @param {module:api/FormsApi~formsFormIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    formsFormIdDelete(formId, callback) {
      let postBody = null;
      // verify the required parameter 'formId' is set
      if (formId === undefined || formId === null) {
        throw new Error("Missing the required parameter 'formId' when calling formsFormIdDelete");
      }

      let pathParams = {
        'form_id': formId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/forms/{form_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the formsFormIdGet operation.
     * @callback module:api/FormsApi~formsFormIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/FormsFormIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View form
     * @param {String} formId 
     * @param {module:api/FormsApi~formsFormIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/FormsFormIdGet200Response}
     */
    formsFormIdGet(formId, callback) {
      let postBody = null;
      // verify the required parameter 'formId' is set
      if (formId === undefined || formId === null) {
        throw new Error("Missing the required parameter 'formId' when calling formsFormIdGet");
      }

      let pathParams = {
        'form_id': formId
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
      let returnType = FormsFormIdGet200Response;
      return this.apiClient.callApi(
        '/forms/{form_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the formsFormIdPut operation.
     * @callback module:api/FormsApi~formsFormIdPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a form
     * @param {String} formId 
     * @param {module:api/FormsApi~formsFormIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    formsFormIdPut(formId, callback) {
      let postBody = null;
      // verify the required parameter 'formId' is set
      if (formId === undefined || formId === null) {
        throw new Error("Missing the required parameter 'formId' when calling formsFormIdPut");
      }

      let pathParams = {
        'form_id': formId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/forms/{form_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the formsGet operation.
     * @callback module:api/FormsApi~formsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/FormsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve array of forms
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [extended] Used to have extended details from the forms from the `Form`'s `FormFields`
     * @param {String} [dateFrom] Used in conjunction with `date_to` to only show forms within these dates - format like `2016-28-05`
     * @param {String} [dateTo] Used in conjunction with `date_from` to only show forms within these dates - format like `2016-28-30`
     * @param {String} [show] Used to show forms with trashed
     * @param {String} [projectId] Used to filter on the `project_id` of the forms
     * @param {String} [createdById] Used to filter on the `created_by_id` of the forms
     * @param {Array.<String>} [formTemplateId] Used to filter on the `form_template_id` of the forms. Accept single value and array.
     * @param {String} [formTemplateType] Filter by `form_templates.identifier` containing string passed in `form_template_type`. Accept strings like [`qa`, `dagseddel`]
     * @param {String} [employeeName] Used to filter forms by user's first or last name
     * @param {module:api/FormsApi~formsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/FormsGet200Response}
     */
    formsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'extended': opts['extended'],
        'date_from': opts['dateFrom'],
        'date_to': opts['dateTo'],
        'show': opts['show'],
        'project_id': opts['projectId'],
        'created_by_id': opts['createdById'],
        'form_template_id': this.apiClient.buildCollectionParam(opts['formTemplateId'], 'csv'),
        'form_template_type': opts['formTemplateType'],
        'employee_name': opts['employeeName']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = FormsGet200Response;
      return this.apiClient.callApi(
        '/forms', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the formsPost operation.
     * @callback module:api/FormsApi~formsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClockingRecordsPost201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add new form
     * Used to add a form into the system
     * @param {Object} opts Optional parameters
     * @param {module:model/FormsPostRequest} [formsPostRequest] 
     * @param {module:api/FormsApi~formsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClockingRecordsPost201Response}
     */
    formsPost(opts, callback) {
      opts = opts || {};
      let postBody = opts['formsPostRequest'];

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
        '/forms', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the formsUndeleteFormIdGet operation.
     * @callback module:api/FormsApi~formsUndeleteFormIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Undelete form and related entities to it
     * @param {String} formId 
     * @param {module:api/FormsApi~formsUndeleteFormIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    formsUndeleteFormIdGet(formId, callback) {
      let postBody = null;
      // verify the required parameter 'formId' is set
      if (formId === undefined || formId === null) {
        throw new Error("Missing the required parameter 'formId' when calling formsUndeleteFormIdGet");
      }

      let pathParams = {
        'form_id': formId
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
        '/forms/undelete/{form_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the formsViewTimeFormPdfFormIdGet operation.
     * @callback module:api/FormsApi~formsViewTimeFormPdfFormIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate time form pdf
     * @param {String} formId 
     * @param {module:api/FormsApi~formsViewTimeFormPdfFormIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    formsViewTimeFormPdfFormIdGet(formId, callback) {
      let postBody = null;
      // verify the required parameter 'formId' is set
      if (formId === undefined || formId === null) {
        throw new Error("Missing the required parameter 'formId' when calling formsViewTimeFormPdfFormIdGet");
      }

      let pathParams = {
        'form_id': formId
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
        '/forms/view_time_form_pdf/{form_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
