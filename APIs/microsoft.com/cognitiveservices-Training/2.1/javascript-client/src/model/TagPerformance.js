/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TagPerformance model module.
 * @module model/TagPerformance
 * @version 2.1
 */
class TagPerformance {
    /**
     * Constructs a new <code>TagPerformance</code>.
     * Represents performance data for a particular tag in a trained iteration
     * @alias module:model/TagPerformance
     */
    constructor() { 
        
        TagPerformance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TagPerformance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TagPerformance} obj Optional instance to populate.
     * @return {module:model/TagPerformance} The populated <code>TagPerformance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TagPerformance();

            if (data.hasOwnProperty('averagePrecision')) {
                obj['averagePrecision'] = ApiClient.convertToType(data['averagePrecision'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
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
     * Validates the JSON data with respect to <code>TagPerformance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TagPerformance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * Gets the average precision when applicable
 * @member {Number} averagePrecision
 */
TagPerformance.prototype['averagePrecision'] = undefined;

/**
 * @member {String} id
 */
TagPerformance.prototype['id'] = undefined;

/**
 * @member {String} name
 */
TagPerformance.prototype['name'] = undefined;

/**
 * Gets the precision
 * @member {Number} precision
 */
TagPerformance.prototype['precision'] = undefined;

/**
 * Gets the standard deviation for the precision
 * @member {Number} precisionStdDeviation
 */
TagPerformance.prototype['precisionStdDeviation'] = undefined;

/**
 * Gets the recall
 * @member {Number} recall
 */
TagPerformance.prototype['recall'] = undefined;

/**
 * Gets the standard deviation for the recall
 * @member {Number} recallStdDeviation
 */
TagPerformance.prototype['recallStdDeviation'] = undefined;






export default TagPerformance;

