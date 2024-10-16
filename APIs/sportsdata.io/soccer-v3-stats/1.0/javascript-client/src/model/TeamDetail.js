/**
 * Soccer v3 Stats
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
            if (data.hasOwnProperty('Address')) {
                obj['Address'] = ApiClient.convertToType(data['Address'], 'String');
            }
            if (data.hasOwnProperty('AreaId')) {
                obj['AreaId'] = ApiClient.convertToType(data['AreaId'], 'Number');
            }
            if (data.hasOwnProperty('AreaName')) {
                obj['AreaName'] = ApiClient.convertToType(data['AreaName'], 'String');
            }
            if (data.hasOwnProperty('City')) {
                obj['City'] = ApiClient.convertToType(data['City'], 'String');
            }
            if (data.hasOwnProperty('ClubColor1')) {
                obj['ClubColor1'] = ApiClient.convertToType(data['ClubColor1'], 'String');
            }
            if (data.hasOwnProperty('ClubColor2')) {
                obj['ClubColor2'] = ApiClient.convertToType(data['ClubColor2'], 'String');
            }
            if (data.hasOwnProperty('ClubColor3')) {
                obj['ClubColor3'] = ApiClient.convertToType(data['ClubColor3'], 'String');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('Fax')) {
                obj['Fax'] = ApiClient.convertToType(data['Fax'], 'String');
            }
            if (data.hasOwnProperty('Founded')) {
                obj['Founded'] = ApiClient.convertToType(data['Founded'], 'Number');
            }
            if (data.hasOwnProperty('FullName')) {
                obj['FullName'] = ApiClient.convertToType(data['FullName'], 'String');
            }
            if (data.hasOwnProperty('Gender')) {
                obj['Gender'] = ApiClient.convertToType(data['Gender'], 'String');
            }
            if (data.hasOwnProperty('GlobalTeamId')) {
                obj['GlobalTeamId'] = ApiClient.convertToType(data['GlobalTeamId'], 'Number');
            }
            if (data.hasOwnProperty('Key')) {
                obj['Key'] = ApiClient.convertToType(data['Key'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Nickname1')) {
                obj['Nickname1'] = ApiClient.convertToType(data['Nickname1'], 'String');
            }
            if (data.hasOwnProperty('Nickname2')) {
                obj['Nickname2'] = ApiClient.convertToType(data['Nickname2'], 'String');
            }
            if (data.hasOwnProperty('Nickname3')) {
                obj['Nickname3'] = ApiClient.convertToType(data['Nickname3'], 'String');
            }
            if (data.hasOwnProperty('Phone')) {
                obj['Phone'] = ApiClient.convertToType(data['Phone'], 'String');
            }
            if (data.hasOwnProperty('Players')) {
                obj['Players'] = ApiClient.convertToType(data['Players'], [Player]);
            }
            if (data.hasOwnProperty('TeamId')) {
                obj['TeamId'] = ApiClient.convertToType(data['TeamId'], 'Number');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
            if (data.hasOwnProperty('VenueId')) {
                obj['VenueId'] = ApiClient.convertToType(data['VenueId'], 'Number');
            }
            if (data.hasOwnProperty('VenueName')) {
                obj['VenueName'] = ApiClient.convertToType(data['VenueName'], 'String');
            }
            if (data.hasOwnProperty('Website')) {
                obj['Website'] = ApiClient.convertToType(data['Website'], 'String');
            }
            if (data.hasOwnProperty('WikipediaLogoUrl')) {
                obj['WikipediaLogoUrl'] = ApiClient.convertToType(data['WikipediaLogoUrl'], 'String');
            }
            if (data.hasOwnProperty('WikipediaWordMarkUrl')) {
                obj['WikipediaWordMarkUrl'] = ApiClient.convertToType(data['WikipediaWordMarkUrl'], 'String');
            }
            if (data.hasOwnProperty('Zip')) {
                obj['Zip'] = ApiClient.convertToType(data['Zip'], 'String');
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
        if (data['Address'] && !(typeof data['Address'] === 'string' || data['Address'] instanceof String)) {
            throw new Error("Expected the field `Address` to be a primitive type in the JSON string but got " + data['Address']);
        }
        // ensure the json data is a string
        if (data['AreaName'] && !(typeof data['AreaName'] === 'string' || data['AreaName'] instanceof String)) {
            throw new Error("Expected the field `AreaName` to be a primitive type in the JSON string but got " + data['AreaName']);
        }
        // ensure the json data is a string
        if (data['City'] && !(typeof data['City'] === 'string' || data['City'] instanceof String)) {
            throw new Error("Expected the field `City` to be a primitive type in the JSON string but got " + data['City']);
        }
        // ensure the json data is a string
        if (data['ClubColor1'] && !(typeof data['ClubColor1'] === 'string' || data['ClubColor1'] instanceof String)) {
            throw new Error("Expected the field `ClubColor1` to be a primitive type in the JSON string but got " + data['ClubColor1']);
        }
        // ensure the json data is a string
        if (data['ClubColor2'] && !(typeof data['ClubColor2'] === 'string' || data['ClubColor2'] instanceof String)) {
            throw new Error("Expected the field `ClubColor2` to be a primitive type in the JSON string but got " + data['ClubColor2']);
        }
        // ensure the json data is a string
        if (data['ClubColor3'] && !(typeof data['ClubColor3'] === 'string' || data['ClubColor3'] instanceof String)) {
            throw new Error("Expected the field `ClubColor3` to be a primitive type in the JSON string but got " + data['ClubColor3']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['Fax'] && !(typeof data['Fax'] === 'string' || data['Fax'] instanceof String)) {
            throw new Error("Expected the field `Fax` to be a primitive type in the JSON string but got " + data['Fax']);
        }
        // ensure the json data is a string
        if (data['FullName'] && !(typeof data['FullName'] === 'string' || data['FullName'] instanceof String)) {
            throw new Error("Expected the field `FullName` to be a primitive type in the JSON string but got " + data['FullName']);
        }
        // ensure the json data is a string
        if (data['Gender'] && !(typeof data['Gender'] === 'string' || data['Gender'] instanceof String)) {
            throw new Error("Expected the field `Gender` to be a primitive type in the JSON string but got " + data['Gender']);
        }
        // ensure the json data is a string
        if (data['Key'] && !(typeof data['Key'] === 'string' || data['Key'] instanceof String)) {
            throw new Error("Expected the field `Key` to be a primitive type in the JSON string but got " + data['Key']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Nickname1'] && !(typeof data['Nickname1'] === 'string' || data['Nickname1'] instanceof String)) {
            throw new Error("Expected the field `Nickname1` to be a primitive type in the JSON string but got " + data['Nickname1']);
        }
        // ensure the json data is a string
        if (data['Nickname2'] && !(typeof data['Nickname2'] === 'string' || data['Nickname2'] instanceof String)) {
            throw new Error("Expected the field `Nickname2` to be a primitive type in the JSON string but got " + data['Nickname2']);
        }
        // ensure the json data is a string
        if (data['Nickname3'] && !(typeof data['Nickname3'] === 'string' || data['Nickname3'] instanceof String)) {
            throw new Error("Expected the field `Nickname3` to be a primitive type in the JSON string but got " + data['Nickname3']);
        }
        // ensure the json data is a string
        if (data['Phone'] && !(typeof data['Phone'] === 'string' || data['Phone'] instanceof String)) {
            throw new Error("Expected the field `Phone` to be a primitive type in the JSON string but got " + data['Phone']);
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
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }
        // ensure the json data is a string
        if (data['VenueName'] && !(typeof data['VenueName'] === 'string' || data['VenueName'] instanceof String)) {
            throw new Error("Expected the field `VenueName` to be a primitive type in the JSON string but got " + data['VenueName']);
        }
        // ensure the json data is a string
        if (data['Website'] && !(typeof data['Website'] === 'string' || data['Website'] instanceof String)) {
            throw new Error("Expected the field `Website` to be a primitive type in the JSON string but got " + data['Website']);
        }
        // ensure the json data is a string
        if (data['WikipediaLogoUrl'] && !(typeof data['WikipediaLogoUrl'] === 'string' || data['WikipediaLogoUrl'] instanceof String)) {
            throw new Error("Expected the field `WikipediaLogoUrl` to be a primitive type in the JSON string but got " + data['WikipediaLogoUrl']);
        }
        // ensure the json data is a string
        if (data['WikipediaWordMarkUrl'] && !(typeof data['WikipediaWordMarkUrl'] === 'string' || data['WikipediaWordMarkUrl'] instanceof String)) {
            throw new Error("Expected the field `WikipediaWordMarkUrl` to be a primitive type in the JSON string but got " + data['WikipediaWordMarkUrl']);
        }
        // ensure the json data is a string
        if (data['Zip'] && !(typeof data['Zip'] === 'string' || data['Zip'] instanceof String)) {
            throw new Error("Expected the field `Zip` to be a primitive type in the JSON string but got " + data['Zip']);
        }

        return true;
    }


}



/**
 * @member {Boolean} Active
 */
TeamDetail.prototype['Active'] = undefined;

/**
 * @member {String} Address
 */
TeamDetail.prototype['Address'] = undefined;

/**
 * @member {Number} AreaId
 */
TeamDetail.prototype['AreaId'] = undefined;

/**
 * @member {String} AreaName
 */
TeamDetail.prototype['AreaName'] = undefined;

/**
 * @member {String} City
 */
TeamDetail.prototype['City'] = undefined;

/**
 * @member {String} ClubColor1
 */
TeamDetail.prototype['ClubColor1'] = undefined;

/**
 * @member {String} ClubColor2
 */
TeamDetail.prototype['ClubColor2'] = undefined;

/**
 * @member {String} ClubColor3
 */
TeamDetail.prototype['ClubColor3'] = undefined;

/**
 * @member {String} Email
 */
TeamDetail.prototype['Email'] = undefined;

/**
 * @member {String} Fax
 */
TeamDetail.prototype['Fax'] = undefined;

/**
 * @member {Number} Founded
 */
TeamDetail.prototype['Founded'] = undefined;

/**
 * @member {String} FullName
 */
TeamDetail.prototype['FullName'] = undefined;

/**
 * @member {String} Gender
 */
TeamDetail.prototype['Gender'] = undefined;

/**
 * @member {Number} GlobalTeamId
 */
TeamDetail.prototype['GlobalTeamId'] = undefined;

/**
 * @member {String} Key
 */
TeamDetail.prototype['Key'] = undefined;

/**
 * @member {String} Name
 */
TeamDetail.prototype['Name'] = undefined;

/**
 * @member {String} Nickname1
 */
TeamDetail.prototype['Nickname1'] = undefined;

/**
 * @member {String} Nickname2
 */
TeamDetail.prototype['Nickname2'] = undefined;

/**
 * @member {String} Nickname3
 */
TeamDetail.prototype['Nickname3'] = undefined;

/**
 * @member {String} Phone
 */
TeamDetail.prototype['Phone'] = undefined;

/**
 * @member {Array.<module:model/Player>} Players
 */
TeamDetail.prototype['Players'] = undefined;

/**
 * @member {Number} TeamId
 */
TeamDetail.prototype['TeamId'] = undefined;

/**
 * @member {String} Type
 */
TeamDetail.prototype['Type'] = undefined;

/**
 * @member {Number} VenueId
 */
TeamDetail.prototype['VenueId'] = undefined;

/**
 * @member {String} VenueName
 */
TeamDetail.prototype['VenueName'] = undefined;

/**
 * @member {String} Website
 */
TeamDetail.prototype['Website'] = undefined;

/**
 * @member {String} WikipediaLogoUrl
 */
TeamDetail.prototype['WikipediaLogoUrl'] = undefined;

/**
 * @member {String} WikipediaWordMarkUrl
 */
TeamDetail.prototype['WikipediaWordMarkUrl'] = undefined;

/**
 * @member {String} Zip
 */
TeamDetail.prototype['Zip'] = undefined;






export default TeamDetail;

