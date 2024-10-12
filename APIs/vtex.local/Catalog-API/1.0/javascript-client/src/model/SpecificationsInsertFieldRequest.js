/**
 * Catalog API
 *   > Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | `{{accountName}}`         | Store account name                                                                      |  | `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |  | `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |
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
 * The SpecificationsInsertFieldRequest model module.
 * @module model/SpecificationsInsertFieldRequest
 * @version 1.0
 */
class SpecificationsInsertFieldRequest {
    /**
     * Constructs a new <code>SpecificationsInsertFieldRequest</code>.
     * @alias module:model/SpecificationsInsertFieldRequest
     * @param categoryId {Number} Category ID.
     * @param defaultValue {String} Specification Field default Value.
     * @param description {String} Specification Field Description.
     * @param fieldGroupId {Number} Specification Field Group ID.
     * @param fieldGroupName {String} Specification Field Group Name.
     * @param fieldId {Number} Specification Field ID.
     * @param fieldTypeId {Number} Specification Field Type ID.
     * @param fieldValueId {Number} Specification Field Value ID.
     * @param isActive {Boolean} Defines if the Specification Field is active. The default value is `true`.
     * @param isFilter {Boolean} Store Framework - Deprecated.  Legacy CMS Portal - To allow the specification to be used as a facet (filter) on the search navigation bar.  
     * @param isOnProductDetails {Boolean} Store Framework - Deprecated.  Legacy CMS Portal -If specification is visible on the product page.  
     * @param isRequired {Boolean} Makes the Specification Field mandatory (`true`) or optional (`false`).
     * @param isSideMenuLinkActive {Boolean} Store Framework - Deprecated.  Legacy CMS Portal - To make the specification field clickable in the search navigation bar.  
     * @param isStockKeepingUnit {Boolean} If `true`, it will be added as a SKU specification. If `false`, it will be added as a product specification field.
     * @param isTopMenuLinkActive {Boolean} Store Framework - Deprecated.  Legacy CMS Portal - To make the specification visible in the store's upper menu.  
     * @param isWizard {Boolean} Deprecated field.
     * @param name {String} Specification Field ID.
     * @param position {Number} Specification Field Position.
     */
    constructor(categoryId, defaultValue, description, fieldGroupId, fieldGroupName, fieldId, fieldTypeId, fieldValueId, isActive, isFilter, isOnProductDetails, isRequired, isSideMenuLinkActive, isStockKeepingUnit, isTopMenuLinkActive, isWizard, name, position) { 
        
        SpecificationsInsertFieldRequest.initialize(this, categoryId, defaultValue, description, fieldGroupId, fieldGroupName, fieldId, fieldTypeId, fieldValueId, isActive, isFilter, isOnProductDetails, isRequired, isSideMenuLinkActive, isStockKeepingUnit, isTopMenuLinkActive, isWizard, name, position);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, categoryId, defaultValue, description, fieldGroupId, fieldGroupName, fieldId, fieldTypeId, fieldValueId, isActive, isFilter, isOnProductDetails, isRequired, isSideMenuLinkActive, isStockKeepingUnit, isTopMenuLinkActive, isWizard, name, position) { 
        obj['CategoryId'] = categoryId;
        obj['DefaultValue'] = defaultValue;
        obj['Description'] = description;
        obj['FieldGroupId'] = fieldGroupId;
        obj['FieldGroupName'] = fieldGroupName;
        obj['FieldId'] = fieldId;
        obj['FieldTypeId'] = fieldTypeId;
        obj['FieldValueId'] = fieldValueId;
        obj['IsActive'] = isActive;
        obj['IsFilter'] = isFilter;
        obj['IsOnProductDetails'] = isOnProductDetails;
        obj['IsRequired'] = isRequired;
        obj['IsSideMenuLinkActive'] = isSideMenuLinkActive;
        obj['IsStockKeepingUnit'] = isStockKeepingUnit;
        obj['IsTopMenuLinkActive'] = isTopMenuLinkActive;
        obj['IsWizard'] = isWizard;
        obj['Name'] = name;
        obj['Position'] = position;
    }

    /**
     * Constructs a <code>SpecificationsInsertFieldRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SpecificationsInsertFieldRequest} obj Optional instance to populate.
     * @return {module:model/SpecificationsInsertFieldRequest} The populated <code>SpecificationsInsertFieldRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SpecificationsInsertFieldRequest();

            if (data.hasOwnProperty('CategoryId')) {
                obj['CategoryId'] = ApiClient.convertToType(data['CategoryId'], 'Number');
            }
            if (data.hasOwnProperty('DefaultValue')) {
                obj['DefaultValue'] = ApiClient.convertToType(data['DefaultValue'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('FieldGroupId')) {
                obj['FieldGroupId'] = ApiClient.convertToType(data['FieldGroupId'], 'Number');
            }
            if (data.hasOwnProperty('FieldGroupName')) {
                obj['FieldGroupName'] = ApiClient.convertToType(data['FieldGroupName'], 'String');
            }
            if (data.hasOwnProperty('FieldId')) {
                obj['FieldId'] = ApiClient.convertToType(data['FieldId'], 'Number');
            }
            if (data.hasOwnProperty('FieldTypeId')) {
                obj['FieldTypeId'] = ApiClient.convertToType(data['FieldTypeId'], 'Number');
            }
            if (data.hasOwnProperty('FieldValueId')) {
                obj['FieldValueId'] = ApiClient.convertToType(data['FieldValueId'], 'Number');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsFilter')) {
                obj['IsFilter'] = ApiClient.convertToType(data['IsFilter'], 'Boolean');
            }
            if (data.hasOwnProperty('IsOnProductDetails')) {
                obj['IsOnProductDetails'] = ApiClient.convertToType(data['IsOnProductDetails'], 'Boolean');
            }
            if (data.hasOwnProperty('IsRequired')) {
                obj['IsRequired'] = ApiClient.convertToType(data['IsRequired'], 'Boolean');
            }
            if (data.hasOwnProperty('IsSideMenuLinkActive')) {
                obj['IsSideMenuLinkActive'] = ApiClient.convertToType(data['IsSideMenuLinkActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsStockKeepingUnit')) {
                obj['IsStockKeepingUnit'] = ApiClient.convertToType(data['IsStockKeepingUnit'], 'Boolean');
            }
            if (data.hasOwnProperty('IsTopMenuLinkActive')) {
                obj['IsTopMenuLinkActive'] = ApiClient.convertToType(data['IsTopMenuLinkActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsWizard')) {
                obj['IsWizard'] = ApiClient.convertToType(data['IsWizard'], 'Boolean');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SpecificationsInsertFieldRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SpecificationsInsertFieldRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SpecificationsInsertFieldRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['DefaultValue'] && !(typeof data['DefaultValue'] === 'string' || data['DefaultValue'] instanceof String)) {
            throw new Error("Expected the field `DefaultValue` to be a primitive type in the JSON string but got " + data['DefaultValue']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['FieldGroupName'] && !(typeof data['FieldGroupName'] === 'string' || data['FieldGroupName'] instanceof String)) {
            throw new Error("Expected the field `FieldGroupName` to be a primitive type in the JSON string but got " + data['FieldGroupName']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }

        return true;
    }


}

SpecificationsInsertFieldRequest.RequiredProperties = ["CategoryId", "DefaultValue", "Description", "FieldGroupId", "FieldGroupName", "FieldId", "FieldTypeId", "FieldValueId", "IsActive", "IsFilter", "IsOnProductDetails", "IsRequired", "IsSideMenuLinkActive", "IsStockKeepingUnit", "IsTopMenuLinkActive", "IsWizard", "Name", "Position"];

/**
 * Category ID.
 * @member {Number} CategoryId
 */
SpecificationsInsertFieldRequest.prototype['CategoryId'] = undefined;

/**
 * Specification Field default Value.
 * @member {String} DefaultValue
 */
SpecificationsInsertFieldRequest.prototype['DefaultValue'] = undefined;

/**
 * Specification Field Description.
 * @member {String} Description
 */
SpecificationsInsertFieldRequest.prototype['Description'] = undefined;

/**
 * Specification Field Group ID.
 * @member {Number} FieldGroupId
 */
SpecificationsInsertFieldRequest.prototype['FieldGroupId'] = undefined;

/**
 * Specification Field Group Name.
 * @member {String} FieldGroupName
 */
SpecificationsInsertFieldRequest.prototype['FieldGroupName'] = undefined;

/**
 * Specification Field ID.
 * @member {Number} FieldId
 */
SpecificationsInsertFieldRequest.prototype['FieldId'] = undefined;

/**
 * Specification Field Type ID.
 * @member {Number} FieldTypeId
 */
SpecificationsInsertFieldRequest.prototype['FieldTypeId'] = undefined;

/**
 * Specification Field Value ID.
 * @member {Number} FieldValueId
 */
SpecificationsInsertFieldRequest.prototype['FieldValueId'] = undefined;

/**
 * Defines if the Specification Field is active. The default value is `true`.
 * @member {Boolean} IsActive
 */
SpecificationsInsertFieldRequest.prototype['IsActive'] = undefined;

/**
 * Store Framework - Deprecated.  Legacy CMS Portal - To allow the specification to be used as a facet (filter) on the search navigation bar.  
 * @member {Boolean} IsFilter
 */
SpecificationsInsertFieldRequest.prototype['IsFilter'] = undefined;

/**
 * Store Framework - Deprecated.  Legacy CMS Portal -If specification is visible on the product page.  
 * @member {Boolean} IsOnProductDetails
 */
SpecificationsInsertFieldRequest.prototype['IsOnProductDetails'] = undefined;

/**
 * Makes the Specification Field mandatory (`true`) or optional (`false`).
 * @member {Boolean} IsRequired
 */
SpecificationsInsertFieldRequest.prototype['IsRequired'] = undefined;

/**
 * Store Framework - Deprecated.  Legacy CMS Portal - To make the specification field clickable in the search navigation bar.  
 * @member {Boolean} IsSideMenuLinkActive
 */
SpecificationsInsertFieldRequest.prototype['IsSideMenuLinkActive'] = undefined;

/**
 * If `true`, it will be added as a SKU specification. If `false`, it will be added as a product specification field.
 * @member {Boolean} IsStockKeepingUnit
 */
SpecificationsInsertFieldRequest.prototype['IsStockKeepingUnit'] = undefined;

/**
 * Store Framework - Deprecated.  Legacy CMS Portal - To make the specification visible in the store's upper menu.  
 * @member {Boolean} IsTopMenuLinkActive
 */
SpecificationsInsertFieldRequest.prototype['IsTopMenuLinkActive'] = undefined;

/**
 * Deprecated field.
 * @member {Boolean} IsWizard
 */
SpecificationsInsertFieldRequest.prototype['IsWizard'] = undefined;

/**
 * Specification Field ID.
 * @member {String} Name
 */
SpecificationsInsertFieldRequest.prototype['Name'] = undefined;

/**
 * Specification Field Position.
 * @member {Number} Position
 */
SpecificationsInsertFieldRequest.prototype['Position'] = undefined;






export default SpecificationsInsertFieldRequest;

