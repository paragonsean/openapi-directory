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
 * The GetNetworkSmDeviceSecurityCenters200ResponseInner model module.
 * @module model/GetNetworkSmDeviceSecurityCenters200ResponseInner
 * @version 1.32.0
 */
class GetNetworkSmDeviceSecurityCenters200ResponseInner {
    /**
     * Constructs a new <code>GetNetworkSmDeviceSecurityCenters200ResponseInner</code>.
     * @alias module:model/GetNetworkSmDeviceSecurityCenters200ResponseInner
     */
    constructor() { 
        
        GetNetworkSmDeviceSecurityCenters200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSmDeviceSecurityCenters200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSmDeviceSecurityCenters200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkSmDeviceSecurityCenters200ResponseInner} The populated <code>GetNetworkSmDeviceSecurityCenters200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSmDeviceSecurityCenters200ResponseInner();

            if (data.hasOwnProperty('antiVirusName')) {
                obj['antiVirusName'] = ApiClient.convertToType(data['antiVirusName'], 'String');
            }
            if (data.hasOwnProperty('fireWallName')) {
                obj['fireWallName'] = ApiClient.convertToType(data['fireWallName'], 'String');
            }
            if (data.hasOwnProperty('hasAntiVirus')) {
                obj['hasAntiVirus'] = ApiClient.convertToType(data['hasAntiVirus'], 'Boolean');
            }
            if (data.hasOwnProperty('hasFireWallInstalled')) {
                obj['hasFireWallInstalled'] = ApiClient.convertToType(data['hasFireWallInstalled'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('isAutoLoginDisabled')) {
                obj['isAutoLoginDisabled'] = ApiClient.convertToType(data['isAutoLoginDisabled'], 'Boolean');
            }
            if (data.hasOwnProperty('isDiskEncrypted')) {
                obj['isDiskEncrypted'] = ApiClient.convertToType(data['isDiskEncrypted'], 'Boolean');
            }
            if (data.hasOwnProperty('isFireWallEnabled')) {
                obj['isFireWallEnabled'] = ApiClient.convertToType(data['isFireWallEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('isRooted')) {
                obj['isRooted'] = ApiClient.convertToType(data['isRooted'], 'Boolean');
            }
            if (data.hasOwnProperty('runningProcs')) {
                obj['runningProcs'] = ApiClient.convertToType(data['runningProcs'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSmDeviceSecurityCenters200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSmDeviceSecurityCenters200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['antiVirusName'] && !(typeof data['antiVirusName'] === 'string' || data['antiVirusName'] instanceof String)) {
            throw new Error("Expected the field `antiVirusName` to be a primitive type in the JSON string but got " + data['antiVirusName']);
        }
        // ensure the json data is a string
        if (data['fireWallName'] && !(typeof data['fireWallName'] === 'string' || data['fireWallName'] instanceof String)) {
            throw new Error("Expected the field `fireWallName` to be a primitive type in the JSON string but got " + data['fireWallName']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['runningProcs'] && !(typeof data['runningProcs'] === 'string' || data['runningProcs'] instanceof String)) {
            throw new Error("Expected the field `runningProcs` to be a primitive type in the JSON string but got " + data['runningProcs']);
        }

        return true;
    }


}



/**
 * The name of the Antivirus.
 * @member {String} antiVirusName
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['antiVirusName'] = undefined;

/**
 * The name of the Firewall.
 * @member {String} fireWallName
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['fireWallName'] = undefined;

/**
 * Boolean indicating if the device has Antivirus.
 * @member {Boolean} hasAntiVirus
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['hasAntiVirus'] = undefined;

/**
 * Boolean indicating if the device has a Firewall installed.
 * @member {Boolean} hasFireWallInstalled
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['hasFireWallInstalled'] = undefined;

/**
 * The Meraki identifier for the security center record.
 * @member {String} id
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['id'] = undefined;

/**
 * Boolean indicating if the device has auto login disabled.
 * @member {Boolean} isAutoLoginDisabled
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['isAutoLoginDisabled'] = undefined;

/**
 * Boolean indicating if the device has disk encryption.
 * @member {Boolean} isDiskEncrypted
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['isDiskEncrypted'] = undefined;

/**
 * Boolean indicating if the device has a Firewall enabled.
 * @member {Boolean} isFireWallEnabled
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['isFireWallEnabled'] = undefined;

/**
 * Boolean indicating if the device is rooted.
 * @member {Boolean} isRooted
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['isRooted'] = undefined;

/**
 * A comma seperated list of procs running on the device.
 * @member {String} runningProcs
 */
GetNetworkSmDeviceSecurityCenters200ResponseInner.prototype['runningProcs'] = undefined;






export default GetNetworkSmDeviceSecurityCenters200ResponseInner;

