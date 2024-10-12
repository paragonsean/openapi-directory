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
 * The OrderRefundAdd200ResponseResult model module.
 * @module model/OrderRefundAdd200ResponseResult
 * @version 1.1
 */
class OrderRefundAdd200ResponseResult {
    /**
     * Constructs a new <code>OrderRefundAdd200ResponseResult</code>.
     * @alias module:model/OrderRefundAdd200ResponseResult
     */
    constructor() { 
        
        OrderRefundAdd200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderRefundAdd200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderRefundAdd200ResponseResult} obj Optional instance to populate.
     * @return {module:model/OrderRefundAdd200ResponseResult} The populated <code>OrderRefundAdd200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderRefundAdd200ResponseResult();

            if (data.hasOwnProperty('refund_id')) {
                obj['refund_id'] = ApiClient.convertToType(data['refund_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderRefundAdd200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderRefundAdd200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['refund_id'] && !(typeof data['refund_id'] === 'string' || data['refund_id'] instanceof String)) {
            throw new Error("Expected the field `refund_id` to be a primitive type in the JSON string but got " + data['refund_id']);
        }

        return true;
    }


}



/**
 * @member {String} refund_id
 */
OrderRefundAdd200ResponseResult.prototype['refund_id'] = undefined;






export default OrderRefundAdd200ResponseResult;

