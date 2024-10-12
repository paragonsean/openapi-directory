/**
 * Golf v2
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
import DfsSlatePlayer from './DfsSlatePlayer';
import DfsSlateTournament from './DfsSlateTournament';

/**
 * The DfsSlate model module.
 * @module model/DfsSlate
 * @version 1.0
 */
class DfsSlate {
    /**
     * Constructs a new <code>DfsSlate</code>.
     * @alias module:model/DfsSlate
     */
    constructor() { 
        
        DfsSlate.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DfsSlate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DfsSlate} obj Optional instance to populate.
     * @return {module:model/DfsSlate} The populated <code>DfsSlate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DfsSlate();

            if (data.hasOwnProperty('DfsSlatePlayers')) {
                obj['DfsSlatePlayers'] = ApiClient.convertToType(data['DfsSlatePlayers'], [DfsSlatePlayer]);
            }
            if (data.hasOwnProperty('DfsSlateTournaments')) {
                obj['DfsSlateTournaments'] = ApiClient.convertToType(data['DfsSlateTournaments'], [DfsSlateTournament]);
            }
            if (data.hasOwnProperty('IsMultiDaySlate')) {
                obj['IsMultiDaySlate'] = ApiClient.convertToType(data['IsMultiDaySlate'], 'Boolean');
            }
            if (data.hasOwnProperty('NumberOfTournaments')) {
                obj['NumberOfTournaments'] = ApiClient.convertToType(data['NumberOfTournaments'], 'Number');
            }
            if (data.hasOwnProperty('Operator')) {
                obj['Operator'] = ApiClient.convertToType(data['Operator'], 'String');
            }
            if (data.hasOwnProperty('OperatorDay')) {
                obj['OperatorDay'] = ApiClient.convertToType(data['OperatorDay'], 'String');
            }
            if (data.hasOwnProperty('OperatorGameType')) {
                obj['OperatorGameType'] = ApiClient.convertToType(data['OperatorGameType'], 'String');
            }
            if (data.hasOwnProperty('OperatorName')) {
                obj['OperatorName'] = ApiClient.convertToType(data['OperatorName'], 'String');
            }
            if (data.hasOwnProperty('OperatorSlateID')) {
                obj['OperatorSlateID'] = ApiClient.convertToType(data['OperatorSlateID'], 'Number');
            }
            if (data.hasOwnProperty('OperatorStartTime')) {
                obj['OperatorStartTime'] = ApiClient.convertToType(data['OperatorStartTime'], 'String');
            }
            if (data.hasOwnProperty('RemovedByOperator')) {
                obj['RemovedByOperator'] = ApiClient.convertToType(data['RemovedByOperator'], 'Boolean');
            }
            if (data.hasOwnProperty('SlateID')) {
                obj['SlateID'] = ApiClient.convertToType(data['SlateID'], 'Number');
            }
            if (data.hasOwnProperty('SlateRosterSlots')) {
                obj['SlateRosterSlots'] = ApiClient.convertToType(data['SlateRosterSlots'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DfsSlate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DfsSlate</code>.
     */
    static validateJSON(data) {
        if (data['DfsSlatePlayers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['DfsSlatePlayers'])) {
                throw new Error("Expected the field `DfsSlatePlayers` to be an array in the JSON data but got " + data['DfsSlatePlayers']);
            }
            // validate the optional field `DfsSlatePlayers` (array)
            for (const item of data['DfsSlatePlayers']) {
                DfsSlatePlayer.validateJSON(item);
            };
        }
        if (data['DfsSlateTournaments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['DfsSlateTournaments'])) {
                throw new Error("Expected the field `DfsSlateTournaments` to be an array in the JSON data but got " + data['DfsSlateTournaments']);
            }
            // validate the optional field `DfsSlateTournaments` (array)
            for (const item of data['DfsSlateTournaments']) {
                DfsSlateTournament.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Operator'] && !(typeof data['Operator'] === 'string' || data['Operator'] instanceof String)) {
            throw new Error("Expected the field `Operator` to be a primitive type in the JSON string but got " + data['Operator']);
        }
        // ensure the json data is a string
        if (data['OperatorDay'] && !(typeof data['OperatorDay'] === 'string' || data['OperatorDay'] instanceof String)) {
            throw new Error("Expected the field `OperatorDay` to be a primitive type in the JSON string but got " + data['OperatorDay']);
        }
        // ensure the json data is a string
        if (data['OperatorGameType'] && !(typeof data['OperatorGameType'] === 'string' || data['OperatorGameType'] instanceof String)) {
            throw new Error("Expected the field `OperatorGameType` to be a primitive type in the JSON string but got " + data['OperatorGameType']);
        }
        // ensure the json data is a string
        if (data['OperatorName'] && !(typeof data['OperatorName'] === 'string' || data['OperatorName'] instanceof String)) {
            throw new Error("Expected the field `OperatorName` to be a primitive type in the JSON string but got " + data['OperatorName']);
        }
        // ensure the json data is a string
        if (data['OperatorStartTime'] && !(typeof data['OperatorStartTime'] === 'string' || data['OperatorStartTime'] instanceof String)) {
            throw new Error("Expected the field `OperatorStartTime` to be a primitive type in the JSON string but got " + data['OperatorStartTime']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['SlateRosterSlots'])) {
            throw new Error("Expected the field `SlateRosterSlots` to be an array in the JSON data but got " + data['SlateRosterSlots']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/DfsSlatePlayer>} DfsSlatePlayers
 */
DfsSlate.prototype['DfsSlatePlayers'] = undefined;

/**
 * @member {Array.<module:model/DfsSlateTournament>} DfsSlateTournaments
 */
DfsSlate.prototype['DfsSlateTournaments'] = undefined;

/**
 * @member {Boolean} IsMultiDaySlate
 */
DfsSlate.prototype['IsMultiDaySlate'] = undefined;

/**
 * @member {Number} NumberOfTournaments
 */
DfsSlate.prototype['NumberOfTournaments'] = undefined;

/**
 * @member {String} Operator
 */
DfsSlate.prototype['Operator'] = undefined;

/**
 * @member {String} OperatorDay
 */
DfsSlate.prototype['OperatorDay'] = undefined;

/**
 * @member {String} OperatorGameType
 */
DfsSlate.prototype['OperatorGameType'] = undefined;

/**
 * @member {String} OperatorName
 */
DfsSlate.prototype['OperatorName'] = undefined;

/**
 * @member {Number} OperatorSlateID
 */
DfsSlate.prototype['OperatorSlateID'] = undefined;

/**
 * @member {String} OperatorStartTime
 */
DfsSlate.prototype['OperatorStartTime'] = undefined;

/**
 * @member {Boolean} RemovedByOperator
 */
DfsSlate.prototype['RemovedByOperator'] = undefined;

/**
 * @member {Number} SlateID
 */
DfsSlate.prototype['SlateID'] = undefined;

/**
 * @member {Array.<String>} SlateRosterSlots
 */
DfsSlate.prototype['SlateRosterSlots'] = undefined;






export default DfsSlate;

