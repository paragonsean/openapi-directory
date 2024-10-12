/**
 * NBA v3 RotoBaller Premium News
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The News model module.
 * @module model/News
 * @version 1.0
 */
class News {
    /**
     * Constructs a new <code>News</code>.
     * @alias module:model/News
     */
    constructor() { 
        
        News.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>News</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/News} obj Optional instance to populate.
     * @return {module:model/News} The populated <code>News</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new News();

            if (data.hasOwnProperty('Author')) {
                obj['Author'] = ApiClient.convertToType(data['Author'], 'String');
            }
            if (data.hasOwnProperty('Categories')) {
                obj['Categories'] = ApiClient.convertToType(data['Categories'], 'String');
            }
            if (data.hasOwnProperty('Content')) {
                obj['Content'] = ApiClient.convertToType(data['Content'], 'String');
            }
            if (data.hasOwnProperty('NewsID')) {
                obj['NewsID'] = ApiClient.convertToType(data['NewsID'], 'Number');
            }
            if (data.hasOwnProperty('OriginalSource')) {
                obj['OriginalSource'] = ApiClient.convertToType(data['OriginalSource'], 'String');
            }
            if (data.hasOwnProperty('OriginalSourceUrl')) {
                obj['OriginalSourceUrl'] = ApiClient.convertToType(data['OriginalSourceUrl'], 'String');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('PlayerID2')) {
                obj['PlayerID2'] = ApiClient.convertToType(data['PlayerID2'], 'Number');
            }
            if (data.hasOwnProperty('Source')) {
                obj['Source'] = ApiClient.convertToType(data['Source'], 'String');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('Team2')) {
                obj['Team2'] = ApiClient.convertToType(data['Team2'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('TeamID2')) {
                obj['TeamID2'] = ApiClient.convertToType(data['TeamID2'], 'Number');
            }
            if (data.hasOwnProperty('TermsOfUse')) {
                obj['TermsOfUse'] = ApiClient.convertToType(data['TermsOfUse'], 'String');
            }
            if (data.hasOwnProperty('TimeAgo')) {
                obj['TimeAgo'] = ApiClient.convertToType(data['TimeAgo'], 'String');
            }
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('Url')) {
                obj['Url'] = ApiClient.convertToType(data['Url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>News</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>News</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Author'] && !(typeof data['Author'] === 'string' || data['Author'] instanceof String)) {
            throw new Error("Expected the field `Author` to be a primitive type in the JSON string but got " + data['Author']);
        }
        // ensure the json data is a string
        if (data['Categories'] && !(typeof data['Categories'] === 'string' || data['Categories'] instanceof String)) {
            throw new Error("Expected the field `Categories` to be a primitive type in the JSON string but got " + data['Categories']);
        }
        // ensure the json data is a string
        if (data['Content'] && !(typeof data['Content'] === 'string' || data['Content'] instanceof String)) {
            throw new Error("Expected the field `Content` to be a primitive type in the JSON string but got " + data['Content']);
        }
        // ensure the json data is a string
        if (data['OriginalSource'] && !(typeof data['OriginalSource'] === 'string' || data['OriginalSource'] instanceof String)) {
            throw new Error("Expected the field `OriginalSource` to be a primitive type in the JSON string but got " + data['OriginalSource']);
        }
        // ensure the json data is a string
        if (data['OriginalSourceUrl'] && !(typeof data['OriginalSourceUrl'] === 'string' || data['OriginalSourceUrl'] instanceof String)) {
            throw new Error("Expected the field `OriginalSourceUrl` to be a primitive type in the JSON string but got " + data['OriginalSourceUrl']);
        }
        // ensure the json data is a string
        if (data['Source'] && !(typeof data['Source'] === 'string' || data['Source'] instanceof String)) {
            throw new Error("Expected the field `Source` to be a primitive type in the JSON string but got " + data['Source']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['Team2'] && !(typeof data['Team2'] === 'string' || data['Team2'] instanceof String)) {
            throw new Error("Expected the field `Team2` to be a primitive type in the JSON string but got " + data['Team2']);
        }
        // ensure the json data is a string
        if (data['TermsOfUse'] && !(typeof data['TermsOfUse'] === 'string' || data['TermsOfUse'] instanceof String)) {
            throw new Error("Expected the field `TermsOfUse` to be a primitive type in the JSON string but got " + data['TermsOfUse']);
        }
        // ensure the json data is a string
        if (data['TimeAgo'] && !(typeof data['TimeAgo'] === 'string' || data['TimeAgo'] instanceof String)) {
            throw new Error("Expected the field `TimeAgo` to be a primitive type in the JSON string but got " + data['TimeAgo']);
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }
        // ensure the json data is a string
        if (data['Url'] && !(typeof data['Url'] === 'string' || data['Url'] instanceof String)) {
            throw new Error("Expected the field `Url` to be a primitive type in the JSON string but got " + data['Url']);
        }

        return true;
    }


}



/**
 * @member {String} Author
 */
News.prototype['Author'] = undefined;

/**
 * @member {String} Categories
 */
News.prototype['Categories'] = undefined;

/**
 * @member {String} Content
 */
News.prototype['Content'] = undefined;

/**
 * @member {Number} NewsID
 */
News.prototype['NewsID'] = undefined;

/**
 * @member {String} OriginalSource
 */
News.prototype['OriginalSource'] = undefined;

/**
 * @member {String} OriginalSourceUrl
 */
News.prototype['OriginalSourceUrl'] = undefined;

/**
 * @member {Number} PlayerID
 */
News.prototype['PlayerID'] = undefined;

/**
 * @member {Number} PlayerID2
 */
News.prototype['PlayerID2'] = undefined;

/**
 * @member {String} Source
 */
News.prototype['Source'] = undefined;

/**
 * @member {String} Team
 */
News.prototype['Team'] = undefined;

/**
 * @member {String} Team2
 */
News.prototype['Team2'] = undefined;

/**
 * @member {Number} TeamID
 */
News.prototype['TeamID'] = undefined;

/**
 * @member {Number} TeamID2
 */
News.prototype['TeamID2'] = undefined;

/**
 * @member {String} TermsOfUse
 */
News.prototype['TermsOfUse'] = undefined;

/**
 * @member {String} TimeAgo
 */
News.prototype['TimeAgo'] = undefined;

/**
 * @member {String} Title
 */
News.prototype['Title'] = undefined;

/**
 * @member {String} Updated
 */
News.prototype['Updated'] = undefined;

/**
 * @member {String} Url
 */
News.prototype['Url'] = undefined;






export default News;

