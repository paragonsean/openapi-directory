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
import Order from './Order';

/**
 * The OrderInfo200Response model module.
 * @module model/OrderInfo200Response
 * @version 1.1
 */
class OrderInfo200Response {
    /**
     * Constructs a new <code>OrderInfo200Response</code>.
     * @alias module:model/OrderInfo200Response
     */
    constructor() { 
        
        OrderInfo200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderInfo200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderInfo200Response} obj Optional instance to populate.
     * @return {module:model/OrderInfo200Response} The populated <code>OrderInfo200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderInfo200Response();

            if (data.hasOwnProperty('result')) {
                obj['result'] = Order.constructFromObject(data['result']);
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
     * Validates the JSON data with respect to <code>OrderInfo200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderInfo200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `result`
        if (data['result']) { // data not null
          Order.validateJSON(data['result']);
        }
        // ensure the json data is a string
        if (data['return_message'] && !(typeof data['return_message'] === 'string' || data['return_message'] instanceof String)) {
            throw new Error("Expected the field `return_message` to be a primitive type in the JSON string but got " + data['return_message']);
        }

        return true;
    }


}



/**
 * @member {module:model/Order} result
 */
OrderInfo200Response.prototype['result'] = undefined;

/**
 * @member {Number} return_code
 */
OrderInfo200Response.prototype['return_code'] = undefined;

/**
 * @member {String} return_message
 */
OrderInfo200Response.prototype['return_message'] = undefined;






export default OrderInfo200Response;

