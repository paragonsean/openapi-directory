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
import AircraftEquipment from './AircraftEquipment';
import FlightEndPoint from './FlightEndPoint';
import FlightStop from './FlightStop';
import OperatingFlight from './OperatingFlight';

/**
 * The FlightSegment model module.
 * @module model/FlightSegment
 * @version 1.9.0
 */
class FlightSegment {
    /**
     * Constructs a new <code>FlightSegment</code>.
     * defining a flight segment; including both operating and marketing details when applicable
     * @alias module:model/FlightSegment
     */
    constructor() { 
        
        FlightSegment.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FlightSegment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlightSegment} obj Optional instance to populate.
     * @return {module:model/FlightSegment} The populated <code>FlightSegment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlightSegment();

            if (data.hasOwnProperty('aircraft')) {
                obj['aircraft'] = AircraftEquipment.constructFromObject(data['aircraft']);
            }
            if (data.hasOwnProperty('arrival')) {
                obj['arrival'] = FlightEndPoint.constructFromObject(data['arrival']);
            }
            if (data.hasOwnProperty('carrierCode')) {
                obj['carrierCode'] = ApiClient.convertToType(data['carrierCode'], 'String');
            }
            if (data.hasOwnProperty('departure')) {
                obj['departure'] = FlightEndPoint.constructFromObject(data['departure']);
            }
            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
            if (data.hasOwnProperty('operating')) {
                obj['operating'] = OperatingFlight.constructFromObject(data['operating']);
            }
            if (data.hasOwnProperty('stops')) {
                obj['stops'] = ApiClient.convertToType(data['stops'], [FlightStop]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlightSegment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlightSegment</code>.
     */
    static validateJSON(data) {
        // validate the optional field `aircraft`
        if (data['aircraft']) { // data not null
          AircraftEquipment.validateJSON(data['aircraft']);
        }
        // validate the optional field `arrival`
        if (data['arrival']) { // data not null
          FlightEndPoint.validateJSON(data['arrival']);
        }
        // ensure the json data is a string
        if (data['carrierCode'] && !(typeof data['carrierCode'] === 'string' || data['carrierCode'] instanceof String)) {
            throw new Error("Expected the field `carrierCode` to be a primitive type in the JSON string but got " + data['carrierCode']);
        }
        // validate the optional field `departure`
        if (data['departure']) { // data not null
          FlightEndPoint.validateJSON(data['departure']);
        }
        // ensure the json data is a string
        if (data['duration'] && !(typeof data['duration'] === 'string' || data['duration'] instanceof String)) {
            throw new Error("Expected the field `duration` to be a primitive type in the JSON string but got " + data['duration']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }
        // validate the optional field `operating`
        if (data['operating']) { // data not null
          OperatingFlight.validateJSON(data['operating']);
        }
        if (data['stops']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['stops'])) {
                throw new Error("Expected the field `stops` to be an array in the JSON data but got " + data['stops']);
            }
            // validate the optional field `stops` (array)
            for (const item of data['stops']) {
                FlightStop.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/AircraftEquipment} aircraft
 */
FlightSegment.prototype['aircraft'] = undefined;

/**
 * @member {module:model/FlightEndPoint} arrival
 */
FlightSegment.prototype['arrival'] = undefined;

/**
 * providing the airline / carrier code
 * @member {String} carrierCode
 */
FlightSegment.prototype['carrierCode'] = undefined;

/**
 * @member {module:model/FlightEndPoint} departure
 */
FlightSegment.prototype['departure'] = undefined;

/**
 * stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
 * @member {String} duration
 */
FlightSegment.prototype['duration'] = undefined;

/**
 * the flight number as assigned by the carrier
 * @member {String} number
 */
FlightSegment.prototype['number'] = undefined;

/**
 * @member {module:model/OperatingFlight} operating
 */
FlightSegment.prototype['operating'] = undefined;

/**
 * information regarding the different stops composing the flight segment. E.g. technical stop, change of gauge...
 * @member {Array.<module:model/FlightStop>} stops
 */
FlightSegment.prototype['stops'] = undefined;






export default FlightSegment;

