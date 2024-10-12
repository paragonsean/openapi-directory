/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SubResource from './SubResource';
import VirtualNetworkRuleProperties from './VirtualNetworkRuleProperties';

/**
 * The VirtualNetworkRule model module.
 * @module model/VirtualNetworkRule
 * @version 2016-11-01
 */
class VirtualNetworkRule {
    /**
     * Constructs a new <code>VirtualNetworkRule</code>.
     * Data Lake Store virtual network rule information.
     * @alias module:model/VirtualNetworkRule
     * @implements module:model/SubResource
     */
    constructor() { 
        SubResource.initialize(this);
        VirtualNetworkRule.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VirtualNetworkRule</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VirtualNetworkRule} obj Optional instance to populate.
     * @return {module:model/VirtualNetworkRule} The populated <code>VirtualNetworkRule</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VirtualNetworkRule();
            SubResource.constructFromObject(data, obj);

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = VirtualNetworkRuleProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VirtualNetworkRule</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VirtualNetworkRule</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          VirtualNetworkRuleProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/VirtualNetworkRuleProperties} properties
 */
VirtualNetworkRule.prototype['properties'] = undefined;

/**
 * The resource identifier.
 * @member {String} id
 */
VirtualNetworkRule.prototype['id'] = undefined;

/**
 * The resource name.
 * @member {String} name
 */
VirtualNetworkRule.prototype['name'] = undefined;

/**
 * The resource type.
 * @member {String} type
 */
VirtualNetworkRule.prototype['type'] = undefined;


// Implement SubResource interface:
/**
 * The resource identifier.
 * @member {String} id
 */
SubResource.prototype['id'] = undefined;
/**
 * The resource name.
 * @member {String} name
 */
SubResource.prototype['name'] = undefined;
/**
 * The resource type.
 * @member {String} type
 */
SubResource.prototype['type'] = undefined;




export default VirtualNetworkRule;

