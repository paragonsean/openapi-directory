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
import java.util.Arrays;
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
 * ApiCatalogPvtProductProductIdPutRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiCatalogPvtProductProductIdPutRequest {
  public static final String SERIALIZED_NAME_AD_WORDS_REMARKETING_CODE = "AdWordsRemarketingCode";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_AD_WORDS_REMARKETING_CODE)
  private String adWordsRemarketingCode;

  public static final String SERIALIZED_NAME_BRAND_ID = "BrandId";
  @SerializedName(SERIALIZED_NAME_BRAND_ID)
  private Integer brandId;

  public static final String SERIALIZED_NAME_CATEGORY_ID = "CategoryId";
  @SerializedName(SERIALIZED_NAME_CATEGORY_ID)
  private Integer categoryId;

  public static final String SERIALIZED_NAME_DEPARTMENT_ID = "DepartmentId";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT_ID)
  private Integer departmentId;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DESCRIPTION_SHORT = "DescriptionShort";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION_SHORT)
  private String descriptionShort;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_VISIBLE = "IsVisible";
  @SerializedName(SERIALIZED_NAME_IS_VISIBLE)
  private Boolean isVisible;

  public static final String SERIALIZED_NAME_KEY_WORDS = "KeyWords";
  @SerializedName(SERIALIZED_NAME_KEY_WORDS)
  private String keyWords;

  public static final String SERIALIZED_NAME_LINK_ID = "LinkId";
  @SerializedName(SERIALIZED_NAME_LINK_ID)
  private String linkId;

  public static final String SERIALIZED_NAME_LOMADEE_CAMPAIGN_CODE = "LomadeeCampaignCode";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_LOMADEE_CAMPAIGN_CODE)
  private String lomadeeCampaignCode;

  public static final String SERIALIZED_NAME_META_TAG_DESCRIPTION = "MetaTagDescription";
  @SerializedName(SERIALIZED_NAME_META_TAG_DESCRIPTION)
  private String metaTagDescription;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_REF_ID = "RefId";
  @SerializedName(SERIALIZED_NAME_REF_ID)
  private String refId;

  public static final String SERIALIZED_NAME_RELEASE_DATE = "ReleaseDate";
  @SerializedName(SERIALIZED_NAME_RELEASE_DATE)
  private String releaseDate;

  public static final String SERIALIZED_NAME_SCORE = "Score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Integer score;

  public static final String SERIALIZED_NAME_SHOW_WITHOUT_STOCK = "ShowWithoutStock";
  @SerializedName(SERIALIZED_NAME_SHOW_WITHOUT_STOCK)
  private Boolean showWithoutStock;

  public static final String SERIALIZED_NAME_SUPPLIER_ID = "SupplierId";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_SUPPLIER_ID)
  private Integer supplierId;

  public static final String SERIALIZED_NAME_TAX_CODE = "TaxCode";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public ApiCatalogPvtProductProductIdPutRequest() {
  }

  @Deprecated
  public ApiCatalogPvtProductProductIdPutRequest adWordsRemarketingCode(String adWordsRemarketingCode) {
    this.adWordsRemarketingCode = adWordsRemarketingCode;
    return this;
  }

  /**
   * This is a legacy field. Do not take this information into consideration.
   * @return adWordsRemarketingCode
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getAdWordsRemarketingCode() {
    return adWordsRemarketingCode;
  }

  @Deprecated
  public void setAdWordsRemarketingCode(String adWordsRemarketingCode) {
    this.adWordsRemarketingCode = adWordsRemarketingCode;
  }


  public ApiCatalogPvtProductProductIdPutRequest brandId(Integer brandId) {
    this.brandId = brandId;
    return this;
  }

  /**
   * Brand ID associated with this product.
   * @return brandId
   */
  @javax.annotation.Nonnull
  public Integer getBrandId() {
    return brandId;
  }

  public void setBrandId(Integer brandId) {
    this.brandId = brandId;
  }


  public ApiCatalogPvtProductProductIdPutRequest categoryId(Integer categoryId) {
    this.categoryId = categoryId;
    return this;
  }

  /**
   * Category ID associated with this product.
   * @return categoryId
   */
  @javax.annotation.Nonnull
  public Integer getCategoryId() {
    return categoryId;
  }

  public void setCategoryId(Integer categoryId) {
    this.categoryId = categoryId;
  }


  public ApiCatalogPvtProductProductIdPutRequest departmentId(Integer departmentId) {
    this.departmentId = departmentId;
    return this;
  }

  /**
   * Department ID according to the product&#39;s category.
   * @return departmentId
   */
  @javax.annotation.Nullable
  public Integer getDepartmentId() {
    return departmentId;
  }

  public void setDepartmentId(Integer departmentId) {
    this.departmentId = departmentId;
  }


  public ApiCatalogPvtProductProductIdPutRequest description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Product description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ApiCatalogPvtProductProductIdPutRequest descriptionShort(String descriptionShort) {
    this.descriptionShort = descriptionShort;
    return this;
  }

  /**
   * Short product description. This information can be displayed on both the product page and the shelf, using the following controls:   Store Framework:  &#x60;$product.DescriptionShort&#x60;.   Legacy CMS Portal: &#x60;&lt;vtex.cmc:productDescriptionShort/&gt;&#x60;.  
   * @return descriptionShort
   */
  @javax.annotation.Nullable
  public String getDescriptionShort() {
    return descriptionShort;
  }

  public void setDescriptionShort(String descriptionShort) {
    this.descriptionShort = descriptionShort;
  }


  public ApiCatalogPvtProductProductIdPutRequest isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Activate (&#x60;true&#x60;) or inactivate (&#x60;false&#x60;) product.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public ApiCatalogPvtProductProductIdPutRequest isVisible(Boolean isVisible) {
    this.isVisible = isVisible;
    return this;
  }

  /**
   * Shows (&#x60;true&#x60;) or hides (&#x60;false&#x60;) the product in search result and product pages, but the product can still be added to the shopping cart. Usually applicable for gifts.
   * @return isVisible
   */
  @javax.annotation.Nullable
  public Boolean getIsVisible() {
    return isVisible;
  }

  public void setIsVisible(Boolean isVisible) {
    this.isVisible = isVisible;
  }


  public ApiCatalogPvtProductProductIdPutRequest keyWords(String keyWords) {
    this.keyWords = keyWords;
    return this;
  }

  /**
   * Store Framework: Deprecated.   Legacy CMS Portal: Keywords or synonyms related to the product, separated by comma (&#x60;,&#x60;). \&quot;Television\&quot;, for example, can have a substitute word like \&quot;TV\&quot;. This field is important to make your searches more comprehensive.  
   * @return keyWords
   */
  @javax.annotation.Nullable
  public String getKeyWords() {
    return keyWords;
  }

  public void setKeyWords(String keyWords) {
    this.keyWords = keyWords;
  }


  public ApiCatalogPvtProductProductIdPutRequest linkId(String linkId) {
    this.linkId = linkId;
    return this;
  }

  /**
   * Slug that will be used to build the product page URL. If it not informed, it will be generated according to the product&#39;s name replacing spaces and special characters by hyphens (&#x60;-&#x60;).
   * @return linkId
   */
  @javax.annotation.Nullable
  public String getLinkId() {
    return linkId;
  }

  public void setLinkId(String linkId) {
    this.linkId = linkId;
  }


  @Deprecated
  public ApiCatalogPvtProductProductIdPutRequest lomadeeCampaignCode(String lomadeeCampaignCode) {
    this.lomadeeCampaignCode = lomadeeCampaignCode;
    return this;
  }

  /**
   * This is a legacy field. Do not take this information into consideration.
   * @return lomadeeCampaignCode
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getLomadeeCampaignCode() {
    return lomadeeCampaignCode;
  }

  @Deprecated
  public void setLomadeeCampaignCode(String lomadeeCampaignCode) {
    this.lomadeeCampaignCode = lomadeeCampaignCode;
  }


  public ApiCatalogPvtProductProductIdPutRequest metaTagDescription(String metaTagDescription) {
    this.metaTagDescription = metaTagDescription;
    return this;
  }

  /**
   * Brief description of the product for SEO. It is recommended not to exceed 150 characters.
   * @return metaTagDescription
   */
  @javax.annotation.Nullable
  public String getMetaTagDescription() {
    return metaTagDescription;
  }

  public void setMetaTagDescription(String metaTagDescription) {
    this.metaTagDescription = metaTagDescription;
  }


  public ApiCatalogPvtProductProductIdPutRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Product&#39;s name. Limited to 150 characters.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ApiCatalogPvtProductProductIdPutRequest refId(String refId) {
    this.refId = refId;
    return this;
  }

  /**
   * Product Reference Code.
   * @return refId
   */
  @javax.annotation.Nullable
  public String getRefId() {
    return refId;
  }

  public void setRefId(String refId) {
    this.refId = refId;
  }


  public ApiCatalogPvtProductProductIdPutRequest releaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
    return this;
  }

  /**
   * Used to assist in the ordering of the search result of the site. Using the &#x60;O&#x3D;OrderByReleaseDateDESC&#x60; query string, you can pull this value and show the display order by release date. This attribute is also used as a condition for dynamic collections.
   * @return releaseDate
   */
  @javax.annotation.Nullable
  public String getReleaseDate() {
    return releaseDate;
  }

  public void setReleaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
  }


  public ApiCatalogPvtProductProductIdPutRequest score(Integer score) {
    this.score = score;
    return this;
  }

  /**
   * Value used to set the priority on the search result page.
   * @return score
   */
  @javax.annotation.Nullable
  public Integer getScore() {
    return score;
  }

  public void setScore(Integer score) {
    this.score = score;
  }


  public ApiCatalogPvtProductProductIdPutRequest showWithoutStock(Boolean showWithoutStock) {
    this.showWithoutStock = showWithoutStock;
    return this;
  }

  /**
   * If &#x60;true&#x60;, activates the [Notify Me](https://help.vtex.com/en/tutorial/setting-up-the-notify-me-option--2VqVifQuf6Co2KG048Yu6e) option when the product is out of stock.
   * @return showWithoutStock
   */
  @javax.annotation.Nullable
  public Boolean getShowWithoutStock() {
    return showWithoutStock;
  }

  public void setShowWithoutStock(Boolean showWithoutStock) {
    this.showWithoutStock = showWithoutStock;
  }


  @Deprecated
  public ApiCatalogPvtProductProductIdPutRequest supplierId(Integer supplierId) {
    this.supplierId = supplierId;
    return this;
  }

  /**
   * Get supplierId
   * @return supplierId
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Integer getSupplierId() {
    return supplierId;
  }

  @Deprecated
  public void setSupplierId(Integer supplierId) {
    this.supplierId = supplierId;
  }


  public ApiCatalogPvtProductProductIdPutRequest taxCode(String taxCode) {
    this.taxCode = taxCode;
    return this;
  }

  /**
   * Product tax code, used for tax calculation.
   * @return taxCode
   */
  @javax.annotation.Nullable
  public String getTaxCode() {
    return taxCode;
  }

  public void setTaxCode(String taxCode) {
    this.taxCode = taxCode;
  }


  public ApiCatalogPvtProductProductIdPutRequest title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Product&#39;s Title tag. Limited to 150 characters. It is presented in the browser tab and corresponds to the title of the product page. This field is important for SEO.
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiCatalogPvtProductProductIdPutRequest apiCatalogPvtProductProductIdPutRequest = (ApiCatalogPvtProductProductIdPutRequest) o;
    return Objects.equals(this.adWordsRemarketingCode, apiCatalogPvtProductProductIdPutRequest.adWordsRemarketingCode) &&
        Objects.equals(this.brandId, apiCatalogPvtProductProductIdPutRequest.brandId) &&
        Objects.equals(this.categoryId, apiCatalogPvtProductProductIdPutRequest.categoryId) &&
        Objects.equals(this.departmentId, apiCatalogPvtProductProductIdPutRequest.departmentId) &&
        Objects.equals(this.description, apiCatalogPvtProductProductIdPutRequest.description) &&
        Objects.equals(this.descriptionShort, apiCatalogPvtProductProductIdPutRequest.descriptionShort) &&
        Objects.equals(this.isActive, apiCatalogPvtProductProductIdPutRequest.isActive) &&
        Objects.equals(this.isVisible, apiCatalogPvtProductProductIdPutRequest.isVisible) &&
        Objects.equals(this.keyWords, apiCatalogPvtProductProductIdPutRequest.keyWords) &&
        Objects.equals(this.linkId, apiCatalogPvtProductProductIdPutRequest.linkId) &&
        Objects.equals(this.lomadeeCampaignCode, apiCatalogPvtProductProductIdPutRequest.lomadeeCampaignCode) &&
        Objects.equals(this.metaTagDescription, apiCatalogPvtProductProductIdPutRequest.metaTagDescription) &&
        Objects.equals(this.name, apiCatalogPvtProductProductIdPutRequest.name) &&
        Objects.equals(this.refId, apiCatalogPvtProductProductIdPutRequest.refId) &&
        Objects.equals(this.releaseDate, apiCatalogPvtProductProductIdPutRequest.releaseDate) &&
        Objects.equals(this.score, apiCatalogPvtProductProductIdPutRequest.score) &&
        Objects.equals(this.showWithoutStock, apiCatalogPvtProductProductIdPutRequest.showWithoutStock) &&
        Objects.equals(this.supplierId, apiCatalogPvtProductProductIdPutRequest.supplierId) &&
        Objects.equals(this.taxCode, apiCatalogPvtProductProductIdPutRequest.taxCode) &&
        Objects.equals(this.title, apiCatalogPvtProductProductIdPutRequest.title);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(adWordsRemarketingCode, brandId, categoryId, departmentId, description, descriptionShort, isActive, isVisible, keyWords, linkId, lomadeeCampaignCode, metaTagDescription, name, refId, releaseDate, score, showWithoutStock, supplierId, taxCode, title);
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
    sb.append("class ApiCatalogPvtProductProductIdPutRequest {\n");
    sb.append("    adWordsRemarketingCode: ").append(toIndentedString(adWordsRemarketingCode)).append("\n");
    sb.append("    brandId: ").append(toIndentedString(brandId)).append("\n");
    sb.append("    categoryId: ").append(toIndentedString(categoryId)).append("\n");
    sb.append("    departmentId: ").append(toIndentedString(departmentId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    descriptionShort: ").append(toIndentedString(descriptionShort)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isVisible: ").append(toIndentedString(isVisible)).append("\n");
    sb.append("    keyWords: ").append(toIndentedString(keyWords)).append("\n");
    sb.append("    linkId: ").append(toIndentedString(linkId)).append("\n");
    sb.append("    lomadeeCampaignCode: ").append(toIndentedString(lomadeeCampaignCode)).append("\n");
    sb.append("    metaTagDescription: ").append(toIndentedString(metaTagDescription)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    refId: ").append(toIndentedString(refId)).append("\n");
    sb.append("    releaseDate: ").append(toIndentedString(releaseDate)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    showWithoutStock: ").append(toIndentedString(showWithoutStock)).append("\n");
    sb.append("    supplierId: ").append(toIndentedString(supplierId)).append("\n");
    sb.append("    taxCode: ").append(toIndentedString(taxCode)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("AdWordsRemarketingCode");
    openapiFields.add("BrandId");
    openapiFields.add("CategoryId");
    openapiFields.add("DepartmentId");
    openapiFields.add("Description");
    openapiFields.add("DescriptionShort");
    openapiFields.add("IsActive");
    openapiFields.add("IsVisible");
    openapiFields.add("KeyWords");
    openapiFields.add("LinkId");
    openapiFields.add("LomadeeCampaignCode");
    openapiFields.add("MetaTagDescription");
    openapiFields.add("Name");
    openapiFields.add("RefId");
    openapiFields.add("ReleaseDate");
    openapiFields.add("Score");
    openapiFields.add("ShowWithoutStock");
    openapiFields.add("SupplierId");
    openapiFields.add("TaxCode");
    openapiFields.add("Title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("BrandId");
    openapiRequiredFields.add("CategoryId");
    openapiRequiredFields.add("Name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiCatalogPvtProductProductIdPutRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiCatalogPvtProductProductIdPutRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiCatalogPvtProductProductIdPutRequest is not found in the empty JSON string", ApiCatalogPvtProductProductIdPutRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiCatalogPvtProductProductIdPutRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiCatalogPvtProductProductIdPutRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ApiCatalogPvtProductProductIdPutRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AdWordsRemarketingCode") != null && !jsonObj.get("AdWordsRemarketingCode").isJsonNull()) && !jsonObj.get("AdWordsRemarketingCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AdWordsRemarketingCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AdWordsRemarketingCode").toString()));
      }
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("DescriptionShort") != null && !jsonObj.get("DescriptionShort").isJsonNull()) && !jsonObj.get("DescriptionShort").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DescriptionShort` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DescriptionShort").toString()));
      }
      if ((jsonObj.get("KeyWords") != null && !jsonObj.get("KeyWords").isJsonNull()) && !jsonObj.get("KeyWords").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `KeyWords` to be a primitive type in the JSON string but got `%s`", jsonObj.get("KeyWords").toString()));
      }
      if ((jsonObj.get("LinkId") != null && !jsonObj.get("LinkId").isJsonNull()) && !jsonObj.get("LinkId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LinkId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LinkId").toString()));
      }
      if ((jsonObj.get("LomadeeCampaignCode") != null && !jsonObj.get("LomadeeCampaignCode").isJsonNull()) && !jsonObj.get("LomadeeCampaignCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LomadeeCampaignCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LomadeeCampaignCode").toString()));
      }
      if ((jsonObj.get("MetaTagDescription") != null && !jsonObj.get("MetaTagDescription").isJsonNull()) && !jsonObj.get("MetaTagDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MetaTagDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MetaTagDescription").toString()));
      }
      if (!jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("RefId") != null && !jsonObj.get("RefId").isJsonNull()) && !jsonObj.get("RefId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RefId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RefId").toString()));
      }
      if ((jsonObj.get("ReleaseDate") != null && !jsonObj.get("ReleaseDate").isJsonNull()) && !jsonObj.get("ReleaseDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ReleaseDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ReleaseDate").toString()));
      }
      if ((jsonObj.get("TaxCode") != null && !jsonObj.get("TaxCode").isJsonNull()) && !jsonObj.get("TaxCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TaxCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TaxCode").toString()));
      }
      if ((jsonObj.get("Title") != null && !jsonObj.get("Title").isJsonNull()) && !jsonObj.get("Title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiCatalogPvtProductProductIdPutRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiCatalogPvtProductProductIdPutRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiCatalogPvtProductProductIdPutRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiCatalogPvtProductProductIdPutRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiCatalogPvtProductProductIdPutRequest>() {
           @Override
           public void write(JsonWriter out, ApiCatalogPvtProductProductIdPutRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiCatalogPvtProductProductIdPutRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiCatalogPvtProductProductIdPutRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiCatalogPvtProductProductIdPutRequest
   * @throws IOException if the JSON string is invalid with respect to ApiCatalogPvtProductProductIdPutRequest
   */
  public static ApiCatalogPvtProductProductIdPutRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiCatalogPvtProductProductIdPutRequest.class);
  }

  /**
   * Convert an instance of ApiCatalogPvtProductProductIdPutRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

