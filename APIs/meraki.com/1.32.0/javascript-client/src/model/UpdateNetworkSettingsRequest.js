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
import GetNetworkSettings200ResponseSecurePort from './GetNetworkSettings200ResponseSecurePort';
import UpdateNetworkSettingsRequestLocalStatusPage from './UpdateNetworkSettingsRequestLocalStatusPage';

/**
 * The UpdateNetworkSettingsRequest model module.
 * @module model/UpdateNetworkSettingsRequest
 * @version 1.32.0
 */
class UpdateNetworkSettingsRequest {
    /**
     * Constructs a new <code>UpdateNetworkSettingsRequest</code>.
     * @alias module:model/UpdateNetworkSettingsRequest
     */
    constructor() { 
        
        UpdateNetworkSettingsRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkSettingsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSettingsRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSettingsRequest} The populated <code>UpdateNetworkSettingsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSettingsRequest();

            if (data.hasOwnProperty('localStatusPage')) {
                obj['localStatusPage'] = UpdateNetworkSettingsRequestLocalStatusPage.constructFromObject(data['localStatusPage']);
            }
            if (data.hasOwnProperty('localStatusPageEnabled')) {
                obj['localStatusPageEnabled'] = ApiClient.convertToType(data['localStatusPageEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('remoteStatusPageEnabled')) {
                obj['remoteStatusPageEnabled'] = ApiClient.convertToType(data['remoteStatusPageEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('securePort')) {
                obj['securePort'] = GetNetworkSettings200ResponseSecurePort.constructFromObject(data['securePort']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSettingsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSettingsRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `localStatusPage`
        if (data['localStatusPage']) { // data not null
          UpdateNetworkSettingsRequestLocalStatusPage.validateJSON(data['localStatusPage']);
        }
        // validate the optional field `securePort`
        if (data['securePort']) { // data not null
          GetNetworkSettings200ResponseSecurePort.validateJSON(data['securePort']);
        }

        return true;
    }


}



/**
 * @member {module:model/UpdateNetworkSettingsRequestLocalStatusPage} localStatusPage
 */
UpdateNetworkSettingsRequest.prototype['localStatusPage'] = undefined;

/**
 * Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
 * @member {Boolean} localStatusPageEnabled
 */
UpdateNetworkSettingsRequest.prototype['localStatusPageEnabled'] = undefined;

/**
 * Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
 * @member {Boolean} remoteStatusPageEnabled
 */
UpdateNetworkSettingsRequest.prototype['remoteStatusPageEnabled'] = undefined;

/**
 * @member {module:model/GetNetworkSettings200ResponseSecurePort} securePort
 */
UpdateNetworkSettingsRequest.prototype['securePort'] = undefined;






export default UpdateNetworkSettingsRequest;

