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
import Penalty from './Penalty';
import ScoringPlay from './ScoringPlay';

/**
 * The Period model module.
 * @module model/Period
 * @version 1.0
 */
class Period {
    /**
     * Constructs a new <code>Period</code>.
     * @alias module:model/Period
     */
    constructor() { 
        
        Period.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Period</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Period} obj Optional instance to populate.
     * @return {module:model/Period} The populated <code>Period</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Period();

            if (data.hasOwnProperty('AwayScore')) {
                obj['AwayScore'] = ApiClient.convertToType(data['AwayScore'], 'Number');
            }
            if (data.hasOwnProperty('GameID')) {
                obj['GameID'] = ApiClient.convertToType(data['GameID'], 'Number');
            }
            if (data.hasOwnProperty('HomeScore')) {
                obj['HomeScore'] = ApiClient.convertToType(data['HomeScore'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Penalties')) {
                obj['Penalties'] = ApiClient.convertToType(data['Penalties'], [Penalty]);
            }
            if (data.hasOwnProperty('PeriodID')) {
                obj['PeriodID'] = ApiClient.convertToType(data['PeriodID'], 'Number');
            }
            if (data.hasOwnProperty('ScoringPlays')) {
                obj['ScoringPlays'] = ApiClient.convertToType(data['ScoringPlays'], [ScoringPlay]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Period</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Period</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        if (data['Penalties']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Penalties'])) {
                throw new Error("Expected the field `Penalties` to be an array in the JSON data but got " + data['Penalties']);
            }
            // validate the optional field `Penalties` (array)
            for (const item of data['Penalties']) {
                Penalty.validateJSON(item);
            };
        }
        if (data['ScoringPlays']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['ScoringPlays'])) {
                throw new Error("Expected the field `ScoringPlays` to be an array in the JSON data but got " + data['ScoringPlays']);
            }
            // validate the optional field `ScoringPlays` (array)
            for (const item of data['ScoringPlays']) {
                ScoringPlay.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} AwayScore
 */
Period.prototype['AwayScore'] = undefined;

/**
 * @member {Number} GameID
 */
Period.prototype['GameID'] = undefined;

/**
 * @member {Number} HomeScore
 */
Period.prototype['HomeScore'] = undefined;

/**
 * @member {String} Name
 */
Period.prototype['Name'] = undefined;

/**
 * @member {Array.<module:model/Penalty>} Penalties
 */
Period.prototype['Penalties'] = undefined;

/**
 * @member {Number} PeriodID
 */
Period.prototype['PeriodID'] = undefined;

/**
 * @member {Array.<module:model/ScoringPlay>} ScoringPlays
 */
Period.prototype['ScoringPlays'] = undefined;






export default Period;

