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
 * The TimeEntriesPostRequest model module.
 * @module model/TimeEntriesPostRequest
 * @version 0.0.42
 */
class TimeEntriesPostRequest {
    /**
     * Constructs a new <code>TimeEntriesPostRequest</code>.
     * @alias module:model/TimeEntriesPostRequest
     * @param timeEntryTypeId {String} 
     * @param userId {String} 
     */
    constructor(timeEntryTypeId, userId) { 
        
        TimeEntriesPostRequest.initialize(this, timeEntryTypeId, userId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, timeEntryTypeId, userId) { 
        obj['time_entry_type_id'] = timeEntryTypeId;
        obj['user_id'] = userId;
    }

    /**
     * Constructs a <code>TimeEntriesPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimeEntriesPostRequest} obj Optional instance to populate.
     * @return {module:model/TimeEntriesPostRequest} The populated <code>TimeEntriesPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimeEntriesPostRequest();

            if (data.hasOwnProperty('form_id')) {
                obj['form_id'] = ApiClient.convertToType(data['form_id'], 'String');
            }
            if (data.hasOwnProperty('from_time')) {
                obj['from_time'] = ApiClient.convertToType(data['from_time'], 'String');
            }
            if (data.hasOwnProperty('is_all_day')) {
                obj['is_all_day'] = ApiClient.convertToType(data['is_all_day'], 'Boolean');
            }
            if (data.hasOwnProperty('project_id')) {
                obj['project_id'] = ApiClient.convertToType(data['project_id'], 'String');
            }
            if (data.hasOwnProperty('sum')) {
                obj['sum'] = ApiClient.convertToType(data['sum'], 'Number');
            }
            if (data.hasOwnProperty('time_entry_type_id')) {
                obj['time_entry_type_id'] = ApiClient.convertToType(data['time_entry_type_id'], 'String');
            }
            if (data.hasOwnProperty('to_time')) {
                obj['to_time'] = ApiClient.convertToType(data['to_time'], 'String');
            }
            if (data.hasOwnProperty('user_id')) {
                obj['user_id'] = ApiClient.convertToType(data['user_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimeEntriesPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimeEntriesPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TimeEntriesPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['form_id'] && !(typeof data['form_id'] === 'string' || data['form_id'] instanceof String)) {
            throw new Error("Expected the field `form_id` to be a primitive type in the JSON string but got " + data['form_id']);
        }
        // ensure the json data is a string
        if (data['from_time'] && !(typeof data['from_time'] === 'string' || data['from_time'] instanceof String)) {
            throw new Error("Expected the field `from_time` to be a primitive type in the JSON string but got " + data['from_time']);
        }
        // ensure the json data is a string
        if (data['project_id'] && !(typeof data['project_id'] === 'string' || data['project_id'] instanceof String)) {
            throw new Error("Expected the field `project_id` to be a primitive type in the JSON string but got " + data['project_id']);
        }
        // ensure the json data is a string
        if (data['time_entry_type_id'] && !(typeof data['time_entry_type_id'] === 'string' || data['time_entry_type_id'] instanceof String)) {
            throw new Error("Expected the field `time_entry_type_id` to be a primitive type in the JSON string but got " + data['time_entry_type_id']);
        }
        // ensure the json data is a string
        if (data['to_time'] && !(typeof data['to_time'] === 'string' || data['to_time'] instanceof String)) {
            throw new Error("Expected the field `to_time` to be a primitive type in the JSON string but got " + data['to_time']);
        }
        // ensure the json data is a string
        if (data['user_id'] && !(typeof data['user_id'] === 'string' || data['user_id'] instanceof String)) {
            throw new Error("Expected the field `user_id` to be a primitive type in the JSON string but got " + data['user_id']);
        }

        return true;
    }


}

TimeEntriesPostRequest.RequiredProperties = ["time_entry_type_id", "user_id"];

/**
 * @member {String} form_id
 */
TimeEntriesPostRequest.prototype['form_id'] = undefined;

/**
 * @member {String} from_time
 */
TimeEntriesPostRequest.prototype['from_time'] = undefined;

/**
 * @member {Boolean} is_all_day
 */
TimeEntriesPostRequest.prototype['is_all_day'] = undefined;

/**
 * @member {String} project_id
 */
TimeEntriesPostRequest.prototype['project_id'] = undefined;

/**
 * Amount of seconds - should only be included when using is_all_day, otherwise will be calculated from from_time and to_time
 * @member {Number} sum
 */
TimeEntriesPostRequest.prototype['sum'] = undefined;

/**
 * @member {String} time_entry_type_id
 */
TimeEntriesPostRequest.prototype['time_entry_type_id'] = undefined;

/**
 * @member {String} to_time
 */
TimeEntriesPostRequest.prototype['to_time'] = undefined;

/**
 * @member {String} user_id
 */
TimeEntriesPostRequest.prototype['user_id'] = undefined;






export default TimeEntriesPostRequest;

