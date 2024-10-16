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
 * The PlayerOwnership model module.
 * @module model/PlayerOwnership
 * @version 1.0
 */
class PlayerOwnership {
    /**
     * Constructs a new <code>PlayerOwnership</code>.
     * @alias module:model/PlayerOwnership
     */
    constructor() { 
        
        PlayerOwnership.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlayerOwnership</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayerOwnership} obj Optional instance to populate.
     * @return {module:model/PlayerOwnership} The populated <code>PlayerOwnership</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayerOwnership();

            if (data.hasOwnProperty('DeltaOwnershipPercentage')) {
                obj['DeltaOwnershipPercentage'] = ApiClient.convertToType(data['DeltaOwnershipPercentage'], 'Number');
            }
            if (data.hasOwnProperty('DeltaStartPercentage')) {
                obj['DeltaStartPercentage'] = ApiClient.convertToType(data['DeltaStartPercentage'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('OwnershipPercentage')) {
                obj['OwnershipPercentage'] = ApiClient.convertToType(data['OwnershipPercentage'], 'Number');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'String');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('StartPercentage')) {
                obj['StartPercentage'] = ApiClient.convertToType(data['StartPercentage'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('Week')) {
                obj['Week'] = ApiClient.convertToType(data['Week'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayerOwnership</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayerOwnership</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Position'] && !(typeof data['Position'] === 'string' || data['Position'] instanceof String)) {
            throw new Error("Expected the field `Position` to be a primitive type in the JSON string but got " + data['Position']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }

        return true;
    }


}



/**
 * @member {Number} DeltaOwnershipPercentage
 */
PlayerOwnership.prototype['DeltaOwnershipPercentage'] = undefined;

/**
 * @member {Number} DeltaStartPercentage
 */
PlayerOwnership.prototype['DeltaStartPercentage'] = undefined;

/**
 * @member {String} Name
 */
PlayerOwnership.prototype['Name'] = undefined;

/**
 * @member {Number} OwnershipPercentage
 */
PlayerOwnership.prototype['OwnershipPercentage'] = undefined;

/**
 * @member {Number} PlayerID
 */
PlayerOwnership.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
PlayerOwnership.prototype['Position'] = undefined;

/**
 * @member {Number} Season
 */
PlayerOwnership.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
PlayerOwnership.prototype['SeasonType'] = undefined;

/**
 * @member {Number} StartPercentage
 */
PlayerOwnership.prototype['StartPercentage'] = undefined;

/**
 * @member {String} Team
 */
PlayerOwnership.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
PlayerOwnership.prototype['TeamID'] = undefined;

/**
 * @member {Number} Week
 */
PlayerOwnership.prototype['Week'] = undefined;






export default PlayerOwnership;

