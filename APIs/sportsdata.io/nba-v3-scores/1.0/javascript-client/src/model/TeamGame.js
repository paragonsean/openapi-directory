/**
 * NBA v3 Scores
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
 * The TeamGame model module.
 * @module model/TeamGame
 * @version 1.0
 */
class TeamGame {
    /**
     * Constructs a new <code>TeamGame</code>.
     * @alias module:model/TeamGame
     */
    constructor() { 
        
        TeamGame.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TeamGame</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamGame} obj Optional instance to populate.
     * @return {module:model/TeamGame} The populated <code>TeamGame</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamGame();

            if (data.hasOwnProperty('Assists')) {
                obj['Assists'] = ApiClient.convertToType(data['Assists'], 'Number');
            }
            if (data.hasOwnProperty('AssistsPercentage')) {
                obj['AssistsPercentage'] = ApiClient.convertToType(data['AssistsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('BlockedShots')) {
                obj['BlockedShots'] = ApiClient.convertToType(data['BlockedShots'], 'Number');
            }
            if (data.hasOwnProperty('BlocksPercentage')) {
                obj['BlocksPercentage'] = ApiClient.convertToType(data['BlocksPercentage'], 'Number');
            }
            if (data.hasOwnProperty('DateTime')) {
                obj['DateTime'] = ApiClient.convertToType(data['DateTime'], 'String');
            }
            if (data.hasOwnProperty('Day')) {
                obj['Day'] = ApiClient.convertToType(data['Day'], 'String');
            }
            if (data.hasOwnProperty('DefensiveRebounds')) {
                obj['DefensiveRebounds'] = ApiClient.convertToType(data['DefensiveRebounds'], 'Number');
            }
            if (data.hasOwnProperty('DefensiveReboundsPercentage')) {
                obj['DefensiveReboundsPercentage'] = ApiClient.convertToType(data['DefensiveReboundsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('DoubleDoubles')) {
                obj['DoubleDoubles'] = ApiClient.convertToType(data['DoubleDoubles'], 'Number');
            }
            if (data.hasOwnProperty('EffectiveFieldGoalsPercentage')) {
                obj['EffectiveFieldGoalsPercentage'] = ApiClient.convertToType(data['EffectiveFieldGoalsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPoints')) {
                obj['FantasyPoints'] = ApiClient.convertToType(data['FantasyPoints'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPointsDraftKings')) {
                obj['FantasyPointsDraftKings'] = ApiClient.convertToType(data['FantasyPointsDraftKings'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPointsFanDuel')) {
                obj['FantasyPointsFanDuel'] = ApiClient.convertToType(data['FantasyPointsFanDuel'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPointsFantasyDraft')) {
                obj['FantasyPointsFantasyDraft'] = ApiClient.convertToType(data['FantasyPointsFantasyDraft'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPointsYahoo')) {
                obj['FantasyPointsYahoo'] = ApiClient.convertToType(data['FantasyPointsYahoo'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsAttempted')) {
                obj['FieldGoalsAttempted'] = ApiClient.convertToType(data['FieldGoalsAttempted'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade')) {
                obj['FieldGoalsMade'] = ApiClient.convertToType(data['FieldGoalsMade'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsPercentage')) {
                obj['FieldGoalsPercentage'] = ApiClient.convertToType(data['FieldGoalsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('FreeThrowsAttempted')) {
                obj['FreeThrowsAttempted'] = ApiClient.convertToType(data['FreeThrowsAttempted'], 'Number');
            }
            if (data.hasOwnProperty('FreeThrowsMade')) {
                obj['FreeThrowsMade'] = ApiClient.convertToType(data['FreeThrowsMade'], 'Number');
            }
            if (data.hasOwnProperty('FreeThrowsPercentage')) {
                obj['FreeThrowsPercentage'] = ApiClient.convertToType(data['FreeThrowsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('GameID')) {
                obj['GameID'] = ApiClient.convertToType(data['GameID'], 'Number');
            }
            if (data.hasOwnProperty('Games')) {
                obj['Games'] = ApiClient.convertToType(data['Games'], 'Number');
            }
            if (data.hasOwnProperty('GlobalGameID')) {
                obj['GlobalGameID'] = ApiClient.convertToType(data['GlobalGameID'], 'Number');
            }
            if (data.hasOwnProperty('GlobalOpponentID')) {
                obj['GlobalOpponentID'] = ApiClient.convertToType(data['GlobalOpponentID'], 'Number');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('HomeOrAway')) {
                obj['HomeOrAway'] = ApiClient.convertToType(data['HomeOrAway'], 'String');
            }
            if (data.hasOwnProperty('IsClosed')) {
                obj['IsClosed'] = ApiClient.convertToType(data['IsClosed'], 'Boolean');
            }
            if (data.hasOwnProperty('IsGameOver')) {
                obj['IsGameOver'] = ApiClient.convertToType(data['IsGameOver'], 'Boolean');
            }
            if (data.hasOwnProperty('LineupConfirmed')) {
                obj['LineupConfirmed'] = ApiClient.convertToType(data['LineupConfirmed'], 'Boolean');
            }
            if (data.hasOwnProperty('LineupStatus')) {
                obj['LineupStatus'] = ApiClient.convertToType(data['LineupStatus'], 'String');
            }
            if (data.hasOwnProperty('Losses')) {
                obj['Losses'] = ApiClient.convertToType(data['Losses'], 'Number');
            }
            if (data.hasOwnProperty('Minutes')) {
                obj['Minutes'] = ApiClient.convertToType(data['Minutes'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('OffensiveRebounds')) {
                obj['OffensiveRebounds'] = ApiClient.convertToType(data['OffensiveRebounds'], 'Number');
            }
            if (data.hasOwnProperty('OffensiveReboundsPercentage')) {
                obj['OffensiveReboundsPercentage'] = ApiClient.convertToType(data['OffensiveReboundsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('Opponent')) {
                obj['Opponent'] = ApiClient.convertToType(data['Opponent'], 'String');
            }
            if (data.hasOwnProperty('OpponentID')) {
                obj['OpponentID'] = ApiClient.convertToType(data['OpponentID'], 'Number');
            }
            if (data.hasOwnProperty('PersonalFouls')) {
                obj['PersonalFouls'] = ApiClient.convertToType(data['PersonalFouls'], 'Number');
            }
            if (data.hasOwnProperty('PlayerEfficiencyRating')) {
                obj['PlayerEfficiencyRating'] = ApiClient.convertToType(data['PlayerEfficiencyRating'], 'Number');
            }
            if (data.hasOwnProperty('PlusMinus')) {
                obj['PlusMinus'] = ApiClient.convertToType(data['PlusMinus'], 'Number');
            }
            if (data.hasOwnProperty('Points')) {
                obj['Points'] = ApiClient.convertToType(data['Points'], 'Number');
            }
            if (data.hasOwnProperty('Possessions')) {
                obj['Possessions'] = ApiClient.convertToType(data['Possessions'], 'Number');
            }
            if (data.hasOwnProperty('Rebounds')) {
                obj['Rebounds'] = ApiClient.convertToType(data['Rebounds'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('Seconds')) {
                obj['Seconds'] = ApiClient.convertToType(data['Seconds'], 'Number');
            }
            if (data.hasOwnProperty('StatID')) {
                obj['StatID'] = ApiClient.convertToType(data['StatID'], 'Number');
            }
            if (data.hasOwnProperty('Steals')) {
                obj['Steals'] = ApiClient.convertToType(data['Steals'], 'Number');
            }
            if (data.hasOwnProperty('StealsPercentage')) {
                obj['StealsPercentage'] = ApiClient.convertToType(data['StealsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('ThreePointersAttempted')) {
                obj['ThreePointersAttempted'] = ApiClient.convertToType(data['ThreePointersAttempted'], 'Number');
            }
            if (data.hasOwnProperty('ThreePointersMade')) {
                obj['ThreePointersMade'] = ApiClient.convertToType(data['ThreePointersMade'], 'Number');
            }
            if (data.hasOwnProperty('ThreePointersPercentage')) {
                obj['ThreePointersPercentage'] = ApiClient.convertToType(data['ThreePointersPercentage'], 'Number');
            }
            if (data.hasOwnProperty('TotalReboundsPercentage')) {
                obj['TotalReboundsPercentage'] = ApiClient.convertToType(data['TotalReboundsPercentage'], 'Number');
            }
            if (data.hasOwnProperty('TripleDoubles')) {
                obj['TripleDoubles'] = ApiClient.convertToType(data['TripleDoubles'], 'Number');
            }
            if (data.hasOwnProperty('TrueShootingAttempts')) {
                obj['TrueShootingAttempts'] = ApiClient.convertToType(data['TrueShootingAttempts'], 'Number');
            }
            if (data.hasOwnProperty('TrueShootingPercentage')) {
                obj['TrueShootingPercentage'] = ApiClient.convertToType(data['TrueShootingPercentage'], 'Number');
            }
            if (data.hasOwnProperty('TurnOversPercentage')) {
                obj['TurnOversPercentage'] = ApiClient.convertToType(data['TurnOversPercentage'], 'Number');
            }
            if (data.hasOwnProperty('Turnovers')) {
                obj['Turnovers'] = ApiClient.convertToType(data['Turnovers'], 'Number');
            }
            if (data.hasOwnProperty('TwoPointersAttempted')) {
                obj['TwoPointersAttempted'] = ApiClient.convertToType(data['TwoPointersAttempted'], 'Number');
            }
            if (data.hasOwnProperty('TwoPointersMade')) {
                obj['TwoPointersMade'] = ApiClient.convertToType(data['TwoPointersMade'], 'Number');
            }
            if (data.hasOwnProperty('TwoPointersPercentage')) {
                obj['TwoPointersPercentage'] = ApiClient.convertToType(data['TwoPointersPercentage'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('UsageRatePercentage')) {
                obj['UsageRatePercentage'] = ApiClient.convertToType(data['UsageRatePercentage'], 'Number');
            }
            if (data.hasOwnProperty('Wins')) {
                obj['Wins'] = ApiClient.convertToType(data['Wins'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamGame</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamGame</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['DateTime'] && !(typeof data['DateTime'] === 'string' || data['DateTime'] instanceof String)) {
            throw new Error("Expected the field `DateTime` to be a primitive type in the JSON string but got " + data['DateTime']);
        }
        // ensure the json data is a string
        if (data['Day'] && !(typeof data['Day'] === 'string' || data['Day'] instanceof String)) {
            throw new Error("Expected the field `Day` to be a primitive type in the JSON string but got " + data['Day']);
        }
        // ensure the json data is a string
        if (data['HomeOrAway'] && !(typeof data['HomeOrAway'] === 'string' || data['HomeOrAway'] instanceof String)) {
            throw new Error("Expected the field `HomeOrAway` to be a primitive type in the JSON string but got " + data['HomeOrAway']);
        }
        // ensure the json data is a string
        if (data['LineupStatus'] && !(typeof data['LineupStatus'] === 'string' || data['LineupStatus'] instanceof String)) {
            throw new Error("Expected the field `LineupStatus` to be a primitive type in the JSON string but got " + data['LineupStatus']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Opponent'] && !(typeof data['Opponent'] === 'string' || data['Opponent'] instanceof String)) {
            throw new Error("Expected the field `Opponent` to be a primitive type in the JSON string but got " + data['Opponent']);
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
 * @member {Number} Assists
 */
TeamGame.prototype['Assists'] = undefined;

/**
 * @member {Number} AssistsPercentage
 */
TeamGame.prototype['AssistsPercentage'] = undefined;

/**
 * @member {Number} BlockedShots
 */
TeamGame.prototype['BlockedShots'] = undefined;

/**
 * @member {Number} BlocksPercentage
 */
TeamGame.prototype['BlocksPercentage'] = undefined;

/**
 * @member {String} DateTime
 */
TeamGame.prototype['DateTime'] = undefined;

/**
 * @member {String} Day
 */
TeamGame.prototype['Day'] = undefined;

/**
 * @member {Number} DefensiveRebounds
 */
TeamGame.prototype['DefensiveRebounds'] = undefined;

/**
 * @member {Number} DefensiveReboundsPercentage
 */
TeamGame.prototype['DefensiveReboundsPercentage'] = undefined;

/**
 * @member {Number} DoubleDoubles
 */
TeamGame.prototype['DoubleDoubles'] = undefined;

/**
 * @member {Number} EffectiveFieldGoalsPercentage
 */
TeamGame.prototype['EffectiveFieldGoalsPercentage'] = undefined;

/**
 * @member {Number} FantasyPoints
 */
TeamGame.prototype['FantasyPoints'] = undefined;

/**
 * @member {Number} FantasyPointsDraftKings
 */
TeamGame.prototype['FantasyPointsDraftKings'] = undefined;

/**
 * @member {Number} FantasyPointsFanDuel
 */
TeamGame.prototype['FantasyPointsFanDuel'] = undefined;

/**
 * @member {Number} FantasyPointsFantasyDraft
 */
TeamGame.prototype['FantasyPointsFantasyDraft'] = undefined;

/**
 * @member {Number} FantasyPointsYahoo
 */
TeamGame.prototype['FantasyPointsYahoo'] = undefined;

/**
 * @member {Number} FieldGoalsAttempted
 */
TeamGame.prototype['FieldGoalsAttempted'] = undefined;

/**
 * @member {Number} FieldGoalsMade
 */
TeamGame.prototype['FieldGoalsMade'] = undefined;

/**
 * @member {Number} FieldGoalsPercentage
 */
TeamGame.prototype['FieldGoalsPercentage'] = undefined;

/**
 * @member {Number} FreeThrowsAttempted
 */
TeamGame.prototype['FreeThrowsAttempted'] = undefined;

/**
 * @member {Number} FreeThrowsMade
 */
TeamGame.prototype['FreeThrowsMade'] = undefined;

/**
 * @member {Number} FreeThrowsPercentage
 */
TeamGame.prototype['FreeThrowsPercentage'] = undefined;

/**
 * @member {Number} GameID
 */
TeamGame.prototype['GameID'] = undefined;

/**
 * @member {Number} Games
 */
TeamGame.prototype['Games'] = undefined;

/**
 * @member {Number} GlobalGameID
 */
TeamGame.prototype['GlobalGameID'] = undefined;

/**
 * @member {Number} GlobalOpponentID
 */
TeamGame.prototype['GlobalOpponentID'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
TeamGame.prototype['GlobalTeamID'] = undefined;

/**
 * @member {String} HomeOrAway
 */
TeamGame.prototype['HomeOrAway'] = undefined;

/**
 * @member {Boolean} IsClosed
 */
TeamGame.prototype['IsClosed'] = undefined;

/**
 * @member {Boolean} IsGameOver
 */
TeamGame.prototype['IsGameOver'] = undefined;

/**
 * @member {Boolean} LineupConfirmed
 */
TeamGame.prototype['LineupConfirmed'] = undefined;

/**
 * @member {String} LineupStatus
 */
TeamGame.prototype['LineupStatus'] = undefined;

/**
 * @member {Number} Losses
 */
TeamGame.prototype['Losses'] = undefined;

/**
 * @member {Number} Minutes
 */
TeamGame.prototype['Minutes'] = undefined;

/**
 * @member {String} Name
 */
TeamGame.prototype['Name'] = undefined;

/**
 * @member {Number} OffensiveRebounds
 */
TeamGame.prototype['OffensiveRebounds'] = undefined;

/**
 * @member {Number} OffensiveReboundsPercentage
 */
TeamGame.prototype['OffensiveReboundsPercentage'] = undefined;

/**
 * @member {String} Opponent
 */
TeamGame.prototype['Opponent'] = undefined;

/**
 * @member {Number} OpponentID
 */
TeamGame.prototype['OpponentID'] = undefined;

/**
 * @member {Number} PersonalFouls
 */
TeamGame.prototype['PersonalFouls'] = undefined;

/**
 * @member {Number} PlayerEfficiencyRating
 */
TeamGame.prototype['PlayerEfficiencyRating'] = undefined;

/**
 * @member {Number} PlusMinus
 */
TeamGame.prototype['PlusMinus'] = undefined;

/**
 * @member {Number} Points
 */
TeamGame.prototype['Points'] = undefined;

/**
 * @member {Number} Possessions
 */
TeamGame.prototype['Possessions'] = undefined;

/**
 * @member {Number} Rebounds
 */
TeamGame.prototype['Rebounds'] = undefined;

/**
 * @member {Number} Season
 */
TeamGame.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
TeamGame.prototype['SeasonType'] = undefined;

/**
 * @member {Number} Seconds
 */
TeamGame.prototype['Seconds'] = undefined;

/**
 * @member {Number} StatID
 */
TeamGame.prototype['StatID'] = undefined;

/**
 * @member {Number} Steals
 */
TeamGame.prototype['Steals'] = undefined;

/**
 * @member {Number} StealsPercentage
 */
TeamGame.prototype['StealsPercentage'] = undefined;

/**
 * @member {String} Team
 */
TeamGame.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
TeamGame.prototype['TeamID'] = undefined;

/**
 * @member {Number} ThreePointersAttempted
 */
TeamGame.prototype['ThreePointersAttempted'] = undefined;

/**
 * @member {Number} ThreePointersMade
 */
TeamGame.prototype['ThreePointersMade'] = undefined;

/**
 * @member {Number} ThreePointersPercentage
 */
TeamGame.prototype['ThreePointersPercentage'] = undefined;

/**
 * @member {Number} TotalReboundsPercentage
 */
TeamGame.prototype['TotalReboundsPercentage'] = undefined;

/**
 * @member {Number} TripleDoubles
 */
TeamGame.prototype['TripleDoubles'] = undefined;

/**
 * @member {Number} TrueShootingAttempts
 */
TeamGame.prototype['TrueShootingAttempts'] = undefined;

/**
 * @member {Number} TrueShootingPercentage
 */
TeamGame.prototype['TrueShootingPercentage'] = undefined;

/**
 * @member {Number} TurnOversPercentage
 */
TeamGame.prototype['TurnOversPercentage'] = undefined;

/**
 * @member {Number} Turnovers
 */
TeamGame.prototype['Turnovers'] = undefined;

/**
 * @member {Number} TwoPointersAttempted
 */
TeamGame.prototype['TwoPointersAttempted'] = undefined;

/**
 * @member {Number} TwoPointersMade
 */
TeamGame.prototype['TwoPointersMade'] = undefined;

/**
 * @member {Number} TwoPointersPercentage
 */
TeamGame.prototype['TwoPointersPercentage'] = undefined;

/**
 * @member {String} Updated
 */
TeamGame.prototype['Updated'] = undefined;

/**
 * @member {Number} UsageRatePercentage
 */
TeamGame.prototype['UsageRatePercentage'] = undefined;

/**
 * @member {Number} Wins
 */
TeamGame.prototype['Wins'] = undefined;






export default TeamGame;

