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
 * The CreateNetworkSwitchStackRequest model module.
 * @module model/CreateNetworkSwitchStackRequest
 * @version 1.32.0
 */
class CreateNetworkSwitchStackRequest {
    /**
     * Constructs a new <code>CreateNetworkSwitchStackRequest</code>.
     * @alias module:model/CreateNetworkSwitchStackRequest
     * @param name {String} The name of the new stack
     * @param serials {Array.<String>} An array of switch serials to be added into the new stack
     */
    constructor(name, serials) { 
        
        CreateNetworkSwitchStackRequest.initialize(this, name, serials);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, serials) { 
        obj['name'] = name;
        obj['serials'] = serials;
    }

    /**
     * Constructs a <code>CreateNetworkSwitchStackRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkSwitchStackRequest} obj Optional instance to populate.
     * @return {module:model/CreateNetworkSwitchStackRequest} The populated <code>CreateNetworkSwitchStackRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkSwitchStackRequest();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('serials')) {
                obj['serials'] = ApiClient.convertToType(data['serials'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkSwitchStackRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkSwitchStackRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkSwitchStackRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['serials'])) {
            throw new Error("Expected the field `serials` to be an array in the JSON data but got " + data['serials']);
        }

        return true;
    }


}

CreateNetworkSwitchStackRequest.RequiredProperties = ["name", "serials"];

/**
 * The name of the new stack
 * @member {String} name
 */
CreateNetworkSwitchStackRequest.prototype['name'] = undefined;

/**
 * An array of switch serials to be added into the new stack
 * @member {Array.<String>} serials
 */
CreateNetworkSwitchStackRequest.prototype['serials'] = undefined;






export default CreateNetworkSwitchStackRequest;

