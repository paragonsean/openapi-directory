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

/**
 * The TeamSeason model module.
 * @module model/TeamSeason
 * @version 1.0
 */
class TeamSeason {
    /**
     * Constructs a new <code>TeamSeason</code>.
     * @alias module:model/TeamSeason
     */
    constructor() { 
        
        TeamSeason.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TeamSeason</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamSeason} obj Optional instance to populate.
     * @return {module:model/TeamSeason} The populated <code>TeamSeason</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamSeason();

            if (data.hasOwnProperty('Assists')) {
                obj['Assists'] = ApiClient.convertToType(data['Assists'], 'Number');
            }
            if (data.hasOwnProperty('BlockedShots')) {
                obj['BlockedShots'] = ApiClient.convertToType(data['BlockedShots'], 'Number');
            }
            if (data.hasOwnProperty('CornersWon')) {
                obj['CornersWon'] = ApiClient.convertToType(data['CornersWon'], 'Number');
            }
            if (data.hasOwnProperty('Crosses')) {
                obj['Crosses'] = ApiClient.convertToType(data['Crosses'], 'Number');
            }
            if (data.hasOwnProperty('DefenderCleanSheets')) {
                obj['DefenderCleanSheets'] = ApiClient.convertToType(data['DefenderCleanSheets'], 'Number');
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
            if (data.hasOwnProperty('FantasyPointsMondogoal')) {
                obj['FantasyPointsMondogoal'] = ApiClient.convertToType(data['FantasyPointsMondogoal'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPointsYahoo')) {
                obj['FantasyPointsYahoo'] = ApiClient.convertToType(data['FantasyPointsYahoo'], 'Number');
            }
            if (data.hasOwnProperty('Fouled')) {
                obj['Fouled'] = ApiClient.convertToType(data['Fouled'], 'Number');
            }
            if (data.hasOwnProperty('Fouls')) {
                obj['Fouls'] = ApiClient.convertToType(data['Fouls'], 'Number');
            }
            if (data.hasOwnProperty('Games')) {
                obj['Games'] = ApiClient.convertToType(data['Games'], 'Number');
            }
            if (data.hasOwnProperty('GlobalTeamId')) {
                obj['GlobalTeamId'] = ApiClient.convertToType(data['GlobalTeamId'], 'Number');
            }
            if (data.hasOwnProperty('GoalkeeperCleanSheets')) {
                obj['GoalkeeperCleanSheets'] = ApiClient.convertToType(data['GoalkeeperCleanSheets'], 'Number');
            }
            if (data.hasOwnProperty('GoalkeeperGoalsAgainst')) {
                obj['GoalkeeperGoalsAgainst'] = ApiClient.convertToType(data['GoalkeeperGoalsAgainst'], 'Number');
            }
            if (data.hasOwnProperty('GoalkeeperSaves')) {
                obj['GoalkeeperSaves'] = ApiClient.convertToType(data['GoalkeeperSaves'], 'Number');
            }
            if (data.hasOwnProperty('GoalkeeperSingleGoalAgainst')) {
                obj['GoalkeeperSingleGoalAgainst'] = ApiClient.convertToType(data['GoalkeeperSingleGoalAgainst'], 'Number');
            }
            if (data.hasOwnProperty('GoalkeeperWins')) {
                obj['GoalkeeperWins'] = ApiClient.convertToType(data['GoalkeeperWins'], 'Number');
            }
            if (data.hasOwnProperty('Goals')) {
                obj['Goals'] = ApiClient.convertToType(data['Goals'], 'Number');
            }
            if (data.hasOwnProperty('Interceptions')) {
                obj['Interceptions'] = ApiClient.convertToType(data['Interceptions'], 'Number');
            }
            if (data.hasOwnProperty('LastManTackle')) {
                obj['LastManTackle'] = ApiClient.convertToType(data['LastManTackle'], 'Number');
            }
            if (data.hasOwnProperty('Minutes')) {
                obj['Minutes'] = ApiClient.convertToType(data['Minutes'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Offsides')) {
                obj['Offsides'] = ApiClient.convertToType(data['Offsides'], 'Number');
            }
            if (data.hasOwnProperty('OpponentScore')) {
                obj['OpponentScore'] = ApiClient.convertToType(data['OpponentScore'], 'Number');
            }
            if (data.hasOwnProperty('OwnGoals')) {
                obj['OwnGoals'] = ApiClient.convertToType(data['OwnGoals'], 'Number');
            }
            if (data.hasOwnProperty('Passes')) {
                obj['Passes'] = ApiClient.convertToType(data['Passes'], 'Number');
            }
            if (data.hasOwnProperty('PassesCompleted')) {
                obj['PassesCompleted'] = ApiClient.convertToType(data['PassesCompleted'], 'Number');
            }
            if (data.hasOwnProperty('PenaltiesConceded')) {
                obj['PenaltiesConceded'] = ApiClient.convertToType(data['PenaltiesConceded'], 'Number');
            }
            if (data.hasOwnProperty('PenaltiesWon')) {
                obj['PenaltiesWon'] = ApiClient.convertToType(data['PenaltiesWon'], 'Number');
            }
            if (data.hasOwnProperty('PenaltyKickGoals')) {
                obj['PenaltyKickGoals'] = ApiClient.convertToType(data['PenaltyKickGoals'], 'Number');
            }
            if (data.hasOwnProperty('PenaltyKickMisses')) {
                obj['PenaltyKickMisses'] = ApiClient.convertToType(data['PenaltyKickMisses'], 'Number');
            }
            if (data.hasOwnProperty('PenaltyKickSaves')) {
                obj['PenaltyKickSaves'] = ApiClient.convertToType(data['PenaltyKickSaves'], 'Number');
            }
            if (data.hasOwnProperty('Possession')) {
                obj['Possession'] = ApiClient.convertToType(data['Possession'], 'Number');
            }
            if (data.hasOwnProperty('RedCards')) {
                obj['RedCards'] = ApiClient.convertToType(data['RedCards'], 'Number');
            }
            if (data.hasOwnProperty('RoundId')) {
                obj['RoundId'] = ApiClient.convertToType(data['RoundId'], 'Number');
            }
            if (data.hasOwnProperty('Score')) {
                obj['Score'] = ApiClient.convertToType(data['Score'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('Shots')) {
                obj['Shots'] = ApiClient.convertToType(data['Shots'], 'Number');
            }
            if (data.hasOwnProperty('ShotsOnGoal')) {
                obj['ShotsOnGoal'] = ApiClient.convertToType(data['ShotsOnGoal'], 'Number');
            }
            if (data.hasOwnProperty('StatId')) {
                obj['StatId'] = ApiClient.convertToType(data['StatId'], 'Number');
            }
            if (data.hasOwnProperty('Tackles')) {
                obj['Tackles'] = ApiClient.convertToType(data['Tackles'], 'Number');
            }
            if (data.hasOwnProperty('TacklesWon')) {
                obj['TacklesWon'] = ApiClient.convertToType(data['TacklesWon'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamId')) {
                obj['TeamId'] = ApiClient.convertToType(data['TeamId'], 'Number');
            }
            if (data.hasOwnProperty('Touches')) {
                obj['Touches'] = ApiClient.convertToType(data['Touches'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('UpdatedUtc')) {
                obj['UpdatedUtc'] = ApiClient.convertToType(data['UpdatedUtc'], 'String');
            }
            if (data.hasOwnProperty('YellowCards')) {
                obj['YellowCards'] = ApiClient.convertToType(data['YellowCards'], 'Number');
            }
            if (data.hasOwnProperty('YellowRedCards')) {
                obj['YellowRedCards'] = ApiClient.convertToType(data['YellowRedCards'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamSeason</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamSeason</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }
        // ensure the json data is a string
        if (data['UpdatedUtc'] && !(typeof data['UpdatedUtc'] === 'string' || data['UpdatedUtc'] instanceof String)) {
            throw new Error("Expected the field `UpdatedUtc` to be a primitive type in the JSON string but got " + data['UpdatedUtc']);
        }

        return true;
    }


}



/**
 * @member {Number} Assists
 */
TeamSeason.prototype['Assists'] = undefined;

/**
 * @member {Number} BlockedShots
 */
TeamSeason.prototype['BlockedShots'] = undefined;

/**
 * @member {Number} CornersWon
 */
TeamSeason.prototype['CornersWon'] = undefined;

/**
 * @member {Number} Crosses
 */
TeamSeason.prototype['Crosses'] = undefined;

/**
 * @member {Number} DefenderCleanSheets
 */
TeamSeason.prototype['DefenderCleanSheets'] = undefined;

/**
 * @member {Number} FantasyPoints
 */
TeamSeason.prototype['FantasyPoints'] = undefined;

/**
 * @member {Number} FantasyPointsDraftKings
 */
TeamSeason.prototype['FantasyPointsDraftKings'] = undefined;

/**
 * @member {Number} FantasyPointsFanDuel
 */
TeamSeason.prototype['FantasyPointsFanDuel'] = undefined;

/**
 * @member {Number} FantasyPointsMondogoal
 */
TeamSeason.prototype['FantasyPointsMondogoal'] = undefined;

/**
 * @member {Number} FantasyPointsYahoo
 */
TeamSeason.prototype['FantasyPointsYahoo'] = undefined;

/**
 * @member {Number} Fouled
 */
TeamSeason.prototype['Fouled'] = undefined;

/**
 * @member {Number} Fouls
 */
TeamSeason.prototype['Fouls'] = undefined;

/**
 * @member {Number} Games
 */
TeamSeason.prototype['Games'] = undefined;

/**
 * @member {Number} GlobalTeamId
 */
TeamSeason.prototype['GlobalTeamId'] = undefined;

/**
 * @member {Number} GoalkeeperCleanSheets
 */
TeamSeason.prototype['GoalkeeperCleanSheets'] = undefined;

/**
 * @member {Number} GoalkeeperGoalsAgainst
 */
TeamSeason.prototype['GoalkeeperGoalsAgainst'] = undefined;

/**
 * @member {Number} GoalkeeperSaves
 */
TeamSeason.prototype['GoalkeeperSaves'] = undefined;

/**
 * @member {Number} GoalkeeperSingleGoalAgainst
 */
TeamSeason.prototype['GoalkeeperSingleGoalAgainst'] = undefined;

/**
 * @member {Number} GoalkeeperWins
 */
TeamSeason.prototype['GoalkeeperWins'] = undefined;

/**
 * @member {Number} Goals
 */
TeamSeason.prototype['Goals'] = undefined;

/**
 * @member {Number} Interceptions
 */
TeamSeason.prototype['Interceptions'] = undefined;

/**
 * @member {Number} LastManTackle
 */
TeamSeason.prototype['LastManTackle'] = undefined;

/**
 * @member {Number} Minutes
 */
TeamSeason.prototype['Minutes'] = undefined;

/**
 * @member {String} Name
 */
TeamSeason.prototype['Name'] = undefined;

/**
 * @member {Number} Offsides
 */
TeamSeason.prototype['Offsides'] = undefined;

/**
 * @member {Number} OpponentScore
 */
TeamSeason.prototype['OpponentScore'] = undefined;

/**
 * @member {Number} OwnGoals
 */
TeamSeason.prototype['OwnGoals'] = undefined;

/**
 * @member {Number} Passes
 */
TeamSeason.prototype['Passes'] = undefined;

/**
 * @member {Number} PassesCompleted
 */
TeamSeason.prototype['PassesCompleted'] = undefined;

/**
 * @member {Number} PenaltiesConceded
 */
TeamSeason.prototype['PenaltiesConceded'] = undefined;

/**
 * @member {Number} PenaltiesWon
 */
TeamSeason.prototype['PenaltiesWon'] = undefined;

/**
 * @member {Number} PenaltyKickGoals
 */
TeamSeason.prototype['PenaltyKickGoals'] = undefined;

/**
 * @member {Number} PenaltyKickMisses
 */
TeamSeason.prototype['PenaltyKickMisses'] = undefined;

/**
 * @member {Number} PenaltyKickSaves
 */
TeamSeason.prototype['PenaltyKickSaves'] = undefined;

/**
 * @member {Number} Possession
 */
TeamSeason.prototype['Possession'] = undefined;

/**
 * @member {Number} RedCards
 */
TeamSeason.prototype['RedCards'] = undefined;

/**
 * @member {Number} RoundId
 */
TeamSeason.prototype['RoundId'] = undefined;

/**
 * @member {Number} Score
 */
TeamSeason.prototype['Score'] = undefined;

/**
 * @member {Number} Season
 */
TeamSeason.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
TeamSeason.prototype['SeasonType'] = undefined;

/**
 * @member {Number} Shots
 */
TeamSeason.prototype['Shots'] = undefined;

/**
 * @member {Number} ShotsOnGoal
 */
TeamSeason.prototype['ShotsOnGoal'] = undefined;

/**
 * @member {Number} StatId
 */
TeamSeason.prototype['StatId'] = undefined;

/**
 * @member {Number} Tackles
 */
TeamSeason.prototype['Tackles'] = undefined;

/**
 * @member {Number} TacklesWon
 */
TeamSeason.prototype['TacklesWon'] = undefined;

/**
 * @member {String} Team
 */
TeamSeason.prototype['Team'] = undefined;

/**
 * @member {Number} TeamId
 */
TeamSeason.prototype['TeamId'] = undefined;

/**
 * @member {Number} Touches
 */
TeamSeason.prototype['Touches'] = undefined;

/**
 * @member {String} Updated
 */
TeamSeason.prototype['Updated'] = undefined;

/**
 * @member {String} UpdatedUtc
 */
TeamSeason.prototype['UpdatedUtc'] = undefined;

/**
 * @member {Number} YellowCards
 */
TeamSeason.prototype['YellowCards'] = undefined;

/**
 * @member {Number} YellowRedCards
 */
TeamSeason.prototype['YellowRedCards'] = undefined;






export default TeamSeason;

