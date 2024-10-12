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

/**
 * The AttributeTypeList200ResponseResult model module.
 * @module model/AttributeTypeList200ResponseResult
 * @version 1.1
 */
class AttributeTypeList200ResponseResult {
    /**
     * Constructs a new <code>AttributeTypeList200ResponseResult</code>.
     * @alias module:model/AttributeTypeList200ResponseResult
     */
    constructor() { 
        
        AttributeTypeList200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AttributeTypeList200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AttributeTypeList200ResponseResult} obj Optional instance to populate.
     * @return {module:model/AttributeTypeList200ResponseResult} The populated <code>AttributeTypeList200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AttributeTypeList200ResponseResult();

            if (data.hasOwnProperty('attribute_type')) {
                obj['attribute_type'] = ApiClient.convertToType(data['attribute_type'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AttributeTypeList200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AttributeTypeList200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['attribute_type'])) {
            throw new Error("Expected the field `attribute_type` to be an array in the JSON data but got " + data['attribute_type']);
        }

        return true;
    }


}



/**
 * @member {Array.<String>} attribute_type
 */
AttributeTypeList200ResponseResult.prototype['attribute_type'] = undefined;






export default AttributeTypeList200ResponseResult;

