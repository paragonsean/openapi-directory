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
 * The CreateDeviceSwitchRoutingInterfaceRequestOspfSettings model module.
 * @module model/CreateDeviceSwitchRoutingInterfaceRequestOspfSettings
 * @version 1.32.0
 */
class CreateDeviceSwitchRoutingInterfaceRequestOspfSettings {
    /**
     * Constructs a new <code>CreateDeviceSwitchRoutingInterfaceRequestOspfSettings</code>.
     * The OSPF routing settings of the interface.
     * @alias module:model/CreateDeviceSwitchRoutingInterfaceRequestOspfSettings
     */
    constructor() { 
        
        CreateDeviceSwitchRoutingInterfaceRequestOspfSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateDeviceSwitchRoutingInterfaceRequestOspfSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateDeviceSwitchRoutingInterfaceRequestOspfSettings} obj Optional instance to populate.
     * @return {module:model/CreateDeviceSwitchRoutingInterfaceRequestOspfSettings} The populated <code>CreateDeviceSwitchRoutingInterfaceRequestOspfSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateDeviceSwitchRoutingInterfaceRequestOspfSettings();

            if (data.hasOwnProperty('area')) {
                obj['area'] = ApiClient.convertToType(data['area'], 'String');
            }
            if (data.hasOwnProperty('cost')) {
                obj['cost'] = ApiClient.convertToType(data['cost'], 'Number');
            }
            if (data.hasOwnProperty('isPassiveEnabled')) {
                obj['isPassiveEnabled'] = ApiClient.convertToType(data['isPassiveEnabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateDeviceSwitchRoutingInterfaceRequestOspfSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateDeviceSwitchRoutingInterfaceRequestOspfSettings</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['area'] && !(typeof data['area'] === 'string' || data['area'] instanceof String)) {
            throw new Error("Expected the field `area` to be a primitive type in the JSON string but got " + data['area']);
        }

        return true;
    }


}



/**
 * The OSPF area to which this interface should belong. Can be either 'disabled' or the identifier of an           existing OSPF area. Defaults to 'disabled'.
 * @member {String} area
 */
CreateDeviceSwitchRoutingInterfaceRequestOspfSettings.prototype['area'] = undefined;

/**
 * The path cost for this interface. Defaults to 1, but can be increased up to 65535           to give lower priority.
 * @member {Number} cost
 */
CreateDeviceSwitchRoutingInterfaceRequestOspfSettings.prototype['cost'] = undefined;

/**
 * When enabled, OSPF will not run on the interface, but the subnet will still be advertised.
 * @member {Boolean} isPassiveEnabled
 */
CreateDeviceSwitchRoutingInterfaceRequestOspfSettings.prototype['isPassiveEnabled'] = undefined;






export default CreateDeviceSwitchRoutingInterfaceRequestOspfSettings;

