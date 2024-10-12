/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PropertyFacilityModel from './PropertyFacilityModel';

/**
 * The PropertyFacilityModelResults model module.
 * @module model/PropertyFacilityModelResults
 * @version v2-basic-tier
 */
class PropertyFacilityModelResults {
    /**
     * Constructs a new <code>PropertyFacilityModelResults</code>.
     * Holds results from a paged query returning PropertyFacilityModel values
     * @alias module:model/PropertyFacilityModelResults
     */
    constructor() { 
        
        PropertyFacilityModelResults.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PropertyFacilityModelResults</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PropertyFacilityModelResults} obj Optional instance to populate.
     * @return {module:model/PropertyFacilityModelResults} The populated <code>PropertyFacilityModelResults</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PropertyFacilityModelResults();

            if (data.hasOwnProperty('Count')) {
                obj['Count'] = ApiClient.convertToType(data['Count'], 'Number');
            }
            if (data.hasOwnProperty('Data')) {
                obj['Data'] = ApiClient.convertToType(data['Data'], [PropertyFacilityModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PropertyFacilityModelResults</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PropertyFacilityModelResults</code>.
     */
    static validateJSON(data) {
        if (data['Data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Data'])) {
                throw new Error("Expected the field `Data` to be an array in the JSON data but got " + data['Data']);
            }
            // validate the optional field `Data` (array)
            for (const item of data['Data']) {
                PropertyFacilityModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The total number of results available for all pages
 * @member {Number} Count
 */
PropertyFacilityModelResults.prototype['Count'] = undefined;

/**
 * The resulting data returned from the paged query range
 * @member {Array.<module:model/PropertyFacilityModel>} Data
 */
PropertyFacilityModelResults.prototype['Data'] = undefined;






export default PropertyFacilityModelResults;

