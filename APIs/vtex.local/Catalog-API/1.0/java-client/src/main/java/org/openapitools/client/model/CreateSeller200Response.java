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
 * CreateSeller200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateSeller200Response {
  public static final String SERIALIZED_NAME_ARCHIVE_ID = "ArchiveId";
  @SerializedName(SERIALIZED_NAME_ARCHIVE_ID)
  private Integer archiveId;

  public static final String SERIALIZED_NAME_C_N_P_J = "CNPJ";
  @SerializedName(SERIALIZED_NAME_C_N_P_J)
  private String CNPJ;

  public static final String SERIALIZED_NAME_CS_C_IDENTIFICATION = "CSCIdentification";
  @SerializedName(SERIALIZED_NAME_CS_C_IDENTIFICATION)
  private String csCIdentification;

  public static final String SERIALIZED_NAME_CATALOG_SYSTEM_ENDPOINT = "CatalogSystemEndpoint";
  @SerializedName(SERIALIZED_NAME_CATALOG_SYSTEM_ENDPOINT)
  private String catalogSystemEndpoint;

  public static final String SERIALIZED_NAME_CATEGORY_COMMISSION_PERCENTAGE = "CategoryCommissionPercentage";
  @SerializedName(SERIALIZED_NAME_CATEGORY_COMMISSION_PERCENTAGE)
  private String categoryCommissionPercentage;

  public static final String SERIALIZED_NAME_DELIVERY_POLICY = "DeliveryPolicy";
  @SerializedName(SERIALIZED_NAME_DELIVERY_POLICY)
  private String deliveryPolicy;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EMAIL = "Email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_EXCHANGE_RETURN_POLICY = "ExchangeReturnPolicy";
  @SerializedName(SERIALIZED_NAME_EXCHANGE_RETURN_POLICY)
  private String exchangeReturnPolicy;

  public static final String SERIALIZED_NAME_FREIGHT_COMMISSION_PERCENTAGE = "FreightCommissionPercentage";
  @SerializedName(SERIALIZED_NAME_FREIGHT_COMMISSION_PERCENTAGE)
  private BigDecimal freightCommissionPercentage;

  public static final String SERIALIZED_NAME_FULFILLMENT_ENDPOINT = "FulfillmentEndpoint";
  @SerializedName(SERIALIZED_NAME_FULFILLMENT_ENDPOINT)
  private String fulfillmentEndpoint;

  public static final String SERIALIZED_NAME_FULFILLMENT_SELLER_ID = "FulfillmentSellerId";
  @SerializedName(SERIALIZED_NAME_FULFILLMENT_SELLER_ID)
  private Integer fulfillmentSellerId;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_BETTER_SCOPE = "IsBetterScope";
  @SerializedName(SERIALIZED_NAME_IS_BETTER_SCOPE)
  private Boolean isBetterScope;

  public static final String SERIALIZED_NAME_MERCHANT_NAME = "MerchantName";
  @SerializedName(SERIALIZED_NAME_MERCHANT_NAME)
  private String merchantName;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PASSWORD = "Password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  public static final String SERIALIZED_NAME_PRODUCT_COMMISSION_PERCENTAGE = "ProductCommissionPercentage";
  @SerializedName(SERIALIZED_NAME_PRODUCT_COMMISSION_PERCENTAGE)
  private BigDecimal productCommissionPercentage;

  public static final String SERIALIZED_NAME_SECUTITY_PRIVACY_POLICY = "SecutityPrivacyPolicy";
  @SerializedName(SERIALIZED_NAME_SECUTITY_PRIVACY_POLICY)
  private String secutityPrivacyPolicy;

  public static final String SERIALIZED_NAME_SELLER_ID = "SellerId";
  @SerializedName(SERIALIZED_NAME_SELLER_ID)
  private String sellerId;

  public static final String SERIALIZED_NAME_SELLER_TYPE = "SellerType";
  @SerializedName(SERIALIZED_NAME_SELLER_TYPE)
  private Integer sellerType;

  public static final String SERIALIZED_NAME_TRUST_POLICY = "TrustPolicy";
  @SerializedName(SERIALIZED_NAME_TRUST_POLICY)
  private String trustPolicy;

  public static final String SERIALIZED_NAME_URL_LOGO = "UrlLogo";
  @SerializedName(SERIALIZED_NAME_URL_LOGO)
  private String urlLogo;

  public static final String SERIALIZED_NAME_USE_HYBRID_PAYMENT_OPTIONS = "UseHybridPaymentOptions";
  @SerializedName(SERIALIZED_NAME_USE_HYBRID_PAYMENT_OPTIONS)
  private Boolean useHybridPaymentOptions;

  public static final String SERIALIZED_NAME_USER_NAME = "UserName";
  @SerializedName(SERIALIZED_NAME_USER_NAME)
  private String userName;

  public CreateSeller200Response() {
  }

  public CreateSeller200Response archiveId(Integer archiveId) {
    this.archiveId = archiveId;
    return this;
  }

  /**
   * Seller archive ID.
   * @return archiveId
   */
  @javax.annotation.Nullable
  public Integer getArchiveId() {
    return archiveId;
  }

  public void setArchiveId(Integer archiveId) {
    this.archiveId = archiveId;
  }


  public CreateSeller200Response CNPJ(String CNPJ) {
    this.CNPJ = CNPJ;
    return this;
  }

  /**
   * Company registration number.
   * @return CNPJ
   */
  @javax.annotation.Nullable
  public String getCNPJ() {
    return CNPJ;
  }

  public void setCNPJ(String CNPJ) {
    this.CNPJ = CNPJ;
  }


  public CreateSeller200Response csCIdentification(String csCIdentification) {
    this.csCIdentification = csCIdentification;
    return this;
  }

  /**
   * CSC identification.
   * @return csCIdentification
   */
  @javax.annotation.Nullable
  public String getCsCIdentification() {
    return csCIdentification;
  }

  public void setCsCIdentification(String csCIdentification) {
    this.csCIdentification = csCIdentification;
  }


  public CreateSeller200Response catalogSystemEndpoint(String catalogSystemEndpoint) {
    this.catalogSystemEndpoint = catalogSystemEndpoint;
    return this;
  }

  /**
   * URL of the endpoint of the seller&#39;s catalog. This field will only be displayed if the seller type is VTEX Store. The field format will be as follows: &#x60;http://{sellerName}.vtexcommercestable.com.br/api/catalog_system/&#x60;.
   * @return catalogSystemEndpoint
   */
  @javax.annotation.Nullable
  public String getCatalogSystemEndpoint() {
    return catalogSystemEndpoint;
  }

  public void setCatalogSystemEndpoint(String catalogSystemEndpoint) {
    this.catalogSystemEndpoint = catalogSystemEndpoint;
  }


  public CreateSeller200Response categoryCommissionPercentage(String categoryCommissionPercentage) {
    this.categoryCommissionPercentage = categoryCommissionPercentage;
    return this;
  }

  /**
   * The percentage that must be filled in as agreed between the marketplace and the seller. If there is no such commission, please fill in the field with the value: &#x60;0.00&#x60;.
   * @return categoryCommissionPercentage
   */
  @javax.annotation.Nullable
  public String getCategoryCommissionPercentage() {
    return categoryCommissionPercentage;
  }

  public void setCategoryCommissionPercentage(String categoryCommissionPercentage) {
    this.categoryCommissionPercentage = categoryCommissionPercentage;
  }


  public CreateSeller200Response deliveryPolicy(String deliveryPolicy) {
    this.deliveryPolicy = deliveryPolicy;
    return this;
  }

  /**
   * Text describing the delivery policy previously agreed between the marketplace and the seller.
   * @return deliveryPolicy
   */
  @javax.annotation.Nullable
  public String getDeliveryPolicy() {
    return deliveryPolicy;
  }

  public void setDeliveryPolicy(String deliveryPolicy) {
    this.deliveryPolicy = deliveryPolicy;
  }


  public CreateSeller200Response description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Text describing the seller with a marketing tone. You can display this text in the marketplace window display by [customizing the CMS](https://help.vtex.com/en/tutorial/list-of-controls-for-templates--tutorials_563).
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public CreateSeller200Response email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Email of the admin responsible for the seller. 
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public CreateSeller200Response exchangeReturnPolicy(String exchangeReturnPolicy) {
    this.exchangeReturnPolicy = exchangeReturnPolicy;
    return this;
  }

  /**
   * Text describing the exchange and return policy previously agreed between the marketplace and the seller.
   * @return exchangeReturnPolicy
   */
  @javax.annotation.Nullable
  public String getExchangeReturnPolicy() {
    return exchangeReturnPolicy;
  }

  public void setExchangeReturnPolicy(String exchangeReturnPolicy) {
    this.exchangeReturnPolicy = exchangeReturnPolicy;
  }


  public CreateSeller200Response freightCommissionPercentage(BigDecimal freightCommissionPercentage) {
    this.freightCommissionPercentage = freightCommissionPercentage;
    return this;
  }

  /**
   * The percentage that must be filled in as agreed between the marketplace and the seller. If there is no such commission, please fill in the field with the value: &#x60;0.00&#x60;.
   * @return freightCommissionPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getFreightCommissionPercentage() {
    return freightCommissionPercentage;
  }

  public void setFreightCommissionPercentage(BigDecimal freightCommissionPercentage) {
    this.freightCommissionPercentage = freightCommissionPercentage;
  }


  public CreateSeller200Response fulfillmentEndpoint(String fulfillmentEndpoint) {
    this.fulfillmentEndpoint = fulfillmentEndpoint;
    return this;
  }

  /**
   * URL of the endpoint for fulfillment of seller&#39;s orders, which the marketplace will use to communicate with the seller. This field applies to all sellers, regardless of their type. However, for &#x60;VTEX Stores&#x60;, you don’t need to fill it in because the system will do that automatically. You can edit this field once the seller has been successfully added.
   * @return fulfillmentEndpoint
   */
  @javax.annotation.Nullable
  public String getFulfillmentEndpoint() {
    return fulfillmentEndpoint;
  }

  public void setFulfillmentEndpoint(String fulfillmentEndpoint) {
    this.fulfillmentEndpoint = fulfillmentEndpoint;
  }


  public CreateSeller200Response fulfillmentSellerId(Integer fulfillmentSellerId) {
    this.fulfillmentSellerId = fulfillmentSellerId;
    return this;
  }

  /**
   * Identification code of the seller responsible for fulfilling the order. This is an optional field used when a seller sells SKUs from another seller. If the seller sells their own SKUs, it must be left blank.
   * @return fulfillmentSellerId
   */
  @javax.annotation.Nullable
  public Integer getFulfillmentSellerId() {
    return fulfillmentSellerId;
  }

  public void setFulfillmentSellerId(Integer fulfillmentSellerId) {
    this.fulfillmentSellerId = fulfillmentSellerId;
  }


  public CreateSeller200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * If the selle is active (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public CreateSeller200Response isBetterScope(Boolean isBetterScope) {
    this.isBetterScope = isBetterScope;
    return this;
  }

  /**
   * Indicates whether it is a [comprehensive seller](https://help.vtex.com/en/tutorial/comprehensive-seller--5Qn4O2GpjUIzWTPpvLUfkI).
   * @return isBetterScope
   */
  @javax.annotation.Nullable
  public Boolean getIsBetterScope() {
    return isBetterScope;
  }

  public void setIsBetterScope(Boolean isBetterScope) {
    this.isBetterScope = isBetterScope;
  }


  public CreateSeller200Response merchantName(String merchantName) {
    this.merchantName = merchantName;
    return this;
  }

  /**
   * Name of the marketplace, used to guide payments. This field should be nulled if the marketplace is responsible for processing payments. Check out our [Split Payment](https://help.vtex.com/en/tutorial/split-de-pagamento--6k5JidhYRUxileNolY2VLx) article to know more.
   * @return merchantName
   */
  @javax.annotation.Nullable
  public String getMerchantName() {
    return merchantName;
  }

  public void setMerchantName(String merchantName) {
    this.merchantName = merchantName;
  }


  public CreateSeller200Response name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the account in the seller&#39;s environment. You can find it on **Account settings &gt; Account &gt; Account Name**). Applicable only if the seller uses their own payment method.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateSeller200Response password(String password) {
    this.password = password;
    return this;
  }

  /**
   * Seller password.
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public CreateSeller200Response productCommissionPercentage(BigDecimal productCommissionPercentage) {
    this.productCommissionPercentage = productCommissionPercentage;
    return this;
  }

  /**
   * The percentage that must be filled in as agreed between the marketplace and the seller. If there is no such commission, please fill in the field with the value: &#x60;0.00&#x60;.
   * @return productCommissionPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getProductCommissionPercentage() {
    return productCommissionPercentage;
  }

  public void setProductCommissionPercentage(BigDecimal productCommissionPercentage) {
    this.productCommissionPercentage = productCommissionPercentage;
  }


  public CreateSeller200Response secutityPrivacyPolicy(String secutityPrivacyPolicy) {
    this.secutityPrivacyPolicy = secutityPrivacyPolicy;
    return this;
  }

  /**
   * Text describing the security policy previously agreed between the marketplace and the seller.
   * @return secutityPrivacyPolicy
   */
  @javax.annotation.Nullable
  public String getSecutityPrivacyPolicy() {
    return secutityPrivacyPolicy;
  }

  public void setSecutityPrivacyPolicy(String secutityPrivacyPolicy) {
    this.secutityPrivacyPolicy = secutityPrivacyPolicy;
  }


  public CreateSeller200Response sellerId(String sellerId) {
    this.sellerId = sellerId;
    return this;
  }

  /**
   * Code used to identify the seller. It is assigned by the marketplace. We recommend filling it in with the seller&#39;s account name.
   * @return sellerId
   */
  @javax.annotation.Nullable
  public String getSellerId() {
    return sellerId;
  }

  public void setSellerId(String sellerId) {
    this.sellerId = sellerId;
  }


  public CreateSeller200Response sellerType(Integer sellerType) {
    this.sellerType = sellerType;
    return this;
  }

  /**
   * Seller type.
   * @return sellerType
   */
  @javax.annotation.Nullable
  public Integer getSellerType() {
    return sellerType;
  }

  public void setSellerType(Integer sellerType) {
    this.sellerType = sellerType;
  }


  public CreateSeller200Response trustPolicy(String trustPolicy) {
    this.trustPolicy = trustPolicy;
    return this;
  }

  /**
   * Seller trust policy. The default value is &#x60;&#39;Default&#39;&#x60;, but if your store is a B2B marketplace and you want to share the customers&#39;emails with the sellers you need to set this field as &#x60;&#39;AllowEmailSharing&#39;&#x60;.
   * @return trustPolicy
   */
  @javax.annotation.Nullable
  public String getTrustPolicy() {
    return trustPolicy;
  }

  public void setTrustPolicy(String trustPolicy) {
    this.trustPolicy = trustPolicy;
  }


  public CreateSeller200Response urlLogo(String urlLogo) {
    this.urlLogo = urlLogo;
    return this;
  }

  /**
   * Seller URL logo.
   * @return urlLogo
   */
  @javax.annotation.Nullable
  public String getUrlLogo() {
    return urlLogo;
  }

  public void setUrlLogo(String urlLogo) {
    this.urlLogo = urlLogo;
  }


  public CreateSeller200Response useHybridPaymentOptions(Boolean useHybridPaymentOptions) {
    this.useHybridPaymentOptions = useHybridPaymentOptions;
    return this;
  }

  /**
   * Allows customers to use gift cards from the seller to buy their products on the marketplace. It identifies purchases made with a gift card so that only the final price (with discounts applied) is paid to the seller. 
   * @return useHybridPaymentOptions
   */
  @javax.annotation.Nullable
  public Boolean getUseHybridPaymentOptions() {
    return useHybridPaymentOptions;
  }

  public void setUseHybridPaymentOptions(Boolean useHybridPaymentOptions) {
    this.useHybridPaymentOptions = useHybridPaymentOptions;
  }


  public CreateSeller200Response userName(String userName) {
    this.userName = userName;
    return this;
  }

  /**
   * Seller username.
   * @return userName
   */
  @javax.annotation.Nullable
  public String getUserName() {
    return userName;
  }

  public void setUserName(String userName) {
    this.userName = userName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateSeller200Response createSeller200Response = (CreateSeller200Response) o;
    return Objects.equals(this.archiveId, createSeller200Response.archiveId) &&
        Objects.equals(this.CNPJ, createSeller200Response.CNPJ) &&
        Objects.equals(this.csCIdentification, createSeller200Response.csCIdentification) &&
        Objects.equals(this.catalogSystemEndpoint, createSeller200Response.catalogSystemEndpoint) &&
        Objects.equals(this.categoryCommissionPercentage, createSeller200Response.categoryCommissionPercentage) &&
        Objects.equals(this.deliveryPolicy, createSeller200Response.deliveryPolicy) &&
        Objects.equals(this.description, createSeller200Response.description) &&
        Objects.equals(this.email, createSeller200Response.email) &&
        Objects.equals(this.exchangeReturnPolicy, createSeller200Response.exchangeReturnPolicy) &&
        Objects.equals(this.freightCommissionPercentage, createSeller200Response.freightCommissionPercentage) &&
        Objects.equals(this.fulfillmentEndpoint, createSeller200Response.fulfillmentEndpoint) &&
        Objects.equals(this.fulfillmentSellerId, createSeller200Response.fulfillmentSellerId) &&
        Objects.equals(this.isActive, createSeller200Response.isActive) &&
        Objects.equals(this.isBetterScope, createSeller200Response.isBetterScope) &&
        Objects.equals(this.merchantName, createSeller200Response.merchantName) &&
        Objects.equals(this.name, createSeller200Response.name) &&
        Objects.equals(this.password, createSeller200Response.password) &&
        Objects.equals(this.productCommissionPercentage, createSeller200Response.productCommissionPercentage) &&
        Objects.equals(this.secutityPrivacyPolicy, createSeller200Response.secutityPrivacyPolicy) &&
        Objects.equals(this.sellerId, createSeller200Response.sellerId) &&
        Objects.equals(this.sellerType, createSeller200Response.sellerType) &&
        Objects.equals(this.trustPolicy, createSeller200Response.trustPolicy) &&
        Objects.equals(this.urlLogo, createSeller200Response.urlLogo) &&
        Objects.equals(this.useHybridPaymentOptions, createSeller200Response.useHybridPaymentOptions) &&
        Objects.equals(this.userName, createSeller200Response.userName);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(archiveId, CNPJ, csCIdentification, catalogSystemEndpoint, categoryCommissionPercentage, deliveryPolicy, description, email, exchangeReturnPolicy, freightCommissionPercentage, fulfillmentEndpoint, fulfillmentSellerId, isActive, isBetterScope, merchantName, name, password, productCommissionPercentage, secutityPrivacyPolicy, sellerId, sellerType, trustPolicy, urlLogo, useHybridPaymentOptions, userName);
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
    sb.append("class CreateSeller200Response {\n");
    sb.append("    archiveId: ").append(toIndentedString(archiveId)).append("\n");
    sb.append("    CNPJ: ").append(toIndentedString(CNPJ)).append("\n");
    sb.append("    csCIdentification: ").append(toIndentedString(csCIdentification)).append("\n");
    sb.append("    catalogSystemEndpoint: ").append(toIndentedString(catalogSystemEndpoint)).append("\n");
    sb.append("    categoryCommissionPercentage: ").append(toIndentedString(categoryCommissionPercentage)).append("\n");
    sb.append("    deliveryPolicy: ").append(toIndentedString(deliveryPolicy)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    exchangeReturnPolicy: ").append(toIndentedString(exchangeReturnPolicy)).append("\n");
    sb.append("    freightCommissionPercentage: ").append(toIndentedString(freightCommissionPercentage)).append("\n");
    sb.append("    fulfillmentEndpoint: ").append(toIndentedString(fulfillmentEndpoint)).append("\n");
    sb.append("    fulfillmentSellerId: ").append(toIndentedString(fulfillmentSellerId)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isBetterScope: ").append(toIndentedString(isBetterScope)).append("\n");
    sb.append("    merchantName: ").append(toIndentedString(merchantName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    productCommissionPercentage: ").append(toIndentedString(productCommissionPercentage)).append("\n");
    sb.append("    secutityPrivacyPolicy: ").append(toIndentedString(secutityPrivacyPolicy)).append("\n");
    sb.append("    sellerId: ").append(toIndentedString(sellerId)).append("\n");
    sb.append("    sellerType: ").append(toIndentedString(sellerType)).append("\n");
    sb.append("    trustPolicy: ").append(toIndentedString(trustPolicy)).append("\n");
    sb.append("    urlLogo: ").append(toIndentedString(urlLogo)).append("\n");
    sb.append("    useHybridPaymentOptions: ").append(toIndentedString(useHybridPaymentOptions)).append("\n");
    sb.append("    userName: ").append(toIndentedString(userName)).append("\n");
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
    openapiFields.add("ArchiveId");
    openapiFields.add("CNPJ");
    openapiFields.add("CSCIdentification");
    openapiFields.add("CatalogSystemEndpoint");
    openapiFields.add("CategoryCommissionPercentage");
    openapiFields.add("DeliveryPolicy");
    openapiFields.add("Description");
    openapiFields.add("Email");
    openapiFields.add("ExchangeReturnPolicy");
    openapiFields.add("FreightCommissionPercentage");
    openapiFields.add("FulfillmentEndpoint");
    openapiFields.add("FulfillmentSellerId");
    openapiFields.add("IsActive");
    openapiFields.add("IsBetterScope");
    openapiFields.add("MerchantName");
    openapiFields.add("Name");
    openapiFields.add("Password");
    openapiFields.add("ProductCommissionPercentage");
    openapiFields.add("SecutityPrivacyPolicy");
    openapiFields.add("SellerId");
    openapiFields.add("SellerType");
    openapiFields.add("TrustPolicy");
    openapiFields.add("UrlLogo");
    openapiFields.add("UseHybridPaymentOptions");
    openapiFields.add("UserName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateSeller200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateSeller200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateSeller200Response is not found in the empty JSON string", CreateSeller200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateSeller200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateSeller200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("CNPJ") != null && !jsonObj.get("CNPJ").isJsonNull()) && !jsonObj.get("CNPJ").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CNPJ` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CNPJ").toString()));
      }
      if ((jsonObj.get("CSCIdentification") != null && !jsonObj.get("CSCIdentification").isJsonNull()) && !jsonObj.get("CSCIdentification").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CSCIdentification` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CSCIdentification").toString()));
      }
      if ((jsonObj.get("CatalogSystemEndpoint") != null && !jsonObj.get("CatalogSystemEndpoint").isJsonNull()) && !jsonObj.get("CatalogSystemEndpoint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CatalogSystemEndpoint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CatalogSystemEndpoint").toString()));
      }
      if ((jsonObj.get("CategoryCommissionPercentage") != null && !jsonObj.get("CategoryCommissionPercentage").isJsonNull()) && !jsonObj.get("CategoryCommissionPercentage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CategoryCommissionPercentage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CategoryCommissionPercentage").toString()));
      }
      if ((jsonObj.get("DeliveryPolicy") != null && !jsonObj.get("DeliveryPolicy").isJsonNull()) && !jsonObj.get("DeliveryPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DeliveryPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DeliveryPolicy").toString()));
      }
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("Email") != null && !jsonObj.get("Email").isJsonNull()) && !jsonObj.get("Email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Email").toString()));
      }
      if ((jsonObj.get("ExchangeReturnPolicy") != null && !jsonObj.get("ExchangeReturnPolicy").isJsonNull()) && !jsonObj.get("ExchangeReturnPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ExchangeReturnPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ExchangeReturnPolicy").toString()));
      }
      if ((jsonObj.get("FulfillmentEndpoint") != null && !jsonObj.get("FulfillmentEndpoint").isJsonNull()) && !jsonObj.get("FulfillmentEndpoint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FulfillmentEndpoint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FulfillmentEndpoint").toString()));
      }
      if ((jsonObj.get("MerchantName") != null && !jsonObj.get("MerchantName").isJsonNull()) && !jsonObj.get("MerchantName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MerchantName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MerchantName").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Password") != null && !jsonObj.get("Password").isJsonNull()) && !jsonObj.get("Password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Password").toString()));
      }
      if ((jsonObj.get("SecutityPrivacyPolicy") != null && !jsonObj.get("SecutityPrivacyPolicy").isJsonNull()) && !jsonObj.get("SecutityPrivacyPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SecutityPrivacyPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SecutityPrivacyPolicy").toString()));
      }
      if ((jsonObj.get("SellerId") != null && !jsonObj.get("SellerId").isJsonNull()) && !jsonObj.get("SellerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SellerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SellerId").toString()));
      }
      if ((jsonObj.get("TrustPolicy") != null && !jsonObj.get("TrustPolicy").isJsonNull()) && !jsonObj.get("TrustPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TrustPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TrustPolicy").toString()));
      }
      if ((jsonObj.get("UrlLogo") != null && !jsonObj.get("UrlLogo").isJsonNull()) && !jsonObj.get("UrlLogo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `UrlLogo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("UrlLogo").toString()));
      }
      if ((jsonObj.get("UserName") != null && !jsonObj.get("UserName").isJsonNull()) && !jsonObj.get("UserName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `UserName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("UserName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateSeller200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateSeller200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateSeller200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateSeller200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateSeller200Response>() {
           @Override
           public void write(JsonWriter out, CreateSeller200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateSeller200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateSeller200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateSeller200Response
   * @throws IOException if the JSON string is invalid with respect to CreateSeller200Response
   */
  public static CreateSeller200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateSeller200Response.class);
  }

  /**
   * Convert an instance of CreateSeller200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

