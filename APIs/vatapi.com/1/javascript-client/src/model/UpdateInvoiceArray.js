/**
 * VAT API
 * A developer friendly API to help your business achieve VAT compliance
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
import InvoiceItems from './InvoiceItems';

/**
 * The UpdateInvoiceArray model module.
 * @module model/UpdateInvoiceArray
 * @version 1
 */
class UpdateInvoiceArray {
    /**
     * Constructs a new <code>UpdateInvoiceArray</code>.
     * @alias module:model/UpdateInvoiceArray
     * @param businessAddress {String} Your business address
     * @param businessName {String} Your business name
     * @param currencyCode {String} 3 character currency code for invoice
     * @param customervatNumber {String} Customers VAT number
     * @param items {Array.<module:model/InvoiceItems>} An array of your invoice items
     * @param type {String} The type of invoice. Either 'sale' or 'refund'
     */
    constructor(businessAddress, businessName, currencyCode, customervatNumber, items, type) { 
        
        UpdateInvoiceArray.initialize(this, businessAddress, businessName, currencyCode, customervatNumber, items, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, businessAddress, businessName, currencyCode, customervatNumber, items, type) { 
        obj['business_address'] = businessAddress;
        obj['business_name'] = businessName;
        obj['currency_code'] = currencyCode;
        obj['customervat_number'] = customervatNumber;
        obj['items'] = items;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>UpdateInvoiceArray</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateInvoiceArray} obj Optional instance to populate.
     * @return {module:model/UpdateInvoiceArray} The populated <code>UpdateInvoiceArray</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateInvoiceArray();

            if (data.hasOwnProperty('business_address')) {
                obj['business_address'] = ApiClient.convertToType(data['business_address'], 'String');
            }
            if (data.hasOwnProperty('business_name')) {
                obj['business_name'] = ApiClient.convertToType(data['business_name'], 'String');
            }
            if (data.hasOwnProperty('conversion_rate')) {
                obj['conversion_rate'] = ApiClient.convertToType(data['conversion_rate'], 'Number');
            }
            if (data.hasOwnProperty('currency_code')) {
                obj['currency_code'] = ApiClient.convertToType(data['currency_code'], 'String');
            }
            if (data.hasOwnProperty('currency_code_conversion')) {
                obj['currency_code_conversion'] = ApiClient.convertToType(data['currency_code_conversion'], 'String');
            }
            if (data.hasOwnProperty('customer_address')) {
                obj['customer_address'] = ApiClient.convertToType(data['customer_address'], 'String');
            }
            if (data.hasOwnProperty('customer_name')) {
                obj['customer_name'] = ApiClient.convertToType(data['customer_name'], 'String');
            }
            if (data.hasOwnProperty('customervat_number')) {
                obj['customervat_number'] = ApiClient.convertToType(data['customervat_number'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('discount_rate')) {
                obj['discount_rate'] = ApiClient.convertToType(data['discount_rate'], 'String');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [InvoiceItems]);
            }
            if (data.hasOwnProperty('logo_url')) {
                obj['logo_url'] = ApiClient.convertToType(data['logo_url'], 'String');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('tax_point')) {
                obj['tax_point'] = ApiClient.convertToType(data['tax_point'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('vat_number')) {
                obj['vat_number'] = ApiClient.convertToType(data['vat_number'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateInvoiceArray</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateInvoiceArray</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateInvoiceArray.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['business_address'] && !(typeof data['business_address'] === 'string' || data['business_address'] instanceof String)) {
            throw new Error("Expected the field `business_address` to be a primitive type in the JSON string but got " + data['business_address']);
        }
        // ensure the json data is a string
        if (data['business_name'] && !(typeof data['business_name'] === 'string' || data['business_name'] instanceof String)) {
            throw new Error("Expected the field `business_name` to be a primitive type in the JSON string but got " + data['business_name']);
        }
        // ensure the json data is a string
        if (data['currency_code'] && !(typeof data['currency_code'] === 'string' || data['currency_code'] instanceof String)) {
            throw new Error("Expected the field `currency_code` to be a primitive type in the JSON string but got " + data['currency_code']);
        }
        // ensure the json data is a string
        if (data['currency_code_conversion'] && !(typeof data['currency_code_conversion'] === 'string' || data['currency_code_conversion'] instanceof String)) {
            throw new Error("Expected the field `currency_code_conversion` to be a primitive type in the JSON string but got " + data['currency_code_conversion']);
        }
        // ensure the json data is a string
        if (data['customer_address'] && !(typeof data['customer_address'] === 'string' || data['customer_address'] instanceof String)) {
            throw new Error("Expected the field `customer_address` to be a primitive type in the JSON string but got " + data['customer_address']);
        }
        // ensure the json data is a string
        if (data['customer_name'] && !(typeof data['customer_name'] === 'string' || data['customer_name'] instanceof String)) {
            throw new Error("Expected the field `customer_name` to be a primitive type in the JSON string but got " + data['customer_name']);
        }
        // ensure the json data is a string
        if (data['customervat_number'] && !(typeof data['customervat_number'] === 'string' || data['customervat_number'] instanceof String)) {
            throw new Error("Expected the field `customervat_number` to be a primitive type in the JSON string but got " + data['customervat_number']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['discount_rate'] && !(typeof data['discount_rate'] === 'string' || data['discount_rate'] instanceof String)) {
            throw new Error("Expected the field `discount_rate` to be a primitive type in the JSON string but got " + data['discount_rate']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                InvoiceItems.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['logo_url'] && !(typeof data['logo_url'] === 'string' || data['logo_url'] instanceof String)) {
            throw new Error("Expected the field `logo_url` to be a primitive type in the JSON string but got " + data['logo_url']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['tax_point'] && !(typeof data['tax_point'] === 'string' || data['tax_point'] instanceof String)) {
            throw new Error("Expected the field `tax_point` to be a primitive type in the JSON string but got " + data['tax_point']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['vat_number'] && !(typeof data['vat_number'] === 'string' || data['vat_number'] instanceof String)) {
            throw new Error("Expected the field `vat_number` to be a primitive type in the JSON string but got " + data['vat_number']);
        }

        return true;
    }


}

UpdateInvoiceArray.RequiredProperties = ["business_address", "business_name", "currency_code", "customervat_number", "items", "type"];

/**
 * Your business address
 * @member {String} business_address
 */
UpdateInvoiceArray.prototype['business_address'] = undefined;

/**
 * Your business name
 * @member {String} business_name
 */
UpdateInvoiceArray.prototype['business_name'] = undefined;

/**
 * The rate of conversion at time of supply
 * @member {Number} conversion_rate
 */
UpdateInvoiceArray.prototype['conversion_rate'] = undefined;

/**
 * 3 character currency code for invoice
 * @member {String} currency_code
 */
UpdateInvoiceArray.prototype['currency_code'] = undefined;

/**
 * 3 character currency code to be converted from original transaction currency
 * @member {String} currency_code_conversion
 */
UpdateInvoiceArray.prototype['currency_code_conversion'] = undefined;

/**
 * Your customers address
 * @member {String} customer_address
 */
UpdateInvoiceArray.prototype['customer_address'] = undefined;

/**
 * Your customers name or trading name
 * @member {String} customer_name
 */
UpdateInvoiceArray.prototype['customer_name'] = undefined;

/**
 * Customers VAT number
 * @member {String} customervat_number
 */
UpdateInvoiceArray.prototype['customervat_number'] = undefined;

/**
 * The date the invoice was issued
 * @member {String} date
 */
UpdateInvoiceArray.prototype['date'] = undefined;

/**
 * The discount rate per item
 * @member {String} discount_rate
 */
UpdateInvoiceArray.prototype['discount_rate'] = undefined;

/**
 * An array of your invoice items
 * @member {Array.<module:model/InvoiceItems>} items
 */
UpdateInvoiceArray.prototype['items'] = undefined;

/**
 * A URL to your logo image. Must be SSL hosted. https://sslimagehost.com is recommended
 * @member {String} logo_url
 */
UpdateInvoiceArray.prototype['logo_url'] = undefined;

/**
 * Add a note to the invoice.
 * @member {String} notes
 */
UpdateInvoiceArray.prototype['notes'] = undefined;

/**
 * (or 'time of supply') if this is different from the invoice date
 * @member {String} tax_point
 */
UpdateInvoiceArray.prototype['tax_point'] = undefined;

/**
 * The type of invoice. Either 'sale' or 'refund'
 * @member {String} type
 */
UpdateInvoiceArray.prototype['type'] = undefined;

/**
 * Your VAT number
 * @member {String} vat_number
 */
UpdateInvoiceArray.prototype['vat_number'] = undefined;






export default UpdateInvoiceArray;

