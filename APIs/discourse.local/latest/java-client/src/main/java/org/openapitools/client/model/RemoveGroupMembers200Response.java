/*
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
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
 * RemoveGroupMembers200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:34.324076-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RemoveGroupMembers200Response {
  public static final String SERIALIZED_NAME_SKIPPED_USERNAMES = "skipped_usernames";
  @SerializedName(SERIALIZED_NAME_SKIPPED_USERNAMES)
  private List<Object> skippedUsernames = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUCCESS = "success";
  @SerializedName(SERIALIZED_NAME_SUCCESS)
  private String success;

  public static final String SERIALIZED_NAME_USERNAMES = "usernames";
  @SerializedName(SERIALIZED_NAME_USERNAMES)
  private List<Object> usernames = new ArrayList<>();

  public RemoveGroupMembers200Response() {
  }

  public RemoveGroupMembers200Response skippedUsernames(List<Object> skippedUsernames) {
    this.skippedUsernames = skippedUsernames;
    return this;
  }

  public RemoveGroupMembers200Response addSkippedUsernamesItem(Object skippedUsernamesItem) {
    if (this.skippedUsernames == null) {
      this.skippedUsernames = new ArrayList<>();
    }
    this.skippedUsernames.add(skippedUsernamesItem);
    return this;
  }

  /**
   * Get skippedUsernames
   * @return skippedUsernames
   */
  @javax.annotation.Nonnull
  public List<Object> getSkippedUsernames() {
    return skippedUsernames;
  }

  public void setSkippedUsernames(List<Object> skippedUsernames) {
    this.skippedUsernames = skippedUsernames;
  }


  public RemoveGroupMembers200Response success(String success) {
    this.success = success;
    return this;
  }

  /**
   * Get success
   * @return success
   */
  @javax.annotation.Nonnull
  public String getSuccess() {
    return success;
  }

  public void setSuccess(String success) {
    this.success = success;
  }


  public RemoveGroupMembers200Response usernames(List<Object> usernames) {
    this.usernames = usernames;
    return this;
  }

  public RemoveGroupMembers200Response addUsernamesItem(Object usernamesItem) {
    if (this.usernames == null) {
      this.usernames = new ArrayList<>();
    }
    this.usernames.add(usernamesItem);
    return this;
  }

  /**
   * Get usernames
   * @return usernames
   */
  @javax.annotation.Nonnull
  public List<Object> getUsernames() {
    return usernames;
  }

  public void setUsernames(List<Object> usernames) {
    this.usernames = usernames;
  }

  /**
   * A container for additional, undeclared properties.
   * This is a holder for any undeclared properties as specified with
   * the 'additionalProperties' keyword in the OAS document.
   */
  private Map<String, Object> additionalProperties;

  /**
   * Set the additional (undeclared) property with the specified name and value.
   * If the property does not already exist, create it otherwise replace it.
   *
   * @param key name of the property
   * @param value value of the property
   * @return the RemoveGroupMembers200Response instance itself
   */
  public RemoveGroupMembers200Response putAdditionalProperty(String key, Object value) {
    if (this.additionalProperties == null) {
        this.additionalProperties = new HashMap<String, Object>();
    }
    this.additionalProperties.put(key, value);
    return this;
  }

  /**
   * Return the additional (undeclared) property.
   *
   * @return a map of objects
   */
  public Map<String, Object> getAdditionalProperties() {
    return additionalProperties;
  }

  /**
   * Return the additional (undeclared) property with the specified name.
   *
   * @param key name of the property
   * @return an object
   */
  public Object getAdditionalProperty(String key) {
    if (this.additionalProperties == null) {
        return null;
    }
    return this.additionalProperties.get(key);
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RemoveGroupMembers200Response removeGroupMembers200Response = (RemoveGroupMembers200Response) o;
    return Objects.equals(this.skippedUsernames, removeGroupMembers200Response.skippedUsernames) &&
        Objects.equals(this.success, removeGroupMembers200Response.success) &&
        Objects.equals(this.usernames, removeGroupMembers200Response.usernames)&&
        Objects.equals(this.additionalProperties, removeGroupMembers200Response.additionalProperties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(skippedUsernames, success, usernames, additionalProperties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RemoveGroupMembers200Response {\n");
    sb.append("    skippedUsernames: ").append(toIndentedString(skippedUsernames)).append("\n");
    sb.append("    success: ").append(toIndentedString(success)).append("\n");
    sb.append("    usernames: ").append(toIndentedString(usernames)).append("\n");
    sb.append("    additionalProperties: ").append(toIndentedString(additionalProperties)).append("\n");
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
    openapiFields.add("skipped_usernames");
    openapiFields.add("success");
    openapiFields.add("usernames");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("skipped_usernames");
    openapiRequiredFields.add("success");
    openapiRequiredFields.add("usernames");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RemoveGroupMembers200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RemoveGroupMembers200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RemoveGroupMembers200Response is not found in the empty JSON string", RemoveGroupMembers200Response.openapiRequiredFields.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : RemoveGroupMembers200Response.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("skipped_usernames") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("skipped_usernames").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `skipped_usernames` to be an array in the JSON string but got `%s`", jsonObj.get("skipped_usernames").toString()));
      }
      if (!jsonObj.get("success").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `success` to be a primitive type in the JSON string but got `%s`", jsonObj.get("success").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("usernames") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("usernames").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `usernames` to be an array in the JSON string but got `%s`", jsonObj.get("usernames").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RemoveGroupMembers200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RemoveGroupMembers200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RemoveGroupMembers200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RemoveGroupMembers200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<RemoveGroupMembers200Response>() {
           @Override
           public void write(JsonWriter out, RemoveGroupMembers200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             obj.remove("additionalProperties");
             // serialize additional properties
             if (value.getAdditionalProperties() != null) {
               for (Map.Entry<String, Object> entry : value.getAdditionalProperties().entrySet()) {
                 if (entry.getValue() instanceof String)
                   obj.addProperty(entry.getKey(), (String) entry.getValue());
                 else if (entry.getValue() instanceof Number)
                   obj.addProperty(entry.getKey(), (Number) entry.getValue());
                 else if (entry.getValue() instanceof Boolean)
                   obj.addProperty(entry.getKey(), (Boolean) entry.getValue());
                 else if (entry.getValue() instanceof Character)
                   obj.addProperty(entry.getKey(), (Character) entry.getValue());
                 else {
                   JsonElement jsonElement = gson.toJsonTree(entry.getValue());
                   if (jsonElement.isJsonArray()) {
                     obj.add(entry.getKey(), jsonElement.getAsJsonArray());
                   } else {
                     obj.add(entry.getKey(), jsonElement.getAsJsonObject());
                   }
                 }
               }
             }
             elementAdapter.write(out, obj);
           }

           @Override
           public RemoveGroupMembers200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             JsonObject jsonObj = jsonElement.getAsJsonObject();
             // store additional fields in the deserialized instance
             RemoveGroupMembers200Response instance = thisAdapter.fromJsonTree(jsonObj);
             for (Map.Entry<String, JsonElement> entry : jsonObj.entrySet()) {
               if (!openapiFields.contains(entry.getKey())) {
                 if (entry.getValue().isJsonPrimitive()) { // primitive type
                   if (entry.getValue().getAsJsonPrimitive().isString())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsString());
                   else if (entry.getValue().getAsJsonPrimitive().isNumber())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsNumber());
                   else if (entry.getValue().getAsJsonPrimitive().isBoolean())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsBoolean());
                   else
                     throw new IllegalArgumentException(String.format("The field `%s` has unknown primitive type. Value: %s", entry.getKey(), entry.getValue().toString()));
                 } else if (entry.getValue().isJsonArray()) {
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), List.class));
                 } else { // JSON object
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), HashMap.class));
                 }
               }
             }
             return instance;
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RemoveGroupMembers200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RemoveGroupMembers200Response
   * @throws IOException if the JSON string is invalid with respect to RemoveGroupMembers200Response
   */
  public static RemoveGroupMembers200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RemoveGroupMembers200Response.class);
  }

  /**
   * Convert an instance of RemoveGroupMembers200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

