/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PredictionQueryTag from './PredictionQueryTag';

/**
 * The PredictionQueryToken model module.
 * @module model/PredictionQueryToken
 * @version 3.1
 */
class PredictionQueryToken {
    /**
     * Constructs a new <code>PredictionQueryToken</code>.
     * @alias module:model/PredictionQueryToken
     */
    constructor() { 
        
        PredictionQueryToken.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PredictionQueryToken</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PredictionQueryToken} obj Optional instance to populate.
     * @return {module:model/PredictionQueryToken} The populated <code>PredictionQueryToken</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PredictionQueryToken();

            if (data.hasOwnProperty('application')) {
                obj['application'] = ApiClient.convertToType(data['application'], 'String');
            }
            if (data.hasOwnProperty('continuation')) {
                obj['continuation'] = ApiClient.convertToType(data['continuation'], 'String');
            }
            if (data.hasOwnProperty('endTime')) {
                obj['endTime'] = ApiClient.convertToType(data['endTime'], 'Date');
            }
            if (data.hasOwnProperty('iterationId')) {
                obj['iterationId'] = ApiClient.convertToType(data['iterationId'], 'String');
            }
            if (data.hasOwnProperty('maxCount')) {
                obj['maxCount'] = ApiClient.convertToType(data['maxCount'], 'Number');
            }
            if (data.hasOwnProperty('orderBy')) {
                obj['orderBy'] = ApiClient.convertToType(data['orderBy'], 'String');
            }
            if (data.hasOwnProperty('session')) {
                obj['session'] = ApiClient.convertToType(data['session'], 'String');
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Date');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], [PredictionQueryTag]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PredictionQueryToken</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PredictionQueryToken</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['application'] && !(typeof data['application'] === 'string' || data['application'] instanceof String)) {
            throw new Error("Expected the field `application` to be a primitive type in the JSON string but got " + data['application']);
        }
        // ensure the json data is a string
        if (data['continuation'] && !(typeof data['continuation'] === 'string' || data['continuation'] instanceof String)) {
            throw new Error("Expected the field `continuation` to be a primitive type in the JSON string but got " + data['continuation']);
        }
        // ensure the json data is a string
        if (data['iterationId'] && !(typeof data['iterationId'] === 'string' || data['iterationId'] instanceof String)) {
            throw new Error("Expected the field `iterationId` to be a primitive type in the JSON string but got " + data['iterationId']);
        }
        // ensure the json data is a string
        if (data['orderBy'] && !(typeof data['orderBy'] === 'string' || data['orderBy'] instanceof String)) {
            throw new Error("Expected the field `orderBy` to be a primitive type in the JSON string but got " + data['orderBy']);
        }
        // ensure the json data is a string
        if (data['session'] && !(typeof data['session'] === 'string' || data['session'] instanceof String)) {
            throw new Error("Expected the field `session` to be a primitive type in the JSON string but got " + data['session']);
        }
        if (data['tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tags'])) {
                throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
            }
            // validate the optional field `tags` (array)
            for (const item of data['tags']) {
                PredictionQueryTag.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} application
 */
PredictionQueryToken.prototype['application'] = undefined;

/**
 * @member {String} continuation
 */
PredictionQueryToken.prototype['continuation'] = undefined;

/**
 * @member {Date} endTime
 */
PredictionQueryToken.prototype['endTime'] = undefined;

/**
 * @member {String} iterationId
 */
PredictionQueryToken.prototype['iterationId'] = undefined;

/**
 * @member {Number} maxCount
 */
PredictionQueryToken.prototype['maxCount'] = undefined;

/**
 * @member {module:model/PredictionQueryToken.OrderByEnum} orderBy
 */
PredictionQueryToken.prototype['orderBy'] = undefined;

/**
 * @member {String} session
 */
PredictionQueryToken.prototype['session'] = undefined;

/**
 * @member {Date} startTime
 */
PredictionQueryToken.prototype['startTime'] = undefined;

/**
 * @member {Array.<module:model/PredictionQueryTag>} tags
 */
PredictionQueryToken.prototype['tags'] = undefined;





/**
 * Allowed values for the <code>orderBy</code> property.
 * @enum {String}
 * @readonly
 */
PredictionQueryToken['OrderByEnum'] = {

    /**
     * value: "Newest"
     * @const
     */
    "Newest": "Newest",

    /**
     * value: "Oldest"
     * @const
     */
    "Oldest": "Oldest",

    /**
     * value: "Suggested"
     * @const
     */
    "Suggested": "Suggested"
};



export default PredictionQueryToken;

