/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PluginDevice from './PluginDevice';

/**
 * The PluginConfigLinux model module.
 * @module model/PluginConfigLinux
 * @version 0.4.27
 */
class PluginConfigLinux {
    /**
     * Constructs a new <code>PluginConfigLinux</code>.
     * PluginConfigLinux plugin config linux
     * @alias module:model/PluginConfigLinux
     * @param allowAllDevices {Boolean} allow all devices
     * @param capabilities {Array.<String>} capabilities
     * @param devices {Array.<module:model/PluginDevice>} devices
     */
    constructor(allowAllDevices, capabilities, devices) { 
        
        PluginConfigLinux.initialize(this, allowAllDevices, capabilities, devices);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, allowAllDevices, capabilities, devices) { 
        obj['AllowAllDevices'] = allowAllDevices;
        obj['Capabilities'] = capabilities;
        obj['Devices'] = devices;
    }

    /**
     * Constructs a <code>PluginConfigLinux</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PluginConfigLinux} obj Optional instance to populate.
     * @return {module:model/PluginConfigLinux} The populated <code>PluginConfigLinux</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PluginConfigLinux();

            if (data.hasOwnProperty('AllowAllDevices')) {
                obj['AllowAllDevices'] = ApiClient.convertToType(data['AllowAllDevices'], 'Boolean');
            }
            if (data.hasOwnProperty('Capabilities')) {
                obj['Capabilities'] = ApiClient.convertToType(data['Capabilities'], ['String']);
            }
            if (data.hasOwnProperty('Devices')) {
                obj['Devices'] = ApiClient.convertToType(data['Devices'], [PluginDevice]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PluginConfigLinux</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PluginConfigLinux</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PluginConfigLinux.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Capabilities'])) {
            throw new Error("Expected the field `Capabilities` to be an array in the JSON data but got " + data['Capabilities']);
        }
        if (data['Devices']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Devices'])) {
                throw new Error("Expected the field `Devices` to be an array in the JSON data but got " + data['Devices']);
            }
            // validate the optional field `Devices` (array)
            for (const item of data['Devices']) {
                PluginDevice.validateJSON(item);
            };
        }

        return true;
    }


}

PluginConfigLinux.RequiredProperties = ["AllowAllDevices", "Capabilities", "Devices"];

/**
 * allow all devices
 * @member {Boolean} AllowAllDevices
 */
PluginConfigLinux.prototype['AllowAllDevices'] = undefined;

/**
 * capabilities
 * @member {Array.<String>} Capabilities
 */
PluginConfigLinux.prototype['Capabilities'] = undefined;

/**
 * devices
 * @member {Array.<module:model/PluginDevice>} Devices
 */
PluginConfigLinux.prototype['Devices'] = undefined;






export default PluginConfigLinux;

