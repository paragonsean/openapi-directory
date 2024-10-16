/**
 * CBB v3 Stats
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
import Game from './Game';

/**
 * The Tournament model module.
 * @module model/Tournament
 * @version 1.0
 */
class Tournament {
    /**
     * Constructs a new <code>Tournament</code>.
     * @alias module:model/Tournament
     */
    constructor() { 
        
        Tournament.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Tournament</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Tournament} obj Optional instance to populate.
     * @return {module:model/Tournament} The populated <code>Tournament</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Tournament();

            if (data.hasOwnProperty('Games')) {
                obj['Games'] = ApiClient.convertToType(data['Games'], [Game]);
            }
            if (data.hasOwnProperty('LeftBottomBracketConference')) {
                obj['LeftBottomBracketConference'] = ApiClient.convertToType(data['LeftBottomBracketConference'], 'String');
            }
            if (data.hasOwnProperty('LeftTopBracketConference')) {
                obj['LeftTopBracketConference'] = ApiClient.convertToType(data['LeftTopBracketConference'], 'String');
            }
            if (data.hasOwnProperty('Location')) {
                obj['Location'] = ApiClient.convertToType(data['Location'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('RightBottomBracketConference')) {
                obj['RightBottomBracketConference'] = ApiClient.convertToType(data['RightBottomBracketConference'], 'String');
            }
            if (data.hasOwnProperty('RightTopBracketConference')) {
                obj['RightTopBracketConference'] = ApiClient.convertToType(data['RightTopBracketConference'], 'String');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('TournamentID')) {
                obj['TournamentID'] = ApiClient.convertToType(data['TournamentID'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Tournament</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Tournament</code>.
     */
    static validateJSON(data) {
        if (data['Games']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Games'])) {
                throw new Error("Expected the field `Games` to be an array in the JSON data but got " + data['Games']);
            }
            // validate the optional field `Games` (array)
            for (const item of data['Games']) {
                Game.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['LeftBottomBracketConference'] && !(typeof data['LeftBottomBracketConference'] === 'string' || data['LeftBottomBracketConference'] instanceof String)) {
            throw new Error("Expected the field `LeftBottomBracketConference` to be a primitive type in the JSON string but got " + data['LeftBottomBracketConference']);
        }
        // ensure the json data is a string
        if (data['LeftTopBracketConference'] && !(typeof data['LeftTopBracketConference'] === 'string' || data['LeftTopBracketConference'] instanceof String)) {
            throw new Error("Expected the field `LeftTopBracketConference` to be a primitive type in the JSON string but got " + data['LeftTopBracketConference']);
        }
        // ensure the json data is a string
        if (data['Location'] && !(typeof data['Location'] === 'string' || data['Location'] instanceof String)) {
            throw new Error("Expected the field `Location` to be a primitive type in the JSON string but got " + data['Location']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['RightBottomBracketConference'] && !(typeof data['RightBottomBracketConference'] === 'string' || data['RightBottomBracketConference'] instanceof String)) {
            throw new Error("Expected the field `RightBottomBracketConference` to be a primitive type in the JSON string but got " + data['RightBottomBracketConference']);
        }
        // ensure the json data is a string
        if (data['RightTopBracketConference'] && !(typeof data['RightTopBracketConference'] === 'string' || data['RightTopBracketConference'] instanceof String)) {
            throw new Error("Expected the field `RightTopBracketConference` to be a primitive type in the JSON string but got " + data['RightTopBracketConference']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Game>} Games
 */
Tournament.prototype['Games'] = undefined;

/**
 * @member {String} LeftBottomBracketConference
 */
Tournament.prototype['LeftBottomBracketConference'] = undefined;

/**
 * @member {String} LeftTopBracketConference
 */
Tournament.prototype['LeftTopBracketConference'] = undefined;

/**
 * @member {String} Location
 */
Tournament.prototype['Location'] = undefined;

/**
 * @member {String} Name
 */
Tournament.prototype['Name'] = undefined;

/**
 * @member {String} RightBottomBracketConference
 */
Tournament.prototype['RightBottomBracketConference'] = undefined;

/**
 * @member {String} RightTopBracketConference
 */
Tournament.prototype['RightTopBracketConference'] = undefined;

/**
 * @member {Number} Season
 */
Tournament.prototype['Season'] = undefined;

/**
 * @member {Number} TournamentID
 */
Tournament.prototype['TournamentID'] = undefined;






export default Tournament;

