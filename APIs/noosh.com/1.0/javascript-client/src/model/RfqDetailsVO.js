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
import RfqItemBaseVO from './RfqItemBaseVO';

/**
 * The RfqDetailsVO model module.
 * @module model/RfqDetailsVO
 * @version 1.0
 */
class RfqDetailsVO {
    /**
     * Constructs a new <code>RfqDetailsVO</code>.
     * Java type: com.noosh.nooshapi.vo.RfqDetailsVO
     * @alias module:model/RfqDetailsVO
     */
    constructor() { 
        
        RfqDetailsVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RfqDetailsVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RfqDetailsVO} obj Optional instance to populate.
     * @return {module:model/RfqDetailsVO} The populated <code>RfqDetailsVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RfqDetailsVO();

            if (data.hasOwnProperty('comments')) {
                obj['comments'] = ApiClient.convertToType(data['comments'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('proposed_completion_date')) {
                obj['proposed_completion_date'] = ApiClient.convertToType(data['proposed_completion_date'], 'Date');
            }
            if (data.hasOwnProperty('quote_due_date')) {
                obj['quote_due_date'] = ApiClient.convertToType(data['quote_due_date'], 'Date');
            }
            if (data.hasOwnProperty('quotes')) {
                obj['quotes'] = ApiClient.convertToType(data['quotes'], [QuoteBaseVO]);
            }
            if (data.hasOwnProperty('received_date')) {
                obj['received_date'] = ApiClient.convertToType(data['received_date'], 'Date');
            }
            if (data.hasOwnProperty('recipient_name')) {
                obj['recipient_name'] = ApiClient.convertToType(data['recipient_name'], 'String');
            }
            if (data.hasOwnProperty('requestor_name')) {
                obj['requestor_name'] = ApiClient.convertToType(data['requestor_name'], 'String');
            }
            if (data.hasOwnProperty('rfq_id')) {
                obj['rfq_id'] = ApiClient.convertToType(data['rfq_id'], 'Number');
            }
            if (data.hasOwnProperty('rfq_items')) {
                obj['rfq_items'] = ApiClient.convertToType(data['rfq_items'], [RfqItemBaseVO]);
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
     * Validates the JSON data with respect to <code>RfqDetailsVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RfqDetailsVO</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['comments'] && !(typeof data['comments'] === 'string' || data['comments'] instanceof String)) {
            throw new Error("Expected the field `comments` to be a primitive type in the JSON string but got " + data['comments']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
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
        if (data['recipient_name'] && !(typeof data['recipient_name'] === 'string' || data['recipient_name'] instanceof String)) {
            throw new Error("Expected the field `recipient_name` to be a primitive type in the JSON string but got " + data['recipient_name']);
        }
        // ensure the json data is a string
        if (data['requestor_name'] && !(typeof data['requestor_name'] === 'string' || data['requestor_name'] instanceof String)) {
            throw new Error("Expected the field `requestor_name` to be a primitive type in the JSON string but got " + data['requestor_name']);
        }
        if (data['rfq_items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rfq_items'])) {
                throw new Error("Expected the field `rfq_items` to be an array in the JSON data but got " + data['rfq_items']);
            }
            // validate the optional field `rfq_items` (array)
            for (const item of data['rfq_items']) {
                RfqItemBaseVO.validateJSON(item);
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
 * @member {String} comments
 */
RfqDetailsVO.prototype['comments'] = undefined;

/**
 * 
 * @member {String} description
 */
RfqDetailsVO.prototype['description'] = undefined;

/**
 * 
 * @member {Date} proposed_completion_date
 */
RfqDetailsVO.prototype['proposed_completion_date'] = undefined;

/**
 * 
 * @member {Date} quote_due_date
 */
RfqDetailsVO.prototype['quote_due_date'] = undefined;

/**
 * 
 * @member {Array.<module:model/QuoteBaseVO>} quotes
 */
RfqDetailsVO.prototype['quotes'] = undefined;

/**
 * 
 * @member {Date} received_date
 */
RfqDetailsVO.prototype['received_date'] = undefined;

/**
 * 
 * @member {String} recipient_name
 */
RfqDetailsVO.prototype['recipient_name'] = undefined;

/**
 * 
 * @member {String} requestor_name
 */
RfqDetailsVO.prototype['requestor_name'] = undefined;

/**
 * 
 * @member {Number} rfq_id
 */
RfqDetailsVO.prototype['rfq_id'] = undefined;

/**
 * 
 * @member {Array.<module:model/RfqItemBaseVO>} rfq_items
 */
RfqDetailsVO.prototype['rfq_items'] = undefined;

/**
 * 
 * @member {String} rfq_title
 */
RfqDetailsVO.prototype['rfq_title'] = undefined;

/**
 * 
 * @member {String} status
 */
RfqDetailsVO.prototype['status'] = undefined;






export default RfqDetailsVO;

