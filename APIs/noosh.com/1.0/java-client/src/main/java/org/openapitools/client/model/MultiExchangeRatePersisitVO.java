/*
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Java type: com.noosh.domain.nooshapi.persist.vo.MultiExchangeRatePersisitVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MultiExchangeRatePersisitVO {
  public static final String SERIALIZED_NAME_ACTIVATE_DATE = "activate_date";
  @SerializedName(SERIALIZED_NAME_ACTIVATE_DATE)
  private LocalDate activateDate;

  public static final String SERIALIZED_NAME_BU_CLIENT_WORKGROUP_ID = "buClientWorkgroupId";
  @SerializedName(SERIALIZED_NAME_BU_CLIENT_WORKGROUP_ID)
  private Long buClientWorkgroupId;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_RATE = "rate";
  @SerializedName(SERIALIZED_NAME_RATE)
  private Object rate = null;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public MultiExchangeRatePersisitVO() {
  }

  public MultiExchangeRatePersisitVO activateDate(LocalDate activateDate) {
    this.activateDate = activateDate;
    return this;
  }

  /**
   * 
   * @return activateDate
   */
  @javax.annotation.Nullable
  public LocalDate getActivateDate() {
    return activateDate;
  }

  public void setActivateDate(LocalDate activateDate) {
    this.activateDate = activateDate;
  }


  public MultiExchangeRatePersisitVO buClientWorkgroupId(Long buClientWorkgroupId) {
    this.buClientWorkgroupId = buClientWorkgroupId;
    return this;
  }

  /**
   * 
   * @return buClientWorkgroupId
   */
  @javax.annotation.Nullable
  public Long getBuClientWorkgroupId() {
    return buClientWorkgroupId;
  }

  public void setBuClientWorkgroupId(Long buClientWorkgroupId) {
    this.buClientWorkgroupId = buClientWorkgroupId;
  }


  public MultiExchangeRatePersisitVO currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * 
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public MultiExchangeRatePersisitVO rate(Object rate) {
    this.rate = rate;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return rate
   */
  @javax.annotation.Nullable
  public Object getRate() {
    return rate;
  }

  public void setRate(Object rate) {
    this.rate = rate;
  }


  public MultiExchangeRatePersisitVO target(String target) {
    this.target = target;
    return this;
  }

  /**
   * 
   * @return target
   */
  @javax.annotation.Nullable
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MultiExchangeRatePersisitVO multiExchangeRatePersisitVO = (MultiExchangeRatePersisitVO) o;
    return Objects.equals(this.activateDate, multiExchangeRatePersisitVO.activateDate) &&
        Objects.equals(this.buClientWorkgroupId, multiExchangeRatePersisitVO.buClientWorkgroupId) &&
        Objects.equals(this.currency, multiExchangeRatePersisitVO.currency) &&
        Objects.equals(this.rate, multiExchangeRatePersisitVO.rate) &&
        Objects.equals(this.target, multiExchangeRatePersisitVO.target);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activateDate, buClientWorkgroupId, currency, rate, target);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MultiExchangeRatePersisitVO {\n");
    sb.append("    activateDate: ").append(toIndentedString(activateDate)).append("\n");
    sb.append("    buClientWorkgroupId: ").append(toIndentedString(buClientWorkgroupId)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    rate: ").append(toIndentedString(rate)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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
    openapiFields.add("activate_date");
    openapiFields.add("buClientWorkgroupId");
    openapiFields.add("currency");
    openapiFields.add("rate");
    openapiFields.add("target");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MultiExchangeRatePersisitVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MultiExchangeRatePersisitVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MultiExchangeRatePersisitVO is not found in the empty JSON string", MultiExchangeRatePersisitVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MultiExchangeRatePersisitVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MultiExchangeRatePersisitVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if ((jsonObj.get("target") != null && !jsonObj.get("target").isJsonNull()) && !jsonObj.get("target").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `target` to be a primitive type in the JSON string but got `%s`", jsonObj.get("target").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MultiExchangeRatePersisitVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MultiExchangeRatePersisitVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MultiExchangeRatePersisitVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MultiExchangeRatePersisitVO.class));

       return (TypeAdapter<T>) new TypeAdapter<MultiExchangeRatePersisitVO>() {
           @Override
           public void write(JsonWriter out, MultiExchangeRatePersisitVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MultiExchangeRatePersisitVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MultiExchangeRatePersisitVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MultiExchangeRatePersisitVO
   * @throws IOException if the JSON string is invalid with respect to MultiExchangeRatePersisitVO
   */
  public static MultiExchangeRatePersisitVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MultiExchangeRatePersisitVO.class);
  }

  /**
   * Convert an instance of MultiExchangeRatePersisitVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

