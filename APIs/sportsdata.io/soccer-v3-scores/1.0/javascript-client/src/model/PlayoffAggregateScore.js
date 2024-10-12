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
 * The PlayoffAggregateScore model module.
 * @module model/PlayoffAggregateScore
 * @version 1.0
 */
class PlayoffAggregateScore {
    /**
     * Constructs a new <code>PlayoffAggregateScore</code>.
     * @alias module:model/PlayoffAggregateScore
     */
    constructor() { 
        
        PlayoffAggregateScore.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlayoffAggregateScore</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayoffAggregateScore} obj Optional instance to populate.
     * @return {module:model/PlayoffAggregateScore} The populated <code>PlayoffAggregateScore</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayoffAggregateScore();

            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'String');
            }
            if (data.hasOwnProperty('TeamA_AggregateScore')) {
                obj['TeamA_AggregateScore'] = ApiClient.convertToType(data['TeamA_AggregateScore'], 'Number');
            }
            if (data.hasOwnProperty('TeamA_Id')) {
                obj['TeamA_Id'] = ApiClient.convertToType(data['TeamA_Id'], 'Number');
            }
            if (data.hasOwnProperty('TeamB_AggregateScore')) {
                obj['TeamB_AggregateScore'] = ApiClient.convertToType(data['TeamB_AggregateScore'], 'Number');
            }
            if (data.hasOwnProperty('TeamB_Id')) {
                obj['TeamB_Id'] = ApiClient.convertToType(data['TeamB_Id'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('WinningTeamId')) {
                obj['WinningTeamId'] = ApiClient.convertToType(data['WinningTeamId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayoffAggregateScore</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayoffAggregateScore</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Created'] && !(typeof data['Created'] === 'string' || data['Created'] instanceof String)) {
            throw new Error("Expected the field `Created` to be a primitive type in the JSON string but got " + data['Created']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {String} Created
 */
PlayoffAggregateScore.prototype['Created'] = undefined;

/**
 * @member {Number} TeamA_AggregateScore
 */
PlayoffAggregateScore.prototype['TeamA_AggregateScore'] = undefined;

/**
 * @member {Number} TeamA_Id
 */
PlayoffAggregateScore.prototype['TeamA_Id'] = undefined;

/**
 * @member {Number} TeamB_AggregateScore
 */
PlayoffAggregateScore.prototype['TeamB_AggregateScore'] = undefined;

/**
 * @member {Number} TeamB_Id
 */
PlayoffAggregateScore.prototype['TeamB_Id'] = undefined;

/**
 * @member {String} Updated
 */
PlayoffAggregateScore.prototype['Updated'] = undefined;

/**
 * @member {Number} WinningTeamId
 */
PlayoffAggregateScore.prototype['WinningTeamId'] = undefined;






export default PlayoffAggregateScore;

