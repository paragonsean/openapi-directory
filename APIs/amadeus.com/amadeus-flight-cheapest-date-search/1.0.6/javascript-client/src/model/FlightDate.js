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
import FlightDateLinks from './FlightDateLinks';
import Price from './Price';

/**
 * The FlightDate model module.
 * @module model/FlightDate
 * @version 1.0.6
 */
class FlightDate {
    /**
     * Constructs a new <code>FlightDate</code>.
     * @alias module:model/FlightDate
     */
    constructor() { 
        
        FlightDate.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FlightDate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlightDate} obj Optional instance to populate.
     * @return {module:model/FlightDate} The populated <code>FlightDate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlightDate();

            if (data.hasOwnProperty('departureDate')) {
                obj['departureDate'] = ApiClient.convertToType(data['departureDate'], 'String');
            }
            if (data.hasOwnProperty('destination')) {
                obj['destination'] = ApiClient.convertToType(data['destination'], 'String');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = FlightDateLinks.constructFromObject(data['links']);
            }
            if (data.hasOwnProperty('origin')) {
                obj['origin'] = ApiClient.convertToType(data['origin'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = Price.constructFromObject(data['price']);
            }
            if (data.hasOwnProperty('returnDate')) {
                obj['returnDate'] = ApiClient.convertToType(data['returnDate'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlightDate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlightDate</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['departureDate'] && !(typeof data['departureDate'] === 'string' || data['departureDate'] instanceof String)) {
            throw new Error("Expected the field `departureDate` to be a primitive type in the JSON string but got " + data['departureDate']);
        }
        // ensure the json data is a string
        if (data['destination'] && !(typeof data['destination'] === 'string' || data['destination'] instanceof String)) {
            throw new Error("Expected the field `destination` to be a primitive type in the JSON string but got " + data['destination']);
        }
        // validate the optional field `links`
        if (data['links']) { // data not null
          FlightDateLinks.validateJSON(data['links']);
        }
        // ensure the json data is a string
        if (data['origin'] && !(typeof data['origin'] === 'string' || data['origin'] instanceof String)) {
            throw new Error("Expected the field `origin` to be a primitive type in the JSON string but got " + data['origin']);
        }
        // validate the optional field `price`
        if (data['price']) { // data not null
          Price.validateJSON(data['price']);
        }
        // ensure the json data is a string
        if (data['returnDate'] && !(typeof data['returnDate'] === 'string' || data['returnDate'] instanceof String)) {
            throw new Error("Expected the field `returnDate` to be a primitive type in the JSON string but got " + data['returnDate']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {String} departureDate
 */
FlightDate.prototype['departureDate'] = undefined;

/**
 * @member {String} destination
 */
FlightDate.prototype['destination'] = undefined;

/**
 * @member {module:model/FlightDateLinks} links
 */
FlightDate.prototype['links'] = undefined;

/**
 * @member {String} origin
 */
FlightDate.prototype['origin'] = undefined;

/**
 * @member {module:model/Price} price
 */
FlightDate.prototype['price'] = undefined;

/**
 * @member {String} returnDate
 */
FlightDate.prototype['returnDate'] = undefined;

/**
 * the resource name
 * @member {String} type
 */
FlightDate.prototype['type'] = undefined;






export default FlightDate;

