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
 * The OrderShipmentTrackingAdd model module.
 * @module model/OrderShipmentTrackingAdd
 * @version 1.1
 */
class OrderShipmentTrackingAdd {
    /**
     * Constructs a new <code>OrderShipmentTrackingAdd</code>.
     * @alias module:model/OrderShipmentTrackingAdd
     * @param shipmentId {String} Shipment id indicates the number of delivery
     * @param trackingNumber {String} Defines tracking number
     */
    constructor(shipmentId, trackingNumber) { 
        
        OrderShipmentTrackingAdd.initialize(this, shipmentId, trackingNumber);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, shipmentId, trackingNumber) { 
        obj['send_notifications'] = false;
        obj['shipment_id'] = shipmentId;
        obj['tracking_number'] = trackingNumber;
    }

    /**
     * Constructs a <code>OrderShipmentTrackingAdd</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderShipmentTrackingAdd} obj Optional instance to populate.
     * @return {module:model/OrderShipmentTrackingAdd} The populated <code>OrderShipmentTrackingAdd</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderShipmentTrackingAdd();

            if (data.hasOwnProperty('carrier_id')) {
                obj['carrier_id'] = ApiClient.convertToType(data['carrier_id'], 'String');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
            if (data.hasOwnProperty('send_notifications')) {
                obj['send_notifications'] = ApiClient.convertToType(data['send_notifications'], 'Boolean');
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
            if (data.hasOwnProperty('tracking_number')) {
                obj['tracking_number'] = ApiClient.convertToType(data['tracking_number'], 'String');
            }
            if (data.hasOwnProperty('tracking_provider')) {
                obj['tracking_provider'] = ApiClient.convertToType(data['tracking_provider'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderShipmentTrackingAdd</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderShipmentTrackingAdd</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrderShipmentTrackingAdd.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['carrier_id'] && !(typeof data['carrier_id'] === 'string' || data['carrier_id'] instanceof String)) {
            throw new Error("Expected the field `carrier_id` to be a primitive type in the JSON string but got " + data['carrier_id']);
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
        // ensure the json data is a string
        if (data['tracking_number'] && !(typeof data['tracking_number'] === 'string' || data['tracking_number'] instanceof String)) {
            throw new Error("Expected the field `tracking_number` to be a primitive type in the JSON string but got " + data['tracking_number']);
        }
        // ensure the json data is a string
        if (data['tracking_provider'] && !(typeof data['tracking_provider'] === 'string' || data['tracking_provider'] instanceof String)) {
            throw new Error("Expected the field `tracking_provider` to be a primitive type in the JSON string but got " + data['tracking_provider']);
        }

        return true;
    }


}

OrderShipmentTrackingAdd.RequiredProperties = ["shipment_id", "tracking_number"];

/**
 * Defines tracking carrier id
 * @member {String} carrier_id
 */
OrderShipmentTrackingAdd.prototype['carrier_id'] = undefined;

/**
 * Defines the order id
 * @member {String} order_id
 */
OrderShipmentTrackingAdd.prototype['order_id'] = undefined;

/**
 * Send notifications to customer after tracking was created
 * @member {Boolean} send_notifications
 * @default false
 */
OrderShipmentTrackingAdd.prototype['send_notifications'] = false;

/**
 * Shipment id indicates the number of delivery
 * @member {String} shipment_id
 */
OrderShipmentTrackingAdd.prototype['shipment_id'] = undefined;

/**
 * Store Id
 * @member {String} store_id
 */
OrderShipmentTrackingAdd.prototype['store_id'] = undefined;

/**
 * Defines custom tracking link
 * @member {String} tracking_link
 */
OrderShipmentTrackingAdd.prototype['tracking_link'] = undefined;

/**
 * Defines tracking number
 * @member {String} tracking_number
 */
OrderShipmentTrackingAdd.prototype['tracking_number'] = undefined;

/**
 * Defines name of the company which provides shipment tracking
 * @member {String} tracking_provider
 */
OrderShipmentTrackingAdd.prototype['tracking_provider'] = undefined;






export default OrderShipmentTrackingAdd;

