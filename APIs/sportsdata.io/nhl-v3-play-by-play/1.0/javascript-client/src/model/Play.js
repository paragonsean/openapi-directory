/**
 * NHL v3 Play-by-Play
 * NHL play-by-play API.
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
 * The Play model module.
 * @module model/Play
 * @version 1.0
 */
class Play {
    /**
     * Constructs a new <code>Play</code>.
     * @alias module:model/Play
     */
    constructor() { 
        
        Play.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Play</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Play} obj Optional instance to populate.
     * @return {module:model/Play} The populated <code>Play</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Play();

            if (data.hasOwnProperty('AwayTeamScore')) {
                obj['AwayTeamScore'] = ApiClient.convertToType(data['AwayTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('Category')) {
                obj['Category'] = ApiClient.convertToType(data['Category'], 'String');
            }
            if (data.hasOwnProperty('ClockMinutes')) {
                obj['ClockMinutes'] = ApiClient.convertToType(data['ClockMinutes'], 'Number');
            }
            if (data.hasOwnProperty('ClockSeconds')) {
                obj['ClockSeconds'] = ApiClient.convertToType(data['ClockSeconds'], 'Number');
            }
            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('FirstAssistedByPlayerID')) {
                obj['FirstAssistedByPlayerID'] = ApiClient.convertToType(data['FirstAssistedByPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamScore')) {
                obj['HomeTeamScore'] = ApiClient.convertToType(data['HomeTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('Opponent')) {
                obj['Opponent'] = ApiClient.convertToType(data['Opponent'], 'String');
            }
            if (data.hasOwnProperty('OpponentID')) {
                obj['OpponentID'] = ApiClient.convertToType(data['OpponentID'], 'Number');
            }
            if (data.hasOwnProperty('OpposingPlayerID')) {
                obj['OpposingPlayerID'] = ApiClient.convertToType(data['OpposingPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('PeriodID')) {
                obj['PeriodID'] = ApiClient.convertToType(data['PeriodID'], 'Number');
            }
            if (data.hasOwnProperty('PeriodName')) {
                obj['PeriodName'] = ApiClient.convertToType(data['PeriodName'], 'String');
            }
            if (data.hasOwnProperty('PlayID')) {
                obj['PlayID'] = ApiClient.convertToType(data['PlayID'], 'Number');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('PowerPlayTeam')) {
                obj['PowerPlayTeam'] = ApiClient.convertToType(data['PowerPlayTeam'], 'String');
            }
            if (data.hasOwnProperty('PowerPlayTeamID')) {
                obj['PowerPlayTeamID'] = ApiClient.convertToType(data['PowerPlayTeamID'], 'Number');
            }
            if (data.hasOwnProperty('SecondAssistedByPlayerID')) {
                obj['SecondAssistedByPlayerID'] = ApiClient.convertToType(data['SecondAssistedByPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Sequence')) {
                obj['Sequence'] = ApiClient.convertToType(data['Sequence'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Play</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Play</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Category'] && !(typeof data['Category'] === 'string' || data['Category'] instanceof String)) {
            throw new Error("Expected the field `Category` to be a primitive type in the JSON string but got " + data['Category']);
        }
        // ensure the json data is a string
        if (data['Created'] && !(typeof data['Created'] === 'string' || data['Created'] instanceof String)) {
            throw new Error("Expected the field `Created` to be a primitive type in the JSON string but got " + data['Created']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['Opponent'] && !(typeof data['Opponent'] === 'string' || data['Opponent'] instanceof String)) {
            throw new Error("Expected the field `Opponent` to be a primitive type in the JSON string but got " + data['Opponent']);
        }
        // ensure the json data is a string
        if (data['PeriodName'] && !(typeof data['PeriodName'] === 'string' || data['PeriodName'] instanceof String)) {
            throw new Error("Expected the field `PeriodName` to be a primitive type in the JSON string but got " + data['PeriodName']);
        }
        // ensure the json data is a string
        if (data['PowerPlayTeam'] && !(typeof data['PowerPlayTeam'] === 'string' || data['PowerPlayTeam'] instanceof String)) {
            throw new Error("Expected the field `PowerPlayTeam` to be a primitive type in the JSON string but got " + data['PowerPlayTeam']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {Number} AwayTeamScore
 */
Play.prototype['AwayTeamScore'] = undefined;

/**
 * @member {String} Category
 */
Play.prototype['Category'] = undefined;

/**
 * @member {Number} ClockMinutes
 */
Play.prototype['ClockMinutes'] = undefined;

/**
 * @member {Number} ClockSeconds
 */
Play.prototype['ClockSeconds'] = undefined;

/**
 * @member {String} Created
 */
Play.prototype['Created'] = undefined;

/**
 * @member {String} Description
 */
Play.prototype['Description'] = undefined;

/**
 * @member {Number} FirstAssistedByPlayerID
 */
Play.prototype['FirstAssistedByPlayerID'] = undefined;

/**
 * @member {Number} HomeTeamScore
 */
Play.prototype['HomeTeamScore'] = undefined;

/**
 * @member {String} Opponent
 */
Play.prototype['Opponent'] = undefined;

/**
 * @member {Number} OpponentID
 */
Play.prototype['OpponentID'] = undefined;

/**
 * @member {Number} OpposingPlayerID
 */
Play.prototype['OpposingPlayerID'] = undefined;

/**
 * @member {Number} PeriodID
 */
Play.prototype['PeriodID'] = undefined;

/**
 * @member {String} PeriodName
 */
Play.prototype['PeriodName'] = undefined;

/**
 * @member {Number} PlayID
 */
Play.prototype['PlayID'] = undefined;

/**
 * @member {Number} PlayerID
 */
Play.prototype['PlayerID'] = undefined;

/**
 * @member {String} PowerPlayTeam
 */
Play.prototype['PowerPlayTeam'] = undefined;

/**
 * @member {Number} PowerPlayTeamID
 */
Play.prototype['PowerPlayTeamID'] = undefined;

/**
 * @member {Number} SecondAssistedByPlayerID
 */
Play.prototype['SecondAssistedByPlayerID'] = undefined;

/**
 * @member {Number} Sequence
 */
Play.prototype['Sequence'] = undefined;

/**
 * @member {String} Team
 */
Play.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
Play.prototype['TeamID'] = undefined;

/**
 * @member {String} Type
 */
Play.prototype['Type'] = undefined;

/**
 * @member {String} Updated
 */
Play.prototype['Updated'] = undefined;






export default Play;

