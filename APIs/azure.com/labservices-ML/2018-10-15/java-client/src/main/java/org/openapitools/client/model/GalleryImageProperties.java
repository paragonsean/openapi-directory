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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.GalleryImageReference;
import org.openapitools.client.model.LatestOperationResult;

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
public class GalleryImageProperties {
  public static final String SERIALIZED_NAME_AUTHOR = "author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private String author;

  public static final String SERIALIZED_NAME_CREATED_DATE = "createdDate";
  @SerializedName(SERIALIZED_NAME_CREATED_DATE)
  private OffsetDateTime createdDate;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private String icon;

  public static final String SERIALIZED_NAME_IMAGE_REFERENCE = "imageReference";
  @SerializedName(SERIALIZED_NAME_IMAGE_REFERENCE)
  private GalleryImageReference imageReference;

  public static final String SERIALIZED_NAME_IS_ENABLED = "isEnabled";
  @SerializedName(SERIALIZED_NAME_IS_ENABLED)
  private Boolean isEnabled;

  public static final String SERIALIZED_NAME_IS_OVERRIDE = "isOverride";
  @SerializedName(SERIALIZED_NAME_IS_OVERRIDE)
  private Boolean isOverride;

  public static final String SERIALIZED_NAME_IS_PLAN_AUTHORIZED = "isPlanAuthorized";
  @SerializedName(SERIALIZED_NAME_IS_PLAN_AUTHORIZED)
  private Boolean isPlanAuthorized;

  public static final String SERIALIZED_NAME_LATEST_OPERATION_RESULT = "latestOperationResult";
  @SerializedName(SERIALIZED_NAME_LATEST_OPERATION_RESULT)
  private LatestOperationResult latestOperationResult;

  public static final String SERIALIZED_NAME_PLAN_ID = "planId";
  @SerializedName(SERIALIZED_NAME_PLAN_ID)
  private String planId;

  public static final String SERIALIZED_NAME_PROVISIONING_STATE = "provisioningState";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATE)
  private String provisioningState;

  public static final String SERIALIZED_NAME_UNIQUE_IDENTIFIER = "uniqueIdentifier";
  @SerializedName(SERIALIZED_NAME_UNIQUE_IDENTIFIER)
  private String uniqueIdentifier;

  public GalleryImageProperties() {
  }

  public GalleryImageProperties(
     String author, 
     OffsetDateTime createdDate, 
     String description, 
     String icon, 
     String planId
  ) {
    this();
    this.author = author;
    this.createdDate = createdDate;
    this.description = description;
    this.icon = icon;
    this.planId = planId;
  }

  /**
   * The author of the gallery image.
   * @return author
   */
  @javax.annotation.Nullable
  public String getAuthor() {
    return author;
  }



  /**
   * The creation date of the gallery image.
   * @return createdDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedDate() {
    return createdDate;
  }



  /**
   * The description of the gallery image.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }



  /**
   * The icon of the gallery image.
   * @return icon
   */
  @javax.annotation.Nullable
  public String getIcon() {
    return icon;
  }



  public GalleryImageProperties imageReference(GalleryImageReference imageReference) {
    this.imageReference = imageReference;
    return this;
  }

  /**
   * Get imageReference
   * @return imageReference
   */
  @javax.annotation.Nullable
  public GalleryImageReference getImageReference() {
    return imageReference;
  }

  public void setImageReference(GalleryImageReference imageReference) {
    this.imageReference = imageReference;
  }


  public GalleryImageProperties isEnabled(Boolean isEnabled) {
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


  public GalleryImageProperties isOverride(Boolean isOverride) {
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


  public GalleryImageProperties isPlanAuthorized(Boolean isPlanAuthorized) {
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


  public GalleryImageProperties latestOperationResult(LatestOperationResult latestOperationResult) {
    this.latestOperationResult = latestOperationResult;
    return this;
  }

  /**
   * Get latestOperationResult
   * @return latestOperationResult
   */
  @javax.annotation.Nullable
  public LatestOperationResult getLatestOperationResult() {
    return latestOperationResult;
  }

  public void setLatestOperationResult(LatestOperationResult latestOperationResult) {
    this.latestOperationResult = latestOperationResult;
  }


  /**
   * The third party plan that applies to this image
   * @return planId
   */
  @javax.annotation.Nullable
  public String getPlanId() {
    return planId;
  }



  public GalleryImageProperties provisioningState(String provisioningState) {
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


  public GalleryImageProperties uniqueIdentifier(String uniqueIdentifier) {
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
    GalleryImageProperties galleryImageProperties = (GalleryImageProperties) o;
    return Objects.equals(this.author, galleryImageProperties.author) &&
        Objects.equals(this.createdDate, galleryImageProperties.createdDate) &&
        Objects.equals(this.description, galleryImageProperties.description) &&
        Objects.equals(this.icon, galleryImageProperties.icon) &&
        Objects.equals(this.imageReference, galleryImageProperties.imageReference) &&
        Objects.equals(this.isEnabled, galleryImageProperties.isEnabled) &&
        Objects.equals(this.isOverride, galleryImageProperties.isOverride) &&
        Objects.equals(this.isPlanAuthorized, galleryImageProperties.isPlanAuthorized) &&
        Objects.equals(this.latestOperationResult, galleryImageProperties.latestOperationResult) &&
        Objects.equals(this.planId, galleryImageProperties.planId) &&
        Objects.equals(this.provisioningState, galleryImageProperties.provisioningState) &&
        Objects.equals(this.uniqueIdentifier, galleryImageProperties.uniqueIdentifier);
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, createdDate, description, icon, imageReference, isEnabled, isOverride, isPlanAuthorized, latestOperationResult, planId, provisioningState, uniqueIdentifier);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GalleryImageProperties {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    createdDate: ").append(toIndentedString(createdDate)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    imageReference: ").append(toIndentedString(imageReference)).append("\n");
    sb.append("    isEnabled: ").append(toIndentedString(isEnabled)).append("\n");
    sb.append("    isOverride: ").append(toIndentedString(isOverride)).append("\n");
    sb.append("    isPlanAuthorized: ").append(toIndentedString(isPlanAuthorized)).append("\n");
    sb.append("    latestOperationResult: ").append(toIndentedString(latestOperationResult)).append("\n");
    sb.append("    planId: ").append(toIndentedString(planId)).append("\n");
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
    openapiFields.add("author");
    openapiFields.add("createdDate");
    openapiFields.add("description");
    openapiFields.add("icon");
    openapiFields.add("imageReference");
    openapiFields.add("isEnabled");
    openapiFields.add("isOverride");
    openapiFields.add("isPlanAuthorized");
    openapiFields.add("latestOperationResult");
    openapiFields.add("planId");
    openapiFields.add("provisioningState");
    openapiFields.add("uniqueIdentifier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GalleryImageProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GalleryImageProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GalleryImageProperties is not found in the empty JSON string", GalleryImageProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GalleryImageProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GalleryImageProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("author") != null && !jsonObj.get("author").isJsonNull()) && !jsonObj.get("author").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `author` to be a primitive type in the JSON string but got `%s`", jsonObj.get("author").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) && !jsonObj.get("icon").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon").toString()));
      }
      // validate the optional field `imageReference`
      if (jsonObj.get("imageReference") != null && !jsonObj.get("imageReference").isJsonNull()) {
        GalleryImageReference.validateJsonElement(jsonObj.get("imageReference"));
      }
      // validate the optional field `latestOperationResult`
      if (jsonObj.get("latestOperationResult") != null && !jsonObj.get("latestOperationResult").isJsonNull()) {
        LatestOperationResult.validateJsonElement(jsonObj.get("latestOperationResult"));
      }
      if ((jsonObj.get("planId") != null && !jsonObj.get("planId").isJsonNull()) && !jsonObj.get("planId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `planId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("planId").toString()));
      }
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
       if (!GalleryImageProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GalleryImageProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GalleryImageProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GalleryImageProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<GalleryImageProperties>() {
           @Override
           public void write(JsonWriter out, GalleryImageProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GalleryImageProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GalleryImageProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GalleryImageProperties
   * @throws IOException if the JSON string is invalid with respect to GalleryImageProperties
   */
  public static GalleryImageProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GalleryImageProperties.class);
  }

  /**
   * Convert an instance of GalleryImageProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

