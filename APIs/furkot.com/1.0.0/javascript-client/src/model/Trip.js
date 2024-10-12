/**
 * Furkot Trips
 * Furkot provides Rest API to access user trip data. Using Furkot API an application can list user trips and display stops for a specific trip. Furkot API uses OAuth2 protocol to authorize applications to access data on behalf of users. 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: trips@furkot.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Trip model module.
 * @module model/Trip
 * @version 1.0.0
 */
class Trip {
    /**
     * Constructs a new <code>Trip</code>.
     * @alias module:model/Trip
     */
    constructor() { 
        
        Trip.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Trip</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Trip} obj Optional instance to populate.
     * @return {module:model/Trip} The populated <code>Trip</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Trip();

            if (data.hasOwnProperty('begin')) {
                obj['begin'] = ApiClient.convertToType(data['begin'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('end')) {
                obj['end'] = ApiClient.convertToType(data['end'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Trip</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Trip</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * begin of the trip in its local timezone as YYYY-MM-DDThh:mm
 * @member {Date} begin
 */
Trip.prototype['begin'] = undefined;

/**
 * description of the trip (truncated to 200 characters)
 * @member {String} description
 */
Trip.prototype['description'] = undefined;

/**
 * end of the trip in its local timezone as YYYY-MM-DDThh:mm
 * @member {Date} end
 */
Trip.prototype['end'] = undefined;

/**
 * Unique ID of the trip
 * @member {String} id
 */
Trip.prototype['id'] = undefined;

/**
 * name of the trip
 * @member {String} name
 */
Trip.prototype['name'] = undefined;






export default Trip;

