/**
 * ResourceHealthMetadata API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ResourceHealthMetadataListDefaultResponseErrorDetailsInner from './ResourceHealthMetadataListDefaultResponseErrorDetailsInner';

/**
 * The ResourceHealthMetadataListDefaultResponseError model module.
 * @module model/ResourceHealthMetadataListDefaultResponseError
 * @version 2018-02-01
 */
class ResourceHealthMetadataListDefaultResponseError {
    /**
     * Constructs a new <code>ResourceHealthMetadataListDefaultResponseError</code>.
     * Error model.
     * @alias module:model/ResourceHealthMetadataListDefaultResponseError
     */
    constructor() { 
        
        ResourceHealthMetadataListDefaultResponseError.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResourceHealthMetadataListDefaultResponseError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourceHealthMetadataListDefaultResponseError} obj Optional instance to populate.
     * @return {module:model/ResourceHealthMetadataListDefaultResponseError} The populated <code>ResourceHealthMetadataListDefaultResponseError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourceHealthMetadataListDefaultResponseError();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], [ResourceHealthMetadataListDefaultResponseErrorDetailsInner]);
            }
            if (data.hasOwnProperty('innererror')) {
                obj['innererror'] = ApiClient.convertToType(data['innererror'], 'String');
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
     * Validates the JSON data with respect to <code>ResourceHealthMetadataListDefaultResponseError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourceHealthMetadataListDefaultResponseError</code>.
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
                ResourceHealthMetadataListDefaultResponseErrorDetailsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['innererror'] && !(typeof data['innererror'] === 'string' || data['innererror'] instanceof String)) {
            throw new Error("Expected the field `innererror` to be a primitive type in the JSON string but got " + data['innererror']);
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
ResourceHealthMetadataListDefaultResponseError.prototype['code'] = undefined;

/**
 * @member {Array.<module:model/ResourceHealthMetadataListDefaultResponseErrorDetailsInner>} details
 */
ResourceHealthMetadataListDefaultResponseError.prototype['details'] = undefined;

/**
 * More information to debug error.
 * @member {String} innererror
 */
ResourceHealthMetadataListDefaultResponseError.prototype['innererror'] = undefined;

/**
 * Detailed error description and debugging information.
 * @member {String} message
 */
ResourceHealthMetadataListDefaultResponseError.prototype['message'] = undefined;

/**
 * Detailed error description and debugging information.
 * @member {String} target
 */
ResourceHealthMetadataListDefaultResponseError.prototype['target'] = undefined;






export default ResourceHealthMetadataListDefaultResponseError;

