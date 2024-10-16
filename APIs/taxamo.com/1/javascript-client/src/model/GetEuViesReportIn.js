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
 * The GetEuViesReportIn model module.
 * @module model/GetEuViesReportIn
 * @version 1
 */
class GetEuViesReportIn {
    /**
     * Constructs a new <code>GetEuViesReportIn</code>.
     * @alias module:model/GetEuViesReportIn
     * @param endMonth {String} Period end month in yyyy-MM format.
     * @param euCountryCode {String} ISO 2-letter country code which will be used for determining which country is domestic.
     * @param startMonth {String} Period start month in yyyy-MM format.
     */
    constructor(endMonth, euCountryCode, startMonth) { 
        
        GetEuViesReportIn.initialize(this, endMonth, euCountryCode, startMonth);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, endMonth, euCountryCode, startMonth) { 
        obj['end_month'] = endMonth;
        obj['eu_country_code'] = euCountryCode;
        obj['start_month'] = startMonth;
    }

    /**
     * Constructs a <code>GetEuViesReportIn</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetEuViesReportIn} obj Optional instance to populate.
     * @return {module:model/GetEuViesReportIn} The populated <code>GetEuViesReportIn</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetEuViesReportIn();

            if (data.hasOwnProperty('currency_code')) {
                obj['currency_code'] = ApiClient.convertToType(data['currency_code'], 'String');
            }
            if (data.hasOwnProperty('end_month')) {
                obj['end_month'] = ApiClient.convertToType(data['end_month'], 'String');
            }
            if (data.hasOwnProperty('eu_country_code')) {
                obj['eu_country_code'] = ApiClient.convertToType(data['eu_country_code'], 'String');
            }
            if (data.hasOwnProperty('format')) {
                obj['format'] = ApiClient.convertToType(data['format'], 'String');
            }
            if (data.hasOwnProperty('fx_date_type')) {
                obj['fx_date_type'] = ApiClient.convertToType(data['fx_date_type'], 'String');
            }
            if (data.hasOwnProperty('lff_sequence_number')) {
                obj['lff_sequence_number'] = ApiClient.convertToType(data['lff_sequence_number'], 'String');
            }
            if (data.hasOwnProperty('period_length')) {
                obj['period_length'] = ApiClient.convertToType(data['period_length'], 'String');
            }
            if (data.hasOwnProperty('start_month')) {
                obj['start_month'] = ApiClient.convertToType(data['start_month'], 'String');
            }
            if (data.hasOwnProperty('tax_id')) {
                obj['tax_id'] = ApiClient.convertToType(data['tax_id'], 'String');
            }
            if (data.hasOwnProperty('transformation')) {
                obj['transformation'] = ApiClient.convertToType(data['transformation'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetEuViesReportIn</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetEuViesReportIn</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetEuViesReportIn.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['currency_code'] && !(typeof data['currency_code'] === 'string' || data['currency_code'] instanceof String)) {
            throw new Error("Expected the field `currency_code` to be a primitive type in the JSON string but got " + data['currency_code']);
        }
        // ensure the json data is a string
        if (data['end_month'] && !(typeof data['end_month'] === 'string' || data['end_month'] instanceof String)) {
            throw new Error("Expected the field `end_month` to be a primitive type in the JSON string but got " + data['end_month']);
        }
        // ensure the json data is a string
        if (data['eu_country_code'] && !(typeof data['eu_country_code'] === 'string' || data['eu_country_code'] instanceof String)) {
            throw new Error("Expected the field `eu_country_code` to be a primitive type in the JSON string but got " + data['eu_country_code']);
        }
        // ensure the json data is a string
        if (data['format'] && !(typeof data['format'] === 'string' || data['format'] instanceof String)) {
            throw new Error("Expected the field `format` to be a primitive type in the JSON string but got " + data['format']);
        }
        // ensure the json data is a string
        if (data['fx_date_type'] && !(typeof data['fx_date_type'] === 'string' || data['fx_date_type'] instanceof String)) {
            throw new Error("Expected the field `fx_date_type` to be a primitive type in the JSON string but got " + data['fx_date_type']);
        }
        // ensure the json data is a string
        if (data['lff_sequence_number'] && !(typeof data['lff_sequence_number'] === 'string' || data['lff_sequence_number'] instanceof String)) {
            throw new Error("Expected the field `lff_sequence_number` to be a primitive type in the JSON string but got " + data['lff_sequence_number']);
        }
        // ensure the json data is a string
        if (data['period_length'] && !(typeof data['period_length'] === 'string' || data['period_length'] instanceof String)) {
            throw new Error("Expected the field `period_length` to be a primitive type in the JSON string but got " + data['period_length']);
        }
        // ensure the json data is a string
        if (data['start_month'] && !(typeof data['start_month'] === 'string' || data['start_month'] instanceof String)) {
            throw new Error("Expected the field `start_month` to be a primitive type in the JSON string but got " + data['start_month']);
        }
        // ensure the json data is a string
        if (data['tax_id'] && !(typeof data['tax_id'] === 'string' || data['tax_id'] instanceof String)) {
            throw new Error("Expected the field `tax_id` to be a primitive type in the JSON string but got " + data['tax_id']);
        }
        // ensure the json data is a string
        if (data['transformation'] && !(typeof data['transformation'] === 'string' || data['transformation'] instanceof String)) {
            throw new Error("Expected the field `transformation` to be a primitive type in the JSON string but got " + data['transformation']);
        }

        return true;
    }


}

GetEuViesReportIn.RequiredProperties = ["end_month", "eu_country_code", "start_month"];

/**
 * ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
 * @member {String} currency_code
 */
GetEuViesReportIn.prototype['currency_code'] = undefined;

/**
 * Period end month in yyyy-MM format.
 * @member {String} end_month
 */
GetEuViesReportIn.prototype['end_month'] = undefined;

/**
 * ISO 2-letter country code which will be used for determining which country is domestic.
 * @member {String} eu_country_code
 */
GetEuViesReportIn.prototype['eu_country_code'] = undefined;

/**
 * Output format. 'xml', 'csv' and 'lff' (only for Ireland) values are accepted as well
 * @member {String} format
 */
GetEuViesReportIn.prototype['format'] = undefined;

/**
 * Which date should be used for FX.
 * @member {String} fx_date_type
 */
GetEuViesReportIn.prototype['fx_date_type'] = undefined;

/**
 * Sequence number used to generate report in Large Filer Format. If not specified then '0000000001' will be used.
 * @member {String} lff_sequence_number
 */
GetEuViesReportIn.prototype['lff_sequence_number'] = undefined;

/**
 * Length of report period. 'month', 'quarter' and 'year' values are accepted. Required only if Large Filer Format is requested.
 * @member {String} period_length
 */
GetEuViesReportIn.prototype['period_length'] = undefined;

/**
 * Period start month in yyyy-MM format.
 * @member {String} start_month
 */
GetEuViesReportIn.prototype['start_month'] = undefined;

/**
 * MOSS-assigned tax ID - if not provided, merchant's national tax number will be used.
 * @member {String} tax_id
 */
GetEuViesReportIn.prototype['tax_id'] = undefined;

/**
 * Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats.
 * @member {String} transformation
 */
GetEuViesReportIn.prototype['transformation'] = undefined;






export default GetEuViesReportIn;

