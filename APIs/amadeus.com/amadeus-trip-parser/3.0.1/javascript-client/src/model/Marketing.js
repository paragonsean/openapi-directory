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
import Carrier from './Carrier';
import FlightDesignator from './FlightDesignator';

/**
 * The Marketing model module.
 * @module model/Marketing
 * @version 3.0.1
 */
class Marketing {
    /**
     * Constructs a new <code>Marketing</code>.
     * @alias module:model/Marketing
     */
    constructor() { 
        
        Marketing.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Marketing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Marketing} obj Optional instance to populate.
     * @return {module:model/Marketing} The populated <code>Marketing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Marketing();

            if (data.hasOwnProperty('carrier')) {
                obj['carrier'] = Carrier.constructFromObject(data['carrier']);
            }
            if (data.hasOwnProperty('flightDesignator')) {
                obj['flightDesignator'] = FlightDesignator.constructFromObject(data['flightDesignator']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Marketing</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Marketing</code>.
     */
    static validateJSON(data) {
        // validate the optional field `carrier`
        if (data['carrier']) { // data not null
          Carrier.validateJSON(data['carrier']);
        }
        // validate the optional field `flightDesignator`
        if (data['flightDesignator']) { // data not null
          FlightDesignator.validateJSON(data['flightDesignator']);
        }

        return true;
    }


}



/**
 * @member {module:model/Carrier} carrier
 */
Marketing.prototype['carrier'] = undefined;

/**
 * @member {module:model/FlightDesignator} flightDesignator
 */
Marketing.prototype['flightDesignator'] = undefined;






export default Marketing;

