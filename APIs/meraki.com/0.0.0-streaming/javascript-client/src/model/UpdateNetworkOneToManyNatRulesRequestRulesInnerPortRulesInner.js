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

/**
 * The UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner model module.
 * @module model/UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner
 * @version 0.0.0-streaming
 */
class UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner {
    /**
     * Constructs a new <code>UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner</code>.
     * @alias module:model/UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner
     */
    constructor() { 
        
        UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner} The populated <code>UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner();

            if (data.hasOwnProperty('allowedIps')) {
                obj['allowedIps'] = ApiClient.convertToType(data['allowedIps'], ['String']);
            }
            if (data.hasOwnProperty('localIp')) {
                obj['localIp'] = ApiClient.convertToType(data['localIp'], 'String');
            }
            if (data.hasOwnProperty('localPort')) {
                obj['localPort'] = ApiClient.convertToType(data['localPort'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('protocol')) {
                obj['protocol'] = ApiClient.convertToType(data['protocol'], 'String');
            }
            if (data.hasOwnProperty('publicPort')) {
                obj['publicPort'] = ApiClient.convertToType(data['publicPort'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['allowedIps'])) {
            throw new Error("Expected the field `allowedIps` to be an array in the JSON data but got " + data['allowedIps']);
        }
        // ensure the json data is a string
        if (data['localIp'] && !(typeof data['localIp'] === 'string' || data['localIp'] instanceof String)) {
            throw new Error("Expected the field `localIp` to be a primitive type in the JSON string but got " + data['localIp']);
        }
        // ensure the json data is a string
        if (data['localPort'] && !(typeof data['localPort'] === 'string' || data['localPort'] instanceof String)) {
            throw new Error("Expected the field `localPort` to be a primitive type in the JSON string but got " + data['localPort']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['protocol'] && !(typeof data['protocol'] === 'string' || data['protocol'] instanceof String)) {
            throw new Error("Expected the field `protocol` to be a primitive type in the JSON string but got " + data['protocol']);
        }
        // ensure the json data is a string
        if (data['publicPort'] && !(typeof data['publicPort'] === 'string' || data['publicPort'] instanceof String)) {
            throw new Error("Expected the field `publicPort` to be a primitive type in the JSON string but got " + data['publicPort']);
        }

        return true;
    }


}



/**
 * Remote IP addresses or ranges that are permitted to access the internal resource via this port forwarding rule, or 'any'
 * @member {Array.<String>} allowedIps
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.prototype['allowedIps'] = undefined;

/**
 * Local IP address to which traffic will be forwarded
 * @member {String} localIp
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.prototype['localIp'] = undefined;

/**
 * Destination port of the forwarded traffic that will be sent from the MX to the specified host on the LAN. If you simply wish to forward the traffic without translating the port, this should be the same as the Public port
 * @member {String} localPort
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.prototype['localPort'] = undefined;

/**
 * A description of the rule
 * @member {String} name
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.prototype['name'] = undefined;

/**
 * 'tcp' or 'udp'
 * @member {module:model/UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.ProtocolEnum} protocol
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.prototype['protocol'] = undefined;

/**
 * Destination port of the traffic that is arriving on the WAN
 * @member {String} publicPort
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner.prototype['publicPort'] = undefined;





/**
 * Allowed values for the <code>protocol</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner['ProtocolEnum'] = {

    /**
     * value: "tcp"
     * @const
     */
    "tcp": "tcp",

    /**
     * value: "udp"
     * @const
     */
    "udp": "udp"
};



export default UpdateNetworkOneToManyNatRulesRequestRulesInnerPortRulesInner;

