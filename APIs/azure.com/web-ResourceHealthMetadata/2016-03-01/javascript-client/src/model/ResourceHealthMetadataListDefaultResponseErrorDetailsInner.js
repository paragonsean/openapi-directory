/**
 * ResourceHealthMetadata API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ResourceHealthMetadataListDefaultResponseErrorDetailsInner model module.
 * @module model/ResourceHealthMetadataListDefaultResponseErrorDetailsInner
 * @version 2016-03-01
 */
class ResourceHealthMetadataListDefaultResponseErrorDetailsInner {
    /**
     * Constructs a new <code>ResourceHealthMetadataListDefaultResponseErrorDetailsInner</code>.
     * Detailed errors.
     * @alias module:model/ResourceHealthMetadataListDefaultResponseErrorDetailsInner
     */
    constructor() { 
        
        ResourceHealthMetadataListDefaultResponseErrorDetailsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResourceHealthMetadataListDefaultResponseErrorDetailsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourceHealthMetadataListDefaultResponseErrorDetailsInner} obj Optional instance to populate.
     * @return {module:model/ResourceHealthMetadataListDefaultResponseErrorDetailsInner} The populated <code>ResourceHealthMetadataListDefaultResponseErrorDetailsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourceHealthMetadataListDefaultResponseErrorDetailsInner();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
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
     * Validates the JSON data with respect to <code>ResourceHealthMetadataListDefaultResponseErrorDetailsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourceHealthMetadataListDefaultResponseErrorDetailsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
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
 * Standardized string to programmatically identify the error.
 * @member {String} code
 */
ResourceHealthMetadataListDefaultResponseErrorDetailsInner.prototype['code'] = undefined;

/**
 * Detailed error description and debugging information.
 * @member {String} message
 */
ResourceHealthMetadataListDefaultResponseErrorDetailsInner.prototype['message'] = undefined;

/**
 * Detailed error description and debugging information.
 * @member {String} target
 */
ResourceHealthMetadataListDefaultResponseErrorDetailsInner.prototype['target'] = undefined;






export default ResourceHealthMetadataListDefaultResponseErrorDetailsInner;

