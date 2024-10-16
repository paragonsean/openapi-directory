/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SourceRef from './SourceRef';

/**
 * The QueryFilters model module.
 * @module model/QueryFilters
 * @version 2.0
 */
class QueryFilters {
    /**
     * Constructs a new <code>QueryFilters</code>.
     * @alias module:model/QueryFilters
     */
    constructor() { 
        
        QueryFilters.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>QueryFilters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/QueryFilters} obj Optional instance to populate.
     * @return {module:model/QueryFilters} The populated <code>QueryFilters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new QueryFilters();

            if (data.hasOwnProperty('seriesTagIds')) {
                obj['seriesTagIds'] = ApiClient.convertToType(data['seriesTagIds'], ['Number']);
            }
            if (data.hasOwnProperty('seriesTypeIds')) {
                obj['seriesTypeIds'] = ApiClient.convertToType(data['seriesTypeIds'], ['Number']);
            }
            if (data.hasOwnProperty('sourceRefs')) {
                obj['sourceRefs'] = ApiClient.convertToType(data['sourceRefs'], [SourceRef]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>QueryFilters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>QueryFilters</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['seriesTagIds'])) {
            throw new Error("Expected the field `seriesTagIds` to be an array in the JSON data but got " + data['seriesTagIds']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['seriesTypeIds'])) {
            throw new Error("Expected the field `seriesTypeIds` to be an array in the JSON data but got " + data['seriesTypeIds']);
        }
        if (data['sourceRefs']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['sourceRefs'])) {
                throw new Error("Expected the field `sourceRefs` to be an array in the JSON data but got " + data['sourceRefs']);
            }
            // validate the optional field `sourceRefs` (array)
            for (const item of data['sourceRefs']) {
                SourceRef.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<Number>} seriesTagIds
 */
QueryFilters.prototype['seriesTagIds'] = undefined;

/**
 * @member {Array.<Number>} seriesTypeIds
 */
QueryFilters.prototype['seriesTypeIds'] = undefined;

/**
 * @member {Array.<module:model/SourceRef>} sourceRefs
 */
QueryFilters.prototype['sourceRefs'] = undefined;






export default QueryFilters;

