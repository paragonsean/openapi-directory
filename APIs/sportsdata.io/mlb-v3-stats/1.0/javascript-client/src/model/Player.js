/**
 * MLB v3 Stats
 * MLB scores, stats, and news API.
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

            if (data.hasOwnProperty('BatHand')) {
                obj['BatHand'] = ApiClient.convertToType(data['BatHand'], 'String');
            }
            if (data.hasOwnProperty('BirthCity')) {
                obj['BirthCity'] = ApiClient.convertToType(data['BirthCity'], 'String');
            }
            if (data.hasOwnProperty('BirthCountry')) {
                obj['BirthCountry'] = ApiClient.convertToType(data['BirthCountry'], 'String');
            }
            if (data.hasOwnProperty('BirthDate')) {
                obj['BirthDate'] = ApiClient.convertToType(data['BirthDate'], 'String');
            }
            if (data.hasOwnProperty('BirthState')) {
                obj['BirthState'] = ApiClient.convertToType(data['BirthState'], 'String');
            }
            if (data.hasOwnProperty('College')) {
                obj['College'] = ApiClient.convertToType(data['College'], 'String');
            }
            if (data.hasOwnProperty('DraftKingsName')) {
                obj['DraftKingsName'] = ApiClient.convertToType(data['DraftKingsName'], 'String');
            }
            if (data.hasOwnProperty('DraftKingsPlayerID')) {
                obj['DraftKingsPlayerID'] = ApiClient.convertToType(data['DraftKingsPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Experience')) {
                obj['Experience'] = ApiClient.convertToType(data['Experience'], 'String');
            }
            if (data.hasOwnProperty('FanDuelName')) {
                obj['FanDuelName'] = ApiClient.convertToType(data['FanDuelName'], 'String');
            }
            if (data.hasOwnProperty('FanDuelPlayerID')) {
                obj['FanDuelPlayerID'] = ApiClient.convertToType(data['FanDuelPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('FantasyAlarmPlayerID')) {
                obj['FantasyAlarmPlayerID'] = ApiClient.convertToType(data['FantasyAlarmPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('FantasyDraftName')) {
                obj['FantasyDraftName'] = ApiClient.convertToType(data['FantasyDraftName'], 'String');
            }
            if (data.hasOwnProperty('FantasyDraftPlayerID')) {
                obj['FantasyDraftPlayerID'] = ApiClient.convertToType(data['FantasyDraftPlayerID'], 'Number');
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
            if (data.hasOwnProperty('MLBAMID')) {
                obj['MLBAMID'] = ApiClient.convertToType(data['MLBAMID'], 'Number');
            }
            if (data.hasOwnProperty('PhotoUrl')) {
                obj['PhotoUrl'] = ApiClient.convertToType(data['PhotoUrl'], 'String');
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
            if (data.hasOwnProperty('ProDebut')) {
                obj['ProDebut'] = ApiClient.convertToType(data['ProDebut'], 'String');
            }
            if (data.hasOwnProperty('RotoWirePlayerID')) {
                obj['RotoWirePlayerID'] = ApiClient.convertToType(data['RotoWirePlayerID'], 'Number');
            }
            if (data.hasOwnProperty('RotoworldPlayerID')) {
                obj['RotoworldPlayerID'] = ApiClient.convertToType(data['RotoworldPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Salary')) {
                obj['Salary'] = ApiClient.convertToType(data['Salary'], 'Number');
            }
            if (data.hasOwnProperty('SportRadarPlayerID')) {
                obj['SportRadarPlayerID'] = ApiClient.convertToType(data['SportRadarPlayerID'], 'String');
            }
            if (data.hasOwnProperty('SportsDataID')) {
                obj['SportsDataID'] = ApiClient.convertToType(data['SportsDataID'], 'String');
            }
            if (data.hasOwnProperty('SportsDirectPlayerID')) {
                obj['SportsDirectPlayerID'] = ApiClient.convertToType(data['SportsDirectPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('StatsPlayerID')) {
                obj['StatsPlayerID'] = ApiClient.convertToType(data['StatsPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('ThrowHand')) {
                obj['ThrowHand'] = ApiClient.convertToType(data['ThrowHand'], 'String');
            }
            if (data.hasOwnProperty('UpcomingGameID')) {
                obj['UpcomingGameID'] = ApiClient.convertToType(data['UpcomingGameID'], 'Number');
            }
            if (data.hasOwnProperty('UsaTodayHeadshotNoBackgroundUpdated')) {
                obj['UsaTodayHeadshotNoBackgroundUpdated'] = ApiClient.convertToType(data['UsaTodayHeadshotNoBackgroundUpdated'], 'String');
            }
            if (data.hasOwnProperty('UsaTodayHeadshotNoBackgroundUrl')) {
                obj['UsaTodayHeadshotNoBackgroundUrl'] = ApiClient.convertToType(data['UsaTodayHeadshotNoBackgroundUrl'], 'String');
            }
            if (data.hasOwnProperty('UsaTodayHeadshotUpdated')) {
                obj['UsaTodayHeadshotUpdated'] = ApiClient.convertToType(data['UsaTodayHeadshotUpdated'], 'String');
            }
            if (data.hasOwnProperty('UsaTodayHeadshotUrl')) {
                obj['UsaTodayHeadshotUrl'] = ApiClient.convertToType(data['UsaTodayHeadshotUrl'], 'String');
            }
            if (data.hasOwnProperty('UsaTodayPlayerID')) {
                obj['UsaTodayPlayerID'] = ApiClient.convertToType(data['UsaTodayPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Weight')) {
                obj['Weight'] = ApiClient.convertToType(data['Weight'], 'Number');
            }
            if (data.hasOwnProperty('XmlTeamPlayerID')) {
                obj['XmlTeamPlayerID'] = ApiClient.convertToType(data['XmlTeamPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('YahooName')) {
                obj['YahooName'] = ApiClient.convertToType(data['YahooName'], 'String');
            }
            if (data.hasOwnProperty('YahooPlayerID')) {
                obj['YahooPlayerID'] = ApiClient.convertToType(data['YahooPlayerID'], 'Number');
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
        if (data['BatHand'] && !(typeof data['BatHand'] === 'string' || data['BatHand'] instanceof String)) {
            throw new Error("Expected the field `BatHand` to be a primitive type in the JSON string but got " + data['BatHand']);
        }
        // ensure the json data is a string
        if (data['BirthCity'] && !(typeof data['BirthCity'] === 'string' || data['BirthCity'] instanceof String)) {
            throw new Error("Expected the field `BirthCity` to be a primitive type in the JSON string but got " + data['BirthCity']);
        }
        // ensure the json data is a string
        if (data['BirthCountry'] && !(typeof data['BirthCountry'] === 'string' || data['BirthCountry'] instanceof String)) {
            throw new Error("Expected the field `BirthCountry` to be a primitive type in the JSON string but got " + data['BirthCountry']);
        }
        // ensure the json data is a string
        if (data['BirthDate'] && !(typeof data['BirthDate'] === 'string' || data['BirthDate'] instanceof String)) {
            throw new Error("Expected the field `BirthDate` to be a primitive type in the JSON string but got " + data['BirthDate']);
        }
        // ensure the json data is a string
        if (data['BirthState'] && !(typeof data['BirthState'] === 'string' || data['BirthState'] instanceof String)) {
            throw new Error("Expected the field `BirthState` to be a primitive type in the JSON string but got " + data['BirthState']);
        }
        // ensure the json data is a string
        if (data['College'] && !(typeof data['College'] === 'string' || data['College'] instanceof String)) {
            throw new Error("Expected the field `College` to be a primitive type in the JSON string but got " + data['College']);
        }
        // ensure the json data is a string
        if (data['DraftKingsName'] && !(typeof data['DraftKingsName'] === 'string' || data['DraftKingsName'] instanceof String)) {
            throw new Error("Expected the field `DraftKingsName` to be a primitive type in the JSON string but got " + data['DraftKingsName']);
        }
        // ensure the json data is a string
        if (data['Experience'] && !(typeof data['Experience'] === 'string' || data['Experience'] instanceof String)) {
            throw new Error("Expected the field `Experience` to be a primitive type in the JSON string but got " + data['Experience']);
        }
        // ensure the json data is a string
        if (data['FanDuelName'] && !(typeof data['FanDuelName'] === 'string' || data['FanDuelName'] instanceof String)) {
            throw new Error("Expected the field `FanDuelName` to be a primitive type in the JSON string but got " + data['FanDuelName']);
        }
        // ensure the json data is a string
        if (data['FantasyDraftName'] && !(typeof data['FantasyDraftName'] === 'string' || data['FantasyDraftName'] instanceof String)) {
            throw new Error("Expected the field `FantasyDraftName` to be a primitive type in the JSON string but got " + data['FantasyDraftName']);
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
        if (data['PhotoUrl'] && !(typeof data['PhotoUrl'] === 'string' || data['PhotoUrl'] instanceof String)) {
            throw new Error("Expected the field `PhotoUrl` to be a primitive type in the JSON string but got " + data['PhotoUrl']);
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
        if (data['ProDebut'] && !(typeof data['ProDebut'] === 'string' || data['ProDebut'] instanceof String)) {
            throw new Error("Expected the field `ProDebut` to be a primitive type in the JSON string but got " + data['ProDebut']);
        }
        // ensure the json data is a string
        if (data['SportRadarPlayerID'] && !(typeof data['SportRadarPlayerID'] === 'string' || data['SportRadarPlayerID'] instanceof String)) {
            throw new Error("Expected the field `SportRadarPlayerID` to be a primitive type in the JSON string but got " + data['SportRadarPlayerID']);
        }
        // ensure the json data is a string
        if (data['SportsDataID'] && !(typeof data['SportsDataID'] === 'string' || data['SportsDataID'] instanceof String)) {
            throw new Error("Expected the field `SportsDataID` to be a primitive type in the JSON string but got " + data['SportsDataID']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['ThrowHand'] && !(typeof data['ThrowHand'] === 'string' || data['ThrowHand'] instanceof String)) {
            throw new Error("Expected the field `ThrowHand` to be a primitive type in the JSON string but got " + data['ThrowHand']);
        }
        // ensure the json data is a string
        if (data['UsaTodayHeadshotNoBackgroundUpdated'] && !(typeof data['UsaTodayHeadshotNoBackgroundUpdated'] === 'string' || data['UsaTodayHeadshotNoBackgroundUpdated'] instanceof String)) {
            throw new Error("Expected the field `UsaTodayHeadshotNoBackgroundUpdated` to be a primitive type in the JSON string but got " + data['UsaTodayHeadshotNoBackgroundUpdated']);
        }
        // ensure the json data is a string
        if (data['UsaTodayHeadshotNoBackgroundUrl'] && !(typeof data['UsaTodayHeadshotNoBackgroundUrl'] === 'string' || data['UsaTodayHeadshotNoBackgroundUrl'] instanceof String)) {
            throw new Error("Expected the field `UsaTodayHeadshotNoBackgroundUrl` to be a primitive type in the JSON string but got " + data['UsaTodayHeadshotNoBackgroundUrl']);
        }
        // ensure the json data is a string
        if (data['UsaTodayHeadshotUpdated'] && !(typeof data['UsaTodayHeadshotUpdated'] === 'string' || data['UsaTodayHeadshotUpdated'] instanceof String)) {
            throw new Error("Expected the field `UsaTodayHeadshotUpdated` to be a primitive type in the JSON string but got " + data['UsaTodayHeadshotUpdated']);
        }
        // ensure the json data is a string
        if (data['UsaTodayHeadshotUrl'] && !(typeof data['UsaTodayHeadshotUrl'] === 'string' || data['UsaTodayHeadshotUrl'] instanceof String)) {
            throw new Error("Expected the field `UsaTodayHeadshotUrl` to be a primitive type in the JSON string but got " + data['UsaTodayHeadshotUrl']);
        }
        // ensure the json data is a string
        if (data['YahooName'] && !(typeof data['YahooName'] === 'string' || data['YahooName'] instanceof String)) {
            throw new Error("Expected the field `YahooName` to be a primitive type in the JSON string but got " + data['YahooName']);
        }

        return true;
    }


}



/**
 * @member {String} BatHand
 */
Player.prototype['BatHand'] = undefined;

/**
 * @member {String} BirthCity
 */
Player.prototype['BirthCity'] = undefined;

/**
 * @member {String} BirthCountry
 */
Player.prototype['BirthCountry'] = undefined;

/**
 * @member {String} BirthDate
 */
Player.prototype['BirthDate'] = undefined;

/**
 * @member {String} BirthState
 */
Player.prototype['BirthState'] = undefined;

/**
 * @member {String} College
 */
Player.prototype['College'] = undefined;

/**
 * @member {String} DraftKingsName
 */
Player.prototype['DraftKingsName'] = undefined;

/**
 * @member {Number} DraftKingsPlayerID
 */
Player.prototype['DraftKingsPlayerID'] = undefined;

/**
 * @member {String} Experience
 */
Player.prototype['Experience'] = undefined;

/**
 * @member {String} FanDuelName
 */
Player.prototype['FanDuelName'] = undefined;

/**
 * @member {Number} FanDuelPlayerID
 */
Player.prototype['FanDuelPlayerID'] = undefined;

/**
 * @member {Number} FantasyAlarmPlayerID
 */
Player.prototype['FantasyAlarmPlayerID'] = undefined;

/**
 * @member {String} FantasyDraftName
 */
Player.prototype['FantasyDraftName'] = undefined;

/**
 * @member {Number} FantasyDraftPlayerID
 */
Player.prototype['FantasyDraftPlayerID'] = undefined;

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
 * @member {Number} MLBAMID
 */
Player.prototype['MLBAMID'] = undefined;

/**
 * @member {String} PhotoUrl
 */
Player.prototype['PhotoUrl'] = undefined;

/**
 * @member {Number} PlayerID
 */
Player.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
Player.prototype['Position'] = undefined;

/**
 * @member {String} PositionCategory
 */
Player.prototype['PositionCategory'] = undefined;

/**
 * @member {String} ProDebut
 */
Player.prototype['ProDebut'] = undefined;

/**
 * @member {Number} RotoWirePlayerID
 */
Player.prototype['RotoWirePlayerID'] = undefined;

/**
 * @member {Number} RotoworldPlayerID
 */
Player.prototype['RotoworldPlayerID'] = undefined;

/**
 * @member {Number} Salary
 */
Player.prototype['Salary'] = undefined;

/**
 * @member {String} SportRadarPlayerID
 */
Player.prototype['SportRadarPlayerID'] = undefined;

/**
 * @member {String} SportsDataID
 */
Player.prototype['SportsDataID'] = undefined;

/**
 * @member {Number} SportsDirectPlayerID
 */
Player.prototype['SportsDirectPlayerID'] = undefined;

/**
 * @member {Number} StatsPlayerID
 */
Player.prototype['StatsPlayerID'] = undefined;

/**
 * @member {String} Status
 */
Player.prototype['Status'] = undefined;

/**
 * @member {String} Team
 */
Player.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
Player.prototype['TeamID'] = undefined;

/**
 * @member {String} ThrowHand
 */
Player.prototype['ThrowHand'] = undefined;

/**
 * @member {Number} UpcomingGameID
 */
Player.prototype['UpcomingGameID'] = undefined;

/**
 * @member {String} UsaTodayHeadshotNoBackgroundUpdated
 */
Player.prototype['UsaTodayHeadshotNoBackgroundUpdated'] = undefined;

/**
 * @member {String} UsaTodayHeadshotNoBackgroundUrl
 */
Player.prototype['UsaTodayHeadshotNoBackgroundUrl'] = undefined;

/**
 * @member {String} UsaTodayHeadshotUpdated
 */
Player.prototype['UsaTodayHeadshotUpdated'] = undefined;

/**
 * @member {String} UsaTodayHeadshotUrl
 */
Player.prototype['UsaTodayHeadshotUrl'] = undefined;

/**
 * @member {Number} UsaTodayPlayerID
 */
Player.prototype['UsaTodayPlayerID'] = undefined;

/**
 * @member {Number} Weight
 */
Player.prototype['Weight'] = undefined;

/**
 * @member {Number} XmlTeamPlayerID
 */
Player.prototype['XmlTeamPlayerID'] = undefined;

/**
 * @member {String} YahooName
 */
Player.prototype['YahooName'] = undefined;

/**
 * @member {Number} YahooPlayerID
 */
Player.prototype['YahooPlayerID'] = undefined;






export default Player;

