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
import ProductVariations200ResponseSkusInnerMeasures from './ProductVariations200ResponseSkusInnerMeasures';

/**
 * The ProductVariations200ResponseSkusInner model module.
 * @module model/ProductVariations200ResponseSkusInner
 * @version 1.0
 */
class ProductVariations200ResponseSkusInner {
    /**
     * Constructs a new <code>ProductVariations200ResponseSkusInner</code>.
     * Object containing information about a specific SKU.
     * @alias module:model/ProductVariations200ResponseSkusInner
     */
    constructor() { 
        
        ProductVariations200ResponseSkusInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductVariations200ResponseSkusInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductVariations200ResponseSkusInner} obj Optional instance to populate.
     * @return {module:model/ProductVariations200ResponseSkusInner} The populated <code>ProductVariations200ResponseSkusInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductVariations200ResponseSkusInner();

            if (data.hasOwnProperty('available')) {
                obj['available'] = ApiClient.convertToType(data['available'], 'Boolean');
            }
            if (data.hasOwnProperty('availablequantity')) {
                obj['availablequantity'] = ApiClient.convertToType(data['availablequantity'], 'Number');
            }
            if (data.hasOwnProperty('bestPrice')) {
                obj['bestPrice'] = ApiClient.convertToType(data['bestPrice'], 'Number');
            }
            if (data.hasOwnProperty('bestPriceFormated')) {
                obj['bestPriceFormated'] = ApiClient.convertToType(data['bestPriceFormated'], 'String');
            }
            if (data.hasOwnProperty('cacheVersionUsedToCallCheckout')) {
                obj['cacheVersionUsedToCallCheckout'] = ApiClient.convertToType(data['cacheVersionUsedToCallCheckout'], 'String');
            }
            if (data.hasOwnProperty('dimensions')) {
                obj['dimensions'] = ApiClient.convertToType(data['dimensions'], {'String': 'String'});
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ApiClient.convertToType(data['image'], 'String');
            }
            if (data.hasOwnProperty('installments')) {
                obj['installments'] = ApiClient.convertToType(data['installments'], 'Number');
            }
            if (data.hasOwnProperty('installmentsInsterestRate')) {
                obj['installmentsInsterestRate'] = ApiClient.convertToType(data['installmentsInsterestRate'], 'Number');
            }
            if (data.hasOwnProperty('installmentsValue')) {
                obj['installmentsValue'] = ApiClient.convertToType(data['installmentsValue'], 'Number');
            }
            if (data.hasOwnProperty('listPrice')) {
                obj['listPrice'] = ApiClient.convertToType(data['listPrice'], 'Number');
            }
            if (data.hasOwnProperty('listPriceFormated')) {
                obj['listPriceFormated'] = ApiClient.convertToType(data['listPriceFormated'], 'String');
            }
            if (data.hasOwnProperty('measures')) {
                obj['measures'] = ProductVariations200ResponseSkusInnerMeasures.constructFromObject(data['measures']);
            }
            if (data.hasOwnProperty('rewardValue')) {
                obj['rewardValue'] = ApiClient.convertToType(data['rewardValue'], 'Number');
            }
            if (data.hasOwnProperty('sellerId')) {
                obj['sellerId'] = ApiClient.convertToType(data['sellerId'], 'String');
            }
            if (data.hasOwnProperty('sku')) {
                obj['sku'] = ApiClient.convertToType(data['sku'], 'Number');
            }
            if (data.hasOwnProperty('skuname')) {
                obj['skuname'] = ApiClient.convertToType(data['skuname'], 'String');
            }
            if (data.hasOwnProperty('spotPrice')) {
                obj['spotPrice'] = ApiClient.convertToType(data['spotPrice'], 'Number');
            }
            if (data.hasOwnProperty('taxAsInt')) {
                obj['taxAsInt'] = ApiClient.convertToType(data['taxAsInt'], 'Number');
            }
            if (data.hasOwnProperty('taxFormated')) {
                obj['taxFormated'] = ApiClient.convertToType(data['taxFormated'], 'String');
            }
            if (data.hasOwnProperty('unitMultiplier')) {
                obj['unitMultiplier'] = ApiClient.convertToType(data['unitMultiplier'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductVariations200ResponseSkusInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductVariations200ResponseSkusInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['bestPriceFormated'] && !(typeof data['bestPriceFormated'] === 'string' || data['bestPriceFormated'] instanceof String)) {
            throw new Error("Expected the field `bestPriceFormated` to be a primitive type in the JSON string but got " + data['bestPriceFormated']);
        }
        // ensure the json data is a string
        if (data['cacheVersionUsedToCallCheckout'] && !(typeof data['cacheVersionUsedToCallCheckout'] === 'string' || data['cacheVersionUsedToCallCheckout'] instanceof String)) {
            throw new Error("Expected the field `cacheVersionUsedToCallCheckout` to be a primitive type in the JSON string but got " + data['cacheVersionUsedToCallCheckout']);
        }
        // ensure the json data is a string
        if (data['image'] && !(typeof data['image'] === 'string' || data['image'] instanceof String)) {
            throw new Error("Expected the field `image` to be a primitive type in the JSON string but got " + data['image']);
        }
        // ensure the json data is a string
        if (data['listPriceFormated'] && !(typeof data['listPriceFormated'] === 'string' || data['listPriceFormated'] instanceof String)) {
            throw new Error("Expected the field `listPriceFormated` to be a primitive type in the JSON string but got " + data['listPriceFormated']);
        }
        // validate the optional field `measures`
        if (data['measures']) { // data not null
          ProductVariations200ResponseSkusInnerMeasures.validateJSON(data['measures']);
        }
        // ensure the json data is a string
        if (data['sellerId'] && !(typeof data['sellerId'] === 'string' || data['sellerId'] instanceof String)) {
            throw new Error("Expected the field `sellerId` to be a primitive type in the JSON string but got " + data['sellerId']);
        }
        // ensure the json data is a string
        if (data['skuname'] && !(typeof data['skuname'] === 'string' || data['skuname'] instanceof String)) {
            throw new Error("Expected the field `skuname` to be a primitive type in the JSON string but got " + data['skuname']);
        }
        // ensure the json data is a string
        if (data['taxFormated'] && !(typeof data['taxFormated'] === 'string' || data['taxFormated'] instanceof String)) {
            throw new Error("Expected the field `taxFormated` to be a primitive type in the JSON string but got " + data['taxFormated']);
        }

        return true;
    }


}



/**
 * Defines if the SKU is available (`true`) or not (`false`).
 * @member {Boolean} available
 */
ProductVariations200ResponseSkusInner.prototype['available'] = undefined;

/**
 * Available quantity of the SKU in stock.
 * @member {Number} availablequantity
 */
ProductVariations200ResponseSkusInner.prototype['availablequantity'] = undefined;

/**
 * Best price.
 * @member {Number} bestPrice
 */
ProductVariations200ResponseSkusInner.prototype['bestPrice'] = undefined;

/**
 * Best price formatted according to the valid currency.
 * @member {String} bestPriceFormated
 */
ProductVariations200ResponseSkusInner.prototype['bestPriceFormated'] = undefined;

/**
 * Cache version used to call Checkout.
 * @member {String} cacheVersionUsedToCallCheckout
 */
ProductVariations200ResponseSkusInner.prototype['cacheVersionUsedToCallCheckout'] = undefined;

/**
 * Lists SKU specifications and their respective values.
 * @member {Object.<String, String>} dimensions
 */
ProductVariations200ResponseSkusInner.prototype['dimensions'] = undefined;

/**
 * SKU image URL.
 * @member {String} image
 */
ProductVariations200ResponseSkusInner.prototype['image'] = undefined;

/**
 * Number of installments.
 * @member {Number} installments
 */
ProductVariations200ResponseSkusInner.prototype['installments'] = undefined;

/**
 * Interest rate of installments.
 * @member {Number} installmentsInsterestRate
 */
ProductVariations200ResponseSkusInner.prototype['installmentsInsterestRate'] = undefined;

/**
 * Value of installments.
 * @member {Number} installmentsValue
 */
ProductVariations200ResponseSkusInner.prototype['installmentsValue'] = undefined;

/**
 * List price.
 * @member {Number} listPrice
 */
ProductVariations200ResponseSkusInner.prototype['listPrice'] = undefined;

/**
 * List price formatted according to the valid currency.
 * @member {String} listPriceFormated
 */
ProductVariations200ResponseSkusInner.prototype['listPriceFormated'] = undefined;

/**
 * @member {module:model/ProductVariations200ResponseSkusInnerMeasures} measures
 */
ProductVariations200ResponseSkusInner.prototype['measures'] = undefined;

/**
 * SKU reward value for rewards program.
 * @member {Number} rewardValue
 */
ProductVariations200ResponseSkusInner.prototype['rewardValue'] = undefined;

/**
 * Seller ID.
 * @member {String} sellerId
 */
ProductVariations200ResponseSkusInner.prototype['sellerId'] = undefined;

/**
 * SKU ID.
 * @member {Number} sku
 */
ProductVariations200ResponseSkusInner.prototype['sku'] = undefined;

/**
 * SKU Name.
 * @member {String} skuname
 */
ProductVariations200ResponseSkusInner.prototype['skuname'] = undefined;

/**
 * Spot price.
 * @member {Number} spotPrice
 */
ProductVariations200ResponseSkusInner.prototype['spotPrice'] = undefined;

/**
 * Tax value.
 * @member {Number} taxAsInt
 */
ProductVariations200ResponseSkusInner.prototype['taxAsInt'] = undefined;

/**
 * Tax value formatted according to the valid currency.
 * @member {String} taxFormated
 */
ProductVariations200ResponseSkusInner.prototype['taxFormated'] = undefined;

/**
 * SKU Unit Multiplier.
 * @member {Number} unitMultiplier
 */
ProductVariations200ResponseSkusInner.prototype['unitMultiplier'] = undefined;






export default ProductVariations200ResponseSkusInner;

