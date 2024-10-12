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
import UpdateVirtualNetworkRuleProperties from './UpdateVirtualNetworkRuleProperties';

/**
 * The UpdateVirtualNetworkRuleWithAccountParameters model module.
 * @module model/UpdateVirtualNetworkRuleWithAccountParameters
 * @version 2016-11-01
 */
class UpdateVirtualNetworkRuleWithAccountParameters {
    /**
     * Constructs a new <code>UpdateVirtualNetworkRuleWithAccountParameters</code>.
     * The parameters used to update a virtual network rule while updating a Data Lake Store account.
     * @alias module:model/UpdateVirtualNetworkRuleWithAccountParameters
     * @param name {String} The unique name of the virtual network rule to update.
     */
    constructor(name) { 
        
        UpdateVirtualNetworkRuleWithAccountParameters.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>UpdateVirtualNetworkRuleWithAccountParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateVirtualNetworkRuleWithAccountParameters} obj Optional instance to populate.
     * @return {module:model/UpdateVirtualNetworkRuleWithAccountParameters} The populated <code>UpdateVirtualNetworkRuleWithAccountParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateVirtualNetworkRuleWithAccountParameters();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = UpdateVirtualNetworkRuleProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateVirtualNetworkRuleWithAccountParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateVirtualNetworkRuleWithAccountParameters</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateVirtualNetworkRuleWithAccountParameters.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          UpdateVirtualNetworkRuleProperties.validateJSON(data['properties']);
        }

        return true;
    }


}

UpdateVirtualNetworkRuleWithAccountParameters.RequiredProperties = ["name"];

/**
 * The unique name of the virtual network rule to update.
 * @member {String} name
 */
UpdateVirtualNetworkRuleWithAccountParameters.prototype['name'] = undefined;

/**
 * @member {module:model/UpdateVirtualNetworkRuleProperties} properties
 */
UpdateVirtualNetworkRuleWithAccountParameters.prototype['properties'] = undefined;






export default UpdateVirtualNetworkRuleWithAccountParameters;

