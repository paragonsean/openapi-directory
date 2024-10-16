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
 * The GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp model module.
 * @module model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
 * @version 1.32.0
 */
class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp {
    /**
     * Constructs a new <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp</code>.
     * UDP attributes of the packet.
     * @alias module:model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
     */
    constructor() { 
        
        GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp} obj Optional instance to populate.
     * @return {module:model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp} The populated <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp();

            if (data.hasOwnProperty('checksum')) {
                obj['checksum'] = ApiClient.convertToType(data['checksum'], 'String');
            }
            if (data.hasOwnProperty('length')) {
                obj['length'] = ApiClient.convertToType(data['length'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['checksum'] && !(typeof data['checksum'] === 'string' || data['checksum'] instanceof String)) {
            throw new Error("Expected the field `checksum` to be a primitive type in the JSON string but got " + data['checksum']);
        }

        return true;
    }


}



/**
 * UDP checksum of the packet.
 * @member {String} checksum
 */
GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.prototype['checksum'] = undefined;

/**
 * UDP length of the packet.
 * @member {Number} length
 */
GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.prototype['length'] = undefined;






export default GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp;

