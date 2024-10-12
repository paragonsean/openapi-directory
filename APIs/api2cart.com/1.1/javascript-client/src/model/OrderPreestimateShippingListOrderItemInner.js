/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner from './OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner';

/**
 * The OrderPreestimateShippingListOrderItemInner model module.
 * @module model/OrderPreestimateShippingListOrderItemInner
 * @version 1.1
 */
class OrderPreestimateShippingListOrderItemInner {
    /**
     * Constructs a new <code>OrderPreestimateShippingListOrderItemInner</code>.
     * @alias module:model/OrderPreestimateShippingListOrderItemInner
     * @param orderItemId {String} Defines orders specified by order item id
     * @param orderItemQuantity {Number} Defines orders specified by order item quantity
     */
    constructor(orderItemId, orderItemQuantity) { 
        
        OrderPreestimateShippingListOrderItemInner.initialize(this, orderItemId, orderItemQuantity);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, orderItemId, orderItemQuantity) { 
        obj['order_item_id'] = orderItemId;
        obj['order_item_quantity'] = orderItemQuantity;
    }

    /**
     * Constructs a <code>OrderPreestimateShippingListOrderItemInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderPreestimateShippingListOrderItemInner} obj Optional instance to populate.
     * @return {module:model/OrderPreestimateShippingListOrderItemInner} The populated <code>OrderPreestimateShippingListOrderItemInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderPreestimateShippingListOrderItemInner();

            if (data.hasOwnProperty('order_item_id')) {
                obj['order_item_id'] = ApiClient.convertToType(data['order_item_id'], 'String');
            }
            if (data.hasOwnProperty('order_item_model')) {
                obj['order_item_model'] = ApiClient.convertToType(data['order_item_model'], 'String');
            }
            if (data.hasOwnProperty('order_item_option')) {
                obj['order_item_option'] = ApiClient.convertToType(data['order_item_option'], [OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner]);
            }
            if (data.hasOwnProperty('order_item_quantity')) {
                obj['order_item_quantity'] = ApiClient.convertToType(data['order_item_quantity'], 'Number');
            }
            if (data.hasOwnProperty('order_item_variant_id')) {
                obj['order_item_variant_id'] = ApiClient.convertToType(data['order_item_variant_id'], 'String');
            }
            if (data.hasOwnProperty('order_item_weight')) {
                obj['order_item_weight'] = ApiClient.convertToType(data['order_item_weight'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderPreestimateShippingListOrderItemInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderPreestimateShippingListOrderItemInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrderPreestimateShippingListOrderItemInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['order_item_id'] && !(typeof data['order_item_id'] === 'string' || data['order_item_id'] instanceof String)) {
            throw new Error("Expected the field `order_item_id` to be a primitive type in the JSON string but got " + data['order_item_id']);
        }
        // ensure the json data is a string
        if (data['order_item_model'] && !(typeof data['order_item_model'] === 'string' || data['order_item_model'] instanceof String)) {
            throw new Error("Expected the field `order_item_model` to be a primitive type in the JSON string but got " + data['order_item_model']);
        }
        if (data['order_item_option']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['order_item_option'])) {
                throw new Error("Expected the field `order_item_option` to be an array in the JSON data but got " + data['order_item_option']);
            }
            // validate the optional field `order_item_option` (array)
            for (const item of data['order_item_option']) {
                OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['order_item_variant_id'] && !(typeof data['order_item_variant_id'] === 'string' || data['order_item_variant_id'] instanceof String)) {
            throw new Error("Expected the field `order_item_variant_id` to be a primitive type in the JSON string but got " + data['order_item_variant_id']);
        }

        return true;
    }


}

OrderPreestimateShippingListOrderItemInner.RequiredProperties = ["order_item_id", "order_item_quantity"];

/**
 * Defines orders specified by order item id
 * @member {String} order_item_id
 */
OrderPreestimateShippingListOrderItemInner.prototype['order_item_id'] = undefined;

/**
 * Defines orders specified by order item model
 * @member {String} order_item_model
 */
OrderPreestimateShippingListOrderItemInner.prototype['order_item_model'] = undefined;

/**
 * @member {Array.<module:model/OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner>} order_item_option
 */
OrderPreestimateShippingListOrderItemInner.prototype['order_item_option'] = undefined;

/**
 * Defines orders specified by order item quantity
 * @member {Number} order_item_quantity
 */
OrderPreestimateShippingListOrderItemInner.prototype['order_item_quantity'] = undefined;

/**
 * Ordered product variant. Where x is order item ID
 * @member {String} order_item_variant_id
 */
OrderPreestimateShippingListOrderItemInner.prototype['order_item_variant_id'] = undefined;

/**
 * Defines orders specified by order item weight
 * @member {Number} order_item_weight
 */
OrderPreestimateShippingListOrderItemInner.prototype['order_item_weight'] = undefined;






export default OrderPreestimateShippingListOrderItemInner;

