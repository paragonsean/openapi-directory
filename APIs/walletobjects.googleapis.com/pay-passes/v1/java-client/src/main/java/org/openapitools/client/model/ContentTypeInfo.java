/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
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
 * Detailed Content-Type information from Scotty. The Content-Type of the media will typically be filled in by the header or Scotty&#39;s best_guess, but this extended information provides the backend with more information so that it can make a better decision if needed. This is only used on media upload requests from Scotty.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ContentTypeInfo {
  public static final String SERIALIZED_NAME_BEST_GUESS = "bestGuess";
  @SerializedName(SERIALIZED_NAME_BEST_GUESS)
  private String bestGuess;

  public static final String SERIALIZED_NAME_FROM_BYTES = "fromBytes";
  @SerializedName(SERIALIZED_NAME_FROM_BYTES)
  private String fromBytes;

  public static final String SERIALIZED_NAME_FROM_FILE_NAME = "fromFileName";
  @SerializedName(SERIALIZED_NAME_FROM_FILE_NAME)
  private String fromFileName;

  public static final String SERIALIZED_NAME_FROM_HEADER = "fromHeader";
  @SerializedName(SERIALIZED_NAME_FROM_HEADER)
  private String fromHeader;

  public static final String SERIALIZED_NAME_FROM_URL_PATH = "fromUrlPath";
  @SerializedName(SERIALIZED_NAME_FROM_URL_PATH)
  private String fromUrlPath;

  public ContentTypeInfo() {
  }

  public ContentTypeInfo bestGuess(String bestGuess) {
    this.bestGuess = bestGuess;
    return this;
  }

  /**
   * Scotty&#39;s best guess of what the content type of the file is.
   * @return bestGuess
   */
  @javax.annotation.Nullable
  public String getBestGuess() {
    return bestGuess;
  }

  public void setBestGuess(String bestGuess) {
    this.bestGuess = bestGuess;
  }


  public ContentTypeInfo fromBytes(String fromBytes) {
    this.fromBytes = fromBytes;
    return this;
  }

  /**
   * The content type of the file derived by looking at specific bytes (i.e. \&quot;magic bytes\&quot;) of the actual file.
   * @return fromBytes
   */
  @javax.annotation.Nullable
  public String getFromBytes() {
    return fromBytes;
  }

  public void setFromBytes(String fromBytes) {
    this.fromBytes = fromBytes;
  }


  public ContentTypeInfo fromFileName(String fromFileName) {
    this.fromFileName = fromFileName;
    return this;
  }

  /**
   * The content type of the file derived from the file extension of the original file name used by the client.
   * @return fromFileName
   */
  @javax.annotation.Nullable
  public String getFromFileName() {
    return fromFileName;
  }

  public void setFromFileName(String fromFileName) {
    this.fromFileName = fromFileName;
  }


  public ContentTypeInfo fromHeader(String fromHeader) {
    this.fromHeader = fromHeader;
    return this;
  }

  /**
   * The content type of the file as specified in the request headers, multipart headers, or RUPIO start request.
   * @return fromHeader
   */
  @javax.annotation.Nullable
  public String getFromHeader() {
    return fromHeader;
  }

  public void setFromHeader(String fromHeader) {
    this.fromHeader = fromHeader;
  }


  public ContentTypeInfo fromUrlPath(String fromUrlPath) {
    this.fromUrlPath = fromUrlPath;
    return this;
  }

  /**
   * The content type of the file derived from the file extension of the URL path. The URL path is assumed to represent a file name (which is typically only true for agents that are providing a REST API).
   * @return fromUrlPath
   */
  @javax.annotation.Nullable
  public String getFromUrlPath() {
    return fromUrlPath;
  }

  public void setFromUrlPath(String fromUrlPath) {
    this.fromUrlPath = fromUrlPath;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ContentTypeInfo contentTypeInfo = (ContentTypeInfo) o;
    return Objects.equals(this.bestGuess, contentTypeInfo.bestGuess) &&
        Objects.equals(this.fromBytes, contentTypeInfo.fromBytes) &&
        Objects.equals(this.fromFileName, contentTypeInfo.fromFileName) &&
        Objects.equals(this.fromHeader, contentTypeInfo.fromHeader) &&
        Objects.equals(this.fromUrlPath, contentTypeInfo.fromUrlPath);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bestGuess, fromBytes, fromFileName, fromHeader, fromUrlPath);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ContentTypeInfo {\n");
    sb.append("    bestGuess: ").append(toIndentedString(bestGuess)).append("\n");
    sb.append("    fromBytes: ").append(toIndentedString(fromBytes)).append("\n");
    sb.append("    fromFileName: ").append(toIndentedString(fromFileName)).append("\n");
    sb.append("    fromHeader: ").append(toIndentedString(fromHeader)).append("\n");
    sb.append("    fromUrlPath: ").append(toIndentedString(fromUrlPath)).append("\n");
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
    openapiFields.add("bestGuess");
    openapiFields.add("fromBytes");
    openapiFields.add("fromFileName");
    openapiFields.add("fromHeader");
    openapiFields.add("fromUrlPath");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ContentTypeInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ContentTypeInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ContentTypeInfo is not found in the empty JSON string", ContentTypeInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ContentTypeInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ContentTypeInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("bestGuess") != null && !jsonObj.get("bestGuess").isJsonNull()) && !jsonObj.get("bestGuess").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bestGuess` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bestGuess").toString()));
      }
      if ((jsonObj.get("fromBytes") != null && !jsonObj.get("fromBytes").isJsonNull()) && !jsonObj.get("fromBytes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fromBytes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fromBytes").toString()));
      }
      if ((jsonObj.get("fromFileName") != null && !jsonObj.get("fromFileName").isJsonNull()) && !jsonObj.get("fromFileName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fromFileName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fromFileName").toString()));
      }
      if ((jsonObj.get("fromHeader") != null && !jsonObj.get("fromHeader").isJsonNull()) && !jsonObj.get("fromHeader").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fromHeader` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fromHeader").toString()));
      }
      if ((jsonObj.get("fromUrlPath") != null && !jsonObj.get("fromUrlPath").isJsonNull()) && !jsonObj.get("fromUrlPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fromUrlPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fromUrlPath").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ContentTypeInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ContentTypeInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ContentTypeInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ContentTypeInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<ContentTypeInfo>() {
           @Override
           public void write(JsonWriter out, ContentTypeInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ContentTypeInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ContentTypeInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ContentTypeInfo
   * @throws IOException if the JSON string is invalid with respect to ContentTypeInfo
   */
  public static ContentTypeInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ContentTypeInfo.class);
  }

  /**
   * Convert an instance of ContentTypeInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

