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
 * The InvoiceArray model module.
 * @module model/InvoiceArray
 * @version 1
 */
class InvoiceArray {
    /**
     * Constructs a new <code>InvoiceArray</code>.
     * @alias module:model/InvoiceArray
     * @param businessAddress {String} Your business address
     * @param businessName {String} Your business name
     * @param currencyCode {String} 3 character currency code for invoice
     * @param date {String} The date the invoice was issued
     * @param discountTotal {Number} Total amount of discount
     * @param invoiceNumber {Number} A sequential invoice number
     * @param invoiceUrl {String} A perminant URL to your VAT invoice
     * @param items {Array.<module:model/InvoiceItems>} An array of your invoice items
     * @param subtotal {Number} Total amount excluding VAT
     * @param taxPoint {String} (or 'time of supply') if this is different from the invoice date
     * @param total {Number} Total amount of including VAT
     * @param type {String} The type of invoice. Either 'sale' or 'refund'
     * @param vatNumber {String} Your VAT number
     * @param vatTotal {Number} Total amount of VAT
     */
    constructor(businessAddress, businessName, currencyCode, date, discountTotal, invoiceNumber, invoiceUrl, items, subtotal, taxPoint, total, type, vatNumber, vatTotal) { 
        
        InvoiceArray.initialize(this, businessAddress, businessName, currencyCode, date, discountTotal, invoiceNumber, invoiceUrl, items, subtotal, taxPoint, total, type, vatNumber, vatTotal);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, businessAddress, businessName, currencyCode, date, discountTotal, invoiceNumber, invoiceUrl, items, subtotal, taxPoint, total, type, vatNumber, vatTotal) { 
        obj['business_address'] = businessAddress;
        obj['business_name'] = businessName;
        obj['currency_code'] = currencyCode;
        obj['date'] = date;
        obj['discount_total'] = discountTotal;
        obj['invoice_number'] = invoiceNumber;
        obj['invoice_url'] = invoiceUrl;
        obj['items'] = items;
        obj['subtotal'] = subtotal;
        obj['tax_point'] = taxPoint;
        obj['total'] = total;
        obj['type'] = type;
        obj['vat_number'] = vatNumber;
        obj['vat_total'] = vatTotal;
    }

    /**
     * Constructs a <code>InvoiceArray</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InvoiceArray} obj Optional instance to populate.
     * @return {module:model/InvoiceArray} The populated <code>InvoiceArray</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InvoiceArray();

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
            if (data.hasOwnProperty('customer_vat_number')) {
                obj['customer_vat_number'] = ApiClient.convertToType(data['customer_vat_number'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('discount_rate')) {
                obj['discount_rate'] = ApiClient.convertToType(data['discount_rate'], 'Number');
            }
            if (data.hasOwnProperty('discount_total')) {
                obj['discount_total'] = ApiClient.convertToType(data['discount_total'], 'Number');
            }
            if (data.hasOwnProperty('invoice_number')) {
                obj['invoice_number'] = ApiClient.convertToType(data['invoice_number'], 'Number');
            }
            if (data.hasOwnProperty('invoice_url')) {
                obj['invoice_url'] = ApiClient.convertToType(data['invoice_url'], 'String');
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
            if (data.hasOwnProperty('subtotal')) {
                obj['subtotal'] = ApiClient.convertToType(data['subtotal'], 'Number');
            }
            if (data.hasOwnProperty('tax_point')) {
                obj['tax_point'] = ApiClient.convertToType(data['tax_point'], 'String');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('vat_number')) {
                obj['vat_number'] = ApiClient.convertToType(data['vat_number'], 'String');
            }
            if (data.hasOwnProperty('vat_total')) {
                obj['vat_total'] = ApiClient.convertToType(data['vat_total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InvoiceArray</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InvoiceArray</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InvoiceArray.RequiredProperties) {
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
        if (data['customer_vat_number'] && !(typeof data['customer_vat_number'] === 'string' || data['customer_vat_number'] instanceof String)) {
            throw new Error("Expected the field `customer_vat_number` to be a primitive type in the JSON string but got " + data['customer_vat_number']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['invoice_url'] && !(typeof data['invoice_url'] === 'string' || data['invoice_url'] instanceof String)) {
            throw new Error("Expected the field `invoice_url` to be a primitive type in the JSON string but got " + data['invoice_url']);
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

InvoiceArray.RequiredProperties = ["business_address", "business_name", "currency_code", "date", "discount_total", "invoice_number", "invoice_url", "items", "subtotal", "tax_point", "total", "type", "vat_number", "vat_total"];

/**
 * Your business address
 * @member {String} business_address
 */
InvoiceArray.prototype['business_address'] = undefined;

/**
 * Your business name
 * @member {String} business_name
 */
InvoiceArray.prototype['business_name'] = undefined;

/**
 * The rate of conversion at time of supply
 * @member {Number} conversion_rate
 */
InvoiceArray.prototype['conversion_rate'] = undefined;

/**
 * 3 character currency code for invoice
 * @member {String} currency_code
 */
InvoiceArray.prototype['currency_code'] = undefined;

/**
 * 3 character currency code to be converted from original transaction currency
 * @member {String} currency_code_conversion
 */
InvoiceArray.prototype['currency_code_conversion'] = undefined;

/**
 * Your customers address
 * @member {String} customer_address
 */
InvoiceArray.prototype['customer_address'] = undefined;

/**
 * Your customers name or trading name
 * @member {String} customer_name
 */
InvoiceArray.prototype['customer_name'] = undefined;

/**
 * Customers VAT number
 * @member {String} customer_vat_number
 */
InvoiceArray.prototype['customer_vat_number'] = undefined;

/**
 * The date the invoice was issued
 * @member {String} date
 */
InvoiceArray.prototype['date'] = undefined;

/**
 * The discount rate per item
 * @member {Number} discount_rate
 */
InvoiceArray.prototype['discount_rate'] = undefined;

/**
 * Total amount of discount
 * @member {Number} discount_total
 */
InvoiceArray.prototype['discount_total'] = undefined;

/**
 * A sequential invoice number
 * @member {Number} invoice_number
 */
InvoiceArray.prototype['invoice_number'] = undefined;

/**
 * A perminant URL to your VAT invoice
 * @member {String} invoice_url
 */
InvoiceArray.prototype['invoice_url'] = undefined;

/**
 * An array of your invoice items
 * @member {Array.<module:model/InvoiceItems>} items
 */
InvoiceArray.prototype['items'] = undefined;

/**
 * A URL to your logo image. Must be SSL hosted. https://sslimagehost.com is recommended
 * @member {String} logo_url
 */
InvoiceArray.prototype['logo_url'] = undefined;

/**
 * Any notes attached to the invoice
 * @member {String} notes
 */
InvoiceArray.prototype['notes'] = undefined;

/**
 * Total amount excluding VAT
 * @member {Number} subtotal
 */
InvoiceArray.prototype['subtotal'] = undefined;

/**
 * (or 'time of supply') if this is different from the invoice date
 * @member {String} tax_point
 */
InvoiceArray.prototype['tax_point'] = undefined;

/**
 * Total amount of including VAT
 * @member {Number} total
 */
InvoiceArray.prototype['total'] = undefined;

/**
 * The type of invoice. Either 'sale' or 'refund'
 * @member {String} type
 */
InvoiceArray.prototype['type'] = undefined;

/**
 * Your VAT number
 * @member {String} vat_number
 */
InvoiceArray.prototype['vat_number'] = undefined;

/**
 * Total amount of VAT
 * @member {Number} vat_total
 */
InvoiceArray.prototype['vat_total'] = undefined;






export default InvoiceArray;

