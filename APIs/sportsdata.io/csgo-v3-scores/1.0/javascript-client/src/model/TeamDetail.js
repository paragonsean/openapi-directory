/**
 * CS:GO v3 Scores
 * CS:GO v3 Scores
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
import Player from './Player';

/**
 * The TeamDetail model module.
 * @module model/TeamDetail
 * @version 1.0
 */
class TeamDetail {
    /**
     * Constructs a new <code>TeamDetail</code>.
     * @alias module:model/TeamDetail
     */
    constructor() { 
        
        TeamDetail.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TeamDetail</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamDetail} obj Optional instance to populate.
     * @return {module:model/TeamDetail} The populated <code>TeamDetail</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamDetail();

            if (data.hasOwnProperty('Active')) {
                obj['Active'] = ApiClient.convertToType(data['Active'], 'Boolean');
            }
            if (data.hasOwnProperty('AreaId')) {
                obj['AreaId'] = ApiClient.convertToType(data['AreaId'], 'Number');
            }
            if (data.hasOwnProperty('AreaName')) {
                obj['AreaName'] = ApiClient.convertToType(data['AreaName'], 'String');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('Facebook')) {
                obj['Facebook'] = ApiClient.convertToType(data['Facebook'], 'String');
            }
            if (data.hasOwnProperty('Founded')) {
                obj['Founded'] = ApiClient.convertToType(data['Founded'], 'Number');
            }
            if (data.hasOwnProperty('Gender')) {
                obj['Gender'] = ApiClient.convertToType(data['Gender'], 'String');
            }
            if (data.hasOwnProperty('Instagram')) {
                obj['Instagram'] = ApiClient.convertToType(data['Instagram'], 'String');
            }
            if (data.hasOwnProperty('Key')) {
                obj['Key'] = ApiClient.convertToType(data['Key'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Players')) {
                obj['Players'] = ApiClient.convertToType(data['Players'], [Player]);
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
            if (data.hasOwnProperty('ShortName')) {
                obj['ShortName'] = ApiClient.convertToType(data['ShortName'], 'String');
            }
            if (data.hasOwnProperty('TeamId')) {
                obj['TeamId'] = ApiClient.convertToType(data['TeamId'], 'Number');
            }
            if (data.hasOwnProperty('TertiaryColor')) {
                obj['TertiaryColor'] = ApiClient.convertToType(data['TertiaryColor'], 'String');
            }
            if (data.hasOwnProperty('Twitter')) {
                obj['Twitter'] = ApiClient.convertToType(data['Twitter'], 'String');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
            if (data.hasOwnProperty('Website')) {
                obj['Website'] = ApiClient.convertToType(data['Website'], 'String');
            }
            if (data.hasOwnProperty('YouTube')) {
                obj['YouTube'] = ApiClient.convertToType(data['YouTube'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamDetail</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamDetail</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AreaName'] && !(typeof data['AreaName'] === 'string' || data['AreaName'] instanceof String)) {
            throw new Error("Expected the field `AreaName` to be a primitive type in the JSON string but got " + data['AreaName']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['Facebook'] && !(typeof data['Facebook'] === 'string' || data['Facebook'] instanceof String)) {
            throw new Error("Expected the field `Facebook` to be a primitive type in the JSON string but got " + data['Facebook']);
        }
        // ensure the json data is a string
        if (data['Gender'] && !(typeof data['Gender'] === 'string' || data['Gender'] instanceof String)) {
            throw new Error("Expected the field `Gender` to be a primitive type in the JSON string but got " + data['Gender']);
        }
        // ensure the json data is a string
        if (data['Instagram'] && !(typeof data['Instagram'] === 'string' || data['Instagram'] instanceof String)) {
            throw new Error("Expected the field `Instagram` to be a primitive type in the JSON string but got " + data['Instagram']);
        }
        // ensure the json data is a string
        if (data['Key'] && !(typeof data['Key'] === 'string' || data['Key'] instanceof String)) {
            throw new Error("Expected the field `Key` to be a primitive type in the JSON string but got " + data['Key']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        if (data['Players']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Players'])) {
                throw new Error("Expected the field `Players` to be an array in the JSON data but got " + data['Players']);
            }
            // validate the optional field `Players` (array)
            for (const item of data['Players']) {
                Player.validateJSON(item);
            };
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
        if (data['ShortName'] && !(typeof data['ShortName'] === 'string' || data['ShortName'] instanceof String)) {
            throw new Error("Expected the field `ShortName` to be a primitive type in the JSON string but got " + data['ShortName']);
        }
        // ensure the json data is a string
        if (data['TertiaryColor'] && !(typeof data['TertiaryColor'] === 'string' || data['TertiaryColor'] instanceof String)) {
            throw new Error("Expected the field `TertiaryColor` to be a primitive type in the JSON string but got " + data['TertiaryColor']);
        }
        // ensure the json data is a string
        if (data['Twitter'] && !(typeof data['Twitter'] === 'string' || data['Twitter'] instanceof String)) {
            throw new Error("Expected the field `Twitter` to be a primitive type in the JSON string but got " + data['Twitter']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }
        // ensure the json data is a string
        if (data['Website'] && !(typeof data['Website'] === 'string' || data['Website'] instanceof String)) {
            throw new Error("Expected the field `Website` to be a primitive type in the JSON string but got " + data['Website']);
        }
        // ensure the json data is a string
        if (data['YouTube'] && !(typeof data['YouTube'] === 'string' || data['YouTube'] instanceof String)) {
            throw new Error("Expected the field `YouTube` to be a primitive type in the JSON string but got " + data['YouTube']);
        }

        return true;
    }


}



/**
 * @member {Boolean} Active
 */
TeamDetail.prototype['Active'] = undefined;

/**
 * @member {Number} AreaId
 */
TeamDetail.prototype['AreaId'] = undefined;

/**
 * @member {String} AreaName
 */
TeamDetail.prototype['AreaName'] = undefined;

/**
 * @member {String} Email
 */
TeamDetail.prototype['Email'] = undefined;

/**
 * @member {String} Facebook
 */
TeamDetail.prototype['Facebook'] = undefined;

/**
 * @member {Number} Founded
 */
TeamDetail.prototype['Founded'] = undefined;

/**
 * @member {String} Gender
 */
TeamDetail.prototype['Gender'] = undefined;

/**
 * @member {String} Instagram
 */
TeamDetail.prototype['Instagram'] = undefined;

/**
 * @member {String} Key
 */
TeamDetail.prototype['Key'] = undefined;

/**
 * @member {String} Name
 */
TeamDetail.prototype['Name'] = undefined;

/**
 * @member {Array.<module:model/Player>} Players
 */
TeamDetail.prototype['Players'] = undefined;

/**
 * @member {String} PrimaryColor
 */
TeamDetail.prototype['PrimaryColor'] = undefined;

/**
 * @member {String} QuaternaryColor
 */
TeamDetail.prototype['QuaternaryColor'] = undefined;

/**
 * @member {String} SecondaryColor
 */
TeamDetail.prototype['SecondaryColor'] = undefined;

/**
 * @member {String} ShortName
 */
TeamDetail.prototype['ShortName'] = undefined;

/**
 * @member {Number} TeamId
 */
TeamDetail.prototype['TeamId'] = undefined;

/**
 * @member {String} TertiaryColor
 */
TeamDetail.prototype['TertiaryColor'] = undefined;

/**
 * @member {String} Twitter
 */
TeamDetail.prototype['Twitter'] = undefined;

/**
 * @member {String} Type
 */
TeamDetail.prototype['Type'] = undefined;

/**
 * @member {String} Website
 */
TeamDetail.prototype['Website'] = undefined;

/**
 * @member {String} YouTube
 */
TeamDetail.prototype['YouTube'] = undefined;






export default TeamDetail;

