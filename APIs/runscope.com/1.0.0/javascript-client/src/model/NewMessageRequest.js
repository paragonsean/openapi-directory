/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The NewMessageRequest model module.
 * @module model/NewMessageRequest
 * @version 1.0.0
 */
class NewMessageRequest {
    /**
     * Constructs a new <code>NewMessageRequest</code>.
     * @alias module:model/NewMessageRequest
     */
    constructor() { 
        
        NewMessageRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NewMessageRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NewMessageRequest} obj Optional instance to populate.
     * @return {module:model/NewMessageRequest} The populated <code>NewMessageRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NewMessageRequest();

            if (data.hasOwnProperty('body')) {
                obj['body'] = ApiClient.convertToType(data['body'], 'String');
            }
            if (data.hasOwnProperty('body_encoding')) {
                obj['body_encoding'] = ApiClient.convertToType(data['body_encoding'], 'String');
            }
            if (data.hasOwnProperty('form')) {
                obj['form'] = ApiClient.convertToType(data['form'], 'String');
            }
            if (data.hasOwnProperty('headers')) {
                obj['headers'] = ApiClient.convertToType(data['headers'], 'String');
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = ApiClient.convertToType(data['method'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Number');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NewMessageRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NewMessageRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['body'] && !(typeof data['body'] === 'string' || data['body'] instanceof String)) {
            throw new Error("Expected the field `body` to be a primitive type in the JSON string but got " + data['body']);
        }
        // ensure the json data is a string
        if (data['body_encoding'] && !(typeof data['body_encoding'] === 'string' || data['body_encoding'] instanceof String)) {
            throw new Error("Expected the field `body_encoding` to be a primitive type in the JSON string but got " + data['body_encoding']);
        }
        // ensure the json data is a string
        if (data['form'] && !(typeof data['form'] === 'string' || data['form'] instanceof String)) {
            throw new Error("Expected the field `form` to be a primitive type in the JSON string but got " + data['form']);
        }
        // ensure the json data is a string
        if (data['headers'] && !(typeof data['headers'] === 'string' || data['headers'] instanceof String)) {
            throw new Error("Expected the field `headers` to be a primitive type in the JSON string but got " + data['headers']);
        }
        // ensure the json data is a string
        if (data['method'] && !(typeof data['method'] === 'string' || data['method'] instanceof String)) {
            throw new Error("Expected the field `method` to be a primitive type in the JSON string but got " + data['method']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * HTTP request body (most commonly used for POST and PUT requests). If the request body contains binary data that cannot be included directly in the  JSON, encode the content with Base64 and include the body_encoding attribute accordingly. 
 * @member {String} body
 */
NewMessageRequest.prototype['body'] = undefined;

/**
 * If the request body was encoded with Base64, this field should be present and set to  \"base64\". If not specified, defaults to \"plaintext\" 
 * @member {String} body_encoding
 */
NewMessageRequest.prototype['body_encoding'] = undefined;

/**
 * JSON object of set of form fields included in a POST request.  Values can either be represented as a string or as an array of strings. 
 * @member {String} form
 */
NewMessageRequest.prototype['form'] = undefined;

/**
 * JSON object of header keys and values -- with values as a string or an array of strings.
 * @member {String} headers
 */
NewMessageRequest.prototype['headers'] = undefined;

/**
 * HTTP method name (GET, POST, PUT, HEAD, OPTIONS, PATCH, DELETE, etc.)
 * @member {String} method
 */
NewMessageRequest.prototype['method'] = undefined;

/**
 * Unix timestamp indicating when the request was made.
 * @member {Number} timestamp
 */
NewMessageRequest.prototype['timestamp'] = undefined;

/**
 * Full URL of the request, including URL querystring parameters.
 * @member {String} url
 */
NewMessageRequest.prototype['url'] = undefined;






export default NewMessageRequest;

