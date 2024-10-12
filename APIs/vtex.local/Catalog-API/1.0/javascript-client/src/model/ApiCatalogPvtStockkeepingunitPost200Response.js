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
 * The ApiCatalogPvtStockkeepingunitPost200Response model module.
 * @module model/ApiCatalogPvtStockkeepingunitPost200Response
 * @version 1.0
 */
class ApiCatalogPvtStockkeepingunitPost200Response {
    /**
     * Constructs a new <code>ApiCatalogPvtStockkeepingunitPost200Response</code>.
     * @alias module:model/ApiCatalogPvtStockkeepingunitPost200Response
     */
    constructor() { 
        
        ApiCatalogPvtStockkeepingunitPost200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiCatalogPvtStockkeepingunitPost200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiCatalogPvtStockkeepingunitPost200Response} obj Optional instance to populate.
     * @return {module:model/ApiCatalogPvtStockkeepingunitPost200Response} The populated <code>ApiCatalogPvtStockkeepingunitPost200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiCatalogPvtStockkeepingunitPost200Response();

            if (data.hasOwnProperty('ActivateIfPossible')) {
                obj['ActivateIfPossible'] = ApiClient.convertToType(data['ActivateIfPossible'], 'Boolean');
            }
            if (data.hasOwnProperty('CommercialConditionId')) {
                obj['CommercialConditionId'] = ApiClient.convertToType(data['CommercialConditionId'], 'Number');
            }
            if (data.hasOwnProperty('CreationDate')) {
                obj['CreationDate'] = ApiClient.convertToType(data['CreationDate'], 'String');
            }
            if (data.hasOwnProperty('CubicWeight')) {
                obj['CubicWeight'] = ApiClient.convertToType(data['CubicWeight'], 'Number');
            }
            if (data.hasOwnProperty('Ean')) {
                obj['Ean'] = ApiClient.convertToType(data['Ean'], 'String');
            }
            if (data.hasOwnProperty('EstimatedDateArrival')) {
                obj['EstimatedDateArrival'] = ApiClient.convertToType(data['EstimatedDateArrival'], 'String');
            }
            if (data.hasOwnProperty('Height')) {
                obj['Height'] = ApiClient.convertToType(data['Height'], 'Number');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsKit')) {
                obj['IsKit'] = ApiClient.convertToType(data['IsKit'], 'Boolean');
            }
            if (data.hasOwnProperty('KitItensSellApart')) {
                obj['KitItensSellApart'] = ApiClient.convertToType(data['KitItensSellApart'], 'Boolean');
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
            if (data.hasOwnProperty('ModalType')) {
                obj['ModalType'] = ApiClient.convertToType(data['ModalType'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('PackagedHeight')) {
                obj['PackagedHeight'] = ApiClient.convertToType(data['PackagedHeight'], 'Number');
            }
            if (data.hasOwnProperty('PackagedLength')) {
                obj['PackagedLength'] = ApiClient.convertToType(data['PackagedLength'], 'Number');
            }
            if (data.hasOwnProperty('PackagedWeightKg')) {
                obj['PackagedWeightKg'] = ApiClient.convertToType(data['PackagedWeightKg'], 'Number');
            }
            if (data.hasOwnProperty('PackagedWidth')) {
                obj['PackagedWidth'] = ApiClient.convertToType(data['PackagedWidth'], 'Number');
            }
            if (data.hasOwnProperty('ProductId')) {
                obj['ProductId'] = ApiClient.convertToType(data['ProductId'], 'Number');
            }
            if (data.hasOwnProperty('RefId')) {
                obj['RefId'] = ApiClient.convertToType(data['RefId'], 'String');
            }
            if (data.hasOwnProperty('RewardValue')) {
                obj['RewardValue'] = ApiClient.convertToType(data['RewardValue'], 'Number');
            }
            if (data.hasOwnProperty('UnitMultiplier')) {
                obj['UnitMultiplier'] = ApiClient.convertToType(data['UnitMultiplier'], 'Number');
            }
            if (data.hasOwnProperty('Videos')) {
                obj['Videos'] = ApiClient.convertToType(data['Videos'], ['String']);
            }
            if (data.hasOwnProperty('WeightKg')) {
                obj['WeightKg'] = ApiClient.convertToType(data['WeightKg'], 'Number');
            }
            if (data.hasOwnProperty('Width')) {
                obj['Width'] = ApiClient.convertToType(data['Width'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiCatalogPvtStockkeepingunitPost200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiCatalogPvtStockkeepingunitPost200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['CreationDate'] && !(typeof data['CreationDate'] === 'string' || data['CreationDate'] instanceof String)) {
            throw new Error("Expected the field `CreationDate` to be a primitive type in the JSON string but got " + data['CreationDate']);
        }
        // ensure the json data is a string
        if (data['Ean'] && !(typeof data['Ean'] === 'string' || data['Ean'] instanceof String)) {
            throw new Error("Expected the field `Ean` to be a primitive type in the JSON string but got " + data['Ean']);
        }
        // ensure the json data is a string
        if (data['EstimatedDateArrival'] && !(typeof data['EstimatedDateArrival'] === 'string' || data['EstimatedDateArrival'] instanceof String)) {
            throw new Error("Expected the field `EstimatedDateArrival` to be a primitive type in the JSON string but got " + data['EstimatedDateArrival']);
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
        // ensure the json data is an array
        if (!Array.isArray(data['Videos'])) {
            throw new Error("Expected the field `Videos` to be an array in the JSON data but got " + data['Videos']);
        }

        return true;
    }


}



/**
 * When set to `true`, this attribute will automatically update the SKU as active once associated with an image or an active component.
 * @member {Boolean} ActivateIfPossible
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['ActivateIfPossible'] = undefined;

/**
 * Used to define SKU specific promotions or installment rules. In case of no specific condition, use `1` (default value). This field does not accept `0`. Find out more by reading [Registering a commercial condition](https://help.vtex.com/tutorial/registering-a-commercial-condition--tutorials_445).
 * @member {Number} CommercialConditionId
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['CommercialConditionId'] = undefined;

/**
 * Date and time of the SKU's creation.
 * @member {String} CreationDate
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['CreationDate'] = undefined;

/**
 * [Cubic weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128).
 * @member {Number} CubicWeight
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['CubicWeight'] = undefined;

/**
 * EAN code. Required only if `RefId` is not informed, but can be used alongside `RefId` as well.
 * @member {String} Ean
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Ean'] = undefined;

/**
 * SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date.
 * @member {String} EstimatedDateArrival
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['EstimatedDateArrival'] = undefined;

/**
 * SKU real height.
 * @member {Number} Height
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Height'] = undefined;

/**
 * SKU unique identifier.
 * @member {Number} Id
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Id'] = undefined;

/**
 * Shows if the SKU is active (`true`) or not (`false`).
 * @member {Boolean} IsActive
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['IsActive'] = undefined;

/**
 * Flag to set whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted.
 * @member {Boolean} IsKit
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['IsKit'] = undefined;

/**
 * Defines if Kit components can be sold apart.
 * @member {Boolean} KitItensSellApart
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['KitItensSellApart'] = undefined;

/**
 * SKU real length.
 * @member {Number} Length
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Length'] = undefined;

/**
 * Provided by the manufacturers to identify their product. This field should be filled in if the product has a specific manufacturer’s code.
 * @member {String} ManufacturerCode
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['ManufacturerCode'] = undefined;

/**
 * Used only in cases when you need to convert the unit of measure for sale. If a product is sold in boxes for example, but customers want to buy per square meter (m²). In common cases, use `'un'`.
 * @member {String} MeasurementUnit
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['MeasurementUnit'] = undefined;

/**
 * Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \"Chemicals\" or \"Refrigerated products\"). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy).
 * @member {String} ModalType
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['ModalType'] = undefined;

/**
 * SKU name, meaning the variation of the previously added product. For example: **Product** - _Fridge_, **SKU** - _110V_.
 * @member {String} Name
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Name'] = undefined;

/**
 * Height used for shipping calculation.
 * @member {Number} PackagedHeight
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['PackagedHeight'] = undefined;

/**
 * Length used for shipping calculation.
 * @member {Number} PackagedLength
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['PackagedLength'] = undefined;

/**
 * Weight used for shipping calculation, in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
 * @member {Number} PackagedWeightKg
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['PackagedWeightKg'] = undefined;

/**
 * Width used for shipping calculation.
 * @member {Number} PackagedWidth
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['PackagedWidth'] = undefined;

/**
 * ID of the Product associated with this SKU.
 * @member {Number} ProductId
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['ProductId'] = undefined;

/**
 * Reference code used internally for organizational purposes. Must be unique. Required only if `Ean` is not informed, but can be used alongside `Ean` as well.
 * @member {String} RefId
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['RefId'] = undefined;

/**
 * Credit that the customer receives when finalizing an order of one specific SKU unit. By filling this field out with `1`, the customer gets U$ 1 credit on the site.
 * @member {Number} RewardValue
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['RewardValue'] = undefined;

/**
 * This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward.
 * @member {Number} UnitMultiplier
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['UnitMultiplier'] = undefined;

/**
 * Videos URLs.
 * @member {Array.<String>} Videos
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Videos'] = undefined;

/**
 * Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
 * @member {Number} WeightKg
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['WeightKg'] = undefined;

/**
 * SKU real width.
 * @member {Number} Width
 */
ApiCatalogPvtStockkeepingunitPost200Response.prototype['Width'] = undefined;






export default ApiCatalogPvtStockkeepingunitPost200Response;

