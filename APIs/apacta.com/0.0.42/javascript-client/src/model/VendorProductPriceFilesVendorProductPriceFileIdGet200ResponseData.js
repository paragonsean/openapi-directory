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
import VendorProductPriceFile from './VendorProductPriceFile';

/**
 * The VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData model module.
 * @module model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData
 * @version 0.0.42
 */
class VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData {
    /**
     * Constructs a new <code>VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData</code>.
     * @alias module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData
     * @implements module:model/VendorProductPriceFile
     */
    constructor() { 
        VendorProductPriceFile.initialize(this);
        VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData} obj Optional instance to populate.
     * @return {module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData} The populated <code>VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData();
            VendorProductPriceFile.constructFromObject(data, obj);

            if (data.hasOwnProperty('companies_vendor_id')) {
                obj['companies_vendor_id'] = ApiClient.convertToType(data['companies_vendor_id'], 'String');
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
            if (data.hasOwnProperty('dir')) {
                obj['dir'] = ApiClient.convertToType(data['dir'], 'String');
            }
            if (data.hasOwnProperty('file')) {
                obj['file'] = ApiClient.convertToType(data['file'], 'String');
            }
            if (data.hasOwnProperty('finished')) {
                obj['finished'] = ApiClient.convertToType(data['finished'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'String');
            }
            if (data.hasOwnProperty('original_file_name')) {
                obj['original_file_name'] = ApiClient.convertToType(data['original_file_name'], 'String');
            }
            if (data.hasOwnProperty('progress')) {
                obj['progress'] = ApiClient.convertToType(data['progress'], 'Number');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('vendor_products_count')) {
                obj['vendor_products_count'] = ApiClient.convertToType(data['vendor_products_count'], 'Number');
            }
            if (data.hasOwnProperty('vendor_products_count_total')) {
                obj['vendor_products_count_total'] = ApiClient.convertToType(data['vendor_products_count_total'], 'Number');
            }
            if (data.hasOwnProperty('download_link')) {
                obj['download_link'] = ApiClient.convertToType(data['download_link'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['companies_vendor_id'] && !(typeof data['companies_vendor_id'] === 'string' || data['companies_vendor_id'] instanceof String)) {
            throw new Error("Expected the field `companies_vendor_id` to be a primitive type in the JSON string but got " + data['companies_vendor_id']);
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
        if (data['dir'] && !(typeof data['dir'] === 'string' || data['dir'] instanceof String)) {
            throw new Error("Expected the field `dir` to be a primitive type in the JSON string but got " + data['dir']);
        }
        // ensure the json data is a string
        if (data['file'] && !(typeof data['file'] === 'string' || data['file'] instanceof String)) {
            throw new Error("Expected the field `file` to be a primitive type in the JSON string but got " + data['file']);
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
        if (data['original_file_name'] && !(typeof data['original_file_name'] === 'string' || data['original_file_name'] instanceof String)) {
            throw new Error("Expected the field `original_file_name` to be a primitive type in the JSON string but got " + data['original_file_name']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['download_link'] && !(typeof data['download_link'] === 'string' || data['download_link'] instanceof String)) {
            throw new Error("Expected the field `download_link` to be a primitive type in the JSON string but got " + data['download_link']);
        }

        return true;
    }


}



/**
 * @member {String} companies_vendor_id
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['companies_vendor_id'] = undefined;

/**
 * @member {String} created
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['created'] = undefined;

/**
 * @member {String} created_by_id
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['created_by_id'] = undefined;

/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['deleted'] = undefined;

/**
 * @member {String} dir
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['dir'] = undefined;

/**
 * @member {String} file
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['file'] = undefined;

/**
 * @member {Boolean} finished
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['finished'] = undefined;

/**
 * @member {String} id
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['id'] = undefined;

/**
 * @member {String} modified
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['modified'] = undefined;

/**
 * @member {String} original_file_name
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['original_file_name'] = undefined;

/**
 * @member {Number} progress
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['progress'] = undefined;

/**
 * @member {Number} size
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['size'] = undefined;

/**
 * @member {module:model/VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.StatusEnum} status
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['status'] = undefined;

/**
 * @member {String} type
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['type'] = undefined;

/**
 * @member {Number} vendor_products_count
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['vendor_products_count'] = undefined;

/**
 * @member {Number} vendor_products_count_total
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['vendor_products_count_total'] = undefined;

/**
 * @member {String} download_link
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData.prototype['download_link'] = undefined;


// Implement VendorProductPriceFile interface:
/**
 * @member {String} companies_vendor_id
 */
VendorProductPriceFile.prototype['companies_vendor_id'] = undefined;
/**
 * @member {String} created
 */
VendorProductPriceFile.prototype['created'] = undefined;
/**
 * @member {String} created_by_id
 */
VendorProductPriceFile.prototype['created_by_id'] = undefined;
/**
 * Only present if it's a deleted object
 * @member {String} deleted
 */
VendorProductPriceFile.prototype['deleted'] = undefined;
/**
 * @member {String} dir
 */
VendorProductPriceFile.prototype['dir'] = undefined;
/**
 * @member {String} file
 */
VendorProductPriceFile.prototype['file'] = undefined;
/**
 * @member {Boolean} finished
 */
VendorProductPriceFile.prototype['finished'] = undefined;
/**
 * @member {String} id
 */
VendorProductPriceFile.prototype['id'] = undefined;
/**
 * @member {String} modified
 */
VendorProductPriceFile.prototype['modified'] = undefined;
/**
 * @member {String} original_file_name
 */
VendorProductPriceFile.prototype['original_file_name'] = undefined;
/**
 * @member {Number} progress
 */
VendorProductPriceFile.prototype['progress'] = undefined;
/**
 * @member {Number} size
 */
VendorProductPriceFile.prototype['size'] = undefined;
/**
 * @member {module:model/VendorProductPriceFile.StatusEnum} status
 */
VendorProductPriceFile.prototype['status'] = undefined;
/**
 * @member {String} type
 */
VendorProductPriceFile.prototype['type'] = undefined;
/**
 * @member {Number} vendor_products_count
 */
VendorProductPriceFile.prototype['vendor_products_count'] = undefined;
/**
 * @member {Number} vendor_products_count_total
 */
VendorProductPriceFile.prototype['vendor_products_count_total'] = undefined;



/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData['StatusEnum'] = {

    /**
     * value: "awaiting"
     * @const
     */
    "awaiting": "awaiting",

    /**
     * value: "fresh"
     * @const
     */
    "fresh": "fresh",

    /**
     * value: "expired"
     * @const
     */
    "expired": "expired",

    /**
     * value: "failed"
     * @const
     */
    "failed": "failed"
};



export default VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData;

