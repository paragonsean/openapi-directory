/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import StoreAttributeGroup from './StoreAttributeGroup';

/**
 * The AttributeAttributesetList200Response model module.
 * @module model/AttributeAttributesetList200Response
 * @version 1.1
 */
class AttributeAttributesetList200Response {
    /**
     * Constructs a new <code>AttributeAttributesetList200Response</code>.
     * @alias module:model/AttributeAttributesetList200Response
     */
    constructor() { 
        
        AttributeAttributesetList200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AttributeAttributesetList200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AttributeAttributesetList200Response} obj Optional instance to populate.
     * @return {module:model/AttributeAttributesetList200Response} The populated <code>AttributeAttributesetList200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AttributeAttributesetList200Response();

            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], [StoreAttributeGroup]);
            }
            if (data.hasOwnProperty('return_code')) {
                obj['return_code'] = ApiClient.convertToType(data['return_code'], 'Number');
            }
            if (data.hasOwnProperty('return_message')) {
                obj['return_message'] = ApiClient.convertToType(data['return_message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AttributeAttributesetList200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AttributeAttributesetList200Response</code>.
     */
    static validateJSON(data) {
        if (data['result']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['result'])) {
                throw new Error("Expected the field `result` to be an array in the JSON data but got " + data['result']);
            }
            // validate the optional field `result` (array)
            for (const item of data['result']) {
                StoreAttributeGroup.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['return_message'] && !(typeof data['return_message'] === 'string' || data['return_message'] instanceof String)) {
            throw new Error("Expected the field `return_message` to be a primitive type in the JSON string but got " + data['return_message']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/StoreAttributeGroup>} result
 */
AttributeAttributesetList200Response.prototype['result'] = undefined;

/**
 * @member {Number} return_code
 */
AttributeAttributesetList200Response.prototype['return_code'] = undefined;

/**
 * @member {String} return_message
 */
AttributeAttributesetList200Response.prototype['return_message'] = undefined;






export default AttributeAttributesetList200Response;

