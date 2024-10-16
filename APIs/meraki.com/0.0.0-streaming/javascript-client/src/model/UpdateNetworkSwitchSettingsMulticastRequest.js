/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UpdateNetworkSwitchSettingsMulticastRequestDefaultSettings from './UpdateNetworkSwitchSettingsMulticastRequestDefaultSettings';
import UpdateNetworkSwitchSettingsMulticastRequestOverridesInner from './UpdateNetworkSwitchSettingsMulticastRequestOverridesInner';

/**
 * The UpdateNetworkSwitchSettingsMulticastRequest model module.
 * @module model/UpdateNetworkSwitchSettingsMulticastRequest
 * @version 0.0.0-streaming
 */
class UpdateNetworkSwitchSettingsMulticastRequest {
    /**
     * Constructs a new <code>UpdateNetworkSwitchSettingsMulticastRequest</code>.
     * @alias module:model/UpdateNetworkSwitchSettingsMulticastRequest
     */
    constructor() { 
        
        UpdateNetworkSwitchSettingsMulticastRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkSwitchSettingsMulticastRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSwitchSettingsMulticastRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSwitchSettingsMulticastRequest} The populated <code>UpdateNetworkSwitchSettingsMulticastRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSwitchSettingsMulticastRequest();

            if (data.hasOwnProperty('defaultSettings')) {
                obj['defaultSettings'] = UpdateNetworkSwitchSettingsMulticastRequestDefaultSettings.constructFromObject(data['defaultSettings']);
            }
            if (data.hasOwnProperty('overrides')) {
                obj['overrides'] = ApiClient.convertToType(data['overrides'], [UpdateNetworkSwitchSettingsMulticastRequestOverridesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSwitchSettingsMulticastRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSwitchSettingsMulticastRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `defaultSettings`
        if (data['defaultSettings']) { // data not null
          UpdateNetworkSwitchSettingsMulticastRequestDefaultSettings.validateJSON(data['defaultSettings']);
        }
        if (data['overrides']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['overrides'])) {
                throw new Error("Expected the field `overrides` to be an array in the JSON data but got " + data['overrides']);
            }
            // validate the optional field `overrides` (array)
            for (const item of data['overrides']) {
                UpdateNetworkSwitchSettingsMulticastRequestOverridesInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/UpdateNetworkSwitchSettingsMulticastRequestDefaultSettings} defaultSettings
 */
UpdateNetworkSwitchSettingsMulticastRequest.prototype['defaultSettings'] = undefined;

/**
 * Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.
 * @member {Array.<module:model/UpdateNetworkSwitchSettingsMulticastRequestOverridesInner>} overrides
 */
UpdateNetworkSwitchSettingsMulticastRequest.prototype['overrides'] = undefined;






export default UpdateNetworkSwitchSettingsMulticastRequest;

