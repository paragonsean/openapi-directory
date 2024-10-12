/*
 * Catalog API
 *   > Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | `{{accountName}}`         | Store account name                                                                      |  | `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |  | `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.AlternateIds;
import org.openapitools.client.model.Attachment;
import org.openapitools.client.model.Dimension;
import org.openapitools.client.model.Image;
import org.openapitools.client.model.ProductSpecification;
import org.openapitools.client.model.RealDimension;
import org.openapitools.client.model.SkuSeller;
import org.openapitools.client.model.SkuSpecification;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for GetSKUAltID
 */
public class GetSKUAltIDTest {
    private final GetSKUAltID model = new GetSKUAltID();

    /**
     * Model tests for GetSKUAltID
     */
    @Test
    public void testGetSKUAltID() {
        // TODO: test GetSKUAltID
    }

    /**
     * Test the property 'alternateIdValues'
     */
    @Test
    public void alternateIdValuesTest() {
        // TODO: test alternateIdValues
    }

    /**
     * Test the property 'alternateIds'
     */
    @Test
    public void alternateIdsTest() {
        // TODO: test alternateIds
    }

    /**
     * Test the property 'attachments'
     */
    @Test
    public void attachmentsTest() {
        // TODO: test attachments
    }

    /**
     * Test the property 'brandId'
     */
    @Test
    public void brandIdTest() {
        // TODO: test brandId
    }

    /**
     * Test the property 'brandName'
     */
    @Test
    public void brandNameTest() {
        // TODO: test brandName
    }

    /**
     * Test the property 'csCIdentification'
     */
    @Test
    public void csCIdentificationTest() {
        // TODO: test csCIdentification
    }

    /**
     * Test the property 'categories'
     */
    @Test
    public void categoriesTest() {
        // TODO: test categories
    }

    /**
     * Test the property 'categoriesFullPath'
     */
    @Test
    public void categoriesFullPathTest() {
        // TODO: test categoriesFullPath
    }

    /**
     * Test the property 'collections'
     */
    @Test
    public void collectionsTest() {
        // TODO: test collections
    }

    /**
     * Test the property 'commercialConditionId'
     */
    @Test
    public void commercialConditionIdTest() {
        // TODO: test commercialConditionId
    }

    /**
     * Test the property 'complementName'
     */
    @Test
    public void complementNameTest() {
        // TODO: test complementName
    }

    /**
     * Test the property 'detailUrl'
     */
    @Test
    public void detailUrlTest() {
        // TODO: test detailUrl
    }

    /**
     * Test the property 'dimension'
     */
    @Test
    public void dimensionTest() {
        // TODO: test dimension
    }

    /**
     * Test the property 'estimatedDateArrival'
     */
    @Test
    public void estimatedDateArrivalTest() {
        // TODO: test estimatedDateArrival
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'imageUrl'
     */
    @Test
    public void imageUrlTest() {
        // TODO: test imageUrl
    }

    /**
     * Test the property 'images'
     */
    @Test
    public void imagesTest() {
        // TODO: test images
    }

    /**
     * Test the property 'informationSource'
     */
    @Test
    public void informationSourceTest() {
        // TODO: test informationSource
    }

    /**
     * Test the property 'isActive'
     */
    @Test
    public void isActiveTest() {
        // TODO: test isActive
    }

    /**
     * Test the property 'isDirectCategoryActive'
     */
    @Test
    public void isDirectCategoryActiveTest() {
        // TODO: test isDirectCategoryActive
    }

    /**
     * Test the property 'isGiftCardRecharge'
     */
    @Test
    public void isGiftCardRechargeTest() {
        // TODO: test isGiftCardRecharge
    }

    /**
     * Test the property 'isInventoried'
     */
    @Test
    public void isInventoriedTest() {
        // TODO: test isInventoried
    }

    /**
     * Test the property 'isKit'
     */
    @Test
    public void isKitTest() {
        // TODO: test isKit
    }

    /**
     * Test the property 'isProductActive'
     */
    @Test
    public void isProductActiveTest() {
        // TODO: test isProductActive
    }

    /**
     * Test the property 'isTransported'
     */
    @Test
    public void isTransportedTest() {
        // TODO: test isTransported
    }

    /**
     * Test the property 'keyWords'
     */
    @Test
    public void keyWordsTest() {
        // TODO: test keyWords
    }

    /**
     * Test the property 'kitItems'
     */
    @Test
    public void kitItemsTest() {
        // TODO: test kitItems
    }

    /**
     * Test the property 'manufacturerCode'
     */
    @Test
    public void manufacturerCodeTest() {
        // TODO: test manufacturerCode
    }

    /**
     * Test the property 'measurementUnit'
     */
    @Test
    public void measurementUnitTest() {
        // TODO: test measurementUnit
    }

    /**
     * Test the property 'modalType'
     */
    @Test
    public void modalTypeTest() {
        // TODO: test modalType
    }

    /**
     * Test the property 'nameComplete'
     */
    @Test
    public void nameCompleteTest() {
        // TODO: test nameComplete
    }

    /**
     * Test the property 'positionsInClusters'
     */
    @Test
    public void positionsInClustersTest() {
        // TODO: test positionsInClusters
    }

    /**
     * Test the property 'productCategories'
     */
    @Test
    public void productCategoriesTest() {
        // TODO: test productCategories
    }

    /**
     * Test the property 'productCategoryIds'
     */
    @Test
    public void productCategoryIdsTest() {
        // TODO: test productCategoryIds
    }

    /**
     * Test the property 'productClusterHighlights'
     */
    @Test
    public void productClusterHighlightsTest() {
        // TODO: test productClusterHighlights
    }

    /**
     * Test the property 'productClusterNames'
     */
    @Test
    public void productClusterNamesTest() {
        // TODO: test productClusterNames
    }

    /**
     * Test the property 'productClustersIds'
     */
    @Test
    public void productClustersIdsTest() {
        // TODO: test productClustersIds
    }

    /**
     * Test the property 'productDescription'
     */
    @Test
    public void productDescriptionTest() {
        // TODO: test productDescription
    }

    /**
     * Test the property 'productFinalScore'
     */
    @Test
    public void productFinalScoreTest() {
        // TODO: test productFinalScore
    }

    /**
     * Test the property 'productGlobalCategoryId'
     */
    @Test
    public void productGlobalCategoryIdTest() {
        // TODO: test productGlobalCategoryId
    }

    /**
     * Test the property 'productId'
     */
    @Test
    public void productIdTest() {
        // TODO: test productId
    }

    /**
     * Test the property 'productIsVisible'
     */
    @Test
    public void productIsVisibleTest() {
        // TODO: test productIsVisible
    }

    /**
     * Test the property 'productName'
     */
    @Test
    public void productNameTest() {
        // TODO: test productName
    }

    /**
     * Test the property 'productRefId'
     */
    @Test
    public void productRefIdTest() {
        // TODO: test productRefId
    }

    /**
     * Test the property 'productSpecifications'
     */
    @Test
    public void productSpecificationsTest() {
        // TODO: test productSpecifications
    }

    /**
     * Test the property 'realDimension'
     */
    @Test
    public void realDimensionTest() {
        // TODO: test realDimension
    }

    /**
     * Test the property 'releaseDate'
     */
    @Test
    public void releaseDateTest() {
        // TODO: test releaseDate
    }

    /**
     * Test the property 'rewardValue'
     */
    @Test
    public void rewardValueTest() {
        // TODO: test rewardValue
    }

    /**
     * Test the property 'salesChannels'
     */
    @Test
    public void salesChannelsTest() {
        // TODO: test salesChannels
    }

    /**
     * Test the property 'services'
     */
    @Test
    public void servicesTest() {
        // TODO: test services
    }

    /**
     * Test the property 'showIfNotAvailable'
     */
    @Test
    public void showIfNotAvailableTest() {
        // TODO: test showIfNotAvailable
    }

    /**
     * Test the property 'skuName'
     */
    @Test
    public void skuNameTest() {
        // TODO: test skuName
    }

    /**
     * Test the property 'skuSellers'
     */
    @Test
    public void skuSellersTest() {
        // TODO: test skuSellers
    }

    /**
     * Test the property 'skuSpecifications'
     */
    @Test
    public void skuSpecificationsTest() {
        // TODO: test skuSpecifications
    }

    /**
     * Test the property 'taxCode'
     */
    @Test
    public void taxCodeTest() {
        // TODO: test taxCode
    }

    /**
     * Test the property 'unitMultiplier'
     */
    @Test
    public void unitMultiplierTest() {
        // TODO: test unitMultiplier
    }

}
