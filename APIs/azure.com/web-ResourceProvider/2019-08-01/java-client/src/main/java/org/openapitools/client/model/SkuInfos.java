/*
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
import org.openapitools.client.model.GlobalCsmSkuDescription;

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
 * Collection of SKU information.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:47.141391-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SkuInfos {
  public static final String SERIALIZED_NAME_RESOURCE_TYPE = "resourceType";
  @SerializedName(SERIALIZED_NAME_RESOURCE_TYPE)
  private String resourceType;

  public static final String SERIALIZED_NAME_SKUS = "skus";
  @SerializedName(SERIALIZED_NAME_SKUS)
  private List<GlobalCsmSkuDescription> skus = new ArrayList<>();

  public SkuInfos() {
  }

  public SkuInfos resourceType(String resourceType) {
    this.resourceType = resourceType;
    return this;
  }

  /**
   * Resource type that this SKU applies to.
   * @return resourceType
   */
  @javax.annotation.Nullable
  public String getResourceType() {
    return resourceType;
  }

  public void setResourceType(String resourceType) {
    this.resourceType = resourceType;
  }


  public SkuInfos skus(List<GlobalCsmSkuDescription> skus) {
    this.skus = skus;
    return this;
  }

  public SkuInfos addSkusItem(GlobalCsmSkuDescription skusItem) {
    if (this.skus == null) {
      this.skus = new ArrayList<>();
    }
    this.skus.add(skusItem);
    return this;
  }

  /**
   * List of SKUs the subscription is able to use.
   * @return skus
   */
  @javax.annotation.Nullable
  public List<GlobalCsmSkuDescription> getSkus() {
    return skus;
  }

  public void setSkus(List<GlobalCsmSkuDescription> skus) {
    this.skus = skus;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SkuInfos skuInfos = (SkuInfos) o;
    return Objects.equals(this.resourceType, skuInfos.resourceType) &&
        Objects.equals(this.skus, skuInfos.skus);
  }

  @Override
  public int hashCode() {
    return Objects.hash(resourceType, skus);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SkuInfos {\n");
    sb.append("    resourceType: ").append(toIndentedString(resourceType)).append("\n");
    sb.append("    skus: ").append(toIndentedString(skus)).append("\n");
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
    openapiFields.add("resourceType");
    openapiFields.add("skus");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SkuInfos
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SkuInfos.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SkuInfos is not found in the empty JSON string", SkuInfos.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SkuInfos.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SkuInfos` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("resourceType") != null && !jsonObj.get("resourceType").isJsonNull()) && !jsonObj.get("resourceType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceType").toString()));
      }
      if (jsonObj.get("skus") != null && !jsonObj.get("skus").isJsonNull()) {
        JsonArray jsonArrayskus = jsonObj.getAsJsonArray("skus");
        if (jsonArrayskus != null) {
          // ensure the json data is an array
          if (!jsonObj.get("skus").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `skus` to be an array in the JSON string but got `%s`", jsonObj.get("skus").toString()));
          }

          // validate the optional field `skus` (array)
          for (int i = 0; i < jsonArrayskus.size(); i++) {
            GlobalCsmSkuDescription.validateJsonElement(jsonArrayskus.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SkuInfos.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SkuInfos' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SkuInfos> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SkuInfos.class));

       return (TypeAdapter<T>) new TypeAdapter<SkuInfos>() {
           @Override
           public void write(JsonWriter out, SkuInfos value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SkuInfos read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SkuInfos given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SkuInfos
   * @throws IOException if the JSON string is invalid with respect to SkuInfos
   */
  public static SkuInfos fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SkuInfos.class);
  }

  /**
   * Convert an instance of SkuInfos to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

