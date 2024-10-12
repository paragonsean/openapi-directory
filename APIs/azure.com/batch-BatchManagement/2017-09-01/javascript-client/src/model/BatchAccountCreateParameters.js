/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BatchAccountCreateProperties from './BatchAccountCreateProperties';

/**
 * The BatchAccountCreateParameters model module.
 * @module model/BatchAccountCreateParameters
 * @version 2017-09-01
 */
class BatchAccountCreateParameters {
    /**
     * Constructs a new <code>BatchAccountCreateParameters</code>.
     * Parameters supplied to the Create operation.
     * @alias module:model/BatchAccountCreateParameters
     * @param location {String} The region in which to create the account.
     */
    constructor(location) { 
        
        BatchAccountCreateParameters.initialize(this, location);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, location) { 
        obj['location'] = location;
    }

    /**
     * Constructs a <code>BatchAccountCreateParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BatchAccountCreateParameters} obj Optional instance to populate.
     * @return {module:model/BatchAccountCreateParameters} The populated <code>BatchAccountCreateParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BatchAccountCreateParameters();

            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = BatchAccountCreateProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BatchAccountCreateParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BatchAccountCreateParameters</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BatchAccountCreateParameters.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          BatchAccountCreateProperties.validateJSON(data['properties']);
        }

        return true;
    }


}

BatchAccountCreateParameters.RequiredProperties = ["location"];

/**
 * The region in which to create the account.
 * @member {String} location
 */
BatchAccountCreateParameters.prototype['location'] = undefined;

/**
 * @member {module:model/BatchAccountCreateProperties} properties
 */
BatchAccountCreateParameters.prototype['properties'] = undefined;

/**
 * The user-specified tags associated with the account.
 * @member {Object.<String, String>} tags
 */
BatchAccountCreateParameters.prototype['tags'] = undefined;






export default BatchAccountCreateParameters;

