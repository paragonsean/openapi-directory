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
 * The CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner model module.
 * @module model/CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner
 * @version 1.32.0
 */
class CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner {
    /**
     * Constructs a new <code>CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner</code>.
     * @alias module:model/CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner
     * @param portId {String} Port identifier of switch port. For modules, the identifier is \"SlotNumber_ModuleType_PortNumber\" (Ex: \"1_8X10G_1\"), otherwise it is just the port number (Ex: \"8\").
     * @param profile {String} Profile identifier.
     */
    constructor(portId, profile) { 
        
        CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner.initialize(this, portId, profile);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, portId, profile) { 
        obj['portId'] = portId;
        obj['profile'] = profile;
    }

    /**
     * Constructs a <code>CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner} obj Optional instance to populate.
     * @return {module:model/CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner} The populated <code>CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner();

            if (data.hasOwnProperty('portId')) {
                obj['portId'] = ApiClient.convertToType(data['portId'], 'String');
            }
            if (data.hasOwnProperty('profile')) {
                obj['profile'] = ApiClient.convertToType(data['profile'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['portId'] && !(typeof data['portId'] === 'string' || data['portId'] instanceof String)) {
            throw new Error("Expected the field `portId` to be a primitive type in the JSON string but got " + data['portId']);
        }
        // ensure the json data is a string
        if (data['profile'] && !(typeof data['profile'] === 'string' || data['profile'] instanceof String)) {
            throw new Error("Expected the field `profile` to be a primitive type in the JSON string but got " + data['profile']);
        }

        return true;
    }


}

CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner.RequiredProperties = ["portId", "profile"];

/**
 * Port identifier of switch port. For modules, the identifier is \"SlotNumber_ModuleType_PortNumber\" (Ex: \"1_8X10G_1\"), otherwise it is just the port number (Ex: \"8\").
 * @member {String} portId
 */
CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner.prototype['portId'] = undefined;

/**
 * Profile identifier.
 * @member {String} profile
 */
CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner.prototype['profile'] = undefined;






export default CreateNetworkSwitchLinkAggregationRequestSwitchProfilePortsInner;

