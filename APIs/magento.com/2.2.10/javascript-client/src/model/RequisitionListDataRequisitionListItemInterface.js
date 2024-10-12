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

/**
 * The RequisitionListDataRequisitionListItemInterface model module.
 * @module model/RequisitionListDataRequisitionListItemInterface
 * @version 2.2.10
 */
class RequisitionListDataRequisitionListItemInterface {
    /**
     * Constructs a new <code>RequisitionListDataRequisitionListItemInterface</code>.
     * Interface RequisitionListItemInterface
     * @alias module:model/RequisitionListDataRequisitionListItemInterface
     * @param addedAt {String} Added_at value.
     * @param id {Number} Requisition List ID.
     * @param options {Array.<String>} Requisition list item options.
     * @param qty {Number} Product Qty.
     * @param requisitionListId {Number} Requisition List ID.
     * @param sku {String} Product SKU.
     * @param storeId {Number} Store ID.
     */
    constructor(addedAt, id, options, qty, requisitionListId, sku, storeId) { 
        
        RequisitionListDataRequisitionListItemInterface.initialize(this, addedAt, id, options, qty, requisitionListId, sku, storeId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, addedAt, id, options, qty, requisitionListId, sku, storeId) { 
        obj['added_at'] = addedAt;
        obj['id'] = id;
        obj['options'] = options;
        obj['qty'] = qty;
        obj['requisition_list_id'] = requisitionListId;
        obj['sku'] = sku;
        obj['store_id'] = storeId;
    }

    /**
     * Constructs a <code>RequisitionListDataRequisitionListItemInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RequisitionListDataRequisitionListItemInterface} obj Optional instance to populate.
     * @return {module:model/RequisitionListDataRequisitionListItemInterface} The populated <code>RequisitionListDataRequisitionListItemInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RequisitionListDataRequisitionListItemInterface();

            if (data.hasOwnProperty('added_at')) {
                obj['added_at'] = ApiClient.convertToType(data['added_at'], 'String');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('options')) {
                obj['options'] = ApiClient.convertToType(data['options'], ['String']);
            }
            if (data.hasOwnProperty('qty')) {
                obj['qty'] = ApiClient.convertToType(data['qty'], 'Number');
            }
            if (data.hasOwnProperty('requisition_list_id')) {
                obj['requisition_list_id'] = ApiClient.convertToType(data['requisition_list_id'], 'Number');
            }
            if (data.hasOwnProperty('sku')) {
                obj['sku'] = ApiClient.convertToType(data['sku'], 'String');
            }
            if (data.hasOwnProperty('store_id')) {
                obj['store_id'] = ApiClient.convertToType(data['store_id'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RequisitionListDataRequisitionListItemInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RequisitionListDataRequisitionListItemInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RequisitionListDataRequisitionListItemInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['added_at'] && !(typeof data['added_at'] === 'string' || data['added_at'] instanceof String)) {
            throw new Error("Expected the field `added_at` to be a primitive type in the JSON string but got " + data['added_at']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['options'])) {
            throw new Error("Expected the field `options` to be an array in the JSON data but got " + data['options']);
        }
        // ensure the json data is a string
        if (data['sku'] && !(typeof data['sku'] === 'string' || data['sku'] instanceof String)) {
            throw new Error("Expected the field `sku` to be a primitive type in the JSON string but got " + data['sku']);
        }

        return true;
    }


}

RequisitionListDataRequisitionListItemInterface.RequiredProperties = ["added_at", "id", "options", "qty", "requisition_list_id", "sku", "store_id"];

/**
 * Added_at value.
 * @member {String} added_at
 */
RequisitionListDataRequisitionListItemInterface.prototype['added_at'] = undefined;

/**
 * ExtensionInterface class for @see \\Magento\\RequisitionList\\Api\\Data\\RequisitionListItemInterface
 * @member {Object} extension_attributes
 */
RequisitionListDataRequisitionListItemInterface.prototype['extension_attributes'] = undefined;

/**
 * Requisition List ID.
 * @member {Number} id
 */
RequisitionListDataRequisitionListItemInterface.prototype['id'] = undefined;

/**
 * Requisition list item options.
 * @member {Array.<String>} options
 */
RequisitionListDataRequisitionListItemInterface.prototype['options'] = undefined;

/**
 * Product Qty.
 * @member {Number} qty
 */
RequisitionListDataRequisitionListItemInterface.prototype['qty'] = undefined;

/**
 * Requisition List ID.
 * @member {Number} requisition_list_id
 */
RequisitionListDataRequisitionListItemInterface.prototype['requisition_list_id'] = undefined;

/**
 * Product SKU.
 * @member {String} sku
 */
RequisitionListDataRequisitionListItemInterface.prototype['sku'] = undefined;

/**
 * Store ID.
 * @member {Number} store_id
 */
RequisitionListDataRequisitionListItemInterface.prototype['store_id'] = undefined;






export default RequisitionListDataRequisitionListItemInterface;

