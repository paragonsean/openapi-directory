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
import org.openapitools.client.model.CommitsListByShaList200ResponseInnerAllOfCommitAuthor;

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
 * CommitsListByShaList200ResponseInnerAllOfCommit
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CommitsListByShaList200ResponseInnerAllOfCommit {
  public static final String SERIALIZED_NAME_AUTHOR = "author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private CommitsListByShaList200ResponseInnerAllOfCommitAuthor author;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public CommitsListByShaList200ResponseInnerAllOfCommit() {
  }

  public CommitsListByShaList200ResponseInnerAllOfCommit author(CommitsListByShaList200ResponseInnerAllOfCommitAuthor author) {
    this.author = author;
    return this;
  }

  /**
   * Get author
   * @return author
   */
  @javax.annotation.Nullable
  public CommitsListByShaList200ResponseInnerAllOfCommitAuthor getAuthor() {
    return author;
  }

  public void setAuthor(CommitsListByShaList200ResponseInnerAllOfCommitAuthor author) {
    this.author = author;
  }


  public CommitsListByShaList200ResponseInnerAllOfCommit message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Commit message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CommitsListByShaList200ResponseInnerAllOfCommit commitsListByShaList200ResponseInnerAllOfCommit = (CommitsListByShaList200ResponseInnerAllOfCommit) o;
    return Objects.equals(this.author, commitsListByShaList200ResponseInnerAllOfCommit.author) &&
        Objects.equals(this.message, commitsListByShaList200ResponseInnerAllOfCommit.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CommitsListByShaList200ResponseInnerAllOfCommit {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
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
    openapiFields.add("message");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CommitsListByShaList200ResponseInnerAllOfCommit
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CommitsListByShaList200ResponseInnerAllOfCommit.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CommitsListByShaList200ResponseInnerAllOfCommit is not found in the empty JSON string", CommitsListByShaList200ResponseInnerAllOfCommit.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CommitsListByShaList200ResponseInnerAllOfCommit.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CommitsListByShaList200ResponseInnerAllOfCommit` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `author`
      if (jsonObj.get("author") != null && !jsonObj.get("author").isJsonNull()) {
        CommitsListByShaList200ResponseInnerAllOfCommitAuthor.validateJsonElement(jsonObj.get("author"));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CommitsListByShaList200ResponseInnerAllOfCommit.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CommitsListByShaList200ResponseInnerAllOfCommit' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CommitsListByShaList200ResponseInnerAllOfCommit> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CommitsListByShaList200ResponseInnerAllOfCommit.class));

       return (TypeAdapter<T>) new TypeAdapter<CommitsListByShaList200ResponseInnerAllOfCommit>() {
           @Override
           public void write(JsonWriter out, CommitsListByShaList200ResponseInnerAllOfCommit value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CommitsListByShaList200ResponseInnerAllOfCommit read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CommitsListByShaList200ResponseInnerAllOfCommit given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CommitsListByShaList200ResponseInnerAllOfCommit
   * @throws IOException if the JSON string is invalid with respect to CommitsListByShaList200ResponseInnerAllOfCommit
   */
  public static CommitsListByShaList200ResponseInnerAllOfCommit fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CommitsListByShaList200ResponseInnerAllOfCommit.class);
  }

  /**
   * Convert an instance of CommitsListByShaList200ResponseInnerAllOfCommit to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

