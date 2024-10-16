/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The QuoteBaseVO model module.
 * @module model/QuoteBaseVO
 * @version 1.0
 */
class QuoteBaseVO {
    /**
     * Constructs a new <code>QuoteBaseVO</code>.
     * Java type: com.noosh.nooshapi.vo.QuoteBaseVO
     * @alias module:model/QuoteBaseVO
     */
    constructor() { 
        
        QuoteBaseVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>QuoteBaseVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/QuoteBaseVO} obj Optional instance to populate.
     * @return {module:model/QuoteBaseVO} The populated <code>QuoteBaseVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new QuoteBaseVO();

            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('grand_total')) {
                obj['grand_total'] = ApiClient.convertToType(data['grand_total'], Object);
            }
            if (data.hasOwnProperty('quote_id')) {
                obj['quote_id'] = ApiClient.convertToType(data['quote_id'], 'Number');
            }
            if (data.hasOwnProperty('quote_title')) {
                obj['quote_title'] = ApiClient.convertToType(data['quote_title'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('submit_date')) {
                obj['submit_date'] = ApiClient.convertToType(data['submit_date'], 'Date');
            }
            if (data.hasOwnProperty('transactional_currency')) {
                obj['transactional_currency'] = ApiClient.convertToType(data['transactional_currency'], 'String');
            }
            if (data.hasOwnProperty('transactional_grand_total')) {
                obj['transactional_grand_total'] = ApiClient.convertToType(data['transactional_grand_total'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>QuoteBaseVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>QuoteBaseVO</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // ensure the json data is a string
        if (data['quote_title'] && !(typeof data['quote_title'] === 'string' || data['quote_title'] instanceof String)) {
            throw new Error("Expected the field `quote_title` to be a primitive type in the JSON string but got " + data['quote_title']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['transactional_currency'] && !(typeof data['transactional_currency'] === 'string' || data['transactional_currency'] instanceof String)) {
            throw new Error("Expected the field `transactional_currency` to be a primitive type in the JSON string but got " + data['transactional_currency']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} currency
 */
QuoteBaseVO.prototype['currency'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} grand_total
 */
QuoteBaseVO.prototype['grand_total'] = undefined;

/**
 * 
 * @member {Number} quote_id
 */
QuoteBaseVO.prototype['quote_id'] = undefined;

/**
 * 
 * @member {String} quote_title
 */
QuoteBaseVO.prototype['quote_title'] = undefined;

/**
 * 
 * @member {String} status
 */
QuoteBaseVO.prototype['status'] = undefined;

/**
 * 
 * @member {Date} submit_date
 */
QuoteBaseVO.prototype['submit_date'] = undefined;

/**
 * 
 * @member {String} transactional_currency
 */
QuoteBaseVO.prototype['transactional_currency'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_grand_total
 */
QuoteBaseVO.prototype['transactional_grand_total'] = undefined;






export default QuoteBaseVO;

