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
 * AttributeUpdate200ResponseResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AttributeUpdate200ResponseResult {
  public static final String SERIALIZED_NAME_UPDATED = "updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private Boolean updated;

  public AttributeUpdate200ResponseResult() {
  }

  public AttributeUpdate200ResponseResult updated(Boolean updated) {
    this.updated = updated;
    return this;
  }

  /**
   * Get updated
   * @return updated
   */
  @javax.annotation.Nullable
  public Boolean getUpdated() {
    return updated;
  }

  public void setUpdated(Boolean updated) {
    this.updated = updated;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AttributeUpdate200ResponseResult attributeUpdate200ResponseResult = (AttributeUpdate200ResponseResult) o;
    return Objects.equals(this.updated, attributeUpdate200ResponseResult.updated);
  }

  @Override
  public int hashCode() {
    return Objects.hash(updated);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AttributeUpdate200ResponseResult {\n");
    sb.append("    updated: ").append(toIndentedString(updated)).append("\n");
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
    openapiFields.add("updated");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AttributeUpdate200ResponseResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AttributeUpdate200ResponseResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AttributeUpdate200ResponseResult is not found in the empty JSON string", AttributeUpdate200ResponseResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AttributeUpdate200ResponseResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AttributeUpdate200ResponseResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AttributeUpdate200ResponseResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AttributeUpdate200ResponseResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AttributeUpdate200ResponseResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AttributeUpdate200ResponseResult.class));

       return (TypeAdapter<T>) new TypeAdapter<AttributeUpdate200ResponseResult>() {
           @Override
           public void write(JsonWriter out, AttributeUpdate200ResponseResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AttributeUpdate200ResponseResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AttributeUpdate200ResponseResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AttributeUpdate200ResponseResult
   * @throws IOException if the JSON string is invalid with respect to AttributeUpdate200ResponseResult
   */
  public static AttributeUpdate200ResponseResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AttributeUpdate200ResponseResult.class);
  }

  /**
   * Convert an instance of AttributeUpdate200ResponseResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

