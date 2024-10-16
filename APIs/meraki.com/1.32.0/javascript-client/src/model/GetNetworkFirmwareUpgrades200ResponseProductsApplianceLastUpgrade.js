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
import GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion from './GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion';
import GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion from './GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion';

/**
 * The GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade model module.
 * @module model/GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade
 * @version 1.32.0
 */
class GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade {
    /**
     * Constructs a new <code>GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade</code>.
     * Details of the last firmware upgrade on the device
     * @alias module:model/GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade
     */
    constructor() { 
        
        GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade} obj Optional instance to populate.
     * @return {module:model/GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade} The populated <code>GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade();

            if (data.hasOwnProperty('fromVersion')) {
                obj['fromVersion'] = GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion.constructFromObject(data['fromVersion']);
            }
            if (data.hasOwnProperty('time')) {
                obj['time'] = ApiClient.convertToType(data['time'], 'Date');
            }
            if (data.hasOwnProperty('toVersion')) {
                obj['toVersion'] = GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion.constructFromObject(data['toVersion']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade</code>.
     */
    static validateJSON(data) {
        // validate the optional field `fromVersion`
        if (data['fromVersion']) { // data not null
          GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion.validateJSON(data['fromVersion']);
        }
        // validate the optional field `toVersion`
        if (data['toVersion']) { // data not null
          GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion.validateJSON(data['toVersion']);
        }

        return true;
    }


}



/**
 * @member {module:model/GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion} fromVersion
 */
GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.prototype['fromVersion'] = undefined;

/**
 * Timestamp of the last successful firmware upgrade
 * @member {Date} time
 */
GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.prototype['time'] = undefined;

/**
 * @member {module:model/GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion} toVersion
 */
GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.prototype['toVersion'] = undefined;






export default GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade;

