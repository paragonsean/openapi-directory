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
 * The TeamRobot model module.
 * @module model/TeamRobot
 * @version 3.8.2
 */
class TeamRobot {
    /**
     * Constructs a new <code>TeamRobot</code>.
     * @alias module:model/TeamRobot
     * @param key {String} Internal TBA identifier for this robot.
     * @param robotName {String} Name of the robot as provided by the team.
     * @param teamKey {String} TBA team key for this robot.
     * @param year {Number} Year this robot competed in.
     */
    constructor(key, robotName, teamKey, year) { 
        
        TeamRobot.initialize(this, key, robotName, teamKey, year);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, key, robotName, teamKey, year) { 
        obj['key'] = key;
        obj['robot_name'] = robotName;
        obj['team_key'] = teamKey;
        obj['year'] = year;
    }

    /**
     * Constructs a <code>TeamRobot</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamRobot} obj Optional instance to populate.
     * @return {module:model/TeamRobot} The populated <code>TeamRobot</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamRobot();

            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('robot_name')) {
                obj['robot_name'] = ApiClient.convertToType(data['robot_name'], 'String');
            }
            if (data.hasOwnProperty('team_key')) {
                obj['team_key'] = ApiClient.convertToType(data['team_key'], 'String');
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamRobot</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamRobot</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TeamRobot.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }
        // ensure the json data is a string
        if (data['robot_name'] && !(typeof data['robot_name'] === 'string' || data['robot_name'] instanceof String)) {
            throw new Error("Expected the field `robot_name` to be a primitive type in the JSON string but got " + data['robot_name']);
        }
        // ensure the json data is a string
        if (data['team_key'] && !(typeof data['team_key'] === 'string' || data['team_key'] instanceof String)) {
            throw new Error("Expected the field `team_key` to be a primitive type in the JSON string but got " + data['team_key']);
        }

        return true;
    }


}

TeamRobot.RequiredProperties = ["key", "robot_name", "team_key", "year"];

/**
 * Internal TBA identifier for this robot.
 * @member {String} key
 */
TeamRobot.prototype['key'] = undefined;

/**
 * Name of the robot as provided by the team.
 * @member {String} robot_name
 */
TeamRobot.prototype['robot_name'] = undefined;

/**
 * TBA team key for this robot.
 * @member {String} team_key
 */
TeamRobot.prototype['team_key'] = undefined;

/**
 * Year this robot competed in.
 * @member {Number} year
 */
TeamRobot.prototype['year'] = undefined;






export default TeamRobot;

