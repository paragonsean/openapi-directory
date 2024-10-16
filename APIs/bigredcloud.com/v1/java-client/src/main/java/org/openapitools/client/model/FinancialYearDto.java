/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
 * FinancialYearDto
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:05.666566-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FinancialYearDto {
  public static final String SERIALIZED_NAME_FIRST_MONTH = "firstMonth";
  @SerializedName(SERIALIZED_NAME_FIRST_MONTH)
  private Integer firstMonth;

  public static final String SERIALIZED_NAME_START_MONTH = "startMonth";
  @SerializedName(SERIALIZED_NAME_START_MONTH)
  private Integer startMonth;

  public static final String SERIALIZED_NAME_START_YEAR = "startYear";
  @SerializedName(SERIALIZED_NAME_START_YEAR)
  private Integer startYear;

  public FinancialYearDto() {
  }

  public FinancialYearDto firstMonth(Integer firstMonth) {
    this.firstMonth = firstMonth;
    return this;
  }

  /**
   * Get firstMonth
   * @return firstMonth
   */
  @javax.annotation.Nullable
  public Integer getFirstMonth() {
    return firstMonth;
  }

  public void setFirstMonth(Integer firstMonth) {
    this.firstMonth = firstMonth;
  }


  public FinancialYearDto startMonth(Integer startMonth) {
    this.startMonth = startMonth;
    return this;
  }

  /**
   * Get startMonth
   * @return startMonth
   */
  @javax.annotation.Nullable
  public Integer getStartMonth() {
    return startMonth;
  }

  public void setStartMonth(Integer startMonth) {
    this.startMonth = startMonth;
  }


  public FinancialYearDto startYear(Integer startYear) {
    this.startYear = startYear;
    return this;
  }

  /**
   * Get startYear
   * @return startYear
   */
  @javax.annotation.Nullable
  public Integer getStartYear() {
    return startYear;
  }

  public void setStartYear(Integer startYear) {
    this.startYear = startYear;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FinancialYearDto financialYearDto = (FinancialYearDto) o;
    return Objects.equals(this.firstMonth, financialYearDto.firstMonth) &&
        Objects.equals(this.startMonth, financialYearDto.startMonth) &&
        Objects.equals(this.startYear, financialYearDto.startYear);
  }

  @Override
  public int hashCode() {
    return Objects.hash(firstMonth, startMonth, startYear);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FinancialYearDto {\n");
    sb.append("    firstMonth: ").append(toIndentedString(firstMonth)).append("\n");
    sb.append("    startMonth: ").append(toIndentedString(startMonth)).append("\n");
    sb.append("    startYear: ").append(toIndentedString(startYear)).append("\n");
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
    openapiFields.add("firstMonth");
    openapiFields.add("startMonth");
    openapiFields.add("startYear");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FinancialYearDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FinancialYearDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FinancialYearDto is not found in the empty JSON string", FinancialYearDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FinancialYearDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FinancialYearDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FinancialYearDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FinancialYearDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FinancialYearDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FinancialYearDto.class));

       return (TypeAdapter<T>) new TypeAdapter<FinancialYearDto>() {
           @Override
           public void write(JsonWriter out, FinancialYearDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FinancialYearDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FinancialYearDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FinancialYearDto
   * @throws IOException if the JSON string is invalid with respect to FinancialYearDto
   */
  public static FinancialYearDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FinancialYearDto.class);
  }

  /**
   * Convert an instance of FinancialYearDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

