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
 * The SkulistbyProductId model module.
 * @module model/SkulistbyProductId
 * @version 1.0
 */
class SkulistbyProductId {
    /**
     * Constructs a new <code>SkulistbyProductId</code>.
     * @alias module:model/SkulistbyProductId
     */
    constructor() { 
        
        SkulistbyProductId.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SkulistbyProductId</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SkulistbyProductId} obj Optional instance to populate.
     * @return {module:model/SkulistbyProductId} The populated <code>SkulistbyProductId</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SkulistbyProductId();

            if (data.hasOwnProperty('ActivateIfPossible')) {
                obj['ActivateIfPossible'] = ApiClient.convertToType(data['ActivateIfPossible'], 'Boolean');
            }
            if (data.hasOwnProperty('CommercialConditionId')) {
                obj['CommercialConditionId'] = ApiClient.convertToType(data['CommercialConditionId'], 'Number');
            }
            if (data.hasOwnProperty('CubicWeight')) {
                obj['CubicWeight'] = ApiClient.convertToType(data['CubicWeight'], 'Number');
            }
            if (data.hasOwnProperty('DateUpdated')) {
                obj['DateUpdated'] = ApiClient.convertToType(data['DateUpdated'], 'String');
            }
            if (data.hasOwnProperty('EstimatedDateArrival')) {
                obj['EstimatedDateArrival'] = ApiClient.convertToType(data['EstimatedDateArrival'], 'String');
            }
            if (data.hasOwnProperty('FlagKitItensSellApart')) {
                obj['FlagKitItensSellApart'] = ApiClient.convertToType(data['FlagKitItensSellApart'], 'Boolean');
            }
            if (data.hasOwnProperty('Height')) {
                obj['Height'] = ApiClient.convertToType(data['Height'], 'Number');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('InternalNote')) {
                obj['InternalNote'] = ApiClient.convertToType(data['InternalNote'], 'String');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsDynamicKit')) {
                obj['IsDynamicKit'] = ApiClient.convertToType(data['IsDynamicKit'], 'String');
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
            if (data.hasOwnProperty('IsPersisted')) {
                obj['IsPersisted'] = ApiClient.convertToType(data['IsPersisted'], 'Boolean');
            }
            if (data.hasOwnProperty('IsRemoved')) {
                obj['IsRemoved'] = ApiClient.convertToType(data['IsRemoved'], 'Boolean');
            }
            if (data.hasOwnProperty('IsTransported')) {
                obj['IsTransported'] = ApiClient.convertToType(data['IsTransported'], 'Boolean');
            }
            if (data.hasOwnProperty('Length')) {
                obj['Length'] = ApiClient.convertToType(data['Length'], 'Number');
            }
            if (data.hasOwnProperty('ManufacturerCode')) {
                obj['ManufacturerCode'] = ApiClient.convertToType(data['ManufacturerCode'], 'String');
            }
            if (data.hasOwnProperty('MeasurementUnit')) {
                obj['MeasurementUnit'] = ApiClient.convertToType(data['MeasurementUnit'], 'String');
            }
            if (data.hasOwnProperty('ModalId')) {
                obj['ModalId'] = ApiClient.convertToType(data['ModalId'], 'Number');
            }
            if (data.hasOwnProperty('ModalType')) {
                obj['ModalType'] = ApiClient.convertToType(data['ModalType'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'Number');
            }
            if (data.hasOwnProperty('ProductId')) {
                obj['ProductId'] = ApiClient.convertToType(data['ProductId'], 'Number');
            }
            if (data.hasOwnProperty('RealHeight')) {
                obj['RealHeight'] = ApiClient.convertToType(data['RealHeight'], 'Number');
            }
            if (data.hasOwnProperty('RealLength')) {
                obj['RealLength'] = ApiClient.convertToType(data['RealLength'], 'Number');
            }
            if (data.hasOwnProperty('RealWeightKg')) {
                obj['RealWeightKg'] = ApiClient.convertToType(data['RealWeightKg'], 'Number');
            }
            if (data.hasOwnProperty('RealWidth')) {
                obj['RealWidth'] = ApiClient.convertToType(data['RealWidth'], 'Number');
            }
            if (data.hasOwnProperty('RefId')) {
                obj['RefId'] = ApiClient.convertToType(data['RefId'], 'String');
            }
            if (data.hasOwnProperty('ReferenceStockKeepingUnitId')) {
                obj['ReferenceStockKeepingUnitId'] = ApiClient.convertToType(data['ReferenceStockKeepingUnitId'], 'String');
            }
            if (data.hasOwnProperty('RewardValue')) {
                obj['RewardValue'] = ApiClient.convertToType(data['RewardValue'], 'Number');
            }
            if (data.hasOwnProperty('UnitMultiplier')) {
                obj['UnitMultiplier'] = ApiClient.convertToType(data['UnitMultiplier'], 'Number');
            }
            if (data.hasOwnProperty('WeightKg')) {
                obj['WeightKg'] = ApiClient.convertToType(data['WeightKg'], 'Number');
            }
            if (data.hasOwnProperty('Width')) {
                obj['Width'] = ApiClient.convertToType(data['Width'], 'Number');
            }
            if (data.hasOwnProperty('isKitOptimized')) {
                obj['isKitOptimized'] = ApiClient.convertToType(data['isKitOptimized'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SkulistbyProductId</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SkulistbyProductId</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['DateUpdated'] && !(typeof data['DateUpdated'] === 'string' || data['DateUpdated'] instanceof String)) {
            throw new Error("Expected the field `DateUpdated` to be a primitive type in the JSON string but got " + data['DateUpdated']);
        }
        // ensure the json data is a string
        if (data['EstimatedDateArrival'] && !(typeof data['EstimatedDateArrival'] === 'string' || data['EstimatedDateArrival'] instanceof String)) {
            throw new Error("Expected the field `EstimatedDateArrival` to be a primitive type in the JSON string but got " + data['EstimatedDateArrival']);
        }
        // ensure the json data is a string
        if (data['InternalNote'] && !(typeof data['InternalNote'] === 'string' || data['InternalNote'] instanceof String)) {
            throw new Error("Expected the field `InternalNote` to be a primitive type in the JSON string but got " + data['InternalNote']);
        }
        // ensure the json data is a string
        if (data['IsDynamicKit'] && !(typeof data['IsDynamicKit'] === 'string' || data['IsDynamicKit'] instanceof String)) {
            throw new Error("Expected the field `IsDynamicKit` to be a primitive type in the JSON string but got " + data['IsDynamicKit']);
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
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['RefId'] && !(typeof data['RefId'] === 'string' || data['RefId'] instanceof String)) {
            throw new Error("Expected the field `RefId` to be a primitive type in the JSON string but got " + data['RefId']);
        }
        // ensure the json data is a string
        if (data['ReferenceStockKeepingUnitId'] && !(typeof data['ReferenceStockKeepingUnitId'] === 'string' || data['ReferenceStockKeepingUnitId'] instanceof String)) {
            throw new Error("Expected the field `ReferenceStockKeepingUnitId` to be a primitive type in the JSON string but got " + data['ReferenceStockKeepingUnitId']);
        }

        return true;
    }


}



/**
 * When set to `true`, this attribute will automatically update the SKU as active once associated with an image or an active component.
 * @member {Boolean} ActivateIfPossible
 */
SkulistbyProductId.prototype['ActivateIfPossible'] = undefined;

/**
 * SKU Commercial Condition ID.
 * @member {Number} CommercialConditionId
 */
SkulistbyProductId.prototype['CommercialConditionId'] = undefined;

/**
 * [Cubic weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128).
 * @member {Number} CubicWeight
 */
SkulistbyProductId.prototype['CubicWeight'] = undefined;

/**
 * Date when the product was updated for the most recent time.
 * @member {String} DateUpdated
 */
SkulistbyProductId.prototype['DateUpdated'] = undefined;

/**
 * SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date.
 * @member {String} EstimatedDateArrival
 */
SkulistbyProductId.prototype['EstimatedDateArrival'] = undefined;

/**
 * Defines if the SKU bundle items can be sold separately.
 * @member {Boolean} FlagKitItensSellApart
 */
SkulistbyProductId.prototype['FlagKitItensSellApart'] = undefined;

/**
 * SKU Height.
 * @member {Number} Height
 */
SkulistbyProductId.prototype['Height'] = undefined;

/**
 * SKU ID.
 * @member {Number} Id
 */
SkulistbyProductId.prototype['Id'] = undefined;

/**
 * Internal note.
 * @member {String} InternalNote
 */
SkulistbyProductId.prototype['InternalNote'] = undefined;

/**
 * Defines if the SKU is active or not.
 * @member {Boolean} IsActive
 */
SkulistbyProductId.prototype['IsActive'] = undefined;

/**
 * @member {String} IsDynamicKit
 */
SkulistbyProductId.prototype['IsDynamicKit'] = undefined;

/**
 * Defines if the purchase of the SKU will generate reward value for the customer.
 * @member {Boolean} IsGiftCardRecharge
 */
SkulistbyProductId.prototype['IsGiftCardRecharge'] = undefined;

/**
 * @member {Boolean} IsInventoried
 */
SkulistbyProductId.prototype['IsInventoried'] = undefined;

/**
 * Flag to set whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted.
 * @member {Boolean} IsKit
 */
SkulistbyProductId.prototype['IsKit'] = undefined;

/**
 * Defines if the SKU is persisted.
 * @member {Boolean} IsPersisted
 */
SkulistbyProductId.prototype['IsPersisted'] = undefined;

/**
 * Defines if the SKU is removed.
 * @member {Boolean} IsRemoved
 */
SkulistbyProductId.prototype['IsRemoved'] = undefined;

/**
 * @member {Boolean} IsTransported
 */
SkulistbyProductId.prototype['IsTransported'] = undefined;

/**
 * SKU Length.
 * @member {Number} Length
 */
SkulistbyProductId.prototype['Length'] = undefined;

/**
 * Product Supplier ID.
 * @member {String} ManufacturerCode
 */
SkulistbyProductId.prototype['ManufacturerCode'] = undefined;

/**
 * Measurement unit.
 * @member {String} MeasurementUnit
 */
SkulistbyProductId.prototype['MeasurementUnit'] = undefined;

/**
 * Delivery Method (Modal Type) ID.
 * @member {Number} ModalId
 */
SkulistbyProductId.prototype['ModalId'] = undefined;

/**
 * Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \"Chemicals\" or \"Refrigerated products\"). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy).
 * @member {String} ModalType
 */
SkulistbyProductId.prototype['ModalType'] = undefined;

/**
 * SKU Name.
 * @member {String} Name
 */
SkulistbyProductId.prototype['Name'] = undefined;

/**
 * SKU Position.
 * @member {Number} Position
 */
SkulistbyProductId.prototype['Position'] = undefined;

/**
 * Product ID.
 * @member {Number} ProductId
 */
SkulistbyProductId.prototype['ProductId'] = undefined;

/**
 * Real SKU Height.
 * @member {Number} RealHeight
 */
SkulistbyProductId.prototype['RealHeight'] = undefined;

/**
 * Real SKU Length.
 * @member {Number} RealLength
 */
SkulistbyProductId.prototype['RealLength'] = undefined;

/**
 * Real Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
 * @member {Number} RealWeightKg
 */
SkulistbyProductId.prototype['RealWeightKg'] = undefined;

/**
 * Real SKU Width.
 * @member {Number} RealWidth
 */
SkulistbyProductId.prototype['RealWidth'] = undefined;

/**
 * Product Reference ID.
 * @member {String} RefId
 */
SkulistbyProductId.prototype['RefId'] = undefined;

/**
 * SKU Reference ID.
 * @member {String} ReferenceStockKeepingUnitId
 */
SkulistbyProductId.prototype['ReferenceStockKeepingUnitId'] = undefined;

/**
 * Reward value related to the SKU.
 * @member {Number} RewardValue
 */
SkulistbyProductId.prototype['RewardValue'] = undefined;

/**
 * This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward.
 * @member {Number} UnitMultiplier
 */
SkulistbyProductId.prototype['UnitMultiplier'] = undefined;

/**
 * Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
 * @member {Number} WeightKg
 */
SkulistbyProductId.prototype['WeightKg'] = undefined;

/**
 * SKU Width.
 * @member {Number} Width
 */
SkulistbyProductId.prototype['Width'] = undefined;

/**
 * Defines if the SKU is a Optimized bundle.
 * @member {Boolean} isKitOptimized
 */
SkulistbyProductId.prototype['isKitOptimized'] = undefined;






export default SkulistbyProductId;

