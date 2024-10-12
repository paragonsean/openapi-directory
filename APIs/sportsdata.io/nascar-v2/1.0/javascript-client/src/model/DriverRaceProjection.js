/**
 * NASCAR v2
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
 * The DriverRaceProjection model module.
 * @module model/DriverRaceProjection
 * @version 1.0
 */
class DriverRaceProjection {
    /**
     * Constructs a new <code>DriverRaceProjection</code>.
     * @alias module:model/DriverRaceProjection
     */
    constructor() { 
        
        DriverRaceProjection.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DriverRaceProjection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DriverRaceProjection} obj Optional instance to populate.
     * @return {module:model/DriverRaceProjection} The populated <code>DriverRaceProjection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DriverRaceProjection();

            if (data.hasOwnProperty('Bonus')) {
                obj['Bonus'] = ApiClient.convertToType(data['Bonus'], 'Number');
            }
            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'String');
            }
            if (data.hasOwnProperty('CurrentPosition')) {
                obj['CurrentPosition'] = ApiClient.convertToType(data['CurrentPosition'], 'Number');
            }
            if (data.hasOwnProperty('DateTime')) {
                obj['DateTime'] = ApiClient.convertToType(data['DateTime'], 'String');
            }
            if (data.hasOwnProperty('Day')) {
                obj['Day'] = ApiClient.convertToType(data['Day'], 'String');
            }
            if (data.hasOwnProperty('DraftKingsSalary')) {
                obj['DraftKingsSalary'] = ApiClient.convertToType(data['DraftKingsSalary'], 'Number');
            }
            if (data.hasOwnProperty('DriverID')) {
                obj['DriverID'] = ApiClient.convertToType(data['DriverID'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPoints')) {
                obj['FantasyPoints'] = ApiClient.convertToType(data['FantasyPoints'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPointsDraftKings')) {
                obj['FantasyPointsDraftKings'] = ApiClient.convertToType(data['FantasyPointsDraftKings'], 'Number');
            }
            if (data.hasOwnProperty('FastestLaps')) {
                obj['FastestLaps'] = ApiClient.convertToType(data['FastestLaps'], 'Number');
            }
            if (data.hasOwnProperty('FinalPosition')) {
                obj['FinalPosition'] = ApiClient.convertToType(data['FinalPosition'], 'Number');
            }
            if (data.hasOwnProperty('Laps')) {
                obj['Laps'] = ApiClient.convertToType(data['Laps'], 'Number');
            }
            if (data.hasOwnProperty('LapsLed')) {
                obj['LapsLed'] = ApiClient.convertToType(data['LapsLed'], 'Number');
            }
            if (data.hasOwnProperty('Manufacturer')) {
                obj['Manufacturer'] = ApiClient.convertToType(data['Manufacturer'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'Number');
            }
            if (data.hasOwnProperty('NumberDisplay')) {
                obj['NumberDisplay'] = ApiClient.convertToType(data['NumberDisplay'], 'String');
            }
            if (data.hasOwnProperty('Penalty')) {
                obj['Penalty'] = ApiClient.convertToType(data['Penalty'], 'Number');
            }
            if (data.hasOwnProperty('Points')) {
                obj['Points'] = ApiClient.convertToType(data['Points'], 'Number');
            }
            if (data.hasOwnProperty('PoleFinalPosition')) {
                obj['PoleFinalPosition'] = ApiClient.convertToType(data['PoleFinalPosition'], 'Number');
            }
            if (data.hasOwnProperty('Poles')) {
                obj['Poles'] = ApiClient.convertToType(data['Poles'], 'Number');
            }
            if (data.hasOwnProperty('PositionDifferential')) {
                obj['PositionDifferential'] = ApiClient.convertToType(data['PositionDifferential'], 'Number');
            }
            if (data.hasOwnProperty('QualifyingSpeed')) {
                obj['QualifyingSpeed'] = ApiClient.convertToType(data['QualifyingSpeed'], 'Number');
            }
            if (data.hasOwnProperty('RaceID')) {
                obj['RaceID'] = ApiClient.convertToType(data['RaceID'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('StartPosition')) {
                obj['StartPosition'] = ApiClient.convertToType(data['StartPosition'], 'Number');
            }
            if (data.hasOwnProperty('StatID')) {
                obj['StatID'] = ApiClient.convertToType(data['StatID'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('Wins')) {
                obj['Wins'] = ApiClient.convertToType(data['Wins'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DriverRaceProjection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DriverRaceProjection</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Created'] && !(typeof data['Created'] === 'string' || data['Created'] instanceof String)) {
            throw new Error("Expected the field `Created` to be a primitive type in the JSON string but got " + data['Created']);
        }
        // ensure the json data is a string
        if (data['DateTime'] && !(typeof data['DateTime'] === 'string' || data['DateTime'] instanceof String)) {
            throw new Error("Expected the field `DateTime` to be a primitive type in the JSON string but got " + data['DateTime']);
        }
        // ensure the json data is a string
        if (data['Day'] && !(typeof data['Day'] === 'string' || data['Day'] instanceof String)) {
            throw new Error("Expected the field `Day` to be a primitive type in the JSON string but got " + data['Day']);
        }
        // ensure the json data is a string
        if (data['Manufacturer'] && !(typeof data['Manufacturer'] === 'string' || data['Manufacturer'] instanceof String)) {
            throw new Error("Expected the field `Manufacturer` to be a primitive type in the JSON string but got " + data['Manufacturer']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['NumberDisplay'] && !(typeof data['NumberDisplay'] === 'string' || data['NumberDisplay'] instanceof String)) {
            throw new Error("Expected the field `NumberDisplay` to be a primitive type in the JSON string but got " + data['NumberDisplay']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {Number} Bonus
 */
DriverRaceProjection.prototype['Bonus'] = undefined;

/**
 * @member {String} Created
 */
DriverRaceProjection.prototype['Created'] = undefined;

/**
 * @member {Number} CurrentPosition
 */
DriverRaceProjection.prototype['CurrentPosition'] = undefined;

/**
 * @member {String} DateTime
 */
DriverRaceProjection.prototype['DateTime'] = undefined;

/**
 * @member {String} Day
 */
DriverRaceProjection.prototype['Day'] = undefined;

/**
 * @member {Number} DraftKingsSalary
 */
DriverRaceProjection.prototype['DraftKingsSalary'] = undefined;

/**
 * @member {Number} DriverID
 */
DriverRaceProjection.prototype['DriverID'] = undefined;

/**
 * @member {Number} FantasyPoints
 */
DriverRaceProjection.prototype['FantasyPoints'] = undefined;

/**
 * @member {Number} FantasyPointsDraftKings
 */
DriverRaceProjection.prototype['FantasyPointsDraftKings'] = undefined;

/**
 * @member {Number} FastestLaps
 */
DriverRaceProjection.prototype['FastestLaps'] = undefined;

/**
 * @member {Number} FinalPosition
 */
DriverRaceProjection.prototype['FinalPosition'] = undefined;

/**
 * @member {Number} Laps
 */
DriverRaceProjection.prototype['Laps'] = undefined;

/**
 * @member {Number} LapsLed
 */
DriverRaceProjection.prototype['LapsLed'] = undefined;

/**
 * @member {String} Manufacturer
 */
DriverRaceProjection.prototype['Manufacturer'] = undefined;

/**
 * @member {String} Name
 */
DriverRaceProjection.prototype['Name'] = undefined;

/**
 * @member {Number} Number
 */
DriverRaceProjection.prototype['Number'] = undefined;

/**
 * @member {String} NumberDisplay
 */
DriverRaceProjection.prototype['NumberDisplay'] = undefined;

/**
 * @member {Number} Penalty
 */
DriverRaceProjection.prototype['Penalty'] = undefined;

/**
 * @member {Number} Points
 */
DriverRaceProjection.prototype['Points'] = undefined;

/**
 * @member {Number} PoleFinalPosition
 */
DriverRaceProjection.prototype['PoleFinalPosition'] = undefined;

/**
 * @member {Number} Poles
 */
DriverRaceProjection.prototype['Poles'] = undefined;

/**
 * @member {Number} PositionDifferential
 */
DriverRaceProjection.prototype['PositionDifferential'] = undefined;

/**
 * @member {Number} QualifyingSpeed
 */
DriverRaceProjection.prototype['QualifyingSpeed'] = undefined;

/**
 * @member {Number} RaceID
 */
DriverRaceProjection.prototype['RaceID'] = undefined;

/**
 * @member {Number} Season
 */
DriverRaceProjection.prototype['Season'] = undefined;

/**
 * @member {Number} StartPosition
 */
DriverRaceProjection.prototype['StartPosition'] = undefined;

/**
 * @member {Number} StatID
 */
DriverRaceProjection.prototype['StatID'] = undefined;

/**
 * @member {String} Updated
 */
DriverRaceProjection.prototype['Updated'] = undefined;

/**
 * @member {Number} Wins
 */
DriverRaceProjection.prototype['Wins'] = undefined;






export default DriverRaceProjection;

