/**
 * Soccer v3 Scores
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
import Round from './Round';

/**
 * The Season model module.
 * @module model/Season
 * @version 1.0
 */
class Season {
    /**
     * Constructs a new <code>Season</code>.
     * @alias module:model/Season
     */
    constructor() { 
        
        Season.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Season</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Season} obj Optional instance to populate.
     * @return {module:model/Season} The populated <code>Season</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Season();

            if (data.hasOwnProperty('CompetitionId')) {
                obj['CompetitionId'] = ApiClient.convertToType(data['CompetitionId'], 'Number');
            }
            if (data.hasOwnProperty('CompetitionName')) {
                obj['CompetitionName'] = ApiClient.convertToType(data['CompetitionName'], 'String');
            }
            if (data.hasOwnProperty('CurrentSeason')) {
                obj['CurrentSeason'] = ApiClient.convertToType(data['CurrentSeason'], 'Boolean');
            }
            if (data.hasOwnProperty('EndDate')) {
                obj['EndDate'] = ApiClient.convertToType(data['EndDate'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Rounds')) {
                obj['Rounds'] = ApiClient.convertToType(data['Rounds'], [Round]);
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonId')) {
                obj['SeasonId'] = ApiClient.convertToType(data['SeasonId'], 'Number');
            }
            if (data.hasOwnProperty('StartDate')) {
                obj['StartDate'] = ApiClient.convertToType(data['StartDate'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Season</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Season</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['CompetitionName'] && !(typeof data['CompetitionName'] === 'string' || data['CompetitionName'] instanceof String)) {
            throw new Error("Expected the field `CompetitionName` to be a primitive type in the JSON string but got " + data['CompetitionName']);
        }
        // ensure the json data is a string
        if (data['EndDate'] && !(typeof data['EndDate'] === 'string' || data['EndDate'] instanceof String)) {
            throw new Error("Expected the field `EndDate` to be a primitive type in the JSON string but got " + data['EndDate']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        if (data['Rounds']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Rounds'])) {
                throw new Error("Expected the field `Rounds` to be an array in the JSON data but got " + data['Rounds']);
            }
            // validate the optional field `Rounds` (array)
            for (const item of data['Rounds']) {
                Round.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['StartDate'] && !(typeof data['StartDate'] === 'string' || data['StartDate'] instanceof String)) {
            throw new Error("Expected the field `StartDate` to be a primitive type in the JSON string but got " + data['StartDate']);
        }

        return true;
    }


}



/**
 * @member {Number} CompetitionId
 */
Season.prototype['CompetitionId'] = undefined;

/**
 * @member {String} CompetitionName
 */
Season.prototype['CompetitionName'] = undefined;

/**
 * @member {Boolean} CurrentSeason
 */
Season.prototype['CurrentSeason'] = undefined;

/**
 * @member {String} EndDate
 */
Season.prototype['EndDate'] = undefined;

/**
 * @member {String} Name
 */
Season.prototype['Name'] = undefined;

/**
 * @member {Array.<module:model/Round>} Rounds
 */
Season.prototype['Rounds'] = undefined;

/**
 * @member {Number} Season
 */
Season.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonId
 */
Season.prototype['SeasonId'] = undefined;

/**
 * @member {String} StartDate
 */
Season.prototype['StartDate'] = undefined;






export default Season;

