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

import java.util.Objects;
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

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * GetSKUAltID
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetSKUAltID {
  public static final String SERIALIZED_NAME_ALTERNATE_ID_VALUES = "AlternateIdValues";
  @SerializedName(SERIALIZED_NAME_ALTERNATE_ID_VALUES)
  private List<String> alternateIdValues = new ArrayList<>();

  public static final String SERIALIZED_NAME_ALTERNATE_IDS = "AlternateIds";
  @SerializedName(SERIALIZED_NAME_ALTERNATE_IDS)
  private AlternateIds alternateIds;

  public static final String SERIALIZED_NAME_ATTACHMENTS = "Attachments";
  @SerializedName(SERIALIZED_NAME_ATTACHMENTS)
  private List<Attachment> attachments = new ArrayList<>();

  public static final String SERIALIZED_NAME_BRAND_ID = "BrandId";
  @SerializedName(SERIALIZED_NAME_BRAND_ID)
  private String brandId;

  public static final String SERIALIZED_NAME_BRAND_NAME = "BrandName";
  @SerializedName(SERIALIZED_NAME_BRAND_NAME)
  private String brandName;

  public static final String SERIALIZED_NAME_CS_C_IDENTIFICATION = "CSCIdentification";
  @SerializedName(SERIALIZED_NAME_CS_C_IDENTIFICATION)
  private String csCIdentification;

  public static final String SERIALIZED_NAME_CATEGORIES = "Categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private List<String> categories = new ArrayList<>();

  public static final String SERIALIZED_NAME_CATEGORIES_FULL_PATH = "CategoriesFullPath";
  @SerializedName(SERIALIZED_NAME_CATEGORIES_FULL_PATH)
  private List<String> categoriesFullPath = new ArrayList<>();

  public static final String SERIALIZED_NAME_COLLECTIONS = "Collections";
  @SerializedName(SERIALIZED_NAME_COLLECTIONS)
  private List<String> collections = new ArrayList<>();

  public static final String SERIALIZED_NAME_COMMERCIAL_CONDITION_ID = "CommercialConditionId";
  @SerializedName(SERIALIZED_NAME_COMMERCIAL_CONDITION_ID)
  private Integer commercialConditionId;

  public static final String SERIALIZED_NAME_COMPLEMENT_NAME = "ComplementName";
  @SerializedName(SERIALIZED_NAME_COMPLEMENT_NAME)
  private String complementName;

  public static final String SERIALIZED_NAME_DETAIL_URL = "DetailUrl";
  @SerializedName(SERIALIZED_NAME_DETAIL_URL)
  private String detailUrl;

  public static final String SERIALIZED_NAME_DIMENSION = "Dimension";
  @SerializedName(SERIALIZED_NAME_DIMENSION)
  private Dimension dimension;

  public static final String SERIALIZED_NAME_ESTIMATED_DATE_ARRIVAL = "EstimatedDateArrival";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_DATE_ARRIVAL)
  private String estimatedDateArrival;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IMAGE_URL = "ImageUrl";
  @SerializedName(SERIALIZED_NAME_IMAGE_URL)
  private String imageUrl;

  public static final String SERIALIZED_NAME_IMAGES = "Images";
  @SerializedName(SERIALIZED_NAME_IMAGES)
  private List<Image> images = new ArrayList<>();

  public static final String SERIALIZED_NAME_INFORMATION_SOURCE = "InformationSource";
  @SerializedName(SERIALIZED_NAME_INFORMATION_SOURCE)
  private String informationSource;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_DIRECT_CATEGORY_ACTIVE = "IsDirectCategoryActive";
  @SerializedName(SERIALIZED_NAME_IS_DIRECT_CATEGORY_ACTIVE)
  private Boolean isDirectCategoryActive;

  public static final String SERIALIZED_NAME_IS_GIFT_CARD_RECHARGE = "IsGiftCardRecharge";
  @SerializedName(SERIALIZED_NAME_IS_GIFT_CARD_RECHARGE)
  private Boolean isGiftCardRecharge;

  public static final String SERIALIZED_NAME_IS_INVENTORIED = "IsInventoried";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_INVENTORIED)
  private Boolean isInventoried;

  public static final String SERIALIZED_NAME_IS_KIT = "IsKit";
  @SerializedName(SERIALIZED_NAME_IS_KIT)
  private Boolean isKit;

  public static final String SERIALIZED_NAME_IS_PRODUCT_ACTIVE = "IsProductActive";
  @SerializedName(SERIALIZED_NAME_IS_PRODUCT_ACTIVE)
  private Boolean isProductActive;

  public static final String SERIALIZED_NAME_IS_TRANSPORTED = "IsTransported";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_TRANSPORTED)
  private Boolean isTransported;

  public static final String SERIALIZED_NAME_KEY_WORDS = "KeyWords";
  @SerializedName(SERIALIZED_NAME_KEY_WORDS)
  private String keyWords;

  public static final String SERIALIZED_NAME_KIT_ITEMS = "KitItems";
  @SerializedName(SERIALIZED_NAME_KIT_ITEMS)
  private List<String> kitItems = new ArrayList<>();

  public static final String SERIALIZED_NAME_MANUFACTURER_CODE = "ManufacturerCode";
  @SerializedName(SERIALIZED_NAME_MANUFACTURER_CODE)
  private String manufacturerCode;

  public static final String SERIALIZED_NAME_MEASUREMENT_UNIT = "MeasurementUnit";
  @SerializedName(SERIALIZED_NAME_MEASUREMENT_UNIT)
  private String measurementUnit;

  public static final String SERIALIZED_NAME_MODAL_TYPE = "ModalType";
  @SerializedName(SERIALIZED_NAME_MODAL_TYPE)
  private String modalType;

  public static final String SERIALIZED_NAME_NAME_COMPLETE = "NameComplete";
  @SerializedName(SERIALIZED_NAME_NAME_COMPLETE)
  private String nameComplete;

  public static final String SERIALIZED_NAME_POSITIONS_IN_CLUSTERS = "PositionsInClusters";
  @SerializedName(SERIALIZED_NAME_POSITIONS_IN_CLUSTERS)
  private Map<String, Map<String, Integer>> positionsInClusters = new HashMap<>();

  public static final String SERIALIZED_NAME_PRODUCT_CATEGORIES = "ProductCategories";
  @SerializedName(SERIALIZED_NAME_PRODUCT_CATEGORIES)
  private Map<String, Map<String, String>> productCategories = new HashMap<>();

  public static final String SERIALIZED_NAME_PRODUCT_CATEGORY_IDS = "ProductCategoryIds";
  @SerializedName(SERIALIZED_NAME_PRODUCT_CATEGORY_IDS)
  private String productCategoryIds;

  public static final String SERIALIZED_NAME_PRODUCT_CLUSTER_HIGHLIGHTS = "ProductClusterHighlights";
  @SerializedName(SERIALIZED_NAME_PRODUCT_CLUSTER_HIGHLIGHTS)
  private Map<String, Map<String, String>> productClusterHighlights = new HashMap<>();

  public static final String SERIALIZED_NAME_PRODUCT_CLUSTER_NAMES = "ProductClusterNames";
  @SerializedName(SERIALIZED_NAME_PRODUCT_CLUSTER_NAMES)
  private Map<String, Map<String, String>> productClusterNames = new HashMap<>();

  public static final String SERIALIZED_NAME_PRODUCT_CLUSTERS_IDS = "ProductClustersIds";
  @SerializedName(SERIALIZED_NAME_PRODUCT_CLUSTERS_IDS)
  private String productClustersIds;

  public static final String SERIALIZED_NAME_PRODUCT_DESCRIPTION = "ProductDescription";
  @SerializedName(SERIALIZED_NAME_PRODUCT_DESCRIPTION)
  private String productDescription;

  public static final String SERIALIZED_NAME_PRODUCT_FINAL_SCORE = "ProductFinalScore";
  @SerializedName(SERIALIZED_NAME_PRODUCT_FINAL_SCORE)
  private Integer productFinalScore;

  public static final String SERIALIZED_NAME_PRODUCT_GLOBAL_CATEGORY_ID = "ProductGlobalCategoryId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_GLOBAL_CATEGORY_ID)
  private Integer productGlobalCategoryId;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "ProductId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private Integer productId;

  public static final String SERIALIZED_NAME_PRODUCT_IS_VISIBLE = "ProductIsVisible";
  @SerializedName(SERIALIZED_NAME_PRODUCT_IS_VISIBLE)
  private Boolean productIsVisible;

  public static final String SERIALIZED_NAME_PRODUCT_NAME = "ProductName";
  @SerializedName(SERIALIZED_NAME_PRODUCT_NAME)
  private String productName;

  public static final String SERIALIZED_NAME_PRODUCT_REF_ID = "ProductRefId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_REF_ID)
  private String productRefId;

  public static final String SERIALIZED_NAME_PRODUCT_SPECIFICATIONS = "ProductSpecifications";
  @SerializedName(SERIALIZED_NAME_PRODUCT_SPECIFICATIONS)
  private List<ProductSpecification> productSpecifications = new ArrayList<>();

  public static final String SERIALIZED_NAME_REAL_DIMENSION = "RealDimension";
  @SerializedName(SERIALIZED_NAME_REAL_DIMENSION)
  private RealDimension realDimension;

  public static final String SERIALIZED_NAME_RELEASE_DATE = "ReleaseDate";
  @SerializedName(SERIALIZED_NAME_RELEASE_DATE)
  private String releaseDate;

  public static final String SERIALIZED_NAME_REWARD_VALUE = "RewardValue";
  @SerializedName(SERIALIZED_NAME_REWARD_VALUE)
  private BigDecimal rewardValue;

  public static final String SERIALIZED_NAME_SALES_CHANNELS = "SalesChannels";
  @SerializedName(SERIALIZED_NAME_SALES_CHANNELS)
  private List<Integer> salesChannels = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVICES = "Services";
  @SerializedName(SERIALIZED_NAME_SERVICES)
  private List<String> services = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHOW_IF_NOT_AVAILABLE = "ShowIfNotAvailable";
  @SerializedName(SERIALIZED_NAME_SHOW_IF_NOT_AVAILABLE)
  private Boolean showIfNotAvailable;

  public static final String SERIALIZED_NAME_SKU_NAME = "SkuName";
  @SerializedName(SERIALIZED_NAME_SKU_NAME)
  private String skuName;

  public static final String SERIALIZED_NAME_SKU_SELLERS = "SkuSellers";
  @SerializedName(SERIALIZED_NAME_SKU_SELLERS)
  private List<SkuSeller> skuSellers = new ArrayList<>();

  public static final String SERIALIZED_NAME_SKU_SPECIFICATIONS = "SkuSpecifications";
  @SerializedName(SERIALIZED_NAME_SKU_SPECIFICATIONS)
  private List<SkuSpecification> skuSpecifications = new ArrayList<>();

  public static final String SERIALIZED_NAME_TAX_CODE = "TaxCode";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_UNIT_MULTIPLIER = "UnitMultiplier";
  @SerializedName(SERIALIZED_NAME_UNIT_MULTIPLIER)
  private BigDecimal unitMultiplier;

  public GetSKUAltID() {
  }

  public GetSKUAltID alternateIdValues(List<String> alternateIdValues) {
    this.alternateIdValues = alternateIdValues;
    return this;
  }

  public GetSKUAltID addAlternateIdValuesItem(String alternateIdValuesItem) {
    if (this.alternateIdValues == null) {
      this.alternateIdValues = new ArrayList<>();
    }
    this.alternateIdValues.add(alternateIdValuesItem);
    return this;
  }

  /**
   * Array with values of alternative SKU IDs.
   * @return alternateIdValues
   */
  @javax.annotation.Nonnull
  public List<String> getAlternateIdValues() {
    return alternateIdValues;
  }

  public void setAlternateIdValues(List<String> alternateIdValues) {
    this.alternateIdValues = alternateIdValues;
  }


  public GetSKUAltID alternateIds(AlternateIds alternateIds) {
    this.alternateIds = alternateIds;
    return this;
  }

  /**
   * Get alternateIds
   * @return alternateIds
   */
  @javax.annotation.Nonnull
  public AlternateIds getAlternateIds() {
    return alternateIds;
  }

  public void setAlternateIds(AlternateIds alternateIds) {
    this.alternateIds = alternateIds;
  }


  public GetSKUAltID attachments(List<Attachment> attachments) {
    this.attachments = attachments;
    return this;
  }

  public GetSKUAltID addAttachmentsItem(Attachment attachmentsItem) {
    if (this.attachments == null) {
      this.attachments = new ArrayList<>();
    }
    this.attachments.add(attachmentsItem);
    return this;
  }

  /**
   * Array with Attachments ID that are related to the SKU.
   * @return attachments
   */
  @javax.annotation.Nonnull
  public List<Attachment> getAttachments() {
    return attachments;
  }

  public void setAttachments(List<Attachment> attachments) {
    this.attachments = attachments;
  }


  public GetSKUAltID brandId(String brandId) {
    this.brandId = brandId;
    return this;
  }

  /**
   * Brand ID.
   * @return brandId
   */
  @javax.annotation.Nonnull
  public String getBrandId() {
    return brandId;
  }

  public void setBrandId(String brandId) {
    this.brandId = brandId;
  }


  public GetSKUAltID brandName(String brandName) {
    this.brandName = brandName;
    return this;
  }

  /**
   * Brand Name.
   * @return brandName
   */
  @javax.annotation.Nonnull
  public String getBrandName() {
    return brandName;
  }

  public void setBrandName(String brandName) {
    this.brandName = brandName;
  }


  public GetSKUAltID csCIdentification(String csCIdentification) {
    this.csCIdentification = csCIdentification;
    return this;
  }

  /**
   * SKU Seller Identification.
   * @return csCIdentification
   */
  @javax.annotation.Nullable
  public String getCsCIdentification() {
    return csCIdentification;
  }

  public void setCsCIdentification(String csCIdentification) {
    this.csCIdentification = csCIdentification;
  }


  public GetSKUAltID categories(List<String> categories) {
    this.categories = categories;
    return this;
  }

  public GetSKUAltID addCategoriesItem(String categoriesItem) {
    if (this.categories == null) {
      this.categories = new ArrayList<>();
    }
    this.categories.add(categoriesItem);
    return this;
  }

  /**
   * Categories of the related product.
   * @return categories
   */
  @javax.annotation.Nonnull
  public List<String> getCategories() {
    return categories;
  }

  public void setCategories(List<String> categories) {
    this.categories = categories;
  }


  public GetSKUAltID categoriesFullPath(List<String> categoriesFullPath) {
    this.categoriesFullPath = categoriesFullPath;
    return this;
  }

  public GetSKUAltID addCategoriesFullPathItem(String categoriesFullPathItem) {
    if (this.categoriesFullPath == null) {
      this.categoriesFullPath = new ArrayList<>();
    }
    this.categoriesFullPath.add(categoriesFullPathItem);
    return this;
  }

  /**
   * Path of Categories of the related product.
   * @return categoriesFullPath
   */
  @javax.annotation.Nullable
  public List<String> getCategoriesFullPath() {
    return categoriesFullPath;
  }

  public void setCategoriesFullPath(List<String> categoriesFullPath) {
    this.categoriesFullPath = categoriesFullPath;
  }


  public GetSKUAltID collections(List<String> collections) {
    this.collections = collections;
    return this;
  }

  public GetSKUAltID addCollectionsItem(String collectionsItem) {
    if (this.collections == null) {
      this.collections = new ArrayList<>();
    }
    this.collections.add(collectionsItem);
    return this;
  }

  /**
   * Array with Collections IDs that are related to the Product.
   * @return collections
   */
  @javax.annotation.Nonnull
  public List<String> getCollections() {
    return collections;
  }

  public void setCollections(List<String> collections) {
    this.collections = collections;
  }


  public GetSKUAltID commercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
    return this;
  }

  /**
   * SKU Commercial Condition ID.
   * @return commercialConditionId
   */
  @javax.annotation.Nonnull
  public Integer getCommercialConditionId() {
    return commercialConditionId;
  }

  public void setCommercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
  }


  public GetSKUAltID complementName(String complementName) {
    this.complementName = complementName;
    return this;
  }

  /**
   * Product Complement Name.
   * @return complementName
   */
  @javax.annotation.Nullable
  public String getComplementName() {
    return complementName;
  }

  public void setComplementName(String complementName) {
    this.complementName = complementName;
  }


  public GetSKUAltID detailUrl(String detailUrl) {
    this.detailUrl = detailUrl;
    return this;
  }

  /**
   * Product slug.
   * @return detailUrl
   */
  @javax.annotation.Nonnull
  public String getDetailUrl() {
    return detailUrl;
  }

  public void setDetailUrl(String detailUrl) {
    this.detailUrl = detailUrl;
  }


  public GetSKUAltID dimension(Dimension dimension) {
    this.dimension = dimension;
    return this;
  }

  /**
   * Get dimension
   * @return dimension
   */
  @javax.annotation.Nonnull
  public Dimension getDimension() {
    return dimension;
  }

  public void setDimension(Dimension dimension) {
    this.dimension = dimension;
  }


  public GetSKUAltID estimatedDateArrival(String estimatedDateArrival) {
    this.estimatedDateArrival = estimatedDateArrival;
    return this;
  }

  /**
   * SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date.
   * @return estimatedDateArrival
   */
  @javax.annotation.Nullable
  public String getEstimatedDateArrival() {
    return estimatedDateArrival;
  }

  public void setEstimatedDateArrival(String estimatedDateArrival) {
    this.estimatedDateArrival = estimatedDateArrival;
  }


  public GetSKUAltID id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * SKU ID.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public GetSKUAltID imageUrl(String imageUrl) {
    this.imageUrl = imageUrl;
    return this;
  }

  /**
   * SKU image URL.
   * @return imageUrl
   */
  @javax.annotation.Nonnull
  public String getImageUrl() {
    return imageUrl;
  }

  public void setImageUrl(String imageUrl) {
    this.imageUrl = imageUrl;
  }


  public GetSKUAltID images(List<Image> images) {
    this.images = images;
    return this;
  }

  public GetSKUAltID addImagesItem(Image imagesItem) {
    if (this.images == null) {
      this.images = new ArrayList<>();
    }
    this.images.add(imagesItem);
    return this;
  }

  /**
   * Array of objects with SKU image details.
   * @return images
   */
  @javax.annotation.Nonnull
  public List<Image> getImages() {
    return images;
  }

  public void setImages(List<Image> images) {
    this.images = images;
  }


  public GetSKUAltID informationSource(String informationSource) {
    this.informationSource = informationSource;
    return this;
  }

  /**
   * Information Source.
   * @return informationSource
   */
  @javax.annotation.Nullable
  public String getInformationSource() {
    return informationSource;
  }

  public void setInformationSource(String informationSource) {
    this.informationSource = informationSource;
  }


  public GetSKUAltID isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Defines if the SKU is active or not.
   * @return isActive
   */
  @javax.annotation.Nonnull
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public GetSKUAltID isDirectCategoryActive(Boolean isDirectCategoryActive) {
    this.isDirectCategoryActive = isDirectCategoryActive;
    return this;
  }

  /**
   * Indicates if the direct Product Category is active or not.
   * @return isDirectCategoryActive
   */
  @javax.annotation.Nullable
  public Boolean getIsDirectCategoryActive() {
    return isDirectCategoryActive;
  }

  public void setIsDirectCategoryActive(Boolean isDirectCategoryActive) {
    this.isDirectCategoryActive = isDirectCategoryActive;
  }


  public GetSKUAltID isGiftCardRecharge(Boolean isGiftCardRecharge) {
    this.isGiftCardRecharge = isGiftCardRecharge;
    return this;
  }

  /**
   * Defines if the purchase of the SKU will generate reward value for the customer.
   * @return isGiftCardRecharge
   */
  @javax.annotation.Nonnull
  public Boolean getIsGiftCardRecharge() {
    return isGiftCardRecharge;
  }

  public void setIsGiftCardRecharge(Boolean isGiftCardRecharge) {
    this.isGiftCardRecharge = isGiftCardRecharge;
  }


  @Deprecated
  public GetSKUAltID isInventoried(Boolean isInventoried) {
    this.isInventoried = isInventoried;
    return this;
  }

  /**
   * Get isInventoried
   * @return isInventoried
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Boolean getIsInventoried() {
    return isInventoried;
  }

  @Deprecated
  public void setIsInventoried(Boolean isInventoried) {
    this.isInventoried = isInventoried;
  }


  public GetSKUAltID isKit(Boolean isKit) {
    this.isKit = isKit;
    return this;
  }

  /**
   * Defines if the SKU is part of a bundle.
   * @return isKit
   */
  @javax.annotation.Nonnull
  public Boolean getIsKit() {
    return isKit;
  }

  public void setIsKit(Boolean isKit) {
    this.isKit = isKit;
  }


  public GetSKUAltID isProductActive(Boolean isProductActive) {
    this.isProductActive = isProductActive;
    return this;
  }

  /**
   * Defines if the product is active or not.
   * @return isProductActive
   */
  @javax.annotation.Nullable
  public Boolean getIsProductActive() {
    return isProductActive;
  }

  public void setIsProductActive(Boolean isProductActive) {
    this.isProductActive = isProductActive;
  }


  @Deprecated
  public GetSKUAltID isTransported(Boolean isTransported) {
    this.isTransported = isTransported;
    return this;
  }

  /**
   * Get isTransported
   * @return isTransported
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nonnull
  public Boolean getIsTransported() {
    return isTransported;
  }

  @Deprecated
  public void setIsTransported(Boolean isTransported) {
    this.isTransported = isTransported;
  }


  public GetSKUAltID keyWords(String keyWords) {
    this.keyWords = keyWords;
    return this;
  }

  /**
   * Keywords related to the product.
   * @return keyWords
   */
  @javax.annotation.Nullable
  public String getKeyWords() {
    return keyWords;
  }

  public void setKeyWords(String keyWords) {
    this.keyWords = keyWords;
  }


  public GetSKUAltID kitItems(List<String> kitItems) {
    this.kitItems = kitItems;
    return this;
  }

  public GetSKUAltID addKitItemsItem(String kitItemsItem) {
    if (this.kitItems == null) {
      this.kitItems = new ArrayList<>();
    }
    this.kitItems.add(kitItemsItem);
    return this;
  }

  /**
   * Array with SKU IDs of bundle components.
   * @return kitItems
   */
  @javax.annotation.Nonnull
  public List<String> getKitItems() {
    return kitItems;
  }

  public void setKitItems(List<String> kitItems) {
    this.kitItems = kitItems;
  }


  public GetSKUAltID manufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
    return this;
  }

  /**
   * Product Supplier ID.
   * @return manufacturerCode
   */
  @javax.annotation.Nonnull
  public String getManufacturerCode() {
    return manufacturerCode;
  }

  public void setManufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
  }


  public GetSKUAltID measurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
    return this;
  }

  /**
   * Measurement unit.
   * @return measurementUnit
   */
  @javax.annotation.Nonnull
  public String getMeasurementUnit() {
    return measurementUnit;
  }

  public void setMeasurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
  }


  public GetSKUAltID modalType(String modalType) {
    this.modalType = modalType;
    return this;
  }

  /**
   * Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy).
   * @return modalType
   */
  @javax.annotation.Nullable
  public String getModalType() {
    return modalType;
  }

  public void setModalType(String modalType) {
    this.modalType = modalType;
  }


  public GetSKUAltID nameComplete(String nameComplete) {
    this.nameComplete = nameComplete;
    return this;
  }

  /**
   * Product Name and SKU Name combined.
   * @return nameComplete
   */
  @javax.annotation.Nonnull
  public String getNameComplete() {
    return nameComplete;
  }

  public void setNameComplete(String nameComplete) {
    this.nameComplete = nameComplete;
  }


  public GetSKUAltID positionsInClusters(Map<String, Map<String, Integer>> positionsInClusters) {
    this.positionsInClusters = positionsInClusters;
    return this;
  }

  public GetSKUAltID putPositionsInClustersItem(String key, Map<String, Integer> positionsInClustersItem) {
    if (this.positionsInClusters == null) {
      this.positionsInClusters = new HashMap<>();
    }
    this.positionsInClusters.put(key, positionsInClustersItem);
    return this;
  }

  /**
   * Product Clusters position in each Cluster. Structure: \&quot;{Product Cluster ID}\&quot;: {Position}.  &#x60;{Product Cluster ID}&#x60; is a string, while &#x60;{Position}&#x60; is an integer.
   * @return positionsInClusters
   */
  @javax.annotation.Nullable
  public Map<String, Map<String, Integer>> getPositionsInClusters() {
    return positionsInClusters;
  }

  public void setPositionsInClusters(Map<String, Map<String, Integer>> positionsInClusters) {
    this.positionsInClusters = positionsInClusters;
  }


  public GetSKUAltID productCategories(Map<String, Map<String, String>> productCategories) {
    this.productCategories = productCategories;
    return this;
  }

  public GetSKUAltID putProductCategoriesItem(String key, Map<String, String> productCategoriesItem) {
    if (this.productCategories == null) {
      this.productCategories = new HashMap<>();
    }
    this.productCategories.put(key, productCategoriesItem);
    return this;
  }

  /**
   * Object containing product categories. Structure: \&quot;{CategoryID}\&quot;: \&quot;{CategoryName}\&quot;. Both the key and the value are strings.
   * @return productCategories
   */
  @javax.annotation.Nonnull
  public Map<String, Map<String, String>> getProductCategories() {
    return productCategories;
  }

  public void setProductCategories(Map<String, Map<String, String>> productCategories) {
    this.productCategories = productCategories;
  }


  public GetSKUAltID productCategoryIds(String productCategoryIds) {
    this.productCategoryIds = productCategoryIds;
    return this;
  }

  /**
   * Category path composed by category IDs separated by &#x60;/&#x60;.
   * @return productCategoryIds
   */
  @javax.annotation.Nonnull
  public String getProductCategoryIds() {
    return productCategoryIds;
  }

  public void setProductCategoryIds(String productCategoryIds) {
    this.productCategoryIds = productCategoryIds;
  }


  public GetSKUAltID productClusterHighlights(Map<String, Map<String, String>> productClusterHighlights) {
    this.productClusterHighlights = productClusterHighlights;
    return this;
  }

  public GetSKUAltID putProductClusterHighlightsItem(String key, Map<String, String> productClusterHighlightsItem) {
    if (this.productClusterHighlights == null) {
      this.productClusterHighlights = new HashMap<>();
    }
    this.productClusterHighlights.put(key, productClusterHighlightsItem);
    return this;
  }

  /**
   * Product Clusters Highlights. Structure: \&quot;{Product Cluster ID}\&quot;: \&quot;{Product Cluster Name}\&quot;. Both the key and the value are strings.
   * @return productClusterHighlights
   */
  @javax.annotation.Nullable
  public Map<String, Map<String, String>> getProductClusterHighlights() {
    return productClusterHighlights;
  }

  public void setProductClusterHighlights(Map<String, Map<String, String>> productClusterHighlights) {
    this.productClusterHighlights = productClusterHighlights;
  }


  public GetSKUAltID productClusterNames(Map<String, Map<String, String>> productClusterNames) {
    this.productClusterNames = productClusterNames;
    return this;
  }

  public GetSKUAltID putProductClusterNamesItem(String key, Map<String, String> productClusterNamesItem) {
    if (this.productClusterNames == null) {
      this.productClusterNames = new HashMap<>();
    }
    this.productClusterNames.put(key, productClusterNamesItem);
    return this;
  }

  /**
   * Product Clusters Names. Structure: \&quot;{Product Cluster ID}\&quot;: \&quot;{Product Cluster Name}\&quot;. Both the key and the value are strings.
   * @return productClusterNames
   */
  @javax.annotation.Nullable
  public Map<String, Map<String, String>> getProductClusterNames() {
    return productClusterNames;
  }

  public void setProductClusterNames(Map<String, Map<String, String>> productClusterNames) {
    this.productClusterNames = productClusterNames;
  }


  public GetSKUAltID productClustersIds(String productClustersIds) {
    this.productClustersIds = productClustersIds;
    return this;
  }

  /**
   * Product Cluster IDs separated by comma (&#x60;,&#x60;).
   * @return productClustersIds
   */
  @javax.annotation.Nonnull
  public String getProductClustersIds() {
    return productClustersIds;
  }

  public void setProductClustersIds(String productClustersIds) {
    this.productClustersIds = productClustersIds;
  }


  public GetSKUAltID productDescription(String productDescription) {
    this.productDescription = productDescription;
    return this;
  }

  /**
   * Product Description. HTML is allowed.
   * @return productDescription
   */
  @javax.annotation.Nonnull
  public String getProductDescription() {
    return productDescription;
  }

  public void setProductDescription(String productDescription) {
    this.productDescription = productDescription;
  }


  public GetSKUAltID productFinalScore(Integer productFinalScore) {
    this.productFinalScore = productFinalScore;
    return this;
  }

  /**
   * Product Final Score.
   * @return productFinalScore
   */
  @javax.annotation.Nullable
  public Integer getProductFinalScore() {
    return productFinalScore;
  }

  public void setProductFinalScore(Integer productFinalScore) {
    this.productFinalScore = productFinalScore;
  }


  public GetSKUAltID productGlobalCategoryId(Integer productGlobalCategoryId) {
    this.productGlobalCategoryId = productGlobalCategoryId;
    return this;
  }

  /**
   * Product Global Category ID.
   * @return productGlobalCategoryId
   */
  @javax.annotation.Nullable
  public Integer getProductGlobalCategoryId() {
    return productGlobalCategoryId;
  }

  public void setProductGlobalCategoryId(Integer productGlobalCategoryId) {
    this.productGlobalCategoryId = productGlobalCategoryId;
  }


  public GetSKUAltID productId(Integer productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Product ID.
   * @return productId
   */
  @javax.annotation.Nonnull
  public Integer getProductId() {
    return productId;
  }

  public void setProductId(Integer productId) {
    this.productId = productId;
  }


  public GetSKUAltID productIsVisible(Boolean productIsVisible) {
    this.productIsVisible = productIsVisible;
    return this;
  }

  /**
   * Defines if the product is visible or not.
   * @return productIsVisible
   */
  @javax.annotation.Nullable
  public Boolean getProductIsVisible() {
    return productIsVisible;
  }

  public void setProductIsVisible(Boolean productIsVisible) {
    this.productIsVisible = productIsVisible;
  }


  public GetSKUAltID productName(String productName) {
    this.productName = productName;
    return this;
  }

  /**
   * Product Name.
   * @return productName
   */
  @javax.annotation.Nonnull
  public String getProductName() {
    return productName;
  }

  public void setProductName(String productName) {
    this.productName = productName;
  }


  public GetSKUAltID productRefId(String productRefId) {
    this.productRefId = productRefId;
    return this;
  }

  /**
   * Product Reference ID.
   * @return productRefId
   */
  @javax.annotation.Nullable
  public String getProductRefId() {
    return productRefId;
  }

  public void setProductRefId(String productRefId) {
    this.productRefId = productRefId;
  }


  public GetSKUAltID productSpecifications(List<ProductSpecification> productSpecifications) {
    this.productSpecifications = productSpecifications;
    return this;
  }

  public GetSKUAltID addProductSpecificationsItem(ProductSpecification productSpecificationsItem) {
    if (this.productSpecifications == null) {
      this.productSpecifications = new ArrayList<>();
    }
    this.productSpecifications.add(productSpecificationsItem);
    return this;
  }

  /**
   * Array with related Product Specifications.
   * @return productSpecifications
   */
  @javax.annotation.Nonnull
  public List<ProductSpecification> getProductSpecifications() {
    return productSpecifications;
  }

  public void setProductSpecifications(List<ProductSpecification> productSpecifications) {
    this.productSpecifications = productSpecifications;
  }


  public GetSKUAltID realDimension(RealDimension realDimension) {
    this.realDimension = realDimension;
    return this;
  }

  /**
   * Get realDimension
   * @return realDimension
   */
  @javax.annotation.Nonnull
  public RealDimension getRealDimension() {
    return realDimension;
  }

  public void setRealDimension(RealDimension realDimension) {
    this.realDimension = realDimension;
  }


  public GetSKUAltID releaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
    return this;
  }

  /**
   * Release date of the product.
   * @return releaseDate
   */
  @javax.annotation.Nullable
  public String getReleaseDate() {
    return releaseDate;
  }

  public void setReleaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
  }


  public GetSKUAltID rewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
    return this;
  }

  /**
   * Reward value related to the SKU.
   * @return rewardValue
   */
  @javax.annotation.Nonnull
  public BigDecimal getRewardValue() {
    return rewardValue;
  }

  public void setRewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
  }


  public GetSKUAltID salesChannels(List<Integer> salesChannels) {
    this.salesChannels = salesChannels;
    return this;
  }

  public GetSKUAltID addSalesChannelsItem(Integer salesChannelsItem) {
    if (this.salesChannels == null) {
      this.salesChannels = new ArrayList<>();
    }
    this.salesChannels.add(salesChannelsItem);
    return this;
  }

  /**
   * Array of trade policy IDs.
   * @return salesChannels
   */
  @javax.annotation.Nonnull
  public List<Integer> getSalesChannels() {
    return salesChannels;
  }

  public void setSalesChannels(List<Integer> salesChannels) {
    this.salesChannels = salesChannels;
  }


  public GetSKUAltID services(List<String> services) {
    this.services = services;
    return this;
  }

  public GetSKUAltID addServicesItem(String servicesItem) {
    if (this.services == null) {
      this.services = new ArrayList<>();
    }
    this.services.add(servicesItem);
    return this;
  }

  /**
   * Array with Service IDs that are related to the SKU.
   * @return services
   */
  @javax.annotation.Nonnull
  public List<String> getServices() {
    return services;
  }

  public void setServices(List<String> services) {
    this.services = services;
  }


  public GetSKUAltID showIfNotAvailable(Boolean showIfNotAvailable) {
    this.showIfNotAvailable = showIfNotAvailable;
    return this;
  }

  /**
   * Defines if the product will be shown if it is not available.
   * @return showIfNotAvailable
   */
  @javax.annotation.Nullable
  public Boolean getShowIfNotAvailable() {
    return showIfNotAvailable;
  }

  public void setShowIfNotAvailable(Boolean showIfNotAvailable) {
    this.showIfNotAvailable = showIfNotAvailable;
  }


  public GetSKUAltID skuName(String skuName) {
    this.skuName = skuName;
    return this;
  }

  /**
   * SKU Name.
   * @return skuName
   */
  @javax.annotation.Nonnull
  public String getSkuName() {
    return skuName;
  }

  public void setSkuName(String skuName) {
    this.skuName = skuName;
  }


  public GetSKUAltID skuSellers(List<SkuSeller> skuSellers) {
    this.skuSellers = skuSellers;
    return this;
  }

  public GetSKUAltID addSkuSellersItem(SkuSeller skuSellersItem) {
    if (this.skuSellers == null) {
      this.skuSellers = new ArrayList<>();
    }
    this.skuSellers.add(skuSellersItem);
    return this;
  }

  /**
   * Array with related Sellers data.
   * @return skuSellers
   */
  @javax.annotation.Nonnull
  public List<SkuSeller> getSkuSellers() {
    return skuSellers;
  }

  public void setSkuSellers(List<SkuSeller> skuSellers) {
    this.skuSellers = skuSellers;
  }


  public GetSKUAltID skuSpecifications(List<SkuSpecification> skuSpecifications) {
    this.skuSpecifications = skuSpecifications;
    return this;
  }

  public GetSKUAltID addSkuSpecificationsItem(SkuSpecification skuSpecificationsItem) {
    if (this.skuSpecifications == null) {
      this.skuSpecifications = new ArrayList<>();
    }
    this.skuSpecifications.add(skuSpecificationsItem);
    return this;
  }

  /**
   * Array with related SKU Specifications.
   * @return skuSpecifications
   */
  @javax.annotation.Nonnull
  public List<SkuSpecification> getSkuSpecifications() {
    return skuSpecifications;
  }

  public void setSkuSpecifications(List<SkuSpecification> skuSpecifications) {
    this.skuSpecifications = skuSpecifications;
  }


  public GetSKUAltID taxCode(String taxCode) {
    this.taxCode = taxCode;
    return this;
  }

  /**
   * SKU Tax Code.
   * @return taxCode
   */
  @javax.annotation.Nullable
  public String getTaxCode() {
    return taxCode;
  }

  public void setTaxCode(String taxCode) {
    this.taxCode = taxCode;
  }


  public GetSKUAltID unitMultiplier(BigDecimal unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
    return this;
  }

  /**
   * This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward.
   * @return unitMultiplier
   */
  @javax.annotation.Nonnull
  public BigDecimal getUnitMultiplier() {
    return unitMultiplier;
  }

  public void setUnitMultiplier(BigDecimal unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetSKUAltID getSKUAltID = (GetSKUAltID) o;
    return Objects.equals(this.alternateIdValues, getSKUAltID.alternateIdValues) &&
        Objects.equals(this.alternateIds, getSKUAltID.alternateIds) &&
        Objects.equals(this.attachments, getSKUAltID.attachments) &&
        Objects.equals(this.brandId, getSKUAltID.brandId) &&
        Objects.equals(this.brandName, getSKUAltID.brandName) &&
        Objects.equals(this.csCIdentification, getSKUAltID.csCIdentification) &&
        Objects.equals(this.categories, getSKUAltID.categories) &&
        Objects.equals(this.categoriesFullPath, getSKUAltID.categoriesFullPath) &&
        Objects.equals(this.collections, getSKUAltID.collections) &&
        Objects.equals(this.commercialConditionId, getSKUAltID.commercialConditionId) &&
        Objects.equals(this.complementName, getSKUAltID.complementName) &&
        Objects.equals(this.detailUrl, getSKUAltID.detailUrl) &&
        Objects.equals(this.dimension, getSKUAltID.dimension) &&
        Objects.equals(this.estimatedDateArrival, getSKUAltID.estimatedDateArrival) &&
        Objects.equals(this.id, getSKUAltID.id) &&
        Objects.equals(this.imageUrl, getSKUAltID.imageUrl) &&
        Objects.equals(this.images, getSKUAltID.images) &&
        Objects.equals(this.informationSource, getSKUAltID.informationSource) &&
        Objects.equals(this.isActive, getSKUAltID.isActive) &&
        Objects.equals(this.isDirectCategoryActive, getSKUAltID.isDirectCategoryActive) &&
        Objects.equals(this.isGiftCardRecharge, getSKUAltID.isGiftCardRecharge) &&
        Objects.equals(this.isInventoried, getSKUAltID.isInventoried) &&
        Objects.equals(this.isKit, getSKUAltID.isKit) &&
        Objects.equals(this.isProductActive, getSKUAltID.isProductActive) &&
        Objects.equals(this.isTransported, getSKUAltID.isTransported) &&
        Objects.equals(this.keyWords, getSKUAltID.keyWords) &&
        Objects.equals(this.kitItems, getSKUAltID.kitItems) &&
        Objects.equals(this.manufacturerCode, getSKUAltID.manufacturerCode) &&
        Objects.equals(this.measurementUnit, getSKUAltID.measurementUnit) &&
        Objects.equals(this.modalType, getSKUAltID.modalType) &&
        Objects.equals(this.nameComplete, getSKUAltID.nameComplete) &&
        Objects.equals(this.positionsInClusters, getSKUAltID.positionsInClusters) &&
        Objects.equals(this.productCategories, getSKUAltID.productCategories) &&
        Objects.equals(this.productCategoryIds, getSKUAltID.productCategoryIds) &&
        Objects.equals(this.productClusterHighlights, getSKUAltID.productClusterHighlights) &&
        Objects.equals(this.productClusterNames, getSKUAltID.productClusterNames) &&
        Objects.equals(this.productClustersIds, getSKUAltID.productClustersIds) &&
        Objects.equals(this.productDescription, getSKUAltID.productDescription) &&
        Objects.equals(this.productFinalScore, getSKUAltID.productFinalScore) &&
        Objects.equals(this.productGlobalCategoryId, getSKUAltID.productGlobalCategoryId) &&
        Objects.equals(this.productId, getSKUAltID.productId) &&
        Objects.equals(this.productIsVisible, getSKUAltID.productIsVisible) &&
        Objects.equals(this.productName, getSKUAltID.productName) &&
        Objects.equals(this.productRefId, getSKUAltID.productRefId) &&
        Objects.equals(this.productSpecifications, getSKUAltID.productSpecifications) &&
        Objects.equals(this.realDimension, getSKUAltID.realDimension) &&
        Objects.equals(this.releaseDate, getSKUAltID.releaseDate) &&
        Objects.equals(this.rewardValue, getSKUAltID.rewardValue) &&
        Objects.equals(this.salesChannels, getSKUAltID.salesChannels) &&
        Objects.equals(this.services, getSKUAltID.services) &&
        Objects.equals(this.showIfNotAvailable, getSKUAltID.showIfNotAvailable) &&
        Objects.equals(this.skuName, getSKUAltID.skuName) &&
        Objects.equals(this.skuSellers, getSKUAltID.skuSellers) &&
        Objects.equals(this.skuSpecifications, getSKUAltID.skuSpecifications) &&
        Objects.equals(this.taxCode, getSKUAltID.taxCode) &&
        Objects.equals(this.unitMultiplier, getSKUAltID.unitMultiplier);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(alternateIdValues, alternateIds, attachments, brandId, brandName, csCIdentification, categories, categoriesFullPath, collections, commercialConditionId, complementName, detailUrl, dimension, estimatedDateArrival, id, imageUrl, images, informationSource, isActive, isDirectCategoryActive, isGiftCardRecharge, isInventoried, isKit, isProductActive, isTransported, keyWords, kitItems, manufacturerCode, measurementUnit, modalType, nameComplete, positionsInClusters, productCategories, productCategoryIds, productClusterHighlights, productClusterNames, productClustersIds, productDescription, productFinalScore, productGlobalCategoryId, productId, productIsVisible, productName, productRefId, productSpecifications, realDimension, releaseDate, rewardValue, salesChannels, services, showIfNotAvailable, skuName, skuSellers, skuSpecifications, taxCode, unitMultiplier);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetSKUAltID {\n");
    sb.append("    alternateIdValues: ").append(toIndentedString(alternateIdValues)).append("\n");
    sb.append("    alternateIds: ").append(toIndentedString(alternateIds)).append("\n");
    sb.append("    attachments: ").append(toIndentedString(attachments)).append("\n");
    sb.append("    brandId: ").append(toIndentedString(brandId)).append("\n");
    sb.append("    brandName: ").append(toIndentedString(brandName)).append("\n");
    sb.append("    csCIdentification: ").append(toIndentedString(csCIdentification)).append("\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
    sb.append("    categoriesFullPath: ").append(toIndentedString(categoriesFullPath)).append("\n");
    sb.append("    collections: ").append(toIndentedString(collections)).append("\n");
    sb.append("    commercialConditionId: ").append(toIndentedString(commercialConditionId)).append("\n");
    sb.append("    complementName: ").append(toIndentedString(complementName)).append("\n");
    sb.append("    detailUrl: ").append(toIndentedString(detailUrl)).append("\n");
    sb.append("    dimension: ").append(toIndentedString(dimension)).append("\n");
    sb.append("    estimatedDateArrival: ").append(toIndentedString(estimatedDateArrival)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    imageUrl: ").append(toIndentedString(imageUrl)).append("\n");
    sb.append("    images: ").append(toIndentedString(images)).append("\n");
    sb.append("    informationSource: ").append(toIndentedString(informationSource)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isDirectCategoryActive: ").append(toIndentedString(isDirectCategoryActive)).append("\n");
    sb.append("    isGiftCardRecharge: ").append(toIndentedString(isGiftCardRecharge)).append("\n");
    sb.append("    isInventoried: ").append(toIndentedString(isInventoried)).append("\n");
    sb.append("    isKit: ").append(toIndentedString(isKit)).append("\n");
    sb.append("    isProductActive: ").append(toIndentedString(isProductActive)).append("\n");
    sb.append("    isTransported: ").append(toIndentedString(isTransported)).append("\n");
    sb.append("    keyWords: ").append(toIndentedString(keyWords)).append("\n");
    sb.append("    kitItems: ").append(toIndentedString(kitItems)).append("\n");
    sb.append("    manufacturerCode: ").append(toIndentedString(manufacturerCode)).append("\n");
    sb.append("    measurementUnit: ").append(toIndentedString(measurementUnit)).append("\n");
    sb.append("    modalType: ").append(toIndentedString(modalType)).append("\n");
    sb.append("    nameComplete: ").append(toIndentedString(nameComplete)).append("\n");
    sb.append("    positionsInClusters: ").append(toIndentedString(positionsInClusters)).append("\n");
    sb.append("    productCategories: ").append(toIndentedString(productCategories)).append("\n");
    sb.append("    productCategoryIds: ").append(toIndentedString(productCategoryIds)).append("\n");
    sb.append("    productClusterHighlights: ").append(toIndentedString(productClusterHighlights)).append("\n");
    sb.append("    productClusterNames: ").append(toIndentedString(productClusterNames)).append("\n");
    sb.append("    productClustersIds: ").append(toIndentedString(productClustersIds)).append("\n");
    sb.append("    productDescription: ").append(toIndentedString(productDescription)).append("\n");
    sb.append("    productFinalScore: ").append(toIndentedString(productFinalScore)).append("\n");
    sb.append("    productGlobalCategoryId: ").append(toIndentedString(productGlobalCategoryId)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    productIsVisible: ").append(toIndentedString(productIsVisible)).append("\n");
    sb.append("    productName: ").append(toIndentedString(productName)).append("\n");
    sb.append("    productRefId: ").append(toIndentedString(productRefId)).append("\n");
    sb.append("    productSpecifications: ").append(toIndentedString(productSpecifications)).append("\n");
    sb.append("    realDimension: ").append(toIndentedString(realDimension)).append("\n");
    sb.append("    releaseDate: ").append(toIndentedString(releaseDate)).append("\n");
    sb.append("    rewardValue: ").append(toIndentedString(rewardValue)).append("\n");
    sb.append("    salesChannels: ").append(toIndentedString(salesChannels)).append("\n");
    sb.append("    services: ").append(toIndentedString(services)).append("\n");
    sb.append("    showIfNotAvailable: ").append(toIndentedString(showIfNotAvailable)).append("\n");
    sb.append("    skuName: ").append(toIndentedString(skuName)).append("\n");
    sb.append("    skuSellers: ").append(toIndentedString(skuSellers)).append("\n");
    sb.append("    skuSpecifications: ").append(toIndentedString(skuSpecifications)).append("\n");
    sb.append("    taxCode: ").append(toIndentedString(taxCode)).append("\n");
    sb.append("    unitMultiplier: ").append(toIndentedString(unitMultiplier)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("AlternateIdValues");
    openapiFields.add("AlternateIds");
    openapiFields.add("Attachments");
    openapiFields.add("BrandId");
    openapiFields.add("BrandName");
    openapiFields.add("CSCIdentification");
    openapiFields.add("Categories");
    openapiFields.add("CategoriesFullPath");
    openapiFields.add("Collections");
    openapiFields.add("CommercialConditionId");
    openapiFields.add("ComplementName");
    openapiFields.add("DetailUrl");
    openapiFields.add("Dimension");
    openapiFields.add("EstimatedDateArrival");
    openapiFields.add("Id");
    openapiFields.add("ImageUrl");
    openapiFields.add("Images");
    openapiFields.add("InformationSource");
    openapiFields.add("IsActive");
    openapiFields.add("IsDirectCategoryActive");
    openapiFields.add("IsGiftCardRecharge");
    openapiFields.add("IsInventoried");
    openapiFields.add("IsKit");
    openapiFields.add("IsProductActive");
    openapiFields.add("IsTransported");
    openapiFields.add("KeyWords");
    openapiFields.add("KitItems");
    openapiFields.add("ManufacturerCode");
    openapiFields.add("MeasurementUnit");
    openapiFields.add("ModalType");
    openapiFields.add("NameComplete");
    openapiFields.add("PositionsInClusters");
    openapiFields.add("ProductCategories");
    openapiFields.add("ProductCategoryIds");
    openapiFields.add("ProductClusterHighlights");
    openapiFields.add("ProductClusterNames");
    openapiFields.add("ProductClustersIds");
    openapiFields.add("ProductDescription");
    openapiFields.add("ProductFinalScore");
    openapiFields.add("ProductGlobalCategoryId");
    openapiFields.add("ProductId");
    openapiFields.add("ProductIsVisible");
    openapiFields.add("ProductName");
    openapiFields.add("ProductRefId");
    openapiFields.add("ProductSpecifications");
    openapiFields.add("RealDimension");
    openapiFields.add("ReleaseDate");
    openapiFields.add("RewardValue");
    openapiFields.add("SalesChannels");
    openapiFields.add("Services");
    openapiFields.add("ShowIfNotAvailable");
    openapiFields.add("SkuName");
    openapiFields.add("SkuSellers");
    openapiFields.add("SkuSpecifications");
    openapiFields.add("TaxCode");
    openapiFields.add("UnitMultiplier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("AlternateIdValues");
    openapiRequiredFields.add("AlternateIds");
    openapiRequiredFields.add("Attachments");
    openapiRequiredFields.add("BrandId");
    openapiRequiredFields.add("BrandName");
    openapiRequiredFields.add("CSCIdentification");
    openapiRequiredFields.add("Categories");
    openapiRequiredFields.add("Collections");
    openapiRequiredFields.add("CommercialConditionId");
    openapiRequiredFields.add("DetailUrl");
    openapiRequiredFields.add("Dimension");
    openapiRequiredFields.add("EstimatedDateArrival");
    openapiRequiredFields.add("Id");
    openapiRequiredFields.add("ImageUrl");
    openapiRequiredFields.add("Images");
    openapiRequiredFields.add("InformationSource");
    openapiRequiredFields.add("IsActive");
    openapiRequiredFields.add("IsGiftCardRecharge");
    openapiRequiredFields.add("IsInventoried");
    openapiRequiredFields.add("IsKit");
    openapiRequiredFields.add("IsTransported");
    openapiRequiredFields.add("KitItems");
    openapiRequiredFields.add("ManufacturerCode");
    openapiRequiredFields.add("MeasurementUnit");
    openapiRequiredFields.add("ModalType");
    openapiRequiredFields.add("NameComplete");
    openapiRequiredFields.add("ProductCategories");
    openapiRequiredFields.add("ProductCategoryIds");
    openapiRequiredFields.add("ProductClustersIds");
    openapiRequiredFields.add("ProductDescription");
    openapiRequiredFields.add("ProductGlobalCategoryId");
    openapiRequiredFields.add("ProductId");
    openapiRequiredFields.add("ProductName");
    openapiRequiredFields.add("ProductSpecifications");
    openapiRequiredFields.add("RealDimension");
    openapiRequiredFields.add("RewardValue");
    openapiRequiredFields.add("SalesChannels");
    openapiRequiredFields.add("Services");
    openapiRequiredFields.add("SkuName");
    openapiRequiredFields.add("SkuSellers");
    openapiRequiredFields.add("SkuSpecifications");
    openapiRequiredFields.add("UnitMultiplier");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetSKUAltID
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetSKUAltID.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetSKUAltID is not found in the empty JSON string", GetSKUAltID.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetSKUAltID.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetSKUAltID` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetSKUAltID.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("AlternateIdValues") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("AlternateIdValues").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `AlternateIdValues` to be an array in the JSON string but got `%s`", jsonObj.get("AlternateIdValues").toString()));
      }
      // validate the required field `AlternateIds`
      AlternateIds.validateJsonElement(jsonObj.get("AlternateIds"));
      // ensure the json data is an array
      if (!jsonObj.get("Attachments").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Attachments` to be an array in the JSON string but got `%s`", jsonObj.get("Attachments").toString()));
      }

      JsonArray jsonArrayattachments = jsonObj.getAsJsonArray("Attachments");
      // validate the required field `Attachments` (array)
      for (int i = 0; i < jsonArrayattachments.size(); i++) {
        Attachment.validateJsonElement(jsonArrayattachments.get(i));
      };
      if (!jsonObj.get("BrandId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BrandId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BrandId").toString()));
      }
      if (!jsonObj.get("BrandName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BrandName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BrandName").toString()));
      }
      if ((jsonObj.get("CSCIdentification") != null && !jsonObj.get("CSCIdentification").isJsonNull()) && !jsonObj.get("CSCIdentification").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CSCIdentification` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CSCIdentification").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("Categories") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("Categories").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Categories` to be an array in the JSON string but got `%s`", jsonObj.get("Categories").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("CategoriesFullPath") != null && !jsonObj.get("CategoriesFullPath").isJsonNull() && !jsonObj.get("CategoriesFullPath").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `CategoriesFullPath` to be an array in the JSON string but got `%s`", jsonObj.get("CategoriesFullPath").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("Collections") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("Collections").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Collections` to be an array in the JSON string but got `%s`", jsonObj.get("Collections").toString()));
      }
      if ((jsonObj.get("ComplementName") != null && !jsonObj.get("ComplementName").isJsonNull()) && !jsonObj.get("ComplementName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ComplementName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ComplementName").toString()));
      }
      if (!jsonObj.get("DetailUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DetailUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DetailUrl").toString()));
      }
      // validate the required field `Dimension`
      Dimension.validateJsonElement(jsonObj.get("Dimension"));
      if ((jsonObj.get("EstimatedDateArrival") != null && !jsonObj.get("EstimatedDateArrival").isJsonNull()) && !jsonObj.get("EstimatedDateArrival").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `EstimatedDateArrival` to be a primitive type in the JSON string but got `%s`", jsonObj.get("EstimatedDateArrival").toString()));
      }
      if (!jsonObj.get("ImageUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ImageUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ImageUrl").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("Images").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Images` to be an array in the JSON string but got `%s`", jsonObj.get("Images").toString()));
      }

      JsonArray jsonArrayimages = jsonObj.getAsJsonArray("Images");
      // validate the required field `Images` (array)
      for (int i = 0; i < jsonArrayimages.size(); i++) {
        Image.validateJsonElement(jsonArrayimages.get(i));
      };
      if ((jsonObj.get("InformationSource") != null && !jsonObj.get("InformationSource").isJsonNull()) && !jsonObj.get("InformationSource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `InformationSource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("InformationSource").toString()));
      }
      if ((jsonObj.get("KeyWords") != null && !jsonObj.get("KeyWords").isJsonNull()) && !jsonObj.get("KeyWords").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `KeyWords` to be a primitive type in the JSON string but got `%s`", jsonObj.get("KeyWords").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("KitItems") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("KitItems").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `KitItems` to be an array in the JSON string but got `%s`", jsonObj.get("KitItems").toString()));
      }
      if (!jsonObj.get("ManufacturerCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ManufacturerCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ManufacturerCode").toString()));
      }
      if (!jsonObj.get("MeasurementUnit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MeasurementUnit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MeasurementUnit").toString()));
      }
      if ((jsonObj.get("ModalType") != null && !jsonObj.get("ModalType").isJsonNull()) && !jsonObj.get("ModalType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ModalType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ModalType").toString()));
      }
      if (!jsonObj.get("NameComplete").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `NameComplete` to be a primitive type in the JSON string but got `%s`", jsonObj.get("NameComplete").toString()));
      }
      if (!jsonObj.get("ProductCategoryIds").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProductCategoryIds` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProductCategoryIds").toString()));
      }
      if (!jsonObj.get("ProductClustersIds").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProductClustersIds` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProductClustersIds").toString()));
      }
      if (!jsonObj.get("ProductDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProductDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProductDescription").toString()));
      }
      if (!jsonObj.get("ProductName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProductName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProductName").toString()));
      }
      if ((jsonObj.get("ProductRefId") != null && !jsonObj.get("ProductRefId").isJsonNull()) && !jsonObj.get("ProductRefId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProductRefId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProductRefId").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("ProductSpecifications").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProductSpecifications` to be an array in the JSON string but got `%s`", jsonObj.get("ProductSpecifications").toString()));
      }

      JsonArray jsonArrayproductSpecifications = jsonObj.getAsJsonArray("ProductSpecifications");
      // validate the required field `ProductSpecifications` (array)
      for (int i = 0; i < jsonArrayproductSpecifications.size(); i++) {
        ProductSpecification.validateJsonElement(jsonArrayproductSpecifications.get(i));
      };
      // validate the required field `RealDimension`
      RealDimension.validateJsonElement(jsonObj.get("RealDimension"));
      if ((jsonObj.get("ReleaseDate") != null && !jsonObj.get("ReleaseDate").isJsonNull()) && !jsonObj.get("ReleaseDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ReleaseDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ReleaseDate").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("SalesChannels") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("SalesChannels").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `SalesChannels` to be an array in the JSON string but got `%s`", jsonObj.get("SalesChannels").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("Services") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("Services").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Services` to be an array in the JSON string but got `%s`", jsonObj.get("Services").toString()));
      }
      if (!jsonObj.get("SkuName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SkuName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SkuName").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("SkuSellers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `SkuSellers` to be an array in the JSON string but got `%s`", jsonObj.get("SkuSellers").toString()));
      }

      JsonArray jsonArrayskuSellers = jsonObj.getAsJsonArray("SkuSellers");
      // validate the required field `SkuSellers` (array)
      for (int i = 0; i < jsonArrayskuSellers.size(); i++) {
        SkuSeller.validateJsonElement(jsonArrayskuSellers.get(i));
      };
      // ensure the json data is an array
      if (!jsonObj.get("SkuSpecifications").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `SkuSpecifications` to be an array in the JSON string but got `%s`", jsonObj.get("SkuSpecifications").toString()));
      }

      JsonArray jsonArrayskuSpecifications = jsonObj.getAsJsonArray("SkuSpecifications");
      // validate the required field `SkuSpecifications` (array)
      for (int i = 0; i < jsonArrayskuSpecifications.size(); i++) {
        SkuSpecification.validateJsonElement(jsonArrayskuSpecifications.get(i));
      };
      if ((jsonObj.get("TaxCode") != null && !jsonObj.get("TaxCode").isJsonNull()) && !jsonObj.get("TaxCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaxCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaxCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetSKUAltID.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetSKUAltID' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetSKUAltID> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetSKUAltID.class));

       return (TypeAdapter<T>) new TypeAdapter<GetSKUAltID>() {
           @Override
           public void write(JsonWriter out, GetSKUAltID value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetSKUAltID read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetSKUAltID given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetSKUAltID
   * @throws IOException if the JSON string is invalid with respect to GetSKUAltID
   */
  public static GetSKUAltID fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetSKUAltID.class);
  }

  /**
   * Convert an instance of GetSKUAltID to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

