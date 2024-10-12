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
 * The Stadium model module.
 * @module model/Stadium
 * @version 1.0
 */
class Stadium {
    /**
     * Constructs a new <code>Stadium</code>.
     * @alias module:model/Stadium
     */
    constructor() { 
        
        Stadium.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Stadium</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Stadium} obj Optional instance to populate.
     * @return {module:model/Stadium} The populated <code>Stadium</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Stadium();

            if (data.hasOwnProperty('Active')) {
                obj['Active'] = ApiClient.convertToType(data['Active'], 'Boolean');
            }
            if (data.hasOwnProperty('Altitude')) {
                obj['Altitude'] = ApiClient.convertToType(data['Altitude'], 'Number');
            }
            if (data.hasOwnProperty('Capacity')) {
                obj['Capacity'] = ApiClient.convertToType(data['Capacity'], 'Number');
            }
            if (data.hasOwnProperty('CenterField')) {
                obj['CenterField'] = ApiClient.convertToType(data['CenterField'], 'Number');
            }
            if (data.hasOwnProperty('City')) {
                obj['City'] = ApiClient.convertToType(data['City'], 'String');
            }
            if (data.hasOwnProperty('Country')) {
                obj['Country'] = ApiClient.convertToType(data['Country'], 'String');
            }
            if (data.hasOwnProperty('GeoLat')) {
                obj['GeoLat'] = ApiClient.convertToType(data['GeoLat'], 'Number');
            }
            if (data.hasOwnProperty('GeoLong')) {
                obj['GeoLong'] = ApiClient.convertToType(data['GeoLong'], 'Number');
            }
            if (data.hasOwnProperty('HomePlateDirection')) {
                obj['HomePlateDirection'] = ApiClient.convertToType(data['HomePlateDirection'], 'Number');
            }
            if (data.hasOwnProperty('LeftCenterField')) {
                obj['LeftCenterField'] = ApiClient.convertToType(data['LeftCenterField'], 'Number');
            }
            if (data.hasOwnProperty('LeftField')) {
                obj['LeftField'] = ApiClient.convertToType(data['LeftField'], 'Number');
            }
            if (data.hasOwnProperty('MidLeftCenterField')) {
                obj['MidLeftCenterField'] = ApiClient.convertToType(data['MidLeftCenterField'], 'Number');
            }
            if (data.hasOwnProperty('MidLeftField')) {
                obj['MidLeftField'] = ApiClient.convertToType(data['MidLeftField'], 'Number');
            }
            if (data.hasOwnProperty('MidRightCenterField')) {
                obj['MidRightCenterField'] = ApiClient.convertToType(data['MidRightCenterField'], 'Number');
            }
            if (data.hasOwnProperty('MidRightField')) {
                obj['MidRightField'] = ApiClient.convertToType(data['MidRightField'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('RightCenterField')) {
                obj['RightCenterField'] = ApiClient.convertToType(data['RightCenterField'], 'Number');
            }
            if (data.hasOwnProperty('RightField')) {
                obj['RightField'] = ApiClient.convertToType(data['RightField'], 'Number');
            }
            if (data.hasOwnProperty('StadiumID')) {
                obj['StadiumID'] = ApiClient.convertToType(data['StadiumID'], 'Number');
            }
            if (data.hasOwnProperty('State')) {
                obj['State'] = ApiClient.convertToType(data['State'], 'String');
            }
            if (data.hasOwnProperty('Surface')) {
                obj['Surface'] = ApiClient.convertToType(data['Surface'], 'String');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Stadium</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Stadium</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['City'] && !(typeof data['City'] === 'string' || data['City'] instanceof String)) {
            throw new Error("Expected the field `City` to be a primitive type in the JSON string but got " + data['City']);
        }
        // ensure the json data is a string
        if (data['Country'] && !(typeof data['Country'] === 'string' || data['Country'] instanceof String)) {
            throw new Error("Expected the field `Country` to be a primitive type in the JSON string but got " + data['Country']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['State'] && !(typeof data['State'] === 'string' || data['State'] instanceof String)) {
            throw new Error("Expected the field `State` to be a primitive type in the JSON string but got " + data['State']);
        }
        // ensure the json data is a string
        if (data['Surface'] && !(typeof data['Surface'] === 'string' || data['Surface'] instanceof String)) {
            throw new Error("Expected the field `Surface` to be a primitive type in the JSON string but got " + data['Surface']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }

        return true;
    }


}



/**
 * @member {Boolean} Active
 */
Stadium.prototype['Active'] = undefined;

/**
 * @member {Number} Altitude
 */
Stadium.prototype['Altitude'] = undefined;

/**
 * @member {Number} Capacity
 */
Stadium.prototype['Capacity'] = undefined;

/**
 * @member {Number} CenterField
 */
Stadium.prototype['CenterField'] = undefined;

/**
 * @member {String} City
 */
Stadium.prototype['City'] = undefined;

/**
 * @member {String} Country
 */
Stadium.prototype['Country'] = undefined;

/**
 * @member {Number} GeoLat
 */
Stadium.prototype['GeoLat'] = undefined;

/**
 * @member {Number} GeoLong
 */
Stadium.prototype['GeoLong'] = undefined;

/**
 * @member {Number} HomePlateDirection
 */
Stadium.prototype['HomePlateDirection'] = undefined;

/**
 * @member {Number} LeftCenterField
 */
Stadium.prototype['LeftCenterField'] = undefined;

/**
 * @member {Number} LeftField
 */
Stadium.prototype['LeftField'] = undefined;

/**
 * @member {Number} MidLeftCenterField
 */
Stadium.prototype['MidLeftCenterField'] = undefined;

/**
 * @member {Number} MidLeftField
 */
Stadium.prototype['MidLeftField'] = undefined;

/**
 * @member {Number} MidRightCenterField
 */
Stadium.prototype['MidRightCenterField'] = undefined;

/**
 * @member {Number} MidRightField
 */
Stadium.prototype['MidRightField'] = undefined;

/**
 * @member {String} Name
 */
Stadium.prototype['Name'] = undefined;

/**
 * @member {Number} RightCenterField
 */
Stadium.prototype['RightCenterField'] = undefined;

/**
 * @member {Number} RightField
 */
Stadium.prototype['RightField'] = undefined;

/**
 * @member {Number} StadiumID
 */
Stadium.prototype['StadiumID'] = undefined;

/**
 * @member {String} State
 */
Stadium.prototype['State'] = undefined;

/**
 * @member {String} Surface
 */
Stadium.prototype['Surface'] = undefined;

/**
 * @member {String} Type
 */
Stadium.prototype['Type'] = undefined;






export default Stadium;

