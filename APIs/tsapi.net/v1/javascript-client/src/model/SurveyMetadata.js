/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Hierarchy from './Hierarchy';
import Language from './Language';
import Variable from './Variable';

/**
 * The SurveyMetadata model module.
 * @module model/SurveyMetadata
 * @version v1
 */
class SurveyMetadata {
    /**
     * Constructs a new <code>SurveyMetadata</code>.
     * @alias module:model/SurveyMetadata
     */
    constructor() { 
        
        SurveyMetadata.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SurveyMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SurveyMetadata} obj Optional instance to populate.
     * @return {module:model/SurveyMetadata} The populated <code>SurveyMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SurveyMetadata();

            if (data.hasOwnProperty('hierarchies')) {
                obj['hierarchies'] = ApiClient.convertToType(data['hierarchies'], [Hierarchy]);
            }
            if (data.hasOwnProperty('interviewCount')) {
                obj['interviewCount'] = ApiClient.convertToType(data['interviewCount'], 'Number');
            }
            if (data.hasOwnProperty('languages')) {
                obj['languages'] = ApiClient.convertToType(data['languages'], [Language]);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('variables')) {
                obj['variables'] = ApiClient.convertToType(data['variables'], [Variable]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SurveyMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SurveyMetadata</code>.
     */
    static validateJSON(data) {
        if (data['hierarchies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['hierarchies'])) {
                throw new Error("Expected the field `hierarchies` to be an array in the JSON data but got " + data['hierarchies']);
            }
            // validate the optional field `hierarchies` (array)
            for (const item of data['hierarchies']) {
                Hierarchy.validateJSON(item);
            };
        }
        if (data['languages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['languages'])) {
                throw new Error("Expected the field `languages` to be an array in the JSON data but got " + data['languages']);
            }
            // validate the optional field `languages` (array)
            for (const item of data['languages']) {
                Language.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        if (data['variables']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['variables'])) {
                throw new Error("Expected the field `variables` to be an array in the JSON data but got " + data['variables']);
            }
            // validate the optional field `variables` (array)
            for (const item of data['variables']) {
                Variable.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Hierarchy>} hierarchies
 */
SurveyMetadata.prototype['hierarchies'] = undefined;

/**
 * @member {Number} interviewCount
 */
SurveyMetadata.prototype['interviewCount'] = undefined;

/**
 * @member {Array.<module:model/Language>} languages
 */
SurveyMetadata.prototype['languages'] = undefined;

/**
 * @member {String} name
 */
SurveyMetadata.prototype['name'] = undefined;

/**
 * @member {String} title
 */
SurveyMetadata.prototype['title'] = undefined;

/**
 * @member {Array.<module:model/Variable>} variables
 */
SurveyMetadata.prototype['variables'] = undefined;






export default SurveyMetadata;

