/*
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
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
import org.openapitools.client.model.BatchFormat;

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
 * BatchOutputFile
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:56.961414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BatchOutputFile {
  public static final String SERIALIZED_NAME_FILENAME = "filename";
  @SerializedName(SERIALIZED_NAME_FILENAME)
  private String filename = "qrcodes";

  public static final String SERIALIZED_NAME_FORMAT = "format";
  @SerializedName(SERIALIZED_NAME_FORMAT)
  private BatchFormat format = BatchFormat.ZIP;

  public BatchOutputFile() {
  }

  public BatchOutputFile filename(String filename) {
    this.filename = filename;
    return this;
  }

  /**
   * Output filename.
   * @return filename
   */
  @javax.annotation.Nullable
  public String getFilename() {
    return filename;
  }

  public void setFilename(String filename) {
    this.filename = filename;
  }


  public BatchOutputFile format(BatchFormat format) {
    this.format = format;
    return this;
  }

  /**
   * Output file format.
   * @return format
   */
  @javax.annotation.Nullable
  public BatchFormat getFormat() {
    return format;
  }

  public void setFormat(BatchFormat format) {
    this.format = format;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BatchOutputFile batchOutputFile = (BatchOutputFile) o;
    return Objects.equals(this.filename, batchOutputFile.filename) &&
        Objects.equals(this.format, batchOutputFile.format);
  }

  @Override
  public int hashCode() {
    return Objects.hash(filename, format);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BatchOutputFile {\n");
    sb.append("    filename: ").append(toIndentedString(filename)).append("\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
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
    openapiFields.add("filename");
    openapiFields.add("format");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BatchOutputFile
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BatchOutputFile.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BatchOutputFile is not found in the empty JSON string", BatchOutputFile.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BatchOutputFile.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BatchOutputFile` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("filename") != null && !jsonObj.get("filename").isJsonNull()) && !jsonObj.get("filename").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `filename` to be a primitive type in the JSON string but got `%s`", jsonObj.get("filename").toString()));
      }
      // validate the optional field `format`
      if (jsonObj.get("format") != null && !jsonObj.get("format").isJsonNull()) {
        BatchFormat.validateJsonElement(jsonObj.get("format"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BatchOutputFile.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BatchOutputFile' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BatchOutputFile> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BatchOutputFile.class));

       return (TypeAdapter<T>) new TypeAdapter<BatchOutputFile>() {
           @Override
           public void write(JsonWriter out, BatchOutputFile value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BatchOutputFile read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BatchOutputFile given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BatchOutputFile
   * @throws IOException if the JSON string is invalid with respect to BatchOutputFile
   */
  public static BatchOutputFile fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BatchOutputFile.class);
  }

  /**
   * Convert an instance of BatchOutputFile to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

