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
import UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6 from './UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6';
import UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings from './UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings';

/**
 * The UpdateNetworkSwitchStackRoutingInterfaceRequest model module.
 * @module model/UpdateNetworkSwitchStackRoutingInterfaceRequest
 * @version 1.32.0
 */
class UpdateNetworkSwitchStackRoutingInterfaceRequest {
    /**
     * Constructs a new <code>UpdateNetworkSwitchStackRoutingInterfaceRequest</code>.
     * @alias module:model/UpdateNetworkSwitchStackRoutingInterfaceRequest
     */
    constructor() { 
        
        UpdateNetworkSwitchStackRoutingInterfaceRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkSwitchStackRoutingInterfaceRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSwitchStackRoutingInterfaceRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSwitchStackRoutingInterfaceRequest} The populated <code>UpdateNetworkSwitchStackRoutingInterfaceRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSwitchStackRoutingInterfaceRequest();

            if (data.hasOwnProperty('defaultGateway')) {
                obj['defaultGateway'] = ApiClient.convertToType(data['defaultGateway'], 'String');
            }
            if (data.hasOwnProperty('interfaceIp')) {
                obj['interfaceIp'] = ApiClient.convertToType(data['interfaceIp'], 'String');
            }
            if (data.hasOwnProperty('ipv6')) {
                obj['ipv6'] = UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6.constructFromObject(data['ipv6']);
            }
            if (data.hasOwnProperty('multicastRouting')) {
                obj['multicastRouting'] = ApiClient.convertToType(data['multicastRouting'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('ospfSettings')) {
                obj['ospfSettings'] = UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings.constructFromObject(data['ospfSettings']);
            }
            if (data.hasOwnProperty('subnet')) {
                obj['subnet'] = ApiClient.convertToType(data['subnet'], 'String');
            }
            if (data.hasOwnProperty('vlanId')) {
                obj['vlanId'] = ApiClient.convertToType(data['vlanId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSwitchStackRoutingInterfaceRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSwitchStackRoutingInterfaceRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['defaultGateway'] && !(typeof data['defaultGateway'] === 'string' || data['defaultGateway'] instanceof String)) {
            throw new Error("Expected the field `defaultGateway` to be a primitive type in the JSON string but got " + data['defaultGateway']);
        }
        // ensure the json data is a string
        if (data['interfaceIp'] && !(typeof data['interfaceIp'] === 'string' || data['interfaceIp'] instanceof String)) {
            throw new Error("Expected the field `interfaceIp` to be a primitive type in the JSON string but got " + data['interfaceIp']);
        }
        // validate the optional field `ipv6`
        if (data['ipv6']) { // data not null
          UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6.validateJSON(data['ipv6']);
        }
        // ensure the json data is a string
        if (data['multicastRouting'] && !(typeof data['multicastRouting'] === 'string' || data['multicastRouting'] instanceof String)) {
            throw new Error("Expected the field `multicastRouting` to be a primitive type in the JSON string but got " + data['multicastRouting']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `ospfSettings`
        if (data['ospfSettings']) { // data not null
          UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings.validateJSON(data['ospfSettings']);
        }
        // ensure the json data is a string
        if (data['subnet'] && !(typeof data['subnet'] === 'string' || data['subnet'] instanceof String)) {
            throw new Error("Expected the field `subnet` to be a primitive type in the JSON string but got " + data['subnet']);
        }

        return true;
    }


}



/**
 * The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
 * @member {String} defaultGateway
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['defaultGateway'] = undefined;

/**
 * The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
 * @member {String} interfaceIp
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['interfaceIp'] = undefined;

/**
 * @member {module:model/UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6} ipv6
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['ipv6'] = undefined;

/**
 * Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
 * @member {module:model/UpdateNetworkSwitchStackRoutingInterfaceRequest.MulticastRoutingEnum} multicastRouting
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['multicastRouting'] = undefined;

/**
 * A friendly name or description for the interface or VLAN.
 * @member {String} name
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['name'] = undefined;

/**
 * @member {module:model/UpdateNetworkSwitchStackRoutingInterfaceRequestOspfSettings} ospfSettings
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['ospfSettings'] = undefined;

/**
 * The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
 * @member {String} subnet
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['subnet'] = undefined;

/**
 * The VLAN this routed interface is on. VLAN must be between 1 and 4094.
 * @member {Number} vlanId
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest.prototype['vlanId'] = undefined;





/**
 * Allowed values for the <code>multicastRouting</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkSwitchStackRoutingInterfaceRequest['MulticastRoutingEnum'] = {

    /**
     * value: "IGMP snooping querier"
     * @const
     */
    "IGMP snooping querier": "IGMP snooping querier",

    /**
     * value: "disabled"
     * @const
     */
    "disabled": "disabled",

    /**
     * value: "enabled"
     * @const
     */
    "enabled": "enabled"
};



export default UpdateNetworkSwitchStackRoutingInterfaceRequest;

