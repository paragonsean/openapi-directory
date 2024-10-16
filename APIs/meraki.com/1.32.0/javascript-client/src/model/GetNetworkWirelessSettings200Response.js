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
import GetNetworkWirelessSettings200ResponseNamedVlans from './GetNetworkWirelessSettings200ResponseNamedVlans';

/**
 * The GetNetworkWirelessSettings200Response model module.
 * @module model/GetNetworkWirelessSettings200Response
 * @version 1.32.0
 */
class GetNetworkWirelessSettings200Response {
    /**
     * Constructs a new <code>GetNetworkWirelessSettings200Response</code>.
     * @alias module:model/GetNetworkWirelessSettings200Response
     */
    constructor() { 
        
        GetNetworkWirelessSettings200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkWirelessSettings200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkWirelessSettings200Response} obj Optional instance to populate.
     * @return {module:model/GetNetworkWirelessSettings200Response} The populated <code>GetNetworkWirelessSettings200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkWirelessSettings200Response();

            if (data.hasOwnProperty('ipv6BridgeEnabled')) {
                obj['ipv6BridgeEnabled'] = ApiClient.convertToType(data['ipv6BridgeEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('ledLightsOn')) {
                obj['ledLightsOn'] = ApiClient.convertToType(data['ledLightsOn'], 'Boolean');
            }
            if (data.hasOwnProperty('locationAnalyticsEnabled')) {
                obj['locationAnalyticsEnabled'] = ApiClient.convertToType(data['locationAnalyticsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('meshingEnabled')) {
                obj['meshingEnabled'] = ApiClient.convertToType(data['meshingEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('namedVlans')) {
                obj['namedVlans'] = GetNetworkWirelessSettings200ResponseNamedVlans.constructFromObject(data['namedVlans']);
            }
            if (data.hasOwnProperty('upgradeStrategy')) {
                obj['upgradeStrategy'] = ApiClient.convertToType(data['upgradeStrategy'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkWirelessSettings200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkWirelessSettings200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `namedVlans`
        if (data['namedVlans']) { // data not null
          GetNetworkWirelessSettings200ResponseNamedVlans.validateJSON(data['namedVlans']);
        }
        // ensure the json data is a string
        if (data['upgradeStrategy'] && !(typeof data['upgradeStrategy'] === 'string' || data['upgradeStrategy'] instanceof String)) {
            throw new Error("Expected the field `upgradeStrategy` to be a primitive type in the JSON string but got " + data['upgradeStrategy']);
        }

        return true;
    }


}



/**
 * Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
 * @member {Boolean} ipv6BridgeEnabled
 */
GetNetworkWirelessSettings200Response.prototype['ipv6BridgeEnabled'] = undefined;

/**
 * Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
 * @member {Boolean} ledLightsOn
 */
GetNetworkWirelessSettings200Response.prototype['ledLightsOn'] = undefined;

/**
 * Toggle for enabling or disabling location analytics for your network
 * @member {Boolean} locationAnalyticsEnabled
 */
GetNetworkWirelessSettings200Response.prototype['locationAnalyticsEnabled'] = undefined;

/**
 * Toggle for enabling or disabling meshing in a network
 * @member {Boolean} meshingEnabled
 */
GetNetworkWirelessSettings200Response.prototype['meshingEnabled'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSettings200ResponseNamedVlans} namedVlans
 */
GetNetworkWirelessSettings200Response.prototype['namedVlans'] = undefined;

/**
 * The upgrade strategy to apply to the network. Must be one of 'minimizeUpgradeTime' or 'minimizeClientDowntime'. Requires firmware version MR 26.8 or higher'
 * @member {module:model/GetNetworkWirelessSettings200Response.UpgradeStrategyEnum} upgradeStrategy
 */
GetNetworkWirelessSettings200Response.prototype['upgradeStrategy'] = undefined;





/**
 * Allowed values for the <code>upgradeStrategy</code> property.
 * @enum {String}
 * @readonly
 */
GetNetworkWirelessSettings200Response['UpgradeStrategyEnum'] = {

    /**
     * value: "minimizeClientDowntime"
     * @const
     */
    "minimizeClientDowntime": "minimizeClientDowntime",

    /**
     * value: "minimizeUpgradeTime"
     * @const
     */
    "minimizeUpgradeTime": "minimizeUpgradeTime"
};



export default GetNetworkWirelessSettings200Response;

