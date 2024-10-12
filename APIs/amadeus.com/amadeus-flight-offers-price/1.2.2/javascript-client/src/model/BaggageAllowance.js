/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BaggageAllowance model module.
 * @module model/BaggageAllowance
 * @version 1.2.2
 */
class BaggageAllowance {
    /**
     * Constructs a new <code>BaggageAllowance</code>.
     * baggageAllowance
     * @alias module:model/BaggageAllowance
     */
    constructor() { 
        
        BaggageAllowance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BaggageAllowance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BaggageAllowance} obj Optional instance to populate.
     * @return {module:model/BaggageAllowance} The populated <code>BaggageAllowance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BaggageAllowance();

            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], 'Number');
            }
            if (data.hasOwnProperty('weight')) {
                obj['weight'] = ApiClient.convertToType(data['weight'], 'Number');
            }
            if (data.hasOwnProperty('weightUnit')) {
                obj['weightUnit'] = ApiClient.convertToType(data['weightUnit'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BaggageAllowance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BaggageAllowance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['weightUnit'] && !(typeof data['weightUnit'] === 'string' || data['weightUnit'] instanceof String)) {
            throw new Error("Expected the field `weightUnit` to be a primitive type in the JSON string but got " + data['weightUnit']);
        }

        return true;
    }


}



/**
 * Total number of units
 * @member {Number} quantity
 */
BaggageAllowance.prototype['quantity'] = undefined;

/**
 * Weight of the baggage allowance
 * @member {Number} weight
 */
BaggageAllowance.prototype['weight'] = undefined;

/**
 * Code to qualify unit as pounds or kilos
 * @member {String} weightUnit
 */
BaggageAllowance.prototype['weightUnit'] = undefined;






export default BaggageAllowance;

