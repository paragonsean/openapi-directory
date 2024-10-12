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
 * The Offer model module.
 * @module model/Offer
 * @version 0.0.42
 */
class Offer {
    /**
     * Constructs a new <code>Offer</code>.
     * @alias module:model/Offer
     */
    constructor() { 
        
        Offer.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Offer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Offer} obj Optional instance to populate.
     * @return {module:model/Offer} The populated <code>Offer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Offer();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('all_lines_one_line')) {
                obj['all_lines_one_line'] = ApiClient.convertToType(data['all_lines_one_line'], 'Boolean');
            }
            if (data.hasOwnProperty('all_products_one_line')) {
                obj['all_products_one_line'] = ApiClient.convertToType(data['all_products_one_line'], 'Boolean');
            }
            if (data.hasOwnProperty('all_working_hours_one_line')) {
                obj['all_working_hours_one_line'] = ApiClient.convertToType(data['all_working_hours_one_line'], 'Boolean');
            }
            if (data.hasOwnProperty('city_id')) {
                obj['city_id'] = ApiClient.convertToType(data['city_id'], 'String');
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
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('discount_percent')) {
                obj['discount_percent'] = ApiClient.convertToType(data['discount_percent'], 'Number');
            }
            if (data.hasOwnProperty('erp_payment_term_id')) {
                obj['erp_payment_term_id'] = ApiClient.convertToType(data['erp_payment_term_id'], 'String');
            }
            if (data.hasOwnProperty('expiraton_date')) {
                obj['expiraton_date'] = ApiClient.convertToType(data['expiraton_date'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('issue_date')) {
                obj['issue_date'] = ApiClient.convertToType(data['issue_date'], 'Date');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'String');
            }
            if (data.hasOwnProperty('modified_by_id')) {
                obj['modified_by_id'] = ApiClient.convertToType(data['modified_by_id'], 'String');
            }
            if (data.hasOwnProperty('offer_number')) {
                obj['offer_number'] = ApiClient.convertToType(data['offer_number'], 'Number');
            }
            if (data.hasOwnProperty('offer_status_id')) {
                obj['offer_status_id'] = ApiClient.convertToType(data['offer_status_id'], 'String');
            }
            if (data.hasOwnProperty('payment_term_id')) {
                obj['payment_term_id'] = ApiClient.convertToType(data['payment_term_id'], 'String');
            }
            if (data.hasOwnProperty('rejection_reason')) {
                obj['rejection_reason'] = ApiClient.convertToType(data['rejection_reason'], 'String');
            }
            if (data.hasOwnProperty('sender_id')) {
                obj['sender_id'] = ApiClient.convertToType(data['sender_id'], 'String');
            }
            if (data.hasOwnProperty('show_employee_name')) {
                obj['show_employee_name'] = ApiClient.convertToType(data['show_employee_name'], 'Boolean');
            }
            if (data.hasOwnProperty('show_offer_lines')) {
                obj['show_offer_lines'] = ApiClient.convertToType(data['show_offer_lines'], 'Boolean');
            }
            if (data.hasOwnProperty('show_payment_term')) {
                obj['show_payment_term'] = ApiClient.convertToType(data['show_payment_term'], 'Boolean');
            }
            if (data.hasOwnProperty('show_prices')) {
                obj['show_prices'] = ApiClient.convertToType(data['show_prices'], 'Boolean');
            }
            if (data.hasOwnProperty('show_product_images')) {
                obj['show_product_images'] = ApiClient.convertToType(data['show_product_images'], 'Boolean');
            }
            if (data.hasOwnProperty('show_products_product_bundle')) {
                obj['show_products_product_bundle'] = ApiClient.convertToType(data['show_products_product_bundle'], 'Boolean');
            }
            if (data.hasOwnProperty('slug')) {
                obj['slug'] = ApiClient.convertToType(data['slug'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('vat_percent')) {
                obj['vat_percent'] = ApiClient.convertToType(data['vat_percent'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Offer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Offer</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }
        // ensure the json data is a string
        if (data['city_id'] && !(typeof data['city_id'] === 'string' || data['city_id'] instanceof String)) {
            throw new Error("Expected the field `city_id` to be a primitive type in the JSON string but got " + data['city_id']);
        }
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
        if (data['deleted'] && !(typeof data['deleted'] === 'string' || data['deleted'] instanceof String)) {
            throw new Error("Expected the field `deleted` to be a primitive type in the JSON string but got " + data['deleted']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['erp_payment_term_id'] && !(typeof data['erp_payment_term_id'] === 'string' || data['erp_payment_term_id'] instanceof String)) {
            throw new Error("Expected the field `erp_payment_term_id` to be a primitive type in the JSON string but got " + data['erp_payment_term_id']);
        }
        // ensure the json data is a string
        if (data['expiraton_date'] && !(typeof data['expiraton_date'] === 'string' || data['expiraton_date'] instanceof String)) {
            throw new Error("Expected the field `expiraton_date` to be a primitive type in the JSON string but got " + data['expiraton_date']);
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
        if (data['offer_status_id'] && !(typeof data['offer_status_id'] === 'string' || data['offer_status_id'] instanceof String)) {
            throw new Error("Expected the field `offer_status_id` to be a primitive type in the JSON string but got " + data['offer_status_id']);
        }
        // ensure the json data is a string
        if (data['payment_term_id'] && !(typeof data['payment_term_id'] === 'string' || data['payment_term_id'] instanceof String)) {
            throw new Error("Expected the field `payment_term_id` to be a primitive type in the JSON string but got " + data['payment_term_id']);
        }
        // ensure the json data is a string
        if (data['rejection_reason'] && !(typeof data['rejection_reason'] === 'string' || data['rejection_reason'] instanceof String)) {
            throw new Error("Expected the field `rejection_reason` to be a primitive type in the JSON string but got " + data['rejection_reason']);
        }
        // ensure the json data is a string
        if (data['sender_id'] && !(typeof data['sender_id'] === 'string' || data['sender_id'] instanceof String)) {
            throw new Error("Expected the field `sender_id` to be a primitive type in the JSON string but got " + data['sender_id']);
        }
        // ensure the json data is a string
        if (data['slug'] && !(typeof data['slug'] === 'string' || data['slug'] instanceof String)) {
            throw new Error("Expected the field `slug` to be a primitive type in the JSON string but got " + data['slug']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}



/**
 * Street address
 * @member {String} address
 */
Offer.prototype['address'] = undefined;

/**
 * @member {Boolean} all_lines_one_line
 */
Offer.prototype['all_lines_one_line'] = undefined;

/**
 * @member {Boolean} all_products_one_line
 */
Offer.prototype['all_products_one_line'] = undefined;

/**
 * @member {Boolean} all_working_hours_one_line
 */
Offer.prototype['all_working_hours_one_line'] = undefined;

/**
 * @member {String} city_id
 */
Offer.prototype['city_id'] = undefined;

/**
 * @member {String} company_id
 */
Offer.prototype['company_id'] = undefined;

/**
 * @member {String} contact_id
 */
Offer.prototype['contact_id'] = undefined;

/**
 * @member {String} created
 */
Offer.prototype['created'] = undefined;

/**
 * @member {String} created_by_id
 */
Offer.prototype['created_by_id'] = undefined;

/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
Offer.prototype['deleted'] = undefined;

/**
 * @member {String} description
 */
Offer.prototype['description'] = undefined;

/**
 * @member {Number} discount_percent
 */
Offer.prototype['discount_percent'] = undefined;

/**
 * @member {String} erp_payment_term_id
 */
Offer.prototype['erp_payment_term_id'] = undefined;

/**
 * @member {String} expiraton_date
 */
Offer.prototype['expiraton_date'] = undefined;

/**
 * @member {String} id
 */
Offer.prototype['id'] = undefined;

/**
 * @member {Date} issue_date
 */
Offer.prototype['issue_date'] = undefined;

/**
 * @member {String} modified
 */
Offer.prototype['modified'] = undefined;

/**
 * @member {String} modified_by_id
 */
Offer.prototype['modified_by_id'] = undefined;

/**
 * @member {Number} offer_number
 */
Offer.prototype['offer_number'] = undefined;

/**
 * @member {String} offer_status_id
 */
Offer.prototype['offer_status_id'] = undefined;

/**
 * @member {String} payment_term_id
 */
Offer.prototype['payment_term_id'] = undefined;

/**
 * @member {String} rejection_reason
 */
Offer.prototype['rejection_reason'] = undefined;

/**
 * @member {String} sender_id
 */
Offer.prototype['sender_id'] = undefined;

/**
 * @member {Boolean} show_employee_name
 */
Offer.prototype['show_employee_name'] = undefined;

/**
 * @member {Boolean} show_offer_lines
 */
Offer.prototype['show_offer_lines'] = undefined;

/**
 * @member {Boolean} show_payment_term
 */
Offer.prototype['show_payment_term'] = undefined;

/**
 * @member {Boolean} show_prices
 */
Offer.prototype['show_prices'] = undefined;

/**
 * @member {Boolean} show_product_images
 */
Offer.prototype['show_product_images'] = undefined;

/**
 * @member {Boolean} show_products_product_bundle
 */
Offer.prototype['show_products_product_bundle'] = undefined;

/**
 * @member {String} slug
 */
Offer.prototype['slug'] = undefined;

/**
 * @member {String} status
 */
Offer.prototype['status'] = undefined;

/**
 * @member {String} title
 */
Offer.prototype['title'] = undefined;

/**
 * @member {Number} vat_percent
 */
Offer.prototype['vat_percent'] = undefined;






export default Offer;

