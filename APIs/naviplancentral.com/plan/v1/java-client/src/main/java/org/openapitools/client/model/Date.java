/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import java.time.OffsetDateTime;
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
 * Date
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Date {
  public static final String SERIALIZED_NAME_DAY = "day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private Integer day;

  public static final String SERIALIZED_NAME_FORMATTED = "formatted";
  @SerializedName(SERIALIZED_NAME_FORMATTED)
  private String formatted;

  public static final String SERIALIZED_NAME_FORMATTED_M_M_M_MDDYYYY = "formattedMMMMddyyyy";
  @SerializedName(SERIALIZED_NAME_FORMATTED_M_M_M_MDDYYYY)
  private String formattedMMMMddyyyy;

  public static final String SERIALIZED_NAME_FORMATTED_M_M_MDD = "formattedMMMdd";
  @SerializedName(SERIALIZED_NAME_FORMATTED_M_M_MDD)
  private String formattedMMMdd;

  public static final String SERIALIZED_NAME_FORMATTED_M_M_MDDYYYY = "formattedMMMddyyyy";
  @SerializedName(SERIALIZED_NAME_FORMATTED_M_M_MDDYYYY)
  private String formattedMMMddyyyy;

  public static final String SERIALIZED_NAME_FORMATTED_M_M_MYYYY = "formattedMMMyyyy";
  @SerializedName(SERIALIZED_NAME_FORMATTED_M_M_MYYYY)
  private String formattedMMMyyyy;

  public static final String SERIALIZED_NAME_FORMATTED_N_A = "formattedNA";
  @SerializedName(SERIALIZED_NAME_FORMATTED_N_A)
  private String formattedNA;

  public static final String SERIALIZED_NAME_MONTH = "month";
  @SerializedName(SERIALIZED_NAME_MONTH)
  private Integer month;

  public static final String SERIALIZED_NAME_TO_DATE_TIME = "toDateTime";
  @SerializedName(SERIALIZED_NAME_TO_DATE_TIME)
  private OffsetDateTime toDateTime;

  public static final String SERIALIZED_NAME_URL_ENCODED = "urlEncoded";
  @SerializedName(SERIALIZED_NAME_URL_ENCODED)
  private String urlEncoded;

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public Date() {
  }

  public Date(
     String formatted, 
     String formattedMMMMddyyyy, 
     String formattedMMMdd, 
     String formattedMMMddyyyy, 
     String formattedMMMyyyy, 
     String formattedNA, 
     OffsetDateTime toDateTime, 
     String urlEncoded
  ) {
    this();
    this.formatted = formatted;
    this.formattedMMMMddyyyy = formattedMMMMddyyyy;
    this.formattedMMMdd = formattedMMMdd;
    this.formattedMMMddyyyy = formattedMMMddyyyy;
    this.formattedMMMyyyy = formattedMMMyyyy;
    this.formattedNA = formattedNA;
    this.toDateTime = toDateTime;
    this.urlEncoded = urlEncoded;
  }

  public Date day(Integer day) {
    this.day = day;
    return this;
  }

  /**
   * Get day
   * @return day
   */
  @javax.annotation.Nullable
  public Integer getDay() {
    return day;
  }

  public void setDay(Integer day) {
    this.day = day;
  }


  /**
   * Get formatted
   * @return formatted
   */
  @javax.annotation.Nullable
  public String getFormatted() {
    return formatted;
  }



  /**
   * Get formattedMMMMddyyyy
   * @return formattedMMMMddyyyy
   */
  @javax.annotation.Nullable
  public String getFormattedMMMMddyyyy() {
    return formattedMMMMddyyyy;
  }



  /**
   * Get formattedMMMdd
   * @return formattedMMMdd
   */
  @javax.annotation.Nullable
  public String getFormattedMMMdd() {
    return formattedMMMdd;
  }



  /**
   * Get formattedMMMddyyyy
   * @return formattedMMMddyyyy
   */
  @javax.annotation.Nullable
  public String getFormattedMMMddyyyy() {
    return formattedMMMddyyyy;
  }



  /**
   * Get formattedMMMyyyy
   * @return formattedMMMyyyy
   */
  @javax.annotation.Nullable
  public String getFormattedMMMyyyy() {
    return formattedMMMyyyy;
  }



  /**
   * Get formattedNA
   * @return formattedNA
   */
  @javax.annotation.Nullable
  public String getFormattedNA() {
    return formattedNA;
  }



  public Date month(Integer month) {
    this.month = month;
    return this;
  }

  /**
   * Get month
   * @return month
   */
  @javax.annotation.Nullable
  public Integer getMonth() {
    return month;
  }

  public void setMonth(Integer month) {
    this.month = month;
  }


  /**
   * Get toDateTime
   * @return toDateTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getToDateTime() {
    return toDateTime;
  }



  /**
   * Get urlEncoded
   * @return urlEncoded
   */
  @javax.annotation.Nullable
  public String getUrlEncoded() {
    return urlEncoded;
  }



  public Date year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * Get year
   * @return year
   */
  @javax.annotation.Nullable
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Date date = (Date) o;
    return Objects.equals(this.day, date.day) &&
        Objects.equals(this.formatted, date.formatted) &&
        Objects.equals(this.formattedMMMMddyyyy, date.formattedMMMMddyyyy) &&
        Objects.equals(this.formattedMMMdd, date.formattedMMMdd) &&
        Objects.equals(this.formattedMMMddyyyy, date.formattedMMMddyyyy) &&
        Objects.equals(this.formattedMMMyyyy, date.formattedMMMyyyy) &&
        Objects.equals(this.formattedNA, date.formattedNA) &&
        Objects.equals(this.month, date.month) &&
        Objects.equals(this.toDateTime, date.toDateTime) &&
        Objects.equals(this.urlEncoded, date.urlEncoded) &&
        Objects.equals(this.year, date.year);
  }

  @Override
  public int hashCode() {
    return Objects.hash(day, formatted, formattedMMMMddyyyy, formattedMMMdd, formattedMMMddyyyy, formattedMMMyyyy, formattedNA, month, toDateTime, urlEncoded, year);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Date {\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    formatted: ").append(toIndentedString(formatted)).append("\n");
    sb.append("    formattedMMMMddyyyy: ").append(toIndentedString(formattedMMMMddyyyy)).append("\n");
    sb.append("    formattedMMMdd: ").append(toIndentedString(formattedMMMdd)).append("\n");
    sb.append("    formattedMMMddyyyy: ").append(toIndentedString(formattedMMMddyyyy)).append("\n");
    sb.append("    formattedMMMyyyy: ").append(toIndentedString(formattedMMMyyyy)).append("\n");
    sb.append("    formattedNA: ").append(toIndentedString(formattedNA)).append("\n");
    sb.append("    month: ").append(toIndentedString(month)).append("\n");
    sb.append("    toDateTime: ").append(toIndentedString(toDateTime)).append("\n");
    sb.append("    urlEncoded: ").append(toIndentedString(urlEncoded)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("day");
    openapiFields.add("formatted");
    openapiFields.add("formattedMMMMddyyyy");
    openapiFields.add("formattedMMMdd");
    openapiFields.add("formattedMMMddyyyy");
    openapiFields.add("formattedMMMyyyy");
    openapiFields.add("formattedNA");
    openapiFields.add("month");
    openapiFields.add("toDateTime");
    openapiFields.add("urlEncoded");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Date
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Date.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Date is not found in the empty JSON string", Date.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Date.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Date` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("formatted") != null && !jsonObj.get("formatted").isJsonNull()) && !jsonObj.get("formatted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formatted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formatted").toString()));
      }
      if ((jsonObj.get("formattedMMMMddyyyy") != null && !jsonObj.get("formattedMMMMddyyyy").isJsonNull()) && !jsonObj.get("formattedMMMMddyyyy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formattedMMMMddyyyy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formattedMMMMddyyyy").toString()));
      }
      if ((jsonObj.get("formattedMMMdd") != null && !jsonObj.get("formattedMMMdd").isJsonNull()) && !jsonObj.get("formattedMMMdd").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formattedMMMdd` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formattedMMMdd").toString()));
      }
      if ((jsonObj.get("formattedMMMddyyyy") != null && !jsonObj.get("formattedMMMddyyyy").isJsonNull()) && !jsonObj.get("formattedMMMddyyyy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formattedMMMddyyyy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formattedMMMddyyyy").toString()));
      }
      if ((jsonObj.get("formattedMMMyyyy") != null && !jsonObj.get("formattedMMMyyyy").isJsonNull()) && !jsonObj.get("formattedMMMyyyy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formattedMMMyyyy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formattedMMMyyyy").toString()));
      }
      if ((jsonObj.get("formattedNA") != null && !jsonObj.get("formattedNA").isJsonNull()) && !jsonObj.get("formattedNA").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formattedNA` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formattedNA").toString()));
      }
      if ((jsonObj.get("urlEncoded") != null && !jsonObj.get("urlEncoded").isJsonNull()) && !jsonObj.get("urlEncoded").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlEncoded` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlEncoded").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Date.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Date' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Date> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Date.class));

       return (TypeAdapter<T>) new TypeAdapter<Date>() {
           @Override
           public void write(JsonWriter out, Date value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Date read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Date given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Date
   * @throws IOException if the JSON string is invalid with respect to Date
   */
  public static Date fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Date.class);
  }

  /**
   * Convert an instance of Date to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

