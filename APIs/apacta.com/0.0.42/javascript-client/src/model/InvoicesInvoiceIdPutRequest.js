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

/**
 * The InvoicesInvoiceIdPutRequest model module.
 * @module model/InvoicesInvoiceIdPutRequest
 * @version 0.0.42
 */
class InvoicesInvoiceIdPutRequest {
    /**
     * Constructs a new <code>InvoicesInvoiceIdPutRequest</code>.
     * @alias module:model/InvoicesInvoiceIdPutRequest
     */
    constructor() { 
        
        InvoicesInvoiceIdPutRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>InvoicesInvoiceIdPutRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InvoicesInvoiceIdPutRequest} obj Optional instance to populate.
     * @return {module:model/InvoicesInvoiceIdPutRequest} The populated <code>InvoicesInvoiceIdPutRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InvoicesInvoiceIdPutRequest();

            if (data.hasOwnProperty('contact_id')) {
                obj['contact_id'] = ApiClient.convertToType(data['contact_id'], 'String');
            }
            if (data.hasOwnProperty('date_from')) {
                obj['date_from'] = ApiClient.convertToType(data['date_from'], 'Date');
            }
            if (data.hasOwnProperty('date_to')) {
                obj['date_to'] = ApiClient.convertToType(data['date_to'], 'Date');
            }
            if (data.hasOwnProperty('erp_id')) {
                obj['erp_id'] = ApiClient.convertToType(data['erp_id'], 'String');
            }
            if (data.hasOwnProperty('erp_payment_term_id')) {
                obj['erp_payment_term_id'] = ApiClient.convertToType(data['erp_payment_term_id'], 'String');
            }
            if (data.hasOwnProperty('invoice_number')) {
                obj['invoice_number'] = ApiClient.convertToType(data['invoice_number'], 'Number');
            }
            if (data.hasOwnProperty('is_draft')) {
                obj['is_draft'] = ApiClient.convertToType(data['is_draft'], 'Boolean');
            }
            if (data.hasOwnProperty('is_locked')) {
                obj['is_locked'] = ApiClient.convertToType(data['is_locked'], 'Boolean');
            }
            if (data.hasOwnProperty('is_offer')) {
                obj['is_offer'] = ApiClient.convertToType(data['is_offer'], 'Boolean');
            }
            if (data.hasOwnProperty('issued_date')) {
                obj['issued_date'] = ApiClient.convertToType(data['issued_date'], 'Date');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('offer_number')) {
                obj['offer_number'] = ApiClient.convertToType(data['offer_number'], 'Number');
            }
            if (data.hasOwnProperty('payment_due_date')) {
                obj['payment_due_date'] = ApiClient.convertToType(data['payment_due_date'], 'Date');
            }
            if (data.hasOwnProperty('payment_term_id')) {
                obj['payment_term_id'] = ApiClient.convertToType(data['payment_term_id'], 'String');
            }
            if (data.hasOwnProperty('project_id')) {
                obj['project_id'] = ApiClient.convertToType(data['project_id'], 'String');
            }
            if (data.hasOwnProperty('reference')) {
                obj['reference'] = ApiClient.convertToType(data['reference'], 'String');
            }
            if (data.hasOwnProperty('vat_percent')) {
                obj['vat_percent'] = ApiClient.convertToType(data['vat_percent'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InvoicesInvoiceIdPutRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InvoicesInvoiceIdPutRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['contact_id'] && !(typeof data['contact_id'] === 'string' || data['contact_id'] instanceof String)) {
            throw new Error("Expected the field `contact_id` to be a primitive type in the JSON string but got " + data['contact_id']);
        }
        // ensure the json data is a string
        if (data['erp_id'] && !(typeof data['erp_id'] === 'string' || data['erp_id'] instanceof String)) {
            throw new Error("Expected the field `erp_id` to be a primitive type in the JSON string but got " + data['erp_id']);
        }
        // ensure the json data is a string
        if (data['erp_payment_term_id'] && !(typeof data['erp_payment_term_id'] === 'string' || data['erp_payment_term_id'] instanceof String)) {
            throw new Error("Expected the field `erp_payment_term_id` to be a primitive type in the JSON string but got " + data['erp_payment_term_id']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['payment_term_id'] && !(typeof data['payment_term_id'] === 'string' || data['payment_term_id'] instanceof String)) {
            throw new Error("Expected the field `payment_term_id` to be a primitive type in the JSON string but got " + data['payment_term_id']);
        }
        // ensure the json data is a string
        if (data['project_id'] && !(typeof data['project_id'] === 'string' || data['project_id'] instanceof String)) {
            throw new Error("Expected the field `project_id` to be a primitive type in the JSON string but got " + data['project_id']);
        }
        // ensure the json data is a string
        if (data['reference'] && !(typeof data['reference'] === 'string' || data['reference'] instanceof String)) {
            throw new Error("Expected the field `reference` to be a primitive type in the JSON string but got " + data['reference']);
        }

        return true;
    }


}



/**
 * @member {String} contact_id
 */
InvoicesInvoiceIdPutRequest.prototype['contact_id'] = undefined;

/**
 * @member {Date} date_from
 */
InvoicesInvoiceIdPutRequest.prototype['date_from'] = undefined;

/**
 * @member {Date} date_to
 */
InvoicesInvoiceIdPutRequest.prototype['date_to'] = undefined;

/**
 * @member {String} erp_id
 */
InvoicesInvoiceIdPutRequest.prototype['erp_id'] = undefined;

/**
 * @member {String} erp_payment_term_id
 */
InvoicesInvoiceIdPutRequest.prototype['erp_payment_term_id'] = undefined;

/**
 * @member {Number} invoice_number
 */
InvoicesInvoiceIdPutRequest.prototype['invoice_number'] = undefined;

/**
 * @member {Boolean} is_draft
 */
InvoicesInvoiceIdPutRequest.prototype['is_draft'] = undefined;

/**
 * @member {Boolean} is_locked
 */
InvoicesInvoiceIdPutRequest.prototype['is_locked'] = undefined;

/**
 * @member {Boolean} is_offer
 */
InvoicesInvoiceIdPutRequest.prototype['is_offer'] = undefined;

/**
 * @member {Date} issued_date
 */
InvoicesInvoiceIdPutRequest.prototype['issued_date'] = undefined;

/**
 * @member {String} message
 */
InvoicesInvoiceIdPutRequest.prototype['message'] = undefined;

/**
 * @member {Number} offer_number
 */
InvoicesInvoiceIdPutRequest.prototype['offer_number'] = undefined;

/**
 * @member {Date} payment_due_date
 */
InvoicesInvoiceIdPutRequest.prototype['payment_due_date'] = undefined;

/**
 * @member {String} payment_term_id
 */
InvoicesInvoiceIdPutRequest.prototype['payment_term_id'] = undefined;

/**
 * @member {String} project_id
 */
InvoicesInvoiceIdPutRequest.prototype['project_id'] = undefined;

/**
 * @member {String} reference
 */
InvoicesInvoiceIdPutRequest.prototype['reference'] = undefined;

/**
 * @member {Number} vat_percent
 */
InvoicesInvoiceIdPutRequest.prototype['vat_percent'] = undefined;






export default InvoicesInvoiceIdPutRequest;

