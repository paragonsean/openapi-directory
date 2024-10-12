/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import org.openapitools.client.model.CatalogDataProductRenderButtonInterface;
import org.openapitools.client.model.CatalogDataProductRenderExtensionInterface;
import org.openapitools.client.model.CatalogDataProductRenderImageInterface;
import org.openapitools.client.model.CatalogDataProductRenderPriceInfoInterface;

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
 * Represents Data Object which holds enough information to render product This information is put into part as Add To Cart or Add to Compare Data or Price Data
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CatalogDataProductRenderInterface {
  public static final String SERIALIZED_NAME_ADD_TO_CART_BUTTON = "add_to_cart_button";
  @SerializedName(SERIALIZED_NAME_ADD_TO_CART_BUTTON)
  private CatalogDataProductRenderButtonInterface addToCartButton;

  public static final String SERIALIZED_NAME_ADD_TO_COMPARE_BUTTON = "add_to_compare_button";
  @SerializedName(SERIALIZED_NAME_ADD_TO_COMPARE_BUTTON)
  private CatalogDataProductRenderButtonInterface addToCompareButton;

  public static final String SERIALIZED_NAME_CURRENCY_CODE = "currency_code";
  @SerializedName(SERIALIZED_NAME_CURRENCY_CODE)
  private String currencyCode;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private CatalogDataProductRenderExtensionInterface extensionAttributes;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IMAGES = "images";
  @SerializedName(SERIALIZED_NAME_IMAGES)
  private List<CatalogDataProductRenderImageInterface> images = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_SALABLE = "is_salable";
  @SerializedName(SERIALIZED_NAME_IS_SALABLE)
  private String isSalable;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PRICE_INFO = "price_info";
  @SerializedName(SERIALIZED_NAME_PRICE_INFO)
  private CatalogDataProductRenderPriceInfoInterface priceInfo;

  public static final String SERIALIZED_NAME_STORE_ID = "store_id";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private Integer storeId;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public CatalogDataProductRenderInterface() {
  }

  public CatalogDataProductRenderInterface addToCartButton(CatalogDataProductRenderButtonInterface addToCartButton) {
    this.addToCartButton = addToCartButton;
    return this;
  }

  /**
   * Get addToCartButton
   * @return addToCartButton
   */
  @javax.annotation.Nonnull
  public CatalogDataProductRenderButtonInterface getAddToCartButton() {
    return addToCartButton;
  }

  public void setAddToCartButton(CatalogDataProductRenderButtonInterface addToCartButton) {
    this.addToCartButton = addToCartButton;
  }


  public CatalogDataProductRenderInterface addToCompareButton(CatalogDataProductRenderButtonInterface addToCompareButton) {
    this.addToCompareButton = addToCompareButton;
    return this;
  }

  /**
   * Get addToCompareButton
   * @return addToCompareButton
   */
  @javax.annotation.Nonnull
  public CatalogDataProductRenderButtonInterface getAddToCompareButton() {
    return addToCompareButton;
  }

  public void setAddToCompareButton(CatalogDataProductRenderButtonInterface addToCompareButton) {
    this.addToCompareButton = addToCompareButton;
  }


  public CatalogDataProductRenderInterface currencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
    return this;
  }

  /**
   * Current or desired currency code to product
   * @return currencyCode
   */
  @javax.annotation.Nonnull
  public String getCurrencyCode() {
    return currencyCode;
  }

  public void setCurrencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
  }


  public CatalogDataProductRenderInterface extensionAttributes(CatalogDataProductRenderExtensionInterface extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * Get extensionAttributes
   * @return extensionAttributes
   */
  @javax.annotation.Nonnull
  public CatalogDataProductRenderExtensionInterface getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(CatalogDataProductRenderExtensionInterface extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public CatalogDataProductRenderInterface id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Product identifier
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public CatalogDataProductRenderInterface images(List<CatalogDataProductRenderImageInterface> images) {
    this.images = images;
    return this;
  }

  public CatalogDataProductRenderInterface addImagesItem(CatalogDataProductRenderImageInterface imagesItem) {
    if (this.images == null) {
      this.images = new ArrayList<>();
    }
    this.images.add(imagesItem);
    return this;
  }

  /**
   * Enough information, that needed to render image on front
   * @return images
   */
  @javax.annotation.Nonnull
  public List<CatalogDataProductRenderImageInterface> getImages() {
    return images;
  }

  public void setImages(List<CatalogDataProductRenderImageInterface> images) {
    this.images = images;
  }


  public CatalogDataProductRenderInterface isSalable(String isSalable) {
    this.isSalable = isSalable;
    return this;
  }

  /**
   * Information about product saleability (In Stock)
   * @return isSalable
   */
  @javax.annotation.Nonnull
  public String getIsSalable() {
    return isSalable;
  }

  public void setIsSalable(String isSalable) {
    this.isSalable = isSalable;
  }


  public CatalogDataProductRenderInterface name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Product name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CatalogDataProductRenderInterface priceInfo(CatalogDataProductRenderPriceInfoInterface priceInfo) {
    this.priceInfo = priceInfo;
    return this;
  }

  /**
   * Get priceInfo
   * @return priceInfo
   */
  @javax.annotation.Nonnull
  public CatalogDataProductRenderPriceInfoInterface getPriceInfo() {
    return priceInfo;
  }

  public void setPriceInfo(CatalogDataProductRenderPriceInfoInterface priceInfo) {
    this.priceInfo = priceInfo;
  }


  public CatalogDataProductRenderInterface storeId(Integer storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * Information about current store id or requested store id
   * @return storeId
   */
  @javax.annotation.Nonnull
  public Integer getStoreId() {
    return storeId;
  }

  public void setStoreId(Integer storeId) {
    this.storeId = storeId;
  }


  public CatalogDataProductRenderInterface type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Product type. Such as bundle, grouped, simple, etc...
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public CatalogDataProductRenderInterface url(String url) {
    this.url = url;
    return this;
  }

  /**
   * Product url
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CatalogDataProductRenderInterface catalogDataProductRenderInterface = (CatalogDataProductRenderInterface) o;
    return Objects.equals(this.addToCartButton, catalogDataProductRenderInterface.addToCartButton) &&
        Objects.equals(this.addToCompareButton, catalogDataProductRenderInterface.addToCompareButton) &&
        Objects.equals(this.currencyCode, catalogDataProductRenderInterface.currencyCode) &&
        Objects.equals(this.extensionAttributes, catalogDataProductRenderInterface.extensionAttributes) &&
        Objects.equals(this.id, catalogDataProductRenderInterface.id) &&
        Objects.equals(this.images, catalogDataProductRenderInterface.images) &&
        Objects.equals(this.isSalable, catalogDataProductRenderInterface.isSalable) &&
        Objects.equals(this.name, catalogDataProductRenderInterface.name) &&
        Objects.equals(this.priceInfo, catalogDataProductRenderInterface.priceInfo) &&
        Objects.equals(this.storeId, catalogDataProductRenderInterface.storeId) &&
        Objects.equals(this.type, catalogDataProductRenderInterface.type) &&
        Objects.equals(this.url, catalogDataProductRenderInterface.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(addToCartButton, addToCompareButton, currencyCode, extensionAttributes, id, images, isSalable, name, priceInfo, storeId, type, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CatalogDataProductRenderInterface {\n");
    sb.append("    addToCartButton: ").append(toIndentedString(addToCartButton)).append("\n");
    sb.append("    addToCompareButton: ").append(toIndentedString(addToCompareButton)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    images: ").append(toIndentedString(images)).append("\n");
    sb.append("    isSalable: ").append(toIndentedString(isSalable)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    priceInfo: ").append(toIndentedString(priceInfo)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("add_to_cart_button");
    openapiFields.add("add_to_compare_button");
    openapiFields.add("currency_code");
    openapiFields.add("extension_attributes");
    openapiFields.add("id");
    openapiFields.add("images");
    openapiFields.add("is_salable");
    openapiFields.add("name");
    openapiFields.add("price_info");
    openapiFields.add("store_id");
    openapiFields.add("type");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("add_to_cart_button");
    openapiRequiredFields.add("add_to_compare_button");
    openapiRequiredFields.add("currency_code");
    openapiRequiredFields.add("extension_attributes");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("images");
    openapiRequiredFields.add("is_salable");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("price_info");
    openapiRequiredFields.add("store_id");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CatalogDataProductRenderInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CatalogDataProductRenderInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CatalogDataProductRenderInterface is not found in the empty JSON string", CatalogDataProductRenderInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CatalogDataProductRenderInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CatalogDataProductRenderInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CatalogDataProductRenderInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `add_to_cart_button`
      CatalogDataProductRenderButtonInterface.validateJsonElement(jsonObj.get("add_to_cart_button"));
      // validate the required field `add_to_compare_button`
      CatalogDataProductRenderButtonInterface.validateJsonElement(jsonObj.get("add_to_compare_button"));
      if (!jsonObj.get("currency_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency_code").toString()));
      }
      // validate the required field `extension_attributes`
      CatalogDataProductRenderExtensionInterface.validateJsonElement(jsonObj.get("extension_attributes"));
      // ensure the json data is an array
      if (!jsonObj.get("images").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `images` to be an array in the JSON string but got `%s`", jsonObj.get("images").toString()));
      }

      JsonArray jsonArrayimages = jsonObj.getAsJsonArray("images");
      // validate the required field `images` (array)
      for (int i = 0; i < jsonArrayimages.size(); i++) {
        CatalogDataProductRenderImageInterface.validateJsonElement(jsonArrayimages.get(i));
      };
      if (!jsonObj.get("is_salable").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_salable` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_salable").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the required field `price_info`
      CatalogDataProductRenderPriceInfoInterface.validateJsonElement(jsonObj.get("price_info"));
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CatalogDataProductRenderInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CatalogDataProductRenderInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CatalogDataProductRenderInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CatalogDataProductRenderInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<CatalogDataProductRenderInterface>() {
           @Override
           public void write(JsonWriter out, CatalogDataProductRenderInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CatalogDataProductRenderInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CatalogDataProductRenderInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CatalogDataProductRenderInterface
   * @throws IOException if the JSON string is invalid with respect to CatalogDataProductRenderInterface
   */
  public static CatalogDataProductRenderInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CatalogDataProductRenderInterface.class);
  }

  /**
   * Convert an instance of CatalogDataProductRenderInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

