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
 * The Project model module.
 * @module model/Project
 * @version 0.0.42
 */
class Project {
    /**
     * Constructs a new <code>Project</code>.
     * @alias module:model/Project
     * @param id {String} 
     * @param name {String} 
     */
    constructor(id, name) { 
        
        Project.initialize(this, id, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, name) { 
        obj['id'] = id;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>Project</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Project} obj Optional instance to populate.
     * @return {module:model/Project} The populated <code>Project</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Project();

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
            if (data.hasOwnProperty('end_time')) {
                obj['end_time'] = ApiClient.convertToType(data['end_time'], 'String');
            }
            if (data.hasOwnProperty('erp_project_id')) {
                obj['erp_project_id'] = ApiClient.convertToType(data['erp_project_id'], 'String');
            }
            if (data.hasOwnProperty('erp_task_id')) {
                obj['erp_task_id'] = ApiClient.convertToType(data['erp_task_id'], 'String');
            }
            if (data.hasOwnProperty('full_name')) {
                obj['full_name'] = ApiClient.convertToType(data['full_name'], 'String');
            }
            if (data.hasOwnProperty('has_final_invoice')) {
                obj['has_final_invoice'] = ApiClient.convertToType(data['has_final_invoice'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('is_fixed_price')) {
                obj['is_fixed_price'] = ApiClient.convertToType(data['is_fixed_price'], 'Boolean');
            }
            if (data.hasOwnProperty('is_offer')) {
                obj['is_offer'] = ApiClient.convertToType(data['is_offer'], 'Boolean');
            }
            if (data.hasOwnProperty('is_rotten')) {
                obj['is_rotten'] = ApiClient.convertToType(data['is_rotten'], 'String');
            }
            if (data.hasOwnProperty('latitude')) {
                obj['latitude'] = ApiClient.convertToType(data['latitude'], 'String');
            }
            if (data.hasOwnProperty('longitude')) {
                obj['longitude'] = ApiClient.convertToType(data['longitude'], 'String');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('not_invoiced_amount')) {
                obj['not_invoiced_amount'] = ApiClient.convertToType(data['not_invoiced_amount'], 'Number');
            }
            if (data.hasOwnProperty('offer_id')) {
                obj['offer_id'] = ApiClient.convertToType(data['offer_id'], 'String');
            }
            if (data.hasOwnProperty('parent_id')) {
                obj['parent_id'] = ApiClient.convertToType(data['parent_id'], 'String');
            }
            if (data.hasOwnProperty('pre_calculation_id')) {
                obj['pre_calculation_id'] = ApiClient.convertToType(data['pre_calculation_id'], 'String');
            }
            if (data.hasOwnProperty('products_total_cost_price')) {
                obj['products_total_cost_price'] = ApiClient.convertToType(data['products_total_cost_price'], 'Number');
            }
            if (data.hasOwnProperty('project_image_url')) {
                obj['project_image_url'] = ApiClient.convertToType(data['project_image_url'], 'String');
            }
            if (data.hasOwnProperty('project_number')) {
                obj['project_number'] = ApiClient.convertToType(data['project_number'], 'Number');
            }
            if (data.hasOwnProperty('project_status_id')) {
                obj['project_status_id'] = ApiClient.convertToType(data['project_status_id'], 'String');
            }
            if (data.hasOwnProperty('shared_project_id')) {
                obj['shared_project_id'] = ApiClient.convertToType(data['shared_project_id'], 'String');
            }
            if (data.hasOwnProperty('start_time')) {
                obj['start_time'] = ApiClient.convertToType(data['start_time'], 'String');
            }
            if (data.hasOwnProperty('street_name')) {
                obj['street_name'] = ApiClient.convertToType(data['street_name'], 'String');
            }
            if (data.hasOwnProperty('thumbnail')) {
                obj['thumbnail'] = ApiClient.convertToType(data['thumbnail'], 'String');
            }
            if (data.hasOwnProperty('total_sales_price')) {
                obj['total_sales_price'] = ApiClient.convertToType(data['total_sales_price'], 'Number');
            }
            if (data.hasOwnProperty('working_hours_total_cost_price')) {
                obj['working_hours_total_cost_price'] = ApiClient.convertToType(data['working_hours_total_cost_price'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Project</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Project</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Project.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
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
        if (data['end_time'] && !(typeof data['end_time'] === 'string' || data['end_time'] instanceof String)) {
            throw new Error("Expected the field `end_time` to be a primitive type in the JSON string but got " + data['end_time']);
        }
        // ensure the json data is a string
        if (data['erp_project_id'] && !(typeof data['erp_project_id'] === 'string' || data['erp_project_id'] instanceof String)) {
            throw new Error("Expected the field `erp_project_id` to be a primitive type in the JSON string but got " + data['erp_project_id']);
        }
        // ensure the json data is a string
        if (data['erp_task_id'] && !(typeof data['erp_task_id'] === 'string' || data['erp_task_id'] instanceof String)) {
            throw new Error("Expected the field `erp_task_id` to be a primitive type in the JSON string but got " + data['erp_task_id']);
        }
        // ensure the json data is a string
        if (data['full_name'] && !(typeof data['full_name'] === 'string' || data['full_name'] instanceof String)) {
            throw new Error("Expected the field `full_name` to be a primitive type in the JSON string but got " + data['full_name']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['is_offer'] && !(typeof data['is_offer'] === 'string' || data['is_offer'] instanceof String)) {
            throw new Error("Expected the field `is_offer` to be a primitive type in the JSON string but got " + data['is_offer']);
        }
        // ensure the json data is a string
        if (data['is_rotten'] && !(typeof data['is_rotten'] === 'string' || data['is_rotten'] instanceof String)) {
            throw new Error("Expected the field `is_rotten` to be a primitive type in the JSON string but got " + data['is_rotten']);
        }
        // ensure the json data is a string
        if (data['latitude'] && !(typeof data['latitude'] === 'string' || data['latitude'] instanceof String)) {
            throw new Error("Expected the field `latitude` to be a primitive type in the JSON string but got " + data['latitude']);
        }
        // ensure the json data is a string
        if (data['longitude'] && !(typeof data['longitude'] === 'string' || data['longitude'] instanceof String)) {
            throw new Error("Expected the field `longitude` to be a primitive type in the JSON string but got " + data['longitude']);
        }
        // ensure the json data is a string
        if (data['modified'] && !(typeof data['modified'] === 'string' || data['modified'] instanceof String)) {
            throw new Error("Expected the field `modified` to be a primitive type in the JSON string but got " + data['modified']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['offer_id'] && !(typeof data['offer_id'] === 'string' || data['offer_id'] instanceof String)) {
            throw new Error("Expected the field `offer_id` to be a primitive type in the JSON string but got " + data['offer_id']);
        }
        // ensure the json data is a string
        if (data['parent_id'] && !(typeof data['parent_id'] === 'string' || data['parent_id'] instanceof String)) {
            throw new Error("Expected the field `parent_id` to be a primitive type in the JSON string but got " + data['parent_id']);
        }
        // ensure the json data is a string
        if (data['pre_calculation_id'] && !(typeof data['pre_calculation_id'] === 'string' || data['pre_calculation_id'] instanceof String)) {
            throw new Error("Expected the field `pre_calculation_id` to be a primitive type in the JSON string but got " + data['pre_calculation_id']);
        }
        // ensure the json data is a string
        if (data['project_image_url'] && !(typeof data['project_image_url'] === 'string' || data['project_image_url'] instanceof String)) {
            throw new Error("Expected the field `project_image_url` to be a primitive type in the JSON string but got " + data['project_image_url']);
        }
        // ensure the json data is a string
        if (data['project_status_id'] && !(typeof data['project_status_id'] === 'string' || data['project_status_id'] instanceof String)) {
            throw new Error("Expected the field `project_status_id` to be a primitive type in the JSON string but got " + data['project_status_id']);
        }
        // ensure the json data is a string
        if (data['shared_project_id'] && !(typeof data['shared_project_id'] === 'string' || data['shared_project_id'] instanceof String)) {
            throw new Error("Expected the field `shared_project_id` to be a primitive type in the JSON string but got " + data['shared_project_id']);
        }
        // ensure the json data is a string
        if (data['start_time'] && !(typeof data['start_time'] === 'string' || data['start_time'] instanceof String)) {
            throw new Error("Expected the field `start_time` to be a primitive type in the JSON string but got " + data['start_time']);
        }
        // ensure the json data is a string
        if (data['street_name'] && !(typeof data['street_name'] === 'string' || data['street_name'] instanceof String)) {
            throw new Error("Expected the field `street_name` to be a primitive type in the JSON string but got " + data['street_name']);
        }
        // ensure the json data is a string
        if (data['thumbnail'] && !(typeof data['thumbnail'] === 'string' || data['thumbnail'] instanceof String)) {
            throw new Error("Expected the field `thumbnail` to be a primitive type in the JSON string but got " + data['thumbnail']);
        }

        return true;
    }


}

Project.RequiredProperties = ["id", "name"];

/**
 * @member {String} city_id
 */
Project.prototype['city_id'] = undefined;

/**
 * @member {String} company_id
 */
Project.prototype['company_id'] = undefined;

/**
 * @member {String} contact_id
 */
Project.prototype['contact_id'] = undefined;

/**
 * @member {String} created
 */
Project.prototype['created'] = undefined;

/**
 * @member {String} created_by_id
 */
Project.prototype['created_by_id'] = undefined;

/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
Project.prototype['deleted'] = undefined;

/**
 * @member {String} description
 */
Project.prototype['description'] = undefined;

/**
 * @member {String} end_time
 */
Project.prototype['end_time'] = undefined;

/**
 * @member {String} erp_project_id
 */
Project.prototype['erp_project_id'] = undefined;

/**
 * @member {String} erp_task_id
 */
Project.prototype['erp_task_id'] = undefined;

/**
 * Project number + name
 * @member {String} full_name
 */
Project.prototype['full_name'] = undefined;

/**
 * Is there at least one final invoice
 * @member {Boolean} has_final_invoice
 */
Project.prototype['has_final_invoice'] = undefined;

/**
 * @member {String} id
 */
Project.prototype['id'] = undefined;

/**
 * @member {Boolean} is_fixed_price
 */
Project.prototype['is_fixed_price'] = undefined;

/**
 * Is the project was offer
 * @member {Boolean} is_offer
 */
Project.prototype['is_offer'] = undefined;

/**
 * Last form date - read-only
 * @member {String} is_rotten
 */
Project.prototype['is_rotten'] = undefined;

/**
 * @member {String} latitude
 */
Project.prototype['latitude'] = undefined;

/**
 * @member {String} longitude
 */
Project.prototype['longitude'] = undefined;

/**
 * @member {String} modified
 */
Project.prototype['modified'] = undefined;

/**
 * @member {String} name
 */
Project.prototype['name'] = undefined;

/**
 * @member {Number} not_invoiced_amount
 */
Project.prototype['not_invoiced_amount'] = undefined;

/**
 * @member {String} offer_id
 */
Project.prototype['offer_id'] = undefined;

/**
 * @member {String} parent_id
 */
Project.prototype['parent_id'] = undefined;

/**
 * @member {String} pre_calculation_id
 */
Project.prototype['pre_calculation_id'] = undefined;

/**
 * @member {Number} products_total_cost_price
 */
Project.prototype['products_total_cost_price'] = undefined;

/**
 * @member {String} project_image_url
 */
Project.prototype['project_image_url'] = undefined;

/**
 * @member {Number} project_number
 */
Project.prototype['project_number'] = undefined;

/**
 * @member {String} project_status_id
 */
Project.prototype['project_status_id'] = undefined;

/**
 * @member {String} shared_project_id
 */
Project.prototype['shared_project_id'] = undefined;

/**
 * @member {String} start_time
 */
Project.prototype['start_time'] = undefined;

/**
 * @member {String} street_name
 */
Project.prototype['street_name'] = undefined;

/**
 * @member {String} thumbnail
 */
Project.prototype['thumbnail'] = undefined;

/**
 * @member {Number} total_sales_price
 */
Project.prototype['total_sales_price'] = undefined;

/**
 * @member {Number} working_hours_total_cost_price
 */
Project.prototype['working_hours_total_cost_price'] = undefined;






export default Project;

