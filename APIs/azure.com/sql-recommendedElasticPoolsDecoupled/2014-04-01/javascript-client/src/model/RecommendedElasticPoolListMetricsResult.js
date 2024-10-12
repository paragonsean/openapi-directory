/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RecommendedElasticPoolMetric from './RecommendedElasticPoolMetric';

/**
 * The RecommendedElasticPoolListMetricsResult model module.
 * @module model/RecommendedElasticPoolListMetricsResult
 * @version 2014-04-01
 */
class RecommendedElasticPoolListMetricsResult {
    /**
     * Constructs a new <code>RecommendedElasticPoolListMetricsResult</code>.
     * Represents the response to a list recommended elastic pool metrics request.
     * @alias module:model/RecommendedElasticPoolListMetricsResult
     * @param value {Array.<module:model/RecommendedElasticPoolMetric>} The list of recommended elastic pools metrics.
     */
    constructor(value) { 
        
        RecommendedElasticPoolListMetricsResult.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>RecommendedElasticPoolListMetricsResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RecommendedElasticPoolListMetricsResult} obj Optional instance to populate.
     * @return {module:model/RecommendedElasticPoolListMetricsResult} The populated <code>RecommendedElasticPoolListMetricsResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RecommendedElasticPoolListMetricsResult();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [RecommendedElasticPoolMetric]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RecommendedElasticPoolListMetricsResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RecommendedElasticPoolListMetricsResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RecommendedElasticPoolListMetricsResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                RecommendedElasticPoolMetric.validateJSON(item);
            };
        }

        return true;
    }


}

RecommendedElasticPoolListMetricsResult.RequiredProperties = ["value"];

/**
 * The list of recommended elastic pools metrics.
 * @member {Array.<module:model/RecommendedElasticPoolMetric>} value
 */
RecommendedElasticPoolListMetricsResult.prototype['value'] = undefined;






export default RecommendedElasticPoolListMetricsResult;

