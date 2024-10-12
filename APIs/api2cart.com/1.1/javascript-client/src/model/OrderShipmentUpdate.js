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
import OrderShipmentAddTrackingNumbersInner from './OrderShipmentAddTrackingNumbersInner';

/**
 * The OrderShipmentUpdate model module.
 * @module model/OrderShipmentUpdate
 * @version 1.1
 */
class OrderShipmentUpdate {
    /**
     * Constructs a new <code>OrderShipmentUpdate</code>.
     * @alias module:model/OrderShipmentUpdate
     * @param shipmentId {String} Shipment id indicates the number of delivery
     */
    constructor(shipmentId) { 
        
        OrderShipmentUpdate.initialize(this, shipmentId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, shipmentId) { 
        obj['is_shipped'] = true;
        obj['replace'] = true;
        obj['shipment_id'] = shipmentId;
    }

    /**
     * Constructs a <code>OrderShipmentUpdate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderShipmentUpdate} obj Optional instance to populate.
     * @return {module:model/OrderShipmentUpdate} The populated <code>OrderShipmentUpdate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderShipmentUpdate();

            if (data.hasOwnProperty('is_shipped')) {
                obj['is_shipped'] = ApiClient.convertToType(data['is_shipped'], 'Boolean');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
            if (data.hasOwnProperty('replace')) {
                obj['replace'] = ApiClient.convertToType(data['replace'], 'Boolean');
            }
            if (data.hasOwnProperty('shipment_id')) {
                obj['shipment_id'] = ApiClient.convertToType(data['shipment_id'], 'String');
            }
            if (data.hasOwnProperty('store_id')) {
                obj['store_id'] = ApiClient.convertToType(data['store_id'], 'String');
            }
            if (data.hasOwnProperty('tracking_link')) {
                obj['tracking_link'] = ApiClient.convertToType(data['tracking_link'], 'String');
            }
            if (data.hasOwnProperty('tracking_numbers')) {
                obj['tracking_numbers'] = ApiClient.convertToType(data['tracking_numbers'], [OrderShipmentAddTrackingNumbersInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderShipmentUpdate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderShipmentUpdate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrderShipmentUpdate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['order_id'] && !(typeof data['order_id'] === 'string' || data['order_id'] instanceof String)) {
            throw new Error("Expected the field `order_id` to be a primitive type in the JSON string but got " + data['order_id']);
        }
        // ensure the json data is a string
        if (data['shipment_id'] && !(typeof data['shipment_id'] === 'string' || data['shipment_id'] instanceof String)) {
            throw new Error("Expected the field `shipment_id` to be a primitive type in the JSON string but got " + data['shipment_id']);
        }
        // ensure the json data is a string
        if (data['store_id'] && !(typeof data['store_id'] === 'string' || data['store_id'] instanceof String)) {
            throw new Error("Expected the field `store_id` to be a primitive type in the JSON string but got " + data['store_id']);
        }
        // ensure the json data is a string
        if (data['tracking_link'] && !(typeof data['tracking_link'] === 'string' || data['tracking_link'] instanceof String)) {
            throw new Error("Expected the field `tracking_link` to be a primitive type in the JSON string but got " + data['tracking_link']);
        }
        if (data['tracking_numbers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tracking_numbers'])) {
                throw new Error("Expected the field `tracking_numbers` to be an array in the JSON data but got " + data['tracking_numbers']);
            }
            // validate the optional field `tracking_numbers` (array)
            for (const item of data['tracking_numbers']) {
                OrderShipmentAddTrackingNumbersInner.validateJSON(item);
            };
        }

        return true;
    }


}

OrderShipmentUpdate.RequiredProperties = ["shipment_id"];

/**
 * Defines shipment's status
 * @member {Boolean} is_shipped
 * @default true
 */
OrderShipmentUpdate.prototype['is_shipped'] = true;

/**
 * Defines the order that will be updated
 * @member {String} order_id
 */
OrderShipmentUpdate.prototype['order_id'] = undefined;

/**
 * Allows rewrite tracking numbers
 * @member {Boolean} replace
 * @default true
 */
OrderShipmentUpdate.prototype['replace'] = true;

/**
 * Shipment id indicates the number of delivery
 * @member {String} shipment_id
 */
OrderShipmentUpdate.prototype['shipment_id'] = undefined;

/**
 * Store Id
 * @member {String} store_id
 */
OrderShipmentUpdate.prototype['store_id'] = undefined;

/**
 * Defines custom tracking link
 * @member {String} tracking_link
 */
OrderShipmentUpdate.prototype['tracking_link'] = undefined;

/**
 * Defines shipment's tracking numbers that have to be added</br> How set tracking numbers to appropriate carrier:<ul><li>tracking_numbers[]=a2c.demo1,a2c.demo2 - set default carrier</li><li>tracking_numbers[<b>carrier_id</b>]=a2c.demo - set appropriate carrier</li></ul>To get the list of carriers IDs that are available in your store, use the <a href = \"https://api2cart.com/docs/#/cart/CartInfo\">cart.info</a > method
 * @member {Array.<module:model/OrderShipmentAddTrackingNumbersInner>} tracking_numbers
 */
OrderShipmentUpdate.prototype['tracking_numbers'] = undefined;






export default OrderShipmentUpdate;

