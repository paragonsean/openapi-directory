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
 * The AttributeDelete200ResponseResult model module.
 * @module model/AttributeDelete200ResponseResult
 * @version 1.1
 */
class AttributeDelete200ResponseResult {
    /**
     * Constructs a new <code>AttributeDelete200ResponseResult</code>.
     * @alias module:model/AttributeDelete200ResponseResult
     */
    constructor() { 
        
        AttributeDelete200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AttributeDelete200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AttributeDelete200ResponseResult} obj Optional instance to populate.
     * @return {module:model/AttributeDelete200ResponseResult} The populated <code>AttributeDelete200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AttributeDelete200ResponseResult();

            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AttributeDelete200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AttributeDelete200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['deleted'] && !(typeof data['deleted'] === 'string' || data['deleted'] instanceof String)) {
            throw new Error("Expected the field `deleted` to be a primitive type in the JSON string but got " + data['deleted']);
        }

        return true;
    }


}



/**
 * @member {String} deleted
 */
AttributeDelete200ResponseResult.prototype['deleted'] = undefined;






export default AttributeDelete200ResponseResult;

