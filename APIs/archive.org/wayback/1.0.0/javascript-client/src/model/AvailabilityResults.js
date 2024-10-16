/**
 * Wayback API
 * API for Internet Archive's Wayback Machine
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ArchivedResult from './ArchivedResult';

/**
 * The AvailabilityResults model module.
 * @module model/AvailabilityResults
 * @version 1.0.0
 */
class AvailabilityResults {
    /**
     * Constructs a new <code>AvailabilityResults</code>.
     * @alias module:model/AvailabilityResults
     * @param results {Array.<module:model/ArchivedResult>} A list of results
     */
    constructor(results) { 
        
        AvailabilityResults.initialize(this, results);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, results) { 
        obj['results'] = results;
    }

    /**
     * Constructs a <code>AvailabilityResults</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailabilityResults} obj Optional instance to populate.
     * @return {module:model/AvailabilityResults} The populated <code>AvailabilityResults</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailabilityResults();

            if (data.hasOwnProperty('results')) {
                obj['results'] = ApiClient.convertToType(data['results'], [ArchivedResult]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailabilityResults</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailabilityResults</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvailabilityResults.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['results'])) {
                throw new Error("Expected the field `results` to be an array in the JSON data but got " + data['results']);
            }
            // validate the optional field `results` (array)
            for (const item of data['results']) {
                ArchivedResult.validateJSON(item);
            };
        }

        return true;
    }


}

AvailabilityResults.RequiredProperties = ["results"];

/**
 * A list of results
 * @member {Array.<module:model/ArchivedResult>} results
 */
AvailabilityResults.prototype['results'] = undefined;






export default AvailabilityResults;

