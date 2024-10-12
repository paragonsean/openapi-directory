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
 * The ProductbyRefId200Response model module.
 * @module model/ProductbyRefId200Response
 * @version 1.0
 */
class ProductbyRefId200Response {
    /**
     * Constructs a new <code>ProductbyRefId200Response</code>.
     * @alias module:model/ProductbyRefId200Response
     */
    constructor() { 
        
        ProductbyRefId200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductbyRefId200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductbyRefId200Response} obj Optional instance to populate.
     * @return {module:model/ProductbyRefId200Response} The populated <code>ProductbyRefId200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductbyRefId200Response();

            if (data.hasOwnProperty('AdWordsRemarketingCode')) {
                obj['AdWordsRemarketingCode'] = ApiClient.convertToType(data['AdWordsRemarketingCode'], 'String');
            }
            if (data.hasOwnProperty('BrandId')) {
                obj['BrandId'] = ApiClient.convertToType(data['BrandId'], 'Number');
            }
            if (data.hasOwnProperty('CategoryId')) {
                obj['CategoryId'] = ApiClient.convertToType(data['CategoryId'], 'Number');
            }
            if (data.hasOwnProperty('DepartmentId')) {
                obj['DepartmentId'] = ApiClient.convertToType(data['DepartmentId'], 'Number');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('DescriptionShort')) {
                obj['DescriptionShort'] = ApiClient.convertToType(data['DescriptionShort'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsVisible')) {
                obj['IsVisible'] = ApiClient.convertToType(data['IsVisible'], 'Boolean');
            }
            if (data.hasOwnProperty('KeyWords')) {
                obj['KeyWords'] = ApiClient.convertToType(data['KeyWords'], 'String');
            }
            if (data.hasOwnProperty('LinkId')) {
                obj['LinkId'] = ApiClient.convertToType(data['LinkId'], 'String');
            }
            if (data.hasOwnProperty('ListStoreId')) {
                obj['ListStoreId'] = ApiClient.convertToType(data['ListStoreId'], ['Number']);
            }
            if (data.hasOwnProperty('LomadeeCampaignCode')) {
                obj['LomadeeCampaignCode'] = ApiClient.convertToType(data['LomadeeCampaignCode'], 'String');
            }
            if (data.hasOwnProperty('MetaTagDescription')) {
                obj['MetaTagDescription'] = ApiClient.convertToType(data['MetaTagDescription'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('RefId')) {
                obj['RefId'] = ApiClient.convertToType(data['RefId'], 'String');
            }
            if (data.hasOwnProperty('ReleaseDate')) {
                obj['ReleaseDate'] = ApiClient.convertToType(data['ReleaseDate'], 'String');
            }
            if (data.hasOwnProperty('ShowWithoutStock')) {
                obj['ShowWithoutStock'] = ApiClient.convertToType(data['ShowWithoutStock'], 'Boolean');
            }
            if (data.hasOwnProperty('SupplierId')) {
                obj['SupplierId'] = ApiClient.convertToType(data['SupplierId'], 'Number');
            }
            if (data.hasOwnProperty('TaxCode')) {
                obj['TaxCode'] = ApiClient.convertToType(data['TaxCode'], 'String');
            }
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductbyRefId200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductbyRefId200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AdWordsRemarketingCode'] && !(typeof data['AdWordsRemarketingCode'] === 'string' || data['AdWordsRemarketingCode'] instanceof String)) {
            throw new Error("Expected the field `AdWordsRemarketingCode` to be a primitive type in the JSON string but got " + data['AdWordsRemarketingCode']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['DescriptionShort'] && !(typeof data['DescriptionShort'] === 'string' || data['DescriptionShort'] instanceof String)) {
            throw new Error("Expected the field `DescriptionShort` to be a primitive type in the JSON string but got " + data['DescriptionShort']);
        }
        // ensure the json data is a string
        if (data['KeyWords'] && !(typeof data['KeyWords'] === 'string' || data['KeyWords'] instanceof String)) {
            throw new Error("Expected the field `KeyWords` to be a primitive type in the JSON string but got " + data['KeyWords']);
        }
        // ensure the json data is a string
        if (data['LinkId'] && !(typeof data['LinkId'] === 'string' || data['LinkId'] instanceof String)) {
            throw new Error("Expected the field `LinkId` to be a primitive type in the JSON string but got " + data['LinkId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ListStoreId'])) {
            throw new Error("Expected the field `ListStoreId` to be an array in the JSON data but got " + data['ListStoreId']);
        }
        // ensure the json data is a string
        if (data['LomadeeCampaignCode'] && !(typeof data['LomadeeCampaignCode'] === 'string' || data['LomadeeCampaignCode'] instanceof String)) {
            throw new Error("Expected the field `LomadeeCampaignCode` to be a primitive type in the JSON string but got " + data['LomadeeCampaignCode']);
        }
        // ensure the json data is a string
        if (data['MetaTagDescription'] && !(typeof data['MetaTagDescription'] === 'string' || data['MetaTagDescription'] instanceof String)) {
            throw new Error("Expected the field `MetaTagDescription` to be a primitive type in the JSON string but got " + data['MetaTagDescription']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['RefId'] && !(typeof data['RefId'] === 'string' || data['RefId'] instanceof String)) {
            throw new Error("Expected the field `RefId` to be a primitive type in the JSON string but got " + data['RefId']);
        }
        // ensure the json data is a string
        if (data['ReleaseDate'] && !(typeof data['ReleaseDate'] === 'string' || data['ReleaseDate'] instanceof String)) {
            throw new Error("Expected the field `ReleaseDate` to be a primitive type in the JSON string but got " + data['ReleaseDate']);
        }
        // ensure the json data is a string
        if (data['TaxCode'] && !(typeof data['TaxCode'] === 'string' || data['TaxCode'] instanceof String)) {
            throw new Error("Expected the field `TaxCode` to be a primitive type in the JSON string but got " + data['TaxCode']);
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }

        return true;
    }


}



/**
 * This is a legacy field. Do not take this information into consideration.
 * @member {String} AdWordsRemarketingCode
 */
ProductbyRefId200Response.prototype['AdWordsRemarketingCode'] = undefined;

/**
 * ID of the product Brand.
 * @member {Number} BrandId
 */
ProductbyRefId200Response.prototype['BrandId'] = undefined;

/**
 * ID of product Category.
 * @member {Number} CategoryId
 */
ProductbyRefId200Response.prototype['CategoryId'] = undefined;

/**
 * ID of product department.
 * @member {Number} DepartmentId
 */
ProductbyRefId200Response.prototype['DepartmentId'] = undefined;

/**
 * Product Description, HTML is allowed.
 * @member {String} Description
 */
ProductbyRefId200Response.prototype['Description'] = undefined;

/**
 * Product Short Description.
 * @member {String} DescriptionShort
 */
ProductbyRefId200Response.prototype['DescriptionShort'] = undefined;

/**
 * ID of the Product.
 * @member {Number} Id
 */
ProductbyRefId200Response.prototype['Id'] = undefined;

/**
 * If the product is Active.
 * @member {Boolean} IsActive
 */
ProductbyRefId200Response.prototype['IsActive'] = undefined;

/**
 * If the product are visible in search and list pages.
 * @member {Boolean} IsVisible
 */
ProductbyRefId200Response.prototype['IsVisible'] = undefined;

/**
 * Alternatives Keywords to improve the product findability.
 * @member {String} KeyWords
 */
ProductbyRefId200Response.prototype['KeyWords'] = undefined;

/**
 * Category URL.
 * @member {String} LinkId
 */
ProductbyRefId200Response.prototype['LinkId'] = undefined;

/**
 * Array with the ID of all the trade policies that are related to the product.
 * @member {Array.<Number>} ListStoreId
 */
ProductbyRefId200Response.prototype['ListStoreId'] = undefined;

/**
 * This is a legacy field. Do not take this information into consideration.
 * @member {String} LomadeeCampaignCode
 */
ProductbyRefId200Response.prototype['LomadeeCampaignCode'] = undefined;

/**
 * Meta Description for the Product page.
 * @member {String} MetaTagDescription
 */
ProductbyRefId200Response.prototype['MetaTagDescription'] = undefined;

/**
 * Name of the Product.
 * @member {String} Name
 */
ProductbyRefId200Response.prototype['Name'] = undefined;

/**
 * Product Reference ID.
 * @member {String} RefId
 */
ProductbyRefId200Response.prototype['RefId'] = undefined;

/**
 * Product Release Date, for list ordering and product cluster highlight.
 * @member {String} ReleaseDate
 */
ProductbyRefId200Response.prototype['ReleaseDate'] = undefined;

/**
 * If the product can be visible without stock.
 * @member {Boolean} ShowWithoutStock
 */
ProductbyRefId200Response.prototype['ShowWithoutStock'] = undefined;

/**
 * Product Supplier ID.
 * @member {Number} SupplierId
 */
ProductbyRefId200Response.prototype['SupplierId'] = undefined;

/**
 * SKU Tax Code.
 * @member {String} TaxCode
 */
ProductbyRefId200Response.prototype['TaxCode'] = undefined;

/**
 * Product's Title tag. Limited to 150 characters. It is presented in the browser tab and corresponds to the title of the product page. This field is important for SEO.
 * @member {String} Title
 */
ProductbyRefId200Response.prototype['Title'] = undefined;






export default ProductbyRefId200Response;

