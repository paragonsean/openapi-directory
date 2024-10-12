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
            if (data.hasOwnProperty('City')) {
                obj['City'] = ApiClient.convertToType(data['City'], 'String');
            }
            if (data.hasOwnProperty('Division')) {
                obj['Division'] = ApiClient.convertToType(data['Division'], 'String');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('Key')) {
                obj['Key'] = ApiClient.convertToType(data['Key'], 'String');
            }
            if (data.hasOwnProperty('League')) {
                obj['League'] = ApiClient.convertToType(data['League'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('PrimaryColor')) {
                obj['PrimaryColor'] = ApiClient.convertToType(data['PrimaryColor'], 'String');
            }
            if (data.hasOwnProperty('QuaternaryColor')) {
                obj['QuaternaryColor'] = ApiClient.convertToType(data['QuaternaryColor'], 'String');
            }
            if (data.hasOwnProperty('SecondaryColor')) {
                obj['SecondaryColor'] = ApiClient.convertToType(data['SecondaryColor'], 'String');
            }
            if (data.hasOwnProperty('StadiumID')) {
                obj['StadiumID'] = ApiClient.convertToType(data['StadiumID'], 'Number');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('TertiaryColor')) {
                obj['TertiaryColor'] = ApiClient.convertToType(data['TertiaryColor'], 'String');
            }
            if (data.hasOwnProperty('WikipediaLogoUrl')) {
                obj['WikipediaLogoUrl'] = ApiClient.convertToType(data['WikipediaLogoUrl'], 'String');
            }
            if (data.hasOwnProperty('WikipediaWordMarkUrl')) {
                obj['WikipediaWordMarkUrl'] = ApiClient.convertToType(data['WikipediaWordMarkUrl'], 'String');
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
        if (data['City'] && !(typeof data['City'] === 'string' || data['City'] instanceof String)) {
            throw new Error("Expected the field `City` to be a primitive type in the JSON string but got " + data['City']);
        }
        // ensure the json data is a string
        if (data['Division'] && !(typeof data['Division'] === 'string' || data['Division'] instanceof String)) {
            throw new Error("Expected the field `Division` to be a primitive type in the JSON string but got " + data['Division']);
        }
        // ensure the json data is a string
        if (data['Key'] && !(typeof data['Key'] === 'string' || data['Key'] instanceof String)) {
            throw new Error("Expected the field `Key` to be a primitive type in the JSON string but got " + data['Key']);
        }
        // ensure the json data is a string
        if (data['League'] && !(typeof data['League'] === 'string' || data['League'] instanceof String)) {
            throw new Error("Expected the field `League` to be a primitive type in the JSON string but got " + data['League']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['PrimaryColor'] && !(typeof data['PrimaryColor'] === 'string' || data['PrimaryColor'] instanceof String)) {
            throw new Error("Expected the field `PrimaryColor` to be a primitive type in the JSON string but got " + data['PrimaryColor']);
        }
        // ensure the json data is a string
        if (data['QuaternaryColor'] && !(typeof data['QuaternaryColor'] === 'string' || data['QuaternaryColor'] instanceof String)) {
            throw new Error("Expected the field `QuaternaryColor` to be a primitive type in the JSON string but got " + data['QuaternaryColor']);
        }
        // ensure the json data is a string
        if (data['SecondaryColor'] && !(typeof data['SecondaryColor'] === 'string' || data['SecondaryColor'] instanceof String)) {
            throw new Error("Expected the field `SecondaryColor` to be a primitive type in the JSON string but got " + data['SecondaryColor']);
        }
        // ensure the json data is a string
        if (data['TertiaryColor'] && !(typeof data['TertiaryColor'] === 'string' || data['TertiaryColor'] instanceof String)) {
            throw new Error("Expected the field `TertiaryColor` to be a primitive type in the JSON string but got " + data['TertiaryColor']);
        }
        // ensure the json data is a string
        if (data['WikipediaLogoUrl'] && !(typeof data['WikipediaLogoUrl'] === 'string' || data['WikipediaLogoUrl'] instanceof String)) {
            throw new Error("Expected the field `WikipediaLogoUrl` to be a primitive type in the JSON string but got " + data['WikipediaLogoUrl']);
        }
        // ensure the json data is a string
        if (data['WikipediaWordMarkUrl'] && !(typeof data['WikipediaWordMarkUrl'] === 'string' || data['WikipediaWordMarkUrl'] instanceof String)) {
            throw new Error("Expected the field `WikipediaWordMarkUrl` to be a primitive type in the JSON string but got " + data['WikipediaWordMarkUrl']);
        }

        return true;
    }


}



/**
 * @member {Boolean} Active
 */
Team.prototype['Active'] = undefined;

/**
 * @member {String} City
 */
Team.prototype['City'] = undefined;

/**
 * @member {String} Division
 */
Team.prototype['Division'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
Team.prototype['GlobalTeamID'] = undefined;

/**
 * @member {String} Key
 */
Team.prototype['Key'] = undefined;

/**
 * @member {String} League
 */
Team.prototype['League'] = undefined;

/**
 * @member {String} Name
 */
Team.prototype['Name'] = undefined;

/**
 * @member {String} PrimaryColor
 */
Team.prototype['PrimaryColor'] = undefined;

/**
 * @member {String} QuaternaryColor
 */
Team.prototype['QuaternaryColor'] = undefined;

/**
 * @member {String} SecondaryColor
 */
Team.prototype['SecondaryColor'] = undefined;

/**
 * @member {Number} StadiumID
 */
Team.prototype['StadiumID'] = undefined;

/**
 * @member {Number} TeamID
 */
Team.prototype['TeamID'] = undefined;

/**
 * @member {String} TertiaryColor
 */
Team.prototype['TertiaryColor'] = undefined;

/**
 * @member {String} WikipediaLogoUrl
 */
Team.prototype['WikipediaLogoUrl'] = undefined;

/**
 * @member {String} WikipediaWordMarkUrl
 */
Team.prototype['WikipediaWordMarkUrl'] = undefined;






export default Team;

