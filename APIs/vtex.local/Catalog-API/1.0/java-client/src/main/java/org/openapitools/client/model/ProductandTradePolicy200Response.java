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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * ProductandTradePolicy200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductandTradePolicy200Response {
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

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

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

  public static final String SERIALIZED_NAME_LIST_STORE_ID = "ListStoreId";
  @SerializedName(SERIALIZED_NAME_LIST_STORE_ID)
  private List<Object> listStoreId = new ArrayList<>();

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

  public static final String SERIALIZED_NAME_SHOW_WITHOUT_STOCK = "ShowWithoutStock";
  @SerializedName(SERIALIZED_NAME_SHOW_WITHOUT_STOCK)
  private Boolean showWithoutStock;

  public static final String SERIALIZED_NAME_SUPPLIER_ID = "SupplierId";
  @SerializedName(SERIALIZED_NAME_SUPPLIER_ID)
  private Integer supplierId;

  public static final String SERIALIZED_NAME_TAX_CODE = "TaxCode";
  @SerializedName(SERIALIZED_NAME_TAX_CODE)
  private String taxCode;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public ProductandTradePolicy200Response() {
  }

  @Deprecated
  public ProductandTradePolicy200Response adWordsRemarketingCode(String adWordsRemarketingCode) {
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


  public ProductandTradePolicy200Response brandId(Integer brandId) {
    this.brandId = brandId;
    return this;
  }

  /**
   * Product brand ID.
   * @return brandId
   */
  @javax.annotation.Nullable
  public Integer getBrandId() {
    return brandId;
  }

  public void setBrandId(Integer brandId) {
    this.brandId = brandId;
  }


  public ProductandTradePolicy200Response categoryId(Integer categoryId) {
    this.categoryId = categoryId;
    return this;
  }

  /**
   * Product category ID.
   * @return categoryId
   */
  @javax.annotation.Nullable
  public Integer getCategoryId() {
    return categoryId;
  }

  public void setCategoryId(Integer categoryId) {
    this.categoryId = categoryId;
  }


  public ProductandTradePolicy200Response departmentId(Integer departmentId) {
    this.departmentId = departmentId;
    return this;
  }

  /**
   * Product department ID.
   * @return departmentId
   */
  @javax.annotation.Nullable
  public Integer getDepartmentId() {
    return departmentId;
  }

  public void setDepartmentId(Integer departmentId) {
    this.departmentId = departmentId;
  }


  public ProductandTradePolicy200Response description(String description) {
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


  public ProductandTradePolicy200Response descriptionShort(String descriptionShort) {
    this.descriptionShort = descriptionShort;
    return this;
  }

  /**
   * Product complement name.
   * @return descriptionShort
   */
  @javax.annotation.Nullable
  public String getDescriptionShort() {
    return descriptionShort;
  }

  public void setDescriptionShort(String descriptionShort) {
    this.descriptionShort = descriptionShort;
  }


  public ProductandTradePolicy200Response id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Product ID.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public ProductandTradePolicy200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * If the product is active (&#x60;true&#x60;) or not (&#x60;false&#x60;) at the store.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public ProductandTradePolicy200Response isVisible(Boolean isVisible) {
    this.isVisible = isVisible;
    return this;
  }

  /**
   * If the Product is visible on the store.
   * @return isVisible
   */
  @javax.annotation.Nullable
  public Boolean getIsVisible() {
    return isVisible;
  }

  public void setIsVisible(Boolean isVisible) {
    this.isVisible = isVisible;
  }


  public ProductandTradePolicy200Response keyWords(String keyWords) {
    this.keyWords = keyWords;
    return this;
  }

  /**
   * Substitutes words for the product.
   * @return keyWords
   */
  @javax.annotation.Nullable
  public String getKeyWords() {
    return keyWords;
  }

  public void setKeyWords(String keyWords) {
    this.keyWords = keyWords;
  }


  public ProductandTradePolicy200Response linkId(String linkId) {
    this.linkId = linkId;
    return this;
  }

  /**
   * Product text link.
   * @return linkId
   */
  @javax.annotation.Nullable
  public String getLinkId() {
    return linkId;
  }

  public void setLinkId(String linkId) {
    this.linkId = linkId;
  }


  public ProductandTradePolicy200Response listStoreId(List<Object> listStoreId) {
    this.listStoreId = listStoreId;
    return this;
  }

  public ProductandTradePolicy200Response addListStoreIdItem(Object listStoreIdItem) {
    if (this.listStoreId == null) {
      this.listStoreId = new ArrayList<>();
    }
    this.listStoreId.add(listStoreIdItem);
    return this;
  }

  /**
   * List with the Trade Policies IDs that the product is included.
   * @return listStoreId
   */
  @javax.annotation.Nullable
  public List<Object> getListStoreId() {
    return listStoreId;
  }

  public void setListStoreId(List<Object> listStoreId) {
    this.listStoreId = listStoreId;
  }


  @Deprecated
  public ProductandTradePolicy200Response lomadeeCampaignCode(String lomadeeCampaignCode) {
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


  public ProductandTradePolicy200Response metaTagDescription(String metaTagDescription) {
    this.metaTagDescription = metaTagDescription;
    return this;
  }

  /**
   * Product meta tag description.
   * @return metaTagDescription
   */
  @javax.annotation.Nullable
  public String getMetaTagDescription() {
    return metaTagDescription;
  }

  public void setMetaTagDescription(String metaTagDescription) {
    this.metaTagDescription = metaTagDescription;
  }


  public ProductandTradePolicy200Response name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Product&#39;s name. Limited to 150 characters.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ProductandTradePolicy200Response refId(String refId) {
    this.refId = refId;
    return this;
  }

  /**
   * Product referecial code.
   * @return refId
   */
  @javax.annotation.Nullable
  public String getRefId() {
    return refId;
  }

  public void setRefId(String refId) {
    this.refId = refId;
  }


  public ProductandTradePolicy200Response releaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
    return this;
  }

  /**
   * Product release date.
   * @return releaseDate
   */
  @javax.annotation.Nullable
  public String getReleaseDate() {
    return releaseDate;
  }

  public void setReleaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
  }


  public ProductandTradePolicy200Response showWithoutStock(Boolean showWithoutStock) {
    this.showWithoutStock = showWithoutStock;
    return this;
  }

  /**
   * Defines if the Product will remain being shown in the store even if it’s out of stock.
   * @return showWithoutStock
   */
  @javax.annotation.Nullable
  public Boolean getShowWithoutStock() {
    return showWithoutStock;
  }

  public void setShowWithoutStock(Boolean showWithoutStock) {
    this.showWithoutStock = showWithoutStock;
  }


  public ProductandTradePolicy200Response supplierId(Integer supplierId) {
    this.supplierId = supplierId;
    return this;
  }

  /**
   * Product supplier ID.
   * @return supplierId
   */
  @javax.annotation.Nullable
  public Integer getSupplierId() {
    return supplierId;
  }

  public void setSupplierId(Integer supplierId) {
    this.supplierId = supplierId;
  }


  public ProductandTradePolicy200Response taxCode(String taxCode) {
    this.taxCode = taxCode;
    return this;
  }

  /**
   * Product fiscal code.
   * @return taxCode
   */
  @javax.annotation.Nullable
  public String getTaxCode() {
    return taxCode;
  }

  public void setTaxCode(String taxCode) {
    this.taxCode = taxCode;
  }


  public ProductandTradePolicy200Response title(String title) {
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
    ProductandTradePolicy200Response productandTradePolicy200Response = (ProductandTradePolicy200Response) o;
    return Objects.equals(this.adWordsRemarketingCode, productandTradePolicy200Response.adWordsRemarketingCode) &&
        Objects.equals(this.brandId, productandTradePolicy200Response.brandId) &&
        Objects.equals(this.categoryId, productandTradePolicy200Response.categoryId) &&
        Objects.equals(this.departmentId, productandTradePolicy200Response.departmentId) &&
        Objects.equals(this.description, productandTradePolicy200Response.description) &&
        Objects.equals(this.descriptionShort, productandTradePolicy200Response.descriptionShort) &&
        Objects.equals(this.id, productandTradePolicy200Response.id) &&
        Objects.equals(this.isActive, productandTradePolicy200Response.isActive) &&
        Objects.equals(this.isVisible, productandTradePolicy200Response.isVisible) &&
        Objects.equals(this.keyWords, productandTradePolicy200Response.keyWords) &&
        Objects.equals(this.linkId, productandTradePolicy200Response.linkId) &&
        Objects.equals(this.listStoreId, productandTradePolicy200Response.listStoreId) &&
        Objects.equals(this.lomadeeCampaignCode, productandTradePolicy200Response.lomadeeCampaignCode) &&
        Objects.equals(this.metaTagDescription, productandTradePolicy200Response.metaTagDescription) &&
        Objects.equals(this.name, productandTradePolicy200Response.name) &&
        Objects.equals(this.refId, productandTradePolicy200Response.refId) &&
        Objects.equals(this.releaseDate, productandTradePolicy200Response.releaseDate) &&
        Objects.equals(this.showWithoutStock, productandTradePolicy200Response.showWithoutStock) &&
        Objects.equals(this.supplierId, productandTradePolicy200Response.supplierId) &&
        Objects.equals(this.taxCode, productandTradePolicy200Response.taxCode) &&
        Objects.equals(this.title, productandTradePolicy200Response.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adWordsRemarketingCode, brandId, categoryId, departmentId, description, descriptionShort, id, isActive, isVisible, keyWords, linkId, listStoreId, lomadeeCampaignCode, metaTagDescription, name, refId, releaseDate, showWithoutStock, supplierId, taxCode, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProductandTradePolicy200Response {\n");
    sb.append("    adWordsRemarketingCode: ").append(toIndentedString(adWordsRemarketingCode)).append("\n");
    sb.append("    brandId: ").append(toIndentedString(brandId)).append("\n");
    sb.append("    categoryId: ").append(toIndentedString(categoryId)).append("\n");
    sb.append("    departmentId: ").append(toIndentedString(departmentId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    descriptionShort: ").append(toIndentedString(descriptionShort)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isVisible: ").append(toIndentedString(isVisible)).append("\n");
    sb.append("    keyWords: ").append(toIndentedString(keyWords)).append("\n");
    sb.append("    linkId: ").append(toIndentedString(linkId)).append("\n");
    sb.append("    listStoreId: ").append(toIndentedString(listStoreId)).append("\n");
    sb.append("    lomadeeCampaignCode: ").append(toIndentedString(lomadeeCampaignCode)).append("\n");
    sb.append("    metaTagDescription: ").append(toIndentedString(metaTagDescription)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    refId: ").append(toIndentedString(refId)).append("\n");
    sb.append("    releaseDate: ").append(toIndentedString(releaseDate)).append("\n");
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
    openapiFields.add("Id");
    openapiFields.add("IsActive");
    openapiFields.add("IsVisible");
    openapiFields.add("KeyWords");
    openapiFields.add("LinkId");
    openapiFields.add("ListStoreId");
    openapiFields.add("LomadeeCampaignCode");
    openapiFields.add("MetaTagDescription");
    openapiFields.add("Name");
    openapiFields.add("RefId");
    openapiFields.add("ReleaseDate");
    openapiFields.add("ShowWithoutStock");
    openapiFields.add("SupplierId");
    openapiFields.add("TaxCode");
    openapiFields.add("Title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProductandTradePolicy200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProductandTradePolicy200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProductandTradePolicy200Response is not found in the empty JSON string", ProductandTradePolicy200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProductandTradePolicy200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProductandTradePolicy200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      // ensure the optional json data is an array if present
      if (jsonObj.get("ListStoreId") != null && !jsonObj.get("ListStoreId").isJsonNull() && !jsonObj.get("ListStoreId").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ListStoreId` to be an array in the JSON string but got `%s`", jsonObj.get("ListStoreId").toString()));
      }
      if ((jsonObj.get("LomadeeCampaignCode") != null && !jsonObj.get("LomadeeCampaignCode").isJsonNull()) && !jsonObj.get("LomadeeCampaignCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LomadeeCampaignCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LomadeeCampaignCode").toString()));
      }
      if ((jsonObj.get("MetaTagDescription") != null && !jsonObj.get("MetaTagDescription").isJsonNull()) && !jsonObj.get("MetaTagDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MetaTagDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MetaTagDescription").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
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
       if (!ProductandTradePolicy200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProductandTradePolicy200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProductandTradePolicy200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProductandTradePolicy200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<ProductandTradePolicy200Response>() {
           @Override
           public void write(JsonWriter out, ProductandTradePolicy200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProductandTradePolicy200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProductandTradePolicy200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProductandTradePolicy200Response
   * @throws IOException if the JSON string is invalid with respect to ProductandTradePolicy200Response
   */
  public static ProductandTradePolicy200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProductandTradePolicy200Response.class);
  }

  /**
   * Convert an instance of ProductandTradePolicy200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

