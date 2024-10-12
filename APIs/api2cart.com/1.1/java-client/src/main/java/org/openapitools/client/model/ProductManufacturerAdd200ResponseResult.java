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
 * ProductManufacturerAdd200ResponseResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductManufacturerAdd200ResponseResult {
  public static final String SERIALIZED_NAME_MANUFACTURER_ID = "manufacturer_id";
  @SerializedName(SERIALIZED_NAME_MANUFACTURER_ID)
  private String manufacturerId;

  public ProductManufacturerAdd200ResponseResult() {
  }

  public ProductManufacturerAdd200ResponseResult manufacturerId(String manufacturerId) {
    this.manufacturerId = manufacturerId;
    return this;
  }

  /**
   * Get manufacturerId
   * @return manufacturerId
   */
  @javax.annotation.Nullable
  public String getManufacturerId() {
    return manufacturerId;
  }

  public void setManufacturerId(String manufacturerId) {
    this.manufacturerId = manufacturerId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProductManufacturerAdd200ResponseResult productManufacturerAdd200ResponseResult = (ProductManufacturerAdd200ResponseResult) o;
    return Objects.equals(this.manufacturerId, productManufacturerAdd200ResponseResult.manufacturerId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(manufacturerId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProductManufacturerAdd200ResponseResult {\n");
    sb.append("    manufacturerId: ").append(toIndentedString(manufacturerId)).append("\n");
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
    openapiFields.add("manufacturer_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProductManufacturerAdd200ResponseResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProductManufacturerAdd200ResponseResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProductManufacturerAdd200ResponseResult is not found in the empty JSON string", ProductManufacturerAdd200ResponseResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProductManufacturerAdd200ResponseResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProductManufacturerAdd200ResponseResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("manufacturer_id") != null && !jsonObj.get("manufacturer_id").isJsonNull()) && !jsonObj.get("manufacturer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `manufacturer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("manufacturer_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProductManufacturerAdd200ResponseResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProductManufacturerAdd200ResponseResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProductManufacturerAdd200ResponseResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProductManufacturerAdd200ResponseResult.class));

       return (TypeAdapter<T>) new TypeAdapter<ProductManufacturerAdd200ResponseResult>() {
           @Override
           public void write(JsonWriter out, ProductManufacturerAdd200ResponseResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProductManufacturerAdd200ResponseResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProductManufacturerAdd200ResponseResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProductManufacturerAdd200ResponseResult
   * @throws IOException if the JSON string is invalid with respect to ProductManufacturerAdd200ResponseResult
   */
  public static ProductManufacturerAdd200ResponseResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProductManufacturerAdd200ResponseResult.class);
  }

  /**
   * Convert an instance of ProductManufacturerAdd200ResponseResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

