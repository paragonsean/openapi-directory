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
 * ConfigurableProductLinkManagementV1AddChildPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ConfigurableProductLinkManagementV1AddChildPostRequest {
  public static final String SERIALIZED_NAME_CHILD_SKU = "childSku";
  @SerializedName(SERIALIZED_NAME_CHILD_SKU)
  private String childSku;

  public ConfigurableProductLinkManagementV1AddChildPostRequest() {
  }

  public ConfigurableProductLinkManagementV1AddChildPostRequest childSku(String childSku) {
    this.childSku = childSku;
    return this;
  }

  /**
   * Get childSku
   * @return childSku
   */
  @javax.annotation.Nonnull
  public String getChildSku() {
    return childSku;
  }

  public void setChildSku(String childSku) {
    this.childSku = childSku;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConfigurableProductLinkManagementV1AddChildPostRequest configurableProductLinkManagementV1AddChildPostRequest = (ConfigurableProductLinkManagementV1AddChildPostRequest) o;
    return Objects.equals(this.childSku, configurableProductLinkManagementV1AddChildPostRequest.childSku);
  }

  @Override
  public int hashCode() {
    return Objects.hash(childSku);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ConfigurableProductLinkManagementV1AddChildPostRequest {\n");
    sb.append("    childSku: ").append(toIndentedString(childSku)).append("\n");
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
    openapiFields.add("childSku");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("childSku");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ConfigurableProductLinkManagementV1AddChildPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ConfigurableProductLinkManagementV1AddChildPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ConfigurableProductLinkManagementV1AddChildPostRequest is not found in the empty JSON string", ConfigurableProductLinkManagementV1AddChildPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ConfigurableProductLinkManagementV1AddChildPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ConfigurableProductLinkManagementV1AddChildPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ConfigurableProductLinkManagementV1AddChildPostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("childSku").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `childSku` to be a primitive type in the JSON string but got `%s`", jsonObj.get("childSku").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ConfigurableProductLinkManagementV1AddChildPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ConfigurableProductLinkManagementV1AddChildPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ConfigurableProductLinkManagementV1AddChildPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ConfigurableProductLinkManagementV1AddChildPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ConfigurableProductLinkManagementV1AddChildPostRequest>() {
           @Override
           public void write(JsonWriter out, ConfigurableProductLinkManagementV1AddChildPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ConfigurableProductLinkManagementV1AddChildPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ConfigurableProductLinkManagementV1AddChildPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ConfigurableProductLinkManagementV1AddChildPostRequest
   * @throws IOException if the JSON string is invalid with respect to ConfigurableProductLinkManagementV1AddChildPostRequest
   */
  public static ConfigurableProductLinkManagementV1AddChildPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ConfigurableProductLinkManagementV1AddChildPostRequest.class);
  }

  /**
   * Convert an instance of ConfigurableProductLinkManagementV1AddChildPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

