/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OriginalFlightStop from './OriginalFlightStop';

/**
 * The FlightStop model module.
 * @module model/FlightStop
 * @version 1.9.0
 */
class FlightStop {
    /**
     * Constructs a new <code>FlightStop</code>.
     * details of stops for direct or change of gauge flights
     * @alias module:model/FlightStop
     * @implements module:model/OriginalFlightStop
     */
    constructor() { 
        OriginalFlightStop.initialize(this);
        FlightStop.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FlightStop</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlightStop} obj Optional instance to populate.
     * @return {module:model/FlightStop} The populated <code>FlightStop</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlightStop();
            OriginalFlightStop.constructFromObject(data, obj);

            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'String');
            }
            if (data.hasOwnProperty('iataCode')) {
                obj['iataCode'] = ApiClient.convertToType(data['iataCode'], 'String');
            }
            if (data.hasOwnProperty('arrivalAt')) {
                obj['arrivalAt'] = ApiClient.convertToType(data['arrivalAt'], 'Date');
            }
            if (data.hasOwnProperty('departureAt')) {
                obj['departureAt'] = ApiClient.convertToType(data['departureAt'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlightStop</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlightStop</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['duration'] && !(typeof data['duration'] === 'string' || data['duration'] instanceof String)) {
            throw new Error("Expected the field `duration` to be a primitive type in the JSON string but got " + data['duration']);
        }
        // ensure the json data is a string
        if (data['iataCode'] && !(typeof data['iataCode'] === 'string' || data['iataCode'] instanceof String)) {
            throw new Error("Expected the field `iataCode` to be a primitive type in the JSON string but got " + data['iataCode']);
        }

        return true;
    }


}



/**
 * stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
 * @member {String} duration
 */
FlightStop.prototype['duration'] = undefined;

/**
 * [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx)
 * @member {String} iataCode
 */
FlightStop.prototype['iataCode'] = undefined;

/**
 * arrival at the stop in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss format, e.g. 2017-02-10T20:40:00
 * @member {Date} arrivalAt
 */
FlightStop.prototype['arrivalAt'] = undefined;

/**
 * departure from the stop in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss format, e.g. 2017-02-10T20:40:00
 * @member {Date} departureAt
 */
FlightStop.prototype['departureAt'] = undefined;


// Implement OriginalFlightStop interface:
/**
 * stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
 * @member {String} duration
 */
OriginalFlightStop.prototype['duration'] = undefined;
/**
 * [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx)
 * @member {String} iataCode
 */
OriginalFlightStop.prototype['iataCode'] = undefined;




export default FlightStop;

