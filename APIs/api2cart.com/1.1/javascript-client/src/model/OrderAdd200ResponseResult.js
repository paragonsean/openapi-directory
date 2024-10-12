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
 * The OrderAdd200ResponseResult model module.
 * @module model/OrderAdd200ResponseResult
 * @version 1.1
 */
class OrderAdd200ResponseResult {
    /**
     * Constructs a new <code>OrderAdd200ResponseResult</code>.
     * @alias module:model/OrderAdd200ResponseResult
     */
    constructor() { 
        
        OrderAdd200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderAdd200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderAdd200ResponseResult} obj Optional instance to populate.
     * @return {module:model/OrderAdd200ResponseResult} The populated <code>OrderAdd200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderAdd200ResponseResult();

            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderAdd200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderAdd200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['order_id'] && !(typeof data['order_id'] === 'string' || data['order_id'] instanceof String)) {
            throw new Error("Expected the field `order_id` to be a primitive type in the JSON string but got " + data['order_id']);
        }

        return true;
    }


}



/**
 * @member {String} order_id
 */
OrderAdd200ResponseResult.prototype['order_id'] = undefined;






export default OrderAdd200ResponseResult;

