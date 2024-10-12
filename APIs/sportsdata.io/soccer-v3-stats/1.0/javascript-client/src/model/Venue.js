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

/**
 * The Venue model module.
 * @module model/Venue
 * @version 1.0
 */
class Venue {
    /**
     * Constructs a new <code>Venue</code>.
     * @alias module:model/Venue
     */
    constructor() { 
        
        Venue.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Venue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Venue} obj Optional instance to populate.
     * @return {module:model/Venue} The populated <code>Venue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Venue();

            if (data.hasOwnProperty('Address')) {
                obj['Address'] = ApiClient.convertToType(data['Address'], 'String');
            }
            if (data.hasOwnProperty('Capacity')) {
                obj['Capacity'] = ApiClient.convertToType(data['Capacity'], 'Number');
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
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Nickname1')) {
                obj['Nickname1'] = ApiClient.convertToType(data['Nickname1'], 'String');
            }
            if (data.hasOwnProperty('Nickname2')) {
                obj['Nickname2'] = ApiClient.convertToType(data['Nickname2'], 'String');
            }
            if (data.hasOwnProperty('Open')) {
                obj['Open'] = ApiClient.convertToType(data['Open'], 'Boolean');
            }
            if (data.hasOwnProperty('Opened')) {
                obj['Opened'] = ApiClient.convertToType(data['Opened'], 'Number');
            }
            if (data.hasOwnProperty('Surface')) {
                obj['Surface'] = ApiClient.convertToType(data['Surface'], 'String');
            }
            if (data.hasOwnProperty('VenueId')) {
                obj['VenueId'] = ApiClient.convertToType(data['VenueId'], 'Number');
            }
            if (data.hasOwnProperty('Zip')) {
                obj['Zip'] = ApiClient.convertToType(data['Zip'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Venue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Venue</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Address'] && !(typeof data['Address'] === 'string' || data['Address'] instanceof String)) {
            throw new Error("Expected the field `Address` to be a primitive type in the JSON string but got " + data['Address']);
        }
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
        if (data['Nickname1'] && !(typeof data['Nickname1'] === 'string' || data['Nickname1'] instanceof String)) {
            throw new Error("Expected the field `Nickname1` to be a primitive type in the JSON string but got " + data['Nickname1']);
        }
        // ensure the json data is a string
        if (data['Nickname2'] && !(typeof data['Nickname2'] === 'string' || data['Nickname2'] instanceof String)) {
            throw new Error("Expected the field `Nickname2` to be a primitive type in the JSON string but got " + data['Nickname2']);
        }
        // ensure the json data is a string
        if (data['Surface'] && !(typeof data['Surface'] === 'string' || data['Surface'] instanceof String)) {
            throw new Error("Expected the field `Surface` to be a primitive type in the JSON string but got " + data['Surface']);
        }
        // ensure the json data is a string
        if (data['Zip'] && !(typeof data['Zip'] === 'string' || data['Zip'] instanceof String)) {
            throw new Error("Expected the field `Zip` to be a primitive type in the JSON string but got " + data['Zip']);
        }

        return true;
    }


}



/**
 * @member {String} Address
 */
Venue.prototype['Address'] = undefined;

/**
 * @member {Number} Capacity
 */
Venue.prototype['Capacity'] = undefined;

/**
 * @member {String} City
 */
Venue.prototype['City'] = undefined;

/**
 * @member {String} Country
 */
Venue.prototype['Country'] = undefined;

/**
 * @member {Number} GeoLat
 */
Venue.prototype['GeoLat'] = undefined;

/**
 * @member {Number} GeoLong
 */
Venue.prototype['GeoLong'] = undefined;

/**
 * @member {String} Name
 */
Venue.prototype['Name'] = undefined;

/**
 * @member {String} Nickname1
 */
Venue.prototype['Nickname1'] = undefined;

/**
 * @member {String} Nickname2
 */
Venue.prototype['Nickname2'] = undefined;

/**
 * @member {Boolean} Open
 */
Venue.prototype['Open'] = undefined;

/**
 * @member {Number} Opened
 */
Venue.prototype['Opened'] = undefined;

/**
 * @member {String} Surface
 */
Venue.prototype['Surface'] = undefined;

/**
 * @member {Number} VenueId
 */
Venue.prototype['VenueId'] = undefined;

/**
 * @member {String} Zip
 */
Venue.prototype['Zip'] = undefined;






export default Venue;

