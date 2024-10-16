/*
 * Native Ads Publisher API
 * This is a Native Ads Publisher API it provides same functionality as Native Ads Publisher Account GUI. 
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
 * Totals
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:20.189109-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Totals {
  public static final String SERIALIZED_NAME_TOTAL_CLICKS = "total_clicks";
  @SerializedName(SERIALIZED_NAME_TOTAL_CLICKS)
  private String totalClicks;

  public static final String SERIALIZED_NAME_TOTAL_CPC = "total_cpc";
  @SerializedName(SERIALIZED_NAME_TOTAL_CPC)
  private String totalCpc;

  public static final String SERIALIZED_NAME_TOTAL_CTR = "total_ctr";
  @SerializedName(SERIALIZED_NAME_TOTAL_CTR)
  private String totalCtr;

  public static final String SERIALIZED_NAME_TOTAL_EARNINGS = "total_earnings";
  @SerializedName(SERIALIZED_NAME_TOTAL_EARNINGS)
  private String totalEarnings;

  public static final String SERIALIZED_NAME_TOTAL_IMPRESSIONS = "total_impressions";
  @SerializedName(SERIALIZED_NAME_TOTAL_IMPRESSIONS)
  private String totalImpressions;

  public static final String SERIALIZED_NAME_TOTAL_NET_ECPM = "total_net_ecpm";
  @SerializedName(SERIALIZED_NAME_TOTAL_NET_ECPM)
  private String totalNetEcpm;

  public static final String SERIALIZED_NAME_TOTAL_RPM = "total_rpm";
  @SerializedName(SERIALIZED_NAME_TOTAL_RPM)
  private String totalRpm;

  public Totals() {
  }

  public Totals totalClicks(String totalClicks) {
    this.totalClicks = totalClicks;
    return this;
  }

  /**
   * Get totalClicks
   * @return totalClicks
   */
  @javax.annotation.Nullable
  public String getTotalClicks() {
    return totalClicks;
  }

  public void setTotalClicks(String totalClicks) {
    this.totalClicks = totalClicks;
  }


  public Totals totalCpc(String totalCpc) {
    this.totalCpc = totalCpc;
    return this;
  }

  /**
   * Get totalCpc
   * @return totalCpc
   */
  @javax.annotation.Nullable
  public String getTotalCpc() {
    return totalCpc;
  }

  public void setTotalCpc(String totalCpc) {
    this.totalCpc = totalCpc;
  }


  public Totals totalCtr(String totalCtr) {
    this.totalCtr = totalCtr;
    return this;
  }

  /**
   * Get totalCtr
   * @return totalCtr
   */
  @javax.annotation.Nullable
  public String getTotalCtr() {
    return totalCtr;
  }

  public void setTotalCtr(String totalCtr) {
    this.totalCtr = totalCtr;
  }


  public Totals totalEarnings(String totalEarnings) {
    this.totalEarnings = totalEarnings;
    return this;
  }

  /**
   * Get totalEarnings
   * @return totalEarnings
   */
  @javax.annotation.Nullable
  public String getTotalEarnings() {
    return totalEarnings;
  }

  public void setTotalEarnings(String totalEarnings) {
    this.totalEarnings = totalEarnings;
  }


  public Totals totalImpressions(String totalImpressions) {
    this.totalImpressions = totalImpressions;
    return this;
  }

  /**
   * Get totalImpressions
   * @return totalImpressions
   */
  @javax.annotation.Nullable
  public String getTotalImpressions() {
    return totalImpressions;
  }

  public void setTotalImpressions(String totalImpressions) {
    this.totalImpressions = totalImpressions;
  }


  public Totals totalNetEcpm(String totalNetEcpm) {
    this.totalNetEcpm = totalNetEcpm;
    return this;
  }

  /**
   * Get totalNetEcpm
   * @return totalNetEcpm
   */
  @javax.annotation.Nullable
  public String getTotalNetEcpm() {
    return totalNetEcpm;
  }

  public void setTotalNetEcpm(String totalNetEcpm) {
    this.totalNetEcpm = totalNetEcpm;
  }


  public Totals totalRpm(String totalRpm) {
    this.totalRpm = totalRpm;
    return this;
  }

  /**
   * Get totalRpm
   * @return totalRpm
   */
  @javax.annotation.Nullable
  public String getTotalRpm() {
    return totalRpm;
  }

  public void setTotalRpm(String totalRpm) {
    this.totalRpm = totalRpm;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Totals totals = (Totals) o;
    return Objects.equals(this.totalClicks, totals.totalClicks) &&
        Objects.equals(this.totalCpc, totals.totalCpc) &&
        Objects.equals(this.totalCtr, totals.totalCtr) &&
        Objects.equals(this.totalEarnings, totals.totalEarnings) &&
        Objects.equals(this.totalImpressions, totals.totalImpressions) &&
        Objects.equals(this.totalNetEcpm, totals.totalNetEcpm) &&
        Objects.equals(this.totalRpm, totals.totalRpm);
  }

  @Override
  public int hashCode() {
    return Objects.hash(totalClicks, totalCpc, totalCtr, totalEarnings, totalImpressions, totalNetEcpm, totalRpm);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Totals {\n");
    sb.append("    totalClicks: ").append(toIndentedString(totalClicks)).append("\n");
    sb.append("    totalCpc: ").append(toIndentedString(totalCpc)).append("\n");
    sb.append("    totalCtr: ").append(toIndentedString(totalCtr)).append("\n");
    sb.append("    totalEarnings: ").append(toIndentedString(totalEarnings)).append("\n");
    sb.append("    totalImpressions: ").append(toIndentedString(totalImpressions)).append("\n");
    sb.append("    totalNetEcpm: ").append(toIndentedString(totalNetEcpm)).append("\n");
    sb.append("    totalRpm: ").append(toIndentedString(totalRpm)).append("\n");
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
    openapiFields.add("total_clicks");
    openapiFields.add("total_cpc");
    openapiFields.add("total_ctr");
    openapiFields.add("total_earnings");
    openapiFields.add("total_impressions");
    openapiFields.add("total_net_ecpm");
    openapiFields.add("total_rpm");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Totals
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Totals.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Totals is not found in the empty JSON string", Totals.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Totals.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Totals` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("total_clicks") != null && !jsonObj.get("total_clicks").isJsonNull()) && !jsonObj.get("total_clicks").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_clicks` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_clicks").toString()));
      }
      if ((jsonObj.get("total_cpc") != null && !jsonObj.get("total_cpc").isJsonNull()) && !jsonObj.get("total_cpc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_cpc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_cpc").toString()));
      }
      if ((jsonObj.get("total_ctr") != null && !jsonObj.get("total_ctr").isJsonNull()) && !jsonObj.get("total_ctr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_ctr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_ctr").toString()));
      }
      if ((jsonObj.get("total_earnings") != null && !jsonObj.get("total_earnings").isJsonNull()) && !jsonObj.get("total_earnings").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_earnings` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_earnings").toString()));
      }
      if ((jsonObj.get("total_impressions") != null && !jsonObj.get("total_impressions").isJsonNull()) && !jsonObj.get("total_impressions").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_impressions` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_impressions").toString()));
      }
      if ((jsonObj.get("total_net_ecpm") != null && !jsonObj.get("total_net_ecpm").isJsonNull()) && !jsonObj.get("total_net_ecpm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_net_ecpm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_net_ecpm").toString()));
      }
      if ((jsonObj.get("total_rpm") != null && !jsonObj.get("total_rpm").isJsonNull()) && !jsonObj.get("total_rpm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `total_rpm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("total_rpm").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Totals.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Totals' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Totals> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Totals.class));

       return (TypeAdapter<T>) new TypeAdapter<Totals>() {
           @Override
           public void write(JsonWriter out, Totals value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Totals read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Totals given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Totals
   * @throws IOException if the JSON string is invalid with respect to Totals
   */
  public static Totals fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Totals.class);
  }

  /**
   * Convert an instance of Totals to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

