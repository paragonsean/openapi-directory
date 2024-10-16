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
import GetDeviceSwitchRoutingInterfaces200ResponseInnerIpv6 from './GetDeviceSwitchRoutingInterfaces200ResponseInnerIpv6';
import GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfSettings from './GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfSettings';
import GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfV3 from './GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfV3';

/**
 * The GetDeviceSwitchRoutingInterfaces200ResponseInner model module.
 * @module model/GetDeviceSwitchRoutingInterfaces200ResponseInner
 * @version 1.32.0
 */
class GetDeviceSwitchRoutingInterfaces200ResponseInner {
    /**
     * Constructs a new <code>GetDeviceSwitchRoutingInterfaces200ResponseInner</code>.
     * @alias module:model/GetDeviceSwitchRoutingInterfaces200ResponseInner
     */
    constructor() { 
        
        GetDeviceSwitchRoutingInterfaces200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetDeviceSwitchRoutingInterfaces200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetDeviceSwitchRoutingInterfaces200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetDeviceSwitchRoutingInterfaces200ResponseInner} The populated <code>GetDeviceSwitchRoutingInterfaces200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetDeviceSwitchRoutingInterfaces200ResponseInner();

            if (data.hasOwnProperty('defaultGateway')) {
                obj['defaultGateway'] = ApiClient.convertToType(data['defaultGateway'], 'String');
            }
            if (data.hasOwnProperty('interfaceId')) {
                obj['interfaceId'] = ApiClient.convertToType(data['interfaceId'], 'String');
            }
            if (data.hasOwnProperty('interfaceIp')) {
                obj['interfaceIp'] = ApiClient.convertToType(data['interfaceIp'], 'String');
            }
            if (data.hasOwnProperty('ipv6')) {
                obj['ipv6'] = GetDeviceSwitchRoutingInterfaces200ResponseInnerIpv6.constructFromObject(data['ipv6']);
            }
            if (data.hasOwnProperty('multicastRouting')) {
                obj['multicastRouting'] = ApiClient.convertToType(data['multicastRouting'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('ospfSettings')) {
                obj['ospfSettings'] = GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfSettings.constructFromObject(data['ospfSettings']);
            }
            if (data.hasOwnProperty('ospfV3')) {
                obj['ospfV3'] = GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfV3.constructFromObject(data['ospfV3']);
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
     * Validates the JSON data with respect to <code>GetDeviceSwitchRoutingInterfaces200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetDeviceSwitchRoutingInterfaces200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['defaultGateway'] && !(typeof data['defaultGateway'] === 'string' || data['defaultGateway'] instanceof String)) {
            throw new Error("Expected the field `defaultGateway` to be a primitive type in the JSON string but got " + data['defaultGateway']);
        }
        // ensure the json data is a string
        if (data['interfaceId'] && !(typeof data['interfaceId'] === 'string' || data['interfaceId'] instanceof String)) {
            throw new Error("Expected the field `interfaceId` to be a primitive type in the JSON string but got " + data['interfaceId']);
        }
        // ensure the json data is a string
        if (data['interfaceIp'] && !(typeof data['interfaceIp'] === 'string' || data['interfaceIp'] instanceof String)) {
            throw new Error("Expected the field `interfaceIp` to be a primitive type in the JSON string but got " + data['interfaceIp']);
        }
        // validate the optional field `ipv6`
        if (data['ipv6']) { // data not null
          GetDeviceSwitchRoutingInterfaces200ResponseInnerIpv6.validateJSON(data['ipv6']);
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
          GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfSettings.validateJSON(data['ospfSettings']);
        }
        // validate the optional field `ospfV3`
        if (data['ospfV3']) { // data not null
          GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfV3.validateJSON(data['ospfV3']);
        }
        // ensure the json data is a string
        if (data['subnet'] && !(typeof data['subnet'] === 'string' || data['subnet'] instanceof String)) {
            throw new Error("Expected the field `subnet` to be a primitive type in the JSON string but got " + data['subnet']);
        }

        return true;
    }


}



/**
 * IPv4 default gateway
 * @member {String} defaultGateway
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['defaultGateway'] = undefined;

/**
 * The id
 * @member {String} interfaceId
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['interfaceId'] = undefined;

/**
 * IPv4 address
 * @member {String} interfaceIp
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['interfaceIp'] = undefined;

/**
 * @member {module:model/GetDeviceSwitchRoutingInterfaces200ResponseInnerIpv6} ipv6
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['ipv6'] = undefined;

/**
 * Multicast routing status
 * @member {String} multicastRouting
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['multicastRouting'] = undefined;

/**
 * The name
 * @member {String} name
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['name'] = undefined;

/**
 * @member {module:model/GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfSettings} ospfSettings
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['ospfSettings'] = undefined;

/**
 * @member {module:model/GetDeviceSwitchRoutingInterfaces200ResponseInnerOspfV3} ospfV3
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['ospfV3'] = undefined;

/**
 * IPv4 subnet
 * @member {String} subnet
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['subnet'] = undefined;

/**
 * VLAN id
 * @member {Number} vlanId
 */
GetDeviceSwitchRoutingInterfaces200ResponseInner.prototype['vlanId'] = undefined;






export default GetDeviceSwitchRoutingInterfaces200ResponseInner;

