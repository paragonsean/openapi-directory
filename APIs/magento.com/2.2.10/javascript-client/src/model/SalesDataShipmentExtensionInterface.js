/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SalesDataShipmentExtensionInterface model module.
 * @module model/SalesDataShipmentExtensionInterface
 * @version 2.2.10
 */
class SalesDataShipmentExtensionInterface {
    /**
     * Constructs a new <code>SalesDataShipmentExtensionInterface</code>.
     * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentInterface
     * @alias module:model/SalesDataShipmentExtensionInterface
     */
    constructor() { 
        
        SalesDataShipmentExtensionInterface.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SalesDataShipmentExtensionInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesDataShipmentExtensionInterface} obj Optional instance to populate.
     * @return {module:model/SalesDataShipmentExtensionInterface} The populated <code>SalesDataShipmentExtensionInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesDataShipmentExtensionInterface();

            if (data.hasOwnProperty('ext_location_id')) {
                obj['ext_location_id'] = ApiClient.convertToType(data['ext_location_id'], 'String');
            }
            if (data.hasOwnProperty('ext_return_shipment_id')) {
                obj['ext_return_shipment_id'] = ApiClient.convertToType(data['ext_return_shipment_id'], 'String');
            }
            if (data.hasOwnProperty('ext_shipment_id')) {
                obj['ext_shipment_id'] = ApiClient.convertToType(data['ext_shipment_id'], 'String');
            }
            if (data.hasOwnProperty('ext_tracking_reference')) {
                obj['ext_tracking_reference'] = ApiClient.convertToType(data['ext_tracking_reference'], 'String');
            }
            if (data.hasOwnProperty('ext_tracking_url')) {
                obj['ext_tracking_url'] = ApiClient.convertToType(data['ext_tracking_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesDataShipmentExtensionInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesDataShipmentExtensionInterface</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ext_location_id'] && !(typeof data['ext_location_id'] === 'string' || data['ext_location_id'] instanceof String)) {
            throw new Error("Expected the field `ext_location_id` to be a primitive type in the JSON string but got " + data['ext_location_id']);
        }
        // ensure the json data is a string
        if (data['ext_return_shipment_id'] && !(typeof data['ext_return_shipment_id'] === 'string' || data['ext_return_shipment_id'] instanceof String)) {
            throw new Error("Expected the field `ext_return_shipment_id` to be a primitive type in the JSON string but got " + data['ext_return_shipment_id']);
        }
        // ensure the json data is a string
        if (data['ext_shipment_id'] && !(typeof data['ext_shipment_id'] === 'string' || data['ext_shipment_id'] instanceof String)) {
            throw new Error("Expected the field `ext_shipment_id` to be a primitive type in the JSON string but got " + data['ext_shipment_id']);
        }
        // ensure the json data is a string
        if (data['ext_tracking_reference'] && !(typeof data['ext_tracking_reference'] === 'string' || data['ext_tracking_reference'] instanceof String)) {
            throw new Error("Expected the field `ext_tracking_reference` to be a primitive type in the JSON string but got " + data['ext_tracking_reference']);
        }
        // ensure the json data is a string
        if (data['ext_tracking_url'] && !(typeof data['ext_tracking_url'] === 'string' || data['ext_tracking_url'] instanceof String)) {
            throw new Error("Expected the field `ext_tracking_url` to be a primitive type in the JSON string but got " + data['ext_tracking_url']);
        }

        return true;
    }


}



/**
 * @member {String} ext_location_id
 */
SalesDataShipmentExtensionInterface.prototype['ext_location_id'] = undefined;

/**
 * @member {String} ext_return_shipment_id
 */
SalesDataShipmentExtensionInterface.prototype['ext_return_shipment_id'] = undefined;

/**
 * @member {String} ext_shipment_id
 */
SalesDataShipmentExtensionInterface.prototype['ext_shipment_id'] = undefined;

/**
 * @member {String} ext_tracking_reference
 */
SalesDataShipmentExtensionInterface.prototype['ext_tracking_reference'] = undefined;

/**
 * @member {String} ext_tracking_url
 */
SalesDataShipmentExtensionInterface.prototype['ext_tracking_url'] = undefined;






export default SalesDataShipmentExtensionInterface;

