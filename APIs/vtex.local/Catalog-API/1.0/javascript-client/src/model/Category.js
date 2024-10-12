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
 * The Category model module.
 * @module model/Category
 * @version 1.0
 */
class Category {
    /**
     * Constructs a new <code>Category</code>.
     * @alias module:model/Category
     * @param activeStoreFrontLink {Boolean} Defines if the Category has an active link on the website (`true`) or not (`false`).
     * @param adWordsRemarketingCode {String} This is a legacy field. Do not take this information into consideration.
     * @param description {String} Describes details about the category.
     * @param fatherCategoryId {Number} ID of the father category, apply in case of category and subcategory.
     * @param globalCategoryId {Number} Google Global Category ID.
     * @param hasChildren {Boolean} Defines if the category has child categories (`true`) or not (`false`).
     * @param id {Number} Category ID.
     * @param isActive {Boolean} Shows if the category is active (`true`) or not (`false`).
     * @param keywords {String} Substitutes words for the category.
     * @param linkId {String} Text Link.
     * @param lomadeeCampaignCode {String} This is a legacy field. Do not take this information into consideration.
     * @param name {String} Category name.
     * @param score {Number} Score for search ordination.
     * @param showBrandFilter {Boolean} Defines if the category has brand filter (`true`) or not (`false`).
     * @param showInStoreFront {Boolean} Defines if the category is shown on side and upper menu (`true`) or not (`false`).
     * @param stockKeepingUnitSelectionMode {String} Defines how the SKU will be exhibited.
     * @param title {String} Category page title.
     */
    constructor(activeStoreFrontLink, adWordsRemarketingCode, description, fatherCategoryId, globalCategoryId, hasChildren, id, isActive, keywords, linkId, lomadeeCampaignCode, name, score, showBrandFilter, showInStoreFront, stockKeepingUnitSelectionMode, title) { 
        
        Category.initialize(this, activeStoreFrontLink, adWordsRemarketingCode, description, fatherCategoryId, globalCategoryId, hasChildren, id, isActive, keywords, linkId, lomadeeCampaignCode, name, score, showBrandFilter, showInStoreFront, stockKeepingUnitSelectionMode, title);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, activeStoreFrontLink, adWordsRemarketingCode, description, fatherCategoryId, globalCategoryId, hasChildren, id, isActive, keywords, linkId, lomadeeCampaignCode, name, score, showBrandFilter, showInStoreFront, stockKeepingUnitSelectionMode, title) { 
        obj['ActiveStoreFrontLink'] = activeStoreFrontLink;
        obj['AdWordsRemarketingCode'] = adWordsRemarketingCode;
        obj['Description'] = description;
        obj['FatherCategoryId'] = fatherCategoryId;
        obj['GlobalCategoryId'] = globalCategoryId;
        obj['HasChildren'] = hasChildren;
        obj['Id'] = id;
        obj['IsActive'] = isActive;
        obj['Keywords'] = keywords;
        obj['LinkId'] = linkId;
        obj['LomadeeCampaignCode'] = lomadeeCampaignCode;
        obj['Name'] = name;
        obj['Score'] = score;
        obj['ShowBrandFilter'] = showBrandFilter;
        obj['ShowInStoreFront'] = showInStoreFront;
        obj['StockKeepingUnitSelectionMode'] = stockKeepingUnitSelectionMode;
        obj['Title'] = title;
    }

    /**
     * Constructs a <code>Category</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Category} obj Optional instance to populate.
     * @return {module:model/Category} The populated <code>Category</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Category();

            if (data.hasOwnProperty('ActiveStoreFrontLink')) {
                obj['ActiveStoreFrontLink'] = ApiClient.convertToType(data['ActiveStoreFrontLink'], 'Boolean');
            }
            if (data.hasOwnProperty('AdWordsRemarketingCode')) {
                obj['AdWordsRemarketingCode'] = ApiClient.convertToType(data['AdWordsRemarketingCode'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('FatherCategoryId')) {
                obj['FatherCategoryId'] = ApiClient.convertToType(data['FatherCategoryId'], 'Number');
            }
            if (data.hasOwnProperty('GlobalCategoryId')) {
                obj['GlobalCategoryId'] = ApiClient.convertToType(data['GlobalCategoryId'], 'Number');
            }
            if (data.hasOwnProperty('HasChildren')) {
                obj['HasChildren'] = ApiClient.convertToType(data['HasChildren'], 'Boolean');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('Keywords')) {
                obj['Keywords'] = ApiClient.convertToType(data['Keywords'], 'String');
            }
            if (data.hasOwnProperty('LinkId')) {
                obj['LinkId'] = ApiClient.convertToType(data['LinkId'], 'String');
            }
            if (data.hasOwnProperty('LomadeeCampaignCode')) {
                obj['LomadeeCampaignCode'] = ApiClient.convertToType(data['LomadeeCampaignCode'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Score')) {
                obj['Score'] = ApiClient.convertToType(data['Score'], 'Number');
            }
            if (data.hasOwnProperty('ShowBrandFilter')) {
                obj['ShowBrandFilter'] = ApiClient.convertToType(data['ShowBrandFilter'], 'Boolean');
            }
            if (data.hasOwnProperty('ShowInStoreFront')) {
                obj['ShowInStoreFront'] = ApiClient.convertToType(data['ShowInStoreFront'], 'Boolean');
            }
            if (data.hasOwnProperty('StockKeepingUnitSelectionMode')) {
                obj['StockKeepingUnitSelectionMode'] = ApiClient.convertToType(data['StockKeepingUnitSelectionMode'], 'String');
            }
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Category</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Category</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Category.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['AdWordsRemarketingCode'] && !(typeof data['AdWordsRemarketingCode'] === 'string' || data['AdWordsRemarketingCode'] instanceof String)) {
            throw new Error("Expected the field `AdWordsRemarketingCode` to be a primitive type in the JSON string but got " + data['AdWordsRemarketingCode']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['Keywords'] && !(typeof data['Keywords'] === 'string' || data['Keywords'] instanceof String)) {
            throw new Error("Expected the field `Keywords` to be a primitive type in the JSON string but got " + data['Keywords']);
        }
        // ensure the json data is a string
        if (data['LinkId'] && !(typeof data['LinkId'] === 'string' || data['LinkId'] instanceof String)) {
            throw new Error("Expected the field `LinkId` to be a primitive type in the JSON string but got " + data['LinkId']);
        }
        // ensure the json data is a string
        if (data['LomadeeCampaignCode'] && !(typeof data['LomadeeCampaignCode'] === 'string' || data['LomadeeCampaignCode'] instanceof String)) {
            throw new Error("Expected the field `LomadeeCampaignCode` to be a primitive type in the JSON string but got " + data['LomadeeCampaignCode']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['StockKeepingUnitSelectionMode'] && !(typeof data['StockKeepingUnitSelectionMode'] === 'string' || data['StockKeepingUnitSelectionMode'] instanceof String)) {
            throw new Error("Expected the field `StockKeepingUnitSelectionMode` to be a primitive type in the JSON string but got " + data['StockKeepingUnitSelectionMode']);
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }

        return true;
    }


}

Category.RequiredProperties = ["ActiveStoreFrontLink", "AdWordsRemarketingCode", "Description", "FatherCategoryId", "GlobalCategoryId", "HasChildren", "Id", "IsActive", "Keywords", "LinkId", "LomadeeCampaignCode", "Name", "Score", "ShowBrandFilter", "ShowInStoreFront", "StockKeepingUnitSelectionMode", "Title"];

/**
 * Defines if the Category has an active link on the website (`true`) or not (`false`).
 * @member {Boolean} ActiveStoreFrontLink
 */
Category.prototype['ActiveStoreFrontLink'] = undefined;

/**
 * This is a legacy field. Do not take this information into consideration.
 * @member {String} AdWordsRemarketingCode
 */
Category.prototype['AdWordsRemarketingCode'] = undefined;

/**
 * Describes details about the category.
 * @member {String} Description
 */
Category.prototype['Description'] = undefined;

/**
 * ID of the father category, apply in case of category and subcategory.
 * @member {Number} FatherCategoryId
 */
Category.prototype['FatherCategoryId'] = undefined;

/**
 * Google Global Category ID.
 * @member {Number} GlobalCategoryId
 */
Category.prototype['GlobalCategoryId'] = undefined;

/**
 * Defines if the category has child categories (`true`) or not (`false`).
 * @member {Boolean} HasChildren
 */
Category.prototype['HasChildren'] = undefined;

/**
 * Category ID.
 * @member {Number} Id
 */
Category.prototype['Id'] = undefined;

/**
 * Shows if the category is active (`true`) or not (`false`).
 * @member {Boolean} IsActive
 */
Category.prototype['IsActive'] = undefined;

/**
 * Substitutes words for the category.
 * @member {String} Keywords
 */
Category.prototype['Keywords'] = undefined;

/**
 * Text Link.
 * @member {String} LinkId
 */
Category.prototype['LinkId'] = undefined;

/**
 * This is a legacy field. Do not take this information into consideration.
 * @member {String} LomadeeCampaignCode
 */
Category.prototype['LomadeeCampaignCode'] = undefined;

/**
 * Category name.
 * @member {String} Name
 */
Category.prototype['Name'] = undefined;

/**
 * Score for search ordination.
 * @member {Number} Score
 */
Category.prototype['Score'] = undefined;

/**
 * Defines if the category has brand filter (`true`) or not (`false`).
 * @member {Boolean} ShowBrandFilter
 */
Category.prototype['ShowBrandFilter'] = undefined;

/**
 * Defines if the category is shown on side and upper menu (`true`) or not (`false`).
 * @member {Boolean} ShowInStoreFront
 */
Category.prototype['ShowInStoreFront'] = undefined;

/**
 * Defines how the SKU will be exhibited.
 * @member {String} StockKeepingUnitSelectionMode
 */
Category.prototype['StockKeepingUnitSelectionMode'] = undefined;

/**
 * Category page title.
 * @member {String} Title
 */
Category.prototype['Title'] = undefined;






export default Category;

