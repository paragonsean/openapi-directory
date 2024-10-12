/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
 * ProductAttributeValueSet200ResponseResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductAttributeValueSet200ResponseResult {
  public static final String SERIALIZED_NAME_ATTRIBUTE_ID = "attribute_id";
  @SerializedName(SERIALIZED_NAME_ATTRIBUTE_ID)
  private String attributeId;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "product_id";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private String productId;

  public static final String SERIALIZED_NAME_VALUE_ID = "value_id";
  @SerializedName(SERIALIZED_NAME_VALUE_ID)
  private String valueId;

  public ProductAttributeValueSet200ResponseResult() {
  }

  public ProductAttributeValueSet200ResponseResult attributeId(String attributeId) {
    this.attributeId = attributeId;
    return this;
  }

  /**
   * Get attributeId
   * @return attributeId
   */
  @javax.annotation.Nullable
  public String getAttributeId() {
    return attributeId;
  }

  public void setAttributeId(String attributeId) {
    this.attributeId = attributeId;
  }


  public ProductAttributeValueSet200ResponseResult productId(String productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Get productId
   * @return productId
   */
  @javax.annotation.Nullable
  public String getProductId() {
    return productId;
  }

  public void setProductId(String productId) {
    this.productId = productId;
  }


  public ProductAttributeValueSet200ResponseResult valueId(String valueId) {
    this.valueId = valueId;
    return this;
  }

  /**
   * Get valueId
   * @return valueId
   */
  @javax.annotation.Nullable
  public String getValueId() {
    return valueId;
  }

  public void setValueId(String valueId) {
    this.valueId = valueId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProductAttributeValueSet200ResponseResult productAttributeValueSet200ResponseResult = (ProductAttributeValueSet200ResponseResult) o;
    return Objects.equals(this.attributeId, productAttributeValueSet200ResponseResult.attributeId) &&
        Objects.equals(this.productId, productAttributeValueSet200ResponseResult.productId) &&
        Objects.equals(this.valueId, productAttributeValueSet200ResponseResult.valueId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(attributeId, productId, valueId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProductAttributeValueSet200ResponseResult {\n");
    sb.append("    attributeId: ").append(toIndentedString(attributeId)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    valueId: ").append(toIndentedString(valueId)).append("\n");
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
    openapiFields.add("attribute_id");
    openapiFields.add("product_id");
    openapiFields.add("value_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProductAttributeValueSet200ResponseResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProductAttributeValueSet200ResponseResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProductAttributeValueSet200ResponseResult is not found in the empty JSON string", ProductAttributeValueSet200ResponseResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProductAttributeValueSet200ResponseResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProductAttributeValueSet200ResponseResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("attribute_id") != null && !jsonObj.get("attribute_id").isJsonNull()) && !jsonObj.get("attribute_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `attribute_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("attribute_id").toString()));
      }
      if ((jsonObj.get("product_id") != null && !jsonObj.get("product_id").isJsonNull()) && !jsonObj.get("product_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `product_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("product_id").toString()));
      }
      if ((jsonObj.get("value_id") != null && !jsonObj.get("value_id").isJsonNull()) && !jsonObj.get("value_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProductAttributeValueSet200ResponseResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProductAttributeValueSet200ResponseResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProductAttributeValueSet200ResponseResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProductAttributeValueSet200ResponseResult.class));

       return (TypeAdapter<T>) new TypeAdapter<ProductAttributeValueSet200ResponseResult>() {
           @Override
           public void write(JsonWriter out, ProductAttributeValueSet200ResponseResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProductAttributeValueSet200ResponseResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProductAttributeValueSet200ResponseResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProductAttributeValueSet200ResponseResult
   * @throws IOException if the JSON string is invalid with respect to ProductAttributeValueSet200ResponseResult
   */
  public static ProductAttributeValueSet200ResponseResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProductAttributeValueSet200ResponseResult.class);
  }

  /**
   * Convert an instance of ProductAttributeValueSet200ResponseResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

