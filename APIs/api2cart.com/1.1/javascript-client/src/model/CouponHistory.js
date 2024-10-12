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
 * The CouponHistory model module.
 * @module model/CouponHistory
 * @version 1.1
 */
class CouponHistory {
    /**
     * Constructs a new <code>CouponHistory</code>.
     * @alias module:model/CouponHistory
     */
    constructor() { 
        
        CouponHistory.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CouponHistory</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CouponHistory} obj Optional instance to populate.
     * @return {module:model/CouponHistory} The populated <code>CouponHistory</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CouponHistory();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CouponHistory</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CouponHistory</code>.
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
 * @member {Object} additional_fields
 */
CouponHistory.prototype['additional_fields'] = undefined;

/**
 * @member {Number} amount
 */
CouponHistory.prototype['amount'] = undefined;

/**
 * @member {Object} custom_fields
 */
CouponHistory.prototype['custom_fields'] = undefined;

/**
 * @member {String} order_id
 */
CouponHistory.prototype['order_id'] = undefined;






export default CouponHistory;

