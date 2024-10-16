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
import QuoteBaseVO from './QuoteBaseVO';

/**
 * The RfqSimpleVO model module.
 * @module model/RfqSimpleVO
 * @version 1.0
 */
class RfqSimpleVO {
    /**
     * Constructs a new <code>RfqSimpleVO</code>.
     * Java type: com.noosh.nooshapi.vo.RfqSimpleVO
     * @alias module:model/RfqSimpleVO
     */
    constructor() { 
        
        RfqSimpleVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RfqSimpleVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RfqSimpleVO} obj Optional instance to populate.
     * @return {module:model/RfqSimpleVO} The populated <code>RfqSimpleVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RfqSimpleVO();

            if (data.hasOwnProperty('quotes')) {
                obj['quotes'] = ApiClient.convertToType(data['quotes'], [QuoteBaseVO]);
            }
            if (data.hasOwnProperty('received_date')) {
                obj['received_date'] = ApiClient.convertToType(data['received_date'], 'Date');
            }
            if (data.hasOwnProperty('rfq_id')) {
                obj['rfq_id'] = ApiClient.convertToType(data['rfq_id'], 'Number');
            }
            if (data.hasOwnProperty('rfq_title')) {
                obj['rfq_title'] = ApiClient.convertToType(data['rfq_title'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RfqSimpleVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RfqSimpleVO</code>.
     */
    static validateJSON(data) {
        if (data['quotes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['quotes'])) {
                throw new Error("Expected the field `quotes` to be an array in the JSON data but got " + data['quotes']);
            }
            // validate the optional field `quotes` (array)
            for (const item of data['quotes']) {
                QuoteBaseVO.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['rfq_title'] && !(typeof data['rfq_title'] === 'string' || data['rfq_title'] instanceof String)) {
            throw new Error("Expected the field `rfq_title` to be a primitive type in the JSON string but got " + data['rfq_title']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * 
 * @member {Array.<module:model/QuoteBaseVO>} quotes
 */
RfqSimpleVO.prototype['quotes'] = undefined;

/**
 * 
 * @member {Date} received_date
 */
RfqSimpleVO.prototype['received_date'] = undefined;

/**
 * 
 * @member {Number} rfq_id
 */
RfqSimpleVO.prototype['rfq_id'] = undefined;

/**
 * 
 * @member {String} rfq_title
 */
RfqSimpleVO.prototype['rfq_title'] = undefined;

/**
 * 
 * @member {String} status
 */
RfqSimpleVO.prototype['status'] = undefined;






export default RfqSimpleVO;

