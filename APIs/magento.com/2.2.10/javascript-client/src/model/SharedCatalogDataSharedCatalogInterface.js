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
 * The SharedCatalogDataSharedCatalogInterface model module.
 * @module model/SharedCatalogDataSharedCatalogInterface
 * @version 2.2.10
 */
class SharedCatalogDataSharedCatalogInterface {
    /**
     * Constructs a new <code>SharedCatalogDataSharedCatalogInterface</code>.
     * SharedCatalogInterface interface.
     * @alias module:model/SharedCatalogDataSharedCatalogInterface
     * @param createdAt {String} Created time for Shared Catalog.
     * @param createdBy {Number} Admin id for Shared Catalog.
     * @param customerGroupId {Number} Customer Group Id.
     * @param description {String} Shared Catalog description.
     * @param name {String} Shared Catalog name.
     * @param storeId {Number} Store id for Shared Catalog.
     * @param taxClassId {Number} Tax class id.
     * @param type {Number} Shared Catalog type.
     */
    constructor(createdAt, createdBy, customerGroupId, description, name, storeId, taxClassId, type) { 
        
        SharedCatalogDataSharedCatalogInterface.initialize(this, createdAt, createdBy, customerGroupId, description, name, storeId, taxClassId, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, createdAt, createdBy, customerGroupId, description, name, storeId, taxClassId, type) { 
        obj['created_at'] = createdAt;
        obj['created_by'] = createdBy;
        obj['customer_group_id'] = customerGroupId;
        obj['description'] = description;
        obj['name'] = name;
        obj['store_id'] = storeId;
        obj['tax_class_id'] = taxClassId;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>SharedCatalogDataSharedCatalogInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SharedCatalogDataSharedCatalogInterface} obj Optional instance to populate.
     * @return {module:model/SharedCatalogDataSharedCatalogInterface} The populated <code>SharedCatalogDataSharedCatalogInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SharedCatalogDataSharedCatalogInterface();

            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('created_by')) {
                obj['created_by'] = ApiClient.convertToType(data['created_by'], 'Number');
            }
            if (data.hasOwnProperty('customer_group_id')) {
                obj['customer_group_id'] = ApiClient.convertToType(data['customer_group_id'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('store_id')) {
                obj['store_id'] = ApiClient.convertToType(data['store_id'], 'Number');
            }
            if (data.hasOwnProperty('tax_class_id')) {
                obj['tax_class_id'] = ApiClient.convertToType(data['tax_class_id'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SharedCatalogDataSharedCatalogInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SharedCatalogDataSharedCatalogInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SharedCatalogDataSharedCatalogInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
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
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

SharedCatalogDataSharedCatalogInterface.RequiredProperties = ["created_at", "created_by", "customer_group_id", "description", "name", "store_id", "tax_class_id", "type"];

/**
 * Created time for Shared Catalog.
 * @member {String} created_at
 */
SharedCatalogDataSharedCatalogInterface.prototype['created_at'] = undefined;

/**
 * Admin id for Shared Catalog.
 * @member {Number} created_by
 */
SharedCatalogDataSharedCatalogInterface.prototype['created_by'] = undefined;

/**
 * Customer Group Id.
 * @member {Number} customer_group_id
 */
SharedCatalogDataSharedCatalogInterface.prototype['customer_group_id'] = undefined;

/**
 * Shared Catalog description.
 * @member {String} description
 */
SharedCatalogDataSharedCatalogInterface.prototype['description'] = undefined;

/**
 * ID.
 * @member {Number} id
 */
SharedCatalogDataSharedCatalogInterface.prototype['id'] = undefined;

/**
 * Shared Catalog name.
 * @member {String} name
 */
SharedCatalogDataSharedCatalogInterface.prototype['name'] = undefined;

/**
 * Store id for Shared Catalog.
 * @member {Number} store_id
 */
SharedCatalogDataSharedCatalogInterface.prototype['store_id'] = undefined;

/**
 * Tax class id.
 * @member {Number} tax_class_id
 */
SharedCatalogDataSharedCatalogInterface.prototype['tax_class_id'] = undefined;

/**
 * Shared Catalog type.
 * @member {Number} type
 */
SharedCatalogDataSharedCatalogInterface.prototype['type'] = undefined;






export default SharedCatalogDataSharedCatalogInterface;

