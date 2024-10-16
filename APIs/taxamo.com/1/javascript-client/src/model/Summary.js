/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Summary model module.
 * @module model/Summary
 * @version 1
 */
class Summary {
    /**
     * Constructs a new <code>Summary</code>.
     * @alias module:model/Summary
     */
    constructor() { 
        
        Summary.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Summary</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Summary} obj Optional instance to populate.
     * @return {module:model/Summary} The populated <code>Summary</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Summary();

            if (data.hasOwnProperty('currency_code')) {
                obj['currency_code'] = ApiClient.convertToType(data['currency_code'], 'String');
            }
            if (data.hasOwnProperty('end_date')) {
                obj['end_date'] = ApiClient.convertToType(data['end_date'], 'String');
            }
            if (data.hasOwnProperty('fx_rate_date')) {
                obj['fx_rate_date'] = ApiClient.convertToType(data['fx_rate_date'], 'String');
            }
            if (data.hasOwnProperty('indicative')) {
                obj['indicative'] = ApiClient.convertToType(data['indicative'], 'Boolean');
            }
            if (data.hasOwnProperty('quarter')) {
                obj['quarter'] = ApiClient.convertToType(data['quarter'], 'String');
            }
            if (data.hasOwnProperty('start_date')) {
                obj['start_date'] = ApiClient.convertToType(data['start_date'], 'String');
            }
            if (data.hasOwnProperty('tax_amount')) {
                obj['tax_amount'] = ApiClient.convertToType(data['tax_amount'], 'Number');
            }
            if (data.hasOwnProperty('tax_entity_name')) {
                obj['tax_entity_name'] = ApiClient.convertToType(data['tax_entity_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Summary</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Summary</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['currency_code'] && !(typeof data['currency_code'] === 'string' || data['currency_code'] instanceof String)) {
            throw new Error("Expected the field `currency_code` to be a primitive type in the JSON string but got " + data['currency_code']);
        }
        // ensure the json data is a string
        if (data['end_date'] && !(typeof data['end_date'] === 'string' || data['end_date'] instanceof String)) {
            throw new Error("Expected the field `end_date` to be a primitive type in the JSON string but got " + data['end_date']);
        }
        // ensure the json data is a string
        if (data['fx_rate_date'] && !(typeof data['fx_rate_date'] === 'string' || data['fx_rate_date'] instanceof String)) {
            throw new Error("Expected the field `fx_rate_date` to be a primitive type in the JSON string but got " + data['fx_rate_date']);
        }
        // ensure the json data is a string
        if (data['quarter'] && !(typeof data['quarter'] === 'string' || data['quarter'] instanceof String)) {
            throw new Error("Expected the field `quarter` to be a primitive type in the JSON string but got " + data['quarter']);
        }
        // ensure the json data is a string
        if (data['start_date'] && !(typeof data['start_date'] === 'string' || data['start_date'] instanceof String)) {
            throw new Error("Expected the field `start_date` to be a primitive type in the JSON string but got " + data['start_date']);
        }
        // ensure the json data is a string
        if (data['tax_entity_name'] && !(typeof data['tax_entity_name'] === 'string' || data['tax_entity_name'] instanceof String)) {
            throw new Error("Expected the field `tax_entity_name` to be a primitive type in the JSON string but got " + data['tax_entity_name']);
        }

        return true;
    }


}



/**
 * In which currency code the settlement was calculated.
 * @member {String} currency_code
 */
Summary.prototype['currency_code'] = undefined;

/**
 * Period end date in yyyy-MM-dd'T'hh:mm:ss'Z' format.
 * @member {String} end_date
 */
Summary.prototype['end_date'] = undefined;

/**
 * Date of ECB FX rate used for conversions in yyyy-MM-dd'T'hh:mm:ss'Z' format.
 * @member {String} fx_rate_date
 */
Summary.prototype['fx_rate_date'] = undefined;

/**
 * If the quarter isn't closed yet, tax amount is indicative, as we cannot determine FX rate or all transactions yet.
 * @member {Boolean} indicative
 */
Summary.prototype['indicative'] = undefined;

/**
 * Quarter that this summary applies to.
 * @member {String} quarter
 */
Summary.prototype['quarter'] = undefined;

/**
 * Period start date in yyyy-MM-dd'T'hh:mm:ss'Z' format.
 * @member {String} start_date
 */
Summary.prototype['start_date'] = undefined;

/**
 * Tax amount due in this quarter.
 * @member {Number} tax_amount
 */
Summary.prototype['tax_amount'] = undefined;

/**
 * Tax entity that the tax is due.
 * @member {String} tax_entity_name
 */
Summary.prototype['tax_entity_name'] = undefined;






export default Summary;

