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
import ContactsPostRequestContactTypes from './ContactsPostRequestContactTypes';

/**
 * The UsersPostRequest model module.
 * @module model/UsersPostRequest
 * @version 0.0.42
 */
class UsersPostRequest {
    /**
     * Constructs a new <code>UsersPostRequest</code>.
     * @alias module:model/UsersPostRequest
     * @param firstName {String} 
     */
    constructor(firstName) { 
        
        UsersPostRequest.initialize(this, firstName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, firstName) { 
        obj['first_name'] = firstName;
    }

    /**
     * Constructs a <code>UsersPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UsersPostRequest} obj Optional instance to populate.
     * @return {module:model/UsersPostRequest} The populated <code>UsersPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UsersPostRequest();

            if (data.hasOwnProperty('city_id')) {
                obj['city_id'] = ApiClient.convertToType(data['city_id'], 'String');
            }
            if (data.hasOwnProperty('cost_price')) {
                obj['cost_price'] = ApiClient.convertToType(data['cost_price'], 'Number');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('expected_billable_hours')) {
                obj['expected_billable_hours'] = ApiClient.convertToType(data['expected_billable_hours'], 'Number');
            }
            if (data.hasOwnProperty('extra_price')) {
                obj['extra_price'] = ApiClient.convertToType(data['extra_price'], 'Number');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('hide_address')) {
                obj['hide_address'] = ApiClient.convertToType(data['hide_address'], 'Boolean');
            }
            if (data.hasOwnProperty('hide_phone')) {
                obj['hide_phone'] = ApiClient.convertToType(data['hide_phone'], 'Boolean');
            }
            if (data.hasOwnProperty('initials')) {
                obj['initials'] = ApiClient.convertToType(data['initials'], 'String');
            }
            if (data.hasOwnProperty('is_active')) {
                obj['is_active'] = ApiClient.convertToType(data['is_active'], 'Boolean');
            }
            if (data.hasOwnProperty('language_id')) {
                obj['language_id'] = ApiClient.convertToType(data['language_id'], 'String');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('mobile')) {
                obj['mobile'] = ApiClient.convertToType(data['mobile'], 'String');
            }
            if (data.hasOwnProperty('mobile_countrycode')) {
                obj['mobile_countrycode'] = ApiClient.convertToType(data['mobile_countrycode'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('phone')) {
                obj['phone'] = ApiClient.convertToType(data['phone'], 'String');
            }
            if (data.hasOwnProperty('phone_countrycode')) {
                obj['phone_countrycode'] = ApiClient.convertToType(data['phone_countrycode'], 'String');
            }
            if (data.hasOwnProperty('receive_form_mails')) {
                obj['receive_form_mails'] = ApiClient.convertToType(data['receive_form_mails'], 'Boolean');
            }
            if (data.hasOwnProperty('roles')) {
                obj['roles'] = ContactsPostRequestContactTypes.constructFromObject(data['roles']);
            }
            if (data.hasOwnProperty('sale_price')) {
                obj['sale_price'] = ApiClient.convertToType(data['sale_price'], 'Number');
            }
            if (data.hasOwnProperty('street_name')) {
                obj['street_name'] = ApiClient.convertToType(data['street_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UsersPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UsersPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UsersPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['city_id'] && !(typeof data['city_id'] === 'string' || data['city_id'] instanceof String)) {
            throw new Error("Expected the field `city_id` to be a primitive type in the JSON string but got " + data['city_id']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['initials'] && !(typeof data['initials'] === 'string' || data['initials'] instanceof String)) {
            throw new Error("Expected the field `initials` to be a primitive type in the JSON string but got " + data['initials']);
        }
        // ensure the json data is a string
        if (data['language_id'] && !(typeof data['language_id'] === 'string' || data['language_id'] instanceof String)) {
            throw new Error("Expected the field `language_id` to be a primitive type in the JSON string but got " + data['language_id']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['mobile'] && !(typeof data['mobile'] === 'string' || data['mobile'] instanceof String)) {
            throw new Error("Expected the field `mobile` to be a primitive type in the JSON string but got " + data['mobile']);
        }
        // ensure the json data is a string
        if (data['mobile_countrycode'] && !(typeof data['mobile_countrycode'] === 'string' || data['mobile_countrycode'] instanceof String)) {
            throw new Error("Expected the field `mobile_countrycode` to be a primitive type in the JSON string but got " + data['mobile_countrycode']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['phone'] && !(typeof data['phone'] === 'string' || data['phone'] instanceof String)) {
            throw new Error("Expected the field `phone` to be a primitive type in the JSON string but got " + data['phone']);
        }
        // ensure the json data is a string
        if (data['phone_countrycode'] && !(typeof data['phone_countrycode'] === 'string' || data['phone_countrycode'] instanceof String)) {
            throw new Error("Expected the field `phone_countrycode` to be a primitive type in the JSON string but got " + data['phone_countrycode']);
        }
        // validate the optional field `roles`
        if (data['roles']) { // data not null
          ContactsPostRequestContactTypes.validateJSON(data['roles']);
        }
        // ensure the json data is a string
        if (data['street_name'] && !(typeof data['street_name'] === 'string' || data['street_name'] instanceof String)) {
            throw new Error("Expected the field `street_name` to be a primitive type in the JSON string but got " + data['street_name']);
        }

        return true;
    }


}

UsersPostRequest.RequiredProperties = ["first_name"];

/**
 * @member {String} city_id
 */
UsersPostRequest.prototype['city_id'] = undefined;

/**
 * Cost of salaries
 * @member {Number} cost_price
 */
UsersPostRequest.prototype['cost_price'] = undefined;

/**
 * @member {String} email
 */
UsersPostRequest.prototype['email'] = undefined;

/**
 * @member {Number} expected_billable_hours
 */
UsersPostRequest.prototype['expected_billable_hours'] = undefined;

/**
 * Additional cost on this employee (pension, vacation etc.)
 * @member {Number} extra_price
 */
UsersPostRequest.prototype['extra_price'] = undefined;

/**
 * @member {String} first_name
 */
UsersPostRequest.prototype['first_name'] = undefined;

/**
 * @member {Boolean} hide_address
 */
UsersPostRequest.prototype['hide_address'] = undefined;

/**
 * @member {Boolean} hide_phone
 */
UsersPostRequest.prototype['hide_phone'] = undefined;

/**
 * @member {String} initials
 */
UsersPostRequest.prototype['initials'] = undefined;

/**
 * @member {Boolean} is_active
 */
UsersPostRequest.prototype['is_active'] = undefined;

/**
 * @member {String} language_id
 */
UsersPostRequest.prototype['language_id'] = undefined;

/**
 * @member {String} last_name
 */
UsersPostRequest.prototype['last_name'] = undefined;

/**
 * @member {String} mobile
 */
UsersPostRequest.prototype['mobile'] = undefined;

/**
 * @member {String} mobile_countrycode
 */
UsersPostRequest.prototype['mobile_countrycode'] = undefined;

/**
 * @member {String} password
 */
UsersPostRequest.prototype['password'] = undefined;

/**
 * @member {String} phone
 */
UsersPostRequest.prototype['phone'] = undefined;

/**
 * @member {String} phone_countrycode
 */
UsersPostRequest.prototype['phone_countrycode'] = undefined;

/**
 * If `true` the employee will receive an email receipt of every form submitted
 * @member {Boolean} receive_form_mails
 */
UsersPostRequest.prototype['receive_form_mails'] = undefined;

/**
 * @member {module:model/ContactsPostRequestContactTypes} roles
 */
UsersPostRequest.prototype['roles'] = undefined;

/**
 * The price this employee costs per hour when working
 * @member {Number} sale_price
 */
UsersPostRequest.prototype['sale_price'] = undefined;

/**
 * @member {String} street_name
 */
UsersPostRequest.prototype['street_name'] = undefined;






export default UsersPostRequest;

