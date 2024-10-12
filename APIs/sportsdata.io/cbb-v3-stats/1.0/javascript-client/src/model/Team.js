/**
 * CBB v3 Stats
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
import Stadium from './Stadium';

/**
 * The Team model module.
 * @module model/Team
 * @version 1.0
 */
class Team {
    /**
     * Constructs a new <code>Team</code>.
     * @alias module:model/Team
     */
    constructor() { 
        
        Team.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Team</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Team} obj Optional instance to populate.
     * @return {module:model/Team} The populated <code>Team</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Team();

            if (data.hasOwnProperty('Active')) {
                obj['Active'] = ApiClient.convertToType(data['Active'], 'Boolean');
            }
            if (data.hasOwnProperty('ApRank')) {
                obj['ApRank'] = ApiClient.convertToType(data['ApRank'], 'Number');
            }
            if (data.hasOwnProperty('Conference')) {
                obj['Conference'] = ApiClient.convertToType(data['Conference'], 'String');
            }
            if (data.hasOwnProperty('ConferenceID')) {
                obj['ConferenceID'] = ApiClient.convertToType(data['ConferenceID'], 'Number');
            }
            if (data.hasOwnProperty('ConferenceLosses')) {
                obj['ConferenceLosses'] = ApiClient.convertToType(data['ConferenceLosses'], 'Number');
            }
            if (data.hasOwnProperty('ConferenceWins')) {
                obj['ConferenceWins'] = ApiClient.convertToType(data['ConferenceWins'], 'Number');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('Key')) {
                obj['Key'] = ApiClient.convertToType(data['Key'], 'String');
            }
            if (data.hasOwnProperty('Losses')) {
                obj['Losses'] = ApiClient.convertToType(data['Losses'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('School')) {
                obj['School'] = ApiClient.convertToType(data['School'], 'String');
            }
            if (data.hasOwnProperty('ShortDisplayName')) {
                obj['ShortDisplayName'] = ApiClient.convertToType(data['ShortDisplayName'], 'String');
            }
            if (data.hasOwnProperty('Stadium')) {
                obj['Stadium'] = Stadium.constructFromObject(data['Stadium']);
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('TeamLogoUrl')) {
                obj['TeamLogoUrl'] = ApiClient.convertToType(data['TeamLogoUrl'], 'String');
            }
            if (data.hasOwnProperty('Wins')) {
                obj['Wins'] = ApiClient.convertToType(data['Wins'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Team</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Team</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Conference'] && !(typeof data['Conference'] === 'string' || data['Conference'] instanceof String)) {
            throw new Error("Expected the field `Conference` to be a primitive type in the JSON string but got " + data['Conference']);
        }
        // ensure the json data is a string
        if (data['Key'] && !(typeof data['Key'] === 'string' || data['Key'] instanceof String)) {
            throw new Error("Expected the field `Key` to be a primitive type in the JSON string but got " + data['Key']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['School'] && !(typeof data['School'] === 'string' || data['School'] instanceof String)) {
            throw new Error("Expected the field `School` to be a primitive type in the JSON string but got " + data['School']);
        }
        // ensure the json data is a string
        if (data['ShortDisplayName'] && !(typeof data['ShortDisplayName'] === 'string' || data['ShortDisplayName'] instanceof String)) {
            throw new Error("Expected the field `ShortDisplayName` to be a primitive type in the JSON string but got " + data['ShortDisplayName']);
        }
        // validate the optional field `Stadium`
        if (data['Stadium']) { // data not null
          Stadium.validateJSON(data['Stadium']);
        }
        // ensure the json data is a string
        if (data['TeamLogoUrl'] && !(typeof data['TeamLogoUrl'] === 'string' || data['TeamLogoUrl'] instanceof String)) {
            throw new Error("Expected the field `TeamLogoUrl` to be a primitive type in the JSON string but got " + data['TeamLogoUrl']);
        }

        return true;
    }


}



/**
 * @member {Boolean} Active
 */
Team.prototype['Active'] = undefined;

/**
 * @member {Number} ApRank
 */
Team.prototype['ApRank'] = undefined;

/**
 * @member {String} Conference
 */
Team.prototype['Conference'] = undefined;

/**
 * @member {Number} ConferenceID
 */
Team.prototype['ConferenceID'] = undefined;

/**
 * @member {Number} ConferenceLosses
 */
Team.prototype['ConferenceLosses'] = undefined;

/**
 * @member {Number} ConferenceWins
 */
Team.prototype['ConferenceWins'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
Team.prototype['GlobalTeamID'] = undefined;

/**
 * @member {String} Key
 */
Team.prototype['Key'] = undefined;

/**
 * @member {Number} Losses
 */
Team.prototype['Losses'] = undefined;

/**
 * @member {String} Name
 */
Team.prototype['Name'] = undefined;

/**
 * @member {String} School
 */
Team.prototype['School'] = undefined;

/**
 * @member {String} ShortDisplayName
 */
Team.prototype['ShortDisplayName'] = undefined;

/**
 * @member {module:model/Stadium} Stadium
 */
Team.prototype['Stadium'] = undefined;

/**
 * @member {Number} TeamID
 */
Team.prototype['TeamID'] = undefined;

/**
 * @member {String} TeamLogoUrl
 */
Team.prototype['TeamLogoUrl'] = undefined;

/**
 * @member {Number} Wins
 */
Team.prototype['Wins'] = undefined;






export default Team;

