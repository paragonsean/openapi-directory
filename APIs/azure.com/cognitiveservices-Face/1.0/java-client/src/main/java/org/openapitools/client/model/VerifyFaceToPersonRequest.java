/*
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
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
 * Request body for face to person verification.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:23.692507-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VerifyFaceToPersonRequest {
  public static final String SERIALIZED_NAME_FACE_ID = "faceId";
  @SerializedName(SERIALIZED_NAME_FACE_ID)
  private UUID faceId;

  public static final String SERIALIZED_NAME_LARGE_PERSON_GROUP_ID = "largePersonGroupId";
  @SerializedName(SERIALIZED_NAME_LARGE_PERSON_GROUP_ID)
  private String largePersonGroupId;

  public static final String SERIALIZED_NAME_PERSON_GROUP_ID = "personGroupId";
  @SerializedName(SERIALIZED_NAME_PERSON_GROUP_ID)
  private String personGroupId;

  public static final String SERIALIZED_NAME_PERSON_ID = "personId";
  @SerializedName(SERIALIZED_NAME_PERSON_ID)
  private UUID personId;

  public VerifyFaceToPersonRequest() {
  }

  public VerifyFaceToPersonRequest faceId(UUID faceId) {
    this.faceId = faceId;
    return this;
  }

  /**
   * FaceId of the face, comes from Face - Detect
   * @return faceId
   */
  @javax.annotation.Nonnull
  public UUID getFaceId() {
    return faceId;
  }

  public void setFaceId(UUID faceId) {
    this.faceId = faceId;
  }


  public VerifyFaceToPersonRequest largePersonGroupId(String largePersonGroupId) {
    this.largePersonGroupId = largePersonGroupId;
    return this;
  }

  /**
   * Using existing largePersonGroupId and personId for fast loading a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
   * @return largePersonGroupId
   */
  @javax.annotation.Nullable
  public String getLargePersonGroupId() {
    return largePersonGroupId;
  }

  public void setLargePersonGroupId(String largePersonGroupId) {
    this.largePersonGroupId = largePersonGroupId;
  }


  public VerifyFaceToPersonRequest personGroupId(String personGroupId) {
    this.personGroupId = personGroupId;
    return this;
  }

  /**
   * Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
   * @return personGroupId
   */
  @javax.annotation.Nullable
  public String getPersonGroupId() {
    return personGroupId;
  }

  public void setPersonGroupId(String personGroupId) {
    this.personGroupId = personGroupId;
  }


  public VerifyFaceToPersonRequest personId(UUID personId) {
    this.personId = personId;
    return this;
  }

  /**
   * Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
   * @return personId
   */
  @javax.annotation.Nonnull
  public UUID getPersonId() {
    return personId;
  }

  public void setPersonId(UUID personId) {
    this.personId = personId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VerifyFaceToPersonRequest verifyFaceToPersonRequest = (VerifyFaceToPersonRequest) o;
    return Objects.equals(this.faceId, verifyFaceToPersonRequest.faceId) &&
        Objects.equals(this.largePersonGroupId, verifyFaceToPersonRequest.largePersonGroupId) &&
        Objects.equals(this.personGroupId, verifyFaceToPersonRequest.personGroupId) &&
        Objects.equals(this.personId, verifyFaceToPersonRequest.personId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(faceId, largePersonGroupId, personGroupId, personId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VerifyFaceToPersonRequest {\n");
    sb.append("    faceId: ").append(toIndentedString(faceId)).append("\n");
    sb.append("    largePersonGroupId: ").append(toIndentedString(largePersonGroupId)).append("\n");
    sb.append("    personGroupId: ").append(toIndentedString(personGroupId)).append("\n");
    sb.append("    personId: ").append(toIndentedString(personId)).append("\n");
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
    openapiFields.add("faceId");
    openapiFields.add("largePersonGroupId");
    openapiFields.add("personGroupId");
    openapiFields.add("personId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("faceId");
    openapiRequiredFields.add("personId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VerifyFaceToPersonRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VerifyFaceToPersonRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VerifyFaceToPersonRequest is not found in the empty JSON string", VerifyFaceToPersonRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VerifyFaceToPersonRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VerifyFaceToPersonRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : VerifyFaceToPersonRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("faceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `faceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("faceId").toString()));
      }
      if ((jsonObj.get("largePersonGroupId") != null && !jsonObj.get("largePersonGroupId").isJsonNull()) && !jsonObj.get("largePersonGroupId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `largePersonGroupId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("largePersonGroupId").toString()));
      }
      if ((jsonObj.get("personGroupId") != null && !jsonObj.get("personGroupId").isJsonNull()) && !jsonObj.get("personGroupId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `personGroupId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("personGroupId").toString()));
      }
      if (!jsonObj.get("personId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `personId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("personId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VerifyFaceToPersonRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VerifyFaceToPersonRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VerifyFaceToPersonRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VerifyFaceToPersonRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<VerifyFaceToPersonRequest>() {
           @Override
           public void write(JsonWriter out, VerifyFaceToPersonRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VerifyFaceToPersonRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VerifyFaceToPersonRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VerifyFaceToPersonRequest
   * @throws IOException if the JSON string is invalid with respect to VerifyFaceToPersonRequest
   */
  public static VerifyFaceToPersonRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VerifyFaceToPersonRequest.class);
  }

  /**
   * Convert an instance of VerifyFaceToPersonRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

