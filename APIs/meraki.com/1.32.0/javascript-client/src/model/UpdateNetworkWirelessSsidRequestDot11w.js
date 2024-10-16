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
 * The UpdateNetworkWirelessSsidRequestDot11w model module.
 * @module model/UpdateNetworkWirelessSsidRequestDot11w
 * @version 1.32.0
 */
class UpdateNetworkWirelessSsidRequestDot11w {
    /**
     * Constructs a new <code>UpdateNetworkWirelessSsidRequestDot11w</code>.
     * The current setting for Protected Management Frames (802.11w).
     * @alias module:model/UpdateNetworkWirelessSsidRequestDot11w
     */
    constructor() { 
        
        UpdateNetworkWirelessSsidRequestDot11w.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkWirelessSsidRequestDot11w</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkWirelessSsidRequestDot11w} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkWirelessSsidRequestDot11w} The populated <code>UpdateNetworkWirelessSsidRequestDot11w</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkWirelessSsidRequestDot11w();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('required')) {
                obj['required'] = ApiClient.convertToType(data['required'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkWirelessSsidRequestDot11w</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkWirelessSsidRequestDot11w</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Whether 802.11w is enabled or not.
 * @member {Boolean} enabled
 */
UpdateNetworkWirelessSsidRequestDot11w.prototype['enabled'] = undefined;

/**
 * (Optional) Whether 802.11w is required or not.
 * @member {Boolean} required
 */
UpdateNetworkWirelessSsidRequestDot11w.prototype['required'] = undefined;






export default UpdateNetworkWirelessSsidRequestDot11w;

