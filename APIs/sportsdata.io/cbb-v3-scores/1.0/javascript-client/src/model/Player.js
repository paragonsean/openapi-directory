/**
 * CBB v3 Scores
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
 * The Player model module.
 * @module model/Player
 * @version 1.0
 */
class Player {
    /**
     * Constructs a new <code>Player</code>.
     * @alias module:model/Player
     */
    constructor() { 
        
        Player.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Player</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Player} obj Optional instance to populate.
     * @return {module:model/Player} The populated <code>Player</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Player();

            if (data.hasOwnProperty('BirthCity')) {
                obj['BirthCity'] = ApiClient.convertToType(data['BirthCity'], 'String');
            }
            if (data.hasOwnProperty('BirthState')) {
                obj['BirthState'] = ApiClient.convertToType(data['BirthState'], 'String');
            }
            if (data.hasOwnProperty('Class')) {
                obj['Class'] = ApiClient.convertToType(data['Class'], 'String');
            }
            if (data.hasOwnProperty('FantasyAlarmPlayerID')) {
                obj['FantasyAlarmPlayerID'] = ApiClient.convertToType(data['FantasyAlarmPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('FirstName')) {
                obj['FirstName'] = ApiClient.convertToType(data['FirstName'], 'String');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('Height')) {
                obj['Height'] = ApiClient.convertToType(data['Height'], 'Number');
            }
            if (data.hasOwnProperty('HighSchool')) {
                obj['HighSchool'] = ApiClient.convertToType(data['HighSchool'], 'String');
            }
            if (data.hasOwnProperty('InjuryBodyPart')) {
                obj['InjuryBodyPart'] = ApiClient.convertToType(data['InjuryBodyPart'], 'String');
            }
            if (data.hasOwnProperty('InjuryNotes')) {
                obj['InjuryNotes'] = ApiClient.convertToType(data['InjuryNotes'], 'String');
            }
            if (data.hasOwnProperty('InjuryStartDate')) {
                obj['InjuryStartDate'] = ApiClient.convertToType(data['InjuryStartDate'], 'String');
            }
            if (data.hasOwnProperty('InjuryStatus')) {
                obj['InjuryStatus'] = ApiClient.convertToType(data['InjuryStatus'], 'String');
            }
            if (data.hasOwnProperty('Jersey')) {
                obj['Jersey'] = ApiClient.convertToType(data['Jersey'], 'Number');
            }
            if (data.hasOwnProperty('LastName')) {
                obj['LastName'] = ApiClient.convertToType(data['LastName'], 'String');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'String');
            }
            if (data.hasOwnProperty('RotoWirePlayerID')) {
                obj['RotoWirePlayerID'] = ApiClient.convertToType(data['RotoWirePlayerID'], 'Number');
            }
            if (data.hasOwnProperty('RotoworldPlayerID')) {
                obj['RotoworldPlayerID'] = ApiClient.convertToType(data['RotoworldPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('SportRadarPlayerID')) {
                obj['SportRadarPlayerID'] = ApiClient.convertToType(data['SportRadarPlayerID'], 'String');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('Weight')) {
                obj['Weight'] = ApiClient.convertToType(data['Weight'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Player</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Player</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['BirthCity'] && !(typeof data['BirthCity'] === 'string' || data['BirthCity'] instanceof String)) {
            throw new Error("Expected the field `BirthCity` to be a primitive type in the JSON string but got " + data['BirthCity']);
        }
        // ensure the json data is a string
        if (data['BirthState'] && !(typeof data['BirthState'] === 'string' || data['BirthState'] instanceof String)) {
            throw new Error("Expected the field `BirthState` to be a primitive type in the JSON string but got " + data['BirthState']);
        }
        // ensure the json data is a string
        if (data['Class'] && !(typeof data['Class'] === 'string' || data['Class'] instanceof String)) {
            throw new Error("Expected the field `Class` to be a primitive type in the JSON string but got " + data['Class']);
        }
        // ensure the json data is a string
        if (data['FirstName'] && !(typeof data['FirstName'] === 'string' || data['FirstName'] instanceof String)) {
            throw new Error("Expected the field `FirstName` to be a primitive type in the JSON string but got " + data['FirstName']);
        }
        // ensure the json data is a string
        if (data['HighSchool'] && !(typeof data['HighSchool'] === 'string' || data['HighSchool'] instanceof String)) {
            throw new Error("Expected the field `HighSchool` to be a primitive type in the JSON string but got " + data['HighSchool']);
        }
        // ensure the json data is a string
        if (data['InjuryBodyPart'] && !(typeof data['InjuryBodyPart'] === 'string' || data['InjuryBodyPart'] instanceof String)) {
            throw new Error("Expected the field `InjuryBodyPart` to be a primitive type in the JSON string but got " + data['InjuryBodyPart']);
        }
        // ensure the json data is a string
        if (data['InjuryNotes'] && !(typeof data['InjuryNotes'] === 'string' || data['InjuryNotes'] instanceof String)) {
            throw new Error("Expected the field `InjuryNotes` to be a primitive type in the JSON string but got " + data['InjuryNotes']);
        }
        // ensure the json data is a string
        if (data['InjuryStartDate'] && !(typeof data['InjuryStartDate'] === 'string' || data['InjuryStartDate'] instanceof String)) {
            throw new Error("Expected the field `InjuryStartDate` to be a primitive type in the JSON string but got " + data['InjuryStartDate']);
        }
        // ensure the json data is a string
        if (data['InjuryStatus'] && !(typeof data['InjuryStatus'] === 'string' || data['InjuryStatus'] instanceof String)) {
            throw new Error("Expected the field `InjuryStatus` to be a primitive type in the JSON string but got " + data['InjuryStatus']);
        }
        // ensure the json data is a string
        if (data['LastName'] && !(typeof data['LastName'] === 'string' || data['LastName'] instanceof String)) {
            throw new Error("Expected the field `LastName` to be a primitive type in the JSON string but got " + data['LastName']);
        }
        // ensure the json data is a string
        if (data['Position'] && !(typeof data['Position'] === 'string' || data['Position'] instanceof String)) {
            throw new Error("Expected the field `Position` to be a primitive type in the JSON string but got " + data['Position']);
        }
        // ensure the json data is a string
        if (data['SportRadarPlayerID'] && !(typeof data['SportRadarPlayerID'] === 'string' || data['SportRadarPlayerID'] instanceof String)) {
            throw new Error("Expected the field `SportRadarPlayerID` to be a primitive type in the JSON string but got " + data['SportRadarPlayerID']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }

        return true;
    }


}



/**
 * @member {String} BirthCity
 */
Player.prototype['BirthCity'] = undefined;

/**
 * @member {String} BirthState
 */
Player.prototype['BirthState'] = undefined;

/**
 * @member {String} Class
 */
Player.prototype['Class'] = undefined;

/**
 * @member {Number} FantasyAlarmPlayerID
 */
Player.prototype['FantasyAlarmPlayerID'] = undefined;

/**
 * @member {String} FirstName
 */
Player.prototype['FirstName'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
Player.prototype['GlobalTeamID'] = undefined;

/**
 * @member {Number} Height
 */
Player.prototype['Height'] = undefined;

/**
 * @member {String} HighSchool
 */
Player.prototype['HighSchool'] = undefined;

/**
 * @member {String} InjuryBodyPart
 */
Player.prototype['InjuryBodyPart'] = undefined;

/**
 * @member {String} InjuryNotes
 */
Player.prototype['InjuryNotes'] = undefined;

/**
 * @member {String} InjuryStartDate
 */
Player.prototype['InjuryStartDate'] = undefined;

/**
 * @member {String} InjuryStatus
 */
Player.prototype['InjuryStatus'] = undefined;

/**
 * @member {Number} Jersey
 */
Player.prototype['Jersey'] = undefined;

/**
 * @member {String} LastName
 */
Player.prototype['LastName'] = undefined;

/**
 * @member {Number} PlayerID
 */
Player.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
Player.prototype['Position'] = undefined;

/**
 * @member {Number} RotoWirePlayerID
 */
Player.prototype['RotoWirePlayerID'] = undefined;

/**
 * @member {Number} RotoworldPlayerID
 */
Player.prototype['RotoworldPlayerID'] = undefined;

/**
 * @member {String} SportRadarPlayerID
 */
Player.prototype['SportRadarPlayerID'] = undefined;

/**
 * @member {String} Team
 */
Player.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
Player.prototype['TeamID'] = undefined;

/**
 * @member {Number} Weight
 */
Player.prototype['Weight'] = undefined;






export default Player;

