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
import AlternateIds from './AlternateIds';
import Attachment from './Attachment';
import Dimension from './Dimension';
import Image from './Image';
import ProductSpecification from './ProductSpecification';
import RealDimension from './RealDimension';
import SkuSeller from './SkuSeller';
import SkuSpecification from './SkuSpecification';

/**
 * The GetSKUandContext model module.
 * @module model/GetSKUandContext
 * @version 1.0
 */
class GetSKUandContext {
    /**
     * Constructs a new <code>GetSKUandContext</code>.
     * @alias module:model/GetSKUandContext
     * @param alternateIdValues {Array.<String>} Array with values of alternative SKU IDs.
     * @param alternateIds {module:model/AlternateIds} 
     * @param attachments {Array.<module:model/Attachment>} Array with Attachments ID that are related to the SKU.
     * @param brandId {String} Product Brand ID.
     * @param brandName {String} Product Brand Name.
     * @param cSCIdentification {String} SKU Seller identification.
     * @param categories {Array.<String>} Array with Categories from the related Product.
     * @param collections {Array.<String>} Array with Collections ID that are related to the Product.
     * @param commercialConditionId {Number} SKU Commercial Condition ID.
     * @param detailUrl {String} Product URL.
     * @param dimension {module:model/Dimension} 
     * @param estimatedDateArrival {String} To add the product as pre-sale, enter the product estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. You must take into consideration both the launch date and the freight calculation for the arrival date.
     * @param id {Number} SKU ID.
     * @param imageUrl {String} SKU image URL.
     * @param images {Array.<module:model/Image>} Array with SKU images.
     * @param informationSource {String} Information Source.
     * @param isActive {Boolean} Defines if the SKU is active or not.
     * @param isGiftCardRecharge {Boolean} Defines if the purchase will generate a reward.
     * @param isInventoried {Boolean} 
     * @param isKit {Boolean} Defines if the SKU is part of a bundle.
     * @param isTransported {Boolean} 
     * @param kitItems {Array.<String>} Array with SKU IDs of bundle components.
     * @param manufacturerCode {String} Product Supplier ID.
     * @param measurementUnit {String} SKU Measurement Unit.
     * @param modalType {String} Modal Type.
     * @param nameComplete {String} Product Name and SKU Name concatenated.
     * @param productCategories {Object.<String, Object.<String, String>>} Object containing product categories. Structure: \"{CategoryID}\": \"{CategoryName}\".
     * @param productCategoryIds {String} Category Hierarchy with Category IDs.
     * @param productClustersIds {String} Product Clusters IDs.
     * @param productDescription {String} Product Description. HTML is allowed.
     * @param productGlobalCategoryId {Number} Global Category ID.
     * @param productId {Number} ID of the related Product.
     * @param productName {String} Product Name.
     * @param productSpecifications {Array.<module:model/ProductSpecification>} Array with related Product Specifications.
     * @param realDimension {module:model/RealDimension} 
     * @param rewardValue {Number} Reward value related to the SKU.
     * @param salesChannels {Array.<Number>} Array with the ID of all the Sales Channels that are related to the product.
     * @param services {Array.<String>} Array with Service IDs that are related to the SKU.
     * @param skuName {String} SKU Name.
     * @param skuSellers {Array.<module:model/SkuSeller>} Array with SKU Sellers data.
     * @param skuSpecifications {Array.<module:model/SkuSpecification>} Array with related SKU Specifications.
     * @param unitMultiplier {Number} This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward.
     */
    constructor(alternateIdValues, alternateIds, attachments, brandId, brandName, cSCIdentification, categories, collections, commercialConditionId, detailUrl, dimension, estimatedDateArrival, id, imageUrl, images, informationSource, isActive, isGiftCardRecharge, isInventoried, isKit, isTransported, kitItems, manufacturerCode, measurementUnit, modalType, nameComplete, productCategories, productCategoryIds, productClustersIds, productDescription, productGlobalCategoryId, productId, productName, productSpecifications, realDimension, rewardValue, salesChannels, services, skuName, skuSellers, skuSpecifications, unitMultiplier) { 
        
        GetSKUandContext.initialize(this, alternateIdValues, alternateIds, attachments, brandId, brandName, cSCIdentification, categories, collections, commercialConditionId, detailUrl, dimension, estimatedDateArrival, id, imageUrl, images, informationSource, isActive, isGiftCardRecharge, isInventoried, isKit, isTransported, kitItems, manufacturerCode, measurementUnit, modalType, nameComplete, productCategories, productCategoryIds, productClustersIds, productDescription, productGlobalCategoryId, productId, productName, productSpecifications, realDimension, rewardValue, salesChannels, services, skuName, skuSellers, skuSpecifications, unitMultiplier);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, alternateIdValues, alternateIds, attachments, brandId, brandName, cSCIdentification, categories, collections, commercialConditionId, detailUrl, dimension, estimatedDateArrival, id, imageUrl, images, informationSource, isActive, isGiftCardRecharge, isInventoried, isKit, isTransported, kitItems, manufacturerCode, measurementUnit, modalType, nameComplete, productCategories, productCategoryIds, productClustersIds, productDescription, productGlobalCategoryId, productId, productName, productSpecifications, realDimension, rewardValue, salesChannels, services, skuName, skuSellers, skuSpecifications, unitMultiplier) { 
        obj['AlternateIdValues'] = alternateIdValues;
        obj['AlternateIds'] = alternateIds;
        obj['Attachments'] = attachments;
        obj['BrandId'] = brandId;
        obj['BrandName'] = brandName;
        obj['CSCIdentification'] = cSCIdentification;
        obj['Categories'] = categories;
        obj['Collections'] = collections;
        obj['CommercialConditionId'] = commercialConditionId;
        obj['DetailUrl'] = detailUrl;
        obj['Dimension'] = dimension;
        obj['EstimatedDateArrival'] = estimatedDateArrival;
        obj['Id'] = id;
        obj['ImageUrl'] = imageUrl;
        obj['Images'] = images;
        obj['InformationSource'] = informationSource;
        obj['IsActive'] = isActive;
        obj['IsGiftCardRecharge'] = isGiftCardRecharge;
        obj['IsInventoried'] = isInventoried;
        obj['IsKit'] = isKit;
        obj['IsTransported'] = isTransported;
        obj['KitItems'] = kitItems;
        obj['ManufacturerCode'] = manufacturerCode;
        obj['MeasurementUnit'] = measurementUnit;
        obj['ModalType'] = modalType;
        obj['NameComplete'] = nameComplete;
        obj['ProductCategories'] = productCategories;
        obj['ProductCategoryIds'] = productCategoryIds;
        obj['ProductClustersIds'] = productClustersIds;
        obj['ProductDescription'] = productDescription;
        obj['ProductGlobalCategoryId'] = productGlobalCategoryId;
        obj['ProductId'] = productId;
        obj['ProductName'] = productName;
        obj['ProductSpecifications'] = productSpecifications;
        obj['RealDimension'] = realDimension;
        obj['RewardValue'] = rewardValue;
        obj['SalesChannels'] = salesChannels;
        obj['Services'] = services;
        obj['SkuName'] = skuName;
        obj['SkuSellers'] = skuSellers;
        obj['SkuSpecifications'] = skuSpecifications;
        obj['UnitMultiplier'] = unitMultiplier;
    }

    /**
     * Constructs a <code>GetSKUandContext</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetSKUandContext} obj Optional instance to populate.
     * @return {module:model/GetSKUandContext} The populated <code>GetSKUandContext</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetSKUandContext();

            if (data.hasOwnProperty('AlternateIdValues')) {
                obj['AlternateIdValues'] = ApiClient.convertToType(data['AlternateIdValues'], ['String']);
            }
            if (data.hasOwnProperty('AlternateIds')) {
                obj['AlternateIds'] = AlternateIds.constructFromObject(data['AlternateIds']);
            }
            if (data.hasOwnProperty('Attachments')) {
                obj['Attachments'] = ApiClient.convertToType(data['Attachments'], [Attachment]);
            }
            if (data.hasOwnProperty('BrandId')) {
                obj['BrandId'] = ApiClient.convertToType(data['BrandId'], 'String');
            }
            if (data.hasOwnProperty('BrandName')) {
                obj['BrandName'] = ApiClient.convertToType(data['BrandName'], 'String');
            }
            if (data.hasOwnProperty('CSCIdentification')) {
                obj['CSCIdentification'] = ApiClient.convertToType(data['CSCIdentification'], 'String');
            }
            if (data.hasOwnProperty('Categories')) {
                obj['Categories'] = ApiClient.convertToType(data['Categories'], ['String']);
            }
            if (data.hasOwnProperty('Collections')) {
                obj['Collections'] = ApiClient.convertToType(data['Collections'], ['String']);
            }
            if (data.hasOwnProperty('CommercialConditionId')) {
                obj['CommercialConditionId'] = ApiClient.convertToType(data['CommercialConditionId'], 'Number');
            }
            if (data.hasOwnProperty('ComplementName')) {
                obj['ComplementName'] = ApiClient.convertToType(data['ComplementName'], 'String');
            }
            if (data.hasOwnProperty('DetailUrl')) {
                obj['DetailUrl'] = ApiClient.convertToType(data['DetailUrl'], 'String');
            }
            if (data.hasOwnProperty('Dimension')) {
                obj['Dimension'] = Dimension.constructFromObject(data['Dimension']);
            }
            if (data.hasOwnProperty('EstimatedDateArrival')) {
                obj['EstimatedDateArrival'] = ApiClient.convertToType(data['EstimatedDateArrival'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('ImageUrl')) {
                obj['ImageUrl'] = ApiClient.convertToType(data['ImageUrl'], 'String');
            }
            if (data.hasOwnProperty('Images')) {
                obj['Images'] = ApiClient.convertToType(data['Images'], [Image]);
            }
            if (data.hasOwnProperty('InformationSource')) {
                obj['InformationSource'] = ApiClient.convertToType(data['InformationSource'], 'String');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsGiftCardRecharge')) {
                obj['IsGiftCardRecharge'] = ApiClient.convertToType(data['IsGiftCardRecharge'], 'Boolean');
            }
            if (data.hasOwnProperty('IsInventoried')) {
                obj['IsInventoried'] = ApiClient.convertToType(data['IsInventoried'], 'Boolean');
            }
            if (data.hasOwnProperty('IsKit')) {
                obj['IsKit'] = ApiClient.convertToType(data['IsKit'], 'Boolean');
            }
            if (data.hasOwnProperty('IsProductActive')) {
                obj['IsProductActive'] = ApiClient.convertToType(data['IsProductActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsTransported')) {
                obj['IsTransported'] = ApiClient.convertToType(data['IsTransported'], 'Boolean');
            }
            if (data.hasOwnProperty('KeyWords')) {
                obj['KeyWords'] = ApiClient.convertToType(data['KeyWords'], 'String');
            }
            if (data.hasOwnProperty('KitItems')) {
                obj['KitItems'] = ApiClient.convertToType(data['KitItems'], ['String']);
            }
            if (data.hasOwnProperty('ManufacturerCode')) {
                obj['ManufacturerCode'] = ApiClient.convertToType(data['ManufacturerCode'], 'String');
            }
            if (data.hasOwnProperty('MeasurementUnit')) {
                obj['MeasurementUnit'] = ApiClient.convertToType(data['MeasurementUnit'], 'String');
            }
            if (data.hasOwnProperty('ModalType')) {
                obj['ModalType'] = ApiClient.convertToType(data['ModalType'], 'String');
            }
            if (data.hasOwnProperty('NameComplete')) {
                obj['NameComplete'] = ApiClient.convertToType(data['NameComplete'], 'String');
            }
            if (data.hasOwnProperty('ProductCategories')) {
                obj['ProductCategories'] = ApiClient.convertToType(data['ProductCategories'], {'String': {'String': 'String'}});
            }
            if (data.hasOwnProperty('ProductCategoryIds')) {
                obj['ProductCategoryIds'] = ApiClient.convertToType(data['ProductCategoryIds'], 'String');
            }
            if (data.hasOwnProperty('ProductClustersIds')) {
                obj['ProductClustersIds'] = ApiClient.convertToType(data['ProductClustersIds'], 'String');
            }
            if (data.hasOwnProperty('ProductDescription')) {
                obj['ProductDescription'] = ApiClient.convertToType(data['ProductDescription'], 'String');
            }
            if (data.hasOwnProperty('ProductFinalScore')) {
                obj['ProductFinalScore'] = ApiClient.convertToType(data['ProductFinalScore'], 'Number');
            }
            if (data.hasOwnProperty('ProductGlobalCategoryId')) {
                obj['ProductGlobalCategoryId'] = ApiClient.convertToType(data['ProductGlobalCategoryId'], 'Number');
            }
            if (data.hasOwnProperty('ProductId')) {
                obj['ProductId'] = ApiClient.convertToType(data['ProductId'], 'Number');
            }
            if (data.hasOwnProperty('ProductIsVisible')) {
                obj['ProductIsVisible'] = ApiClient.convertToType(data['ProductIsVisible'], 'Boolean');
            }
            if (data.hasOwnProperty('ProductName')) {
                obj['ProductName'] = ApiClient.convertToType(data['ProductName'], 'String');
            }
            if (data.hasOwnProperty('ProductRefId')) {
                obj['ProductRefId'] = ApiClient.convertToType(data['ProductRefId'], 'String');
            }
            if (data.hasOwnProperty('ProductSpecifications')) {
                obj['ProductSpecifications'] = ApiClient.convertToType(data['ProductSpecifications'], [ProductSpecification]);
            }
            if (data.hasOwnProperty('RealDimension')) {
                obj['RealDimension'] = RealDimension.constructFromObject(data['RealDimension']);
            }
            if (data.hasOwnProperty('ReleaseDate')) {
                obj['ReleaseDate'] = ApiClient.convertToType(data['ReleaseDate'], 'String');
            }
            if (data.hasOwnProperty('RewardValue')) {
                obj['RewardValue'] = ApiClient.convertToType(data['RewardValue'], 'Number');
            }
            if (data.hasOwnProperty('SalesChannels')) {
                obj['SalesChannels'] = ApiClient.convertToType(data['SalesChannels'], ['Number']);
            }
            if (data.hasOwnProperty('Services')) {
                obj['Services'] = ApiClient.convertToType(data['Services'], ['String']);
            }
            if (data.hasOwnProperty('ShowIfNotAvailable')) {
                obj['ShowIfNotAvailable'] = ApiClient.convertToType(data['ShowIfNotAvailable'], 'Boolean');
            }
            if (data.hasOwnProperty('SkuName')) {
                obj['SkuName'] = ApiClient.convertToType(data['SkuName'], 'String');
            }
            if (data.hasOwnProperty('SkuSellers')) {
                obj['SkuSellers'] = ApiClient.convertToType(data['SkuSellers'], [SkuSeller]);
            }
            if (data.hasOwnProperty('SkuSpecifications')) {
                obj['SkuSpecifications'] = ApiClient.convertToType(data['SkuSpecifications'], [SkuSpecification]);
            }
            if (data.hasOwnProperty('TaxCode')) {
                obj['TaxCode'] = ApiClient.convertToType(data['TaxCode'], 'String');
            }
            if (data.hasOwnProperty('UnitMultiplier')) {
                obj['UnitMultiplier'] = ApiClient.convertToType(data['UnitMultiplier'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetSKUandContext</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetSKUandContext</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetSKUandContext.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['AlternateIdValues'])) {
            throw new Error("Expected the field `AlternateIdValues` to be an array in the JSON data but got " + data['AlternateIdValues']);
        }
        // validate the optional field `AlternateIds`
        if (data['AlternateIds']) { // data not null
          AlternateIds.validateJSON(data['AlternateIds']);
        }
        if (data['Attachments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Attachments'])) {
                throw new Error("Expected the field `Attachments` to be an array in the JSON data but got " + data['Attachments']);
            }
            // validate the optional field `Attachments` (array)
            for (const item of data['Attachments']) {
                Attachment.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['BrandId'] && !(typeof data['BrandId'] === 'string' || data['BrandId'] instanceof String)) {
            throw new Error("Expected the field `BrandId` to be a primitive type in the JSON string but got " + data['BrandId']);
        }
        // ensure the json data is a string
        if (data['BrandName'] && !(typeof data['BrandName'] === 'string' || data['BrandName'] instanceof String)) {
            throw new Error("Expected the field `BrandName` to be a primitive type in the JSON string but got " + data['BrandName']);
        }
        // ensure the json data is a string
        if (data['CSCIdentification'] && !(typeof data['CSCIdentification'] === 'string' || data['CSCIdentification'] instanceof String)) {
            throw new Error("Expected the field `CSCIdentification` to be a primitive type in the JSON string but got " + data['CSCIdentification']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Categories'])) {
            throw new Error("Expected the field `Categories` to be an array in the JSON data but got " + data['Categories']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Collections'])) {
            throw new Error("Expected the field `Collections` to be an array in the JSON data but got " + data['Collections']);
        }
        // ensure the json data is a string
        if (data['ComplementName'] && !(typeof data['ComplementName'] === 'string' || data['ComplementName'] instanceof String)) {
            throw new Error("Expected the field `ComplementName` to be a primitive type in the JSON string but got " + data['ComplementName']);
        }
        // ensure the json data is a string
        if (data['DetailUrl'] && !(typeof data['DetailUrl'] === 'string' || data['DetailUrl'] instanceof String)) {
            throw new Error("Expected the field `DetailUrl` to be a primitive type in the JSON string but got " + data['DetailUrl']);
        }
        // validate the optional field `Dimension`
        if (data['Dimension']) { // data not null
          Dimension.validateJSON(data['Dimension']);
        }
        // ensure the json data is a string
        if (data['EstimatedDateArrival'] && !(typeof data['EstimatedDateArrival'] === 'string' || data['EstimatedDateArrival'] instanceof String)) {
            throw new Error("Expected the field `EstimatedDateArrival` to be a primitive type in the JSON string but got " + data['EstimatedDateArrival']);
        }
        // ensure the json data is a string
        if (data['ImageUrl'] && !(typeof data['ImageUrl'] === 'string' || data['ImageUrl'] instanceof String)) {
            throw new Error("Expected the field `ImageUrl` to be a primitive type in the JSON string but got " + data['ImageUrl']);
        }
        if (data['Images']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Images'])) {
                throw new Error("Expected the field `Images` to be an array in the JSON data but got " + data['Images']);
            }
            // validate the optional field `Images` (array)
            for (const item of data['Images']) {
                Image.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['InformationSource'] && !(typeof data['InformationSource'] === 'string' || data['InformationSource'] instanceof String)) {
            throw new Error("Expected the field `InformationSource` to be a primitive type in the JSON string but got " + data['InformationSource']);
        }
        // ensure the json data is a string
        if (data['KeyWords'] && !(typeof data['KeyWords'] === 'string' || data['KeyWords'] instanceof String)) {
            throw new Error("Expected the field `KeyWords` to be a primitive type in the JSON string but got " + data['KeyWords']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['KitItems'])) {
            throw new Error("Expected the field `KitItems` to be an array in the JSON data but got " + data['KitItems']);
        }
        // ensure the json data is a string
        if (data['ManufacturerCode'] && !(typeof data['ManufacturerCode'] === 'string' || data['ManufacturerCode'] instanceof String)) {
            throw new Error("Expected the field `ManufacturerCode` to be a primitive type in the JSON string but got " + data['ManufacturerCode']);
        }
        // ensure the json data is a string
        if (data['MeasurementUnit'] && !(typeof data['MeasurementUnit'] === 'string' || data['MeasurementUnit'] instanceof String)) {
            throw new Error("Expected the field `MeasurementUnit` to be a primitive type in the JSON string but got " + data['MeasurementUnit']);
        }
        // ensure the json data is a string
        if (data['ModalType'] && !(typeof data['ModalType'] === 'string' || data['ModalType'] instanceof String)) {
            throw new Error("Expected the field `ModalType` to be a primitive type in the JSON string but got " + data['ModalType']);
        }
        // ensure the json data is a string
        if (data['NameComplete'] && !(typeof data['NameComplete'] === 'string' || data['NameComplete'] instanceof String)) {
            throw new Error("Expected the field `NameComplete` to be a primitive type in the JSON string but got " + data['NameComplete']);
        }
        // ensure the json data is a string
        if (data['ProductCategoryIds'] && !(typeof data['ProductCategoryIds'] === 'string' || data['ProductCategoryIds'] instanceof String)) {
            throw new Error("Expected the field `ProductCategoryIds` to be a primitive type in the JSON string but got " + data['ProductCategoryIds']);
        }
        // ensure the json data is a string
        if (data['ProductClustersIds'] && !(typeof data['ProductClustersIds'] === 'string' || data['ProductClustersIds'] instanceof String)) {
            throw new Error("Expected the field `ProductClustersIds` to be a primitive type in the JSON string but got " + data['ProductClustersIds']);
        }
        // ensure the json data is a string
        if (data['ProductDescription'] && !(typeof data['ProductDescription'] === 'string' || data['ProductDescription'] instanceof String)) {
            throw new Error("Expected the field `ProductDescription` to be a primitive type in the JSON string but got " + data['ProductDescription']);
        }
        // ensure the json data is a string
        if (data['ProductName'] && !(typeof data['ProductName'] === 'string' || data['ProductName'] instanceof String)) {
            throw new Error("Expected the field `ProductName` to be a primitive type in the JSON string but got " + data['ProductName']);
        }
        // ensure the json data is a string
        if (data['ProductRefId'] && !(typeof data['ProductRefId'] === 'string' || data['ProductRefId'] instanceof String)) {
            throw new Error("Expected the field `ProductRefId` to be a primitive type in the JSON string but got " + data['ProductRefId']);
        }
        if (data['ProductSpecifications']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['ProductSpecifications'])) {
                throw new Error("Expected the field `ProductSpecifications` to be an array in the JSON data but got " + data['ProductSpecifications']);
            }
            // validate the optional field `ProductSpecifications` (array)
            for (const item of data['ProductSpecifications']) {
                ProductSpecification.validateJSON(item);
            };
        }
        // validate the optional field `RealDimension`
        if (data['RealDimension']) { // data not null
          RealDimension.validateJSON(data['RealDimension']);
        }
        // ensure the json data is a string
        if (data['ReleaseDate'] && !(typeof data['ReleaseDate'] === 'string' || data['ReleaseDate'] instanceof String)) {
            throw new Error("Expected the field `ReleaseDate` to be a primitive type in the JSON string but got " + data['ReleaseDate']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['SalesChannels'])) {
            throw new Error("Expected the field `SalesChannels` to be an array in the JSON data but got " + data['SalesChannels']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Services'])) {
            throw new Error("Expected the field `Services` to be an array in the JSON data but got " + data['Services']);
        }
        // ensure the json data is a string
        if (data['SkuName'] && !(typeof data['SkuName'] === 'string' || data['SkuName'] instanceof String)) {
            throw new Error("Expected the field `SkuName` to be a primitive type in the JSON string but got " + data['SkuName']);
        }
        if (data['SkuSellers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['SkuSellers'])) {
                throw new Error("Expected the field `SkuSellers` to be an array in the JSON data but got " + data['SkuSellers']);
            }
            // validate the optional field `SkuSellers` (array)
            for (const item of data['SkuSellers']) {
                SkuSeller.validateJSON(item);
            };
        }
        if (data['SkuSpecifications']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['SkuSpecifications'])) {
                throw new Error("Expected the field `SkuSpecifications` to be an array in the JSON data but got " + data['SkuSpecifications']);
            }
            // validate the optional field `SkuSpecifications` (array)
            for (const item of data['SkuSpecifications']) {
                SkuSpecification.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['TaxCode'] && !(typeof data['TaxCode'] === 'string' || data['TaxCode'] instanceof String)) {
            throw new Error("Expected the field `TaxCode` to be a primitive type in the JSON string but got " + data['TaxCode']);
        }

        return true;
    }


}

GetSKUandContext.RequiredProperties = ["AlternateIdValues", "AlternateIds", "Attachments", "BrandId", "BrandName", "CSCIdentification", "Categories", "Collections", "CommercialConditionId", "DetailUrl", "Dimension", "EstimatedDateArrival", "Id", "ImageUrl", "Images", "InformationSource", "IsActive", "IsGiftCardRecharge", "IsInventoried", "IsKit", "IsTransported", "KitItems", "ManufacturerCode", "MeasurementUnit", "ModalType", "NameComplete", "ProductCategories", "ProductCategoryIds", "ProductClustersIds", "ProductDescription", "ProductGlobalCategoryId", "ProductId", "ProductName", "ProductSpecifications", "RealDimension", "RewardValue", "SalesChannels", "Services", "SkuName", "SkuSellers", "SkuSpecifications", "UnitMultiplier"];

/**
 * Array with values of alternative SKU IDs.
 * @member {Array.<String>} AlternateIdValues
 */
GetSKUandContext.prototype['AlternateIdValues'] = undefined;

/**
 * @member {module:model/AlternateIds} AlternateIds
 */
GetSKUandContext.prototype['AlternateIds'] = undefined;

/**
 * Array with Attachments ID that are related to the SKU.
 * @member {Array.<module:model/Attachment>} Attachments
 */
GetSKUandContext.prototype['Attachments'] = undefined;

/**
 * Product Brand ID.
 * @member {String} BrandId
 */
GetSKUandContext.prototype['BrandId'] = undefined;

/**
 * Product Brand Name.
 * @member {String} BrandName
 */
GetSKUandContext.prototype['BrandName'] = undefined;

/**
 * SKU Seller identification.
 * @member {String} CSCIdentification
 */
GetSKUandContext.prototype['CSCIdentification'] = undefined;

/**
 * Array with Categories from the related Product.
 * @member {Array.<String>} Categories
 */
GetSKUandContext.prototype['Categories'] = undefined;

/**
 * Array with Collections ID that are related to the Product.
 * @member {Array.<String>} Collections
 */
GetSKUandContext.prototype['Collections'] = undefined;

/**
 * SKU Commercial Condition ID.
 * @member {Number} CommercialConditionId
 */
GetSKUandContext.prototype['CommercialConditionId'] = undefined;

/**
 * Product Complement Name.
 * @member {String} ComplementName
 */
GetSKUandContext.prototype['ComplementName'] = undefined;

/**
 * Product URL.
 * @member {String} DetailUrl
 */
GetSKUandContext.prototype['DetailUrl'] = undefined;

/**
 * @member {module:model/Dimension} Dimension
 */
GetSKUandContext.prototype['Dimension'] = undefined;

/**
 * To add the product as pre-sale, enter the product estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. You must take into consideration both the launch date and the freight calculation for the arrival date.
 * @member {String} EstimatedDateArrival
 */
GetSKUandContext.prototype['EstimatedDateArrival'] = undefined;

/**
 * SKU ID.
 * @member {Number} Id
 */
GetSKUandContext.prototype['Id'] = undefined;

/**
 * SKU image URL.
 * @member {String} ImageUrl
 */
GetSKUandContext.prototype['ImageUrl'] = undefined;

/**
 * Array with SKU images.
 * @member {Array.<module:model/Image>} Images
 */
GetSKUandContext.prototype['Images'] = undefined;

/**
 * Information Source.
 * @member {String} InformationSource
 */
GetSKUandContext.prototype['InformationSource'] = undefined;

/**
 * Defines if the SKU is active or not.
 * @member {Boolean} IsActive
 */
GetSKUandContext.prototype['IsActive'] = undefined;

/**
 * Defines if the purchase will generate a reward.
 * @member {Boolean} IsGiftCardRecharge
 */
GetSKUandContext.prototype['IsGiftCardRecharge'] = undefined;

/**
 * @member {Boolean} IsInventoried
 */
GetSKUandContext.prototype['IsInventoried'] = undefined;

/**
 * Defines if the SKU is part of a bundle.
 * @member {Boolean} IsKit
 */
GetSKUandContext.prototype['IsKit'] = undefined;

/**
 * Defines if the product is active or not.
 * @member {Boolean} IsProductActive
 */
GetSKUandContext.prototype['IsProductActive'] = undefined;

/**
 * @member {Boolean} IsTransported
 */
GetSKUandContext.prototype['IsTransported'] = undefined;

/**
 * Keywords related to the product.
 * @member {String} KeyWords
 */
GetSKUandContext.prototype['KeyWords'] = undefined;

/**
 * Array with SKU IDs of bundle components.
 * @member {Array.<String>} KitItems
 */
GetSKUandContext.prototype['KitItems'] = undefined;

/**
 * Product Supplier ID.
 * @member {String} ManufacturerCode
 */
GetSKUandContext.prototype['ManufacturerCode'] = undefined;

/**
 * SKU Measurement Unit.
 * @member {String} MeasurementUnit
 */
GetSKUandContext.prototype['MeasurementUnit'] = undefined;

/**
 * Modal Type.
 * @member {String} ModalType
 */
GetSKUandContext.prototype['ModalType'] = undefined;

/**
 * Product Name and SKU Name concatenated.
 * @member {String} NameComplete
 */
GetSKUandContext.prototype['NameComplete'] = undefined;

/**
 * Object containing product categories. Structure: \"{CategoryID}\": \"{CategoryName}\".
 * @member {Object.<String, Object.<String, String>>} ProductCategories
 */
GetSKUandContext.prototype['ProductCategories'] = undefined;

/**
 * Category Hierarchy with Category IDs.
 * @member {String} ProductCategoryIds
 */
GetSKUandContext.prototype['ProductCategoryIds'] = undefined;

/**
 * Product Clusters IDs.
 * @member {String} ProductClustersIds
 */
GetSKUandContext.prototype['ProductClustersIds'] = undefined;

/**
 * Product Description. HTML is allowed.
 * @member {String} ProductDescription
 */
GetSKUandContext.prototype['ProductDescription'] = undefined;

/**
 * Product Final Score.
 * @member {Number} ProductFinalScore
 */
GetSKUandContext.prototype['ProductFinalScore'] = undefined;

/**
 * Global Category ID.
 * @member {Number} ProductGlobalCategoryId
 */
GetSKUandContext.prototype['ProductGlobalCategoryId'] = undefined;

/**
 * ID of the related Product.
 * @member {Number} ProductId
 */
GetSKUandContext.prototype['ProductId'] = undefined;

/**
 * Defines if the product is visible or not.
 * @member {Boolean} ProductIsVisible
 */
GetSKUandContext.prototype['ProductIsVisible'] = undefined;

/**
 * Product Name.
 * @member {String} ProductName
 */
GetSKUandContext.prototype['ProductName'] = undefined;

/**
 * Reference ID of the related Product.
 * @member {String} ProductRefId
 */
GetSKUandContext.prototype['ProductRefId'] = undefined;

/**
 * Array with related Product Specifications.
 * @member {Array.<module:model/ProductSpecification>} ProductSpecifications
 */
GetSKUandContext.prototype['ProductSpecifications'] = undefined;

/**
 * @member {module:model/RealDimension} RealDimension
 */
GetSKUandContext.prototype['RealDimension'] = undefined;

/**
 * Release date of the product.
 * @member {String} ReleaseDate
 */
GetSKUandContext.prototype['ReleaseDate'] = undefined;

/**
 * Reward value related to the SKU.
 * @member {Number} RewardValue
 */
GetSKUandContext.prototype['RewardValue'] = undefined;

/**
 * Array with the ID of all the Sales Channels that are related to the product.
 * @member {Array.<Number>} SalesChannels
 */
GetSKUandContext.prototype['SalesChannels'] = undefined;

/**
 * Array with Service IDs that are related to the SKU.
 * @member {Array.<String>} Services
 */
GetSKUandContext.prototype['Services'] = undefined;

/**
 * Defines if the product will be shown if it is not available.
 * @member {Boolean} ShowIfNotAvailable
 */
GetSKUandContext.prototype['ShowIfNotAvailable'] = undefined;

/**
 * SKU Name.
 * @member {String} SkuName
 */
GetSKUandContext.prototype['SkuName'] = undefined;

/**
 * Array with SKU Sellers data.
 * @member {Array.<module:model/SkuSeller>} SkuSellers
 */
GetSKUandContext.prototype['SkuSellers'] = undefined;

/**
 * Array with related SKU Specifications.
 * @member {Array.<module:model/SkuSpecification>} SkuSpecifications
 */
GetSKUandContext.prototype['SkuSpecifications'] = undefined;

/**
 * SKU Tax Code.
 * @member {String} TaxCode
 */
GetSKUandContext.prototype['TaxCode'] = undefined;

/**
 * This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward.
 * @member {Number} UnitMultiplier
 */
GetSKUandContext.prototype['UnitMultiplier'] = undefined;






export default GetSKUandContext;

