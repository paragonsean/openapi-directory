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
 * Parameters specific to media downloads.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DownloadParameters {
  public static final String SERIALIZED_NAME_ALLOW_GZIP_COMPRESSION = "allowGzipCompression";
  @SerializedName(SERIALIZED_NAME_ALLOW_GZIP_COMPRESSION)
  private Boolean allowGzipCompression;

  public static final String SERIALIZED_NAME_IGNORE_RANGE = "ignoreRange";
  @SerializedName(SERIALIZED_NAME_IGNORE_RANGE)
  private Boolean ignoreRange;

  public DownloadParameters() {
  }

  public DownloadParameters allowGzipCompression(Boolean allowGzipCompression) {
    this.allowGzipCompression = allowGzipCompression;
    return this;
  }

  /**
   * A boolean to be returned in the response to Scotty. Allows/disallows gzip encoding of the payload content when the server thinks it&#39;s advantageous (hence, does not guarantee compression) which allows Scotty to GZip the response to the client.
   * @return allowGzipCompression
   */
  @javax.annotation.Nullable
  public Boolean getAllowGzipCompression() {
    return allowGzipCompression;
  }

  public void setAllowGzipCompression(Boolean allowGzipCompression) {
    this.allowGzipCompression = allowGzipCompression;
  }


  public DownloadParameters ignoreRange(Boolean ignoreRange) {
    this.ignoreRange = ignoreRange;
    return this;
  }

  /**
   * Determining whether or not Apiary should skip the inclusion of any Content-Range header on its response to Scotty.
   * @return ignoreRange
   */
  @javax.annotation.Nullable
  public Boolean getIgnoreRange() {
    return ignoreRange;
  }

  public void setIgnoreRange(Boolean ignoreRange) {
    this.ignoreRange = ignoreRange;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DownloadParameters downloadParameters = (DownloadParameters) o;
    return Objects.equals(this.allowGzipCompression, downloadParameters.allowGzipCompression) &&
        Objects.equals(this.ignoreRange, downloadParameters.ignoreRange);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowGzipCompression, ignoreRange);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DownloadParameters {\n");
    sb.append("    allowGzipCompression: ").append(toIndentedString(allowGzipCompression)).append("\n");
    sb.append("    ignoreRange: ").append(toIndentedString(ignoreRange)).append("\n");
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
    openapiFields.add("allowGzipCompression");
    openapiFields.add("ignoreRange");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DownloadParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DownloadParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DownloadParameters is not found in the empty JSON string", DownloadParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DownloadParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DownloadParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DownloadParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DownloadParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DownloadParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DownloadParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<DownloadParameters>() {
           @Override
           public void write(JsonWriter out, DownloadParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DownloadParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DownloadParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DownloadParameters
   * @throws IOException if the JSON string is invalid with respect to DownloadParameters
   */
  public static DownloadParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DownloadParameters.class);
  }

  /**
   * Convert an instance of DownloadParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

