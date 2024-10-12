/*
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
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
 * The gallery image properties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:25.069739-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GalleryImagePropertiesFragment {
  public static final String SERIALIZED_NAME_IS_ENABLED = "isEnabled";
  @SerializedName(SERIALIZED_NAME_IS_ENABLED)
  private Boolean isEnabled;

  public static final String SERIALIZED_NAME_IS_OVERRIDE = "isOverride";
  @SerializedName(SERIALIZED_NAME_IS_OVERRIDE)
  private Boolean isOverride;

  public static final String SERIALIZED_NAME_IS_PLAN_AUTHORIZED = "isPlanAuthorized";
  @SerializedName(SERIALIZED_NAME_IS_PLAN_AUTHORIZED)
  private Boolean isPlanAuthorized;

  public static final String SERIALIZED_NAME_PROVISIONING_STATE = "provisioningState";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATE)
  private String provisioningState;

  public static final String SERIALIZED_NAME_UNIQUE_IDENTIFIER = "uniqueIdentifier";
  @SerializedName(SERIALIZED_NAME_UNIQUE_IDENTIFIER)
  private String uniqueIdentifier;

  public GalleryImagePropertiesFragment() {
  }

  public GalleryImagePropertiesFragment isEnabled(Boolean isEnabled) {
    this.isEnabled = isEnabled;
    return this;
  }

  /**
   * Indicates whether this gallery image is enabled.
   * @return isEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIsEnabled() {
    return isEnabled;
  }

  public void setIsEnabled(Boolean isEnabled) {
    this.isEnabled = isEnabled;
  }


  public GalleryImagePropertiesFragment isOverride(Boolean isOverride) {
    this.isOverride = isOverride;
    return this;
  }

  /**
   * Indicates whether this gallery has been overridden for this lab account
   * @return isOverride
   */
  @javax.annotation.Nullable
  public Boolean getIsOverride() {
    return isOverride;
  }

  public void setIsOverride(Boolean isOverride) {
    this.isOverride = isOverride;
  }


  public GalleryImagePropertiesFragment isPlanAuthorized(Boolean isPlanAuthorized) {
    this.isPlanAuthorized = isPlanAuthorized;
    return this;
  }

  /**
   * Indicates if the plan has been authorized for programmatic deployment.
   * @return isPlanAuthorized
   */
  @javax.annotation.Nullable
  public Boolean getIsPlanAuthorized() {
    return isPlanAuthorized;
  }

  public void setIsPlanAuthorized(Boolean isPlanAuthorized) {
    this.isPlanAuthorized = isPlanAuthorized;
  }


  public GalleryImagePropertiesFragment provisioningState(String provisioningState) {
    this.provisioningState = provisioningState;
    return this;
  }

  /**
   * The provisioning status of the resource.
   * @return provisioningState
   */
  @javax.annotation.Nullable
  public String getProvisioningState() {
    return provisioningState;
  }

  public void setProvisioningState(String provisioningState) {
    this.provisioningState = provisioningState;
  }


  public GalleryImagePropertiesFragment uniqueIdentifier(String uniqueIdentifier) {
    this.uniqueIdentifier = uniqueIdentifier;
    return this;
  }

  /**
   * The unique immutable identifier of a resource (Guid).
   * @return uniqueIdentifier
   */
  @javax.annotation.Nullable
  public String getUniqueIdentifier() {
    return uniqueIdentifier;
  }

  public void setUniqueIdentifier(String uniqueIdentifier) {
    this.uniqueIdentifier = uniqueIdentifier;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GalleryImagePropertiesFragment galleryImagePropertiesFragment = (GalleryImagePropertiesFragment) o;
    return Objects.equals(this.isEnabled, galleryImagePropertiesFragment.isEnabled) &&
        Objects.equals(this.isOverride, galleryImagePropertiesFragment.isOverride) &&
        Objects.equals(this.isPlanAuthorized, galleryImagePropertiesFragment.isPlanAuthorized) &&
        Objects.equals(this.provisioningState, galleryImagePropertiesFragment.provisioningState) &&
        Objects.equals(this.uniqueIdentifier, galleryImagePropertiesFragment.uniqueIdentifier);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isEnabled, isOverride, isPlanAuthorized, provisioningState, uniqueIdentifier);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GalleryImagePropertiesFragment {\n");
    sb.append("    isEnabled: ").append(toIndentedString(isEnabled)).append("\n");
    sb.append("    isOverride: ").append(toIndentedString(isOverride)).append("\n");
    sb.append("    isPlanAuthorized: ").append(toIndentedString(isPlanAuthorized)).append("\n");
    sb.append("    provisioningState: ").append(toIndentedString(provisioningState)).append("\n");
    sb.append("    uniqueIdentifier: ").append(toIndentedString(uniqueIdentifier)).append("\n");
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
    openapiFields.add("isEnabled");
    openapiFields.add("isOverride");
    openapiFields.add("isPlanAuthorized");
    openapiFields.add("provisioningState");
    openapiFields.add("uniqueIdentifier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GalleryImagePropertiesFragment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GalleryImagePropertiesFragment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GalleryImagePropertiesFragment is not found in the empty JSON string", GalleryImagePropertiesFragment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GalleryImagePropertiesFragment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GalleryImagePropertiesFragment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) && !jsonObj.get("provisioningState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioningState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioningState").toString()));
      }
      if ((jsonObj.get("uniqueIdentifier") != null && !jsonObj.get("uniqueIdentifier").isJsonNull()) && !jsonObj.get("uniqueIdentifier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uniqueIdentifier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uniqueIdentifier").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GalleryImagePropertiesFragment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GalleryImagePropertiesFragment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GalleryImagePropertiesFragment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GalleryImagePropertiesFragment.class));

       return (TypeAdapter<T>) new TypeAdapter<GalleryImagePropertiesFragment>() {
           @Override
           public void write(JsonWriter out, GalleryImagePropertiesFragment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GalleryImagePropertiesFragment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GalleryImagePropertiesFragment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GalleryImagePropertiesFragment
   * @throws IOException if the JSON string is invalid with respect to GalleryImagePropertiesFragment
   */
  public static GalleryImagePropertiesFragment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GalleryImagePropertiesFragment.class);
  }

  /**
   * Convert an instance of GalleryImagePropertiesFragment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

