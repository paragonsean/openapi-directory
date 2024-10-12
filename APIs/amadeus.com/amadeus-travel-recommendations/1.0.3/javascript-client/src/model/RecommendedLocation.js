/**
 * Travel Recommendations API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GeoCode from './GeoCode';

/**
 * The RecommendedLocation model module.
 * @module model/RecommendedLocation
 * @version 1.0.3
 */
class RecommendedLocation {
    /**
     * Constructs a new <code>RecommendedLocation</code>.
     * Similar Location
     * @alias module:model/RecommendedLocation
     */
    constructor() { 
        
        RecommendedLocation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RecommendedLocation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RecommendedLocation} obj Optional instance to populate.
     * @return {module:model/RecommendedLocation} The populated <code>RecommendedLocation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RecommendedLocation();

            if (data.hasOwnProperty('geoCode')) {
                obj['geoCode'] = GeoCode.constructFromObject(data['geoCode']);
            }
            if (data.hasOwnProperty('iataCode')) {
                obj['iataCode'] = ApiClient.convertToType(data['iataCode'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('subtype')) {
                obj['subtype'] = ApiClient.convertToType(data['subtype'], 'String');
            }
            if (data.hasOwnProperty('relevance')) {
                obj['relevance'] = ApiClient.convertToType(data['relevance'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RecommendedLocation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RecommendedLocation</code>.
     */
    static validateJSON(data) {
        // validate the optional field `geoCode`
        if (data['geoCode']) { // data not null
          GeoCode.validateJSON(data['geoCode']);
        }
        // ensure the json data is a string
        if (data['iataCode'] && !(typeof data['iataCode'] === 'string' || data['iataCode'] instanceof String)) {
            throw new Error("Expected the field `iataCode` to be a primitive type in the JSON string but got " + data['iataCode']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['subtype'] && !(typeof data['subtype'] === 'string' || data['subtype'] instanceof String)) {
            throw new Error("Expected the field `subtype` to be a primitive type in the JSON string but got " + data['subtype']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/GeoCode} geoCode
 */
RecommendedLocation.prototype['geoCode'] = undefined;

/**
 * IATA location code
 * @member {String} iataCode
 */
RecommendedLocation.prototype['iataCode'] = undefined;

/**
 * Label associated to the location (e.g. Eiffel Tower, Madison Square)
 * @member {String} name
 */
RecommendedLocation.prototype['name'] = undefined;

/**
 * Location sub-type (e.g. airport, port, rail-station, restaurant, atm...)
 * @member {String} subtype
 */
RecommendedLocation.prototype['subtype'] = undefined;

/**
 * percentage of similarity.  0 for not similar to 1 for exactly the same
 * @member {Number} relevance
 */
RecommendedLocation.prototype['relevance'] = undefined;

/**
 * Ressource type
 * @member {String} type
 */
RecommendedLocation.prototype['type'] = undefined;






export default RecommendedLocation;

