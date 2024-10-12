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
 * The CartClearCache200ResponseResult model module.
 * @module model/CartClearCache200ResponseResult
 * @version 1.1
 */
class CartClearCache200ResponseResult {
    /**
     * Constructs a new <code>CartClearCache200ResponseResult</code>.
     * @alias module:model/CartClearCache200ResponseResult
     */
    constructor() { 
        
        CartClearCache200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartClearCache200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartClearCache200ResponseResult} obj Optional instance to populate.
     * @return {module:model/CartClearCache200ResponseResult} The populated <code>CartClearCache200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartClearCache200ResponseResult();

            if (data.hasOwnProperty('cache_cleared')) {
                obj['cache_cleared'] = ApiClient.convertToType(data['cache_cleared'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartClearCache200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartClearCache200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['cache_cleared'] && !(typeof data['cache_cleared'] === 'string' || data['cache_cleared'] instanceof String)) {
            throw new Error("Expected the field `cache_cleared` to be a primitive type in the JSON string but got " + data['cache_cleared']);
        }

        return true;
    }


}



/**
 * @member {String} cache_cleared
 */
CartClearCache200ResponseResult.prototype['cache_cleared'] = undefined;






export default CartClearCache200ResponseResult;

