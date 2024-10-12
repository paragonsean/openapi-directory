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
 * The BrandCreateUpdate model module.
 * @module model/BrandCreateUpdate
 * @version 1.0
 */
class BrandCreateUpdate {
    /**
     * Constructs a new <code>BrandCreateUpdate</code>.
     * Object containing Brand information.
     * @alias module:model/BrandCreateUpdate
     * @param id {Number} Brand's unique numerical identifier.
     * @param name {String} Brand name.
     */
    constructor(id, name) { 
        
        BrandCreateUpdate.initialize(this, id, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, name) { 
        obj['Id'] = id;
        obj['Name'] = name;
    }

    /**
     * Constructs a <code>BrandCreateUpdate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BrandCreateUpdate} obj Optional instance to populate.
     * @return {module:model/BrandCreateUpdate} The populated <code>BrandCreateUpdate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BrandCreateUpdate();

            if (data.hasOwnProperty('Active')) {
                obj['Active'] = ApiClient.convertToType(data['Active'], 'Boolean');
            }
            if (data.hasOwnProperty('AdWordsRemarketingCode')) {
                obj['AdWordsRemarketingCode'] = ApiClient.convertToType(data['AdWordsRemarketingCode'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
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
            if (data.hasOwnProperty('MenuHome')) {
                obj['MenuHome'] = ApiClient.convertToType(data['MenuHome'], 'Boolean');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Score')) {
                obj['Score'] = ApiClient.convertToType(data['Score'], 'Number');
            }
            if (data.hasOwnProperty('SiteTitle')) {
                obj['SiteTitle'] = ApiClient.convertToType(data['SiteTitle'], 'String');
            }
            if (data.hasOwnProperty('Text')) {
                obj['Text'] = ApiClient.convertToType(data['Text'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BrandCreateUpdate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BrandCreateUpdate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BrandCreateUpdate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['AdWordsRemarketingCode'] && !(typeof data['AdWordsRemarketingCode'] === 'string' || data['AdWordsRemarketingCode'] instanceof String)) {
            throw new Error("Expected the field `AdWordsRemarketingCode` to be a primitive type in the JSON string but got " + data['AdWordsRemarketingCode']);
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
        if (data['SiteTitle'] && !(typeof data['SiteTitle'] === 'string' || data['SiteTitle'] instanceof String)) {
            throw new Error("Expected the field `SiteTitle` to be a primitive type in the JSON string but got " + data['SiteTitle']);
        }
        // ensure the json data is a string
        if (data['Text'] && !(typeof data['Text'] === 'string' || data['Text'] instanceof String)) {
            throw new Error("Expected the field `Text` to be a primitive type in the JSON string but got " + data['Text']);
        }

        return true;
    }


}

BrandCreateUpdate.RequiredProperties = ["Id", "Name"];

/**
 * Defines if the brand is active (`true`) or not (`false`).
 * @member {Boolean} Active
 */
BrandCreateUpdate.prototype['Active'] = undefined;

/**
 * This is a legacy field. Do not take this information into consideration.
 * @member {String} AdWordsRemarketingCode
 */
BrandCreateUpdate.prototype['AdWordsRemarketingCode'] = undefined;

/**
 * Brand's unique numerical identifier.
 * @member {Number} Id
 */
BrandCreateUpdate.prototype['Id'] = undefined;

/**
 * Store Framework - Deprecated.  Legacy CMS Portal - Alternative search terms that will lead to the specific brand. The user can find the desired brand even when misspelling it. Used especially when words are of foreign origin and have a distinct spelling that is transcribed into a generic one, or when small spelling mistakes occur.  
 * @member {String} Keywords
 */
BrandCreateUpdate.prototype['Keywords'] = undefined;

/**
 * Brand page slug. Only lowercase letters and hyphens (`-`) are allowed.
 * @member {String} LinkId
 */
BrandCreateUpdate.prototype['LinkId'] = undefined;

/**
 * This is a legacy field. Do not take this information into consideration.
 * @member {String} LomadeeCampaignCode
 */
BrandCreateUpdate.prototype['LomadeeCampaignCode'] = undefined;

/**
 * Store Framework - Deprecated.  Legacy CMS Portal - Defines if the Brand appears in the Department Menu control (`<vtex.cmc:departmentNavigator/>`).  
 * @member {Boolean} MenuHome
 */
BrandCreateUpdate.prototype['MenuHome'] = undefined;

/**
 * Brand name.
 * @member {String} Name
 */
BrandCreateUpdate.prototype['Name'] = undefined;

/**
 * Store Framework - Deprecated  Legacy CMS Portal - Value used to set the priority on the search result page.  
 * @member {Number} Score
 */
BrandCreateUpdate.prototype['Score'] = undefined;

/**
 * Meta Title for the Brand page.
 * @member {String} SiteTitle
 */
BrandCreateUpdate.prototype['SiteTitle'] = undefined;

/**
 * Meta Description for the Brand page. A brief description of the brand, displayed by search engines. Since search engines can only display less than 150 characters, we recommend not exceeding this character limit when creating the description.
 * @member {String} Text
 */
BrandCreateUpdate.prototype['Text'] = undefined;






export default BrandCreateUpdate;

