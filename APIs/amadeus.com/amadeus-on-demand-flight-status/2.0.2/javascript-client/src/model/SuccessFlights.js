/**
 * On-Demand Flight Status
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CollectionMeta from './CollectionMeta';
import DatedFlight from './DatedFlight';
import Issue from './Issue';

/**
 * The SuccessFlights model module.
 * @module model/SuccessFlights
 * @version 2.0.2
 */
class SuccessFlights {
    /**
     * Constructs a new <code>SuccessFlights</code>.
     * @alias module:model/SuccessFlights
     * @param data {Array.<module:model/DatedFlight>} 
     */
    constructor(data) { 
        
        SuccessFlights.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>SuccessFlights</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SuccessFlights} obj Optional instance to populate.
     * @return {module:model/SuccessFlights} The populated <code>SuccessFlights</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SuccessFlights();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], [DatedFlight]);
            }
            if (data.hasOwnProperty('meta')) {
                obj['meta'] = CollectionMeta.constructFromObject(data['meta']);
            }
            if (data.hasOwnProperty('warnings')) {
                obj['warnings'] = ApiClient.convertToType(data['warnings'], [Issue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SuccessFlights</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SuccessFlights</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SuccessFlights.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['data'])) {
                throw new Error("Expected the field `data` to be an array in the JSON data but got " + data['data']);
            }
            // validate the optional field `data` (array)
            for (const item of data['data']) {
                DatedFlight.validateJSON(item);
            };
        }
        // validate the optional field `meta`
        if (data['meta']) { // data not null
          CollectionMeta.validateJSON(data['meta']);
        }
        if (data['warnings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['warnings'])) {
                throw new Error("Expected the field `warnings` to be an array in the JSON data but got " + data['warnings']);
            }
            // validate the optional field `warnings` (array)
            for (const item of data['warnings']) {
                Issue.validateJSON(item);
            };
        }

        return true;
    }


}

SuccessFlights.RequiredProperties = ["data"];

/**
 * @member {Array.<module:model/DatedFlight>} data
 */
SuccessFlights.prototype['data'] = undefined;

/**
 * @member {module:model/CollectionMeta} meta
 */
SuccessFlights.prototype['meta'] = undefined;

/**
 * @member {Array.<module:model/Issue>} warnings
 */
SuccessFlights.prototype['warnings'] = undefined;






export default SuccessFlights;

