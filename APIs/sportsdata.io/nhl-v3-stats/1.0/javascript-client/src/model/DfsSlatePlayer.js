/**
 * NHL v3 Stats
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
 * The DfsSlatePlayer model module.
 * @module model/DfsSlatePlayer
 * @version 1.0
 */
class DfsSlatePlayer {
    /**
     * Constructs a new <code>DfsSlatePlayer</code>.
     * @alias module:model/DfsSlatePlayer
     */
    constructor() { 
        
        DfsSlatePlayer.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DfsSlatePlayer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DfsSlatePlayer} obj Optional instance to populate.
     * @return {module:model/DfsSlatePlayer} The populated <code>DfsSlatePlayer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DfsSlatePlayer();

            if (data.hasOwnProperty('OperatorPlayerID')) {
                obj['OperatorPlayerID'] = ApiClient.convertToType(data['OperatorPlayerID'], 'String');
            }
            if (data.hasOwnProperty('OperatorPlayerName')) {
                obj['OperatorPlayerName'] = ApiClient.convertToType(data['OperatorPlayerName'], 'String');
            }
            if (data.hasOwnProperty('OperatorPosition')) {
                obj['OperatorPosition'] = ApiClient.convertToType(data['OperatorPosition'], 'String');
            }
            if (data.hasOwnProperty('OperatorRosterSlots')) {
                obj['OperatorRosterSlots'] = ApiClient.convertToType(data['OperatorRosterSlots'], ['String']);
            }
            if (data.hasOwnProperty('OperatorSalary')) {
                obj['OperatorSalary'] = ApiClient.convertToType(data['OperatorSalary'], 'Number');
            }
            if (data.hasOwnProperty('OperatorSlatePlayerID')) {
                obj['OperatorSlatePlayerID'] = ApiClient.convertToType(data['OperatorSlatePlayerID'], 'String');
            }
            if (data.hasOwnProperty('PlayerGameProjectionStatID')) {
                obj['PlayerGameProjectionStatID'] = ApiClient.convertToType(data['PlayerGameProjectionStatID'], 'Number');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('RemovedByOperator')) {
                obj['RemovedByOperator'] = ApiClient.convertToType(data['RemovedByOperator'], 'Boolean');
            }
            if (data.hasOwnProperty('SlateGameID')) {
                obj['SlateGameID'] = ApiClient.convertToType(data['SlateGameID'], 'Number');
            }
            if (data.hasOwnProperty('SlateID')) {
                obj['SlateID'] = ApiClient.convertToType(data['SlateID'], 'Number');
            }
            if (data.hasOwnProperty('SlatePlayerID')) {
                obj['SlatePlayerID'] = ApiClient.convertToType(data['SlatePlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DfsSlatePlayer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DfsSlatePlayer</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['OperatorPlayerID'] && !(typeof data['OperatorPlayerID'] === 'string' || data['OperatorPlayerID'] instanceof String)) {
            throw new Error("Expected the field `OperatorPlayerID` to be a primitive type in the JSON string but got " + data['OperatorPlayerID']);
        }
        // ensure the json data is a string
        if (data['OperatorPlayerName'] && !(typeof data['OperatorPlayerName'] === 'string' || data['OperatorPlayerName'] instanceof String)) {
            throw new Error("Expected the field `OperatorPlayerName` to be a primitive type in the JSON string but got " + data['OperatorPlayerName']);
        }
        // ensure the json data is a string
        if (data['OperatorPosition'] && !(typeof data['OperatorPosition'] === 'string' || data['OperatorPosition'] instanceof String)) {
            throw new Error("Expected the field `OperatorPosition` to be a primitive type in the JSON string but got " + data['OperatorPosition']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['OperatorRosterSlots'])) {
            throw new Error("Expected the field `OperatorRosterSlots` to be an array in the JSON data but got " + data['OperatorRosterSlots']);
        }
        // ensure the json data is a string
        if (data['OperatorSlatePlayerID'] && !(typeof data['OperatorSlatePlayerID'] === 'string' || data['OperatorSlatePlayerID'] instanceof String)) {
            throw new Error("Expected the field `OperatorSlatePlayerID` to be a primitive type in the JSON string but got " + data['OperatorSlatePlayerID']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }

        return true;
    }


}



/**
 * @member {String} OperatorPlayerID
 */
DfsSlatePlayer.prototype['OperatorPlayerID'] = undefined;

/**
 * @member {String} OperatorPlayerName
 */
DfsSlatePlayer.prototype['OperatorPlayerName'] = undefined;

/**
 * @member {String} OperatorPosition
 */
DfsSlatePlayer.prototype['OperatorPosition'] = undefined;

/**
 * @member {Array.<String>} OperatorRosterSlots
 */
DfsSlatePlayer.prototype['OperatorRosterSlots'] = undefined;

/**
 * @member {Number} OperatorSalary
 */
DfsSlatePlayer.prototype['OperatorSalary'] = undefined;

/**
 * @member {String} OperatorSlatePlayerID
 */
DfsSlatePlayer.prototype['OperatorSlatePlayerID'] = undefined;

/**
 * @member {Number} PlayerGameProjectionStatID
 */
DfsSlatePlayer.prototype['PlayerGameProjectionStatID'] = undefined;

/**
 * @member {Number} PlayerID
 */
DfsSlatePlayer.prototype['PlayerID'] = undefined;

/**
 * @member {Boolean} RemovedByOperator
 */
DfsSlatePlayer.prototype['RemovedByOperator'] = undefined;

/**
 * @member {Number} SlateGameID
 */
DfsSlatePlayer.prototype['SlateGameID'] = undefined;

/**
 * @member {Number} SlateID
 */
DfsSlatePlayer.prototype['SlateID'] = undefined;

/**
 * @member {Number} SlatePlayerID
 */
DfsSlatePlayer.prototype['SlatePlayerID'] = undefined;

/**
 * @member {String} Team
 */
DfsSlatePlayer.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
DfsSlatePlayer.prototype['TeamID'] = undefined;






export default DfsSlatePlayer;

