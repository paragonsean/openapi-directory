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

            if (data.hasOwnProperty('Active')) {
                obj['Active'] = ApiClient.convertToType(data['Active'], 'Boolean');
            }
            if (data.hasOwnProperty('Age')) {
                obj['Age'] = ApiClient.convertToType(data['Age'], 'Number');
            }
            if (data.hasOwnProperty('AverageDraftPosition')) {
                obj['AverageDraftPosition'] = ApiClient.convertToType(data['AverageDraftPosition'], 'Number');
            }
            if (data.hasOwnProperty('BirthDate')) {
                obj['BirthDate'] = ApiClient.convertToType(data['BirthDate'], 'String');
            }
            if (data.hasOwnProperty('BirthDateString')) {
                obj['BirthDateString'] = ApiClient.convertToType(data['BirthDateString'], 'String');
            }
            if (data.hasOwnProperty('ByeWeek')) {
                obj['ByeWeek'] = ApiClient.convertToType(data['ByeWeek'], 'Number');
            }
            if (data.hasOwnProperty('College')) {
                obj['College'] = ApiClient.convertToType(data['College'], 'String');
            }
            if (data.hasOwnProperty('CollegeDraftPick')) {
                obj['CollegeDraftPick'] = ApiClient.convertToType(data['CollegeDraftPick'], 'Number');
            }
            if (data.hasOwnProperty('CollegeDraftRound')) {
                obj['CollegeDraftRound'] = ApiClient.convertToType(data['CollegeDraftRound'], 'Number');
            }
            if (data.hasOwnProperty('CollegeDraftTeam')) {
                obj['CollegeDraftTeam'] = ApiClient.convertToType(data['CollegeDraftTeam'], 'String');
            }
            if (data.hasOwnProperty('CollegeDraftYear')) {
                obj['CollegeDraftYear'] = ApiClient.convertToType(data['CollegeDraftYear'], 'Number');
            }
            if (data.hasOwnProperty('CurrentStatus')) {
                obj['CurrentStatus'] = ApiClient.convertToType(data['CurrentStatus'], 'String');
            }
            if (data.hasOwnProperty('CurrentTeam')) {
                obj['CurrentTeam'] = ApiClient.convertToType(data['CurrentTeam'], 'String');
            }
            if (data.hasOwnProperty('DeclaredInactive')) {
                obj['DeclaredInactive'] = ApiClient.convertToType(data['DeclaredInactive'], 'Boolean');
            }
            if (data.hasOwnProperty('DepthDisplayOrder')) {
                obj['DepthDisplayOrder'] = ApiClient.convertToType(data['DepthDisplayOrder'], 'Number');
            }
            if (data.hasOwnProperty('DepthOrder')) {
                obj['DepthOrder'] = ApiClient.convertToType(data['DepthOrder'], 'Number');
            }
            if (data.hasOwnProperty('DepthPosition')) {
                obj['DepthPosition'] = ApiClient.convertToType(data['DepthPosition'], 'String');
            }
            if (data.hasOwnProperty('DepthPositionCategory')) {
                obj['DepthPositionCategory'] = ApiClient.convertToType(data['DepthPositionCategory'], 'String');
            }
            if (data.hasOwnProperty('DraftKingsName')) {
                obj['DraftKingsName'] = ApiClient.convertToType(data['DraftKingsName'], 'String');
            }
            if (data.hasOwnProperty('DraftKingsPlayerID')) {
                obj['DraftKingsPlayerID'] = ApiClient.convertToType(data['DraftKingsPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Experience')) {
                obj['Experience'] = ApiClient.convertToType(data['Experience'], 'Number');
            }
            if (data.hasOwnProperty('ExperienceString')) {
                obj['ExperienceString'] = ApiClient.convertToType(data['ExperienceString'], 'String');
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
            if (data.hasOwnProperty('FantasyPosition')) {
                obj['FantasyPosition'] = ApiClient.convertToType(data['FantasyPosition'], 'String');
            }
            if (data.hasOwnProperty('FantasyPositionDepthOrder')) {
                obj['FantasyPositionDepthOrder'] = ApiClient.convertToType(data['FantasyPositionDepthOrder'], 'Number');
            }
            if (data.hasOwnProperty('FirstName')) {
                obj['FirstName'] = ApiClient.convertToType(data['FirstName'], 'String');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('Height')) {
                obj['Height'] = ApiClient.convertToType(data['Height'], 'String');
            }
            if (data.hasOwnProperty('HeightFeet')) {
                obj['HeightFeet'] = ApiClient.convertToType(data['HeightFeet'], 'Number');
            }
            if (data.hasOwnProperty('HeightInches')) {
                obj['HeightInches'] = ApiClient.convertToType(data['HeightInches'], 'Number');
            }
            if (data.hasOwnProperty('InjuryBodyPart')) {
                obj['InjuryBodyPart'] = ApiClient.convertToType(data['InjuryBodyPart'], 'String');
            }
            if (data.hasOwnProperty('InjuryNotes')) {
                obj['InjuryNotes'] = ApiClient.convertToType(data['InjuryNotes'], 'String');
            }
            if (data.hasOwnProperty('InjuryPractice')) {
                obj['InjuryPractice'] = ApiClient.convertToType(data['InjuryPractice'], 'String');
            }
            if (data.hasOwnProperty('InjuryPracticeDescription')) {
                obj['InjuryPracticeDescription'] = ApiClient.convertToType(data['InjuryPracticeDescription'], 'String');
            }
            if (data.hasOwnProperty('InjuryStartDate')) {
                obj['InjuryStartDate'] = ApiClient.convertToType(data['InjuryStartDate'], 'String');
            }
            if (data.hasOwnProperty('InjuryStatus')) {
                obj['InjuryStatus'] = ApiClient.convertToType(data['InjuryStatus'], 'String');
            }
            if (data.hasOwnProperty('IsUndraftedFreeAgent')) {
                obj['IsUndraftedFreeAgent'] = ApiClient.convertToType(data['IsUndraftedFreeAgent'], 'Boolean');
            }
            if (data.hasOwnProperty('LastName')) {
                obj['LastName'] = ApiClient.convertToType(data['LastName'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'Number');
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
            if (data.hasOwnProperty('RotoWirePlayerID')) {
                obj['RotoWirePlayerID'] = ApiClient.convertToType(data['RotoWirePlayerID'], 'Number');
            }
            if (data.hasOwnProperty('RotoworldPlayerID')) {
                obj['RotoworldPlayerID'] = ApiClient.convertToType(data['RotoworldPlayerID'], 'Number');
            }
            if (data.hasOwnProperty('ShortName')) {
                obj['ShortName'] = ApiClient.convertToType(data['ShortName'], 'String');
            }
            if (data.hasOwnProperty('SportRadarPlayerID')) {
                obj['SportRadarPlayerID'] = ApiClient.convertToType(data['SportRadarPlayerID'], 'String');
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
            if (data.hasOwnProperty('UpcomingDraftKingsSalary')) {
                obj['UpcomingDraftKingsSalary'] = ApiClient.convertToType(data['UpcomingDraftKingsSalary'], 'Number');
            }
            if (data.hasOwnProperty('UpcomingFanDuelSalary')) {
                obj['UpcomingFanDuelSalary'] = ApiClient.convertToType(data['UpcomingFanDuelSalary'], 'Number');
            }
            if (data.hasOwnProperty('UpcomingGameOpponent')) {
                obj['UpcomingGameOpponent'] = ApiClient.convertToType(data['UpcomingGameOpponent'], 'String');
            }
            if (data.hasOwnProperty('UpcomingGameWeek')) {
                obj['UpcomingGameWeek'] = ApiClient.convertToType(data['UpcomingGameWeek'], 'Number');
            }
            if (data.hasOwnProperty('UpcomingOpponentPositionRank')) {
                obj['UpcomingOpponentPositionRank'] = ApiClient.convertToType(data['UpcomingOpponentPositionRank'], 'Number');
            }
            if (data.hasOwnProperty('UpcomingOpponentRank')) {
                obj['UpcomingOpponentRank'] = ApiClient.convertToType(data['UpcomingOpponentRank'], 'Number');
            }
            if (data.hasOwnProperty('UpcomingSalary')) {
                obj['UpcomingSalary'] = ApiClient.convertToType(data['UpcomingSalary'], 'Number');
            }
            if (data.hasOwnProperty('UpcomingYahooSalary')) {
                obj['UpcomingYahooSalary'] = ApiClient.convertToType(data['UpcomingYahooSalary'], 'Number');
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
        if (data['BirthDate'] && !(typeof data['BirthDate'] === 'string' || data['BirthDate'] instanceof String)) {
            throw new Error("Expected the field `BirthDate` to be a primitive type in the JSON string but got " + data['BirthDate']);
        }
        // ensure the json data is a string
        if (data['BirthDateString'] && !(typeof data['BirthDateString'] === 'string' || data['BirthDateString'] instanceof String)) {
            throw new Error("Expected the field `BirthDateString` to be a primitive type in the JSON string but got " + data['BirthDateString']);
        }
        // ensure the json data is a string
        if (data['College'] && !(typeof data['College'] === 'string' || data['College'] instanceof String)) {
            throw new Error("Expected the field `College` to be a primitive type in the JSON string but got " + data['College']);
        }
        // ensure the json data is a string
        if (data['CollegeDraftTeam'] && !(typeof data['CollegeDraftTeam'] === 'string' || data['CollegeDraftTeam'] instanceof String)) {
            throw new Error("Expected the field `CollegeDraftTeam` to be a primitive type in the JSON string but got " + data['CollegeDraftTeam']);
        }
        // ensure the json data is a string
        if (data['CurrentStatus'] && !(typeof data['CurrentStatus'] === 'string' || data['CurrentStatus'] instanceof String)) {
            throw new Error("Expected the field `CurrentStatus` to be a primitive type in the JSON string but got " + data['CurrentStatus']);
        }
        // ensure the json data is a string
        if (data['CurrentTeam'] && !(typeof data['CurrentTeam'] === 'string' || data['CurrentTeam'] instanceof String)) {
            throw new Error("Expected the field `CurrentTeam` to be a primitive type in the JSON string but got " + data['CurrentTeam']);
        }
        // ensure the json data is a string
        if (data['DepthPosition'] && !(typeof data['DepthPosition'] === 'string' || data['DepthPosition'] instanceof String)) {
            throw new Error("Expected the field `DepthPosition` to be a primitive type in the JSON string but got " + data['DepthPosition']);
        }
        // ensure the json data is a string
        if (data['DepthPositionCategory'] && !(typeof data['DepthPositionCategory'] === 'string' || data['DepthPositionCategory'] instanceof String)) {
            throw new Error("Expected the field `DepthPositionCategory` to be a primitive type in the JSON string but got " + data['DepthPositionCategory']);
        }
        // ensure the json data is a string
        if (data['DraftKingsName'] && !(typeof data['DraftKingsName'] === 'string' || data['DraftKingsName'] instanceof String)) {
            throw new Error("Expected the field `DraftKingsName` to be a primitive type in the JSON string but got " + data['DraftKingsName']);
        }
        // ensure the json data is a string
        if (data['ExperienceString'] && !(typeof data['ExperienceString'] === 'string' || data['ExperienceString'] instanceof String)) {
            throw new Error("Expected the field `ExperienceString` to be a primitive type in the JSON string but got " + data['ExperienceString']);
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
        if (data['FantasyPosition'] && !(typeof data['FantasyPosition'] === 'string' || data['FantasyPosition'] instanceof String)) {
            throw new Error("Expected the field `FantasyPosition` to be a primitive type in the JSON string but got " + data['FantasyPosition']);
        }
        // ensure the json data is a string
        if (data['FirstName'] && !(typeof data['FirstName'] === 'string' || data['FirstName'] instanceof String)) {
            throw new Error("Expected the field `FirstName` to be a primitive type in the JSON string but got " + data['FirstName']);
        }
        // ensure the json data is a string
        if (data['Height'] && !(typeof data['Height'] === 'string' || data['Height'] instanceof String)) {
            throw new Error("Expected the field `Height` to be a primitive type in the JSON string but got " + data['Height']);
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
        if (data['InjuryPractice'] && !(typeof data['InjuryPractice'] === 'string' || data['InjuryPractice'] instanceof String)) {
            throw new Error("Expected the field `InjuryPractice` to be a primitive type in the JSON string but got " + data['InjuryPractice']);
        }
        // ensure the json data is a string
        if (data['InjuryPracticeDescription'] && !(typeof data['InjuryPracticeDescription'] === 'string' || data['InjuryPracticeDescription'] instanceof String)) {
            throw new Error("Expected the field `InjuryPracticeDescription` to be a primitive type in the JSON string but got " + data['InjuryPracticeDescription']);
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
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
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
        if (data['ShortName'] && !(typeof data['ShortName'] === 'string' || data['ShortName'] instanceof String)) {
            throw new Error("Expected the field `ShortName` to be a primitive type in the JSON string but got " + data['ShortName']);
        }
        // ensure the json data is a string
        if (data['SportRadarPlayerID'] && !(typeof data['SportRadarPlayerID'] === 'string' || data['SportRadarPlayerID'] instanceof String)) {
            throw new Error("Expected the field `SportRadarPlayerID` to be a primitive type in the JSON string but got " + data['SportRadarPlayerID']);
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
        if (data['UpcomingGameOpponent'] && !(typeof data['UpcomingGameOpponent'] === 'string' || data['UpcomingGameOpponent'] instanceof String)) {
            throw new Error("Expected the field `UpcomingGameOpponent` to be a primitive type in the JSON string but got " + data['UpcomingGameOpponent']);
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
 * @member {Boolean} Active
 */
Player.prototype['Active'] = undefined;

/**
 * @member {Number} Age
 */
Player.prototype['Age'] = undefined;

/**
 * @member {Number} AverageDraftPosition
 */
Player.prototype['AverageDraftPosition'] = undefined;

/**
 * @member {String} BirthDate
 */
Player.prototype['BirthDate'] = undefined;

/**
 * @member {String} BirthDateString
 */
Player.prototype['BirthDateString'] = undefined;

/**
 * @member {Number} ByeWeek
 */
Player.prototype['ByeWeek'] = undefined;

/**
 * @member {String} College
 */
Player.prototype['College'] = undefined;

/**
 * @member {Number} CollegeDraftPick
 */
Player.prototype['CollegeDraftPick'] = undefined;

/**
 * @member {Number} CollegeDraftRound
 */
Player.prototype['CollegeDraftRound'] = undefined;

/**
 * @member {String} CollegeDraftTeam
 */
Player.prototype['CollegeDraftTeam'] = undefined;

/**
 * @member {Number} CollegeDraftYear
 */
Player.prototype['CollegeDraftYear'] = undefined;

/**
 * @member {String} CurrentStatus
 */
Player.prototype['CurrentStatus'] = undefined;

/**
 * @member {String} CurrentTeam
 */
Player.prototype['CurrentTeam'] = undefined;

/**
 * @member {Boolean} DeclaredInactive
 */
Player.prototype['DeclaredInactive'] = undefined;

/**
 * @member {Number} DepthDisplayOrder
 */
Player.prototype['DepthDisplayOrder'] = undefined;

/**
 * @member {Number} DepthOrder
 */
Player.prototype['DepthOrder'] = undefined;

/**
 * @member {String} DepthPosition
 */
Player.prototype['DepthPosition'] = undefined;

/**
 * @member {String} DepthPositionCategory
 */
Player.prototype['DepthPositionCategory'] = undefined;

/**
 * @member {String} DraftKingsName
 */
Player.prototype['DraftKingsName'] = undefined;

/**
 * @member {Number} DraftKingsPlayerID
 */
Player.prototype['DraftKingsPlayerID'] = undefined;

/**
 * @member {Number} Experience
 */
Player.prototype['Experience'] = undefined;

/**
 * @member {String} ExperienceString
 */
Player.prototype['ExperienceString'] = undefined;

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
 * @member {String} FantasyPosition
 */
Player.prototype['FantasyPosition'] = undefined;

/**
 * @member {Number} FantasyPositionDepthOrder
 */
Player.prototype['FantasyPositionDepthOrder'] = undefined;

/**
 * @member {String} FirstName
 */
Player.prototype['FirstName'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
Player.prototype['GlobalTeamID'] = undefined;

/**
 * @member {String} Height
 */
Player.prototype['Height'] = undefined;

/**
 * @member {Number} HeightFeet
 */
Player.prototype['HeightFeet'] = undefined;

/**
 * @member {Number} HeightInches
 */
Player.prototype['HeightInches'] = undefined;

/**
 * @member {String} InjuryBodyPart
 */
Player.prototype['InjuryBodyPart'] = undefined;

/**
 * @member {String} InjuryNotes
 */
Player.prototype['InjuryNotes'] = undefined;

/**
 * @member {String} InjuryPractice
 */
Player.prototype['InjuryPractice'] = undefined;

/**
 * @member {String} InjuryPracticeDescription
 */
Player.prototype['InjuryPracticeDescription'] = undefined;

/**
 * @member {String} InjuryStartDate
 */
Player.prototype['InjuryStartDate'] = undefined;

/**
 * @member {String} InjuryStatus
 */
Player.prototype['InjuryStatus'] = undefined;

/**
 * @member {Boolean} IsUndraftedFreeAgent
 */
Player.prototype['IsUndraftedFreeAgent'] = undefined;

/**
 * @member {String} LastName
 */
Player.prototype['LastName'] = undefined;

/**
 * @member {String} Name
 */
Player.prototype['Name'] = undefined;

/**
 * @member {Number} Number
 */
Player.prototype['Number'] = undefined;

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
 * @member {Number} RotoWirePlayerID
 */
Player.prototype['RotoWirePlayerID'] = undefined;

/**
 * @member {Number} RotoworldPlayerID
 */
Player.prototype['RotoworldPlayerID'] = undefined;

/**
 * @member {String} ShortName
 */
Player.prototype['ShortName'] = undefined;

/**
 * @member {String} SportRadarPlayerID
 */
Player.prototype['SportRadarPlayerID'] = undefined;

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
 * @member {Number} UpcomingDraftKingsSalary
 */
Player.prototype['UpcomingDraftKingsSalary'] = undefined;

/**
 * @member {Number} UpcomingFanDuelSalary
 */
Player.prototype['UpcomingFanDuelSalary'] = undefined;

/**
 * @member {String} UpcomingGameOpponent
 */
Player.prototype['UpcomingGameOpponent'] = undefined;

/**
 * @member {Number} UpcomingGameWeek
 */
Player.prototype['UpcomingGameWeek'] = undefined;

/**
 * @member {Number} UpcomingOpponentPositionRank
 */
Player.prototype['UpcomingOpponentPositionRank'] = undefined;

/**
 * @member {Number} UpcomingOpponentRank
 */
Player.prototype['UpcomingOpponentRank'] = undefined;

/**
 * @member {Number} UpcomingSalary
 */
Player.prototype['UpcomingSalary'] = undefined;

/**
 * @member {Number} UpcomingYahooSalary
 */
Player.prototype['UpcomingYahooSalary'] = undefined;

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

