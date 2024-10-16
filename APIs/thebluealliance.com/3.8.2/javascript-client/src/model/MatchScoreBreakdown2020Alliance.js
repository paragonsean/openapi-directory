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
 * The MatchScoreBreakdown2020Alliance model module.
 * @module model/MatchScoreBreakdown2020Alliance
 * @version 3.8.2
 */
class MatchScoreBreakdown2020Alliance {
    /**
     * Constructs a new <code>MatchScoreBreakdown2020Alliance</code>.
     * @alias module:model/MatchScoreBreakdown2020Alliance
     */
    constructor() { 
        
        MatchScoreBreakdown2020Alliance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MatchScoreBreakdown2020Alliance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MatchScoreBreakdown2020Alliance} obj Optional instance to populate.
     * @return {module:model/MatchScoreBreakdown2020Alliance} The populated <code>MatchScoreBreakdown2020Alliance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MatchScoreBreakdown2020Alliance();

            if (data.hasOwnProperty('adjustPoints')) {
                obj['adjustPoints'] = ApiClient.convertToType(data['adjustPoints'], 'Number');
            }
            if (data.hasOwnProperty('autoCellPoints')) {
                obj['autoCellPoints'] = ApiClient.convertToType(data['autoCellPoints'], 'Number');
            }
            if (data.hasOwnProperty('autoCellsBottom')) {
                obj['autoCellsBottom'] = ApiClient.convertToType(data['autoCellsBottom'], 'Number');
            }
            if (data.hasOwnProperty('autoCellsInner')) {
                obj['autoCellsInner'] = ApiClient.convertToType(data['autoCellsInner'], 'Number');
            }
            if (data.hasOwnProperty('autoCellsOuter')) {
                obj['autoCellsOuter'] = ApiClient.convertToType(data['autoCellsOuter'], 'Number');
            }
            if (data.hasOwnProperty('autoInitLinePoints')) {
                obj['autoInitLinePoints'] = ApiClient.convertToType(data['autoInitLinePoints'], 'Number');
            }
            if (data.hasOwnProperty('autoPoints')) {
                obj['autoPoints'] = ApiClient.convertToType(data['autoPoints'], 'Number');
            }
            if (data.hasOwnProperty('controlPanelPoints')) {
                obj['controlPanelPoints'] = ApiClient.convertToType(data['controlPanelPoints'], 'Number');
            }
            if (data.hasOwnProperty('endgamePoints')) {
                obj['endgamePoints'] = ApiClient.convertToType(data['endgamePoints'], 'Number');
            }
            if (data.hasOwnProperty('endgameRobot1')) {
                obj['endgameRobot1'] = ApiClient.convertToType(data['endgameRobot1'], 'String');
            }
            if (data.hasOwnProperty('endgameRobot2')) {
                obj['endgameRobot2'] = ApiClient.convertToType(data['endgameRobot2'], 'String');
            }
            if (data.hasOwnProperty('endgameRobot3')) {
                obj['endgameRobot3'] = ApiClient.convertToType(data['endgameRobot3'], 'String');
            }
            if (data.hasOwnProperty('endgameRungIsLevel')) {
                obj['endgameRungIsLevel'] = ApiClient.convertToType(data['endgameRungIsLevel'], 'String');
            }
            if (data.hasOwnProperty('foulCount')) {
                obj['foulCount'] = ApiClient.convertToType(data['foulCount'], 'Number');
            }
            if (data.hasOwnProperty('foulPoints')) {
                obj['foulPoints'] = ApiClient.convertToType(data['foulPoints'], 'Number');
            }
            if (data.hasOwnProperty('initLineRobot1')) {
                obj['initLineRobot1'] = ApiClient.convertToType(data['initLineRobot1'], 'String');
            }
            if (data.hasOwnProperty('initLineRobot2')) {
                obj['initLineRobot2'] = ApiClient.convertToType(data['initLineRobot2'], 'String');
            }
            if (data.hasOwnProperty('initLineRobot3')) {
                obj['initLineRobot3'] = ApiClient.convertToType(data['initLineRobot3'], 'String');
            }
            if (data.hasOwnProperty('rp')) {
                obj['rp'] = ApiClient.convertToType(data['rp'], 'Number');
            }
            if (data.hasOwnProperty('shieldEnergizedRankingPoint')) {
                obj['shieldEnergizedRankingPoint'] = ApiClient.convertToType(data['shieldEnergizedRankingPoint'], 'Boolean');
            }
            if (data.hasOwnProperty('shieldOperationalRankingPoint')) {
                obj['shieldOperationalRankingPoint'] = ApiClient.convertToType(data['shieldOperationalRankingPoint'], 'Boolean');
            }
            if (data.hasOwnProperty('stage1Activated')) {
                obj['stage1Activated'] = ApiClient.convertToType(data['stage1Activated'], 'Boolean');
            }
            if (data.hasOwnProperty('stage2Activated')) {
                obj['stage2Activated'] = ApiClient.convertToType(data['stage2Activated'], 'Boolean');
            }
            if (data.hasOwnProperty('stage3Activated')) {
                obj['stage3Activated'] = ApiClient.convertToType(data['stage3Activated'], 'Boolean');
            }
            if (data.hasOwnProperty('stage3TargetColor')) {
                obj['stage3TargetColor'] = ApiClient.convertToType(data['stage3TargetColor'], 'String');
            }
            if (data.hasOwnProperty('tba_numRobotsHanging')) {
                obj['tba_numRobotsHanging'] = ApiClient.convertToType(data['tba_numRobotsHanging'], 'Number');
            }
            if (data.hasOwnProperty('tba_shieldEnergizedRankingPointFromFoul')) {
                obj['tba_shieldEnergizedRankingPointFromFoul'] = ApiClient.convertToType(data['tba_shieldEnergizedRankingPointFromFoul'], 'Boolean');
            }
            if (data.hasOwnProperty('techFoulCount')) {
                obj['techFoulCount'] = ApiClient.convertToType(data['techFoulCount'], 'Number');
            }
            if (data.hasOwnProperty('teleopCellPoints')) {
                obj['teleopCellPoints'] = ApiClient.convertToType(data['teleopCellPoints'], 'Number');
            }
            if (data.hasOwnProperty('teleopCellsBottom')) {
                obj['teleopCellsBottom'] = ApiClient.convertToType(data['teleopCellsBottom'], 'Number');
            }
            if (data.hasOwnProperty('teleopCellsInner')) {
                obj['teleopCellsInner'] = ApiClient.convertToType(data['teleopCellsInner'], 'Number');
            }
            if (data.hasOwnProperty('teleopCellsOuter')) {
                obj['teleopCellsOuter'] = ApiClient.convertToType(data['teleopCellsOuter'], 'Number');
            }
            if (data.hasOwnProperty('teleopPoints')) {
                obj['teleopPoints'] = ApiClient.convertToType(data['teleopPoints'], 'Number');
            }
            if (data.hasOwnProperty('totalPoints')) {
                obj['totalPoints'] = ApiClient.convertToType(data['totalPoints'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MatchScoreBreakdown2020Alliance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MatchScoreBreakdown2020Alliance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['endgameRobot1'] && !(typeof data['endgameRobot1'] === 'string' || data['endgameRobot1'] instanceof String)) {
            throw new Error("Expected the field `endgameRobot1` to be a primitive type in the JSON string but got " + data['endgameRobot1']);
        }
        // ensure the json data is a string
        if (data['endgameRobot2'] && !(typeof data['endgameRobot2'] === 'string' || data['endgameRobot2'] instanceof String)) {
            throw new Error("Expected the field `endgameRobot2` to be a primitive type in the JSON string but got " + data['endgameRobot2']);
        }
        // ensure the json data is a string
        if (data['endgameRobot3'] && !(typeof data['endgameRobot3'] === 'string' || data['endgameRobot3'] instanceof String)) {
            throw new Error("Expected the field `endgameRobot3` to be a primitive type in the JSON string but got " + data['endgameRobot3']);
        }
        // ensure the json data is a string
        if (data['endgameRungIsLevel'] && !(typeof data['endgameRungIsLevel'] === 'string' || data['endgameRungIsLevel'] instanceof String)) {
            throw new Error("Expected the field `endgameRungIsLevel` to be a primitive type in the JSON string but got " + data['endgameRungIsLevel']);
        }
        // ensure the json data is a string
        if (data['initLineRobot1'] && !(typeof data['initLineRobot1'] === 'string' || data['initLineRobot1'] instanceof String)) {
            throw new Error("Expected the field `initLineRobot1` to be a primitive type in the JSON string but got " + data['initLineRobot1']);
        }
        // ensure the json data is a string
        if (data['initLineRobot2'] && !(typeof data['initLineRobot2'] === 'string' || data['initLineRobot2'] instanceof String)) {
            throw new Error("Expected the field `initLineRobot2` to be a primitive type in the JSON string but got " + data['initLineRobot2']);
        }
        // ensure the json data is a string
        if (data['initLineRobot3'] && !(typeof data['initLineRobot3'] === 'string' || data['initLineRobot3'] instanceof String)) {
            throw new Error("Expected the field `initLineRobot3` to be a primitive type in the JSON string but got " + data['initLineRobot3']);
        }
        // ensure the json data is a string
        if (data['stage3TargetColor'] && !(typeof data['stage3TargetColor'] === 'string' || data['stage3TargetColor'] instanceof String)) {
            throw new Error("Expected the field `stage3TargetColor` to be a primitive type in the JSON string but got " + data['stage3TargetColor']);
        }

        return true;
    }


}



/**
 * @member {Number} adjustPoints
 */
MatchScoreBreakdown2020Alliance.prototype['adjustPoints'] = undefined;

/**
 * @member {Number} autoCellPoints
 */
MatchScoreBreakdown2020Alliance.prototype['autoCellPoints'] = undefined;

/**
 * @member {Number} autoCellsBottom
 */
MatchScoreBreakdown2020Alliance.prototype['autoCellsBottom'] = undefined;

/**
 * @member {Number} autoCellsInner
 */
MatchScoreBreakdown2020Alliance.prototype['autoCellsInner'] = undefined;

/**
 * @member {Number} autoCellsOuter
 */
MatchScoreBreakdown2020Alliance.prototype['autoCellsOuter'] = undefined;

/**
 * @member {Number} autoInitLinePoints
 */
MatchScoreBreakdown2020Alliance.prototype['autoInitLinePoints'] = undefined;

/**
 * @member {Number} autoPoints
 */
MatchScoreBreakdown2020Alliance.prototype['autoPoints'] = undefined;

/**
 * @member {Number} controlPanelPoints
 */
MatchScoreBreakdown2020Alliance.prototype['controlPanelPoints'] = undefined;

/**
 * @member {Number} endgamePoints
 */
MatchScoreBreakdown2020Alliance.prototype['endgamePoints'] = undefined;

/**
 * @member {String} endgameRobot1
 */
MatchScoreBreakdown2020Alliance.prototype['endgameRobot1'] = undefined;

/**
 * @member {String} endgameRobot2
 */
MatchScoreBreakdown2020Alliance.prototype['endgameRobot2'] = undefined;

/**
 * @member {String} endgameRobot3
 */
MatchScoreBreakdown2020Alliance.prototype['endgameRobot3'] = undefined;

/**
 * @member {String} endgameRungIsLevel
 */
MatchScoreBreakdown2020Alliance.prototype['endgameRungIsLevel'] = undefined;

/**
 * @member {Number} foulCount
 */
MatchScoreBreakdown2020Alliance.prototype['foulCount'] = undefined;

/**
 * @member {Number} foulPoints
 */
MatchScoreBreakdown2020Alliance.prototype['foulPoints'] = undefined;

/**
 * @member {String} initLineRobot1
 */
MatchScoreBreakdown2020Alliance.prototype['initLineRobot1'] = undefined;

/**
 * @member {String} initLineRobot2
 */
MatchScoreBreakdown2020Alliance.prototype['initLineRobot2'] = undefined;

/**
 * @member {String} initLineRobot3
 */
MatchScoreBreakdown2020Alliance.prototype['initLineRobot3'] = undefined;

/**
 * @member {Number} rp
 */
MatchScoreBreakdown2020Alliance.prototype['rp'] = undefined;

/**
 * @member {Boolean} shieldEnergizedRankingPoint
 */
MatchScoreBreakdown2020Alliance.prototype['shieldEnergizedRankingPoint'] = undefined;

/**
 * @member {Boolean} shieldOperationalRankingPoint
 */
MatchScoreBreakdown2020Alliance.prototype['shieldOperationalRankingPoint'] = undefined;

/**
 * @member {Boolean} stage1Activated
 */
MatchScoreBreakdown2020Alliance.prototype['stage1Activated'] = undefined;

/**
 * @member {Boolean} stage2Activated
 */
MatchScoreBreakdown2020Alliance.prototype['stage2Activated'] = undefined;

/**
 * @member {Boolean} stage3Activated
 */
MatchScoreBreakdown2020Alliance.prototype['stage3Activated'] = undefined;

/**
 * @member {String} stage3TargetColor
 */
MatchScoreBreakdown2020Alliance.prototype['stage3TargetColor'] = undefined;

/**
 * Unofficial TBA-computed value that counts the number of robots who were hanging at the end of the match.
 * @member {Number} tba_numRobotsHanging
 */
MatchScoreBreakdown2020Alliance.prototype['tba_numRobotsHanging'] = undefined;

/**
 * Unofficial TBA-computed value that indicates whether the shieldEnergizedRankingPoint was earned normally or awarded due to a foul.
 * @member {Boolean} tba_shieldEnergizedRankingPointFromFoul
 */
MatchScoreBreakdown2020Alliance.prototype['tba_shieldEnergizedRankingPointFromFoul'] = undefined;

/**
 * @member {Number} techFoulCount
 */
MatchScoreBreakdown2020Alliance.prototype['techFoulCount'] = undefined;

/**
 * @member {Number} teleopCellPoints
 */
MatchScoreBreakdown2020Alliance.prototype['teleopCellPoints'] = undefined;

/**
 * @member {Number} teleopCellsBottom
 */
MatchScoreBreakdown2020Alliance.prototype['teleopCellsBottom'] = undefined;

/**
 * @member {Number} teleopCellsInner
 */
MatchScoreBreakdown2020Alliance.prototype['teleopCellsInner'] = undefined;

/**
 * @member {Number} teleopCellsOuter
 */
MatchScoreBreakdown2020Alliance.prototype['teleopCellsOuter'] = undefined;

/**
 * @member {Number} teleopPoints
 */
MatchScoreBreakdown2020Alliance.prototype['teleopPoints'] = undefined;

/**
 * @member {Number} totalPoints
 */
MatchScoreBreakdown2020Alliance.prototype['totalPoints'] = undefined;






export default MatchScoreBreakdown2020Alliance;

