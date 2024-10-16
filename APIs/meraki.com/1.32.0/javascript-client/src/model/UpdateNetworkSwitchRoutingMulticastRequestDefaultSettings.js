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
 * The UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings model module.
 * @module model/UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings
 * @version 1.32.0
 */
class UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings {
    /**
     * Constructs a new <code>UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings</code>.
     * Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
     * @alias module:model/UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings
     */
    constructor() { 
        
        UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings} The populated <code>UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings();

            if (data.hasOwnProperty('floodUnknownMulticastTrafficEnabled')) {
                obj['floodUnknownMulticastTrafficEnabled'] = ApiClient.convertToType(data['floodUnknownMulticastTrafficEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('igmpSnoopingEnabled')) {
                obj['igmpSnoopingEnabled'] = ApiClient.convertToType(data['igmpSnoopingEnabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Flood unknown multicast traffic setting for entire network
 * @member {Boolean} floodUnknownMulticastTrafficEnabled
 */
UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.prototype['floodUnknownMulticastTrafficEnabled'] = undefined;

/**
 * IGMP snooping setting for entire network
 * @member {Boolean} igmpSnoopingEnabled
 */
UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.prototype['igmpSnoopingEnabled'] = undefined;






export default UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings;

