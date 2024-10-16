/**
 * MLB v3 Scores
 * MLB scores API.
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
 * The Inning model module.
 * @module model/Inning
 * @version 1.0
 */
class Inning {
    /**
     * Constructs a new <code>Inning</code>.
     * @alias module:model/Inning
     */
    constructor() { 
        
        Inning.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Inning</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Inning} obj Optional instance to populate.
     * @return {module:model/Inning} The populated <code>Inning</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Inning();

            if (data.hasOwnProperty('AwayTeamRuns')) {
                obj['AwayTeamRuns'] = ApiClient.convertToType(data['AwayTeamRuns'], 'Number');
            }
            if (data.hasOwnProperty('GameID')) {
                obj['GameID'] = ApiClient.convertToType(data['GameID'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamRuns')) {
                obj['HomeTeamRuns'] = ApiClient.convertToType(data['HomeTeamRuns'], 'Number');
            }
            if (data.hasOwnProperty('InningID')) {
                obj['InningID'] = ApiClient.convertToType(data['InningID'], 'Number');
            }
            if (data.hasOwnProperty('InningNumber')) {
                obj['InningNumber'] = ApiClient.convertToType(data['InningNumber'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Inning</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Inning</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} AwayTeamRuns
 */
Inning.prototype['AwayTeamRuns'] = undefined;

/**
 * @member {Number} GameID
 */
Inning.prototype['GameID'] = undefined;

/**
 * @member {Number} HomeTeamRuns
 */
Inning.prototype['HomeTeamRuns'] = undefined;

/**
 * @member {Number} InningID
 */
Inning.prototype['InningID'] = undefined;

/**
 * @member {Number} InningNumber
 */
Inning.prototype['InningNumber'] = undefined;






export default Inning;

