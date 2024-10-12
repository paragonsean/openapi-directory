/**
 * NFL v3 Projections
 * NFL projected stats API.
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
import Schedule from './Schedule';

/**
 * The DfsSlateGame model module.
 * @module model/DfsSlateGame
 * @version 1.0
 */
class DfsSlateGame {
    /**
     * Constructs a new <code>DfsSlateGame</code>.
     * @alias module:model/DfsSlateGame
     */
    constructor() { 
        
        DfsSlateGame.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DfsSlateGame</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DfsSlateGame} obj Optional instance to populate.
     * @return {module:model/DfsSlateGame} The populated <code>DfsSlateGame</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DfsSlateGame();

            if (data.hasOwnProperty('Game')) {
                obj['Game'] = Schedule.constructFromObject(data['Game']);
            }
            if (data.hasOwnProperty('GameID')) {
                obj['GameID'] = ApiClient.convertToType(data['GameID'], 'Number');
            }
            if (data.hasOwnProperty('OperatorGameID')) {
                obj['OperatorGameID'] = ApiClient.convertToType(data['OperatorGameID'], 'Number');
            }
            if (data.hasOwnProperty('RemovedByOperator')) {
                obj['RemovedByOperator'] = ApiClient.convertToType(data['RemovedByOperator'], 'Boolean');
            }
            if (data.hasOwnProperty('ScoreID')) {
                obj['ScoreID'] = ApiClient.convertToType(data['ScoreID'], 'Number');
            }
            if (data.hasOwnProperty('SlateGameID')) {
                obj['SlateGameID'] = ApiClient.convertToType(data['SlateGameID'], 'Number');
            }
            if (data.hasOwnProperty('SlateID')) {
                obj['SlateID'] = ApiClient.convertToType(data['SlateID'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DfsSlateGame</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DfsSlateGame</code>.
     */
    static validateJSON(data) {
        // validate the optional field `Game`
        if (data['Game']) { // data not null
          Schedule.validateJSON(data['Game']);
        }

        return true;
    }


}



/**
 * @member {module:model/Schedule} Game
 */
DfsSlateGame.prototype['Game'] = undefined;

/**
 * @member {Number} GameID
 */
DfsSlateGame.prototype['GameID'] = undefined;

/**
 * @member {Number} OperatorGameID
 */
DfsSlateGame.prototype['OperatorGameID'] = undefined;

/**
 * @member {Boolean} RemovedByOperator
 */
DfsSlateGame.prototype['RemovedByOperator'] = undefined;

/**
 * @member {Number} ScoreID
 */
DfsSlateGame.prototype['ScoreID'] = undefined;

/**
 * @member {Number} SlateGameID
 */
DfsSlateGame.prototype['SlateGameID'] = undefined;

/**
 * @member {Number} SlateID
 */
DfsSlateGame.prototype['SlateID'] = undefined;






export default DfsSlateGame;

