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
 * The OrderShipmentAdd200ResponseResult model module.
 * @module model/OrderShipmentAdd200ResponseResult
 * @version 1.1
 */
class OrderShipmentAdd200ResponseResult {
    /**
     * Constructs a new <code>OrderShipmentAdd200ResponseResult</code>.
     * @alias module:model/OrderShipmentAdd200ResponseResult
     */
    constructor() { 
        
        OrderShipmentAdd200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderShipmentAdd200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderShipmentAdd200ResponseResult} obj Optional instance to populate.
     * @return {module:model/OrderShipmentAdd200ResponseResult} The populated <code>OrderShipmentAdd200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderShipmentAdd200ResponseResult();

            if (data.hasOwnProperty('shipment_id')) {
                obj['shipment_id'] = ApiClient.convertToType(data['shipment_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderShipmentAdd200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderShipmentAdd200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['shipment_id'] && !(typeof data['shipment_id'] === 'string' || data['shipment_id'] instanceof String)) {
            throw new Error("Expected the field `shipment_id` to be a primitive type in the JSON string but got " + data['shipment_id']);
        }

        return true;
    }


}



/**
 * @member {String} shipment_id
 */
OrderShipmentAdd200ResponseResult.prototype['shipment_id'] = undefined;






export default OrderShipmentAdd200ResponseResult;

