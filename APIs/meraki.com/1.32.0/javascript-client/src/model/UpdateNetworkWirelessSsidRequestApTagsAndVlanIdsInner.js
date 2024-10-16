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
 * The UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner model module.
 * @module model/UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner
 * @version 1.32.0
 */
class UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner {
    /**
     * Constructs a new <code>UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner</code>.
     * @alias module:model/UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner
     */
    constructor() { 
        
        UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner} The populated <code>UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner();

            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
            }
            if (data.hasOwnProperty('vlanId')) {
                obj['vlanId'] = ApiClient.convertToType(data['vlanId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['tags'])) {
            throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
        }

        return true;
    }


}



/**
 * Array of AP tags
 * @member {Array.<String>} tags
 */
UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner.prototype['tags'] = undefined;

/**
 * Numerical identifier that is assigned to the VLAN
 * @member {Number} vlanId
 */
UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner.prototype['vlanId'] = undefined;






export default UpdateNetworkWirelessSsidRequestApTagsAndVlanIdsInner;

