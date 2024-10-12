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


import ApiClient from './ApiClient';
import AlternateIds from './model/AlternateIds';
import ApiCatalogPvtAttachmentsGet200Response from './model/ApiCatalogPvtAttachmentsGet200Response';
import ApiCatalogPvtCategoryCategoryIdPutRequest from './model/ApiCatalogPvtCategoryCategoryIdPutRequest';
import ApiCatalogPvtCollectionCollectionIdPositionPostRequest from './model/ApiCatalogPvtCollectionCollectionIdPositionPostRequest';
import ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner from './model/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner';
import ApiCatalogPvtCollectionPost200Response from './model/ApiCatalogPvtCollectionPost200Response';
import ApiCatalogPvtProductPost200Response from './model/ApiCatalogPvtProductPost200Response';
import ApiCatalogPvtProductPostRequest from './model/ApiCatalogPvtProductPostRequest';
import ApiCatalogPvtProductProductIdPutRequest from './model/ApiCatalogPvtProductProductIdPutRequest';
import ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner from './model/ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner';
import ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response from './model/ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response';
import ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner from './model/ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner';
import ApiCatalogPvtProductProductIdSpecificationPost200Response from './model/ApiCatalogPvtProductProductIdSpecificationPost200Response';
import ApiCatalogPvtProductProductIdSpecificationPostRequest from './model/ApiCatalogPvtProductProductIdSpecificationPostRequest';
import ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner from './model/ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner';
import ApiCatalogPvtProductProductIdSpecificationvaluePutRequest from './model/ApiCatalogPvtProductProductIdSpecificationvaluePutRequest';
import ApiCatalogPvtSkuattachmentPost200Response from './model/ApiCatalogPvtSkuattachmentPost200Response';
import ApiCatalogPvtSkuservicetypeattachmentPost200Response from './model/ApiCatalogPvtSkuservicetypeattachmentPost200Response';
import ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner from './model/ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner';
import ApiCatalogPvtSpecificationPost200Response from './model/ApiCatalogPvtSpecificationPost200Response';
import ApiCatalogPvtSpecificationPostRequest from './model/ApiCatalogPvtSpecificationPostRequest';
import ApiCatalogPvtSpecificationgroupGroupIdPut200Response from './model/ApiCatalogPvtSpecificationgroupGroupIdPut200Response';
import ApiCatalogPvtSpecificationvaluePost200Response from './model/ApiCatalogPvtSpecificationvaluePost200Response';
import ApiCatalogPvtSpecificationvaluePostRequest from './model/ApiCatalogPvtSpecificationvaluePostRequest';
import ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response from './model/ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response';
import ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner from './model/ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner';
import ApiCatalogPvtStockkeepingunitGet200Response from './model/ApiCatalogPvtStockkeepingunitGet200Response';
import ApiCatalogPvtStockkeepingunitPost200Response from './model/ApiCatalogPvtStockkeepingunitPost200Response';
import ApiCatalogPvtStockkeepingunitPostRequest from './model/ApiCatalogPvtStockkeepingunitPostRequest';
import ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner from './model/ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner';
import ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response from './model/ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response';
import ApiCatalogPvtStockkeepingunitSkuIdPut200Response from './model/ApiCatalogPvtStockkeepingunitSkuIdPut200Response';
import ApiCatalogPvtStockkeepingunitSkuIdPutRequest from './model/ApiCatalogPvtStockkeepingunitSkuIdPutRequest';
import ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest from './model/ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest';
import ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner from './model/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner';
import ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest from './model/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest';
import ApiCatalogPvtSubcollectionPost200Response from './model/ApiCatalogPvtSubcollectionPost200Response';
import ApiCatalogPvtSubcollectionPostRequest from './model/ApiCatalogPvtSubcollectionPostRequest';
import ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response from './model/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response';
import ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response from './model/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response';
import ApiCatalogPvtSubcollectionSubCollectionIdPutRequest from './model/ApiCatalogPvtSubcollectionSubCollectionIdPutRequest';
import ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response from './model/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response';
import ArrayWithInformationOfAllTheCommercialConditionsInner from './model/ArrayWithInformationOfAllTheCommercialConditionsInner';
import AssociateattachmentstoSKURequest from './model/AssociateattachmentstoSKURequest';
import Attachment from './model/Attachment';
import AttachmentRequest from './model/AttachmentRequest';
import AttachmentResponse from './model/AttachmentResponse';
import BrandCreateUpdate from './model/BrandCreateUpdate';
import BrandGet from './model/BrandGet';
import BrandListPerPage200Response from './model/BrandListPerPage200Response';
import Category from './model/Category';
import CategorySpecificationInner from './model/CategorySpecificationInner';
import CreateCategoryRequest from './model/CreateCategoryRequest';
import CreateSeller200Response from './model/CreateSeller200Response';
import CreateSellerRequest from './model/CreateSellerRequest';
import CurrencyFormatInfo from './model/CurrencyFormatInfo';
import Dimension from './model/Dimension';
import DomainsInner from './model/DomainsInner';
import Field from './model/Field';
import GetCategoryTree from './model/GetCategoryTree';
import GetCategoryTreeChild from './model/GetCategoryTreeChild';
import GetCommercialConditions200Response from './model/GetCommercialConditions200Response';
import GetGiftList200Response from './model/GetGiftList200Response';
import GetProductSpecificationbyProductID200ResponseInner from './model/GetProductSpecificationbyProductID200ResponseInner';
import GetProductbyid200Response from './model/GetProductbyid200Response';
import GetSKUAltID from './model/GetSKUAltID';
import GetSKUandContext from './model/GetSKUandContext';
import GetSKUcomplementsbytype200Response from './model/GetSKUcomplementsbytype200Response';
import GetSKUseller200Response from './model/GetSKUseller200Response';
import GetSellerbyId200Response from './model/GetSellerbyId200Response';
import GetSellersbyId200Response from './model/GetSellersbyId200Response';
import GetSpecFieldValue from './model/GetSpecFieldValue';
import GetorUpdateProductSpecification from './model/GetorUpdateProductSpecification';
import GiftListMembersInner from './model/GiftListMembersInner';
import Image from './model/Image';
import Paging from './model/Paging';
import ProductAndSkuIds200Response from './model/ProductAndSkuIds200Response';
import ProductAndSkuIds200ResponseData from './model/ProductAndSkuIds200ResponseData';
import ProductAndSkuIds200ResponseRange from './model/ProductAndSkuIds200ResponseRange';
import ProductSpecification from './model/ProductSpecification';
import ProductVariations200Response from './model/ProductVariations200Response';
import ProductVariations200ResponseSkusInner from './model/ProductVariations200ResponseSkusInner';
import ProductVariations200ResponseSkusInnerMeasures from './model/ProductVariations200ResponseSkusInnerMeasures';
import ProductandTradePolicy200Response from './model/ProductandTradePolicy200Response';
import ProductbyRefId200Response from './model/ProductbyRefId200Response';
import RealDimension from './model/RealDimension';
import RequestBody from './model/RequestBody';
import RequestBody1 from './model/RequestBody1';
import RequestBody10 from './model/RequestBody10';
import RequestBody11 from './model/RequestBody11';
import RequestBody12 from './model/RequestBody12';
import RequestBody2 from './model/RequestBody2';
import RequestBody3 from './model/RequestBody3';
import RequestBody4 from './model/RequestBody4';
import RequestBody5 from './model/RequestBody5';
import RequestBody6 from './model/RequestBody6';
import RequestBody7 from './model/RequestBody7';
import RequestBody8 from './model/RequestBody8';
import RequestBody9 from './model/RequestBody9';
import ResquestBody from './model/ResquestBody';
import ResquestBody1 from './model/ResquestBody1';
import SKUFileURL from './model/SKUFileURL';
import SKUService from './model/SKUService';
import SKUServiceTypeRequest from './model/SKUServiceTypeRequest';
import SKUServiceTypeResponse from './model/SKUServiceTypeResponse';
import SKUServiceValueRequest from './model/SKUServiceValueRequest';
import SKUServiceValueResponse from './model/SKUServiceValueResponse';
import SKUSpecificationResponse from './model/SKUSpecificationResponse';
import SalesChannelbyId200Response from './model/SalesChannelbyId200Response';
import Sku200Response from './model/Sku200Response';
import SkuComplementInner from './model/SkuComplementInner';
import SkuKit from './model/SkuKit';
import SkuSeller from './model/SkuSeller';
import SkuSpecification from './model/SkuSpecification';
import SkulistbyProductId from './model/SkulistbyProductId';
import SpecificationGroupInsert2200Response from './model/SpecificationGroupInsert2200Response';
import SpecificationGroupInsertRequest from './model/SpecificationGroupInsertRequest';
import SpecificationsField200Response from './model/SpecificationsField200Response';
import SpecificationsGroup from './model/SpecificationsGroup';
import SpecificationsInsertFieldRequest from './model/SpecificationsInsertFieldRequest';
import SpecificationsInsertFieldUpdateRequest from './model/SpecificationsInsertFieldUpdateRequest';
import SpecificationsInsertFieldValueRequest from './model/SpecificationsInsertFieldValueRequest';
import SpecificationsUpdateFieldValueRequest from './model/SpecificationsUpdateFieldValueRequest';
import SupplierRequest from './model/SupplierRequest';
import SupplierResponse from './model/SupplierResponse';
import UpdateSeller200Response from './model/UpdateSeller200Response';
import UpdateSellerRequest from './model/UpdateSellerRequest';
import AttachmentApi from './api/AttachmentApi';
import BrandApi from './api/BrandApi';
import CategoryApi from './api/CategoryApi';
import CategorySpecificationApi from './api/CategorySpecificationApi';
import CollectionBetaApi from './api/CollectionBetaApi';
import CommercialConditionsApi from './api/CommercialConditionsApi';
import GiftListApi from './api/GiftListApi';
import LegacyCollectionApi from './api/LegacyCollectionApi';
import LegacySubcollectionApi from './api/LegacySubcollectionApi';
import NonStructuredSpecificationApi from './api/NonStructuredSpecificationApi';
import ProductApi from './api/ProductApi';
import ProductIndexingApi from './api/ProductIndexingApi';
import ProductSpecificationApi from './api/ProductSpecificationApi';
import SKUApi from './api/SKUApi';
import SKUAttachmentApi from './api/SKUAttachmentApi';
import SKUComplementApi from './api/SKUComplementApi';
import SKUEANApi from './api/SKUEANApi';
import SKUFileApi from './api/SKUFileApi';
import SKUKitApi from './api/SKUKitApi';
import SKUSellerApi from './api/SKUSellerApi';
import SKUServiceApi from './api/SKUServiceApi';
import SKUServiceAttachmentApi from './api/SKUServiceAttachmentApi';
import SKUServiceTypeApi from './api/SKUServiceTypeApi';
import SKUServiceValueApi from './api/SKUServiceValueApi';
import SKUSpecificationApi from './api/SKUSpecificationApi';
import SalesChannelApi from './api/SalesChannelApi';
import SellerApi from './api/SellerApi';
import SimilarCategoryApi from './api/SimilarCategoryApi';
import SpecificationApi from './api/SpecificationApi';
import SpecificationFieldApi from './api/SpecificationFieldApi';
import SpecificationFieldValueApi from './api/SpecificationFieldValueApi';
import SpecificationGroupApi from './api/SpecificationGroupApi';
import SpecificationValueApi from './api/SpecificationValueApi';
import SupplierApi from './api/SupplierApi';
import TradePolicyApi from './api/TradePolicyApi';


/**
*   &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between &#x60;{{}}&#x60; keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale&#x3D;en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale&#x3D;en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale&#x3D;en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale&#x3D;en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale&#x3D;en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale&#x3D;en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&amp;utm_source&#x3D;autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale&#x3D;en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale&#x3D;en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale&#x3D;en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale&#x3D;en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | &#x60;{{accountName}}&#x60;         | Store account name                                                                      |  | &#x60;{{environment}&#x60;          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | &#x60;{{X-VTEX-API-AppKey}}&#x60;   | Located in the headers of the requests, user authentication key                         |  | &#x60;{{X-VTEX-API-AppToken}}&#x60; | Located in the headers of the requests, authentication password                         |.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var CatalogApi = require('index'); // See note below*.
* var xxxSvc = new CatalogApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new CatalogApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new CatalogApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new CatalogApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AlternateIds model constructor.
     * @property {module:model/AlternateIds}
     */
    AlternateIds,

    /**
     * The ApiCatalogPvtAttachmentsGet200Response model constructor.
     * @property {module:model/ApiCatalogPvtAttachmentsGet200Response}
     */
    ApiCatalogPvtAttachmentsGet200Response,

    /**
     * The ApiCatalogPvtCategoryCategoryIdPutRequest model constructor.
     * @property {module:model/ApiCatalogPvtCategoryCategoryIdPutRequest}
     */
    ApiCatalogPvtCategoryCategoryIdPutRequest,

    /**
     * The ApiCatalogPvtCollectionCollectionIdPositionPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtCollectionCollectionIdPositionPostRequest}
     */
    ApiCatalogPvtCollectionCollectionIdPositionPostRequest,

    /**
     * The ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner}
     */
    ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner,

    /**
     * The ApiCatalogPvtCollectionPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtCollectionPost200Response}
     */
    ApiCatalogPvtCollectionPost200Response,

    /**
     * The ApiCatalogPvtProductPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtProductPost200Response}
     */
    ApiCatalogPvtProductPost200Response,

    /**
     * The ApiCatalogPvtProductPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtProductPostRequest}
     */
    ApiCatalogPvtProductPostRequest,

    /**
     * The ApiCatalogPvtProductProductIdPutRequest model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdPutRequest}
     */
    ApiCatalogPvtProductProductIdPutRequest,

    /**
     * The ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner}
     */
    ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner,

    /**
     * The ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response}
     */
    ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response,

    /**
     * The ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner}
     */
    ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner,

    /**
     * The ApiCatalogPvtProductProductIdSpecificationPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSpecificationPost200Response}
     */
    ApiCatalogPvtProductProductIdSpecificationPost200Response,

    /**
     * The ApiCatalogPvtProductProductIdSpecificationPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSpecificationPostRequest}
     */
    ApiCatalogPvtProductProductIdSpecificationPostRequest,

    /**
     * The ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner}
     */
    ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner,

    /**
     * The ApiCatalogPvtProductProductIdSpecificationvaluePutRequest model constructor.
     * @property {module:model/ApiCatalogPvtProductProductIdSpecificationvaluePutRequest}
     */
    ApiCatalogPvtProductProductIdSpecificationvaluePutRequest,

    /**
     * The ApiCatalogPvtSkuattachmentPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSkuattachmentPost200Response}
     */
    ApiCatalogPvtSkuattachmentPost200Response,

    /**
     * The ApiCatalogPvtSkuservicetypeattachmentPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSkuservicetypeattachmentPost200Response}
     */
    ApiCatalogPvtSkuservicetypeattachmentPost200Response,

    /**
     * The ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner}
     */
    ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner,

    /**
     * The ApiCatalogPvtSpecificationPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationPost200Response}
     */
    ApiCatalogPvtSpecificationPost200Response,

    /**
     * The ApiCatalogPvtSpecificationPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationPostRequest}
     */
    ApiCatalogPvtSpecificationPostRequest,

    /**
     * The ApiCatalogPvtSpecificationgroupGroupIdPut200Response model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationgroupGroupIdPut200Response}
     */
    ApiCatalogPvtSpecificationgroupGroupIdPut200Response,

    /**
     * The ApiCatalogPvtSpecificationvaluePost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationvaluePost200Response}
     */
    ApiCatalogPvtSpecificationvaluePost200Response,

    /**
     * The ApiCatalogPvtSpecificationvaluePostRequest model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationvaluePostRequest}
     */
    ApiCatalogPvtSpecificationvaluePostRequest,

    /**
     * The ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response model constructor.
     * @property {module:model/ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response}
     */
    ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response,

    /**
     * The ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner}
     */
    ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner,

    /**
     * The ApiCatalogPvtStockkeepingunitGet200Response model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitGet200Response}
     */
    ApiCatalogPvtStockkeepingunitGet200Response,

    /**
     * The ApiCatalogPvtStockkeepingunitPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitPost200Response}
     */
    ApiCatalogPvtStockkeepingunitPost200Response,

    /**
     * The ApiCatalogPvtStockkeepingunitPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitPostRequest}
     */
    ApiCatalogPvtStockkeepingunitPostRequest,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner}
     */
    ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response}
     */
    ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdPut200Response model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdPut200Response}
     */
    ApiCatalogPvtStockkeepingunitSkuIdPut200Response,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdPutRequest model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdPutRequest}
     */
    ApiCatalogPvtStockkeepingunitSkuIdPutRequest,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest}
     */
    ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner}
     */
    ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner,

    /**
     * The ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest model constructor.
     * @property {module:model/ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest}
     */
    ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest,

    /**
     * The ApiCatalogPvtSubcollectionPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSubcollectionPost200Response}
     */
    ApiCatalogPvtSubcollectionPost200Response,

    /**
     * The ApiCatalogPvtSubcollectionPostRequest model constructor.
     * @property {module:model/ApiCatalogPvtSubcollectionPostRequest}
     */
    ApiCatalogPvtSubcollectionPostRequest,

    /**
     * The ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response}
     */
    ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response,

    /**
     * The ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response}
     */
    ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response,

    /**
     * The ApiCatalogPvtSubcollectionSubCollectionIdPutRequest model constructor.
     * @property {module:model/ApiCatalogPvtSubcollectionSubCollectionIdPutRequest}
     */
    ApiCatalogPvtSubcollectionSubCollectionIdPutRequest,

    /**
     * The ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response model constructor.
     * @property {module:model/ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response}
     */
    ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response,

    /**
     * The ArrayWithInformationOfAllTheCommercialConditionsInner model constructor.
     * @property {module:model/ArrayWithInformationOfAllTheCommercialConditionsInner}
     */
    ArrayWithInformationOfAllTheCommercialConditionsInner,

    /**
     * The AssociateattachmentstoSKURequest model constructor.
     * @property {module:model/AssociateattachmentstoSKURequest}
     */
    AssociateattachmentstoSKURequest,

    /**
     * The Attachment model constructor.
     * @property {module:model/Attachment}
     */
    Attachment,

    /**
     * The AttachmentRequest model constructor.
     * @property {module:model/AttachmentRequest}
     */
    AttachmentRequest,

    /**
     * The AttachmentResponse model constructor.
     * @property {module:model/AttachmentResponse}
     */
    AttachmentResponse,

    /**
     * The BrandCreateUpdate model constructor.
     * @property {module:model/BrandCreateUpdate}
     */
    BrandCreateUpdate,

    /**
     * The BrandGet model constructor.
     * @property {module:model/BrandGet}
     */
    BrandGet,

    /**
     * The BrandListPerPage200Response model constructor.
     * @property {module:model/BrandListPerPage200Response}
     */
    BrandListPerPage200Response,

    /**
     * The Category model constructor.
     * @property {module:model/Category}
     */
    Category,

    /**
     * The CategorySpecificationInner model constructor.
     * @property {module:model/CategorySpecificationInner}
     */
    CategorySpecificationInner,

    /**
     * The CreateCategoryRequest model constructor.
     * @property {module:model/CreateCategoryRequest}
     */
    CreateCategoryRequest,

    /**
     * The CreateSeller200Response model constructor.
     * @property {module:model/CreateSeller200Response}
     */
    CreateSeller200Response,

    /**
     * The CreateSellerRequest model constructor.
     * @property {module:model/CreateSellerRequest}
     */
    CreateSellerRequest,

    /**
     * The CurrencyFormatInfo model constructor.
     * @property {module:model/CurrencyFormatInfo}
     */
    CurrencyFormatInfo,

    /**
     * The Dimension model constructor.
     * @property {module:model/Dimension}
     */
    Dimension,

    /**
     * The DomainsInner model constructor.
     * @property {module:model/DomainsInner}
     */
    DomainsInner,

    /**
     * The Field model constructor.
     * @property {module:model/Field}
     */
    Field,

    /**
     * The GetCategoryTree model constructor.
     * @property {module:model/GetCategoryTree}
     */
    GetCategoryTree,

    /**
     * The GetCategoryTreeChild model constructor.
     * @property {module:model/GetCategoryTreeChild}
     */
    GetCategoryTreeChild,

    /**
     * The GetCommercialConditions200Response model constructor.
     * @property {module:model/GetCommercialConditions200Response}
     */
    GetCommercialConditions200Response,

    /**
     * The GetGiftList200Response model constructor.
     * @property {module:model/GetGiftList200Response}
     */
    GetGiftList200Response,

    /**
     * The GetProductSpecificationbyProductID200ResponseInner model constructor.
     * @property {module:model/GetProductSpecificationbyProductID200ResponseInner}
     */
    GetProductSpecificationbyProductID200ResponseInner,

    /**
     * The GetProductbyid200Response model constructor.
     * @property {module:model/GetProductbyid200Response}
     */
    GetProductbyid200Response,

    /**
     * The GetSKUAltID model constructor.
     * @property {module:model/GetSKUAltID}
     */
    GetSKUAltID,

    /**
     * The GetSKUandContext model constructor.
     * @property {module:model/GetSKUandContext}
     */
    GetSKUandContext,

    /**
     * The GetSKUcomplementsbytype200Response model constructor.
     * @property {module:model/GetSKUcomplementsbytype200Response}
     */
    GetSKUcomplementsbytype200Response,

    /**
     * The GetSKUseller200Response model constructor.
     * @property {module:model/GetSKUseller200Response}
     */
    GetSKUseller200Response,

    /**
     * The GetSellerbyId200Response model constructor.
     * @property {module:model/GetSellerbyId200Response}
     */
    GetSellerbyId200Response,

    /**
     * The GetSellersbyId200Response model constructor.
     * @property {module:model/GetSellersbyId200Response}
     */
    GetSellersbyId200Response,

    /**
     * The GetSpecFieldValue model constructor.
     * @property {module:model/GetSpecFieldValue}
     */
    GetSpecFieldValue,

    /**
     * The GetorUpdateProductSpecification model constructor.
     * @property {module:model/GetorUpdateProductSpecification}
     */
    GetorUpdateProductSpecification,

    /**
     * The GiftListMembersInner model constructor.
     * @property {module:model/GiftListMembersInner}
     */
    GiftListMembersInner,

    /**
     * The Image model constructor.
     * @property {module:model/Image}
     */
    Image,

    /**
     * The Paging model constructor.
     * @property {module:model/Paging}
     */
    Paging,

    /**
     * The ProductAndSkuIds200Response model constructor.
     * @property {module:model/ProductAndSkuIds200Response}
     */
    ProductAndSkuIds200Response,

    /**
     * The ProductAndSkuIds200ResponseData model constructor.
     * @property {module:model/ProductAndSkuIds200ResponseData}
     */
    ProductAndSkuIds200ResponseData,

    /**
     * The ProductAndSkuIds200ResponseRange model constructor.
     * @property {module:model/ProductAndSkuIds200ResponseRange}
     */
    ProductAndSkuIds200ResponseRange,

    /**
     * The ProductSpecification model constructor.
     * @property {module:model/ProductSpecification}
     */
    ProductSpecification,

    /**
     * The ProductVariations200Response model constructor.
     * @property {module:model/ProductVariations200Response}
     */
    ProductVariations200Response,

    /**
     * The ProductVariations200ResponseSkusInner model constructor.
     * @property {module:model/ProductVariations200ResponseSkusInner}
     */
    ProductVariations200ResponseSkusInner,

    /**
     * The ProductVariations200ResponseSkusInnerMeasures model constructor.
     * @property {module:model/ProductVariations200ResponseSkusInnerMeasures}
     */
    ProductVariations200ResponseSkusInnerMeasures,

    /**
     * The ProductandTradePolicy200Response model constructor.
     * @property {module:model/ProductandTradePolicy200Response}
     */
    ProductandTradePolicy200Response,

    /**
     * The ProductbyRefId200Response model constructor.
     * @property {module:model/ProductbyRefId200Response}
     */
    ProductbyRefId200Response,

    /**
     * The RealDimension model constructor.
     * @property {module:model/RealDimension}
     */
    RealDimension,

    /**
     * The RequestBody model constructor.
     * @property {module:model/RequestBody}
     */
    RequestBody,

    /**
     * The RequestBody1 model constructor.
     * @property {module:model/RequestBody1}
     */
    RequestBody1,

    /**
     * The RequestBody10 model constructor.
     * @property {module:model/RequestBody10}
     */
    RequestBody10,

    /**
     * The RequestBody11 model constructor.
     * @property {module:model/RequestBody11}
     */
    RequestBody11,

    /**
     * The RequestBody12 model constructor.
     * @property {module:model/RequestBody12}
     */
    RequestBody12,

    /**
     * The RequestBody2 model constructor.
     * @property {module:model/RequestBody2}
     */
    RequestBody2,

    /**
     * The RequestBody3 model constructor.
     * @property {module:model/RequestBody3}
     */
    RequestBody3,

    /**
     * The RequestBody4 model constructor.
     * @property {module:model/RequestBody4}
     */
    RequestBody4,

    /**
     * The RequestBody5 model constructor.
     * @property {module:model/RequestBody5}
     */
    RequestBody5,

    /**
     * The RequestBody6 model constructor.
     * @property {module:model/RequestBody6}
     */
    RequestBody6,

    /**
     * The RequestBody7 model constructor.
     * @property {module:model/RequestBody7}
     */
    RequestBody7,

    /**
     * The RequestBody8 model constructor.
     * @property {module:model/RequestBody8}
     */
    RequestBody8,

    /**
     * The RequestBody9 model constructor.
     * @property {module:model/RequestBody9}
     */
    RequestBody9,

    /**
     * The ResquestBody model constructor.
     * @property {module:model/ResquestBody}
     */
    ResquestBody,

    /**
     * The ResquestBody1 model constructor.
     * @property {module:model/ResquestBody1}
     */
    ResquestBody1,

    /**
     * The SKUFileURL model constructor.
     * @property {module:model/SKUFileURL}
     */
    SKUFileURL,

    /**
     * The SKUService model constructor.
     * @property {module:model/SKUService}
     */
    SKUService,

    /**
     * The SKUServiceTypeRequest model constructor.
     * @property {module:model/SKUServiceTypeRequest}
     */
    SKUServiceTypeRequest,

    /**
     * The SKUServiceTypeResponse model constructor.
     * @property {module:model/SKUServiceTypeResponse}
     */
    SKUServiceTypeResponse,

    /**
     * The SKUServiceValueRequest model constructor.
     * @property {module:model/SKUServiceValueRequest}
     */
    SKUServiceValueRequest,

    /**
     * The SKUServiceValueResponse model constructor.
     * @property {module:model/SKUServiceValueResponse}
     */
    SKUServiceValueResponse,

    /**
     * The SKUSpecificationResponse model constructor.
     * @property {module:model/SKUSpecificationResponse}
     */
    SKUSpecificationResponse,

    /**
     * The SalesChannelbyId200Response model constructor.
     * @property {module:model/SalesChannelbyId200Response}
     */
    SalesChannelbyId200Response,

    /**
     * The Sku200Response model constructor.
     * @property {module:model/Sku200Response}
     */
    Sku200Response,

    /**
     * The SkuComplementInner model constructor.
     * @property {module:model/SkuComplementInner}
     */
    SkuComplementInner,

    /**
     * The SkuKit model constructor.
     * @property {module:model/SkuKit}
     */
    SkuKit,

    /**
     * The SkuSeller model constructor.
     * @property {module:model/SkuSeller}
     */
    SkuSeller,

    /**
     * The SkuSpecification model constructor.
     * @property {module:model/SkuSpecification}
     */
    SkuSpecification,

    /**
     * The SkulistbyProductId model constructor.
     * @property {module:model/SkulistbyProductId}
     */
    SkulistbyProductId,

    /**
     * The SpecificationGroupInsert2200Response model constructor.
     * @property {module:model/SpecificationGroupInsert2200Response}
     */
    SpecificationGroupInsert2200Response,

    /**
     * The SpecificationGroupInsertRequest model constructor.
     * @property {module:model/SpecificationGroupInsertRequest}
     */
    SpecificationGroupInsertRequest,

    /**
     * The SpecificationsField200Response model constructor.
     * @property {module:model/SpecificationsField200Response}
     */
    SpecificationsField200Response,

    /**
     * The SpecificationsGroup model constructor.
     * @property {module:model/SpecificationsGroup}
     */
    SpecificationsGroup,

    /**
     * The SpecificationsInsertFieldRequest model constructor.
     * @property {module:model/SpecificationsInsertFieldRequest}
     */
    SpecificationsInsertFieldRequest,

    /**
     * The SpecificationsInsertFieldUpdateRequest model constructor.
     * @property {module:model/SpecificationsInsertFieldUpdateRequest}
     */
    SpecificationsInsertFieldUpdateRequest,

    /**
     * The SpecificationsInsertFieldValueRequest model constructor.
     * @property {module:model/SpecificationsInsertFieldValueRequest}
     */
    SpecificationsInsertFieldValueRequest,

    /**
     * The SpecificationsUpdateFieldValueRequest model constructor.
     * @property {module:model/SpecificationsUpdateFieldValueRequest}
     */
    SpecificationsUpdateFieldValueRequest,

    /**
     * The SupplierRequest model constructor.
     * @property {module:model/SupplierRequest}
     */
    SupplierRequest,

    /**
     * The SupplierResponse model constructor.
     * @property {module:model/SupplierResponse}
     */
    SupplierResponse,

    /**
     * The UpdateSeller200Response model constructor.
     * @property {module:model/UpdateSeller200Response}
     */
    UpdateSeller200Response,

    /**
     * The UpdateSellerRequest model constructor.
     * @property {module:model/UpdateSellerRequest}
     */
    UpdateSellerRequest,

    /**
    * The AttachmentApi service constructor.
    * @property {module:api/AttachmentApi}
    */
    AttachmentApi,

    /**
    * The BrandApi service constructor.
    * @property {module:api/BrandApi}
    */
    BrandApi,

    /**
    * The CategoryApi service constructor.
    * @property {module:api/CategoryApi}
    */
    CategoryApi,

    /**
    * The CategorySpecificationApi service constructor.
    * @property {module:api/CategorySpecificationApi}
    */
    CategorySpecificationApi,

    /**
    * The CollectionBetaApi service constructor.
    * @property {module:api/CollectionBetaApi}
    */
    CollectionBetaApi,

    /**
    * The CommercialConditionsApi service constructor.
    * @property {module:api/CommercialConditionsApi}
    */
    CommercialConditionsApi,

    /**
    * The GiftListApi service constructor.
    * @property {module:api/GiftListApi}
    */
    GiftListApi,

    /**
    * The LegacyCollectionApi service constructor.
    * @property {module:api/LegacyCollectionApi}
    */
    LegacyCollectionApi,

    /**
    * The LegacySubcollectionApi service constructor.
    * @property {module:api/LegacySubcollectionApi}
    */
    LegacySubcollectionApi,

    /**
    * The NonStructuredSpecificationApi service constructor.
    * @property {module:api/NonStructuredSpecificationApi}
    */
    NonStructuredSpecificationApi,

    /**
    * The ProductApi service constructor.
    * @property {module:api/ProductApi}
    */
    ProductApi,

    /**
    * The ProductIndexingApi service constructor.
    * @property {module:api/ProductIndexingApi}
    */
    ProductIndexingApi,

    /**
    * The ProductSpecificationApi service constructor.
    * @property {module:api/ProductSpecificationApi}
    */
    ProductSpecificationApi,

    /**
    * The SKUApi service constructor.
    * @property {module:api/SKUApi}
    */
    SKUApi,

    /**
    * The SKUAttachmentApi service constructor.
    * @property {module:api/SKUAttachmentApi}
    */
    SKUAttachmentApi,

    /**
    * The SKUComplementApi service constructor.
    * @property {module:api/SKUComplementApi}
    */
    SKUComplementApi,

    /**
    * The SKUEANApi service constructor.
    * @property {module:api/SKUEANApi}
    */
    SKUEANApi,

    /**
    * The SKUFileApi service constructor.
    * @property {module:api/SKUFileApi}
    */
    SKUFileApi,

    /**
    * The SKUKitApi service constructor.
    * @property {module:api/SKUKitApi}
    */
    SKUKitApi,

    /**
    * The SKUSellerApi service constructor.
    * @property {module:api/SKUSellerApi}
    */
    SKUSellerApi,

    /**
    * The SKUServiceApi service constructor.
    * @property {module:api/SKUServiceApi}
    */
    SKUServiceApi,

    /**
    * The SKUServiceAttachmentApi service constructor.
    * @property {module:api/SKUServiceAttachmentApi}
    */
    SKUServiceAttachmentApi,

    /**
    * The SKUServiceTypeApi service constructor.
    * @property {module:api/SKUServiceTypeApi}
    */
    SKUServiceTypeApi,

    /**
    * The SKUServiceValueApi service constructor.
    * @property {module:api/SKUServiceValueApi}
    */
    SKUServiceValueApi,

    /**
    * The SKUSpecificationApi service constructor.
    * @property {module:api/SKUSpecificationApi}
    */
    SKUSpecificationApi,

    /**
    * The SalesChannelApi service constructor.
    * @property {module:api/SalesChannelApi}
    */
    SalesChannelApi,

    /**
    * The SellerApi service constructor.
    * @property {module:api/SellerApi}
    */
    SellerApi,

    /**
    * The SimilarCategoryApi service constructor.
    * @property {module:api/SimilarCategoryApi}
    */
    SimilarCategoryApi,

    /**
    * The SpecificationApi service constructor.
    * @property {module:api/SpecificationApi}
    */
    SpecificationApi,

    /**
    * The SpecificationFieldApi service constructor.
    * @property {module:api/SpecificationFieldApi}
    */
    SpecificationFieldApi,

    /**
    * The SpecificationFieldValueApi service constructor.
    * @property {module:api/SpecificationFieldValueApi}
    */
    SpecificationFieldValueApi,

    /**
    * The SpecificationGroupApi service constructor.
    * @property {module:api/SpecificationGroupApi}
    */
    SpecificationGroupApi,

    /**
    * The SpecificationValueApi service constructor.
    * @property {module:api/SpecificationValueApi}
    */
    SpecificationValueApi,

    /**
    * The SupplierApi service constructor.
    * @property {module:api/SupplierApi}
    */
    SupplierApi,

    /**
    * The TradePolicyApi service constructor.
    * @property {module:api/TradePolicyApi}
    */
    TradePolicyApi
};
