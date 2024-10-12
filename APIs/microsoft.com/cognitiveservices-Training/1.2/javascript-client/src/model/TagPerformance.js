/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
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
 * @version 1.2
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

            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Precision')) {
                obj['Precision'] = ApiClient.convertToType(data['Precision'], 'Number');
            }
            if (data.hasOwnProperty('PrecisionStdDeviation')) {
                obj['PrecisionStdDeviation'] = ApiClient.convertToType(data['PrecisionStdDeviation'], 'Number');
            }
            if (data.hasOwnProperty('Recall')) {
                obj['Recall'] = ApiClient.convertToType(data['Recall'], 'Number');
            }
            if (data.hasOwnProperty('RecallStdDeviation')) {
                obj['RecallStdDeviation'] = ApiClient.convertToType(data['RecallStdDeviation'], 'Number');
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
        if (data['Id'] && !(typeof data['Id'] === 'string' || data['Id'] instanceof String)) {
            throw new Error("Expected the field `Id` to be a primitive type in the JSON string but got " + data['Id']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }

        return true;
    }


}



/**
 * @member {String} Id
 */
TagPerformance.prototype['Id'] = undefined;

/**
 * @member {String} Name
 */
TagPerformance.prototype['Name'] = undefined;

/**
 * Gets the precision
 * @member {Number} Precision
 */
TagPerformance.prototype['Precision'] = undefined;

/**
 * Gets the standard deviation for the precision
 * @member {Number} PrecisionStdDeviation
 */
TagPerformance.prototype['PrecisionStdDeviation'] = undefined;

/**
 * Gets the recall
 * @member {Number} Recall
 */
TagPerformance.prototype['Recall'] = undefined;

/**
 * Gets the standard deviation for the recall
 * @member {Number} RecallStdDeviation
 */
TagPerformance.prototype['RecallStdDeviation'] = undefined;






export default TagPerformance;

