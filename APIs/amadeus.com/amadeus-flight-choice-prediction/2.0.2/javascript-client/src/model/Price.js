/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
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
import Fee from './Fee';
import Tax from './Tax';

/**
 * The Price model module.
 * @module model/Price
 * @version 2.0.2
 */
class Price {
    /**
     * Constructs a new <code>Price</code>.
     * @alias module:model/Price
     */
    constructor() { 
        
        Price.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Price</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Price} obj Optional instance to populate.
     * @return {module:model/Price} The populated <code>Price</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Price();

            if (data.hasOwnProperty('base')) {
                obj['base'] = ApiClient.convertToType(data['base'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('fees')) {
                obj['fees'] = ApiClient.convertToType(data['fees'], [Fee]);
            }
            if (data.hasOwnProperty('taxes')) {
                obj['taxes'] = ApiClient.convertToType(data['taxes'], [Tax]);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Price</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Price</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['base'] && !(typeof data['base'] === 'string' || data['base'] instanceof String)) {
            throw new Error("Expected the field `base` to be a primitive type in the JSON string but got " + data['base']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        if (data['fees']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['fees'])) {
                throw new Error("Expected the field `fees` to be an array in the JSON data but got " + data['fees']);
            }
            // validate the optional field `fees` (array)
            for (const item of data['fees']) {
                Fee.validateJSON(item);
            };
        }
        if (data['taxes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['taxes'])) {
                throw new Error("Expected the field `taxes` to be an array in the JSON data but got " + data['taxes']);
            }
            // validate the optional field `taxes` (array)
            for (const item of data['taxes']) {
                Tax.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['total'] && !(typeof data['total'] === 'string' || data['total'] instanceof String)) {
            throw new Error("Expected the field `total` to be a primitive type in the JSON string but got " + data['total']);
        }

        return true;
    }


}



/**
 * Amount without taxes
 * @member {String} base
 */
Price.prototype['base'] = undefined;

/**
 * @member {String} currency
 */
Price.prototype['currency'] = undefined;

/**
 * List of applicable fees
 * @member {Array.<module:model/Fee>} fees
 */
Price.prototype['fees'] = undefined;

/**
 * @member {Array.<module:model/Tax>} taxes
 */
Price.prototype['taxes'] = undefined;

/**
 * Total amount paid by the user
 * @member {String} total
 */
Price.prototype['total'] = undefined;






export default Price;

