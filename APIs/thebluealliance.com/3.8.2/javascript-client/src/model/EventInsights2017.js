/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The EventInsights2017 model module.
 * @module model/EventInsights2017
 * @version 3.8.2
 */
class EventInsights2017 {
    /**
     * Constructs a new <code>EventInsights2017</code>.
     * Insights for FIRST STEAMWORKS qualification and elimination matches.
     * @alias module:model/EventInsights2017
     * @param averageFoulScore {Number} Average foul score.
     * @param averageFuelPoints {Number} Average fuel points scored.
     * @param averageFuelPointsAuto {Number} Average fuel points scored during auto.
     * @param averageFuelPointsTeleop {Number} Average fuel points scored during teleop.
     * @param averageHighGoals {Number} Average points scored in the high goal.
     * @param averageHighGoalsAuto {Number} Average points scored in the high goal during auto.
     * @param averageHighGoalsTeleop {Number} Average points scored in the high goal during teleop.
     * @param averageLowGoals {Number} Average points scored in the low goal.
     * @param averageLowGoalsAuto {Number} Average points scored in the low goal during auto.
     * @param averageLowGoalsTeleop {Number} Average points scored in the low goal during teleop.
     * @param averageMobilityPointsAuto {Number} Average mobility points scored during auto.
     * @param averagePointsAuto {Number} Average points scored during auto.
     * @param averagePointsTeleop {Number} Average points scored during teleop.
     * @param averageRotorPoints {Number} Average rotor points scored.
     * @param averageRotorPointsAuto {Number} Average rotor points scored during auto.
     * @param averageRotorPointsTeleop {Number} Average rotor points scored during teleop.
     * @param averageScore {Number} Average score.
     * @param averageTakeoffPointsTeleop {Number} Average takeoff points scored during teleop.
     * @param averageWinMargin {Number} Average margin of victory.
     * @param averageWinScore {Number} Average winning score.
     * @param highKpa {Array.<String>} An array with three values, kPa scored, match key from the match with the high kPa, and the name of the match
     * @param highScore {Array.<String>} An array with three values, high score, match key from the match with the high score, and the name of the match
     * @param kpaAchieved {Array.<Number>} An array with three values, number of times kPa bonus achieved, number of opportunities to bonus, and percentage.
     * @param mobilityCounts {Array.<Number>} An array with three values, number of times mobility bonus achieved, number of opportunities to bonus, and percentage.
     * @param rotor1Engaged {Array.<Number>} An array with three values, number of times rotor 1 engaged, number of opportunities to engage, and percentage.
     * @param rotor1EngagedAuto {Array.<Number>} An array with three values, number of times rotor 1 engaged in auto, number of opportunities to engage in auto, and percentage.
     * @param rotor2Engaged {Array.<Number>} An array with three values, number of times rotor 2 engaged, number of opportunities to engage, and percentage.
     * @param rotor2EngagedAuto {Array.<Number>} An array with three values, number of times rotor 2 engaged in auto, number of opportunities to engage in auto, and percentage.
     * @param rotor3Engaged {Array.<Number>} An array with three values, number of times rotor 3 engaged, number of opportunities to engage, and percentage.
     * @param rotor4Engaged {Array.<Number>} An array with three values, number of times rotor 4 engaged, number of opportunities to engage, and percentage.
     * @param takeoffCounts {Array.<Number>} An array with three values, number of times takeoff was counted, number of opportunities to takeoff, and percentage.
     * @param unicornMatches {Array.<Number>} An array with three values, number of times a unicorn match (Win + kPa & Rotor Bonuses) occured, number of opportunities to have a unicorn match, and percentage.
     */
    constructor(averageFoulScore, averageFuelPoints, averageFuelPointsAuto, averageFuelPointsTeleop, averageHighGoals, averageHighGoalsAuto, averageHighGoalsTeleop, averageLowGoals, averageLowGoalsAuto, averageLowGoalsTeleop, averageMobilityPointsAuto, averagePointsAuto, averagePointsTeleop, averageRotorPoints, averageRotorPointsAuto, averageRotorPointsTeleop, averageScore, averageTakeoffPointsTeleop, averageWinMargin, averageWinScore, highKpa, highScore, kpaAchieved, mobilityCounts, rotor1Engaged, rotor1EngagedAuto, rotor2Engaged, rotor2EngagedAuto, rotor3Engaged, rotor4Engaged, takeoffCounts, unicornMatches) { 
        
        EventInsights2017.initialize(this, averageFoulScore, averageFuelPoints, averageFuelPointsAuto, averageFuelPointsTeleop, averageHighGoals, averageHighGoalsAuto, averageHighGoalsTeleop, averageLowGoals, averageLowGoalsAuto, averageLowGoalsTeleop, averageMobilityPointsAuto, averagePointsAuto, averagePointsTeleop, averageRotorPoints, averageRotorPointsAuto, averageRotorPointsTeleop, averageScore, averageTakeoffPointsTeleop, averageWinMargin, averageWinScore, highKpa, highScore, kpaAchieved, mobilityCounts, rotor1Engaged, rotor1EngagedAuto, rotor2Engaged, rotor2EngagedAuto, rotor3Engaged, rotor4Engaged, takeoffCounts, unicornMatches);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, averageFoulScore, averageFuelPoints, averageFuelPointsAuto, averageFuelPointsTeleop, averageHighGoals, averageHighGoalsAuto, averageHighGoalsTeleop, averageLowGoals, averageLowGoalsAuto, averageLowGoalsTeleop, averageMobilityPointsAuto, averagePointsAuto, averagePointsTeleop, averageRotorPoints, averageRotorPointsAuto, averageRotorPointsTeleop, averageScore, averageTakeoffPointsTeleop, averageWinMargin, averageWinScore, highKpa, highScore, kpaAchieved, mobilityCounts, rotor1Engaged, rotor1EngagedAuto, rotor2Engaged, rotor2EngagedAuto, rotor3Engaged, rotor4Engaged, takeoffCounts, unicornMatches) { 
        obj['average_foul_score'] = averageFoulScore;
        obj['average_fuel_points'] = averageFuelPoints;
        obj['average_fuel_points_auto'] = averageFuelPointsAuto;
        obj['average_fuel_points_teleop'] = averageFuelPointsTeleop;
        obj['average_high_goals'] = averageHighGoals;
        obj['average_high_goals_auto'] = averageHighGoalsAuto;
        obj['average_high_goals_teleop'] = averageHighGoalsTeleop;
        obj['average_low_goals'] = averageLowGoals;
        obj['average_low_goals_auto'] = averageLowGoalsAuto;
        obj['average_low_goals_teleop'] = averageLowGoalsTeleop;
        obj['average_mobility_points_auto'] = averageMobilityPointsAuto;
        obj['average_points_auto'] = averagePointsAuto;
        obj['average_points_teleop'] = averagePointsTeleop;
        obj['average_rotor_points'] = averageRotorPoints;
        obj['average_rotor_points_auto'] = averageRotorPointsAuto;
        obj['average_rotor_points_teleop'] = averageRotorPointsTeleop;
        obj['average_score'] = averageScore;
        obj['average_takeoff_points_teleop'] = averageTakeoffPointsTeleop;
        obj['average_win_margin'] = averageWinMargin;
        obj['average_win_score'] = averageWinScore;
        obj['high_kpa'] = highKpa;
        obj['high_score'] = highScore;
        obj['kpa_achieved'] = kpaAchieved;
        obj['mobility_counts'] = mobilityCounts;
        obj['rotor_1_engaged'] = rotor1Engaged;
        obj['rotor_1_engaged_auto'] = rotor1EngagedAuto;
        obj['rotor_2_engaged'] = rotor2Engaged;
        obj['rotor_2_engaged_auto'] = rotor2EngagedAuto;
        obj['rotor_3_engaged'] = rotor3Engaged;
        obj['rotor_4_engaged'] = rotor4Engaged;
        obj['takeoff_counts'] = takeoffCounts;
        obj['unicorn_matches'] = unicornMatches;
    }

    /**
     * Constructs a <code>EventInsights2017</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventInsights2017} obj Optional instance to populate.
     * @return {module:model/EventInsights2017} The populated <code>EventInsights2017</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventInsights2017();

            if (data.hasOwnProperty('average_foul_score')) {
                obj['average_foul_score'] = ApiClient.convertToType(data['average_foul_score'], 'Number');
            }
            if (data.hasOwnProperty('average_fuel_points')) {
                obj['average_fuel_points'] = ApiClient.convertToType(data['average_fuel_points'], 'Number');
            }
            if (data.hasOwnProperty('average_fuel_points_auto')) {
                obj['average_fuel_points_auto'] = ApiClient.convertToType(data['average_fuel_points_auto'], 'Number');
            }
            if (data.hasOwnProperty('average_fuel_points_teleop')) {
                obj['average_fuel_points_teleop'] = ApiClient.convertToType(data['average_fuel_points_teleop'], 'Number');
            }
            if (data.hasOwnProperty('average_high_goals')) {
                obj['average_high_goals'] = ApiClient.convertToType(data['average_high_goals'], 'Number');
            }
            if (data.hasOwnProperty('average_high_goals_auto')) {
                obj['average_high_goals_auto'] = ApiClient.convertToType(data['average_high_goals_auto'], 'Number');
            }
            if (data.hasOwnProperty('average_high_goals_teleop')) {
                obj['average_high_goals_teleop'] = ApiClient.convertToType(data['average_high_goals_teleop'], 'Number');
            }
            if (data.hasOwnProperty('average_low_goals')) {
                obj['average_low_goals'] = ApiClient.convertToType(data['average_low_goals'], 'Number');
            }
            if (data.hasOwnProperty('average_low_goals_auto')) {
                obj['average_low_goals_auto'] = ApiClient.convertToType(data['average_low_goals_auto'], 'Number');
            }
            if (data.hasOwnProperty('average_low_goals_teleop')) {
                obj['average_low_goals_teleop'] = ApiClient.convertToType(data['average_low_goals_teleop'], 'Number');
            }
            if (data.hasOwnProperty('average_mobility_points_auto')) {
                obj['average_mobility_points_auto'] = ApiClient.convertToType(data['average_mobility_points_auto'], 'Number');
            }
            if (data.hasOwnProperty('average_points_auto')) {
                obj['average_points_auto'] = ApiClient.convertToType(data['average_points_auto'], 'Number');
            }
            if (data.hasOwnProperty('average_points_teleop')) {
                obj['average_points_teleop'] = ApiClient.convertToType(data['average_points_teleop'], 'Number');
            }
            if (data.hasOwnProperty('average_rotor_points')) {
                obj['average_rotor_points'] = ApiClient.convertToType(data['average_rotor_points'], 'Number');
            }
            if (data.hasOwnProperty('average_rotor_points_auto')) {
                obj['average_rotor_points_auto'] = ApiClient.convertToType(data['average_rotor_points_auto'], 'Number');
            }
            if (data.hasOwnProperty('average_rotor_points_teleop')) {
                obj['average_rotor_points_teleop'] = ApiClient.convertToType(data['average_rotor_points_teleop'], 'Number');
            }
            if (data.hasOwnProperty('average_score')) {
                obj['average_score'] = ApiClient.convertToType(data['average_score'], 'Number');
            }
            if (data.hasOwnProperty('average_takeoff_points_teleop')) {
                obj['average_takeoff_points_teleop'] = ApiClient.convertToType(data['average_takeoff_points_teleop'], 'Number');
            }
            if (data.hasOwnProperty('average_win_margin')) {
                obj['average_win_margin'] = ApiClient.convertToType(data['average_win_margin'], 'Number');
            }
            if (data.hasOwnProperty('average_win_score')) {
                obj['average_win_score'] = ApiClient.convertToType(data['average_win_score'], 'Number');
            }
            if (data.hasOwnProperty('high_kpa')) {
                obj['high_kpa'] = ApiClient.convertToType(data['high_kpa'], ['String']);
            }
            if (data.hasOwnProperty('high_score')) {
                obj['high_score'] = ApiClient.convertToType(data['high_score'], ['String']);
            }
            if (data.hasOwnProperty('kpa_achieved')) {
                obj['kpa_achieved'] = ApiClient.convertToType(data['kpa_achieved'], ['Number']);
            }
            if (data.hasOwnProperty('mobility_counts')) {
                obj['mobility_counts'] = ApiClient.convertToType(data['mobility_counts'], ['Number']);
            }
            if (data.hasOwnProperty('rotor_1_engaged')) {
                obj['rotor_1_engaged'] = ApiClient.convertToType(data['rotor_1_engaged'], ['Number']);
            }
            if (data.hasOwnProperty('rotor_1_engaged_auto')) {
                obj['rotor_1_engaged_auto'] = ApiClient.convertToType(data['rotor_1_engaged_auto'], ['Number']);
            }
            if (data.hasOwnProperty('rotor_2_engaged')) {
                obj['rotor_2_engaged'] = ApiClient.convertToType(data['rotor_2_engaged'], ['Number']);
            }
            if (data.hasOwnProperty('rotor_2_engaged_auto')) {
                obj['rotor_2_engaged_auto'] = ApiClient.convertToType(data['rotor_2_engaged_auto'], ['Number']);
            }
            if (data.hasOwnProperty('rotor_3_engaged')) {
                obj['rotor_3_engaged'] = ApiClient.convertToType(data['rotor_3_engaged'], ['Number']);
            }
            if (data.hasOwnProperty('rotor_4_engaged')) {
                obj['rotor_4_engaged'] = ApiClient.convertToType(data['rotor_4_engaged'], ['Number']);
            }
            if (data.hasOwnProperty('takeoff_counts')) {
                obj['takeoff_counts'] = ApiClient.convertToType(data['takeoff_counts'], ['Number']);
            }
            if (data.hasOwnProperty('unicorn_matches')) {
                obj['unicorn_matches'] = ApiClient.convertToType(data['unicorn_matches'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventInsights2017</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventInsights2017</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EventInsights2017.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['high_kpa'])) {
            throw new Error("Expected the field `high_kpa` to be an array in the JSON data but got " + data['high_kpa']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['high_score'])) {
            throw new Error("Expected the field `high_score` to be an array in the JSON data but got " + data['high_score']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['kpa_achieved'])) {
            throw new Error("Expected the field `kpa_achieved` to be an array in the JSON data but got " + data['kpa_achieved']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['mobility_counts'])) {
            throw new Error("Expected the field `mobility_counts` to be an array in the JSON data but got " + data['mobility_counts']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rotor_1_engaged'])) {
            throw new Error("Expected the field `rotor_1_engaged` to be an array in the JSON data but got " + data['rotor_1_engaged']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rotor_1_engaged_auto'])) {
            throw new Error("Expected the field `rotor_1_engaged_auto` to be an array in the JSON data but got " + data['rotor_1_engaged_auto']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rotor_2_engaged'])) {
            throw new Error("Expected the field `rotor_2_engaged` to be an array in the JSON data but got " + data['rotor_2_engaged']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rotor_2_engaged_auto'])) {
            throw new Error("Expected the field `rotor_2_engaged_auto` to be an array in the JSON data but got " + data['rotor_2_engaged_auto']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rotor_3_engaged'])) {
            throw new Error("Expected the field `rotor_3_engaged` to be an array in the JSON data but got " + data['rotor_3_engaged']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rotor_4_engaged'])) {
            throw new Error("Expected the field `rotor_4_engaged` to be an array in the JSON data but got " + data['rotor_4_engaged']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['takeoff_counts'])) {
            throw new Error("Expected the field `takeoff_counts` to be an array in the JSON data but got " + data['takeoff_counts']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['unicorn_matches'])) {
            throw new Error("Expected the field `unicorn_matches` to be an array in the JSON data but got " + data['unicorn_matches']);
        }

        return true;
    }


}

EventInsights2017.RequiredProperties = ["average_foul_score", "average_fuel_points", "average_fuel_points_auto", "average_fuel_points_teleop", "average_high_goals", "average_high_goals_auto", "average_high_goals_teleop", "average_low_goals", "average_low_goals_auto", "average_low_goals_teleop", "average_mobility_points_auto", "average_points_auto", "average_points_teleop", "average_rotor_points", "average_rotor_points_auto", "average_rotor_points_teleop", "average_score", "average_takeoff_points_teleop", "average_win_margin", "average_win_score", "high_kpa", "high_score", "kpa_achieved", "mobility_counts", "rotor_1_engaged", "rotor_1_engaged_auto", "rotor_2_engaged", "rotor_2_engaged_auto", "rotor_3_engaged", "rotor_4_engaged", "takeoff_counts", "unicorn_matches"];

/**
 * Average foul score.
 * @member {Number} average_foul_score
 */
EventInsights2017.prototype['average_foul_score'] = undefined;

/**
 * Average fuel points scored.
 * @member {Number} average_fuel_points
 */
EventInsights2017.prototype['average_fuel_points'] = undefined;

/**
 * Average fuel points scored during auto.
 * @member {Number} average_fuel_points_auto
 */
EventInsights2017.prototype['average_fuel_points_auto'] = undefined;

/**
 * Average fuel points scored during teleop.
 * @member {Number} average_fuel_points_teleop
 */
EventInsights2017.prototype['average_fuel_points_teleop'] = undefined;

/**
 * Average points scored in the high goal.
 * @member {Number} average_high_goals
 */
EventInsights2017.prototype['average_high_goals'] = undefined;

/**
 * Average points scored in the high goal during auto.
 * @member {Number} average_high_goals_auto
 */
EventInsights2017.prototype['average_high_goals_auto'] = undefined;

/**
 * Average points scored in the high goal during teleop.
 * @member {Number} average_high_goals_teleop
 */
EventInsights2017.prototype['average_high_goals_teleop'] = undefined;

/**
 * Average points scored in the low goal.
 * @member {Number} average_low_goals
 */
EventInsights2017.prototype['average_low_goals'] = undefined;

/**
 * Average points scored in the low goal during auto.
 * @member {Number} average_low_goals_auto
 */
EventInsights2017.prototype['average_low_goals_auto'] = undefined;

/**
 * Average points scored in the low goal during teleop.
 * @member {Number} average_low_goals_teleop
 */
EventInsights2017.prototype['average_low_goals_teleop'] = undefined;

/**
 * Average mobility points scored during auto.
 * @member {Number} average_mobility_points_auto
 */
EventInsights2017.prototype['average_mobility_points_auto'] = undefined;

/**
 * Average points scored during auto.
 * @member {Number} average_points_auto
 */
EventInsights2017.prototype['average_points_auto'] = undefined;

/**
 * Average points scored during teleop.
 * @member {Number} average_points_teleop
 */
EventInsights2017.prototype['average_points_teleop'] = undefined;

/**
 * Average rotor points scored.
 * @member {Number} average_rotor_points
 */
EventInsights2017.prototype['average_rotor_points'] = undefined;

/**
 * Average rotor points scored during auto.
 * @member {Number} average_rotor_points_auto
 */
EventInsights2017.prototype['average_rotor_points_auto'] = undefined;

/**
 * Average rotor points scored during teleop.
 * @member {Number} average_rotor_points_teleop
 */
EventInsights2017.prototype['average_rotor_points_teleop'] = undefined;

/**
 * Average score.
 * @member {Number} average_score
 */
EventInsights2017.prototype['average_score'] = undefined;

/**
 * Average takeoff points scored during teleop.
 * @member {Number} average_takeoff_points_teleop
 */
EventInsights2017.prototype['average_takeoff_points_teleop'] = undefined;

/**
 * Average margin of victory.
 * @member {Number} average_win_margin
 */
EventInsights2017.prototype['average_win_margin'] = undefined;

/**
 * Average winning score.
 * @member {Number} average_win_score
 */
EventInsights2017.prototype['average_win_score'] = undefined;

/**
 * An array with three values, kPa scored, match key from the match with the high kPa, and the name of the match
 * @member {Array.<String>} high_kpa
 */
EventInsights2017.prototype['high_kpa'] = undefined;

/**
 * An array with three values, high score, match key from the match with the high score, and the name of the match
 * @member {Array.<String>} high_score
 */
EventInsights2017.prototype['high_score'] = undefined;

/**
 * An array with three values, number of times kPa bonus achieved, number of opportunities to bonus, and percentage.
 * @member {Array.<Number>} kpa_achieved
 */
EventInsights2017.prototype['kpa_achieved'] = undefined;

/**
 * An array with three values, number of times mobility bonus achieved, number of opportunities to bonus, and percentage.
 * @member {Array.<Number>} mobility_counts
 */
EventInsights2017.prototype['mobility_counts'] = undefined;

/**
 * An array with three values, number of times rotor 1 engaged, number of opportunities to engage, and percentage.
 * @member {Array.<Number>} rotor_1_engaged
 */
EventInsights2017.prototype['rotor_1_engaged'] = undefined;

/**
 * An array with three values, number of times rotor 1 engaged in auto, number of opportunities to engage in auto, and percentage.
 * @member {Array.<Number>} rotor_1_engaged_auto
 */
EventInsights2017.prototype['rotor_1_engaged_auto'] = undefined;

/**
 * An array with three values, number of times rotor 2 engaged, number of opportunities to engage, and percentage.
 * @member {Array.<Number>} rotor_2_engaged
 */
EventInsights2017.prototype['rotor_2_engaged'] = undefined;

/**
 * An array with three values, number of times rotor 2 engaged in auto, number of opportunities to engage in auto, and percentage.
 * @member {Array.<Number>} rotor_2_engaged_auto
 */
EventInsights2017.prototype['rotor_2_engaged_auto'] = undefined;

/**
 * An array with three values, number of times rotor 3 engaged, number of opportunities to engage, and percentage.
 * @member {Array.<Number>} rotor_3_engaged
 */
EventInsights2017.prototype['rotor_3_engaged'] = undefined;

/**
 * An array with three values, number of times rotor 4 engaged, number of opportunities to engage, and percentage.
 * @member {Array.<Number>} rotor_4_engaged
 */
EventInsights2017.prototype['rotor_4_engaged'] = undefined;

/**
 * An array with three values, number of times takeoff was counted, number of opportunities to takeoff, and percentage.
 * @member {Array.<Number>} takeoff_counts
 */
EventInsights2017.prototype['takeoff_counts'] = undefined;

/**
 * An array with three values, number of times a unicorn match (Win + kPa & Rotor Bonuses) occured, number of opportunities to have a unicorn match, and percentage.
 * @member {Array.<Number>} unicorn_matches
 */
EventInsights2017.prototype['unicorn_matches'] = undefined;






export default EventInsights2017;

