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
import UpdateNetworkSmDevicesFieldsRequestDeviceFields from './UpdateNetworkSmDevicesFieldsRequestDeviceFields';

/**
 * The UpdateNetworkSmDevicesFieldsRequest model module.
 * @module model/UpdateNetworkSmDevicesFieldsRequest
 * @version 1.32.0
 */
class UpdateNetworkSmDevicesFieldsRequest {
    /**
     * Constructs a new <code>UpdateNetworkSmDevicesFieldsRequest</code>.
     * @alias module:model/UpdateNetworkSmDevicesFieldsRequest
     * @param deviceFields {module:model/UpdateNetworkSmDevicesFieldsRequestDeviceFields} 
     */
    constructor(deviceFields) { 
        
        UpdateNetworkSmDevicesFieldsRequest.initialize(this, deviceFields);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deviceFields) { 
        obj['deviceFields'] = deviceFields;
    }

    /**
     * Constructs a <code>UpdateNetworkSmDevicesFieldsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSmDevicesFieldsRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSmDevicesFieldsRequest} The populated <code>UpdateNetworkSmDevicesFieldsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSmDevicesFieldsRequest();

            if (data.hasOwnProperty('deviceFields')) {
                obj['deviceFields'] = UpdateNetworkSmDevicesFieldsRequestDeviceFields.constructFromObject(data['deviceFields']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
            if (data.hasOwnProperty('wifiMac')) {
                obj['wifiMac'] = ApiClient.convertToType(data['wifiMac'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSmDevicesFieldsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSmDevicesFieldsRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateNetworkSmDevicesFieldsRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `deviceFields`
        if (data['deviceFields']) { // data not null
          UpdateNetworkSmDevicesFieldsRequestDeviceFields.validateJSON(data['deviceFields']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }
        // ensure the json data is a string
        if (data['wifiMac'] && !(typeof data['wifiMac'] === 'string' || data['wifiMac'] instanceof String)) {
            throw new Error("Expected the field `wifiMac` to be a primitive type in the JSON string but got " + data['wifiMac']);
        }

        return true;
    }


}

UpdateNetworkSmDevicesFieldsRequest.RequiredProperties = ["deviceFields"];

/**
 * @member {module:model/UpdateNetworkSmDevicesFieldsRequestDeviceFields} deviceFields
 */
UpdateNetworkSmDevicesFieldsRequest.prototype['deviceFields'] = undefined;

/**
 * The id of the device to be modified.
 * @member {String} id
 */
UpdateNetworkSmDevicesFieldsRequest.prototype['id'] = undefined;

/**
 * The serial of the device to be modified.
 * @member {String} serial
 */
UpdateNetworkSmDevicesFieldsRequest.prototype['serial'] = undefined;

/**
 * The wifiMac of the device to be modified.
 * @member {String} wifiMac
 */
UpdateNetworkSmDevicesFieldsRequest.prototype['wifiMac'] = undefined;






export default UpdateNetworkSmDevicesFieldsRequest;

