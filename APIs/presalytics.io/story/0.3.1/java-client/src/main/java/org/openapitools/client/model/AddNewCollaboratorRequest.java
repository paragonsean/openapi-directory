/*
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
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
 * required subset of collaborator data to get a permission
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:17.561584-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AddNewCollaboratorRequest {
  public static final String SERIALIZED_NAME_COLLABORATOR_TYPE = "collaborator_type";
  @SerializedName(SERIALIZED_NAME_COLLABORATOR_TYPE)
  private String collaboratorType;

  public static final String SERIALIZED_NAME_USER_EMAIL = "user_email";
  @SerializedName(SERIALIZED_NAME_USER_EMAIL)
  private String userEmail;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private UUID userId;

  public AddNewCollaboratorRequest() {
  }

  public AddNewCollaboratorRequest collaboratorType(String collaboratorType) {
    this.collaboratorType = collaboratorType;
    return this;
  }

  /**
   * Get collaboratorType
   * @return collaboratorType
   */
  @javax.annotation.Nullable
  public String getCollaboratorType() {
    return collaboratorType;
  }

  public void setCollaboratorType(String collaboratorType) {
    this.collaboratorType = collaboratorType;
  }


  public AddNewCollaboratorRequest userEmail(String userEmail) {
    this.userEmail = userEmail;
    return this;
  }

  /**
   * Get userEmail
   * @return userEmail
   */
  @javax.annotation.Nullable
  public String getUserEmail() {
    return userEmail;
  }

  public void setUserEmail(String userEmail) {
    this.userEmail = userEmail;
  }


  public AddNewCollaboratorRequest userId(UUID userId) {
    this.userId = userId;
    return this;
  }

  /**
   * Get userId
   * @return userId
   */
  @javax.annotation.Nullable
  public UUID getUserId() {
    return userId;
  }

  public void setUserId(UUID userId) {
    this.userId = userId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddNewCollaboratorRequest addNewCollaboratorRequest = (AddNewCollaboratorRequest) o;
    return Objects.equals(this.collaboratorType, addNewCollaboratorRequest.collaboratorType) &&
        Objects.equals(this.userEmail, addNewCollaboratorRequest.userEmail) &&
        Objects.equals(this.userId, addNewCollaboratorRequest.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(collaboratorType, userEmail, userId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddNewCollaboratorRequest {\n");
    sb.append("    collaboratorType: ").append(toIndentedString(collaboratorType)).append("\n");
    sb.append("    userEmail: ").append(toIndentedString(userEmail)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
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
    openapiFields.add("collaborator_type");
    openapiFields.add("user_email");
    openapiFields.add("user_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AddNewCollaboratorRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AddNewCollaboratorRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AddNewCollaboratorRequest is not found in the empty JSON string", AddNewCollaboratorRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AddNewCollaboratorRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AddNewCollaboratorRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("collaborator_type") != null && !jsonObj.get("collaborator_type").isJsonNull()) && !jsonObj.get("collaborator_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `collaborator_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("collaborator_type").toString()));
      }
      if ((jsonObj.get("user_email") != null && !jsonObj.get("user_email").isJsonNull()) && !jsonObj.get("user_email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_email").toString()));
      }
      if ((jsonObj.get("user_id") != null && !jsonObj.get("user_id").isJsonNull()) && !jsonObj.get("user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AddNewCollaboratorRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AddNewCollaboratorRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AddNewCollaboratorRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AddNewCollaboratorRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AddNewCollaboratorRequest>() {
           @Override
           public void write(JsonWriter out, AddNewCollaboratorRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AddNewCollaboratorRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AddNewCollaboratorRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AddNewCollaboratorRequest
   * @throws IOException if the JSON string is invalid with respect to AddNewCollaboratorRequest
   */
  public static AddNewCollaboratorRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AddNewCollaboratorRequest.class);
  }

  /**
   * Convert an instance of AddNewCollaboratorRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

