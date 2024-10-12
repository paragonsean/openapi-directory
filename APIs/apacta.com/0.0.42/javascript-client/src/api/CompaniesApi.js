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
import CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response from '../model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response';
import CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest from '../model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest';
import CompaniesCompanyIdFormTemplatesGet200Response from '../model/CompaniesCompanyIdFormTemplatesGet200Response';
import CompaniesCompanyIdGet200Response from '../model/CompaniesCompanyIdGet200Response';
import CompaniesCompanyIdIntegrationFeatureSettingsGet200Response from '../model/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response';
import CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response from '../model/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response';
import CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response from '../model/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response';
import CompaniesCompanyIdIntegrationSettingsGet200Response from '../model/CompaniesCompanyIdIntegrationSettingsGet200Response';
import CompaniesCompanyIdIntegrationSettingsPostRequest from '../model/CompaniesCompanyIdIntegrationSettingsPostRequest';
import CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response from '../model/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response';
import CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest from '../model/CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest';
import CompaniesGet200Response from '../model/CompaniesGet200Response';
import CompaniesSubscriptionSelfServiceGet200Response from '../model/CompaniesSubscriptionSelfServiceGet200Response';
import CreateSuccessResponse from '../model/CreateSuccessResponse';
import EmptySuccessResponse from '../model/EmptySuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import ErrorValidation from '../model/ErrorValidation';
import ForbiddenError from '../model/ForbiddenError';

/**
* Companies service.
* @module api/CompaniesApi
* @version 0.0.42
*/
export default class CompaniesApi {

    /**
    * Constructs a new CompaniesApi. 
    * @alias module:api/CompaniesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * View a company integration feature setting
     * @param {String} companyId 
     * @param {String} cIntegrationFeatureSettingId 
     * @param {module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response}
     */
    companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(companyId, cIntegrationFeatureSettingId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet");
      }
      // verify the required parameter 'cIntegrationFeatureSettingId' is set
      if (cIntegrationFeatureSettingId === undefined || cIntegrationFeatureSettingId === null) {
        throw new Error("Missing the required parameter 'cIntegrationFeatureSettingId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet");
      }

      let pathParams = {
        'company_id': companyId,
        'c_integration_feature_setting_id': cIntegrationFeatureSettingId
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
      let returnType = CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a company integration feature setting
     * @param {String} companyId 
     * @param {String} cIntegrationFeatureSettingId 
     * @param {module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response}
     */
    companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(companyId, cIntegrationFeatureSettingId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut");
      }
      // verify the required parameter 'cIntegrationFeatureSettingId' is set
      if (cIntegrationFeatureSettingId === undefined || cIntegrationFeatureSettingId === null) {
        throw new Error("Missing the required parameter 'cIntegrationFeatureSettingId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut");
      }

      let pathParams = {
        'company_id': companyId,
        'c_integration_feature_setting_id': cIntegrationFeatureSettingId
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
      let returnType = CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdCompaniesIntegrationFeatureSettingsGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List a company integration feature settings
     * @param {String} companyId 
     * @param {module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response}
     */
    companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(companyId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsGet");
      }

      let pathParams = {
        'company_id': companyId
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
      let returnType = CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/companies_integration_feature_settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdCompaniesIntegrationFeatureSettingsPost operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a company integration feature setting
     * @param {String} companyId 
     * @param {Object} opts Optional parameters
     * @param {module:model/CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest} [companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest] 
     * @param {module:api/CompaniesApi~companiesCompanyIdCompaniesIntegrationFeatureSettingsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(companyId, opts, callback) {
      opts = opts || {};
      let postBody = opts['companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest'];
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdCompaniesIntegrationFeatureSettingsPost");
      }

      let pathParams = {
        'company_id': companyId
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
        '/companies/{company_id}/companies_integration_feature_settings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdFormTemplatesFormTemplateIdDelete operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdFormTemplatesFormTemplateIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a form template company
     * @param {String} companyId 
     * @param {String} formTemplateId Automatically added
     * @param {module:api/CompaniesApi~companiesCompanyIdFormTemplatesFormTemplateIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    companiesCompanyIdFormTemplatesFormTemplateIdDelete(companyId, formTemplateId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdFormTemplatesFormTemplateIdDelete");
      }
      // verify the required parameter 'formTemplateId' is set
      if (formTemplateId === undefined || formTemplateId === null) {
        throw new Error("Missing the required parameter 'formTemplateId' when calling companiesCompanyIdFormTemplatesFormTemplateIdDelete");
      }

      let pathParams = {
        'company_id': companyId,
        'form_template_id': formTemplateId
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
        '/companies/{company_id}/form_templates/{form_template_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdFormTemplatesFormTemplateIdGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdFormTemplatesFormTemplateIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdFormTemplatesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a company form template
     * @param {String} companyId 
     * @param {String} id 
     * @param {String} formTemplateId Automatically added
     * @param {module:api/CompaniesApi~companiesCompanyIdFormTemplatesFormTemplateIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdFormTemplatesGet200Response}
     */
    companiesCompanyIdFormTemplatesFormTemplateIdGet(companyId, id, formTemplateId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdFormTemplatesFormTemplateIdGet");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling companiesCompanyIdFormTemplatesFormTemplateIdGet");
      }
      // verify the required parameter 'formTemplateId' is set
      if (formTemplateId === undefined || formTemplateId === null) {
        throw new Error("Missing the required parameter 'formTemplateId' when calling companiesCompanyIdFormTemplatesFormTemplateIdGet");
      }

      let pathParams = {
        'company_id': companyId,
        'form_template_id': formTemplateId
      };
      let queryParams = {
        'id': id
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CompaniesCompanyIdFormTemplatesGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/form_templates/{form_template_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdFormTemplatesGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdFormTemplatesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdFormTemplatesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of company form templates
     * @param {String} companyId 
     * @param {String} formTemplateId 
     * @param {module:api/CompaniesApi~companiesCompanyIdFormTemplatesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdFormTemplatesGet200Response}
     */
    companiesCompanyIdFormTemplatesGet(companyId, formTemplateId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdFormTemplatesGet");
      }
      // verify the required parameter 'formTemplateId' is set
      if (formTemplateId === undefined || formTemplateId === null) {
        throw new Error("Missing the required parameter 'formTemplateId' when calling companiesCompanyIdFormTemplatesGet");
      }

      let pathParams = {
        'company_id': companyId
      };
      let queryParams = {
        'form_template_id': formTemplateId
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CompaniesCompanyIdFormTemplatesGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/form_templates/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Details of 1 company
     * @param {String} companyId 
     * @param {module:api/CompaniesApi~companiesCompanyIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdGet200Response}
     */
    companiesCompanyIdGet(companyId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdGet");
      }

      let pathParams = {
        'company_id': companyId
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
      let returnType = CompaniesCompanyIdGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationFeatureSettingsGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationFeatureSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of integration feature settings
     * @param {String} companyId 
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationFeatureSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdIntegrationFeatureSettingsGet200Response}
     */
    companiesCompanyIdIntegrationFeatureSettingsGet(companyId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationFeatureSettingsGet");
      }

      let pathParams = {
        'company_id': companyId
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
      let returnType = CompaniesCompanyIdIntegrationFeatureSettingsGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/integration_feature_settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show details of 1 integration feature setting
     * @param {String} companyId 
     * @param {String} integrationFeatureSettingId 
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response}
     */
    companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(companyId, integrationFeatureSettingId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet");
      }
      // verify the required parameter 'integrationFeatureSettingId' is set
      if (integrationFeatureSettingId === undefined || integrationFeatureSettingId === null) {
        throw new Error("Missing the required parameter 'integrationFeatureSettingId' when calling companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet");
      }

      let pathParams = {
        'company_id': companyId,
        'integration_feature_setting_id': integrationFeatureSettingId
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
      let returnType = CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/integration_feature_settings/{integration_feature_setting_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a company integration setting
     * @param {String} companyId 
     * @param {String} companiesIntegrationSettingId 
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(companyId, companiesIntegrationSettingId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete");
      }
      // verify the required parameter 'companiesIntegrationSettingId' is set
      if (companiesIntegrationSettingId === undefined || companiesIntegrationSettingId === null) {
        throw new Error("Missing the required parameter 'companiesIntegrationSettingId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete");
      }

      let pathParams = {
        'company_id': companyId,
        'companies_integration_setting_id': companiesIntegrationSettingId
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
        '/companies/{company_id}/integration_settings/{companies_integration_setting_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a company integration setting
     * @param {String} companyId 
     * @param {String} companiesIntegrationSettingId 
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response}
     */
    companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(companyId, companiesIntegrationSettingId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet");
      }
      // verify the required parameter 'companiesIntegrationSettingId' is set
      if (companiesIntegrationSettingId === undefined || companiesIntegrationSettingId === null) {
        throw new Error("Missing the required parameter 'companiesIntegrationSettingId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet");
      }

      let pathParams = {
        'company_id': companyId,
        'companies_integration_setting_id': companiesIntegrationSettingId
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
      let returnType = CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/integration_settings/{companies_integration_setting_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit a company integration setting
     * @param {String} companyId 
     * @param {String} companiesIntegrationSettingId 
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(companyId, companiesIntegrationSettingId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut");
      }
      // verify the required parameter 'companiesIntegrationSettingId' is set
      if (companiesIntegrationSettingId === undefined || companiesIntegrationSettingId === null) {
        throw new Error("Missing the required parameter 'companiesIntegrationSettingId' when calling companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut");
      }

      let pathParams = {
        'company_id': companyId,
        'companies_integration_setting_id': companiesIntegrationSettingId
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
        '/companies/{company_id}/integration_settings/{companies_integration_setting_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationSettingsGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdIntegrationSettingsGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of company integration settings
     * @param {String} companyId 
     * @param {Object} opts Optional parameters
     * @param {String} [identifier] The identifier of an ERP integration
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdIntegrationSettingsGet200Response}
     */
    companiesCompanyIdIntegrationSettingsGet(companyId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsGet");
      }

      let pathParams = {
        'company_id': companyId
      };
      let queryParams = {
        'identifier': opts['identifier']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CompaniesCompanyIdIntegrationSettingsGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/integration_settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdIntegrationSettingsPost operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a company integration setting
     * @param {String} companyId 
     * @param {Object} opts Optional parameters
     * @param {module:model/CompaniesCompanyIdIntegrationSettingsPostRequest} [companiesCompanyIdIntegrationSettingsPostRequest] 
     * @param {module:api/CompaniesApi~companiesCompanyIdIntegrationSettingsPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    companiesCompanyIdIntegrationSettingsPost(companyId, opts, callback) {
      opts = opts || {};
      let postBody = opts['companiesCompanyIdIntegrationSettingsPostRequest'];
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdIntegrationSettingsPost");
      }

      let pathParams = {
        'company_id': companyId
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
        '/companies/{company_id}/integration_settings', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdPriceMarginsPriceMarginsIdDelete operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmptySuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a company price margin
     * @param {String} companyId 
     * @param {String} priceMarginId 
     * @param {String} priceMarginsId Automatically added
     * @param {module:api/CompaniesApi~companiesCompanyIdPriceMarginsPriceMarginsIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmptySuccessResponse}
     */
    companiesCompanyIdPriceMarginsPriceMarginsIdDelete(companyId, priceMarginId, priceMarginsId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdDelete");
      }
      // verify the required parameter 'priceMarginId' is set
      if (priceMarginId === undefined || priceMarginId === null) {
        throw new Error("Missing the required parameter 'priceMarginId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdDelete");
      }
      // verify the required parameter 'priceMarginsId' is set
      if (priceMarginsId === undefined || priceMarginsId === null) {
        throw new Error("Missing the required parameter 'priceMarginsId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdDelete");
      }

      let pathParams = {
        'company_id': companyId,
        'price_margins_id': priceMarginsId
      };
      let queryParams = {
        'price_margin_id': priceMarginId
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
        '/companies/{company_id}/price_margins/{price_margins_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdPriceMarginsPriceMarginsIdGet operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdPriceMarginsPriceMarginsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of company price margins
     * @param {String} companyId 
     * @param {String} priceMarginsId Automatically added
     * @param {module:api/CompaniesApi~companiesCompanyIdPriceMarginsPriceMarginsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response}
     */
    companiesCompanyIdPriceMarginsPriceMarginsIdGet(companyId, priceMarginsId, callback) {
      let postBody = null;
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdGet");
      }
      // verify the required parameter 'priceMarginsId' is set
      if (priceMarginsId === undefined || priceMarginsId === null) {
        throw new Error("Missing the required parameter 'priceMarginsId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdGet");
      }

      let pathParams = {
        'company_id': companyId,
        'price_margins_id': priceMarginsId
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
      let returnType = CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response;
      return this.apiClient.callApi(
        '/companies/{company_id}/price_margins/{price_margins_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesCompanyIdPriceMarginsPriceMarginsIdPost operation.
     * @callback module:api/CompaniesApi~companiesCompanyIdPriceMarginsPriceMarginsIdPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a company price margin
     * @param {String} companyId 
     * @param {String} priceMarginsId Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest} [companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest] 
     * @param {module:api/CompaniesApi~companiesCompanyIdPriceMarginsPriceMarginsIdPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    companiesCompanyIdPriceMarginsPriceMarginsIdPost(companyId, priceMarginsId, opts, callback) {
      opts = opts || {};
      let postBody = opts['companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest'];
      // verify the required parameter 'companyId' is set
      if (companyId === undefined || companyId === null) {
        throw new Error("Missing the required parameter 'companyId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdPost");
      }
      // verify the required parameter 'priceMarginsId' is set
      if (priceMarginsId === undefined || priceMarginsId === null) {
        throw new Error("Missing the required parameter 'priceMarginsId' when calling companiesCompanyIdPriceMarginsPriceMarginsIdPost");
      }

      let pathParams = {
        'company_id': companyId,
        'price_margins_id': priceMarginsId
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
        '/companies/{company_id}/price_margins/{price_margins_id}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesGet operation.
     * @callback module:api/CompaniesApi~companiesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of companies
     * @param {module:api/CompaniesApi~companiesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesGet200Response}
     */
    companiesGet(callback) {
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
      let returnType = CompaniesGet200Response;
      return this.apiClient.callApi(
        '/companies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the companiesSubscriptionSelfServiceGet operation.
     * @callback module:api/CompaniesApi~companiesSubscriptionSelfServiceGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CompaniesSubscriptionSelfServiceGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * URL for subscription selfservice
     * @param {module:api/CompaniesApi~companiesSubscriptionSelfServiceGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CompaniesSubscriptionSelfServiceGet200Response}
     */
    companiesSubscriptionSelfServiceGet(callback) {
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
      let returnType = CompaniesSubscriptionSelfServiceGet200Response;
      return this.apiClient.callApi(
        '/companies/subscription_self_service', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
