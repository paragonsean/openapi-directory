/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OriginalFlightEndPoint from './OriginalFlightEndPoint';

/**
 * The FlightEndPoint model module.
 * @module model/FlightEndPoint
 * @version 1.0.2
 */
class FlightEndPoint {
    /**
     * Constructs a new <code>FlightEndPoint</code>.
     * departure or arrival information
     * @alias module:model/FlightEndPoint
     * @implements module:model/OriginalFlightEndPoint
     */
    constructor() { 
        OriginalFlightEndPoint.initialize(this);
        FlightEndPoint.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FlightEndPoint</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlightEndPoint} obj Optional instance to populate.
     * @return {module:model/FlightEndPoint} The populated <code>FlightEndPoint</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlightEndPoint();
            OriginalFlightEndPoint.constructFromObject(data, obj);

            if (data.hasOwnProperty('iataCode')) {
                obj['iataCode'] = ApiClient.convertToType(data['iataCode'], 'String');
            }
            if (data.hasOwnProperty('terminal')) {
                obj['terminal'] = ApiClient.convertToType(data['terminal'], 'String');
            }
            if (data.hasOwnProperty('at')) {
                obj['at'] = ApiClient.convertToType(data['at'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlightEndPoint</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlightEndPoint</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['iataCode'] && !(typeof data['iataCode'] === 'string' || data['iataCode'] instanceof String)) {
            throw new Error("Expected the field `iataCode` to be a primitive type in the JSON string but got " + data['iataCode']);
        }
        // ensure the json data is a string
        if (data['terminal'] && !(typeof data['terminal'] === 'string' || data['terminal'] instanceof String)) {
            throw new Error("Expected the field `terminal` to be a primitive type in the JSON string but got " + data['terminal']);
        }

        return true;
    }


}



/**
 * [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx)
 * @member {String} iataCode
 */
FlightEndPoint.prototype['iataCode'] = undefined;

/**
 * terminal name / number
 * @member {String} terminal
 */
FlightEndPoint.prototype['terminal'] = undefined;

/**
 * local date and time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss format, e.g. 2017-02-10T20:40:00
 * @member {Date} at
 */
FlightEndPoint.prototype['at'] = undefined;


// Implement OriginalFlightEndPoint interface:
/**
 * [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx)
 * @member {String} iataCode
 */
OriginalFlightEndPoint.prototype['iataCode'] = undefined;
/**
 * terminal name / number
 * @member {String} terminal
 */
OriginalFlightEndPoint.prototype['terminal'] = undefined;




export default FlightEndPoint;

