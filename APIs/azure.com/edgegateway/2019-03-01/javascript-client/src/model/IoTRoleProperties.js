/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IoTDeviceInfo from './IoTDeviceInfo';
import MountPointMap from './MountPointMap';

/**
 * The IoTRoleProperties model module.
 * @module model/IoTRoleProperties
 * @version 2019-03-01
 */
class IoTRoleProperties {
    /**
     * Constructs a new <code>IoTRoleProperties</code>.
     * IoT role properties.
     * @alias module:model/IoTRoleProperties
     * @param hostPlatform {module:model/IoTRoleProperties.HostPlatformEnum} Host OS supported by the IoT role.
     * @param ioTDeviceDetails {module:model/IoTDeviceInfo} 
     * @param ioTEdgeDeviceDetails {module:model/IoTDeviceInfo} 
     * @param roleStatus {module:model/IoTRoleProperties.RoleStatusEnum} Role status.
     */
    constructor(hostPlatform, ioTDeviceDetails, ioTEdgeDeviceDetails, roleStatus) { 
        
        IoTRoleProperties.initialize(this, hostPlatform, ioTDeviceDetails, ioTEdgeDeviceDetails, roleStatus);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, hostPlatform, ioTDeviceDetails, ioTEdgeDeviceDetails, roleStatus) { 
        obj['hostPlatform'] = hostPlatform;
        obj['ioTDeviceDetails'] = ioTDeviceDetails;
        obj['ioTEdgeDeviceDetails'] = ioTEdgeDeviceDetails;
        obj['roleStatus'] = roleStatus;
    }

    /**
     * Constructs a <code>IoTRoleProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IoTRoleProperties} obj Optional instance to populate.
     * @return {module:model/IoTRoleProperties} The populated <code>IoTRoleProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IoTRoleProperties();

            if (data.hasOwnProperty('hostPlatform')) {
                obj['hostPlatform'] = ApiClient.convertToType(data['hostPlatform'], 'String');
            }
            if (data.hasOwnProperty('ioTDeviceDetails')) {
                obj['ioTDeviceDetails'] = IoTDeviceInfo.constructFromObject(data['ioTDeviceDetails']);
            }
            if (data.hasOwnProperty('ioTEdgeDeviceDetails')) {
                obj['ioTEdgeDeviceDetails'] = IoTDeviceInfo.constructFromObject(data['ioTEdgeDeviceDetails']);
            }
            if (data.hasOwnProperty('roleStatus')) {
                obj['roleStatus'] = ApiClient.convertToType(data['roleStatus'], 'String');
            }
            if (data.hasOwnProperty('shareMappings')) {
                obj['shareMappings'] = ApiClient.convertToType(data['shareMappings'], [MountPointMap]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IoTRoleProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IoTRoleProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of IoTRoleProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['hostPlatform'] && !(typeof data['hostPlatform'] === 'string' || data['hostPlatform'] instanceof String)) {
            throw new Error("Expected the field `hostPlatform` to be a primitive type in the JSON string but got " + data['hostPlatform']);
        }
        // validate the optional field `ioTDeviceDetails`
        if (data['ioTDeviceDetails']) { // data not null
          IoTDeviceInfo.validateJSON(data['ioTDeviceDetails']);
        }
        // validate the optional field `ioTEdgeDeviceDetails`
        if (data['ioTEdgeDeviceDetails']) { // data not null
          IoTDeviceInfo.validateJSON(data['ioTEdgeDeviceDetails']);
        }
        // ensure the json data is a string
        if (data['roleStatus'] && !(typeof data['roleStatus'] === 'string' || data['roleStatus'] instanceof String)) {
            throw new Error("Expected the field `roleStatus` to be a primitive type in the JSON string but got " + data['roleStatus']);
        }
        if (data['shareMappings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['shareMappings'])) {
                throw new Error("Expected the field `shareMappings` to be an array in the JSON data but got " + data['shareMappings']);
            }
            // validate the optional field `shareMappings` (array)
            for (const item of data['shareMappings']) {
                MountPointMap.validateJSON(item);
            };
        }

        return true;
    }


}

IoTRoleProperties.RequiredProperties = ["hostPlatform", "ioTDeviceDetails", "ioTEdgeDeviceDetails", "roleStatus"];

/**
 * Host OS supported by the IoT role.
 * @member {module:model/IoTRoleProperties.HostPlatformEnum} hostPlatform
 */
IoTRoleProperties.prototype['hostPlatform'] = undefined;

/**
 * @member {module:model/IoTDeviceInfo} ioTDeviceDetails
 */
IoTRoleProperties.prototype['ioTDeviceDetails'] = undefined;

/**
 * @member {module:model/IoTDeviceInfo} ioTEdgeDeviceDetails
 */
IoTRoleProperties.prototype['ioTEdgeDeviceDetails'] = undefined;

/**
 * Role status.
 * @member {module:model/IoTRoleProperties.RoleStatusEnum} roleStatus
 */
IoTRoleProperties.prototype['roleStatus'] = undefined;

/**
 * Mount points of shares in role(s).
 * @member {Array.<module:model/MountPointMap>} shareMappings
 */
IoTRoleProperties.prototype['shareMappings'] = undefined;





/**
 * Allowed values for the <code>hostPlatform</code> property.
 * @enum {String}
 * @readonly
 */
IoTRoleProperties['HostPlatformEnum'] = {

    /**
     * value: "Windows"
     * @const
     */
    "Windows": "Windows",

    /**
     * value: "Linux"
     * @const
     */
    "Linux": "Linux"
};


/**
 * Allowed values for the <code>roleStatus</code> property.
 * @enum {String}
 * @readonly
 */
IoTRoleProperties['RoleStatusEnum'] = {

    /**
     * value: "Enabled"
     * @const
     */
    "Enabled": "Enabled",

    /**
     * value: "Disabled"
     * @const
     */
    "Disabled": "Disabled"
};



export default IoTRoleProperties;

