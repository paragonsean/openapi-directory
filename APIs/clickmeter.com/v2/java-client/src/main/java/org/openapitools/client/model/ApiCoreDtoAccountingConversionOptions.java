/*
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
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
 * ApiCoreDtoAccountingConversionOptions
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:30.746224-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiCoreDtoAccountingConversionOptions {
  public static final String SERIALIZED_NAME_HIDE_COM_COST = "hideComCost";
  @SerializedName(SERIALIZED_NAME_HIDE_COM_COST)
  private Boolean hideComCost;

  public static final String SERIALIZED_NAME_HIDE_COST = "hideCost";
  @SerializedName(SERIALIZED_NAME_HIDE_COST)
  private Boolean hideCost;

  public static final String SERIALIZED_NAME_HIDE_COUNT = "hideCount";
  @SerializedName(SERIALIZED_NAME_HIDE_COUNT)
  private Boolean hideCount;

  public static final String SERIALIZED_NAME_HIDE_PARAMS = "hideParams";
  @SerializedName(SERIALIZED_NAME_HIDE_PARAMS)
  private Boolean hideParams;

  public static final String SERIALIZED_NAME_HIDE_VALUE = "hideValue";
  @SerializedName(SERIALIZED_NAME_HIDE_VALUE)
  private Boolean hideValue;

  public static final String SERIALIZED_NAME_PERCENT_COMMISSION = "percentCommission";
  @SerializedName(SERIALIZED_NAME_PERCENT_COMMISSION)
  private Integer percentCommission;

  public static final String SERIALIZED_NAME_PERCENT_VALUE = "percentValue";
  @SerializedName(SERIALIZED_NAME_PERCENT_VALUE)
  private Integer percentValue;

  public ApiCoreDtoAccountingConversionOptions() {
  }

  public ApiCoreDtoAccountingConversionOptions hideComCost(Boolean hideComCost) {
    this.hideComCost = hideComCost;
    return this;
  }

  /**
   * Get hideComCost
   * @return hideComCost
   */
  @javax.annotation.Nullable
  public Boolean getHideComCost() {
    return hideComCost;
  }

  public void setHideComCost(Boolean hideComCost) {
    this.hideComCost = hideComCost;
  }


  public ApiCoreDtoAccountingConversionOptions hideCost(Boolean hideCost) {
    this.hideCost = hideCost;
    return this;
  }

  /**
   * Get hideCost
   * @return hideCost
   */
  @javax.annotation.Nullable
  public Boolean getHideCost() {
    return hideCost;
  }

  public void setHideCost(Boolean hideCost) {
    this.hideCost = hideCost;
  }


  public ApiCoreDtoAccountingConversionOptions hideCount(Boolean hideCount) {
    this.hideCount = hideCount;
    return this;
  }

  /**
   * Get hideCount
   * @return hideCount
   */
  @javax.annotation.Nullable
  public Boolean getHideCount() {
    return hideCount;
  }

  public void setHideCount(Boolean hideCount) {
    this.hideCount = hideCount;
  }


  public ApiCoreDtoAccountingConversionOptions hideParams(Boolean hideParams) {
    this.hideParams = hideParams;
    return this;
  }

  /**
   * Get hideParams
   * @return hideParams
   */
  @javax.annotation.Nullable
  public Boolean getHideParams() {
    return hideParams;
  }

  public void setHideParams(Boolean hideParams) {
    this.hideParams = hideParams;
  }


  public ApiCoreDtoAccountingConversionOptions hideValue(Boolean hideValue) {
    this.hideValue = hideValue;
    return this;
  }

  /**
   * Get hideValue
   * @return hideValue
   */
  @javax.annotation.Nullable
  public Boolean getHideValue() {
    return hideValue;
  }

  public void setHideValue(Boolean hideValue) {
    this.hideValue = hideValue;
  }


  public ApiCoreDtoAccountingConversionOptions percentCommission(Integer percentCommission) {
    this.percentCommission = percentCommission;
    return this;
  }

  /**
   * Get percentCommission
   * @return percentCommission
   */
  @javax.annotation.Nullable
  public Integer getPercentCommission() {
    return percentCommission;
  }

  public void setPercentCommission(Integer percentCommission) {
    this.percentCommission = percentCommission;
  }


  public ApiCoreDtoAccountingConversionOptions percentValue(Integer percentValue) {
    this.percentValue = percentValue;
    return this;
  }

  /**
   * Get percentValue
   * @return percentValue
   */
  @javax.annotation.Nullable
  public Integer getPercentValue() {
    return percentValue;
  }

  public void setPercentValue(Integer percentValue) {
    this.percentValue = percentValue;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiCoreDtoAccountingConversionOptions apiCoreDtoAccountingConversionOptions = (ApiCoreDtoAccountingConversionOptions) o;
    return Objects.equals(this.hideComCost, apiCoreDtoAccountingConversionOptions.hideComCost) &&
        Objects.equals(this.hideCost, apiCoreDtoAccountingConversionOptions.hideCost) &&
        Objects.equals(this.hideCount, apiCoreDtoAccountingConversionOptions.hideCount) &&
        Objects.equals(this.hideParams, apiCoreDtoAccountingConversionOptions.hideParams) &&
        Objects.equals(this.hideValue, apiCoreDtoAccountingConversionOptions.hideValue) &&
        Objects.equals(this.percentCommission, apiCoreDtoAccountingConversionOptions.percentCommission) &&
        Objects.equals(this.percentValue, apiCoreDtoAccountingConversionOptions.percentValue);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hideComCost, hideCost, hideCount, hideParams, hideValue, percentCommission, percentValue);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiCoreDtoAccountingConversionOptions {\n");
    sb.append("    hideComCost: ").append(toIndentedString(hideComCost)).append("\n");
    sb.append("    hideCost: ").append(toIndentedString(hideCost)).append("\n");
    sb.append("    hideCount: ").append(toIndentedString(hideCount)).append("\n");
    sb.append("    hideParams: ").append(toIndentedString(hideParams)).append("\n");
    sb.append("    hideValue: ").append(toIndentedString(hideValue)).append("\n");
    sb.append("    percentCommission: ").append(toIndentedString(percentCommission)).append("\n");
    sb.append("    percentValue: ").append(toIndentedString(percentValue)).append("\n");
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
    openapiFields.add("hideComCost");
    openapiFields.add("hideCost");
    openapiFields.add("hideCount");
    openapiFields.add("hideParams");
    openapiFields.add("hideValue");
    openapiFields.add("percentCommission");
    openapiFields.add("percentValue");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiCoreDtoAccountingConversionOptions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiCoreDtoAccountingConversionOptions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiCoreDtoAccountingConversionOptions is not found in the empty JSON string", ApiCoreDtoAccountingConversionOptions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiCoreDtoAccountingConversionOptions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiCoreDtoAccountingConversionOptions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiCoreDtoAccountingConversionOptions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiCoreDtoAccountingConversionOptions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiCoreDtoAccountingConversionOptions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiCoreDtoAccountingConversionOptions.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiCoreDtoAccountingConversionOptions>() {
           @Override
           public void write(JsonWriter out, ApiCoreDtoAccountingConversionOptions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiCoreDtoAccountingConversionOptions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiCoreDtoAccountingConversionOptions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiCoreDtoAccountingConversionOptions
   * @throws IOException if the JSON string is invalid with respect to ApiCoreDtoAccountingConversionOptions
   */
  public static ApiCoreDtoAccountingConversionOptions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiCoreDtoAccountingConversionOptions.class);
  }

  /**
   * Convert an instance of ApiCoreDtoAccountingConversionOptions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

