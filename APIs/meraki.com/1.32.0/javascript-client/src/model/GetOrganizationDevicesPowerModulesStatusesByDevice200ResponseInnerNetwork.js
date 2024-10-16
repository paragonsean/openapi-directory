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
 * The GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork model module.
 * @module model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork
 * @version 1.32.0
 */
class GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork {
    /**
     * Constructs a new <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork</code>.
     * Network info.
     * @alias module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork
     */
    constructor() { 
        
        GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork} obj Optional instance to populate.
     * @return {module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork} The populated <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * ID for the network that the device is associated with.
 * @member {String} id
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork.prototype['id'] = undefined;






export default GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork;

