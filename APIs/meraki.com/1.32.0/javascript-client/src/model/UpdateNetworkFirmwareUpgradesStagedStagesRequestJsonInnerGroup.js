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
 * The UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup model module.
 * @module model/UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup
 * @version 1.32.0
 */
class UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup {
    /**
     * Constructs a new <code>UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup</code>.
     * The Staged Upgrade Group
     * @alias module:model/UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup
     * @param id {String} ID of the Staged Upgrade Group
     */
    constructor(id) { 
        
        UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup} The populated <code>UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}

UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup.RequiredProperties = ["id"];

/**
 * ID of the Staged Upgrade Group
 * @member {String} id
 */
UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup.prototype['id'] = undefined;






export default UpdateNetworkFirmwareUpgradesStagedStagesRequestJsonInnerGroup;

