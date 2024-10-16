/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
import org.openapitools.client.model.AnonymizationProfile;

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
 * OutgoingTransaction
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:37.231084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OutgoingTransaction {
  public static final String SERIALIZED_NAME_BOX_ID = "boxId";
  @SerializedName(SERIALIZED_NAME_BOX_ID)
  private Long boxId;

  public static final String SERIALIZED_NAME_BOX_NAME = "boxName";
  @SerializedName(SERIALIZED_NAME_BOX_NAME)
  private String boxName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_PROFILE = "profile";
  @SerializedName(SERIALIZED_NAME_PROFILE)
  private AnonymizationProfile profile;

  public static final String SERIALIZED_NAME_SENT_IMAGE_COUNT = "sentImageCount";
  @SerializedName(SERIALIZED_NAME_SENT_IMAGE_COUNT)
  private Long sentImageCount;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TOTAL_IMAGE_COUNT = "totalImageCount";
  @SerializedName(SERIALIZED_NAME_TOTAL_IMAGE_COUNT)
  private Long totalImageCount;

  public static final String SERIALIZED_NAME_UPDATED = "updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private Long updated;

  public OutgoingTransaction() {
  }

  public OutgoingTransaction boxId(Long boxId) {
    this.boxId = boxId;
    return this;
  }

  /**
   * Get boxId
   * @return boxId
   */
  @javax.annotation.Nullable
  public Long getBoxId() {
    return boxId;
  }

  public void setBoxId(Long boxId) {
    this.boxId = boxId;
  }


  public OutgoingTransaction boxName(String boxName) {
    this.boxName = boxName;
    return this;
  }

  /**
   * Get boxName
   * @return boxName
   */
  @javax.annotation.Nullable
  public String getBoxName() {
    return boxName;
  }

  public void setBoxName(String boxName) {
    this.boxName = boxName;
  }


  public OutgoingTransaction id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public OutgoingTransaction profile(AnonymizationProfile profile) {
    this.profile = profile;
    return this;
  }

  /**
   * Get profile
   * @return profile
   */
  @javax.annotation.Nullable
  public AnonymizationProfile getProfile() {
    return profile;
  }

  public void setProfile(AnonymizationProfile profile) {
    this.profile = profile;
  }


  public OutgoingTransaction sentImageCount(Long sentImageCount) {
    this.sentImageCount = sentImageCount;
    return this;
  }

  /**
   * Get sentImageCount
   * @return sentImageCount
   */
  @javax.annotation.Nullable
  public Long getSentImageCount() {
    return sentImageCount;
  }

  public void setSentImageCount(Long sentImageCount) {
    this.sentImageCount = sentImageCount;
  }


  public OutgoingTransaction status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public OutgoingTransaction totalImageCount(Long totalImageCount) {
    this.totalImageCount = totalImageCount;
    return this;
  }

  /**
   * Get totalImageCount
   * @return totalImageCount
   */
  @javax.annotation.Nullable
  public Long getTotalImageCount() {
    return totalImageCount;
  }

  public void setTotalImageCount(Long totalImageCount) {
    this.totalImageCount = totalImageCount;
  }


  public OutgoingTransaction updated(Long updated) {
    this.updated = updated;
    return this;
  }

  /**
   * Get updated
   * @return updated
   */
  @javax.annotation.Nullable
  public Long getUpdated() {
    return updated;
  }

  public void setUpdated(Long updated) {
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
    OutgoingTransaction outgoingTransaction = (OutgoingTransaction) o;
    return Objects.equals(this.boxId, outgoingTransaction.boxId) &&
        Objects.equals(this.boxName, outgoingTransaction.boxName) &&
        Objects.equals(this.id, outgoingTransaction.id) &&
        Objects.equals(this.profile, outgoingTransaction.profile) &&
        Objects.equals(this.sentImageCount, outgoingTransaction.sentImageCount) &&
        Objects.equals(this.status, outgoingTransaction.status) &&
        Objects.equals(this.totalImageCount, outgoingTransaction.totalImageCount) &&
        Objects.equals(this.updated, outgoingTransaction.updated);
  }

  @Override
  public int hashCode() {
    return Objects.hash(boxId, boxName, id, profile, sentImageCount, status, totalImageCount, updated);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OutgoingTransaction {\n");
    sb.append("    boxId: ").append(toIndentedString(boxId)).append("\n");
    sb.append("    boxName: ").append(toIndentedString(boxName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    profile: ").append(toIndentedString(profile)).append("\n");
    sb.append("    sentImageCount: ").append(toIndentedString(sentImageCount)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    totalImageCount: ").append(toIndentedString(totalImageCount)).append("\n");
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
    openapiFields.add("boxId");
    openapiFields.add("boxName");
    openapiFields.add("id");
    openapiFields.add("profile");
    openapiFields.add("sentImageCount");
    openapiFields.add("status");
    openapiFields.add("totalImageCount");
    openapiFields.add("updated");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OutgoingTransaction
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OutgoingTransaction.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OutgoingTransaction is not found in the empty JSON string", OutgoingTransaction.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OutgoingTransaction.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OutgoingTransaction` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("boxName") != null && !jsonObj.get("boxName").isJsonNull()) && !jsonObj.get("boxName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `boxName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("boxName").toString()));
      }
      // validate the optional field `profile`
      if (jsonObj.get("profile") != null && !jsonObj.get("profile").isJsonNull()) {
        AnonymizationProfile.validateJsonElement(jsonObj.get("profile"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OutgoingTransaction.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OutgoingTransaction' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OutgoingTransaction> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OutgoingTransaction.class));

       return (TypeAdapter<T>) new TypeAdapter<OutgoingTransaction>() {
           @Override
           public void write(JsonWriter out, OutgoingTransaction value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OutgoingTransaction read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OutgoingTransaction given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OutgoingTransaction
   * @throws IOException if the JSON string is invalid with respect to OutgoingTransaction
   */
  public static OutgoingTransaction fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OutgoingTransaction.class);
  }

  /**
   * Convert an instance of OutgoingTransaction to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

