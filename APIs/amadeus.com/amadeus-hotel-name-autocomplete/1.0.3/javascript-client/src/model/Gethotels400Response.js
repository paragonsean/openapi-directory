/**
 * Hotel Name Autocomplete
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Gethotels400ResponseErrorsInner from './Gethotels400ResponseErrorsInner';

/**
 * The Gethotels400Response model module.
 * @module model/Gethotels400Response
 * @version 1.0.3
 */
class Gethotels400Response {
    /**
     * Constructs a new <code>Gethotels400Response</code>.
     * @alias module:model/Gethotels400Response
     * @param errors {Array.<module:model/Gethotels400ResponseErrorsInner>} 
     */
    constructor(errors) { 
        
        Gethotels400Response.initialize(this, errors);
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
     * Constructs a <code>Gethotels400Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Gethotels400Response} obj Optional instance to populate.
     * @return {module:model/Gethotels400Response} The populated <code>Gethotels400Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Gethotels400Response();

            if (data.hasOwnProperty('errors')) {
                obj['errors'] = ApiClient.convertToType(data['errors'], [Gethotels400ResponseErrorsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Gethotels400Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Gethotels400Response</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Gethotels400Response.RequiredProperties) {
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
                Gethotels400ResponseErrorsInner.validateJSON(item);
            };
        }

        return true;
    }


}

Gethotels400Response.RequiredProperties = ["errors"];

/**
 * @member {Array.<module:model/Gethotels400ResponseErrorsInner>} errors
 */
Gethotels400Response.prototype['errors'] = undefined;






export default Gethotels400Response;

