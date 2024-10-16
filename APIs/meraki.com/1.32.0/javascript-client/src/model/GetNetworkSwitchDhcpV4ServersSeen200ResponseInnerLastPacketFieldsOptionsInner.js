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
 * The GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner model module.
 * @module model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner
 * @version 1.32.0
 */
class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner {
    /**
     * Constructs a new <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner</code>.
     * @alias module:model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner
     */
    constructor() { 
        
        GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner} The populated <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * Option name.
 * @member {String} name
 */
GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner.prototype['name'] = undefined;

/**
 * Option value.
 * @member {String} value
 */
GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner.prototype['value'] = undefined;






export default GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketFieldsOptionsInner;

