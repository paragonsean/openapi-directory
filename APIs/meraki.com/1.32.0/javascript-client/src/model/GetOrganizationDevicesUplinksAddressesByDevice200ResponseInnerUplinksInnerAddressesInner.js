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
import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic from './GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic';

/**
 * The GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner model module.
 * @module model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner
 * @version 1.32.0
 */
class GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner {
    /**
     * Constructs a new <code>GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner</code>.
     * @alias module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner
     */
    constructor() { 
        
        GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner} obj Optional instance to populate.
     * @return {module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner} The populated <code>GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('assignmentMode')) {
                obj['assignmentMode'] = ApiClient.convertToType(data['assignmentMode'], 'String');
            }
            if (data.hasOwnProperty('gateway')) {
                obj['gateway'] = ApiClient.convertToType(data['gateway'], 'String');
            }
            if (data.hasOwnProperty('protocol')) {
                obj['protocol'] = ApiClient.convertToType(data['protocol'], 'String');
            }
            if (data.hasOwnProperty('public')) {
                obj['public'] = GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic.constructFromObject(data['public']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }
        // ensure the json data is a string
        if (data['assignmentMode'] && !(typeof data['assignmentMode'] === 'string' || data['assignmentMode'] instanceof String)) {
            throw new Error("Expected the field `assignmentMode` to be a primitive type in the JSON string but got " + data['assignmentMode']);
        }
        // ensure the json data is a string
        if (data['gateway'] && !(typeof data['gateway'] === 'string' || data['gateway'] instanceof String)) {
            throw new Error("Expected the field `gateway` to be a primitive type in the JSON string but got " + data['gateway']);
        }
        // ensure the json data is a string
        if (data['protocol'] && !(typeof data['protocol'] === 'string' || data['protocol'] instanceof String)) {
            throw new Error("Expected the field `protocol` to be a primitive type in the JSON string but got " + data['protocol']);
        }
        // validate the optional field `public`
        if (data['public']) { // data not null
          GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic.validateJSON(data['public']);
        }

        return true;
    }


}



/**
 * Device uplink address.
 * @member {String} address
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.prototype['address'] = undefined;

/**
 * Indicates how the device uplink address is assigned. Available options are: static, dynamic.
 * @member {module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.AssignmentModeEnum} assignmentMode
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.prototype['assignmentMode'] = undefined;

/**
 * Device uplink gateway address.
 * @member {String} gateway
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.prototype['gateway'] = undefined;

/**
 * Type of address for the device uplink. Available options are: ipv4, ipv6.
 * @member {module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.ProtocolEnum} protocol
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.prototype['protocol'] = undefined;

/**
 * @member {module:model/GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic} public
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner.prototype['public'] = undefined;





/**
 * Allowed values for the <code>assignmentMode</code> property.
 * @enum {String}
 * @readonly
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner['AssignmentModeEnum'] = {

    /**
     * value: "dynamic"
     * @const
     */
    "dynamic": "dynamic",

    /**
     * value: "static"
     * @const
     */
    "static": "static"
};


/**
 * Allowed values for the <code>protocol</code> property.
 * @enum {String}
 * @readonly
 */
GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner['ProtocolEnum'] = {

    /**
     * value: "ipv4"
     * @const
     */
    "ipv4": "ipv4",

    /**
     * value: "ipv6"
     * @const
     */
    "ipv6": "ipv6"
};



export default GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner;

