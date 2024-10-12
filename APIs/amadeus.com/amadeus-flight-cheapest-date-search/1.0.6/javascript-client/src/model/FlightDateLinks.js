/**
 * Flight Cheapest Date Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FlightDateLinks model module.
 * @module model/FlightDateLinks
 * @version 1.0.6
 */
class FlightDateLinks {
    /**
     * Constructs a new <code>FlightDateLinks</code>.
     * @alias module:model/FlightDateLinks
     */
    constructor() { 
        
        FlightDateLinks.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FlightDateLinks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlightDateLinks} obj Optional instance to populate.
     * @return {module:model/FlightDateLinks} The populated <code>FlightDateLinks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlightDateLinks();

            if (data.hasOwnProperty('flightDestinations')) {
                obj['flightDestinations'] = ApiClient.convertToType(data['flightDestinations'], 'String');
            }
            if (data.hasOwnProperty('flightOffers')) {
                obj['flightOffers'] = ApiClient.convertToType(data['flightOffers'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlightDateLinks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlightDateLinks</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['flightDestinations'] && !(typeof data['flightDestinations'] === 'string' || data['flightDestinations'] instanceof String)) {
            throw new Error("Expected the field `flightDestinations` to be a primitive type in the JSON string but got " + data['flightDestinations']);
        }
        // ensure the json data is a string
        if (data['flightOffers'] && !(typeof data['flightOffers'] === 'string' || data['flightOffers'] instanceof String)) {
            throw new Error("Expected the field `flightOffers` to be a primitive type in the JSON string but got " + data['flightOffers']);
        }

        return true;
    }


}



/**
 * @member {String} flightDestinations
 */
FlightDateLinks.prototype['flightDestinations'] = undefined;

/**
 * @member {String} flightOffers
 */
FlightDateLinks.prototype['flightOffers'] = undefined;






export default FlightDateLinks;

