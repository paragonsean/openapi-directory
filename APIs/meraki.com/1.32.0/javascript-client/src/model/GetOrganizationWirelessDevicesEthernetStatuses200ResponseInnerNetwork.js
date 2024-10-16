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
 * The GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork model module.
 * @module model/GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork
 * @version 1.32.0
 */
class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork {
    /**
     * Constructs a new <code>GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork</code>.
     * Network details object
     * @alias module:model/GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork
     */
    constructor() { 
        
        GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork} obj Optional instance to populate.
     * @return {module:model/GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork} The populated <code>GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * The network ID the AP is associated to
 * @member {String} id
 */
GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork.prototype['id'] = undefined;






export default GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerNetwork;

