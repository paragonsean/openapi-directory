/*
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
 * OverallQualityResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:42.973620-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OverallQualityResponse {
  public static final String SERIALIZED_NAME_DATA_QUALITY = "data_quality";
  @SerializedName(SERIALIZED_NAME_DATA_QUALITY)
  private Integer dataQuality;

  public static final String SERIALIZED_NAME_END_DATE = "end_date";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_ROW_COUNT = "row_count";
  @SerializedName(SERIALIZED_NAME_ROW_COUNT)
  private Integer rowCount;

  public static final String SERIALIZED_NAME_SITES = "sites";
  @SerializedName(SERIALIZED_NAME_SITES)
  private String sites;

  public static final String SERIALIZED_NAME_START_DATE = "start_date";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private String startDate;

  public OverallQualityResponse() {
  }

  public OverallQualityResponse dataQuality(Integer dataQuality) {
    this.dataQuality = dataQuality;
    return this;
  }

  /**
   * Get dataQuality
   * @return dataQuality
   */
  @javax.annotation.Nullable
  public Integer getDataQuality() {
    return dataQuality;
  }

  public void setDataQuality(Integer dataQuality) {
    this.dataQuality = dataQuality;
  }


  public OverallQualityResponse endDate(String endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public String getEndDate() {
    return endDate;
  }

  public void setEndDate(String endDate) {
    this.endDate = endDate;
  }


  public OverallQualityResponse rowCount(Integer rowCount) {
    this.rowCount = rowCount;
    return this;
  }

  /**
   * Get rowCount
   * @return rowCount
   */
  @javax.annotation.Nullable
  public Integer getRowCount() {
    return rowCount;
  }

  public void setRowCount(Integer rowCount) {
    this.rowCount = rowCount;
  }


  public OverallQualityResponse sites(String sites) {
    this.sites = sites;
    return this;
  }

  /**
   * Get sites
   * @return sites
   */
  @javax.annotation.Nullable
  public String getSites() {
    return sites;
  }

  public void setSites(String sites) {
    this.sites = sites;
  }


  public OverallQualityResponse startDate(String startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public String getStartDate() {
    return startDate;
  }

  public void setStartDate(String startDate) {
    this.startDate = startDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OverallQualityResponse overallQualityResponse = (OverallQualityResponse) o;
    return Objects.equals(this.dataQuality, overallQualityResponse.dataQuality) &&
        Objects.equals(this.endDate, overallQualityResponse.endDate) &&
        Objects.equals(this.rowCount, overallQualityResponse.rowCount) &&
        Objects.equals(this.sites, overallQualityResponse.sites) &&
        Objects.equals(this.startDate, overallQualityResponse.startDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dataQuality, endDate, rowCount, sites, startDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OverallQualityResponse {\n");
    sb.append("    dataQuality: ").append(toIndentedString(dataQuality)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    rowCount: ").append(toIndentedString(rowCount)).append("\n");
    sb.append("    sites: ").append(toIndentedString(sites)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
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
    openapiFields.add("data_quality");
    openapiFields.add("end_date");
    openapiFields.add("row_count");
    openapiFields.add("sites");
    openapiFields.add("start_date");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OverallQualityResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OverallQualityResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OverallQualityResponse is not found in the empty JSON string", OverallQualityResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OverallQualityResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OverallQualityResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("end_date") != null && !jsonObj.get("end_date").isJsonNull()) && !jsonObj.get("end_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_date").toString()));
      }
      if ((jsonObj.get("sites") != null && !jsonObj.get("sites").isJsonNull()) && !jsonObj.get("sites").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sites` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sites").toString()));
      }
      if ((jsonObj.get("start_date") != null && !jsonObj.get("start_date").isJsonNull()) && !jsonObj.get("start_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `start_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("start_date").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OverallQualityResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OverallQualityResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OverallQualityResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OverallQualityResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<OverallQualityResponse>() {
           @Override
           public void write(JsonWriter out, OverallQualityResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OverallQualityResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OverallQualityResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OverallQualityResponse
   * @throws IOException if the JSON string is invalid with respect to OverallQualityResponse
   */
  public static OverallQualityResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OverallQualityResponse.class);
  }

  /**
   * Convert an instance of OverallQualityResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

