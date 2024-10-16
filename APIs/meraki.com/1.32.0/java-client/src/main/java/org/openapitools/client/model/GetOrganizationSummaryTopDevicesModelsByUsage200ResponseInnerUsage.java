/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * Usage info in megabytes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage {
  public static final String SERIALIZED_NAME_AVERAGE = "average";
  @SerializedName(SERIALIZED_NAME_AVERAGE)
  private Float average;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Float total;

  public GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage() {
  }

  public GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage average(Float average) {
    this.average = average;
    return this;
  }

  /**
   * Average usage in megabytes
   * @return average
   */
  @javax.annotation.Nullable
  public Float getAverage() {
    return average;
  }

  public void setAverage(Float average) {
    this.average = average;
  }


  public GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage total(Float total) {
    this.total = total;
    return this;
  }

  /**
   * Total usage in megabytes
   * @return total
   */
  @javax.annotation.Nullable
  public Float getTotal() {
    return total;
  }

  public void setTotal(Float total) {
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
    GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage getOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage = (GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage) o;
    return Objects.equals(this.average, getOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.average) &&
        Objects.equals(this.total, getOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.total);
  }

  @Override
  public int hashCode() {
    return Objects.hash(average, total);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage {\n");
    sb.append("    average: ").append(toIndentedString(average)).append("\n");
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
    openapiFields.add("average");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage is not found in the empty JSON string", GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage>() {
           @Override
           public void write(JsonWriter out, GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage
   */
  public static GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage.class);
  }

  /**
   * Convert an instance of GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInnerUsage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

