/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Address from './Address';

/**
 * The End model module.
 * @module model/End
 * @version 3.0.1
 */
class End {
    /**
     * Constructs a new <code>End</code>.
     * Description of a particular point or place in physical space
     * @alias module:model/End
     */
    constructor() { 
        
        End.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>End</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/End} obj Optional instance to populate.
     * @return {module:model/End} The populated <code>End</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new End();

            if (data.hasOwnProperty('address')) {
                obj['address'] = Address.constructFromObject(data['address']);
            }
            if (data.hasOwnProperty('iataCode')) {
                obj['iataCode'] = ApiClient.convertToType(data['iataCode'], 'String');
            }
            if (data.hasOwnProperty('localDateTime')) {
                obj['localDateTime'] = ApiClient.convertToType(data['localDateTime'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>End</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>End</code>.
     */
    static validateJSON(data) {
        // validate the optional field `address`
        if (data['address']) { // data not null
          Address.validateJSON(data['address']);
        }
        // ensure the json data is a string
        if (data['iataCode'] && !(typeof data['iataCode'] === 'string' || data['iataCode'] instanceof String)) {
            throw new Error("Expected the field `iataCode` to be a primitive type in the JSON string but got " + data['iataCode']);
        }
        // ensure the json data is a string
        if (data['localDateTime'] && !(typeof data['localDateTime'] === 'string' || data['localDateTime'] instanceof String)) {
            throw new Error("Expected the field `localDateTime` to be a primitive type in the JSON string but got " + data['localDateTime']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {module:model/Address} address
 */
End.prototype['address'] = undefined;

/**
 * IATA location code
 * @member {String} iataCode
 */
End.prototype['iataCode'] = undefined;

/**
 * Local Date/Time of the itinerary end in format ISO 8601 (YYYY-MM-DDTHH:MM:SS)
 * @member {String} localDateTime
 */
End.prototype['localDateTime'] = undefined;

/**
 * Label associated to the location (e.g. Eiffel Tower, Madison Square)
 * @member {String} name
 */
End.prototype['name'] = undefined;






export default End;

