/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CatalogDataProductOptionInterface from './CatalogDataProductOptionInterface';
import SalesDataOrderItemExtensionInterface from './SalesDataOrderItemExtensionInterface';

/**
 * The SalesDataOrderItemInterface model module.
 * @module model/SalesDataOrderItemInterface
 * @version 2.2.10
 */
class SalesDataOrderItemInterface {
    /**
     * Constructs a new <code>SalesDataOrderItemInterface</code>.
     * Order item interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.
     * @alias module:model/SalesDataOrderItemInterface
     * @param sku {String} SKU.
     */
    constructor(sku) { 
        
        SalesDataOrderItemInterface.initialize(this, sku);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, sku) { 
        obj['sku'] = sku;
    }

    /**
     * Constructs a <code>SalesDataOrderItemInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesDataOrderItemInterface} obj Optional instance to populate.
     * @return {module:model/SalesDataOrderItemInterface} The populated <code>SalesDataOrderItemInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesDataOrderItemInterface();

            if (data.hasOwnProperty('additional_data')) {
                obj['additional_data'] = ApiClient.convertToType(data['additional_data'], 'String');
            }
            if (data.hasOwnProperty('amount_refunded')) {
                obj['amount_refunded'] = ApiClient.convertToType(data['amount_refunded'], 'Number');
            }
            if (data.hasOwnProperty('applied_rule_ids')) {
                obj['applied_rule_ids'] = ApiClient.convertToType(data['applied_rule_ids'], 'String');
            }
            if (data.hasOwnProperty('base_amount_refunded')) {
                obj['base_amount_refunded'] = ApiClient.convertToType(data['base_amount_refunded'], 'Number');
            }
            if (data.hasOwnProperty('base_cost')) {
                obj['base_cost'] = ApiClient.convertToType(data['base_cost'], 'Number');
            }
            if (data.hasOwnProperty('base_discount_amount')) {
                obj['base_discount_amount'] = ApiClient.convertToType(data['base_discount_amount'], 'Number');
            }
            if (data.hasOwnProperty('base_discount_invoiced')) {
                obj['base_discount_invoiced'] = ApiClient.convertToType(data['base_discount_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('base_discount_refunded')) {
                obj['base_discount_refunded'] = ApiClient.convertToType(data['base_discount_refunded'], 'Number');
            }
            if (data.hasOwnProperty('base_discount_tax_compensation_amount')) {
                obj['base_discount_tax_compensation_amount'] = ApiClient.convertToType(data['base_discount_tax_compensation_amount'], 'Number');
            }
            if (data.hasOwnProperty('base_discount_tax_compensation_invoiced')) {
                obj['base_discount_tax_compensation_invoiced'] = ApiClient.convertToType(data['base_discount_tax_compensation_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('base_discount_tax_compensation_refunded')) {
                obj['base_discount_tax_compensation_refunded'] = ApiClient.convertToType(data['base_discount_tax_compensation_refunded'], 'Number');
            }
            if (data.hasOwnProperty('base_original_price')) {
                obj['base_original_price'] = ApiClient.convertToType(data['base_original_price'], 'Number');
            }
            if (data.hasOwnProperty('base_price')) {
                obj['base_price'] = ApiClient.convertToType(data['base_price'], 'Number');
            }
            if (data.hasOwnProperty('base_price_incl_tax')) {
                obj['base_price_incl_tax'] = ApiClient.convertToType(data['base_price_incl_tax'], 'Number');
            }
            if (data.hasOwnProperty('base_row_invoiced')) {
                obj['base_row_invoiced'] = ApiClient.convertToType(data['base_row_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('base_row_total')) {
                obj['base_row_total'] = ApiClient.convertToType(data['base_row_total'], 'Number');
            }
            if (data.hasOwnProperty('base_row_total_incl_tax')) {
                obj['base_row_total_incl_tax'] = ApiClient.convertToType(data['base_row_total_incl_tax'], 'Number');
            }
            if (data.hasOwnProperty('base_tax_amount')) {
                obj['base_tax_amount'] = ApiClient.convertToType(data['base_tax_amount'], 'Number');
            }
            if (data.hasOwnProperty('base_tax_before_discount')) {
                obj['base_tax_before_discount'] = ApiClient.convertToType(data['base_tax_before_discount'], 'Number');
            }
            if (data.hasOwnProperty('base_tax_invoiced')) {
                obj['base_tax_invoiced'] = ApiClient.convertToType(data['base_tax_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('base_tax_refunded')) {
                obj['base_tax_refunded'] = ApiClient.convertToType(data['base_tax_refunded'], 'Number');
            }
            if (data.hasOwnProperty('base_weee_tax_applied_amount')) {
                obj['base_weee_tax_applied_amount'] = ApiClient.convertToType(data['base_weee_tax_applied_amount'], 'Number');
            }
            if (data.hasOwnProperty('base_weee_tax_applied_row_amnt')) {
                obj['base_weee_tax_applied_row_amnt'] = ApiClient.convertToType(data['base_weee_tax_applied_row_amnt'], 'Number');
            }
            if (data.hasOwnProperty('base_weee_tax_disposition')) {
                obj['base_weee_tax_disposition'] = ApiClient.convertToType(data['base_weee_tax_disposition'], 'Number');
            }
            if (data.hasOwnProperty('base_weee_tax_row_disposition')) {
                obj['base_weee_tax_row_disposition'] = ApiClient.convertToType(data['base_weee_tax_row_disposition'], 'Number');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('discount_amount')) {
                obj['discount_amount'] = ApiClient.convertToType(data['discount_amount'], 'Number');
            }
            if (data.hasOwnProperty('discount_invoiced')) {
                obj['discount_invoiced'] = ApiClient.convertToType(data['discount_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('discount_percent')) {
                obj['discount_percent'] = ApiClient.convertToType(data['discount_percent'], 'Number');
            }
            if (data.hasOwnProperty('discount_refunded')) {
                obj['discount_refunded'] = ApiClient.convertToType(data['discount_refunded'], 'Number');
            }
            if (data.hasOwnProperty('discount_tax_compensation_amount')) {
                obj['discount_tax_compensation_amount'] = ApiClient.convertToType(data['discount_tax_compensation_amount'], 'Number');
            }
            if (data.hasOwnProperty('discount_tax_compensation_canceled')) {
                obj['discount_tax_compensation_canceled'] = ApiClient.convertToType(data['discount_tax_compensation_canceled'], 'Number');
            }
            if (data.hasOwnProperty('discount_tax_compensation_invoiced')) {
                obj['discount_tax_compensation_invoiced'] = ApiClient.convertToType(data['discount_tax_compensation_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('discount_tax_compensation_refunded')) {
                obj['discount_tax_compensation_refunded'] = ApiClient.convertToType(data['discount_tax_compensation_refunded'], 'Number');
            }
            if (data.hasOwnProperty('event_id')) {
                obj['event_id'] = ApiClient.convertToType(data['event_id'], 'Number');
            }
            if (data.hasOwnProperty('ext_order_item_id')) {
                obj['ext_order_item_id'] = ApiClient.convertToType(data['ext_order_item_id'], 'String');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = SalesDataOrderItemExtensionInterface.constructFromObject(data['extension_attributes']);
            }
            if (data.hasOwnProperty('free_shipping')) {
                obj['free_shipping'] = ApiClient.convertToType(data['free_shipping'], 'Number');
            }
            if (data.hasOwnProperty('gw_base_price')) {
                obj['gw_base_price'] = ApiClient.convertToType(data['gw_base_price'], 'Number');
            }
            if (data.hasOwnProperty('gw_base_price_invoiced')) {
                obj['gw_base_price_invoiced'] = ApiClient.convertToType(data['gw_base_price_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('gw_base_price_refunded')) {
                obj['gw_base_price_refunded'] = ApiClient.convertToType(data['gw_base_price_refunded'], 'Number');
            }
            if (data.hasOwnProperty('gw_base_tax_amount')) {
                obj['gw_base_tax_amount'] = ApiClient.convertToType(data['gw_base_tax_amount'], 'Number');
            }
            if (data.hasOwnProperty('gw_base_tax_amount_invoiced')) {
                obj['gw_base_tax_amount_invoiced'] = ApiClient.convertToType(data['gw_base_tax_amount_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('gw_base_tax_amount_refunded')) {
                obj['gw_base_tax_amount_refunded'] = ApiClient.convertToType(data['gw_base_tax_amount_refunded'], 'Number');
            }
            if (data.hasOwnProperty('gw_id')) {
                obj['gw_id'] = ApiClient.convertToType(data['gw_id'], 'Number');
            }
            if (data.hasOwnProperty('gw_price')) {
                obj['gw_price'] = ApiClient.convertToType(data['gw_price'], 'Number');
            }
            if (data.hasOwnProperty('gw_price_invoiced')) {
                obj['gw_price_invoiced'] = ApiClient.convertToType(data['gw_price_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('gw_price_refunded')) {
                obj['gw_price_refunded'] = ApiClient.convertToType(data['gw_price_refunded'], 'Number');
            }
            if (data.hasOwnProperty('gw_tax_amount')) {
                obj['gw_tax_amount'] = ApiClient.convertToType(data['gw_tax_amount'], 'Number');
            }
            if (data.hasOwnProperty('gw_tax_amount_invoiced')) {
                obj['gw_tax_amount_invoiced'] = ApiClient.convertToType(data['gw_tax_amount_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('gw_tax_amount_refunded')) {
                obj['gw_tax_amount_refunded'] = ApiClient.convertToType(data['gw_tax_amount_refunded'], 'Number');
            }
            if (data.hasOwnProperty('is_qty_decimal')) {
                obj['is_qty_decimal'] = ApiClient.convertToType(data['is_qty_decimal'], 'Number');
            }
            if (data.hasOwnProperty('is_virtual')) {
                obj['is_virtual'] = ApiClient.convertToType(data['is_virtual'], 'Number');
            }
            if (data.hasOwnProperty('item_id')) {
                obj['item_id'] = ApiClient.convertToType(data['item_id'], 'Number');
            }
            if (data.hasOwnProperty('locked_do_invoice')) {
                obj['locked_do_invoice'] = ApiClient.convertToType(data['locked_do_invoice'], 'Number');
            }
            if (data.hasOwnProperty('locked_do_ship')) {
                obj['locked_do_ship'] = ApiClient.convertToType(data['locked_do_ship'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('no_discount')) {
                obj['no_discount'] = ApiClient.convertToType(data['no_discount'], 'Number');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'Number');
            }
            if (data.hasOwnProperty('original_price')) {
                obj['original_price'] = ApiClient.convertToType(data['original_price'], 'Number');
            }
            if (data.hasOwnProperty('parent_item')) {
                obj['parent_item'] = SalesDataOrderItemInterface.constructFromObject(data['parent_item']);
            }
            if (data.hasOwnProperty('parent_item_id')) {
                obj['parent_item_id'] = ApiClient.convertToType(data['parent_item_id'], 'Number');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('price_incl_tax')) {
                obj['price_incl_tax'] = ApiClient.convertToType(data['price_incl_tax'], 'Number');
            }
            if (data.hasOwnProperty('product_id')) {
                obj['product_id'] = ApiClient.convertToType(data['product_id'], 'Number');
            }
            if (data.hasOwnProperty('product_option')) {
                obj['product_option'] = CatalogDataProductOptionInterface.constructFromObject(data['product_option']);
            }
            if (data.hasOwnProperty('product_type')) {
                obj['product_type'] = ApiClient.convertToType(data['product_type'], 'String');
            }
            if (data.hasOwnProperty('qty_backordered')) {
                obj['qty_backordered'] = ApiClient.convertToType(data['qty_backordered'], 'Number');
            }
            if (data.hasOwnProperty('qty_canceled')) {
                obj['qty_canceled'] = ApiClient.convertToType(data['qty_canceled'], 'Number');
            }
            if (data.hasOwnProperty('qty_invoiced')) {
                obj['qty_invoiced'] = ApiClient.convertToType(data['qty_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('qty_ordered')) {
                obj['qty_ordered'] = ApiClient.convertToType(data['qty_ordered'], 'Number');
            }
            if (data.hasOwnProperty('qty_refunded')) {
                obj['qty_refunded'] = ApiClient.convertToType(data['qty_refunded'], 'Number');
            }
            if (data.hasOwnProperty('qty_returned')) {
                obj['qty_returned'] = ApiClient.convertToType(data['qty_returned'], 'Number');
            }
            if (data.hasOwnProperty('qty_shipped')) {
                obj['qty_shipped'] = ApiClient.convertToType(data['qty_shipped'], 'Number');
            }
            if (data.hasOwnProperty('quote_item_id')) {
                obj['quote_item_id'] = ApiClient.convertToType(data['quote_item_id'], 'Number');
            }
            if (data.hasOwnProperty('row_invoiced')) {
                obj['row_invoiced'] = ApiClient.convertToType(data['row_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('row_total')) {
                obj['row_total'] = ApiClient.convertToType(data['row_total'], 'Number');
            }
            if (data.hasOwnProperty('row_total_incl_tax')) {
                obj['row_total_incl_tax'] = ApiClient.convertToType(data['row_total_incl_tax'], 'Number');
            }
            if (data.hasOwnProperty('row_weight')) {
                obj['row_weight'] = ApiClient.convertToType(data['row_weight'], 'Number');
            }
            if (data.hasOwnProperty('sku')) {
                obj['sku'] = ApiClient.convertToType(data['sku'], 'String');
            }
            if (data.hasOwnProperty('store_id')) {
                obj['store_id'] = ApiClient.convertToType(data['store_id'], 'Number');
            }
            if (data.hasOwnProperty('tax_amount')) {
                obj['tax_amount'] = ApiClient.convertToType(data['tax_amount'], 'Number');
            }
            if (data.hasOwnProperty('tax_before_discount')) {
                obj['tax_before_discount'] = ApiClient.convertToType(data['tax_before_discount'], 'Number');
            }
            if (data.hasOwnProperty('tax_canceled')) {
                obj['tax_canceled'] = ApiClient.convertToType(data['tax_canceled'], 'Number');
            }
            if (data.hasOwnProperty('tax_invoiced')) {
                obj['tax_invoiced'] = ApiClient.convertToType(data['tax_invoiced'], 'Number');
            }
            if (data.hasOwnProperty('tax_percent')) {
                obj['tax_percent'] = ApiClient.convertToType(data['tax_percent'], 'Number');
            }
            if (data.hasOwnProperty('tax_refunded')) {
                obj['tax_refunded'] = ApiClient.convertToType(data['tax_refunded'], 'Number');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
            if (data.hasOwnProperty('weee_tax_applied')) {
                obj['weee_tax_applied'] = ApiClient.convertToType(data['weee_tax_applied'], 'String');
            }
            if (data.hasOwnProperty('weee_tax_applied_amount')) {
                obj['weee_tax_applied_amount'] = ApiClient.convertToType(data['weee_tax_applied_amount'], 'Number');
            }
            if (data.hasOwnProperty('weee_tax_applied_row_amount')) {
                obj['weee_tax_applied_row_amount'] = ApiClient.convertToType(data['weee_tax_applied_row_amount'], 'Number');
            }
            if (data.hasOwnProperty('weee_tax_disposition')) {
                obj['weee_tax_disposition'] = ApiClient.convertToType(data['weee_tax_disposition'], 'Number');
            }
            if (data.hasOwnProperty('weee_tax_row_disposition')) {
                obj['weee_tax_row_disposition'] = ApiClient.convertToType(data['weee_tax_row_disposition'], 'Number');
            }
            if (data.hasOwnProperty('weight')) {
                obj['weight'] = ApiClient.convertToType(data['weight'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesDataOrderItemInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesDataOrderItemInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SalesDataOrderItemInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['additional_data'] && !(typeof data['additional_data'] === 'string' || data['additional_data'] instanceof String)) {
            throw new Error("Expected the field `additional_data` to be a primitive type in the JSON string but got " + data['additional_data']);
        }
        // ensure the json data is a string
        if (data['applied_rule_ids'] && !(typeof data['applied_rule_ids'] === 'string' || data['applied_rule_ids'] instanceof String)) {
            throw new Error("Expected the field `applied_rule_ids` to be a primitive type in the JSON string but got " + data['applied_rule_ids']);
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['ext_order_item_id'] && !(typeof data['ext_order_item_id'] === 'string' || data['ext_order_item_id'] instanceof String)) {
            throw new Error("Expected the field `ext_order_item_id` to be a primitive type in the JSON string but got " + data['ext_order_item_id']);
        }
        // validate the optional field `extension_attributes`
        if (data['extension_attributes']) { // data not null
          SalesDataOrderItemExtensionInterface.validateJSON(data['extension_attributes']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `parent_item`
        if (data['parent_item']) { // data not null
          SalesDataOrderItemInterface.validateJSON(data['parent_item']);
        }
        // validate the optional field `product_option`
        if (data['product_option']) { // data not null
          CatalogDataProductOptionInterface.validateJSON(data['product_option']);
        }
        // ensure the json data is a string
        if (data['product_type'] && !(typeof data['product_type'] === 'string' || data['product_type'] instanceof String)) {
            throw new Error("Expected the field `product_type` to be a primitive type in the JSON string but got " + data['product_type']);
        }
        // ensure the json data is a string
        if (data['sku'] && !(typeof data['sku'] === 'string' || data['sku'] instanceof String)) {
            throw new Error("Expected the field `sku` to be a primitive type in the JSON string but got " + data['sku']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }
        // ensure the json data is a string
        if (data['weee_tax_applied'] && !(typeof data['weee_tax_applied'] === 'string' || data['weee_tax_applied'] instanceof String)) {
            throw new Error("Expected the field `weee_tax_applied` to be a primitive type in the JSON string but got " + data['weee_tax_applied']);
        }

        return true;
    }


}

SalesDataOrderItemInterface.RequiredProperties = ["sku"];

/**
 * Additional data.
 * @member {String} additional_data
 */
SalesDataOrderItemInterface.prototype['additional_data'] = undefined;

/**
 * Amount refunded.
 * @member {Number} amount_refunded
 */
SalesDataOrderItemInterface.prototype['amount_refunded'] = undefined;

/**
 * Applied rule IDs.
 * @member {String} applied_rule_ids
 */
SalesDataOrderItemInterface.prototype['applied_rule_ids'] = undefined;

/**
 * Base amount refunded.
 * @member {Number} base_amount_refunded
 */
SalesDataOrderItemInterface.prototype['base_amount_refunded'] = undefined;

/**
 * Base cost.
 * @member {Number} base_cost
 */
SalesDataOrderItemInterface.prototype['base_cost'] = undefined;

/**
 * Base discount amount.
 * @member {Number} base_discount_amount
 */
SalesDataOrderItemInterface.prototype['base_discount_amount'] = undefined;

/**
 * Base discount invoiced.
 * @member {Number} base_discount_invoiced
 */
SalesDataOrderItemInterface.prototype['base_discount_invoiced'] = undefined;

/**
 * Base discount refunded.
 * @member {Number} base_discount_refunded
 */
SalesDataOrderItemInterface.prototype['base_discount_refunded'] = undefined;

/**
 * Base discount tax compensation amount.
 * @member {Number} base_discount_tax_compensation_amount
 */
SalesDataOrderItemInterface.prototype['base_discount_tax_compensation_amount'] = undefined;

/**
 * Base discount tax compensation invoiced.
 * @member {Number} base_discount_tax_compensation_invoiced
 */
SalesDataOrderItemInterface.prototype['base_discount_tax_compensation_invoiced'] = undefined;

/**
 * Base discount tax compensation refunded.
 * @member {Number} base_discount_tax_compensation_refunded
 */
SalesDataOrderItemInterface.prototype['base_discount_tax_compensation_refunded'] = undefined;

/**
 * Base original price.
 * @member {Number} base_original_price
 */
SalesDataOrderItemInterface.prototype['base_original_price'] = undefined;

/**
 * Base price.
 * @member {Number} base_price
 */
SalesDataOrderItemInterface.prototype['base_price'] = undefined;

/**
 * Base price including tax.
 * @member {Number} base_price_incl_tax
 */
SalesDataOrderItemInterface.prototype['base_price_incl_tax'] = undefined;

/**
 * Base row invoiced.
 * @member {Number} base_row_invoiced
 */
SalesDataOrderItemInterface.prototype['base_row_invoiced'] = undefined;

/**
 * Base row total.
 * @member {Number} base_row_total
 */
SalesDataOrderItemInterface.prototype['base_row_total'] = undefined;

/**
 * Base row total including tax.
 * @member {Number} base_row_total_incl_tax
 */
SalesDataOrderItemInterface.prototype['base_row_total_incl_tax'] = undefined;

/**
 * Base tax amount.
 * @member {Number} base_tax_amount
 */
SalesDataOrderItemInterface.prototype['base_tax_amount'] = undefined;

/**
 * Base tax before discount.
 * @member {Number} base_tax_before_discount
 */
SalesDataOrderItemInterface.prototype['base_tax_before_discount'] = undefined;

/**
 * Base tax invoiced.
 * @member {Number} base_tax_invoiced
 */
SalesDataOrderItemInterface.prototype['base_tax_invoiced'] = undefined;

/**
 * Base tax refunded.
 * @member {Number} base_tax_refunded
 */
SalesDataOrderItemInterface.prototype['base_tax_refunded'] = undefined;

/**
 * Base WEEE tax applied amount.
 * @member {Number} base_weee_tax_applied_amount
 */
SalesDataOrderItemInterface.prototype['base_weee_tax_applied_amount'] = undefined;

/**
 * Base WEEE tax applied row amount.
 * @member {Number} base_weee_tax_applied_row_amnt
 */
SalesDataOrderItemInterface.prototype['base_weee_tax_applied_row_amnt'] = undefined;

/**
 * Base WEEE tax disposition.
 * @member {Number} base_weee_tax_disposition
 */
SalesDataOrderItemInterface.prototype['base_weee_tax_disposition'] = undefined;

/**
 * Base WEEE tax row disposition.
 * @member {Number} base_weee_tax_row_disposition
 */
SalesDataOrderItemInterface.prototype['base_weee_tax_row_disposition'] = undefined;

/**
 * Created-at timestamp.
 * @member {String} created_at
 */
SalesDataOrderItemInterface.prototype['created_at'] = undefined;

/**
 * Description.
 * @member {String} description
 */
SalesDataOrderItemInterface.prototype['description'] = undefined;

/**
 * Discount amount.
 * @member {Number} discount_amount
 */
SalesDataOrderItemInterface.prototype['discount_amount'] = undefined;

/**
 * Discount invoiced.
 * @member {Number} discount_invoiced
 */
SalesDataOrderItemInterface.prototype['discount_invoiced'] = undefined;

/**
 * Discount percent.
 * @member {Number} discount_percent
 */
SalesDataOrderItemInterface.prototype['discount_percent'] = undefined;

/**
 * Discount refunded.
 * @member {Number} discount_refunded
 */
SalesDataOrderItemInterface.prototype['discount_refunded'] = undefined;

/**
 * Discount tax compensation amount.
 * @member {Number} discount_tax_compensation_amount
 */
SalesDataOrderItemInterface.prototype['discount_tax_compensation_amount'] = undefined;

/**
 * Discount tax compensation canceled.
 * @member {Number} discount_tax_compensation_canceled
 */
SalesDataOrderItemInterface.prototype['discount_tax_compensation_canceled'] = undefined;

/**
 * Discount tax compensation invoiced.
 * @member {Number} discount_tax_compensation_invoiced
 */
SalesDataOrderItemInterface.prototype['discount_tax_compensation_invoiced'] = undefined;

/**
 * Discount tax compensation refunded.
 * @member {Number} discount_tax_compensation_refunded
 */
SalesDataOrderItemInterface.prototype['discount_tax_compensation_refunded'] = undefined;

/**
 * Event ID.
 * @member {Number} event_id
 */
SalesDataOrderItemInterface.prototype['event_id'] = undefined;

/**
 * External order item ID.
 * @member {String} ext_order_item_id
 */
SalesDataOrderItemInterface.prototype['ext_order_item_id'] = undefined;

/**
 * @member {module:model/SalesDataOrderItemExtensionInterface} extension_attributes
 */
SalesDataOrderItemInterface.prototype['extension_attributes'] = undefined;

/**
 * Free-shipping flag value.
 * @member {Number} free_shipping
 */
SalesDataOrderItemInterface.prototype['free_shipping'] = undefined;

/**
 * GW base price.
 * @member {Number} gw_base_price
 */
SalesDataOrderItemInterface.prototype['gw_base_price'] = undefined;

/**
 * GW base price invoiced.
 * @member {Number} gw_base_price_invoiced
 */
SalesDataOrderItemInterface.prototype['gw_base_price_invoiced'] = undefined;

/**
 * GW base price refunded.
 * @member {Number} gw_base_price_refunded
 */
SalesDataOrderItemInterface.prototype['gw_base_price_refunded'] = undefined;

/**
 * GW base tax amount.
 * @member {Number} gw_base_tax_amount
 */
SalesDataOrderItemInterface.prototype['gw_base_tax_amount'] = undefined;

/**
 * GW base tax amount invoiced.
 * @member {Number} gw_base_tax_amount_invoiced
 */
SalesDataOrderItemInterface.prototype['gw_base_tax_amount_invoiced'] = undefined;

/**
 * GW base tax amount refunded.
 * @member {Number} gw_base_tax_amount_refunded
 */
SalesDataOrderItemInterface.prototype['gw_base_tax_amount_refunded'] = undefined;

/**
 * GW ID.
 * @member {Number} gw_id
 */
SalesDataOrderItemInterface.prototype['gw_id'] = undefined;

/**
 * GW price.
 * @member {Number} gw_price
 */
SalesDataOrderItemInterface.prototype['gw_price'] = undefined;

/**
 * GW price invoiced.
 * @member {Number} gw_price_invoiced
 */
SalesDataOrderItemInterface.prototype['gw_price_invoiced'] = undefined;

/**
 * GW price refunded.
 * @member {Number} gw_price_refunded
 */
SalesDataOrderItemInterface.prototype['gw_price_refunded'] = undefined;

/**
 * GW tax amount.
 * @member {Number} gw_tax_amount
 */
SalesDataOrderItemInterface.prototype['gw_tax_amount'] = undefined;

/**
 * GW tax amount invoiced.
 * @member {Number} gw_tax_amount_invoiced
 */
SalesDataOrderItemInterface.prototype['gw_tax_amount_invoiced'] = undefined;

/**
 * GW tax amount refunded.
 * @member {Number} gw_tax_amount_refunded
 */
SalesDataOrderItemInterface.prototype['gw_tax_amount_refunded'] = undefined;

/**
 * Is-quantity-decimal flag value.
 * @member {Number} is_qty_decimal
 */
SalesDataOrderItemInterface.prototype['is_qty_decimal'] = undefined;

/**
 * Is-virtual flag value.
 * @member {Number} is_virtual
 */
SalesDataOrderItemInterface.prototype['is_virtual'] = undefined;

/**
 * Item ID.
 * @member {Number} item_id
 */
SalesDataOrderItemInterface.prototype['item_id'] = undefined;

/**
 * Locked DO invoice flag value.
 * @member {Number} locked_do_invoice
 */
SalesDataOrderItemInterface.prototype['locked_do_invoice'] = undefined;

/**
 * Locked DO ship flag value.
 * @member {Number} locked_do_ship
 */
SalesDataOrderItemInterface.prototype['locked_do_ship'] = undefined;

/**
 * Name.
 * @member {String} name
 */
SalesDataOrderItemInterface.prototype['name'] = undefined;

/**
 * No-discount flag value.
 * @member {Number} no_discount
 */
SalesDataOrderItemInterface.prototype['no_discount'] = undefined;

/**
 * Order ID.
 * @member {Number} order_id
 */
SalesDataOrderItemInterface.prototype['order_id'] = undefined;

/**
 * Original price.
 * @member {Number} original_price
 */
SalesDataOrderItemInterface.prototype['original_price'] = undefined;

/**
 * @member {module:model/SalesDataOrderItemInterface} parent_item
 */
SalesDataOrderItemInterface.prototype['parent_item'] = undefined;

/**
 * Parent item ID.
 * @member {Number} parent_item_id
 */
SalesDataOrderItemInterface.prototype['parent_item_id'] = undefined;

/**
 * Price.
 * @member {Number} price
 */
SalesDataOrderItemInterface.prototype['price'] = undefined;

/**
 * Price including tax.
 * @member {Number} price_incl_tax
 */
SalesDataOrderItemInterface.prototype['price_incl_tax'] = undefined;

/**
 * Product ID.
 * @member {Number} product_id
 */
SalesDataOrderItemInterface.prototype['product_id'] = undefined;

/**
 * @member {module:model/CatalogDataProductOptionInterface} product_option
 */
SalesDataOrderItemInterface.prototype['product_option'] = undefined;

/**
 * Product type.
 * @member {String} product_type
 */
SalesDataOrderItemInterface.prototype['product_type'] = undefined;

/**
 * Quantity backordered.
 * @member {Number} qty_backordered
 */
SalesDataOrderItemInterface.prototype['qty_backordered'] = undefined;

/**
 * Quantity canceled.
 * @member {Number} qty_canceled
 */
SalesDataOrderItemInterface.prototype['qty_canceled'] = undefined;

/**
 * Quantity invoiced.
 * @member {Number} qty_invoiced
 */
SalesDataOrderItemInterface.prototype['qty_invoiced'] = undefined;

/**
 * Quantity ordered.
 * @member {Number} qty_ordered
 */
SalesDataOrderItemInterface.prototype['qty_ordered'] = undefined;

/**
 * Quantity refunded.
 * @member {Number} qty_refunded
 */
SalesDataOrderItemInterface.prototype['qty_refunded'] = undefined;

/**
 * Quantity returned.
 * @member {Number} qty_returned
 */
SalesDataOrderItemInterface.prototype['qty_returned'] = undefined;

/**
 * Quantity shipped.
 * @member {Number} qty_shipped
 */
SalesDataOrderItemInterface.prototype['qty_shipped'] = undefined;

/**
 * Quote item ID.
 * @member {Number} quote_item_id
 */
SalesDataOrderItemInterface.prototype['quote_item_id'] = undefined;

/**
 * Row invoiced.
 * @member {Number} row_invoiced
 */
SalesDataOrderItemInterface.prototype['row_invoiced'] = undefined;

/**
 * Row total.
 * @member {Number} row_total
 */
SalesDataOrderItemInterface.prototype['row_total'] = undefined;

/**
 * Row total including tax.
 * @member {Number} row_total_incl_tax
 */
SalesDataOrderItemInterface.prototype['row_total_incl_tax'] = undefined;

/**
 * Row weight.
 * @member {Number} row_weight
 */
SalesDataOrderItemInterface.prototype['row_weight'] = undefined;

/**
 * SKU.
 * @member {String} sku
 */
SalesDataOrderItemInterface.prototype['sku'] = undefined;

/**
 * Store ID.
 * @member {Number} store_id
 */
SalesDataOrderItemInterface.prototype['store_id'] = undefined;

/**
 * Tax amount.
 * @member {Number} tax_amount
 */
SalesDataOrderItemInterface.prototype['tax_amount'] = undefined;

/**
 * Tax before discount.
 * @member {Number} tax_before_discount
 */
SalesDataOrderItemInterface.prototype['tax_before_discount'] = undefined;

/**
 * Tax canceled.
 * @member {Number} tax_canceled
 */
SalesDataOrderItemInterface.prototype['tax_canceled'] = undefined;

/**
 * Tax invoiced.
 * @member {Number} tax_invoiced
 */
SalesDataOrderItemInterface.prototype['tax_invoiced'] = undefined;

/**
 * Tax percent.
 * @member {Number} tax_percent
 */
SalesDataOrderItemInterface.prototype['tax_percent'] = undefined;

/**
 * Tax refunded.
 * @member {Number} tax_refunded
 */
SalesDataOrderItemInterface.prototype['tax_refunded'] = undefined;

/**
 * Updated-at timestamp.
 * @member {String} updated_at
 */
SalesDataOrderItemInterface.prototype['updated_at'] = undefined;

/**
 * WEEE tax applied.
 * @member {String} weee_tax_applied
 */
SalesDataOrderItemInterface.prototype['weee_tax_applied'] = undefined;

/**
 * WEEE tax applied amount.
 * @member {Number} weee_tax_applied_amount
 */
SalesDataOrderItemInterface.prototype['weee_tax_applied_amount'] = undefined;

/**
 * WEEE tax applied row amount.
 * @member {Number} weee_tax_applied_row_amount
 */
SalesDataOrderItemInterface.prototype['weee_tax_applied_row_amount'] = undefined;

/**
 * WEEE tax disposition.
 * @member {Number} weee_tax_disposition
 */
SalesDataOrderItemInterface.prototype['weee_tax_disposition'] = undefined;

/**
 * WEEE tax row disposition.
 * @member {Number} weee_tax_row_disposition
 */
SalesDataOrderItemInterface.prototype['weee_tax_row_disposition'] = undefined;

/**
 * Weight.
 * @member {Number} weight
 */
SalesDataOrderItemInterface.prototype['weight'] = undefined;






export default SalesDataOrderItemInterface;

