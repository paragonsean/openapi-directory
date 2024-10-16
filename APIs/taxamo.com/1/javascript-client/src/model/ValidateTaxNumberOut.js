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
 * The ValidateTaxNumberOut model module.
 * @module model/ValidateTaxNumberOut
 * @version 1
 */
class ValidateTaxNumberOut {
    /**
     * Constructs a new <code>ValidateTaxNumberOut</code>.
     * @alias module:model/ValidateTaxNumberOut
     */
    constructor() { 
        
        ValidateTaxNumberOut.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ValidateTaxNumberOut</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ValidateTaxNumberOut} obj Optional instance to populate.
     * @return {module:model/ValidateTaxNumberOut} The populated <code>ValidateTaxNumberOut</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ValidateTaxNumberOut();

            if (data.hasOwnProperty('billing_country_code')) {
                obj['billing_country_code'] = ApiClient.convertToType(data['billing_country_code'], 'String');
            }
            if (data.hasOwnProperty('buyer_tax_number')) {
                obj['buyer_tax_number'] = ApiClient.convertToType(data['buyer_tax_number'], 'String');
            }
            if (data.hasOwnProperty('buyer_tax_number_valid')) {
                obj['buyer_tax_number_valid'] = ApiClient.convertToType(data['buyer_tax_number_valid'], 'Boolean');
            }
            if (data.hasOwnProperty('tax_deducted')) {
                obj['tax_deducted'] = ApiClient.convertToType(data['tax_deducted'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ValidateTaxNumberOut</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ValidateTaxNumberOut</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['billing_country_code'] && !(typeof data['billing_country_code'] === 'string' || data['billing_country_code'] instanceof String)) {
            throw new Error("Expected the field `billing_country_code` to be a primitive type in the JSON string but got " + data['billing_country_code']);
        }
        // ensure the json data is a string
        if (data['buyer_tax_number'] && !(typeof data['buyer_tax_number'] === 'string' || data['buyer_tax_number'] instanceof String)) {
            throw new Error("Expected the field `buyer_tax_number` to be a primitive type in the JSON string but got " + data['buyer_tax_number']);
        }

        return true;
    }


}



/**
 * Billing two letter ISO country code.
 * @member {String} billing_country_code
 */
ValidateTaxNumberOut.prototype['billing_country_code'] = undefined;

/**
 *  Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
 * @member {String} buyer_tax_number
 */
ValidateTaxNumberOut.prototype['buyer_tax_number'] = undefined;

/**
 * If the buyer tax number has been provided and was validated successfully. Always true for domestic transactions (billing country same as merchant's country), tax number doesn't get validated in that case.
 * @member {Boolean} buyer_tax_number_valid
 */
ValidateTaxNumberOut.prototype['buyer_tax_number_valid'] = undefined;

/**
 * If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
 * @member {Boolean} tax_deducted
 */
ValidateTaxNumberOut.prototype['tax_deducted'] = undefined;






export default ValidateTaxNumberOut;

