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
import java.util.UUID;

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
 * DistributionGroupAADGroupResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DistributionGroupAADGroupResponse {
  public static final String SERIALIZED_NAME_AAD_GROUP_ID = "aad_group_id";
  @SerializedName(SERIALIZED_NAME_AAD_GROUP_ID)
  private UUID aadGroupId;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_DISTRIBUTION_GROUP_NAME = "distribution_group_name";
  @SerializedName(SERIALIZED_NAME_DISTRIBUTION_GROUP_NAME)
  private String distributionGroupName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_AAD_GROUP = "is_aad_group";
  @SerializedName(SERIALIZED_NAME_IS_AAD_GROUP)
  private Boolean isAadGroup;

  public DistributionGroupAADGroupResponse() {
  }

  public DistributionGroupAADGroupResponse aadGroupId(UUID aadGroupId) {
    this.aadGroupId = aadGroupId;
    return this;
  }

  /**
   * The AAD unique id (UUID) of the AAD group.
   * @return aadGroupId
   */
  @javax.annotation.Nullable
  public UUID getAadGroupId() {
    return aadGroupId;
  }

  public void setAadGroupId(UUID aadGroupId) {
    this.aadGroupId = aadGroupId;
  }


  public DistributionGroupAADGroupResponse displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * The display name of the AAD group
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public DistributionGroupAADGroupResponse distributionGroupName(String distributionGroupName) {
    this.distributionGroupName = distributionGroupName;
    return this;
  }

  /**
   * The distribution group of the AAD group
   * @return distributionGroupName
   */
  @javax.annotation.Nullable
  public String getDistributionGroupName() {
    return distributionGroupName;
  }

  public void setDistributionGroupName(String distributionGroupName) {
    this.distributionGroupName = distributionGroupName;
  }


  public DistributionGroupAADGroupResponse id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * The internal unique id (UUID) of the AAD group.
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public DistributionGroupAADGroupResponse isAadGroup(Boolean isAadGroup) {
    this.isAadGroup = isAadGroup;
    return this;
  }

  /**
   * Get isAadGroup
   * @return isAadGroup
   */
  @javax.annotation.Nullable
  public Boolean getIsAadGroup() {
    return isAadGroup;
  }

  public void setIsAadGroup(Boolean isAadGroup) {
    this.isAadGroup = isAadGroup;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DistributionGroupAADGroupResponse distributionGroupAADGroupResponse = (DistributionGroupAADGroupResponse) o;
    return Objects.equals(this.aadGroupId, distributionGroupAADGroupResponse.aadGroupId) &&
        Objects.equals(this.displayName, distributionGroupAADGroupResponse.displayName) &&
        Objects.equals(this.distributionGroupName, distributionGroupAADGroupResponse.distributionGroupName) &&
        Objects.equals(this.id, distributionGroupAADGroupResponse.id) &&
        Objects.equals(this.isAadGroup, distributionGroupAADGroupResponse.isAadGroup);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aadGroupId, displayName, distributionGroupName, id, isAadGroup);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DistributionGroupAADGroupResponse {\n");
    sb.append("    aadGroupId: ").append(toIndentedString(aadGroupId)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    distributionGroupName: ").append(toIndentedString(distributionGroupName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isAadGroup: ").append(toIndentedString(isAadGroup)).append("\n");
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
    openapiFields.add("aad_group_id");
    openapiFields.add("display_name");
    openapiFields.add("distribution_group_name");
    openapiFields.add("id");
    openapiFields.add("is_aad_group");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DistributionGroupAADGroupResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DistributionGroupAADGroupResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DistributionGroupAADGroupResponse is not found in the empty JSON string", DistributionGroupAADGroupResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DistributionGroupAADGroupResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DistributionGroupAADGroupResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("aad_group_id") != null && !jsonObj.get("aad_group_id").isJsonNull()) && !jsonObj.get("aad_group_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `aad_group_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("aad_group_id").toString()));
      }
      if ((jsonObj.get("display_name") != null && !jsonObj.get("display_name").isJsonNull()) && !jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
      if ((jsonObj.get("distribution_group_name") != null && !jsonObj.get("distribution_group_name").isJsonNull()) && !jsonObj.get("distribution_group_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `distribution_group_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("distribution_group_name").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DistributionGroupAADGroupResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DistributionGroupAADGroupResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DistributionGroupAADGroupResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DistributionGroupAADGroupResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<DistributionGroupAADGroupResponse>() {
           @Override
           public void write(JsonWriter out, DistributionGroupAADGroupResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DistributionGroupAADGroupResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DistributionGroupAADGroupResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DistributionGroupAADGroupResponse
   * @throws IOException if the JSON string is invalid with respect to DistributionGroupAADGroupResponse
   */
  public static DistributionGroupAADGroupResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DistributionGroupAADGroupResponse.class);
  }

  /**
   * Convert an instance of DistributionGroupAADGroupResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

