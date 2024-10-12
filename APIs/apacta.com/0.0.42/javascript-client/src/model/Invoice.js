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
 * The Invoice model module.
 * @module model/Invoice
 * @version 0.0.42
 */
class Invoice {
    /**
     * Constructs a new <code>Invoice</code>.
     * @alias module:model/Invoice
     */
    constructor() { 
        
        Invoice.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Invoice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Invoice} obj Optional instance to populate.
     * @return {module:model/Invoice} The populated <code>Invoice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Invoice();

            if (data.hasOwnProperty('all_products_one_line')) {
                obj['all_products_one_line'] = ApiClient.convertToType(data['all_products_one_line'], 'Boolean');
            }
            if (data.hasOwnProperty('all_working_hours_one_line')) {
                obj['all_working_hours_one_line'] = ApiClient.convertToType(data['all_working_hours_one_line'], 'Boolean');
            }
            if (data.hasOwnProperty('company_id')) {
                obj['company_id'] = ApiClient.convertToType(data['company_id'], 'String');
            }
            if (data.hasOwnProperty('contact_id')) {
                obj['contact_id'] = ApiClient.convertToType(data['contact_id'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'String');
            }
            if (data.hasOwnProperty('created_by_id')) {
                obj['created_by_id'] = ApiClient.convertToType(data['created_by_id'], 'String');
            }
            if (data.hasOwnProperty('currency_id')) {
                obj['currency_id'] = ApiClient.convertToType(data['currency_id'], 'String');
            }
            if (data.hasOwnProperty('date_from')) {
                obj['date_from'] = ApiClient.convertToType(data['date_from'], 'Date');
            }
            if (data.hasOwnProperty('date_to')) {
                obj['date_to'] = ApiClient.convertToType(data['date_to'], 'Date');
            }
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'String');
            }
            if (data.hasOwnProperty('downloaded')) {
                obj['downloaded'] = ApiClient.convertToType(data['downloaded'], 'String');
            }
            if (data.hasOwnProperty('erp_id')) {
                obj['erp_id'] = ApiClient.convertToType(data['erp_id'], 'String');
            }
            if (data.hasOwnProperty('erp_payment_term_id')) {
                obj['erp_payment_term_id'] = ApiClient.convertToType(data['erp_payment_term_id'], 'String');
            }
            if (data.hasOwnProperty('eu_customer')) {
                obj['eu_customer'] = ApiClient.convertToType(data['eu_customer'], 'Boolean');
            }
            if (data.hasOwnProperty('gross_payment')) {
                obj['gross_payment'] = ApiClient.convertToType(data['gross_payment'], 'Number');
            }
            if (data.hasOwnProperty('group_by_forms')) {
                obj['group_by_forms'] = ApiClient.convertToType(data['group_by_forms'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('include_invoiced_lines')) {
                obj['include_invoiced_lines'] = ApiClient.convertToType(data['include_invoiced_lines'], 'Boolean');
            }
            if (data.hasOwnProperty('integration_id')) {
                obj['integration_id'] = ApiClient.convertToType(data['integration_id'], 'String');
            }
            if (data.hasOwnProperty('invoice_number')) {
                obj['invoice_number'] = ApiClient.convertToType(data['invoice_number'], 'Number');
            }
            if (data.hasOwnProperty('is_draft')) {
                obj['is_draft'] = ApiClient.convertToType(data['is_draft'], 'Boolean');
            }
            if (data.hasOwnProperty('is_final_invoice')) {
                obj['is_final_invoice'] = ApiClient.convertToType(data['is_final_invoice'], 'Boolean');
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
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'String');
            }
            if (data.hasOwnProperty('net_payment')) {
                obj['net_payment'] = ApiClient.convertToType(data['net_payment'], 'Number');
            }
            if (data.hasOwnProperty('offer_number')) {
                obj['offer_number'] = ApiClient.convertToType(data['offer_number'], 'Number');
            }
            if (data.hasOwnProperty('order_line_group_id')) {
                obj['order_line_group_id'] = ApiClient.convertToType(data['order_line_group_id'], 'String');
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
            if (data.hasOwnProperty('project_overview_attached')) {
                obj['project_overview_attached'] = ApiClient.convertToType(data['project_overview_attached'], 'Boolean');
            }
            if (data.hasOwnProperty('reference')) {
                obj['reference'] = ApiClient.convertToType(data['reference'], 'String');
            }
            if (data.hasOwnProperty('show_employee_name')) {
                obj['show_employee_name'] = ApiClient.convertToType(data['show_employee_name'], 'Boolean');
            }
            if (data.hasOwnProperty('show_price_product_bundle')) {
                obj['show_price_product_bundle'] = ApiClient.convertToType(data['show_price_product_bundle'], 'Boolean');
            }
            if (data.hasOwnProperty('show_prices_products_and_hours')) {
                obj['show_prices_products_and_hours'] = ApiClient.convertToType(data['show_prices_products_and_hours'], 'Boolean');
            }
            if (data.hasOwnProperty('show_product_images')) {
                obj['show_product_images'] = ApiClient.convertToType(data['show_product_images'], 'Boolean');
            }
            if (data.hasOwnProperty('show_products_product_bundle')) {
                obj['show_products_product_bundle'] = ApiClient.convertToType(data['show_products_product_bundle'], 'Boolean');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('total_cost_price')) {
                obj['total_cost_price'] = ApiClient.convertToType(data['total_cost_price'], 'Number');
            }
            if (data.hasOwnProperty('total_discount_percent')) {
                obj['total_discount_percent'] = ApiClient.convertToType(data['total_discount_percent'], 'Number');
            }
            if (data.hasOwnProperty('vat_percent')) {
                obj['vat_percent'] = ApiClient.convertToType(data['vat_percent'], 'Number');
            }
            if (data.hasOwnProperty('vendor_id')) {
                obj['vendor_id'] = ApiClient.convertToType(data['vendor_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Invoice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Invoice</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['company_id'] && !(typeof data['company_id'] === 'string' || data['company_id'] instanceof String)) {
            throw new Error("Expected the field `company_id` to be a primitive type in the JSON string but got " + data['company_id']);
        }
        // ensure the json data is a string
        if (data['contact_id'] && !(typeof data['contact_id'] === 'string' || data['contact_id'] instanceof String)) {
            throw new Error("Expected the field `contact_id` to be a primitive type in the JSON string but got " + data['contact_id']);
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
        if (data['currency_id'] && !(typeof data['currency_id'] === 'string' || data['currency_id'] instanceof String)) {
            throw new Error("Expected the field `currency_id` to be a primitive type in the JSON string but got " + data['currency_id']);
        }
        // ensure the json data is a string
        if (data['deleted'] && !(typeof data['deleted'] === 'string' || data['deleted'] instanceof String)) {
            throw new Error("Expected the field `deleted` to be a primitive type in the JSON string but got " + data['deleted']);
        }
        // ensure the json data is a string
        if (data['downloaded'] && !(typeof data['downloaded'] === 'string' || data['downloaded'] instanceof String)) {
            throw new Error("Expected the field `downloaded` to be a primitive type in the JSON string but got " + data['downloaded']);
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
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['integration_id'] && !(typeof data['integration_id'] === 'string' || data['integration_id'] instanceof String)) {
            throw new Error("Expected the field `integration_id` to be a primitive type in the JSON string but got " + data['integration_id']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['modified'] && !(typeof data['modified'] === 'string' || data['modified'] instanceof String)) {
            throw new Error("Expected the field `modified` to be a primitive type in the JSON string but got " + data['modified']);
        }
        // ensure the json data is a string
        if (data['order_line_group_id'] && !(typeof data['order_line_group_id'] === 'string' || data['order_line_group_id'] instanceof String)) {
            throw new Error("Expected the field `order_line_group_id` to be a primitive type in the JSON string but got " + data['order_line_group_id']);
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
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['vendor_id'] && !(typeof data['vendor_id'] === 'string' || data['vendor_id'] instanceof String)) {
            throw new Error("Expected the field `vendor_id` to be a primitive type in the JSON string but got " + data['vendor_id']);
        }

        return true;
    }


}



/**
 * @member {Boolean} all_products_one_line
 */
Invoice.prototype['all_products_one_line'] = undefined;

/**
 * @member {Boolean} all_working_hours_one_line
 */
Invoice.prototype['all_working_hours_one_line'] = undefined;

/**
 * @member {String} company_id
 */
Invoice.prototype['company_id'] = undefined;

/**
 * @member {String} contact_id
 */
Invoice.prototype['contact_id'] = undefined;

/**
 * @member {String} created
 */
Invoice.prototype['created'] = undefined;

/**
 * @member {String} created_by_id
 */
Invoice.prototype['created_by_id'] = undefined;

/**
 * @member {String} currency_id
 */
Invoice.prototype['currency_id'] = undefined;

/**
 * @member {Date} date_from
 */
Invoice.prototype['date_from'] = undefined;

/**
 * @member {Date} date_to
 */
Invoice.prototype['date_to'] = undefined;

/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
Invoice.prototype['deleted'] = undefined;

/**
 * @member {String} downloaded
 */
Invoice.prototype['downloaded'] = undefined;

/**
 * @member {String} erp_id
 */
Invoice.prototype['erp_id'] = undefined;

/**
 * @member {String} erp_payment_term_id
 */
Invoice.prototype['erp_payment_term_id'] = undefined;

/**
 * @member {Boolean} eu_customer
 */
Invoice.prototype['eu_customer'] = undefined;

/**
 * @member {Number} gross_payment
 */
Invoice.prototype['gross_payment'] = undefined;

/**
 * @member {Boolean} group_by_forms
 */
Invoice.prototype['group_by_forms'] = undefined;

/**
 * @member {String} id
 */
Invoice.prototype['id'] = undefined;

/**
 * @member {Boolean} include_invoiced_lines
 */
Invoice.prototype['include_invoiced_lines'] = undefined;

/**
 * @member {String} integration_id
 */
Invoice.prototype['integration_id'] = undefined;

/**
 * @member {Number} invoice_number
 */
Invoice.prototype['invoice_number'] = undefined;

/**
 * @member {Boolean} is_draft
 */
Invoice.prototype['is_draft'] = undefined;

/**
 * @member {Boolean} is_final_invoice
 */
Invoice.prototype['is_final_invoice'] = undefined;

/**
 * @member {Boolean} is_locked
 */
Invoice.prototype['is_locked'] = undefined;

/**
 * @member {Boolean} is_offer
 */
Invoice.prototype['is_offer'] = undefined;

/**
 * @member {Date} issued_date
 */
Invoice.prototype['issued_date'] = undefined;

/**
 * @member {String} message
 */
Invoice.prototype['message'] = undefined;

/**
 * @member {String} modified
 */
Invoice.prototype['modified'] = undefined;

/**
 * @member {Number} net_payment
 */
Invoice.prototype['net_payment'] = undefined;

/**
 * @member {Number} offer_number
 */
Invoice.prototype['offer_number'] = undefined;

/**
 * @member {String} order_line_group_id
 */
Invoice.prototype['order_line_group_id'] = undefined;

/**
 * @member {Date} payment_due_date
 */
Invoice.prototype['payment_due_date'] = undefined;

/**
 * @member {String} payment_term_id
 */
Invoice.prototype['payment_term_id'] = undefined;

/**
 * @member {String} project_id
 */
Invoice.prototype['project_id'] = undefined;

/**
 * @member {Boolean} project_overview_attached
 */
Invoice.prototype['project_overview_attached'] = undefined;

/**
 * @member {String} reference
 */
Invoice.prototype['reference'] = undefined;

/**
 * @member {Boolean} show_employee_name
 */
Invoice.prototype['show_employee_name'] = undefined;

/**
 * @member {Boolean} show_price_product_bundle
 */
Invoice.prototype['show_price_product_bundle'] = undefined;

/**
 * @member {Boolean} show_prices_products_and_hours
 */
Invoice.prototype['show_prices_products_and_hours'] = undefined;

/**
 * @member {Boolean} show_product_images
 */
Invoice.prototype['show_product_images'] = undefined;

/**
 * @member {Boolean} show_products_product_bundle
 */
Invoice.prototype['show_products_product_bundle'] = undefined;

/**
 * @member {String} title
 */
Invoice.prototype['title'] = undefined;

/**
 * @member {Number} total_cost_price
 */
Invoice.prototype['total_cost_price'] = undefined;

/**
 * @member {Number} total_discount_percent
 */
Invoice.prototype['total_discount_percent'] = undefined;

/**
 * @member {Number} vat_percent
 */
Invoice.prototype['vat_percent'] = undefined;

/**
 * @member {String} vendor_id
 */
Invoice.prototype['vendor_id'] = undefined;






export default Invoice;

