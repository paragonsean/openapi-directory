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
 * ReleaseCount
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReleaseCount {
  public static final String SERIALIZED_NAME_DISTRIBUTION_GROUP = "distribution_group";
  @SerializedName(SERIALIZED_NAME_DISTRIBUTION_GROUP)
  private String distributionGroup;

  public static final String SERIALIZED_NAME_RELEASE_ID = "release_id";
  @SerializedName(SERIALIZED_NAME_RELEASE_ID)
  private String releaseId;

  public static final String SERIALIZED_NAME_TOTAL_COUNT = "total_count";
  @SerializedName(SERIALIZED_NAME_TOTAL_COUNT)
  private Long totalCount;

  public static final String SERIALIZED_NAME_UNIQUE_COUNT = "unique_count";
  @SerializedName(SERIALIZED_NAME_UNIQUE_COUNT)
  private Long uniqueCount;

  public ReleaseCount() {
  }

  public ReleaseCount distributionGroup(String distributionGroup) {
    this.distributionGroup = distributionGroup;
    return this;
  }

  /**
   * Distribution group queried. 
   * @return distributionGroup
   */
  @javax.annotation.Nullable
  public String getDistributionGroup() {
    return distributionGroup;
  }

  public void setDistributionGroup(String distributionGroup) {
    this.distributionGroup = distributionGroup;
  }


  public ReleaseCount releaseId(String releaseId) {
    this.releaseId = releaseId;
    return this;
  }

  /**
   * Get releaseId
   * @return releaseId
   */
  @javax.annotation.Nonnull
  public String getReleaseId() {
    return releaseId;
  }

  public void setReleaseId(String releaseId) {
    this.releaseId = releaseId;
  }


  public ReleaseCount totalCount(Long totalCount) {
    this.totalCount = totalCount;
    return this;
  }

  /**
   * Total count of downloads. 
   * @return totalCount
   */
  @javax.annotation.Nonnull
  public Long getTotalCount() {
    return totalCount;
  }

  public void setTotalCount(Long totalCount) {
    this.totalCount = totalCount;
  }


  public ReleaseCount uniqueCount(Long uniqueCount) {
    this.uniqueCount = uniqueCount;
    return this;
  }

  /**
   * Count of unique downloads against user id. 
   * @return uniqueCount
   */
  @javax.annotation.Nonnull
  public Long getUniqueCount() {
    return uniqueCount;
  }

  public void setUniqueCount(Long uniqueCount) {
    this.uniqueCount = uniqueCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReleaseCount releaseCount = (ReleaseCount) o;
    return Objects.equals(this.distributionGroup, releaseCount.distributionGroup) &&
        Objects.equals(this.releaseId, releaseCount.releaseId) &&
        Objects.equals(this.totalCount, releaseCount.totalCount) &&
        Objects.equals(this.uniqueCount, releaseCount.uniqueCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(distributionGroup, releaseId, totalCount, uniqueCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReleaseCount {\n");
    sb.append("    distributionGroup: ").append(toIndentedString(distributionGroup)).append("\n");
    sb.append("    releaseId: ").append(toIndentedString(releaseId)).append("\n");
    sb.append("    totalCount: ").append(toIndentedString(totalCount)).append("\n");
    sb.append("    uniqueCount: ").append(toIndentedString(uniqueCount)).append("\n");
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
    openapiFields.add("distribution_group");
    openapiFields.add("release_id");
    openapiFields.add("total_count");
    openapiFields.add("unique_count");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("release_id");
    openapiRequiredFields.add("total_count");
    openapiRequiredFields.add("unique_count");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReleaseCount
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReleaseCount.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReleaseCount is not found in the empty JSON string", ReleaseCount.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReleaseCount.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReleaseCount` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ReleaseCount.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("distribution_group") != null && !jsonObj.get("distribution_group").isJsonNull()) && !jsonObj.get("distribution_group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `distribution_group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("distribution_group").toString()));
      }
      if (!jsonObj.get("release_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReleaseCount.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReleaseCount' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReleaseCount> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReleaseCount.class));

       return (TypeAdapter<T>) new TypeAdapter<ReleaseCount>() {
           @Override
           public void write(JsonWriter out, ReleaseCount value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReleaseCount read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReleaseCount given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReleaseCount
   * @throws IOException if the JSON string is invalid with respect to ReleaseCount
   */
  public static ReleaseCount fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReleaseCount.class);
  }

  /**
   * Convert an instance of ReleaseCount to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

