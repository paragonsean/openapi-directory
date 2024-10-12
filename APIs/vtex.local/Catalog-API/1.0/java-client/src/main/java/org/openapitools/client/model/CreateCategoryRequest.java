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
 * CreateCategoryRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateCategoryRequest {
  public static final String SERIALIZED_NAME_ACTIVE_STORE_FRONT_LINK = "ActiveStoreFrontLink";
  @SerializedName(SERIALIZED_NAME_ACTIVE_STORE_FRONT_LINK)
  private Boolean activeStoreFrontLink;

  public static final String SERIALIZED_NAME_AD_WORDS_REMARKETING_CODE = "AdWordsRemarketingCode";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_AD_WORDS_REMARKETING_CODE)
  private String adWordsRemarketingCode;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FATHER_CATEGORY_ID = "FatherCategoryId";
  @SerializedName(SERIALIZED_NAME_FATHER_CATEGORY_ID)
  private Integer fatherCategoryId;

  public static final String SERIALIZED_NAME_GLOBAL_CATEGORY_ID = "GlobalCategoryId";
  @SerializedName(SERIALIZED_NAME_GLOBAL_CATEGORY_ID)
  private Integer globalCategoryId;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_KEYWORDS = "Keywords";
  @SerializedName(SERIALIZED_NAME_KEYWORDS)
  private String keywords;

  public static final String SERIALIZED_NAME_LOMADEE_CAMPAIGN_CODE = "LomadeeCampaignCode";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_LOMADEE_CAMPAIGN_CODE)
  private String lomadeeCampaignCode;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SCORE = "Score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Integer score;

  public static final String SERIALIZED_NAME_SHOW_BRAND_FILTER = "ShowBrandFilter";
  @SerializedName(SERIALIZED_NAME_SHOW_BRAND_FILTER)
  private Boolean showBrandFilter;

  public static final String SERIALIZED_NAME_SHOW_IN_STORE_FRONT = "ShowInStoreFront";
  @SerializedName(SERIALIZED_NAME_SHOW_IN_STORE_FRONT)
  private Boolean showInStoreFront;

  public static final String SERIALIZED_NAME_STOCK_KEEPING_UNIT_SELECTION_MODE = "StockKeepingUnitSelectionMode";
  @SerializedName(SERIALIZED_NAME_STOCK_KEEPING_UNIT_SELECTION_MODE)
  private String stockKeepingUnitSelectionMode;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public CreateCategoryRequest() {
  }

  public CreateCategoryRequest activeStoreFrontLink(Boolean activeStoreFrontLink) {
    this.activeStoreFrontLink = activeStoreFrontLink;
    return this;
  }

  /**
   * If true, the Category link becomes active in store.
   * @return activeStoreFrontLink
   */
  @javax.annotation.Nonnull
  public Boolean getActiveStoreFrontLink() {
    return activeStoreFrontLink;
  }

  public void setActiveStoreFrontLink(Boolean activeStoreFrontLink) {
    this.activeStoreFrontLink = activeStoreFrontLink;
  }


  @Deprecated
  public CreateCategoryRequest adWordsRemarketingCode(String adWordsRemarketingCode) {
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


  public CreateCategoryRequest description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Text used in meta description tag for Category page.
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public CreateCategoryRequest fatherCategoryId(Integer fatherCategoryId) {
    this.fatherCategoryId = fatherCategoryId;
    return this;
  }

  /**
   * ID of the parent category, apply in case of category and subcategory.
   * @return fatherCategoryId
   */
  @javax.annotation.Nullable
  public Integer getFatherCategoryId() {
    return fatherCategoryId;
  }

  public void setFatherCategoryId(Integer fatherCategoryId) {
    this.fatherCategoryId = fatherCategoryId;
  }


  public CreateCategoryRequest globalCategoryId(Integer globalCategoryId) {
    this.globalCategoryId = globalCategoryId;
    return this;
  }

  /**
   * Google Global Category ID.
   * @return globalCategoryId
   */
  @javax.annotation.Nonnull
  public Integer getGlobalCategoryId() {
    return globalCategoryId;
  }

  public void setGlobalCategoryId(Integer globalCategoryId) {
    this.globalCategoryId = globalCategoryId;
  }


  public CreateCategoryRequest id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Category unique identifier. If not informed, it will be automatically generated by VTEX.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public CreateCategoryRequest isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * If true, the Category page becomes available in store.
   * @return isActive
   */
  @javax.annotation.Nonnull
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public CreateCategoryRequest keywords(String keywords) {
    this.keywords = keywords;
    return this;
  }

  /**
   * Substitute words for the Category.
   * @return keywords
   */
  @javax.annotation.Nonnull
  public String getKeywords() {
    return keywords;
  }

  public void setKeywords(String keywords) {
    this.keywords = keywords;
  }


  @Deprecated
  public CreateCategoryRequest lomadeeCampaignCode(String lomadeeCampaignCode) {
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


  public CreateCategoryRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Category name.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateCategoryRequest score(Integer score) {
    this.score = score;
    return this;
  }

  /**
   * Score for search sorting order.
   * @return score
   */
  @javax.annotation.Nullable
  public Integer getScore() {
    return score;
  }

  public void setScore(Integer score) {
    this.score = score;
  }


  public CreateCategoryRequest showBrandFilter(Boolean showBrandFilter) {
    this.showBrandFilter = showBrandFilter;
    return this;
  }

  /**
   * If true, the Category page displays a Brand filter.
   * @return showBrandFilter
   */
  @javax.annotation.Nonnull
  public Boolean getShowBrandFilter() {
    return showBrandFilter;
  }

  public void setShowBrandFilter(Boolean showBrandFilter) {
    this.showBrandFilter = showBrandFilter;
  }


  public CreateCategoryRequest showInStoreFront(Boolean showInStoreFront) {
    this.showInStoreFront = showInStoreFront;
    return this;
  }

  /**
   * If true, the Category is shown in the top and side menu.
   * @return showInStoreFront
   */
  @javax.annotation.Nonnull
  public Boolean getShowInStoreFront() {
    return showInStoreFront;
  }

  public void setShowInStoreFront(Boolean showInStoreFront) {
    this.showInStoreFront = showInStoreFront;
  }


  public CreateCategoryRequest stockKeepingUnitSelectionMode(String stockKeepingUnitSelectionMode) {
    this.stockKeepingUnitSelectionMode = stockKeepingUnitSelectionMode;
    return this;
  }

  /**
   * Defines how the SKU will be exhibited
   * @return stockKeepingUnitSelectionMode
   */
  @javax.annotation.Nonnull
  public String getStockKeepingUnitSelectionMode() {
    return stockKeepingUnitSelectionMode;
  }

  public void setStockKeepingUnitSelectionMode(String stockKeepingUnitSelectionMode) {
    this.stockKeepingUnitSelectionMode = stockKeepingUnitSelectionMode;
  }


  public CreateCategoryRequest title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Text used in title tag for Category page.
   * @return title
   */
  @javax.annotation.Nonnull
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
    CreateCategoryRequest createCategoryRequest = (CreateCategoryRequest) o;
    return Objects.equals(this.activeStoreFrontLink, createCategoryRequest.activeStoreFrontLink) &&
        Objects.equals(this.adWordsRemarketingCode, createCategoryRequest.adWordsRemarketingCode) &&
        Objects.equals(this.description, createCategoryRequest.description) &&
        Objects.equals(this.fatherCategoryId, createCategoryRequest.fatherCategoryId) &&
        Objects.equals(this.globalCategoryId, createCategoryRequest.globalCategoryId) &&
        Objects.equals(this.id, createCategoryRequest.id) &&
        Objects.equals(this.isActive, createCategoryRequest.isActive) &&
        Objects.equals(this.keywords, createCategoryRequest.keywords) &&
        Objects.equals(this.lomadeeCampaignCode, createCategoryRequest.lomadeeCampaignCode) &&
        Objects.equals(this.name, createCategoryRequest.name) &&
        Objects.equals(this.score, createCategoryRequest.score) &&
        Objects.equals(this.showBrandFilter, createCategoryRequest.showBrandFilter) &&
        Objects.equals(this.showInStoreFront, createCategoryRequest.showInStoreFront) &&
        Objects.equals(this.stockKeepingUnitSelectionMode, createCategoryRequest.stockKeepingUnitSelectionMode) &&
        Objects.equals(this.title, createCategoryRequest.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(activeStoreFrontLink, adWordsRemarketingCode, description, fatherCategoryId, globalCategoryId, id, isActive, keywords, lomadeeCampaignCode, name, score, showBrandFilter, showInStoreFront, stockKeepingUnitSelectionMode, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateCategoryRequest {\n");
    sb.append("    activeStoreFrontLink: ").append(toIndentedString(activeStoreFrontLink)).append("\n");
    sb.append("    adWordsRemarketingCode: ").append(toIndentedString(adWordsRemarketingCode)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    fatherCategoryId: ").append(toIndentedString(fatherCategoryId)).append("\n");
    sb.append("    globalCategoryId: ").append(toIndentedString(globalCategoryId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    keywords: ").append(toIndentedString(keywords)).append("\n");
    sb.append("    lomadeeCampaignCode: ").append(toIndentedString(lomadeeCampaignCode)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    showBrandFilter: ").append(toIndentedString(showBrandFilter)).append("\n");
    sb.append("    showInStoreFront: ").append(toIndentedString(showInStoreFront)).append("\n");
    sb.append("    stockKeepingUnitSelectionMode: ").append(toIndentedString(stockKeepingUnitSelectionMode)).append("\n");
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
    openapiFields.add("ActiveStoreFrontLink");
    openapiFields.add("AdWordsRemarketingCode");
    openapiFields.add("Description");
    openapiFields.add("FatherCategoryId");
    openapiFields.add("GlobalCategoryId");
    openapiFields.add("Id");
    openapiFields.add("IsActive");
    openapiFields.add("Keywords");
    openapiFields.add("LomadeeCampaignCode");
    openapiFields.add("Name");
    openapiFields.add("Score");
    openapiFields.add("ShowBrandFilter");
    openapiFields.add("ShowInStoreFront");
    openapiFields.add("StockKeepingUnitSelectionMode");
    openapiFields.add("Title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ActiveStoreFrontLink");
    openapiRequiredFields.add("AdWordsRemarketingCode");
    openapiRequiredFields.add("Description");
    openapiRequiredFields.add("FatherCategoryId");
    openapiRequiredFields.add("GlobalCategoryId");
    openapiRequiredFields.add("IsActive");
    openapiRequiredFields.add("Keywords");
    openapiRequiredFields.add("LomadeeCampaignCode");
    openapiRequiredFields.add("Name");
    openapiRequiredFields.add("Score");
    openapiRequiredFields.add("ShowBrandFilter");
    openapiRequiredFields.add("ShowInStoreFront");
    openapiRequiredFields.add("StockKeepingUnitSelectionMode");
    openapiRequiredFields.add("Title");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateCategoryRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateCategoryRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateCategoryRequest is not found in the empty JSON string", CreateCategoryRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateCategoryRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateCategoryRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateCategoryRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AdWordsRemarketingCode") != null && !jsonObj.get("AdWordsRemarketingCode").isJsonNull()) && !jsonObj.get("AdWordsRemarketingCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AdWordsRemarketingCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AdWordsRemarketingCode").toString()));
      }
      if (!jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if (!jsonObj.get("Keywords").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Keywords` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Keywords").toString()));
      }
      if ((jsonObj.get("LomadeeCampaignCode") != null && !jsonObj.get("LomadeeCampaignCode").isJsonNull()) && !jsonObj.get("LomadeeCampaignCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LomadeeCampaignCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LomadeeCampaignCode").toString()));
      }
      if (!jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if (!jsonObj.get("StockKeepingUnitSelectionMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `StockKeepingUnitSelectionMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("StockKeepingUnitSelectionMode").toString()));
      }
      if (!jsonObj.get("Title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateCategoryRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateCategoryRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateCategoryRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateCategoryRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateCategoryRequest>() {
           @Override
           public void write(JsonWriter out, CreateCategoryRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateCategoryRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateCategoryRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateCategoryRequest
   * @throws IOException if the JSON string is invalid with respect to CreateCategoryRequest
   */
  public static CreateCategoryRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateCategoryRequest.class);
  }

  /**
   * Convert an instance of CreateCategoryRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

