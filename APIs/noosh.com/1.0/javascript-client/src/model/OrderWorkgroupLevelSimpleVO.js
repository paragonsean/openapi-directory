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
import OrderSimpleBaseVO from './OrderSimpleBaseVO';
import ProjectBaseVO from './ProjectBaseVO';
import WorkgroupBaseVO from './WorkgroupBaseVO';

/**
 * The OrderWorkgroupLevelSimpleVO model module.
 * @module model/OrderWorkgroupLevelSimpleVO
 * @version 1.0
 */
class OrderWorkgroupLevelSimpleVO {
    /**
     * Constructs a new <code>OrderWorkgroupLevelSimpleVO</code>.
     * Java type: com.noosh.nooshapi.vo.OrderWorkgroupLevelSimpleVO
     * @alias module:model/OrderWorkgroupLevelSimpleVO
     */
    constructor() { 
        
        OrderWorkgroupLevelSimpleVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderWorkgroupLevelSimpleVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderWorkgroupLevelSimpleVO} obj Optional instance to populate.
     * @return {module:model/OrderWorkgroupLevelSimpleVO} The populated <code>OrderWorkgroupLevelSimpleVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderWorkgroupLevelSimpleVO();

            if (data.hasOwnProperty('buyer_workgroup')) {
                obj['buyer_workgroup'] = WorkgroupBaseVO.constructFromObject(data['buyer_workgroup']);
            }
            if (data.hasOwnProperty('change_orders')) {
                obj['change_orders'] = ApiClient.convertToType(data['change_orders'], [OrderSimpleBaseVO]);
            }
            if (data.hasOwnProperty('closing_change_orders')) {
                obj['closing_change_orders'] = ApiClient.convertToType(data['closing_change_orders'], [OrderSimpleBaseVO]);
            }
            if (data.hasOwnProperty('comments')) {
                obj['comments'] = ApiClient.convertToType(data['comments'], 'String');
            }
            if (data.hasOwnProperty('completion_date')) {
                obj['completion_date'] = ApiClient.convertToType(data['completion_date'], 'Date');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('grand_total')) {
                obj['grand_total'] = ApiClient.convertToType(data['grand_total'], Object);
            }
            if (data.hasOwnProperty('grand_total_with_changes')) {
                obj['grand_total_with_changes'] = ApiClient.convertToType(data['grand_total_with_changes'], Object);
            }
            if (data.hasOwnProperty('last_changed')) {
                obj['last_changed'] = ApiClient.convertToType(data['last_changed'], 'Date');
            }
            if (data.hasOwnProperty('last_status_change')) {
                obj['last_status_change'] = ApiClient.convertToType(data['last_status_change'], 'Date');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'Number');
            }
            if (data.hasOwnProperty('order_number')) {
                obj['order_number'] = ApiClient.convertToType(data['order_number'], 'String');
            }
            if (data.hasOwnProperty('order_title')) {
                obj['order_title'] = ApiClient.convertToType(data['order_title'], 'String');
            }
            if (data.hasOwnProperty('payment_reference')) {
                obj['payment_reference'] = ApiClient.convertToType(data['payment_reference'], 'String');
            }
            if (data.hasOwnProperty('print_order_ids')) {
                obj['print_order_ids'] = ApiClient.convertToType(data['print_order_ids'], ['Number']);
            }
            if (data.hasOwnProperty('project')) {
                obj['project'] = ProjectBaseVO.constructFromObject(data['project']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('status_comments')) {
                obj['status_comments'] = ApiClient.convertToType(data['status_comments'], 'String');
            }
            if (data.hasOwnProperty('supplier_reference')) {
                obj['supplier_reference'] = ApiClient.convertToType(data['supplier_reference'], 'String');
            }
            if (data.hasOwnProperty('supplier_workgroup')) {
                obj['supplier_workgroup'] = WorkgroupBaseVO.constructFromObject(data['supplier_workgroup']);
            }
            if (data.hasOwnProperty('transactional_currency')) {
                obj['transactional_currency'] = ApiClient.convertToType(data['transactional_currency'], 'String');
            }
            if (data.hasOwnProperty('transactional_grand_total')) {
                obj['transactional_grand_total'] = ApiClient.convertToType(data['transactional_grand_total'], Object);
            }
            if (data.hasOwnProperty('transactional_grand_total_with_changes')) {
                obj['transactional_grand_total_with_changes'] = ApiClient.convertToType(data['transactional_grand_total_with_changes'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderWorkgroupLevelSimpleVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderWorkgroupLevelSimpleVO</code>.
     */
    static validateJSON(data) {
        // validate the optional field `buyer_workgroup`
        if (data['buyer_workgroup']) { // data not null
          WorkgroupBaseVO.validateJSON(data['buyer_workgroup']);
        }
        if (data['change_orders']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['change_orders'])) {
                throw new Error("Expected the field `change_orders` to be an array in the JSON data but got " + data['change_orders']);
            }
            // validate the optional field `change_orders` (array)
            for (const item of data['change_orders']) {
                OrderSimpleBaseVO.validateJSON(item);
            };
        }
        if (data['closing_change_orders']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['closing_change_orders'])) {
                throw new Error("Expected the field `closing_change_orders` to be an array in the JSON data but got " + data['closing_change_orders']);
            }
            // validate the optional field `closing_change_orders` (array)
            for (const item of data['closing_change_orders']) {
                OrderSimpleBaseVO.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['comments'] && !(typeof data['comments'] === 'string' || data['comments'] instanceof String)) {
            throw new Error("Expected the field `comments` to be a primitive type in the JSON string but got " + data['comments']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // ensure the json data is a string
        if (data['order_number'] && !(typeof data['order_number'] === 'string' || data['order_number'] instanceof String)) {
            throw new Error("Expected the field `order_number` to be a primitive type in the JSON string but got " + data['order_number']);
        }
        // ensure the json data is a string
        if (data['order_title'] && !(typeof data['order_title'] === 'string' || data['order_title'] instanceof String)) {
            throw new Error("Expected the field `order_title` to be a primitive type in the JSON string but got " + data['order_title']);
        }
        // ensure the json data is a string
        if (data['payment_reference'] && !(typeof data['payment_reference'] === 'string' || data['payment_reference'] instanceof String)) {
            throw new Error("Expected the field `payment_reference` to be a primitive type in the JSON string but got " + data['payment_reference']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['print_order_ids'])) {
            throw new Error("Expected the field `print_order_ids` to be an array in the JSON data but got " + data['print_order_ids']);
        }
        // validate the optional field `project`
        if (data['project']) { // data not null
          ProjectBaseVO.validateJSON(data['project']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['status_comments'] && !(typeof data['status_comments'] === 'string' || data['status_comments'] instanceof String)) {
            throw new Error("Expected the field `status_comments` to be a primitive type in the JSON string but got " + data['status_comments']);
        }
        // ensure the json data is a string
        if (data['supplier_reference'] && !(typeof data['supplier_reference'] === 'string' || data['supplier_reference'] instanceof String)) {
            throw new Error("Expected the field `supplier_reference` to be a primitive type in the JSON string but got " + data['supplier_reference']);
        }
        // validate the optional field `supplier_workgroup`
        if (data['supplier_workgroup']) { // data not null
          WorkgroupBaseVO.validateJSON(data['supplier_workgroup']);
        }
        // ensure the json data is a string
        if (data['transactional_currency'] && !(typeof data['transactional_currency'] === 'string' || data['transactional_currency'] instanceof String)) {
            throw new Error("Expected the field `transactional_currency` to be a primitive type in the JSON string but got " + data['transactional_currency']);
        }

        return true;
    }


}



/**
 * @member {module:model/WorkgroupBaseVO} buyer_workgroup
 */
OrderWorkgroupLevelSimpleVO.prototype['buyer_workgroup'] = undefined;

/**
 * 
 * @member {Array.<module:model/OrderSimpleBaseVO>} change_orders
 */
OrderWorkgroupLevelSimpleVO.prototype['change_orders'] = undefined;

/**
 * 
 * @member {Array.<module:model/OrderSimpleBaseVO>} closing_change_orders
 */
OrderWorkgroupLevelSimpleVO.prototype['closing_change_orders'] = undefined;

/**
 * 
 * @member {String} comments
 */
OrderWorkgroupLevelSimpleVO.prototype['comments'] = undefined;

/**
 * 
 * @member {Date} completion_date
 */
OrderWorkgroupLevelSimpleVO.prototype['completion_date'] = undefined;

/**
 * 
 * @member {String} currency
 */
OrderWorkgroupLevelSimpleVO.prototype['currency'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} grand_total
 */
OrderWorkgroupLevelSimpleVO.prototype['grand_total'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} grand_total_with_changes
 */
OrderWorkgroupLevelSimpleVO.prototype['grand_total_with_changes'] = undefined;

/**
 * 
 * @member {Date} last_changed
 */
OrderWorkgroupLevelSimpleVO.prototype['last_changed'] = undefined;

/**
 * 
 * @member {Date} last_status_change
 */
OrderWorkgroupLevelSimpleVO.prototype['last_status_change'] = undefined;

/**
 * 
 * @member {Number} order_id
 */
OrderWorkgroupLevelSimpleVO.prototype['order_id'] = undefined;

/**
 * 
 * @member {String} order_number
 */
OrderWorkgroupLevelSimpleVO.prototype['order_number'] = undefined;

/**
 * 
 * @member {String} order_title
 */
OrderWorkgroupLevelSimpleVO.prototype['order_title'] = undefined;

/**
 * 
 * @member {String} payment_reference
 */
OrderWorkgroupLevelSimpleVO.prototype['payment_reference'] = undefined;

/**
 * 
 * @member {Array.<Number>} print_order_ids
 */
OrderWorkgroupLevelSimpleVO.prototype['print_order_ids'] = undefined;

/**
 * @member {module:model/ProjectBaseVO} project
 */
OrderWorkgroupLevelSimpleVO.prototype['project'] = undefined;

/**
 * 
 * @member {String} status
 */
OrderWorkgroupLevelSimpleVO.prototype['status'] = undefined;

/**
 * 
 * @member {String} status_comments
 */
OrderWorkgroupLevelSimpleVO.prototype['status_comments'] = undefined;

/**
 * 
 * @member {String} supplier_reference
 */
OrderWorkgroupLevelSimpleVO.prototype['supplier_reference'] = undefined;

/**
 * @member {module:model/WorkgroupBaseVO} supplier_workgroup
 */
OrderWorkgroupLevelSimpleVO.prototype['supplier_workgroup'] = undefined;

/**
 * 
 * @member {String} transactional_currency
 */
OrderWorkgroupLevelSimpleVO.prototype['transactional_currency'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_grand_total
 */
OrderWorkgroupLevelSimpleVO.prototype['transactional_grand_total'] = undefined;

/**
 * Java type: java.math.BigDecimal
 * @member {Object} transactional_grand_total_with_changes
 */
OrderWorkgroupLevelSimpleVO.prototype['transactional_grand_total_with_changes'] = undefined;






export default OrderWorkgroupLevelSimpleVO;

