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
import UpdateTrustedIdProviderProperties from './UpdateTrustedIdProviderProperties';

/**
 * The UpdateTrustedIdProviderWithAccountParameters model module.
 * @module model/UpdateTrustedIdProviderWithAccountParameters
 * @version 2016-11-01
 */
class UpdateTrustedIdProviderWithAccountParameters {
    /**
     * Constructs a new <code>UpdateTrustedIdProviderWithAccountParameters</code>.
     * The parameters used to update a trusted identity provider while updating a Data Lake Store account.
     * @alias module:model/UpdateTrustedIdProviderWithAccountParameters
     * @param name {String} The unique name of the trusted identity provider to update.
     */
    constructor(name) { 
        
        UpdateTrustedIdProviderWithAccountParameters.initialize(this, name);
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
     * Constructs a <code>UpdateTrustedIdProviderWithAccountParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateTrustedIdProviderWithAccountParameters} obj Optional instance to populate.
     * @return {module:model/UpdateTrustedIdProviderWithAccountParameters} The populated <code>UpdateTrustedIdProviderWithAccountParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateTrustedIdProviderWithAccountParameters();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = UpdateTrustedIdProviderProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateTrustedIdProviderWithAccountParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateTrustedIdProviderWithAccountParameters</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateTrustedIdProviderWithAccountParameters.RequiredProperties) {
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
          UpdateTrustedIdProviderProperties.validateJSON(data['properties']);
        }

        return true;
    }


}

UpdateTrustedIdProviderWithAccountParameters.RequiredProperties = ["name"];

/**
 * The unique name of the trusted identity provider to update.
 * @member {String} name
 */
UpdateTrustedIdProviderWithAccountParameters.prototype['name'] = undefined;

/**
 * @member {module:model/UpdateTrustedIdProviderProperties} properties
 */
UpdateTrustedIdProviderWithAccountParameters.prototype['properties'] = undefined;






export default UpdateTrustedIdProviderWithAccountParameters;

