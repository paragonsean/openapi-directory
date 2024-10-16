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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AnalyticsOperatingSystemCounts200ResponseOsesInner;

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
 * AnalyticsOperatingSystemCounts200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AnalyticsOperatingSystemCounts200Response {
  public static final String SERIALIZED_NAME_OSES = "oses";
  @SerializedName(SERIALIZED_NAME_OSES)
  private List<AnalyticsOperatingSystemCounts200ResponseOsesInner> oses = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Long total;

  public AnalyticsOperatingSystemCounts200Response() {
  }

  public AnalyticsOperatingSystemCounts200Response oses(List<AnalyticsOperatingSystemCounts200ResponseOsesInner> oses) {
    this.oses = oses;
    return this;
  }

  public AnalyticsOperatingSystemCounts200Response addOsesItem(AnalyticsOperatingSystemCounts200ResponseOsesInner osesItem) {
    if (this.oses == null) {
      this.oses = new ArrayList<>();
    }
    this.oses.add(osesItem);
    return this;
  }

  /**
   * Get oses
   * @return oses
   */
  @javax.annotation.Nullable
  public List<AnalyticsOperatingSystemCounts200ResponseOsesInner> getOses() {
    return oses;
  }

  public void setOses(List<AnalyticsOperatingSystemCounts200ResponseOsesInner> oses) {
    this.oses = oses;
  }


  public AnalyticsOperatingSystemCounts200Response total(Long total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public Long getTotal() {
    return total;
  }

  public void setTotal(Long total) {
    this.total = total;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalyticsOperatingSystemCounts200Response analyticsOperatingSystemCounts200Response = (AnalyticsOperatingSystemCounts200Response) o;
    return Objects.equals(this.oses, analyticsOperatingSystemCounts200Response.oses) &&
        Objects.equals(this.total, analyticsOperatingSystemCounts200Response.total);
  }

  @Override
  public int hashCode() {
    return Objects.hash(oses, total);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalyticsOperatingSystemCounts200Response {\n");
    sb.append("    oses: ").append(toIndentedString(oses)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("oses");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AnalyticsOperatingSystemCounts200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AnalyticsOperatingSystemCounts200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AnalyticsOperatingSystemCounts200Response is not found in the empty JSON string", AnalyticsOperatingSystemCounts200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AnalyticsOperatingSystemCounts200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AnalyticsOperatingSystemCounts200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("oses") != null && !jsonObj.get("oses").isJsonNull()) {
        JsonArray jsonArrayoses = jsonObj.getAsJsonArray("oses");
        if (jsonArrayoses != null) {
          // ensure the json data is an array
          if (!jsonObj.get("oses").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `oses` to be an array in the JSON string but got `%s`", jsonObj.get("oses").toString()));
          }

          // validate the optional field `oses` (array)
          for (int i = 0; i < jsonArrayoses.size(); i++) {
            AnalyticsOperatingSystemCounts200ResponseOsesInner.validateJsonElement(jsonArrayoses.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AnalyticsOperatingSystemCounts200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AnalyticsOperatingSystemCounts200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AnalyticsOperatingSystemCounts200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AnalyticsOperatingSystemCounts200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<AnalyticsOperatingSystemCounts200Response>() {
           @Override
           public void write(JsonWriter out, AnalyticsOperatingSystemCounts200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AnalyticsOperatingSystemCounts200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AnalyticsOperatingSystemCounts200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AnalyticsOperatingSystemCounts200Response
   * @throws IOException if the JSON string is invalid with respect to AnalyticsOperatingSystemCounts200Response
   */
  public static AnalyticsOperatingSystemCounts200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AnalyticsOperatingSystemCounts200Response.class);
  }

  /**
   * Convert an instance of AnalyticsOperatingSystemCounts200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

