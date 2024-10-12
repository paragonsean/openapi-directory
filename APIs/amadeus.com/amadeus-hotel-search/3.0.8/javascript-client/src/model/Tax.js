/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Tax model module.
 * @module model/Tax
 * @version 3.0.8
 */
class Tax {
    /**
     * Constructs a new <code>Tax</code>.
     * IATA Tax definition: An impost for raising revenue for the general treasury and which will be used for general public purposes.
     * @alias module:model/Tax
     */
    constructor() { 
        
        Tax.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Tax</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Tax} obj Optional instance to populate.
     * @return {module:model/Tax} The populated <code>Tax</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Tax();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'String');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('included')) {
                obj['included'] = ApiClient.convertToType(data['included'], 'Boolean');
            }
            if (data.hasOwnProperty('percentage')) {
                obj['percentage'] = ApiClient.convertToType(data['percentage'], 'String');
            }
            if (data.hasOwnProperty('pricingFrequency')) {
                obj['pricingFrequency'] = ApiClient.convertToType(data['pricingFrequency'], 'String');
            }
            if (data.hasOwnProperty('pricingMode')) {
                obj['pricingMode'] = ApiClient.convertToType(data['pricingMode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Tax</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Tax</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['amount'] && !(typeof data['amount'] === 'string' || data['amount'] instanceof String)) {
            throw new Error("Expected the field `amount` to be a primitive type in the JSON string but got " + data['amount']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['percentage'] && !(typeof data['percentage'] === 'string' || data['percentage'] instanceof String)) {
            throw new Error("Expected the field `percentage` to be a primitive type in the JSON string but got " + data['percentage']);
        }
        // ensure the json data is a string
        if (data['pricingFrequency'] && !(typeof data['pricingFrequency'] === 'string' || data['pricingFrequency'] instanceof String)) {
            throw new Error("Expected the field `pricingFrequency` to be a primitive type in the JSON string but got " + data['pricingFrequency']);
        }
        // ensure the json data is a string
        if (data['pricingMode'] && !(typeof data['pricingMode'] === 'string' || data['pricingMode'] instanceof String)) {
            throw new Error("Expected the field `pricingMode` to be a primitive type in the JSON string but got " + data['pricingMode']);
        }

        return true;
    }


}



/**
 * Defines amount with decimal separator.
 * @member {String} amount
 */
Tax.prototype['amount'] = undefined;

/**
 * International Standards Organization (ISO) Tax code.It is a two-letter country code.
 * @member {String} code
 */
Tax.prototype['code'] = undefined;

/**
 * Defines a monetary unit. It is a three alpha code (iata code). Example: EUR for Euros, USD for US dollar, etc.
 * @member {String} currency
 */
Tax.prototype['currency'] = undefined;

/**
 * Example - \"Governement tax\"
 * @member {String} description
 */
Tax.prototype['description'] = undefined;

/**
 * Indicates if tax is included or not
 * @member {Boolean} included
 */
Tax.prototype['included'] = undefined;

/**
 * In the case of a tax on TST value, the percentage of the tax will be indicated in this field.
 * @member {String} percentage
 */
Tax.prototype['percentage'] = undefined;

/**
 * Specifies if the tax applies per stay or per night   - PER_STAY   - PER_NIGHT
 * @member {String} pricingFrequency
 */
Tax.prototype['pricingFrequency'] = undefined;

/**
 * Specifies if the tax applies per occupant or per room   - PER_OCCUPANT   - PER_PRODUCT
 * @member {String} pricingMode
 */
Tax.prototype['pricingMode'] = undefined;






export default Tax;

