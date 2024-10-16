/**
 * LoL v3 Scores
 * LoL v3 Scores
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
 * The Round model module.
 * @module model/Round
 * @version 1.0
 */
class Round {
    /**
     * Constructs a new <code>Round</code>.
     * @alias module:model/Round
     */
    constructor() { 
        
        Round.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Round</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Round} obj Optional instance to populate.
     * @return {module:model/Round} The populated <code>Round</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Round();

            if (data.hasOwnProperty('CurrentRound')) {
                obj['CurrentRound'] = ApiClient.convertToType(data['CurrentRound'], 'Boolean');
            }
            if (data.hasOwnProperty('CurrentWeek')) {
                obj['CurrentWeek'] = ApiClient.convertToType(data['CurrentWeek'], 'Number');
            }
            if (data.hasOwnProperty('EndDate')) {
                obj['EndDate'] = ApiClient.convertToType(data['EndDate'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('RoundId')) {
                obj['RoundId'] = ApiClient.convertToType(data['RoundId'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonId')) {
                obj['SeasonId'] = ApiClient.convertToType(data['SeasonId'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('StartDate')) {
                obj['StartDate'] = ApiClient.convertToType(data['StartDate'], 'String');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Round</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Round</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['EndDate'] && !(typeof data['EndDate'] === 'string' || data['EndDate'] instanceof String)) {
            throw new Error("Expected the field `EndDate` to be a primitive type in the JSON string but got " + data['EndDate']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['StartDate'] && !(typeof data['StartDate'] === 'string' || data['StartDate'] instanceof String)) {
            throw new Error("Expected the field `StartDate` to be a primitive type in the JSON string but got " + data['StartDate']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }

        return true;
    }


}



/**
 * @member {Boolean} CurrentRound
 */
Round.prototype['CurrentRound'] = undefined;

/**
 * @member {Number} CurrentWeek
 */
Round.prototype['CurrentWeek'] = undefined;

/**
 * @member {String} EndDate
 */
Round.prototype['EndDate'] = undefined;

/**
 * @member {String} Name
 */
Round.prototype['Name'] = undefined;

/**
 * @member {Number} RoundId
 */
Round.prototype['RoundId'] = undefined;

/**
 * @member {Number} Season
 */
Round.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonId
 */
Round.prototype['SeasonId'] = undefined;

/**
 * @member {Number} SeasonType
 */
Round.prototype['SeasonType'] = undefined;

/**
 * @member {String} StartDate
 */
Round.prototype['StartDate'] = undefined;

/**
 * @member {String} Type
 */
Round.prototype['Type'] = undefined;






export default Round;

