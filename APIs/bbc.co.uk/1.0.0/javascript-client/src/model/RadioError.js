/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
 * The RadioError model module.
 * @module model/RadioError
 * @version 1.0.0
 */
class RadioError {
    /**
     * Constructs a new <code>RadioError</code>.
     * @alias module:model/RadioError
     * @param code {String} 
     * @param detail {String} 
     * @param href {String} 
     * @param id {String} 
     * @param status {Number} 
     * @param timestamp {Number} 
     * @param title {String} 
     */
    constructor(code, detail, href, id, status, timestamp, title) { 
        
        RadioError.initialize(this, code, detail, href, id, status, timestamp, title);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code, detail, href, id, status, timestamp, title) { 
        obj['code'] = code;
        obj['detail'] = detail;
        obj['href'] = href;
        obj['id'] = id;
        obj['status'] = status;
        obj['timestamp'] = timestamp;
        obj['title'] = title;
    }

    /**
     * Constructs a <code>RadioError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RadioError} obj Optional instance to populate.
     * @return {module:model/RadioError} The populated <code>RadioError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RadioError();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('detail')) {
                obj['detail'] = ApiClient.convertToType(data['detail'], 'String');
            }
            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'Number');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Number');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RadioError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RadioError</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RadioError.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['detail'] && !(typeof data['detail'] === 'string' || data['detail'] instanceof String)) {
            throw new Error("Expected the field `detail` to be a primitive type in the JSON string but got " + data['detail']);
        }
        // ensure the json data is a string
        if (data['href'] && !(typeof data['href'] === 'string' || data['href'] instanceof String)) {
            throw new Error("Expected the field `href` to be a primitive type in the JSON string but got " + data['href']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

RadioError.RequiredProperties = ["code", "detail", "href", "id", "status", "timestamp", "title"];

/**
 * @member {String} code
 */
RadioError.prototype['code'] = undefined;

/**
 * @member {String} detail
 */
RadioError.prototype['detail'] = undefined;

/**
 * @member {String} href
 */
RadioError.prototype['href'] = undefined;

/**
 * @member {String} id
 */
RadioError.prototype['id'] = undefined;

/**
 * @member {Number} status
 */
RadioError.prototype['status'] = undefined;

/**
 * @member {Number} timestamp
 */
RadioError.prototype['timestamp'] = undefined;

/**
 * @member {String} title
 */
RadioError.prototype['title'] = undefined;






export default RadioError;

