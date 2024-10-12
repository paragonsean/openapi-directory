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
 * The Expense model module.
 * @module model/Expense
 * @version 0.0.42
 */
class Expense {
    /**
     * Constructs a new <code>Expense</code>.
     * @alias module:model/Expense
     */
    constructor() { 
        
        Expense.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Expense</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Expense} obj Optional instance to populate.
     * @return {module:model/Expense} The populated <code>Expense</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Expense();

            if (data.hasOwnProperty('activity_id')) {
                obj['activity_id'] = ApiClient.convertToType(data['activity_id'], 'String');
            }
            if (data.hasOwnProperty('comment')) {
                obj['comment'] = ApiClient.convertToType(data['comment'], 'String');
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
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'String');
            }
            if (data.hasOwnProperty('delivery_date')) {
                obj['delivery_date'] = ApiClient.convertToType(data['delivery_date'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('due_date')) {
                obj['due_date'] = ApiClient.convertToType(data['due_date'], 'Date');
            }
            if (data.hasOwnProperty('file_reference')) {
                obj['file_reference'] = ApiClient.convertToType(data['file_reference'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('is_imported')) {
                obj['is_imported'] = ApiClient.convertToType(data['is_imported'], 'String');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'String');
            }
            if (data.hasOwnProperty('order_number')) {
                obj['order_number'] = ApiClient.convertToType(data['order_number'], 'String');
            }
            if (data.hasOwnProperty('project_id')) {
                obj['project_id'] = ApiClient.convertToType(data['project_id'], 'String');
            }
            if (data.hasOwnProperty('readsoft_id')) {
                obj['readsoft_id'] = ApiClient.convertToType(data['readsoft_id'], 'String');
            }
            if (data.hasOwnProperty('reference')) {
                obj['reference'] = ApiClient.convertToType(data['reference'], 'String');
            }
            if (data.hasOwnProperty('roger_id')) {
                obj['roger_id'] = ApiClient.convertToType(data['roger_id'], 'String');
            }
            if (data.hasOwnProperty('sent_to_email')) {
                obj['sent_to_email'] = ApiClient.convertToType(data['sent_to_email'], 'String');
            }
            if (data.hasOwnProperty('short_text')) {
                obj['short_text'] = ApiClient.convertToType(data['short_text'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('supplier_invoice_number')) {
                obj['supplier_invoice_number'] = ApiClient.convertToType(data['supplier_invoice_number'], 'String');
            }
            if (data.hasOwnProperty('total_buying_price')) {
                obj['total_buying_price'] = ApiClient.convertToType(data['total_buying_price'], 'Number');
            }
            if (data.hasOwnProperty('total_selling_price')) {
                obj['total_selling_price'] = ApiClient.convertToType(data['total_selling_price'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Expense</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Expense</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['activity_id'] && !(typeof data['activity_id'] === 'string' || data['activity_id'] instanceof String)) {
            throw new Error("Expected the field `activity_id` to be a primitive type in the JSON string but got " + data['activity_id']);
        }
        // ensure the json data is a string
        if (data['comment'] && !(typeof data['comment'] === 'string' || data['comment'] instanceof String)) {
            throw new Error("Expected the field `comment` to be a primitive type in the JSON string but got " + data['comment']);
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
        if (data['currency_id'] && !(typeof data['currency_id'] === 'string' || data['currency_id'] instanceof String)) {
            throw new Error("Expected the field `currency_id` to be a primitive type in the JSON string but got " + data['currency_id']);
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
        if (data['file_reference'] && !(typeof data['file_reference'] === 'string' || data['file_reference'] instanceof String)) {
            throw new Error("Expected the field `file_reference` to be a primitive type in the JSON string but got " + data['file_reference']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['is_imported'] && !(typeof data['is_imported'] === 'string' || data['is_imported'] instanceof String)) {
            throw new Error("Expected the field `is_imported` to be a primitive type in the JSON string but got " + data['is_imported']);
        }
        // ensure the json data is a string
        if (data['modified'] && !(typeof data['modified'] === 'string' || data['modified'] instanceof String)) {
            throw new Error("Expected the field `modified` to be a primitive type in the JSON string but got " + data['modified']);
        }
        // ensure the json data is a string
        if (data['order_number'] && !(typeof data['order_number'] === 'string' || data['order_number'] instanceof String)) {
            throw new Error("Expected the field `order_number` to be a primitive type in the JSON string but got " + data['order_number']);
        }
        // ensure the json data is a string
        if (data['project_id'] && !(typeof data['project_id'] === 'string' || data['project_id'] instanceof String)) {
            throw new Error("Expected the field `project_id` to be a primitive type in the JSON string but got " + data['project_id']);
        }
        // ensure the json data is a string
        if (data['readsoft_id'] && !(typeof data['readsoft_id'] === 'string' || data['readsoft_id'] instanceof String)) {
            throw new Error("Expected the field `readsoft_id` to be a primitive type in the JSON string but got " + data['readsoft_id']);
        }
        // ensure the json data is a string
        if (data['reference'] && !(typeof data['reference'] === 'string' || data['reference'] instanceof String)) {
            throw new Error("Expected the field `reference` to be a primitive type in the JSON string but got " + data['reference']);
        }
        // ensure the json data is a string
        if (data['roger_id'] && !(typeof data['roger_id'] === 'string' || data['roger_id'] instanceof String)) {
            throw new Error("Expected the field `roger_id` to be a primitive type in the JSON string but got " + data['roger_id']);
        }
        // ensure the json data is a string
        if (data['sent_to_email'] && !(typeof data['sent_to_email'] === 'string' || data['sent_to_email'] instanceof String)) {
            throw new Error("Expected the field `sent_to_email` to be a primitive type in the JSON string but got " + data['sent_to_email']);
        }
        // ensure the json data is a string
        if (data['short_text'] && !(typeof data['short_text'] === 'string' || data['short_text'] instanceof String)) {
            throw new Error("Expected the field `short_text` to be a primitive type in the JSON string but got " + data['short_text']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['supplier_invoice_number'] && !(typeof data['supplier_invoice_number'] === 'string' || data['supplier_invoice_number'] instanceof String)) {
            throw new Error("Expected the field `supplier_invoice_number` to be a primitive type in the JSON string but got " + data['supplier_invoice_number']);
        }

        return true;
    }


}



/**
 * @member {String} activity_id
 */
Expense.prototype['activity_id'] = undefined;

/**
 * @member {String} comment
 */
Expense.prototype['comment'] = undefined;

/**
 * Read-only
 * @member {String} company_id
 */
Expense.prototype['company_id'] = undefined;

/**
 * @member {String} contact_id
 */
Expense.prototype['contact_id'] = undefined;

/**
 * @member {String} created
 */
Expense.prototype['created'] = undefined;

/**
 * Read-only
 * @member {String} created_by_id
 */
Expense.prototype['created_by_id'] = undefined;

/**
 * @member {String} currency_id
 */
Expense.prototype['currency_id'] = undefined;

/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
Expense.prototype['deleted'] = undefined;

/**
 * @member {Date} delivery_date
 */
Expense.prototype['delivery_date'] = undefined;

/**
 * @member {String} description
 */
Expense.prototype['description'] = undefined;

/**
 * @member {Date} due_date
 */
Expense.prototype['due_date'] = undefined;

/**
 * @member {String} file_reference
 */
Expense.prototype['file_reference'] = undefined;

/**
 * Read-only
 * @member {String} id
 */
Expense.prototype['id'] = undefined;

/**
 * @member {String} is_imported
 */
Expense.prototype['is_imported'] = undefined;

/**
 * @member {String} modified
 */
Expense.prototype['modified'] = undefined;

/**
 * @member {String} order_number
 */
Expense.prototype['order_number'] = undefined;

/**
 * @member {String} project_id
 */
Expense.prototype['project_id'] = undefined;

/**
 * @member {String} readsoft_id
 */
Expense.prototype['readsoft_id'] = undefined;

/**
 * @member {String} reference
 */
Expense.prototype['reference'] = undefined;

/**
 * @member {String} roger_id
 */
Expense.prototype['roger_id'] = undefined;

/**
 * @member {String} sent_to_email
 */
Expense.prototype['sent_to_email'] = undefined;

/**
 * @member {String} short_text
 */
Expense.prototype['short_text'] = undefined;

/**
 * @member {String} status
 */
Expense.prototype['status'] = undefined;

/**
 * @member {String} supplier_invoice_number
 */
Expense.prototype['supplier_invoice_number'] = undefined;

/**
 * Sum of all `buying_price` from expense lines
 * @member {Number} total_buying_price
 */
Expense.prototype['total_buying_price'] = undefined;

/**
 * Sum of all `selling_price` from expense lines
 * @member {Number} total_selling_price
 */
Expense.prototype['total_selling_price'] = undefined;






export default Expense;

