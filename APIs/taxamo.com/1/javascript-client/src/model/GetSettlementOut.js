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
import Report from './Report';

/**
 * The GetSettlementOut model module.
 * @module model/GetSettlementOut
 * @version 1
 */
class GetSettlementOut {
    /**
     * Constructs a new <code>GetSettlementOut</code>.
     * @alias module:model/GetSettlementOut
     */
    constructor() { 
        
        GetSettlementOut.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetSettlementOut</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetSettlementOut} obj Optional instance to populate.
     * @return {module:model/GetSettlementOut} The populated <code>GetSettlementOut</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetSettlementOut();

            if (data.hasOwnProperty('end_date')) {
                obj['end_date'] = ApiClient.convertToType(data['end_date'], 'String');
            }
            if (data.hasOwnProperty('fx_rate_date')) {
                obj['fx_rate_date'] = ApiClient.convertToType(data['fx_rate_date'], 'String');
            }
            if (data.hasOwnProperty('indicative')) {
                obj['indicative'] = ApiClient.convertToType(data['indicative'], 'Boolean');
            }
            if (data.hasOwnProperty('report')) {
                obj['report'] = ApiClient.convertToType(data['report'], [Report]);
            }
            if (data.hasOwnProperty('start_date')) {
                obj['start_date'] = ApiClient.convertToType(data['start_date'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetSettlementOut</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetSettlementOut</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['end_date'] && !(typeof data['end_date'] === 'string' || data['end_date'] instanceof String)) {
            throw new Error("Expected the field `end_date` to be a primitive type in the JSON string but got " + data['end_date']);
        }
        // ensure the json data is a string
        if (data['fx_rate_date'] && !(typeof data['fx_rate_date'] === 'string' || data['fx_rate_date'] instanceof String)) {
            throw new Error("Expected the field `fx_rate_date` to be a primitive type in the JSON string but got " + data['fx_rate_date']);
        }
        if (data['report']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['report'])) {
                throw new Error("Expected the field `report` to be an array in the JSON data but got " + data['report']);
            }
            // validate the optional field `report` (array)
            for (const item of data['report']) {
                Report.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['start_date'] && !(typeof data['start_date'] === 'string' || data['start_date'] instanceof String)) {
            throw new Error("Expected the field `start_date` to be a primitive type in the JSON string but got " + data['start_date']);
        }

        return true;
    }


}



/**
 * Period end date in yyyy-MM-dd'T'hh:mm:ss'Z' format.
 * @member {String} end_date
 */
GetSettlementOut.prototype['end_date'] = undefined;

/**
 * Date of ECB FX rate used for conversions in yyyy-MM-dd'T'hh:mm:ss'Z' format. Applies to tax regions where 
 * @member {String} fx_rate_date
 */
GetSettlementOut.prototype['fx_rate_date'] = undefined;

/**
 * If the quarter isn't closed yet, tax amount is indicative, as we cannot determine FX rate or all transactions yet.
 * @member {Boolean} indicative
 */
GetSettlementOut.prototype['indicative'] = undefined;

/**
 * Settlement report.
 * @member {Array.<module:model/Report>} report
 */
GetSettlementOut.prototype['report'] = undefined;

/**
 * Period start date in yyyy-MM-dd'T'hh:mm:ss'Z' format.
 * @member {String} start_date
 */
GetSettlementOut.prototype['start_date'] = undefined;






export default GetSettlementOut;

