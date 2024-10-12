/*
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.BucketsBucketKeyMessagesPost200ResponseDataInner;
import org.openapitools.client.model.BucketsBucketKeyMessagesPost200ResponseMeta;

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
 * BucketsBucketKeyMessagesPost200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:55.705127-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BucketsBucketKeyMessagesPost200Response {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private List<BucketsBucketKeyMessagesPost200ResponseDataInner> data = new ArrayList<>();

  public static final String SERIALIZED_NAME_META = "meta";
  @SerializedName(SERIALIZED_NAME_META)
  private BucketsBucketKeyMessagesPost200ResponseMeta meta;

  public BucketsBucketKeyMessagesPost200Response() {
  }

  public BucketsBucketKeyMessagesPost200Response data(List<BucketsBucketKeyMessagesPost200ResponseDataInner> data) {
    this.data = data;
    return this;
  }

  public BucketsBucketKeyMessagesPost200Response addDataItem(BucketsBucketKeyMessagesPost200ResponseDataInner dataItem) {
    if (this.data == null) {
      this.data = new ArrayList<>();
    }
    this.data.add(dataItem);
    return this;
  }

  /**
   * Get data
   * @return data
   */
  @javax.annotation.Nullable
  public List<BucketsBucketKeyMessagesPost200ResponseDataInner> getData() {
    return data;
  }

  public void setData(List<BucketsBucketKeyMessagesPost200ResponseDataInner> data) {
    this.data = data;
  }


  public BucketsBucketKeyMessagesPost200Response meta(BucketsBucketKeyMessagesPost200ResponseMeta meta) {
    this.meta = meta;
    return this;
  }

  /**
   * Get meta
   * @return meta
   */
  @javax.annotation.Nullable
  public BucketsBucketKeyMessagesPost200ResponseMeta getMeta() {
    return meta;
  }

  public void setMeta(BucketsBucketKeyMessagesPost200ResponseMeta meta) {
    this.meta = meta;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BucketsBucketKeyMessagesPost200Response bucketsBucketKeyMessagesPost200Response = (BucketsBucketKeyMessagesPost200Response) o;
    return Objects.equals(this.data, bucketsBucketKeyMessagesPost200Response.data) &&
        Objects.equals(this.meta, bucketsBucketKeyMessagesPost200Response.meta);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, meta);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BucketsBucketKeyMessagesPost200Response {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    meta: ").append(toIndentedString(meta)).append("\n");
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
    openapiFields.add("data");
    openapiFields.add("meta");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BucketsBucketKeyMessagesPost200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BucketsBucketKeyMessagesPost200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BucketsBucketKeyMessagesPost200Response is not found in the empty JSON string", BucketsBucketKeyMessagesPost200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BucketsBucketKeyMessagesPost200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BucketsBucketKeyMessagesPost200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("data") != null && !jsonObj.get("data").isJsonNull()) {
        JsonArray jsonArraydata = jsonObj.getAsJsonArray("data");
        if (jsonArraydata != null) {
          // ensure the json data is an array
          if (!jsonObj.get("data").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `data` to be an array in the JSON string but got `%s`", jsonObj.get("data").toString()));
          }

          // validate the optional field `data` (array)
          for (int i = 0; i < jsonArraydata.size(); i++) {
            BucketsBucketKeyMessagesPost200ResponseDataInner.validateJsonElement(jsonArraydata.get(i));
          };
        }
      }
      // validate the optional field `meta`
      if (jsonObj.get("meta") != null && !jsonObj.get("meta").isJsonNull()) {
        BucketsBucketKeyMessagesPost200ResponseMeta.validateJsonElement(jsonObj.get("meta"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BucketsBucketKeyMessagesPost200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BucketsBucketKeyMessagesPost200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BucketsBucketKeyMessagesPost200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BucketsBucketKeyMessagesPost200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<BucketsBucketKeyMessagesPost200Response>() {
           @Override
           public void write(JsonWriter out, BucketsBucketKeyMessagesPost200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BucketsBucketKeyMessagesPost200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BucketsBucketKeyMessagesPost200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BucketsBucketKeyMessagesPost200Response
   * @throws IOException if the JSON string is invalid with respect to BucketsBucketKeyMessagesPost200Response
   */
  public static BucketsBucketKeyMessagesPost200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BucketsBucketKeyMessagesPost200Response.class);
  }

  /**
   * Convert an instance of BucketsBucketKeyMessagesPost200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

