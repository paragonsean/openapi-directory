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
 * The CreateSeller200Response model module.
 * @module model/CreateSeller200Response
 * @version 1.0
 */
class CreateSeller200Response {
    /**
     * Constructs a new <code>CreateSeller200Response</code>.
     * @alias module:model/CreateSeller200Response
     */
    constructor() { 
        
        CreateSeller200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateSeller200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateSeller200Response} obj Optional instance to populate.
     * @return {module:model/CreateSeller200Response} The populated <code>CreateSeller200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateSeller200Response();

            if (data.hasOwnProperty('ArchiveId')) {
                obj['ArchiveId'] = ApiClient.convertToType(data['ArchiveId'], 'Number');
            }
            if (data.hasOwnProperty('CNPJ')) {
                obj['CNPJ'] = ApiClient.convertToType(data['CNPJ'], 'String');
            }
            if (data.hasOwnProperty('CSCIdentification')) {
                obj['CSCIdentification'] = ApiClient.convertToType(data['CSCIdentification'], 'String');
            }
            if (data.hasOwnProperty('CatalogSystemEndpoint')) {
                obj['CatalogSystemEndpoint'] = ApiClient.convertToType(data['CatalogSystemEndpoint'], 'String');
            }
            if (data.hasOwnProperty('CategoryCommissionPercentage')) {
                obj['CategoryCommissionPercentage'] = ApiClient.convertToType(data['CategoryCommissionPercentage'], 'String');
            }
            if (data.hasOwnProperty('DeliveryPolicy')) {
                obj['DeliveryPolicy'] = ApiClient.convertToType(data['DeliveryPolicy'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('ExchangeReturnPolicy')) {
                obj['ExchangeReturnPolicy'] = ApiClient.convertToType(data['ExchangeReturnPolicy'], 'String');
            }
            if (data.hasOwnProperty('FreightCommissionPercentage')) {
                obj['FreightCommissionPercentage'] = ApiClient.convertToType(data['FreightCommissionPercentage'], 'Number');
            }
            if (data.hasOwnProperty('FulfillmentEndpoint')) {
                obj['FulfillmentEndpoint'] = ApiClient.convertToType(data['FulfillmentEndpoint'], 'String');
            }
            if (data.hasOwnProperty('FulfillmentSellerId')) {
                obj['FulfillmentSellerId'] = ApiClient.convertToType(data['FulfillmentSellerId'], 'Number');
            }
            if (data.hasOwnProperty('IsActive')) {
                obj['IsActive'] = ApiClient.convertToType(data['IsActive'], 'Boolean');
            }
            if (data.hasOwnProperty('IsBetterScope')) {
                obj['IsBetterScope'] = ApiClient.convertToType(data['IsBetterScope'], 'Boolean');
            }
            if (data.hasOwnProperty('MerchantName')) {
                obj['MerchantName'] = ApiClient.convertToType(data['MerchantName'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Password')) {
                obj['Password'] = ApiClient.convertToType(data['Password'], 'String');
            }
            if (data.hasOwnProperty('ProductCommissionPercentage')) {
                obj['ProductCommissionPercentage'] = ApiClient.convertToType(data['ProductCommissionPercentage'], 'Number');
            }
            if (data.hasOwnProperty('SecutityPrivacyPolicy')) {
                obj['SecutityPrivacyPolicy'] = ApiClient.convertToType(data['SecutityPrivacyPolicy'], 'String');
            }
            if (data.hasOwnProperty('SellerId')) {
                obj['SellerId'] = ApiClient.convertToType(data['SellerId'], 'String');
            }
            if (data.hasOwnProperty('SellerType')) {
                obj['SellerType'] = ApiClient.convertToType(data['SellerType'], 'Number');
            }
            if (data.hasOwnProperty('TrustPolicy')) {
                obj['TrustPolicy'] = ApiClient.convertToType(data['TrustPolicy'], 'String');
            }
            if (data.hasOwnProperty('UrlLogo')) {
                obj['UrlLogo'] = ApiClient.convertToType(data['UrlLogo'], 'String');
            }
            if (data.hasOwnProperty('UseHybridPaymentOptions')) {
                obj['UseHybridPaymentOptions'] = ApiClient.convertToType(data['UseHybridPaymentOptions'], 'Boolean');
            }
            if (data.hasOwnProperty('UserName')) {
                obj['UserName'] = ApiClient.convertToType(data['UserName'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateSeller200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateSeller200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['CNPJ'] && !(typeof data['CNPJ'] === 'string' || data['CNPJ'] instanceof String)) {
            throw new Error("Expected the field `CNPJ` to be a primitive type in the JSON string but got " + data['CNPJ']);
        }
        // ensure the json data is a string
        if (data['CSCIdentification'] && !(typeof data['CSCIdentification'] === 'string' || data['CSCIdentification'] instanceof String)) {
            throw new Error("Expected the field `CSCIdentification` to be a primitive type in the JSON string but got " + data['CSCIdentification']);
        }
        // ensure the json data is a string
        if (data['CatalogSystemEndpoint'] && !(typeof data['CatalogSystemEndpoint'] === 'string' || data['CatalogSystemEndpoint'] instanceof String)) {
            throw new Error("Expected the field `CatalogSystemEndpoint` to be a primitive type in the JSON string but got " + data['CatalogSystemEndpoint']);
        }
        // ensure the json data is a string
        if (data['CategoryCommissionPercentage'] && !(typeof data['CategoryCommissionPercentage'] === 'string' || data['CategoryCommissionPercentage'] instanceof String)) {
            throw new Error("Expected the field `CategoryCommissionPercentage` to be a primitive type in the JSON string but got " + data['CategoryCommissionPercentage']);
        }
        // ensure the json data is a string
        if (data['DeliveryPolicy'] && !(typeof data['DeliveryPolicy'] === 'string' || data['DeliveryPolicy'] instanceof String)) {
            throw new Error("Expected the field `DeliveryPolicy` to be a primitive type in the JSON string but got " + data['DeliveryPolicy']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['ExchangeReturnPolicy'] && !(typeof data['ExchangeReturnPolicy'] === 'string' || data['ExchangeReturnPolicy'] instanceof String)) {
            throw new Error("Expected the field `ExchangeReturnPolicy` to be a primitive type in the JSON string but got " + data['ExchangeReturnPolicy']);
        }
        // ensure the json data is a string
        if (data['FulfillmentEndpoint'] && !(typeof data['FulfillmentEndpoint'] === 'string' || data['FulfillmentEndpoint'] instanceof String)) {
            throw new Error("Expected the field `FulfillmentEndpoint` to be a primitive type in the JSON string but got " + data['FulfillmentEndpoint']);
        }
        // ensure the json data is a string
        if (data['MerchantName'] && !(typeof data['MerchantName'] === 'string' || data['MerchantName'] instanceof String)) {
            throw new Error("Expected the field `MerchantName` to be a primitive type in the JSON string but got " + data['MerchantName']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Password'] && !(typeof data['Password'] === 'string' || data['Password'] instanceof String)) {
            throw new Error("Expected the field `Password` to be a primitive type in the JSON string but got " + data['Password']);
        }
        // ensure the json data is a string
        if (data['SecutityPrivacyPolicy'] && !(typeof data['SecutityPrivacyPolicy'] === 'string' || data['SecutityPrivacyPolicy'] instanceof String)) {
            throw new Error("Expected the field `SecutityPrivacyPolicy` to be a primitive type in the JSON string but got " + data['SecutityPrivacyPolicy']);
        }
        // ensure the json data is a string
        if (data['SellerId'] && !(typeof data['SellerId'] === 'string' || data['SellerId'] instanceof String)) {
            throw new Error("Expected the field `SellerId` to be a primitive type in the JSON string but got " + data['SellerId']);
        }
        // ensure the json data is a string
        if (data['TrustPolicy'] && !(typeof data['TrustPolicy'] === 'string' || data['TrustPolicy'] instanceof String)) {
            throw new Error("Expected the field `TrustPolicy` to be a primitive type in the JSON string but got " + data['TrustPolicy']);
        }
        // ensure the json data is a string
        if (data['UrlLogo'] && !(typeof data['UrlLogo'] === 'string' || data['UrlLogo'] instanceof String)) {
            throw new Error("Expected the field `UrlLogo` to be a primitive type in the JSON string but got " + data['UrlLogo']);
        }
        // ensure the json data is a string
        if (data['UserName'] && !(typeof data['UserName'] === 'string' || data['UserName'] instanceof String)) {
            throw new Error("Expected the field `UserName` to be a primitive type in the JSON string but got " + data['UserName']);
        }

        return true;
    }


}



/**
 * Seller archive ID.
 * @member {Number} ArchiveId
 */
CreateSeller200Response.prototype['ArchiveId'] = undefined;

/**
 * Company registration number.
 * @member {String} CNPJ
 */
CreateSeller200Response.prototype['CNPJ'] = undefined;

/**
 * CSC identification.
 * @member {String} CSCIdentification
 */
CreateSeller200Response.prototype['CSCIdentification'] = undefined;

/**
 * URL of the endpoint of the seller's catalog. This field will only be displayed if the seller type is VTEX Store. The field format will be as follows: `http://{sellerName}.vtexcommercestable.com.br/api/catalog_system/`.
 * @member {String} CatalogSystemEndpoint
 */
CreateSeller200Response.prototype['CatalogSystemEndpoint'] = undefined;

/**
 * The percentage that must be filled in as agreed between the marketplace and the seller. If there is no such commission, please fill in the field with the value: `0.00`.
 * @member {String} CategoryCommissionPercentage
 */
CreateSeller200Response.prototype['CategoryCommissionPercentage'] = undefined;

/**
 * Text describing the delivery policy previously agreed between the marketplace and the seller.
 * @member {String} DeliveryPolicy
 */
CreateSeller200Response.prototype['DeliveryPolicy'] = undefined;

/**
 * Text describing the seller with a marketing tone. You can display this text in the marketplace window display by [customizing the CMS](https://help.vtex.com/en/tutorial/list-of-controls-for-templates--tutorials_563).
 * @member {String} Description
 */
CreateSeller200Response.prototype['Description'] = undefined;

/**
 * Email of the admin responsible for the seller. 
 * @member {String} Email
 */
CreateSeller200Response.prototype['Email'] = undefined;

/**
 * Text describing the exchange and return policy previously agreed between the marketplace and the seller.
 * @member {String} ExchangeReturnPolicy
 */
CreateSeller200Response.prototype['ExchangeReturnPolicy'] = undefined;

/**
 * The percentage that must be filled in as agreed between the marketplace and the seller. If there is no such commission, please fill in the field with the value: `0.00`.
 * @member {Number} FreightCommissionPercentage
 */
CreateSeller200Response.prototype['FreightCommissionPercentage'] = undefined;

/**
 * URL of the endpoint for fulfillment of seller's orders, which the marketplace will use to communicate with the seller. This field applies to all sellers, regardless of their type. However, for `VTEX Stores`, you don’t need to fill it in because the system will do that automatically. You can edit this field once the seller has been successfully added.
 * @member {String} FulfillmentEndpoint
 */
CreateSeller200Response.prototype['FulfillmentEndpoint'] = undefined;

/**
 * Identification code of the seller responsible for fulfilling the order. This is an optional field used when a seller sells SKUs from another seller. If the seller sells their own SKUs, it must be left blank.
 * @member {Number} FulfillmentSellerId
 */
CreateSeller200Response.prototype['FulfillmentSellerId'] = undefined;

/**
 * If the selle is active (`true`) or not (`false`).
 * @member {Boolean} IsActive
 */
CreateSeller200Response.prototype['IsActive'] = undefined;

/**
 * Indicates whether it is a [comprehensive seller](https://help.vtex.com/en/tutorial/comprehensive-seller--5Qn4O2GpjUIzWTPpvLUfkI).
 * @member {Boolean} IsBetterScope
 */
CreateSeller200Response.prototype['IsBetterScope'] = undefined;

/**
 * Name of the marketplace, used to guide payments. This field should be nulled if the marketplace is responsible for processing payments. Check out our [Split Payment](https://help.vtex.com/en/tutorial/split-de-pagamento--6k5JidhYRUxileNolY2VLx) article to know more.
 * @member {String} MerchantName
 */
CreateSeller200Response.prototype['MerchantName'] = undefined;

/**
 * Name of the account in the seller's environment. You can find it on **Account settings > Account > Account Name**). Applicable only if the seller uses their own payment method.
 * @member {String} Name
 */
CreateSeller200Response.prototype['Name'] = undefined;

/**
 * Seller password.
 * @member {String} Password
 */
CreateSeller200Response.prototype['Password'] = undefined;

/**
 * The percentage that must be filled in as agreed between the marketplace and the seller. If there is no such commission, please fill in the field with the value: `0.00`.
 * @member {Number} ProductCommissionPercentage
 */
CreateSeller200Response.prototype['ProductCommissionPercentage'] = undefined;

/**
 * Text describing the security policy previously agreed between the marketplace and the seller.
 * @member {String} SecutityPrivacyPolicy
 */
CreateSeller200Response.prototype['SecutityPrivacyPolicy'] = undefined;

/**
 * Code used to identify the seller. It is assigned by the marketplace. We recommend filling it in with the seller's account name.
 * @member {String} SellerId
 */
CreateSeller200Response.prototype['SellerId'] = undefined;

/**
 * Seller type.
 * @member {Number} SellerType
 */
CreateSeller200Response.prototype['SellerType'] = undefined;

/**
 * Seller trust policy. The default value is `'Default'`, but if your store is a B2B marketplace and you want to share the customers'emails with the sellers you need to set this field as `'AllowEmailSharing'`.
 * @member {String} TrustPolicy
 */
CreateSeller200Response.prototype['TrustPolicy'] = undefined;

/**
 * Seller URL logo.
 * @member {String} UrlLogo
 */
CreateSeller200Response.prototype['UrlLogo'] = undefined;

/**
 * Allows customers to use gift cards from the seller to buy their products on the marketplace. It identifies purchases made with a gift card so that only the final price (with discounts applied) is paid to the seller. 
 * @member {Boolean} UseHybridPaymentOptions
 */
CreateSeller200Response.prototype['UseHybridPaymentOptions'] = undefined;

/**
 * Seller username.
 * @member {String} UserName
 */
CreateSeller200Response.prototype['UserName'] = undefined;






export default CreateSeller200Response;

