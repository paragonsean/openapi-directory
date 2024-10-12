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
 * The BasketItemAdd200ResponseResult model module.
 * @module model/BasketItemAdd200ResponseResult
 * @version 1.1
 */
class BasketItemAdd200ResponseResult {
    /**
     * Constructs a new <code>BasketItemAdd200ResponseResult</code>.
     * @alias module:model/BasketItemAdd200ResponseResult
     */
    constructor() { 
        
        BasketItemAdd200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BasketItemAdd200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BasketItemAdd200ResponseResult} obj Optional instance to populate.
     * @return {module:model/BasketItemAdd200ResponseResult} The populated <code>BasketItemAdd200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BasketItemAdd200ResponseResult();

            if (data.hasOwnProperty('added')) {
                obj['added'] = ApiClient.convertToType(data['added'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BasketItemAdd200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BasketItemAdd200ResponseResult</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Boolean} added
 */
BasketItemAdd200ResponseResult.prototype['added'] = undefined;






export default BasketItemAdd200ResponseResult;

