/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AdditionalService from './AdditionalService';
import Fee from './Fee';
import Price from './Price';
import Tax from './Tax';

/**
 * The ExtendedPrice model module.
 * @module model/ExtendedPrice
 * @version 1.0.1
 */
class ExtendedPrice {
    /**
     * Constructs a new <code>ExtendedPrice</code>.
     * price information
     * @alias module:model/ExtendedPrice
     * @implements module:model/Price
     */
    constructor() { 
        Price.initialize(this);
        ExtendedPrice.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ExtendedPrice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExtendedPrice} obj Optional instance to populate.
     * @return {module:model/ExtendedPrice} The populated <code>ExtendedPrice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExtendedPrice();
            Price.constructFromObject(data, obj);

            if (data.hasOwnProperty('base')) {
                obj['base'] = ApiClient.convertToType(data['base'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('fees')) {
                obj['fees'] = ApiClient.convertToType(data['fees'], [Fee]);
            }
            if (data.hasOwnProperty('refundableTaxes')) {
                obj['refundableTaxes'] = ApiClient.convertToType(data['refundableTaxes'], 'String');
            }
            if (data.hasOwnProperty('taxes')) {
                obj['taxes'] = ApiClient.convertToType(data['taxes'], [Tax]);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'String');
            }
            if (data.hasOwnProperty('additionalServices')) {
                obj['additionalServices'] = ApiClient.convertToType(data['additionalServices'], [AdditionalService]);
            }
            if (data.hasOwnProperty('billingCurrency')) {
                obj['billingCurrency'] = ApiClient.convertToType(data['billingCurrency'], 'String');
            }
            if (data.hasOwnProperty('grandTotal')) {
                obj['grandTotal'] = ApiClient.convertToType(data['grandTotal'], 'String');
            }
            if (data.hasOwnProperty('margin')) {
                obj['margin'] = ApiClient.convertToType(data['margin'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExtendedPrice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExtendedPrice</code>.
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
        // ensure the json data is a string
        if (data['refundableTaxes'] && !(typeof data['refundableTaxes'] === 'string' || data['refundableTaxes'] instanceof String)) {
            throw new Error("Expected the field `refundableTaxes` to be a primitive type in the JSON string but got " + data['refundableTaxes']);
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
        if (data['additionalServices']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['additionalServices'])) {
                throw new Error("Expected the field `additionalServices` to be an array in the JSON data but got " + data['additionalServices']);
            }
            // validate the optional field `additionalServices` (array)
            for (const item of data['additionalServices']) {
                AdditionalService.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['billingCurrency'] && !(typeof data['billingCurrency'] === 'string' || data['billingCurrency'] instanceof String)) {
            throw new Error("Expected the field `billingCurrency` to be a primitive type in the JSON string but got " + data['billingCurrency']);
        }
        // ensure the json data is a string
        if (data['grandTotal'] && !(typeof data['grandTotal'] === 'string' || data['grandTotal'] instanceof String)) {
            throw new Error("Expected the field `grandTotal` to be a primitive type in the JSON string but got " + data['grandTotal']);
        }
        // ensure the json data is a string
        if (data['margin'] && !(typeof data['margin'] === 'string' || data['margin'] instanceof String)) {
            throw new Error("Expected the field `margin` to be a primitive type in the JSON string but got " + data['margin']);
        }

        return true;
    }


}



/**
 * Amount without taxes
 * @member {String} base
 */
ExtendedPrice.prototype['base'] = undefined;

/**
 * @member {String} currency
 */
ExtendedPrice.prototype['currency'] = undefined;

/**
 * List of applicable fees
 * @member {Array.<module:model/Fee>} fees
 */
ExtendedPrice.prototype['fees'] = undefined;

/**
 * The amount of taxes which are refundable
 * @member {String} refundableTaxes
 */
ExtendedPrice.prototype['refundableTaxes'] = undefined;

/**
 * @member {Array.<module:model/Tax>} taxes
 */
ExtendedPrice.prototype['taxes'] = undefined;

/**
 * Total amount paid by the user
 * @member {String} total
 */
ExtendedPrice.prototype['total'] = undefined;

/**
 * @member {Array.<module:model/AdditionalService>} additionalServices
 */
ExtendedPrice.prototype['additionalServices'] = undefined;

/**
 * Currency of the payment. It may be different than the requested currency
 * @member {String} billingCurrency
 */
ExtendedPrice.prototype['billingCurrency'] = undefined;

/**
 * Total amount paid by the user (including fees and selected additional services).
 * @member {String} grandTotal
 */
ExtendedPrice.prototype['grandTotal'] = undefined;

/**
 * BOOK step ONLY - The price margin percentage (plus or minus) that the booking can tolerate. When set to 0, then no price magin is tolerated.
 * @member {String} margin
 */
ExtendedPrice.prototype['margin'] = undefined;


// Implement Price interface:
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
 * The amount of taxes which are refundable
 * @member {String} refundableTaxes
 */
Price.prototype['refundableTaxes'] = undefined;
/**
 * @member {Array.<module:model/Tax>} taxes
 */
Price.prototype['taxes'] = undefined;
/**
 * Total amount paid by the user
 * @member {String} total
 */
Price.prototype['total'] = undefined;




export default ExtendedPrice;

