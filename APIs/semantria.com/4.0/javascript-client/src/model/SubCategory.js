/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SubCategory model module.
 * @module model/SubCategory
 * @version 4.0
 */
class SubCategory {
    /**
     * Constructs a new <code>SubCategory</code>.
     * @alias module:model/SubCategory
     * @param strengthScore {Number} Strength of the category matches with the document content
     * @param title {String} The category title, which is its label in the text
     * @param type {String} Type of category; can be either \"node\" (root level) or \"leaf\" (nested) value
     */
    constructor(strengthScore, title, type) { 
        
        SubCategory.initialize(this, strengthScore, title, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, strengthScore, title, type) { 
        obj['strength_score'] = strengthScore;
        obj['title'] = title;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>SubCategory</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SubCategory} obj Optional instance to populate.
     * @return {module:model/SubCategory} The populated <code>SubCategory</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubCategory();

            if (data.hasOwnProperty('strength_score')) {
                obj['strength_score'] = ApiClient.convertToType(data['strength_score'], 'Number');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SubCategory</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SubCategory</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SubCategory.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

SubCategory.RequiredProperties = ["strength_score", "title", "type"];

/**
 * Strength of the category matches with the document content
 * @member {Number} strength_score
 */
SubCategory.prototype['strength_score'] = undefined;

/**
 * The category title, which is its label in the text
 * @member {String} title
 */
SubCategory.prototype['title'] = undefined;

/**
 * Type of category; can be either \"node\" (root level) or \"leaf\" (nested) value
 * @member {String} type
 */
SubCategory.prototype['type'] = undefined;






export default SubCategory;

