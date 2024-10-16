/*
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
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
 * SettlementDailyStatsSchema
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SettlementDailyStatsSchema {
  public static final String SERIALIZED_NAME_B2B = "b2b";
  @SerializedName(SERIALIZED_NAME_B2B)
  private Integer b2b;

  public static final String SERIALIZED_NAME_B2C = "b2c";
  @SerializedName(SERIALIZED_NAME_B2C)
  private Integer b2c;

  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Integer count;

  public static final String SERIALIZED_NAME_DAY = "day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private String day;

  public static final String SERIALIZED_NAME_DAY_RAW = "day_raw";
  @SerializedName(SERIALIZED_NAME_DAY_RAW)
  private String dayRaw;

  public static final String SERIALIZED_NAME_EU_B2B = "eu_b2b";
  @SerializedName(SERIALIZED_NAME_EU_B2B)
  private Integer euB2b;

  public static final String SERIALIZED_NAME_EU_TAXED = "eu_taxed";
  @SerializedName(SERIALIZED_NAME_EU_TAXED)
  private Integer euTaxed;

  public static final String SERIALIZED_NAME_EU_TOTAL = "eu_total";
  @SerializedName(SERIALIZED_NAME_EU_TOTAL)
  private Integer euTotal;

  public static final String SERIALIZED_NAME_UNTAXED = "untaxed";
  @SerializedName(SERIALIZED_NAME_UNTAXED)
  private Integer untaxed;

  public SettlementDailyStatsSchema() {
  }

  public SettlementDailyStatsSchema b2b(Integer b2b) {
    this.b2b = b2b;
    return this;
  }

  /**
   * B2B transaction count.
   * @return b2b
   */
  @javax.annotation.Nullable
  public Integer getB2b() {
    return b2b;
  }

  public void setB2b(Integer b2b) {
    this.b2b = b2b;
  }


  public SettlementDailyStatsSchema b2c(Integer b2c) {
    this.b2c = b2c;
    return this;
  }

  /**
   * B2C transaction count.
   * @return b2c
   */
  @javax.annotation.Nullable
  public Integer getB2c() {
    return b2c;
  }

  public void setB2c(Integer b2c) {
    this.b2c = b2c;
  }


  public SettlementDailyStatsSchema count(Integer count) {
    this.count = count;
    return this;
  }

  /**
   * Total transaction count.
   * @return count
   */
  @javax.annotation.Nullable
  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }


  public SettlementDailyStatsSchema day(String day) {
    this.day = day;
    return this;
  }

  /**
   * Date for stats in yyyy-MM-dd format.
   * @return day
   */
  @javax.annotation.Nullable
  public String getDay() {
    return day;
  }

  public void setDay(String day) {
    this.day = day;
  }


  public SettlementDailyStatsSchema dayRaw(String dayRaw) {
    this.dayRaw = dayRaw;
    return this;
  }

  /**
   * Date for stats in yyyy-MM-dd&#39;T&#39;hh:mm:ss&#39;Z&#39; format.
   * @return dayRaw
   */
  @javax.annotation.Nullable
  public String getDayRaw() {
    return dayRaw;
  }

  public void setDayRaw(String dayRaw) {
    this.dayRaw = dayRaw;
  }


  public SettlementDailyStatsSchema euB2b(Integer euB2b) {
    this.euB2b = euB2b;
    return this;
  }

  /**
   * Total EU B2B transaction count.
   * @return euB2b
   */
  @javax.annotation.Nullable
  public Integer getEuB2b() {
    return euB2b;
  }

  public void setEuB2b(Integer euB2b) {
    this.euB2b = euB2b;
  }


  public SettlementDailyStatsSchema euTaxed(Integer euTaxed) {
    this.euTaxed = euTaxed;
    return this;
  }

  /**
   * Total EU Taxed transaction count.
   * @return euTaxed
   */
  @javax.annotation.Nullable
  public Integer getEuTaxed() {
    return euTaxed;
  }

  public void setEuTaxed(Integer euTaxed) {
    this.euTaxed = euTaxed;
  }


  public SettlementDailyStatsSchema euTotal(Integer euTotal) {
    this.euTotal = euTotal;
    return this;
  }

  /**
   * Total EU transaction count.
   * @return euTotal
   */
  @javax.annotation.Nullable
  public Integer getEuTotal() {
    return euTotal;
  }

  public void setEuTotal(Integer euTotal) {
    this.euTotal = euTotal;
  }


  public SettlementDailyStatsSchema untaxed(Integer untaxed) {
    this.untaxed = untaxed;
    return this;
  }

  /**
   * Untaxed transaction count.
   * @return untaxed
   */
  @javax.annotation.Nullable
  public Integer getUntaxed() {
    return untaxed;
  }

  public void setUntaxed(Integer untaxed) {
    this.untaxed = untaxed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SettlementDailyStatsSchema settlementDailyStatsSchema = (SettlementDailyStatsSchema) o;
    return Objects.equals(this.b2b, settlementDailyStatsSchema.b2b) &&
        Objects.equals(this.b2c, settlementDailyStatsSchema.b2c) &&
        Objects.equals(this.count, settlementDailyStatsSchema.count) &&
        Objects.equals(this.day, settlementDailyStatsSchema.day) &&
        Objects.equals(this.dayRaw, settlementDailyStatsSchema.dayRaw) &&
        Objects.equals(this.euB2b, settlementDailyStatsSchema.euB2b) &&
        Objects.equals(this.euTaxed, settlementDailyStatsSchema.euTaxed) &&
        Objects.equals(this.euTotal, settlementDailyStatsSchema.euTotal) &&
        Objects.equals(this.untaxed, settlementDailyStatsSchema.untaxed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(b2b, b2c, count, day, dayRaw, euB2b, euTaxed, euTotal, untaxed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SettlementDailyStatsSchema {\n");
    sb.append("    b2b: ").append(toIndentedString(b2b)).append("\n");
    sb.append("    b2c: ").append(toIndentedString(b2c)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    dayRaw: ").append(toIndentedString(dayRaw)).append("\n");
    sb.append("    euB2b: ").append(toIndentedString(euB2b)).append("\n");
    sb.append("    euTaxed: ").append(toIndentedString(euTaxed)).append("\n");
    sb.append("    euTotal: ").append(toIndentedString(euTotal)).append("\n");
    sb.append("    untaxed: ").append(toIndentedString(untaxed)).append("\n");
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
    openapiFields.add("b2b");
    openapiFields.add("b2c");
    openapiFields.add("count");
    openapiFields.add("day");
    openapiFields.add("day_raw");
    openapiFields.add("eu_b2b");
    openapiFields.add("eu_taxed");
    openapiFields.add("eu_total");
    openapiFields.add("untaxed");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SettlementDailyStatsSchema
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SettlementDailyStatsSchema.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SettlementDailyStatsSchema is not found in the empty JSON string", SettlementDailyStatsSchema.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SettlementDailyStatsSchema.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SettlementDailyStatsSchema` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("day") != null && !jsonObj.get("day").isJsonNull()) && !jsonObj.get("day").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `day` to be a primitive type in the JSON string but got `%s`", jsonObj.get("day").toString()));
      }
      if ((jsonObj.get("day_raw") != null && !jsonObj.get("day_raw").isJsonNull()) && !jsonObj.get("day_raw").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `day_raw` to be a primitive type in the JSON string but got `%s`", jsonObj.get("day_raw").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SettlementDailyStatsSchema.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SettlementDailyStatsSchema' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SettlementDailyStatsSchema> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SettlementDailyStatsSchema.class));

       return (TypeAdapter<T>) new TypeAdapter<SettlementDailyStatsSchema>() {
           @Override
           public void write(JsonWriter out, SettlementDailyStatsSchema value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SettlementDailyStatsSchema read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SettlementDailyStatsSchema given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SettlementDailyStatsSchema
   * @throws IOException if the JSON string is invalid with respect to SettlementDailyStatsSchema
   */
  public static SettlementDailyStatsSchema fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SettlementDailyStatsSchema.class);
  }

  /**
   * Convert an instance of SettlementDailyStatsSchema to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

