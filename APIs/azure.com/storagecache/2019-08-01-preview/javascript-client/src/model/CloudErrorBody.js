/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CloudErrorBody model module.
 * @module model/CloudErrorBody
 * @version 2019-08-01-preview
 */
class CloudErrorBody {
    /**
     * Constructs a new <code>CloudErrorBody</code>.
     * An error response.
     * @alias module:model/CloudErrorBody
     */
    constructor() { 
        
        CloudErrorBody.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CloudErrorBody</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CloudErrorBody} obj Optional instance to populate.
     * @return {module:model/CloudErrorBody} The populated <code>CloudErrorBody</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CloudErrorBody();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], [CloudErrorBody]);
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('target')) {
                obj['target'] = ApiClient.convertToType(data['target'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CloudErrorBody</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CloudErrorBody</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        if (data['details']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['details'])) {
                throw new Error("Expected the field `details` to be an array in the JSON data but got " + data['details']);
            }
            // validate the optional field `details` (array)
            for (const item of data['details']) {
                CloudErrorBody.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['target'] && !(typeof data['target'] === 'string' || data['target'] instanceof String)) {
            throw new Error("Expected the field `target` to be a primitive type in the JSON string but got " + data['target']);
        }

        return true;
    }


}



/**
 * An identifier for the error. Codes are invariant and are intended to be consumed programmatically.
 * @member {String} code
 */
CloudErrorBody.prototype['code'] = undefined;

/**
 * A list of additional details about the error.
 * @member {Array.<module:model/CloudErrorBody>} details
 */
CloudErrorBody.prototype['details'] = undefined;

/**
 * A message describing the error, intended to be suitable for display in a user interface.
 * @member {String} message
 */
CloudErrorBody.prototype['message'] = undefined;

/**
 * The target of the particular error. For example, the name of the property in error.
 * @member {String} target
 */
CloudErrorBody.prototype['target'] = undefined;






export default CloudErrorBody;

