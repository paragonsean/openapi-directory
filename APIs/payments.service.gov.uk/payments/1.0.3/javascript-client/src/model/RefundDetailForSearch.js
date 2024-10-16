/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RefundLinksForSearch from './RefundLinksForSearch';
import RefundSettlementSummary from './RefundSettlementSummary';

/**
 * The RefundDetailForSearch model module.
 * @module model/RefundDetailForSearch
 * @version 1.0.3
 */
class RefundDetailForSearch {
    /**
     * Constructs a new <code>RefundDetailForSearch</code>.
     * @alias module:model/RefundDetailForSearch
     */
    constructor() { 
        
        RefundDetailForSearch.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RefundDetailForSearch</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RefundDetailForSearch} obj Optional instance to populate.
     * @return {module:model/RefundDetailForSearch} The populated <code>RefundDetailForSearch</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RefundDetailForSearch();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = RefundLinksForSearch.constructFromObject(data['_links']);
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('created_date')) {
                obj['created_date'] = ApiClient.convertToType(data['created_date'], 'String');
            }
            if (data.hasOwnProperty('refund_id')) {
                obj['refund_id'] = ApiClient.convertToType(data['refund_id'], 'String');
            }
            if (data.hasOwnProperty('settlement_summary')) {
                obj['settlement_summary'] = RefundSettlementSummary.constructFromObject(data['settlement_summary']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RefundDetailForSearch</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RefundDetailForSearch</code>.
     */
    static validateJSON(data) {
        // validate the optional field `_links`
        if (data['_links']) { // data not null
          RefundLinksForSearch.validateJSON(data['_links']);
        }
        // ensure the json data is a string
        if (data['created_date'] && !(typeof data['created_date'] === 'string' || data['created_date'] instanceof String)) {
            throw new Error("Expected the field `created_date` to be a primitive type in the JSON string but got " + data['created_date']);
        }
        // ensure the json data is a string
        if (data['refund_id'] && !(typeof data['refund_id'] === 'string' || data['refund_id'] instanceof String)) {
            throw new Error("Expected the field `refund_id` to be a primitive type in the JSON string but got " + data['refund_id']);
        }
        // validate the optional field `settlement_summary`
        if (data['settlement_summary']) { // data not null
          RefundSettlementSummary.validateJSON(data['settlement_summary']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * @member {module:model/RefundLinksForSearch} _links
 */
RefundDetailForSearch.prototype['_links'] = undefined;

/**
 * @member {Number} amount
 */
RefundDetailForSearch.prototype['amount'] = undefined;

/**
 * @member {String} created_date
 */
RefundDetailForSearch.prototype['created_date'] = undefined;

/**
 * @member {String} refund_id
 */
RefundDetailForSearch.prototype['refund_id'] = undefined;

/**
 * @member {module:model/RefundSettlementSummary} settlement_summary
 */
RefundDetailForSearch.prototype['settlement_summary'] = undefined;

/**
 * @member {module:model/RefundDetailForSearch.StatusEnum} status
 */
RefundDetailForSearch.prototype['status'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
RefundDetailForSearch['StatusEnum'] = {

    /**
     * value: "submitted"
     * @const
     */
    "submitted": "submitted",

    /**
     * value: "success"
     * @const
     */
    "success": "success",

    /**
     * value: "error"
     * @const
     */
    "error": "error"
};



export default RefundDetailForSearch;

