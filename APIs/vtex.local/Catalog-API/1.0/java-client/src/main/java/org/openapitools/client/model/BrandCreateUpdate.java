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
 * Object containing Brand information.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BrandCreateUpdate {
  public static final String SERIALIZED_NAME_ACTIVE = "Active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_AD_WORDS_REMARKETING_CODE = "AdWordsRemarketingCode";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_AD_WORDS_REMARKETING_CODE)
  private String adWordsRemarketingCode;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_KEYWORDS = "Keywords";
  @SerializedName(SERIALIZED_NAME_KEYWORDS)
  private String keywords;

  public static final String SERIALIZED_NAME_LINK_ID = "LinkId";
  @SerializedName(SERIALIZED_NAME_LINK_ID)
  private String linkId;

  public static final String SERIALIZED_NAME_LOMADEE_CAMPAIGN_CODE = "LomadeeCampaignCode";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_LOMADEE_CAMPAIGN_CODE)
  private String lomadeeCampaignCode;

  public static final String SERIALIZED_NAME_MENU_HOME = "MenuHome";
  @SerializedName(SERIALIZED_NAME_MENU_HOME)
  private Boolean menuHome;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SCORE = "Score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Integer score;

  public static final String SERIALIZED_NAME_SITE_TITLE = "SiteTitle";
  @SerializedName(SERIALIZED_NAME_SITE_TITLE)
  private String siteTitle;

  public static final String SERIALIZED_NAME_TEXT = "Text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public BrandCreateUpdate() {
  }

  public BrandCreateUpdate active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * Defines if the brand is active (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return active
   */
  @javax.annotation.Nullable
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  @Deprecated
  public BrandCreateUpdate adWordsRemarketingCode(String adWordsRemarketingCode) {
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


  public BrandCreateUpdate id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Brand&#39;s unique numerical identifier.
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public BrandCreateUpdate keywords(String keywords) {
    this.keywords = keywords;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal - Alternative search terms that will lead to the specific brand. The user can find the desired brand even when misspelling it. Used especially when words are of foreign origin and have a distinct spelling that is transcribed into a generic one, or when small spelling mistakes occur.  
   * @return keywords
   */
  @javax.annotation.Nullable
  public String getKeywords() {
    return keywords;
  }

  public void setKeywords(String keywords) {
    this.keywords = keywords;
  }


  public BrandCreateUpdate linkId(String linkId) {
    this.linkId = linkId;
    return this;
  }

  /**
   * Brand page slug. Only lowercase letters and hyphens (&#x60;-&#x60;) are allowed.
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
  public BrandCreateUpdate lomadeeCampaignCode(String lomadeeCampaignCode) {
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


  public BrandCreateUpdate menuHome(Boolean menuHome) {
    this.menuHome = menuHome;
    return this;
  }

  /**
   * Store Framework - Deprecated.  Legacy CMS Portal - Defines if the Brand appears in the Department Menu control (&#x60;&lt;vtex.cmc:departmentNavigator/&gt;&#x60;).  
   * @return menuHome
   */
  @javax.annotation.Nullable
  public Boolean getMenuHome() {
    return menuHome;
  }

  public void setMenuHome(Boolean menuHome) {
    this.menuHome = menuHome;
  }


  public BrandCreateUpdate name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Brand name.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public BrandCreateUpdate score(Integer score) {
    this.score = score;
    return this;
  }

  /**
   * Store Framework - Deprecated  Legacy CMS Portal - Value used to set the priority on the search result page.  
   * @return score
   */
  @javax.annotation.Nullable
  public Integer getScore() {
    return score;
  }

  public void setScore(Integer score) {
    this.score = score;
  }


  public BrandCreateUpdate siteTitle(String siteTitle) {
    this.siteTitle = siteTitle;
    return this;
  }

  /**
   * Meta Title for the Brand page.
   * @return siteTitle
   */
  @javax.annotation.Nullable
  public String getSiteTitle() {
    return siteTitle;
  }

  public void setSiteTitle(String siteTitle) {
    this.siteTitle = siteTitle;
  }


  public BrandCreateUpdate text(String text) {
    this.text = text;
    return this;
  }

  /**
   * Meta Description for the Brand page. A brief description of the brand, displayed by search engines. Since search engines can only display less than 150 characters, we recommend not exceeding this character limit when creating the description.
   * @return text
   */
  @javax.annotation.Nullable
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BrandCreateUpdate brandCreateUpdate = (BrandCreateUpdate) o;
    return Objects.equals(this.active, brandCreateUpdate.active) &&
        Objects.equals(this.adWordsRemarketingCode, brandCreateUpdate.adWordsRemarketingCode) &&
        Objects.equals(this.id, brandCreateUpdate.id) &&
        Objects.equals(this.keywords, brandCreateUpdate.keywords) &&
        Objects.equals(this.linkId, brandCreateUpdate.linkId) &&
        Objects.equals(this.lomadeeCampaignCode, brandCreateUpdate.lomadeeCampaignCode) &&
        Objects.equals(this.menuHome, brandCreateUpdate.menuHome) &&
        Objects.equals(this.name, brandCreateUpdate.name) &&
        Objects.equals(this.score, brandCreateUpdate.score) &&
        Objects.equals(this.siteTitle, brandCreateUpdate.siteTitle) &&
        Objects.equals(this.text, brandCreateUpdate.text);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, adWordsRemarketingCode, id, keywords, linkId, lomadeeCampaignCode, menuHome, name, score, siteTitle, text);
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
    sb.append("class BrandCreateUpdate {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    adWordsRemarketingCode: ").append(toIndentedString(adWordsRemarketingCode)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    keywords: ").append(toIndentedString(keywords)).append("\n");
    sb.append("    linkId: ").append(toIndentedString(linkId)).append("\n");
    sb.append("    lomadeeCampaignCode: ").append(toIndentedString(lomadeeCampaignCode)).append("\n");
    sb.append("    menuHome: ").append(toIndentedString(menuHome)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    siteTitle: ").append(toIndentedString(siteTitle)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
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
    openapiFields.add("Active");
    openapiFields.add("AdWordsRemarketingCode");
    openapiFields.add("Id");
    openapiFields.add("Keywords");
    openapiFields.add("LinkId");
    openapiFields.add("LomadeeCampaignCode");
    openapiFields.add("MenuHome");
    openapiFields.add("Name");
    openapiFields.add("Score");
    openapiFields.add("SiteTitle");
    openapiFields.add("Text");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("Id");
    openapiRequiredFields.add("Name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BrandCreateUpdate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BrandCreateUpdate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BrandCreateUpdate is not found in the empty JSON string", BrandCreateUpdate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BrandCreateUpdate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BrandCreateUpdate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BrandCreateUpdate.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AdWordsRemarketingCode") != null && !jsonObj.get("AdWordsRemarketingCode").isJsonNull()) && !jsonObj.get("AdWordsRemarketingCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AdWordsRemarketingCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AdWordsRemarketingCode").toString()));
      }
      if ((jsonObj.get("Keywords") != null && !jsonObj.get("Keywords").isJsonNull()) && !jsonObj.get("Keywords").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Keywords` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Keywords").toString()));
      }
      if ((jsonObj.get("LinkId") != null && !jsonObj.get("LinkId").isJsonNull()) && !jsonObj.get("LinkId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LinkId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LinkId").toString()));
      }
      if ((jsonObj.get("LomadeeCampaignCode") != null && !jsonObj.get("LomadeeCampaignCode").isJsonNull()) && !jsonObj.get("LomadeeCampaignCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LomadeeCampaignCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LomadeeCampaignCode").toString()));
      }
      if (!jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("SiteTitle") != null && !jsonObj.get("SiteTitle").isJsonNull()) && !jsonObj.get("SiteTitle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SiteTitle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SiteTitle").toString()));
      }
      if ((jsonObj.get("Text") != null && !jsonObj.get("Text").isJsonNull()) && !jsonObj.get("Text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Text").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BrandCreateUpdate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BrandCreateUpdate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BrandCreateUpdate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BrandCreateUpdate.class));

       return (TypeAdapter<T>) new TypeAdapter<BrandCreateUpdate>() {
           @Override
           public void write(JsonWriter out, BrandCreateUpdate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BrandCreateUpdate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BrandCreateUpdate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BrandCreateUpdate
   * @throws IOException if the JSON string is invalid with respect to BrandCreateUpdate
   */
  public static BrandCreateUpdate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BrandCreateUpdate.class);
  }

  /**
   * Convert an instance of BrandCreateUpdate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

