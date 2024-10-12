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
 * SpecificationsField200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SpecificationsField200Response {
  public static final String SERIALIZED_NAME_DEFAULT_VALUE = "DefaultValue";
  @SerializedName(SERIALIZED_NAME_DEFAULT_VALUE)
  private String defaultValue;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FIELD_GROUP_ID = "FieldGroupId";
  @SerializedName(SERIALIZED_NAME_FIELD_GROUP_ID)
  private Integer fieldGroupId;

  public static final String SERIALIZED_NAME_FIELD_GROUP_NAME = "FieldGroupName";
  @SerializedName(SERIALIZED_NAME_FIELD_GROUP_NAME)
  private String fieldGroupName;

  public static final String SERIALIZED_NAME_FIELD_ID = "FieldId";
  @SerializedName(SERIALIZED_NAME_FIELD_ID)
  private Integer fieldId;

  public static final String SERIALIZED_NAME_FIELD_TYPE_ID = "FieldTypeId";
  @SerializedName(SERIALIZED_NAME_FIELD_TYPE_ID)
  private Integer fieldTypeId;

  public static final String SERIALIZED_NAME_FIELD_TYPE_NAME = "FieldTypeName";
  @SerializedName(SERIALIZED_NAME_FIELD_TYPE_NAME)
  private String fieldTypeName;

  public static final String SERIALIZED_NAME_FIELD_VALUE_ID = "FieldValueId";
  @SerializedName(SERIALIZED_NAME_FIELD_VALUE_ID)
  private Integer fieldValueId;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_FILTER = "IsFilter";
  @SerializedName(SERIALIZED_NAME_IS_FILTER)
  private Boolean isFilter;

  public static final String SERIALIZED_NAME_IS_ON_PRODUCT_DETAILS = "IsOnProductDetails";
  @SerializedName(SERIALIZED_NAME_IS_ON_PRODUCT_DETAILS)
  private Boolean isOnProductDetails;

  public static final String SERIALIZED_NAME_IS_REQUIRED = "IsRequired";
  @SerializedName(SERIALIZED_NAME_IS_REQUIRED)
  private Boolean isRequired;

  public static final String SERIALIZED_NAME_IS_SIDE_MENU_LINK_ACTIVE = "IsSideMenuLinkActive";
  @SerializedName(SERIALIZED_NAME_IS_SIDE_MENU_LINK_ACTIVE)
  private Boolean isSideMenuLinkActive;

  public static final String SERIALIZED_NAME_IS_STOCK_KEEPING_UNIT = "IsStockKeepingUnit";
  @SerializedName(SERIALIZED_NAME_IS_STOCK_KEEPING_UNIT)
  private Boolean isStockKeepingUnit;

  public static final String SERIALIZED_NAME_IS_TOP_MENU_LINK_ACTIVE = "IsTopMenuLinkActive";
  @SerializedName(SERIALIZED_NAME_IS_TOP_MENU_LINK_ACTIVE)
  private Boolean isTopMenuLinkActive;

  public static final String SERIALIZED_NAME_IS_WIZARD = "IsWizard";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_WIZARD)
  private Boolean isWizard;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_POSITION = "Position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private Integer position;

  public SpecificationsField200Response() {
  }

  public SpecificationsField200Response defaultValue(String defaultValue) {
    this.defaultValue = defaultValue;
    return this;
  }

  /**
   * Specification default value.
   * @return defaultValue
   */
  @javax.annotation.Nullable
  public String getDefaultValue() {
    return defaultValue;
  }

  public void setDefaultValue(String defaultValue) {
    this.defaultValue = defaultValue;
  }


  @Deprecated
  public SpecificationsField200Response description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  @Deprecated
  public void setDescription(String description) {
    this.description = description;
  }


  public SpecificationsField200Response fieldGroupId(Integer fieldGroupId) {
    this.fieldGroupId = fieldGroupId;
    return this;
  }

  /**
   * ID of the group of specifications that contains the new specification.
   * @return fieldGroupId
   */
  @javax.annotation.Nullable
  public Integer getFieldGroupId() {
    return fieldGroupId;
  }

  public void setFieldGroupId(Integer fieldGroupId) {
    this.fieldGroupId = fieldGroupId;
  }


  public SpecificationsField200Response fieldGroupName(String fieldGroupName) {
    this.fieldGroupName = fieldGroupName;
    return this;
  }

  /**
   * Specification Field Group Name.
   * @return fieldGroupName
   */
  @javax.annotation.Nullable
  public String getFieldGroupName() {
    return fieldGroupName;
  }

  public void setFieldGroupName(String fieldGroupName) {
    this.fieldGroupName = fieldGroupName;
  }


  public SpecificationsField200Response fieldId(Integer fieldId) {
    this.fieldId = fieldId;
    return this;
  }

  /**
   * Specification field ID.
   * @return fieldId
   */
  @javax.annotation.Nullable
  public Integer getFieldId() {
    return fieldId;
  }

  public void setFieldId(Integer fieldId) {
    this.fieldId = fieldId;
  }


  public SpecificationsField200Response fieldTypeId(Integer fieldTypeId) {
    this.fieldTypeId = fieldTypeId;
    return this;
  }

  /**
   * Field Type ID can be &#x60;1 - Text&#x60;, &#x60;2 - Multi-Line Text&#x60;, &#x60;4 - Number&#x60;, &#x60;5 - Combo&#x60;, &#x60;6 - Radio&#x60;, &#x60;7 - Checkbox&#x60;, &#x60;8 - Indexed Text&#x60;, &#x60;9 - Indexed Multi-Line Text&#x60;.
   * @return fieldTypeId
   */
  @javax.annotation.Nullable
  public Integer getFieldTypeId() {
    return fieldTypeId;
  }

  public void setFieldTypeId(Integer fieldTypeId) {
    this.fieldTypeId = fieldTypeId;
  }


  public SpecificationsField200Response fieldTypeName(String fieldTypeName) {
    this.fieldTypeName = fieldTypeName;
    return this;
  }

  /**
   * Field Type name, which can be &#x60;Text&#x60;, &#x60;Multi-Line Text&#x60;, &#x60;Number&#x60;, &#x60;Combo&#x60;, &#x60;Radio&#x60;, &#x60;Checkbox&#x60;, &#x60;Indexed Text&#x60; or &#x60;Indexed Multi-Line Text&#x60;.
   * @return fieldTypeName
   */
  @javax.annotation.Nullable
  public String getFieldTypeName() {
    return fieldTypeName;
  }

  public void setFieldTypeName(String fieldTypeName) {
    this.fieldTypeName = fieldTypeName;
  }


  public SpecificationsField200Response fieldValueId(Integer fieldValueId) {
    this.fieldValueId = fieldValueId;
    return this;
  }

  /**
   * Specification value ID.
   * @return fieldValueId
   */
  @javax.annotation.Nullable
  public Integer getFieldValueId() {
    return fieldValueId;
  }

  public void setFieldValueId(Integer fieldValueId) {
    this.fieldValueId = fieldValueId;
  }


  public SpecificationsField200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Enable (&#x60;true&#x60;) or disable (&#x60;false&#x60;) specification.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public SpecificationsField200Response isFilter(Boolean isFilter) {
    this.isFilter = isFilter;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal - To allow the specification to be used as a facet (filter) on the search navigation bar.  
   * @return isFilter
   */
  @javax.annotation.Nullable
  public Boolean getIsFilter() {
    return isFilter;
  }

  public void setIsFilter(Boolean isFilter) {
    this.isFilter = isFilter;
  }


  public SpecificationsField200Response isOnProductDetails(Boolean isOnProductDetails) {
    this.isOnProductDetails = isOnProductDetails;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal -If specification is visible on the product page.  
   * @return isOnProductDetails
   */
  @javax.annotation.Nullable
  public Boolean getIsOnProductDetails() {
    return isOnProductDetails;
  }

  public void setIsOnProductDetails(Boolean isOnProductDetails) {
    this.isOnProductDetails = isOnProductDetails;
  }


  public SpecificationsField200Response isRequired(Boolean isRequired) {
    this.isRequired = isRequired;
    return this;
  }

  /**
   * Makes the specification mandatory (&#x60;true&#x60;) or optional (&#x60;false&#x60;).
   * @return isRequired
   */
  @javax.annotation.Nullable
  public Boolean getIsRequired() {
    return isRequired;
  }

  public void setIsRequired(Boolean isRequired) {
    this.isRequired = isRequired;
  }


  public SpecificationsField200Response isSideMenuLinkActive(Boolean isSideMenuLinkActive) {
    this.isSideMenuLinkActive = isSideMenuLinkActive;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal - To make the specification field clickable in the search navigation bar.  
   * @return isSideMenuLinkActive
   */
  @javax.annotation.Nullable
  public Boolean getIsSideMenuLinkActive() {
    return isSideMenuLinkActive;
  }

  public void setIsSideMenuLinkActive(Boolean isSideMenuLinkActive) {
    this.isSideMenuLinkActive = isSideMenuLinkActive;
  }


  public SpecificationsField200Response isStockKeepingUnit(Boolean isStockKeepingUnit) {
    this.isStockKeepingUnit = isStockKeepingUnit;
    return this;
  }

  /**
   * If &#x60;true&#x60;, it will be added as a SKU specification. If &#x60;false&#x60;, it will be added as a product specification field.
   * @return isStockKeepingUnit
   */
  @javax.annotation.Nullable
  public Boolean getIsStockKeepingUnit() {
    return isStockKeepingUnit;
  }

  public void setIsStockKeepingUnit(Boolean isStockKeepingUnit) {
    this.isStockKeepingUnit = isStockKeepingUnit;
  }


  public SpecificationsField200Response isTopMenuLinkActive(Boolean isTopMenuLinkActive) {
    this.isTopMenuLinkActive = isTopMenuLinkActive;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal - To make the specification visible in the store&#39;s upper menu.  
   * @return isTopMenuLinkActive
   */
  @javax.annotation.Nullable
  public Boolean getIsTopMenuLinkActive() {
    return isTopMenuLinkActive;
  }

  public void setIsTopMenuLinkActive(Boolean isTopMenuLinkActive) {
    this.isTopMenuLinkActive = isTopMenuLinkActive;
  }


  @Deprecated
  public SpecificationsField200Response isWizard(Boolean isWizard) {
    this.isWizard = isWizard;
    return this;
  }

  /**
   * Get isWizard
   * @return isWizard
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getIsWizard() {
    return isWizard;
  }

  @Deprecated
  public void setIsWizard(Boolean isWizard) {
    this.isWizard = isWizard;
  }


  public SpecificationsField200Response name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Specification field name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SpecificationsField200Response position(Integer position) {
    this.position = position;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal - This position number is used in ordering the specifications both in the navigation menu and in the specification listing on the product page.  
   * @return position
   */
  @javax.annotation.Nullable
  public Integer getPosition() {
    return position;
  }

  public void setPosition(Integer position) {
    this.position = position;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SpecificationsField200Response specificationsField200Response = (SpecificationsField200Response) o;
    return Objects.equals(this.defaultValue, specificationsField200Response.defaultValue) &&
        Objects.equals(this.description, specificationsField200Response.description) &&
        Objects.equals(this.fieldGroupId, specificationsField200Response.fieldGroupId) &&
        Objects.equals(this.fieldGroupName, specificationsField200Response.fieldGroupName) &&
        Objects.equals(this.fieldId, specificationsField200Response.fieldId) &&
        Objects.equals(this.fieldTypeId, specificationsField200Response.fieldTypeId) &&
        Objects.equals(this.fieldTypeName, specificationsField200Response.fieldTypeName) &&
        Objects.equals(this.fieldValueId, specificationsField200Response.fieldValueId) &&
        Objects.equals(this.isActive, specificationsField200Response.isActive) &&
        Objects.equals(this.isFilter, specificationsField200Response.isFilter) &&
        Objects.equals(this.isOnProductDetails, specificationsField200Response.isOnProductDetails) &&
        Objects.equals(this.isRequired, specificationsField200Response.isRequired) &&
        Objects.equals(this.isSideMenuLinkActive, specificationsField200Response.isSideMenuLinkActive) &&
        Objects.equals(this.isStockKeepingUnit, specificationsField200Response.isStockKeepingUnit) &&
        Objects.equals(this.isTopMenuLinkActive, specificationsField200Response.isTopMenuLinkActive) &&
        Objects.equals(this.isWizard, specificationsField200Response.isWizard) &&
        Objects.equals(this.name, specificationsField200Response.name) &&
        Objects.equals(this.position, specificationsField200Response.position);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(defaultValue, description, fieldGroupId, fieldGroupName, fieldId, fieldTypeId, fieldTypeName, fieldValueId, isActive, isFilter, isOnProductDetails, isRequired, isSideMenuLinkActive, isStockKeepingUnit, isTopMenuLinkActive, isWizard, name, position);
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
    sb.append("class SpecificationsField200Response {\n");
    sb.append("    defaultValue: ").append(toIndentedString(defaultValue)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    fieldGroupId: ").append(toIndentedString(fieldGroupId)).append("\n");
    sb.append("    fieldGroupName: ").append(toIndentedString(fieldGroupName)).append("\n");
    sb.append("    fieldId: ").append(toIndentedString(fieldId)).append("\n");
    sb.append("    fieldTypeId: ").append(toIndentedString(fieldTypeId)).append("\n");
    sb.append("    fieldTypeName: ").append(toIndentedString(fieldTypeName)).append("\n");
    sb.append("    fieldValueId: ").append(toIndentedString(fieldValueId)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isFilter: ").append(toIndentedString(isFilter)).append("\n");
    sb.append("    isOnProductDetails: ").append(toIndentedString(isOnProductDetails)).append("\n");
    sb.append("    isRequired: ").append(toIndentedString(isRequired)).append("\n");
    sb.append("    isSideMenuLinkActive: ").append(toIndentedString(isSideMenuLinkActive)).append("\n");
    sb.append("    isStockKeepingUnit: ").append(toIndentedString(isStockKeepingUnit)).append("\n");
    sb.append("    isTopMenuLinkActive: ").append(toIndentedString(isTopMenuLinkActive)).append("\n");
    sb.append("    isWizard: ").append(toIndentedString(isWizard)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
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
    openapiFields.add("DefaultValue");
    openapiFields.add("Description");
    openapiFields.add("FieldGroupId");
    openapiFields.add("FieldGroupName");
    openapiFields.add("FieldId");
    openapiFields.add("FieldTypeId");
    openapiFields.add("FieldTypeName");
    openapiFields.add("FieldValueId");
    openapiFields.add("IsActive");
    openapiFields.add("IsFilter");
    openapiFields.add("IsOnProductDetails");
    openapiFields.add("IsRequired");
    openapiFields.add("IsSideMenuLinkActive");
    openapiFields.add("IsStockKeepingUnit");
    openapiFields.add("IsTopMenuLinkActive");
    openapiFields.add("IsWizard");
    openapiFields.add("Name");
    openapiFields.add("Position");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SpecificationsField200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SpecificationsField200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SpecificationsField200Response is not found in the empty JSON string", SpecificationsField200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SpecificationsField200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SpecificationsField200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("DefaultValue") != null && !jsonObj.get("DefaultValue").isJsonNull()) && !jsonObj.get("DefaultValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DefaultValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DefaultValue").toString()));
      }
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("FieldGroupName") != null && !jsonObj.get("FieldGroupName").isJsonNull()) && !jsonObj.get("FieldGroupName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FieldGroupName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FieldGroupName").toString()));
      }
      if ((jsonObj.get("FieldTypeName") != null && !jsonObj.get("FieldTypeName").isJsonNull()) && !jsonObj.get("FieldTypeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FieldTypeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FieldTypeName").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SpecificationsField200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SpecificationsField200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SpecificationsField200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SpecificationsField200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<SpecificationsField200Response>() {
           @Override
           public void write(JsonWriter out, SpecificationsField200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SpecificationsField200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SpecificationsField200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SpecificationsField200Response
   * @throws IOException if the JSON string is invalid with respect to SpecificationsField200Response
   */
  public static SpecificationsField200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SpecificationsField200Response.class);
  }

  /**
   * Convert an instance of SpecificationsField200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

