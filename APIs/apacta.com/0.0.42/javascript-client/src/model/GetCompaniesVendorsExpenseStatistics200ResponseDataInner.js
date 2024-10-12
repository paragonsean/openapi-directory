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

import ApiClient from '../ApiClient';
import GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner from './GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner';

/**
 * The GetCompaniesVendorsExpenseStatistics200ResponseDataInner model module.
 * @module model/GetCompaniesVendorsExpenseStatistics200ResponseDataInner
 * @version 0.0.42
 */
class GetCompaniesVendorsExpenseStatistics200ResponseDataInner {
    /**
     * Constructs a new <code>GetCompaniesVendorsExpenseStatistics200ResponseDataInner</code>.
     * @alias module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInner
     */
    constructor() { 
        
        GetCompaniesVendorsExpenseStatistics200ResponseDataInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetCompaniesVendorsExpenseStatistics200ResponseDataInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInner} obj Optional instance to populate.
     * @return {module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInner} The populated <code>GetCompaniesVendorsExpenseStatistics200ResponseDataInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetCompaniesVendorsExpenseStatistics200ResponseDataInner();

            if (data.hasOwnProperty('last_month')) {
                obj['last_month'] = ApiClient.convertToType(data['last_month'], [GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner]);
            }
            if (data.hasOwnProperty('thirty_days')) {
                obj['thirty_days'] = ApiClient.convertToType(data['thirty_days'], [GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner]);
            }
            if (data.hasOwnProperty('vendor_id')) {
                obj['vendor_id'] = ApiClient.convertToType(data['vendor_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetCompaniesVendorsExpenseStatistics200ResponseDataInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetCompaniesVendorsExpenseStatistics200ResponseDataInner</code>.
     */
    static validateJSON(data) {
        if (data['last_month']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['last_month'])) {
                throw new Error("Expected the field `last_month` to be an array in the JSON data but got " + data['last_month']);
            }
            // validate the optional field `last_month` (array)
            for (const item of data['last_month']) {
                GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner.validateJSON(item);
            };
        }
        if (data['thirty_days']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['thirty_days'])) {
                throw new Error("Expected the field `thirty_days` to be an array in the JSON data but got " + data['thirty_days']);
            }
            // validate the optional field `thirty_days` (array)
            for (const item of data['thirty_days']) {
                GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['vendor_id'] && !(typeof data['vendor_id'] === 'string' || data['vendor_id'] instanceof String)) {
            throw new Error("Expected the field `vendor_id` to be a primitive type in the JSON string but got " + data['vendor_id']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner>} last_month
 */
GetCompaniesVendorsExpenseStatistics200ResponseDataInner.prototype['last_month'] = undefined;

/**
 * @member {Array.<module:model/GetCompaniesVendorsExpenseStatistics200ResponseDataInnerLastMonthInner>} thirty_days
 */
GetCompaniesVendorsExpenseStatistics200ResponseDataInner.prototype['thirty_days'] = undefined;

/**
 * @member {String} vendor_id
 */
GetCompaniesVendorsExpenseStatistics200ResponseDataInner.prototype['vendor_id'] = undefined;






export default GetCompaniesVendorsExpenseStatistics200ResponseDataInner;

