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
import CreateSuccessResponse from '../model/CreateSuccessResponse';
import ErrorNotFound from '../model/ErrorNotFound';
import VendorProductPriceFilesGet200Response from '../model/VendorProductPriceFilesGet200Response';
import VendorProductPriceFilesVendorProductPriceFileIdGet200Response from '../model/VendorProductPriceFilesVendorProductPriceFileIdGet200Response';

/**
* VendorProductPriceFiles service.
* @module api/VendorProductPriceFilesApi
* @version 0.0.42
*/
export default class VendorProductPriceFilesApi {

    /**
    * Constructs a new VendorProductPriceFilesApi. 
    * @alias module:api/VendorProductPriceFilesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the vendorProductPriceFilesGet operation.
     * @callback module:api/VendorProductPriceFilesApi~vendorProductPriceFilesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VendorProductPriceFilesGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of price files
     * @param {Object} opts Optional parameters
     * @param {String} [fileName] 
     * @param {String} [vendorName] 
     * @param {Array.<String>} [vendorIds] 
     * @param {module:model/String} [status] 
     * @param {module:api/VendorProductPriceFilesApi~vendorProductPriceFilesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VendorProductPriceFilesGet200Response}
     */
    vendorProductPriceFilesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'file_name': opts['fileName'],
        'vendor_name': opts['vendorName'],
        'vendor_ids': this.apiClient.buildCollectionParam(opts['vendorIds'], 'csv'),
        'status': opts['status']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = VendorProductPriceFilesGet200Response;
      return this.apiClient.callApi(
        '/vendor_product_price_files', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the vendorProductPriceFilesPost operation.
     * @callback module:api/VendorProductPriceFilesApi~vendorProductPriceFilesPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateSuccessResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upload a vendor price file
     * @param {String} companiesVendorId 
     * @param {File} file 
     * @param {module:api/VendorProductPriceFilesApi~vendorProductPriceFilesPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateSuccessResponse}
     */
    vendorProductPriceFilesPost(companiesVendorId, file, callback) {
      let postBody = null;
      // verify the required parameter 'companiesVendorId' is set
      if (companiesVendorId === undefined || companiesVendorId === null) {
        throw new Error("Missing the required parameter 'companiesVendorId' when calling vendorProductPriceFilesPost");
      }
      // verify the required parameter 'file' is set
      if (file === undefined || file === null) {
        throw new Error("Missing the required parameter 'file' when calling vendorProductPriceFilesPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'companies_vendor_id': companiesVendorId,
        'file': file
      };

      let authNames = ['api_key', 'X-Auth-Token'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = CreateSuccessResponse;
      return this.apiClient.callApi(
        '/vendor_product_price_files', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the vendorProductPriceFilesVendorProductPriceFileIdGet operation.
     * @callback module:api/VendorProductPriceFilesApi~vendorProductPriceFilesVendorProductPriceFileIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a single price file
     * @param {String} vendorProductPriceFileId Automatically added
     * @param {module:api/VendorProductPriceFilesApi~vendorProductPriceFilesVendorProductPriceFileIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200Response}
     */
    vendorProductPriceFilesVendorProductPriceFileIdGet(vendorProductPriceFileId, callback) {
      let postBody = null;
      // verify the required parameter 'vendorProductPriceFileId' is set
      if (vendorProductPriceFileId === undefined || vendorProductPriceFileId === null) {
        throw new Error("Missing the required parameter 'vendorProductPriceFileId' when calling vendorProductPriceFilesVendorProductPriceFileIdGet");
      }

      let pathParams = {
        'vendor_product_price_file_id': vendorProductPriceFileId
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
      let returnType = VendorProductPriceFilesVendorProductPriceFileIdGet200Response;
      return this.apiClient.callApi(
        '/vendor_product_price_files/{vendor_product_price_file_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
