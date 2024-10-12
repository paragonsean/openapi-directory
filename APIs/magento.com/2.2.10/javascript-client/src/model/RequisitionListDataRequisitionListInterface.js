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
import RequisitionListDataRequisitionListItemInterface from './RequisitionListDataRequisitionListItemInterface';

/**
 * The RequisitionListDataRequisitionListInterface model module.
 * @module model/RequisitionListDataRequisitionListInterface
 * @version 2.2.10
 */
class RequisitionListDataRequisitionListInterface {
    /**
     * Constructs a new <code>RequisitionListDataRequisitionListInterface</code>.
     * Interface RequisitionListInterface
     * @alias module:model/RequisitionListDataRequisitionListInterface
     * @param customerId {Number} Customer ID
     * @param description {String} Requisition List Description
     * @param id {Number} Requisition List ID
     * @param items {Array.<module:model/RequisitionListDataRequisitionListItemInterface>} Requisition List Items
     * @param name {String} Requisition List Name
     * @param updatedAt {String} Requisition List Update Time
     */
    constructor(customerId, description, id, items, name, updatedAt) { 
        
        RequisitionListDataRequisitionListInterface.initialize(this, customerId, description, id, items, name, updatedAt);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, customerId, description, id, items, name, updatedAt) { 
        obj['customer_id'] = customerId;
        obj['description'] = description;
        obj['id'] = id;
        obj['items'] = items;
        obj['name'] = name;
        obj['updated_at'] = updatedAt;
    }

    /**
     * Constructs a <code>RequisitionListDataRequisitionListInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RequisitionListDataRequisitionListInterface} obj Optional instance to populate.
     * @return {module:model/RequisitionListDataRequisitionListInterface} The populated <code>RequisitionListDataRequisitionListInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RequisitionListDataRequisitionListInterface();

            if (data.hasOwnProperty('customer_id')) {
                obj['customer_id'] = ApiClient.convertToType(data['customer_id'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [RequisitionListDataRequisitionListItemInterface]);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RequisitionListDataRequisitionListInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RequisitionListDataRequisitionListInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RequisitionListDataRequisitionListInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                RequisitionListDataRequisitionListItemInterface.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }

        return true;
    }


}

RequisitionListDataRequisitionListInterface.RequiredProperties = ["customer_id", "description", "id", "items", "name", "updated_at"];

/**
 * Customer ID
 * @member {Number} customer_id
 */
RequisitionListDataRequisitionListInterface.prototype['customer_id'] = undefined;

/**
 * Requisition List Description
 * @member {String} description
 */
RequisitionListDataRequisitionListInterface.prototype['description'] = undefined;

/**
 * ExtensionInterface class for @see \\Magento\\RequisitionList\\Api\\Data\\RequisitionListInterface
 * @member {Object} extension_attributes
 */
RequisitionListDataRequisitionListInterface.prototype['extension_attributes'] = undefined;

/**
 * Requisition List ID
 * @member {Number} id
 */
RequisitionListDataRequisitionListInterface.prototype['id'] = undefined;

/**
 * Requisition List Items
 * @member {Array.<module:model/RequisitionListDataRequisitionListItemInterface>} items
 */
RequisitionListDataRequisitionListInterface.prototype['items'] = undefined;

/**
 * Requisition List Name
 * @member {String} name
 */
RequisitionListDataRequisitionListInterface.prototype['name'] = undefined;

/**
 * Requisition List Update Time
 * @member {String} updated_at
 */
RequisitionListDataRequisitionListInterface.prototype['updated_at'] = undefined;






export default RequisitionListDataRequisitionListInterface;

