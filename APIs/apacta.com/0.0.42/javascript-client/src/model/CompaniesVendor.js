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
import Vendor from './Vendor';

/**
 * The CompaniesVendor model module.
 * @module model/CompaniesVendor
 * @version 0.0.42
 */
class CompaniesVendor {
    /**
     * Constructs a new <code>CompaniesVendor</code>.
     * @alias module:model/CompaniesVendor
     */
    constructor() { 
        
        CompaniesVendor.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CompaniesVendor</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CompaniesVendor} obj Optional instance to populate.
     * @return {module:model/CompaniesVendor} The populated <code>CompaniesVendor</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CompaniesVendor();

            if (data.hasOwnProperty('company_id')) {
                obj['company_id'] = ApiClient.convertToType(data['company_id'], 'String');
            }
            if (data.hasOwnProperty('company_password')) {
                obj['company_password'] = ApiClient.convertToType(data['company_password'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'String');
            }
            if (data.hasOwnProperty('created_by_id')) {
                obj['created_by_id'] = ApiClient.convertToType(data['created_by_id'], 'String');
            }
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'String');
            }
            if (data.hasOwnProperty('delivery_price')) {
                obj['delivery_price'] = ApiClient.convertToType(data['delivery_price'], 'Number');
            }
            if (data.hasOwnProperty('free_delivery_price')) {
                obj['free_delivery_price'] = ApiClient.convertToType(data['free_delivery_price'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('is_active')) {
                obj['is_active'] = ApiClient.convertToType(data['is_active'], 'Boolean');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'String');
            }
            if (data.hasOwnProperty('modified_by_id')) {
                obj['modified_by_id'] = ApiClient.convertToType(data['modified_by_id'], 'String');
            }
            if (data.hasOwnProperty('receive_automatic_price_files')) {
                obj['receive_automatic_price_files'] = ApiClient.convertToType(data['receive_automatic_price_files'], 'Boolean');
            }
            if (data.hasOwnProperty('receive_invoice_mails')) {
                obj['receive_invoice_mails'] = ApiClient.convertToType(data['receive_invoice_mails'], 'Boolean');
            }
            if (data.hasOwnProperty('reviewed')) {
                obj['reviewed'] = ApiClient.convertToType(data['reviewed'], 'Boolean');
            }
            if (data.hasOwnProperty('use_price_files')) {
                obj['use_price_files'] = ApiClient.convertToType(data['use_price_files'], 'Boolean');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
            if (data.hasOwnProperty('vendor')) {
                obj['vendor'] = Vendor.constructFromObject(data['vendor']);
            }
            if (data.hasOwnProperty('vendor_account_reference')) {
                obj['vendor_account_reference'] = ApiClient.convertToType(data['vendor_account_reference'], 'String');
            }
            if (data.hasOwnProperty('vendor_department_id')) {
                obj['vendor_department_id'] = ApiClient.convertToType(data['vendor_department_id'], 'String');
            }
            if (data.hasOwnProperty('vendor_email')) {
                obj['vendor_email'] = ApiClient.convertToType(data['vendor_email'], 'String');
            }
            if (data.hasOwnProperty('vendor_id')) {
                obj['vendor_id'] = ApiClient.convertToType(data['vendor_id'], 'String');
            }
            if (data.hasOwnProperty('vendor_name')) {
                obj['vendor_name'] = ApiClient.convertToType(data['vendor_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CompaniesVendor</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CompaniesVendor</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['company_id'] && !(typeof data['company_id'] === 'string' || data['company_id'] instanceof String)) {
            throw new Error("Expected the field `company_id` to be a primitive type in the JSON string but got " + data['company_id']);
        }
        // ensure the json data is a string
        if (data['company_password'] && !(typeof data['company_password'] === 'string' || data['company_password'] instanceof String)) {
            throw new Error("Expected the field `company_password` to be a primitive type in the JSON string but got " + data['company_password']);
        }
        // ensure the json data is a string
        if (data['created'] && !(typeof data['created'] === 'string' || data['created'] instanceof String)) {
            throw new Error("Expected the field `created` to be a primitive type in the JSON string but got " + data['created']);
        }
        // ensure the json data is a string
        if (data['created_by_id'] && !(typeof data['created_by_id'] === 'string' || data['created_by_id'] instanceof String)) {
            throw new Error("Expected the field `created_by_id` to be a primitive type in the JSON string but got " + data['created_by_id']);
        }
        // ensure the json data is a string
        if (data['deleted'] && !(typeof data['deleted'] === 'string' || data['deleted'] instanceof String)) {
            throw new Error("Expected the field `deleted` to be a primitive type in the JSON string but got " + data['deleted']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['modified'] && !(typeof data['modified'] === 'string' || data['modified'] instanceof String)) {
            throw new Error("Expected the field `modified` to be a primitive type in the JSON string but got " + data['modified']);
        }
        // ensure the json data is a string
        if (data['modified_by_id'] && !(typeof data['modified_by_id'] === 'string' || data['modified_by_id'] instanceof String)) {
            throw new Error("Expected the field `modified_by_id` to be a primitive type in the JSON string but got " + data['modified_by_id']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }
        // validate the optional field `vendor`
        if (data['vendor']) { // data not null
          Vendor.validateJSON(data['vendor']);
        }
        // ensure the json data is a string
        if (data['vendor_account_reference'] && !(typeof data['vendor_account_reference'] === 'string' || data['vendor_account_reference'] instanceof String)) {
            throw new Error("Expected the field `vendor_account_reference` to be a primitive type in the JSON string but got " + data['vendor_account_reference']);
        }
        // ensure the json data is a string
        if (data['vendor_department_id'] && !(typeof data['vendor_department_id'] === 'string' || data['vendor_department_id'] instanceof String)) {
            throw new Error("Expected the field `vendor_department_id` to be a primitive type in the JSON string but got " + data['vendor_department_id']);
        }
        // ensure the json data is a string
        if (data['vendor_email'] && !(typeof data['vendor_email'] === 'string' || data['vendor_email'] instanceof String)) {
            throw new Error("Expected the field `vendor_email` to be a primitive type in the JSON string but got " + data['vendor_email']);
        }
        // ensure the json data is a string
        if (data['vendor_id'] && !(typeof data['vendor_id'] === 'string' || data['vendor_id'] instanceof String)) {
            throw new Error("Expected the field `vendor_id` to be a primitive type in the JSON string but got " + data['vendor_id']);
        }
        // ensure the json data is a string
        if (data['vendor_name'] && !(typeof data['vendor_name'] === 'string' || data['vendor_name'] instanceof String)) {
            throw new Error("Expected the field `vendor_name` to be a primitive type in the JSON string but got " + data['vendor_name']);
        }

        return true;
    }


}



/**
 * @member {String} company_id
 */
CompaniesVendor.prototype['company_id'] = undefined;

/**
 * @member {String} company_password
 */
CompaniesVendor.prototype['company_password'] = undefined;

/**
 * @member {String} created
 */
CompaniesVendor.prototype['created'] = undefined;

/**
 * @member {String} created_by_id
 */
CompaniesVendor.prototype['created_by_id'] = undefined;

/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
CompaniesVendor.prototype['deleted'] = undefined;

/**
 * @member {Number} delivery_price
 */
CompaniesVendor.prototype['delivery_price'] = undefined;

/**
 * @member {Number} free_delivery_price
 */
CompaniesVendor.prototype['free_delivery_price'] = undefined;

/**
 * @member {String} id
 */
CompaniesVendor.prototype['id'] = undefined;

/**
 * @member {Boolean} is_active
 */
CompaniesVendor.prototype['is_active'] = undefined;

/**
 * @member {String} modified
 */
CompaniesVendor.prototype['modified'] = undefined;

/**
 * @member {String} modified_by_id
 */
CompaniesVendor.prototype['modified_by_id'] = undefined;

/**
 * @member {Boolean} receive_automatic_price_files
 */
CompaniesVendor.prototype['receive_automatic_price_files'] = undefined;

/**
 * @member {Boolean} receive_invoice_mails
 */
CompaniesVendor.prototype['receive_invoice_mails'] = undefined;

/**
 * @member {Boolean} reviewed
 */
CompaniesVendor.prototype['reviewed'] = undefined;

/**
 * @member {Boolean} use_price_files
 */
CompaniesVendor.prototype['use_price_files'] = undefined;

/**
 * @member {String} username
 */
CompaniesVendor.prototype['username'] = undefined;

/**
 * @member {module:model/Vendor} vendor
 */
CompaniesVendor.prototype['vendor'] = undefined;

/**
 * @member {String} vendor_account_reference
 */
CompaniesVendor.prototype['vendor_account_reference'] = undefined;

/**
 * @member {String} vendor_department_id
 */
CompaniesVendor.prototype['vendor_department_id'] = undefined;

/**
 * @member {String} vendor_email
 */
CompaniesVendor.prototype['vendor_email'] = undefined;

/**
 * @member {String} vendor_id
 */
CompaniesVendor.prototype['vendor_id'] = undefined;

/**
 * @member {String} vendor_name
 */
CompaniesVendor.prototype['vendor_name'] = undefined;






export default CompaniesVendor;

