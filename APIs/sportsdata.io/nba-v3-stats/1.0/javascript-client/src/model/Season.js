/**
 * NBA v3 Stats
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
 * The Season model module.
 * @module model/Season
 * @version 1.0
 */
class Season {
    /**
     * Constructs a new <code>Season</code>.
     * @alias module:model/Season
     */
    constructor() { 
        
        Season.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Season</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Season} obj Optional instance to populate.
     * @return {module:model/Season} The populated <code>Season</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Season();

            if (data.hasOwnProperty('ApiSeason')) {
                obj['ApiSeason'] = ApiClient.convertToType(data['ApiSeason'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('EndYear')) {
                obj['EndYear'] = ApiClient.convertToType(data['EndYear'], 'Number');
            }
            if (data.hasOwnProperty('PostSeasonStartDate')) {
                obj['PostSeasonStartDate'] = ApiClient.convertToType(data['PostSeasonStartDate'], 'String');
            }
            if (data.hasOwnProperty('RegularSeasonStartDate')) {
                obj['RegularSeasonStartDate'] = ApiClient.convertToType(data['RegularSeasonStartDate'], 'String');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'String');
            }
            if (data.hasOwnProperty('StartYear')) {
                obj['StartYear'] = ApiClient.convertToType(data['StartYear'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Season</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Season</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ApiSeason'] && !(typeof data['ApiSeason'] === 'string' || data['ApiSeason'] instanceof String)) {
            throw new Error("Expected the field `ApiSeason` to be a primitive type in the JSON string but got " + data['ApiSeason']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['PostSeasonStartDate'] && !(typeof data['PostSeasonStartDate'] === 'string' || data['PostSeasonStartDate'] instanceof String)) {
            throw new Error("Expected the field `PostSeasonStartDate` to be a primitive type in the JSON string but got " + data['PostSeasonStartDate']);
        }
        // ensure the json data is a string
        if (data['RegularSeasonStartDate'] && !(typeof data['RegularSeasonStartDate'] === 'string' || data['RegularSeasonStartDate'] instanceof String)) {
            throw new Error("Expected the field `RegularSeasonStartDate` to be a primitive type in the JSON string but got " + data['RegularSeasonStartDate']);
        }
        // ensure the json data is a string
        if (data['SeasonType'] && !(typeof data['SeasonType'] === 'string' || data['SeasonType'] instanceof String)) {
            throw new Error("Expected the field `SeasonType` to be a primitive type in the JSON string but got " + data['SeasonType']);
        }

        return true;
    }


}



/**
 * @member {String} ApiSeason
 */
Season.prototype['ApiSeason'] = undefined;

/**
 * @member {String} Description
 */
Season.prototype['Description'] = undefined;

/**
 * @member {Number} EndYear
 */
Season.prototype['EndYear'] = undefined;

/**
 * @member {String} PostSeasonStartDate
 */
Season.prototype['PostSeasonStartDate'] = undefined;

/**
 * @member {String} RegularSeasonStartDate
 */
Season.prototype['RegularSeasonStartDate'] = undefined;

/**
 * @member {Number} Season
 */
Season.prototype['Season'] = undefined;

/**
 * @member {String} SeasonType
 */
Season.prototype['SeasonType'] = undefined;

/**
 * @member {Number} StartYear
 */
Season.prototype['StartYear'] = undefined;






export default Season;

