/**
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
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
 * The PlayerDefense model module.
 * @module model/PlayerDefense
 * @version 1.0
 */
class PlayerDefense {
    /**
     * Constructs a new <code>PlayerDefense</code>.
     * @alias module:model/PlayerDefense
     */
    constructor() { 
        
        PlayerDefense.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlayerDefense</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayerDefense} obj Optional instance to populate.
     * @return {module:model/PlayerDefense} The populated <code>PlayerDefense</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayerDefense();

            if (data.hasOwnProperty('AssistedTackles')) {
                obj['AssistedTackles'] = ApiClient.convertToType(data['AssistedTackles'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPoints')) {
                obj['FantasyPoints'] = ApiClient.convertToType(data['FantasyPoints'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPosition')) {
                obj['FantasyPosition'] = ApiClient.convertToType(data['FantasyPosition'], 'String');
            }
            if (data.hasOwnProperty('FumbleReturnTouchdowns')) {
                obj['FumbleReturnTouchdowns'] = ApiClient.convertToType(data['FumbleReturnTouchdowns'], 'Number');
            }
            if (data.hasOwnProperty('FumblesForced')) {
                obj['FumblesForced'] = ApiClient.convertToType(data['FumblesForced'], 'Number');
            }
            if (data.hasOwnProperty('FumblesRecovered')) {
                obj['FumblesRecovered'] = ApiClient.convertToType(data['FumblesRecovered'], 'Number');
            }
            if (data.hasOwnProperty('InterceptionReturnTouchdowns')) {
                obj['InterceptionReturnTouchdowns'] = ApiClient.convertToType(data['InterceptionReturnTouchdowns'], 'Number');
            }
            if (data.hasOwnProperty('InterceptionReturnYards')) {
                obj['InterceptionReturnYards'] = ApiClient.convertToType(data['InterceptionReturnYards'], 'Number');
            }
            if (data.hasOwnProperty('Interceptions')) {
                obj['Interceptions'] = ApiClient.convertToType(data['Interceptions'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'Number');
            }
            if (data.hasOwnProperty('PassesDefended')) {
                obj['PassesDefended'] = ApiClient.convertToType(data['PassesDefended'], 'Number');
            }
            if (data.hasOwnProperty('PlayerGameID')) {
                obj['PlayerGameID'] = ApiClient.convertToType(data['PlayerGameID'], 'Number');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'String');
            }
            if (data.hasOwnProperty('PositionCategory')) {
                obj['PositionCategory'] = ApiClient.convertToType(data['PositionCategory'], 'String');
            }
            if (data.hasOwnProperty('QuarterbackHits')) {
                obj['QuarterbackHits'] = ApiClient.convertToType(data['QuarterbackHits'], 'Number');
            }
            if (data.hasOwnProperty('SackYards')) {
                obj['SackYards'] = ApiClient.convertToType(data['SackYards'], 'Number');
            }
            if (data.hasOwnProperty('Sacks')) {
                obj['Sacks'] = ApiClient.convertToType(data['Sacks'], 'Number');
            }
            if (data.hasOwnProperty('Safeties')) {
                obj['Safeties'] = ApiClient.convertToType(data['Safeties'], 'Number');
            }
            if (data.hasOwnProperty('ShortName')) {
                obj['ShortName'] = ApiClient.convertToType(data['ShortName'], 'String');
            }
            if (data.hasOwnProperty('SoloTackles')) {
                obj['SoloTackles'] = ApiClient.convertToType(data['SoloTackles'], 'Number');
            }
            if (data.hasOwnProperty('Tackles')) {
                obj['Tackles'] = ApiClient.convertToType(data['Tackles'], 'Number');
            }
            if (data.hasOwnProperty('TacklesForLoss')) {
                obj['TacklesForLoss'] = ApiClient.convertToType(data['TacklesForLoss'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayerDefense</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayerDefense</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['FantasyPosition'] && !(typeof data['FantasyPosition'] === 'string' || data['FantasyPosition'] instanceof String)) {
            throw new Error("Expected the field `FantasyPosition` to be a primitive type in the JSON string but got " + data['FantasyPosition']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Position'] && !(typeof data['Position'] === 'string' || data['Position'] instanceof String)) {
            throw new Error("Expected the field `Position` to be a primitive type in the JSON string but got " + data['Position']);
        }
        // ensure the json data is a string
        if (data['PositionCategory'] && !(typeof data['PositionCategory'] === 'string' || data['PositionCategory'] instanceof String)) {
            throw new Error("Expected the field `PositionCategory` to be a primitive type in the JSON string but got " + data['PositionCategory']);
        }
        // ensure the json data is a string
        if (data['ShortName'] && !(typeof data['ShortName'] === 'string' || data['ShortName'] instanceof String)) {
            throw new Error("Expected the field `ShortName` to be a primitive type in the JSON string but got " + data['ShortName']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {Number} AssistedTackles
 */
PlayerDefense.prototype['AssistedTackles'] = undefined;

/**
 * @member {Number} FantasyPoints
 */
PlayerDefense.prototype['FantasyPoints'] = undefined;

/**
 * @member {String} FantasyPosition
 */
PlayerDefense.prototype['FantasyPosition'] = undefined;

/**
 * @member {Number} FumbleReturnTouchdowns
 */
PlayerDefense.prototype['FumbleReturnTouchdowns'] = undefined;

/**
 * @member {Number} FumblesForced
 */
PlayerDefense.prototype['FumblesForced'] = undefined;

/**
 * @member {Number} FumblesRecovered
 */
PlayerDefense.prototype['FumblesRecovered'] = undefined;

/**
 * @member {Number} InterceptionReturnTouchdowns
 */
PlayerDefense.prototype['InterceptionReturnTouchdowns'] = undefined;

/**
 * @member {Number} InterceptionReturnYards
 */
PlayerDefense.prototype['InterceptionReturnYards'] = undefined;

/**
 * @member {Number} Interceptions
 */
PlayerDefense.prototype['Interceptions'] = undefined;

/**
 * @member {String} Name
 */
PlayerDefense.prototype['Name'] = undefined;

/**
 * @member {Number} Number
 */
PlayerDefense.prototype['Number'] = undefined;

/**
 * @member {Number} PassesDefended
 */
PlayerDefense.prototype['PassesDefended'] = undefined;

/**
 * @member {Number} PlayerGameID
 */
PlayerDefense.prototype['PlayerGameID'] = undefined;

/**
 * @member {Number} PlayerID
 */
PlayerDefense.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
PlayerDefense.prototype['Position'] = undefined;

/**
 * @member {String} PositionCategory
 */
PlayerDefense.prototype['PositionCategory'] = undefined;

/**
 * @member {Number} QuarterbackHits
 */
PlayerDefense.prototype['QuarterbackHits'] = undefined;

/**
 * @member {Number} SackYards
 */
PlayerDefense.prototype['SackYards'] = undefined;

/**
 * @member {Number} Sacks
 */
PlayerDefense.prototype['Sacks'] = undefined;

/**
 * @member {Number} Safeties
 */
PlayerDefense.prototype['Safeties'] = undefined;

/**
 * @member {String} ShortName
 */
PlayerDefense.prototype['ShortName'] = undefined;

/**
 * @member {Number} SoloTackles
 */
PlayerDefense.prototype['SoloTackles'] = undefined;

/**
 * @member {Number} Tackles
 */
PlayerDefense.prototype['Tackles'] = undefined;

/**
 * @member {Number} TacklesForLoss
 */
PlayerDefense.prototype['TacklesForLoss'] = undefined;

/**
 * @member {String} Team
 */
PlayerDefense.prototype['Team'] = undefined;

/**
 * @member {String} Updated
 */
PlayerDefense.prototype['Updated'] = undefined;






export default PlayerDefense;

