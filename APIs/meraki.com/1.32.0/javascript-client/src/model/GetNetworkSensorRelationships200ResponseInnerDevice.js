/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GetNetworkSensorRelationships200ResponseInnerDevice model module.
 * @module model/GetNetworkSensorRelationships200ResponseInnerDevice
 * @version 1.32.0
 */
class GetNetworkSensorRelationships200ResponseInnerDevice {
    /**
     * Constructs a new <code>GetNetworkSensorRelationships200ResponseInnerDevice</code>.
     * A sensor or gateway device in the network
     * @alias module:model/GetNetworkSensorRelationships200ResponseInnerDevice
     */
    constructor() { 
        
        GetNetworkSensorRelationships200ResponseInnerDevice.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSensorRelationships200ResponseInnerDevice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSensorRelationships200ResponseInnerDevice} obj Optional instance to populate.
     * @return {module:model/GetNetworkSensorRelationships200ResponseInnerDevice} The populated <code>GetNetworkSensorRelationships200ResponseInnerDevice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSensorRelationships200ResponseInnerDevice();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('productType')) {
                obj['productType'] = ApiClient.convertToType(data['productType'], 'String');
            }
            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSensorRelationships200ResponseInnerDevice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSensorRelationships200ResponseInnerDevice</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['productType'] && !(typeof data['productType'] === 'string' || data['productType'] instanceof String)) {
            throw new Error("Expected the field `productType` to be a primitive type in the JSON string but got " + data['productType']);
        }
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }

        return true;
    }


}



/**
 * The name of the device
 * @member {String} name
 */
GetNetworkSensorRelationships200ResponseInnerDevice.prototype['name'] = undefined;

/**
 * The product type of the device
 * @member {module:model/GetNetworkSensorRelationships200ResponseInnerDevice.ProductTypeEnum} productType
 */
GetNetworkSensorRelationships200ResponseInnerDevice.prototype['productType'] = undefined;

/**
 * The serial of the device
 * @member {String} serial
 */
GetNetworkSensorRelationships200ResponseInnerDevice.prototype['serial'] = undefined;





/**
 * Allowed values for the <code>productType</code> property.
 * @enum {String}
 * @readonly
 */
GetNetworkSensorRelationships200ResponseInnerDevice['ProductTypeEnum'] = {

    /**
     * value: "camera"
     * @const
     */
    "camera": "camera",

    /**
     * value: "sensor"
     * @const
     */
    "sensor": "sensor"
};



export default GetNetworkSensorRelationships200ResponseInnerDevice;

