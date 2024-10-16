/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import org.openapitools.client.model.StoresCreateRequestIntuneDetailsAppCategory;
import org.openapitools.client.model.StoresCreateRequestIntuneDetailsTargetAudience;

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
 * PrivateIntuneStoreRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PrivateIntuneStoreRequest {
  public static final String SERIALIZED_NAME_APP_CATEGORY = "app_category";
  @SerializedName(SERIALIZED_NAME_APP_CATEGORY)
  private StoresCreateRequestIntuneDetailsAppCategory appCategory;

  public static final String SERIALIZED_NAME_TARGET_AUDIENCE = "target_audience";
  @SerializedName(SERIALIZED_NAME_TARGET_AUDIENCE)
  private StoresCreateRequestIntuneDetailsTargetAudience targetAudience;

  public static final String SERIALIZED_NAME_TENANT_ID = "tenant_id";
  @SerializedName(SERIALIZED_NAME_TENANT_ID)
  private String tenantId;

  public PrivateIntuneStoreRequest() {
  }

  public PrivateIntuneStoreRequest appCategory(StoresCreateRequestIntuneDetailsAppCategory appCategory) {
    this.appCategory = appCategory;
    return this;
  }

  /**
   * Get appCategory
   * @return appCategory
   */
  @javax.annotation.Nullable
  public StoresCreateRequestIntuneDetailsAppCategory getAppCategory() {
    return appCategory;
  }

  public void setAppCategory(StoresCreateRequestIntuneDetailsAppCategory appCategory) {
    this.appCategory = appCategory;
  }


  public PrivateIntuneStoreRequest targetAudience(StoresCreateRequestIntuneDetailsTargetAudience targetAudience) {
    this.targetAudience = targetAudience;
    return this;
  }

  /**
   * Get targetAudience
   * @return targetAudience
   */
  @javax.annotation.Nullable
  public StoresCreateRequestIntuneDetailsTargetAudience getTargetAudience() {
    return targetAudience;
  }

  public void setTargetAudience(StoresCreateRequestIntuneDetailsTargetAudience targetAudience) {
    this.targetAudience = targetAudience;
  }


  public PrivateIntuneStoreRequest tenantId(String tenantId) {
    this.tenantId = tenantId;
    return this;
  }

  /**
   * tenant id of the intune store
   * @return tenantId
   */
  @javax.annotation.Nullable
  public String getTenantId() {
    return tenantId;
  }

  public void setTenantId(String tenantId) {
    this.tenantId = tenantId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PrivateIntuneStoreRequest privateIntuneStoreRequest = (PrivateIntuneStoreRequest) o;
    return Objects.equals(this.appCategory, privateIntuneStoreRequest.appCategory) &&
        Objects.equals(this.targetAudience, privateIntuneStoreRequest.targetAudience) &&
        Objects.equals(this.tenantId, privateIntuneStoreRequest.tenantId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appCategory, targetAudience, tenantId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PrivateIntuneStoreRequest {\n");
    sb.append("    appCategory: ").append(toIndentedString(appCategory)).append("\n");
    sb.append("    targetAudience: ").append(toIndentedString(targetAudience)).append("\n");
    sb.append("    tenantId: ").append(toIndentedString(tenantId)).append("\n");
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
    openapiFields.add("app_category");
    openapiFields.add("target_audience");
    openapiFields.add("tenant_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PrivateIntuneStoreRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PrivateIntuneStoreRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PrivateIntuneStoreRequest is not found in the empty JSON string", PrivateIntuneStoreRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PrivateIntuneStoreRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PrivateIntuneStoreRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `app_category`
      if (jsonObj.get("app_category") != null && !jsonObj.get("app_category").isJsonNull()) {
        StoresCreateRequestIntuneDetailsAppCategory.validateJsonElement(jsonObj.get("app_category"));
      }
      // validate the optional field `target_audience`
      if (jsonObj.get("target_audience") != null && !jsonObj.get("target_audience").isJsonNull()) {
        StoresCreateRequestIntuneDetailsTargetAudience.validateJsonElement(jsonObj.get("target_audience"));
      }
      if ((jsonObj.get("tenant_id") != null && !jsonObj.get("tenant_id").isJsonNull()) && !jsonObj.get("tenant_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tenant_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tenant_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PrivateIntuneStoreRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PrivateIntuneStoreRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PrivateIntuneStoreRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PrivateIntuneStoreRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<PrivateIntuneStoreRequest>() {
           @Override
           public void write(JsonWriter out, PrivateIntuneStoreRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PrivateIntuneStoreRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PrivateIntuneStoreRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PrivateIntuneStoreRequest
   * @throws IOException if the JSON string is invalid with respect to PrivateIntuneStoreRequest
   */
  public static PrivateIntuneStoreRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PrivateIntuneStoreRequest.class);
  }

  /**
   * Convert an instance of PrivateIntuneStoreRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

