/**
 * On-Demand Flight Status
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FlightDesignator from './FlightDesignator';

/**
 * The Partnership model module.
 * @module model/Partnership
 * @version 2.0.2
 */
class Partnership {
    /**
     * Constructs a new <code>Partnership</code>.
     * @alias module:model/Partnership
     */
    constructor() { 
        
        Partnership.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Partnership</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Partnership} obj Optional instance to populate.
     * @return {module:model/Partnership} The populated <code>Partnership</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Partnership();

            if (data.hasOwnProperty('operatingFlight')) {
                obj['operatingFlight'] = FlightDesignator.constructFromObject(data['operatingFlight']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Partnership</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Partnership</code>.
     */
    static validateJSON(data) {
        // validate the optional field `operatingFlight`
        if (data['operatingFlight']) { // data not null
          FlightDesignator.validateJSON(data['operatingFlight']);
        }

        return true;
    }


}



/**
 * @member {module:model/FlightDesignator} operatingFlight
 */
Partnership.prototype['operatingFlight'] = undefined;






export default Partnership;

