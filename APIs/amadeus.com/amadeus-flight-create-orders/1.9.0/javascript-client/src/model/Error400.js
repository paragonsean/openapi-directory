/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Issue from './Issue';

/**
 * The Error400 model module.
 * @module model/Error400
 * @version 1.9.0
 */
class Error400 {
    /**
     * Constructs a new <code>Error400</code>.
     * @alias module:model/Error400
     * @param errors {Array.<module:model/Issue>} 
     */
    constructor(errors) { 
        
        Error400.initialize(this, errors);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, errors) { 
        obj['errors'] = errors;
    }

    /**
     * Constructs a <code>Error400</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Error400} obj Optional instance to populate.
     * @return {module:model/Error400} The populated <code>Error400</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Error400();

            if (data.hasOwnProperty('errors')) {
                obj['errors'] = ApiClient.convertToType(data['errors'], [Issue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Error400</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Error400</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Error400.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['errors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['errors'])) {
                throw new Error("Expected the field `errors` to be an array in the JSON data but got " + data['errors']);
            }
            // validate the optional field `errors` (array)
            for (const item of data['errors']) {
                Issue.validateJSON(item);
            };
        }

        return true;
    }


}

Error400.RequiredProperties = ["errors"];

/**
 * @member {Array.<module:model/Issue>} errors
 */
Error400.prototype['errors'] = undefined;






export default Error400;

