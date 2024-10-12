/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TagPerformance from './TagPerformance';

/**
 * The IterationPerformance model module.
 * @module model/IterationPerformance
 * @version 3.2
 */
class IterationPerformance {
    /**
     * Constructs a new <code>IterationPerformance</code>.
     * Represents the detailed performance data for a trained iteration.
     * @alias module:model/IterationPerformance
     */
    constructor() { 
        
        IterationPerformance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IterationPerformance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IterationPerformance} obj Optional instance to populate.
     * @return {module:model/IterationPerformance} The populated <code>IterationPerformance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IterationPerformance();

            if (data.hasOwnProperty('averagePrecision')) {
                obj['averagePrecision'] = ApiClient.convertToType(data['averagePrecision'], 'Number');
            }
            if (data.hasOwnProperty('perTagPerformance')) {
                obj['perTagPerformance'] = ApiClient.convertToType(data['perTagPerformance'], [TagPerformance]);
            }
            if (data.hasOwnProperty('precision')) {
                obj['precision'] = ApiClient.convertToType(data['precision'], 'Number');
            }
            if (data.hasOwnProperty('precisionStdDeviation')) {
                obj['precisionStdDeviation'] = ApiClient.convertToType(data['precisionStdDeviation'], 'Number');
            }
            if (data.hasOwnProperty('recall')) {
                obj['recall'] = ApiClient.convertToType(data['recall'], 'Number');
            }
            if (data.hasOwnProperty('recallStdDeviation')) {
                obj['recallStdDeviation'] = ApiClient.convertToType(data['recallStdDeviation'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IterationPerformance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IterationPerformance</code>.
     */
    static validateJSON(data) {
        if (data['perTagPerformance']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['perTagPerformance'])) {
                throw new Error("Expected the field `perTagPerformance` to be an array in the JSON data but got " + data['perTagPerformance']);
            }
            // validate the optional field `perTagPerformance` (array)
            for (const item of data['perTagPerformance']) {
                TagPerformance.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Gets the average precision when applicable.
 * @member {Number} averagePrecision
 */
IterationPerformance.prototype['averagePrecision'] = undefined;

/**
 * Gets the per-tag performance details for this iteration.
 * @member {Array.<module:model/TagPerformance>} perTagPerformance
 */
IterationPerformance.prototype['perTagPerformance'] = undefined;

/**
 * Gets the precision.
 * @member {Number} precision
 */
IterationPerformance.prototype['precision'] = undefined;

/**
 * Gets the standard deviation for the precision.
 * @member {Number} precisionStdDeviation
 */
IterationPerformance.prototype['precisionStdDeviation'] = undefined;

/**
 * Gets the recall.
 * @member {Number} recall
 */
IterationPerformance.prototype['recall'] = undefined;

/**
 * Gets the standard deviation for the recall.
 * @member {Number} recallStdDeviation
 */
IterationPerformance.prototype['recallStdDeviation'] = undefined;






export default IterationPerformance;

