/*
 * OpenUV - Global Real-Time UV Index Forecast API
 * The missing minimalistic JSON real-time UV Index API for awesome Developers, Innovators and Smart Home Enthusiasts
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
import java.math.BigDecimal;
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
 * ProtectionResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:48.126805-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProtectionResult {
  public static final String SERIALIZED_NAME_OZONE = "ozone";
  @SerializedName(SERIALIZED_NAME_OZONE)
  private BigDecimal ozone;

  public static final String SERIALIZED_NAME_OZONE_TIME = "ozone_time";
  @SerializedName(SERIALIZED_NAME_OZONE_TIME)
  private String ozoneTime;

  public static final String SERIALIZED_NAME_UV = "uv";
  @SerializedName(SERIALIZED_NAME_UV)
  private BigDecimal uv;

  public static final String SERIALIZED_NAME_UV_MAX = "uv_max";
  @SerializedName(SERIALIZED_NAME_UV_MAX)
  private BigDecimal uvMax;

  public static final String SERIALIZED_NAME_UV_MAX_TIME = "uv_max_time";
  @SerializedName(SERIALIZED_NAME_UV_MAX_TIME)
  private String uvMaxTime;

  public static final String SERIALIZED_NAME_UV_TIME = "uv_time";
  @SerializedName(SERIALIZED_NAME_UV_TIME)
  private String uvTime;

  public ProtectionResult() {
  }

  public ProtectionResult ozone(BigDecimal ozone) {
    this.ozone = ozone;
    return this;
  }

  /**
   * Get ozone
   * @return ozone
   */
  @javax.annotation.Nonnull
  public BigDecimal getOzone() {
    return ozone;
  }

  public void setOzone(BigDecimal ozone) {
    this.ozone = ozone;
  }


  public ProtectionResult ozoneTime(String ozoneTime) {
    this.ozoneTime = ozoneTime;
    return this;
  }

  /**
   * Get ozoneTime
   * @return ozoneTime
   */
  @javax.annotation.Nonnull
  public String getOzoneTime() {
    return ozoneTime;
  }

  public void setOzoneTime(String ozoneTime) {
    this.ozoneTime = ozoneTime;
  }


  public ProtectionResult uv(BigDecimal uv) {
    this.uv = uv;
    return this;
  }

  /**
   * Get uv
   * @return uv
   */
  @javax.annotation.Nonnull
  public BigDecimal getUv() {
    return uv;
  }

  public void setUv(BigDecimal uv) {
    this.uv = uv;
  }


  public ProtectionResult uvMax(BigDecimal uvMax) {
    this.uvMax = uvMax;
    return this;
  }

  /**
   * Get uvMax
   * @return uvMax
   */
  @javax.annotation.Nonnull
  public BigDecimal getUvMax() {
    return uvMax;
  }

  public void setUvMax(BigDecimal uvMax) {
    this.uvMax = uvMax;
  }


  public ProtectionResult uvMaxTime(String uvMaxTime) {
    this.uvMaxTime = uvMaxTime;
    return this;
  }

  /**
   * Get uvMaxTime
   * @return uvMaxTime
   */
  @javax.annotation.Nonnull
  public String getUvMaxTime() {
    return uvMaxTime;
  }

  public void setUvMaxTime(String uvMaxTime) {
    this.uvMaxTime = uvMaxTime;
  }


  public ProtectionResult uvTime(String uvTime) {
    this.uvTime = uvTime;
    return this;
  }

  /**
   * Get uvTime
   * @return uvTime
   */
  @javax.annotation.Nonnull
  public String getUvTime() {
    return uvTime;
  }

  public void setUvTime(String uvTime) {
    this.uvTime = uvTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProtectionResult protectionResult = (ProtectionResult) o;
    return Objects.equals(this.ozone, protectionResult.ozone) &&
        Objects.equals(this.ozoneTime, protectionResult.ozoneTime) &&
        Objects.equals(this.uv, protectionResult.uv) &&
        Objects.equals(this.uvMax, protectionResult.uvMax) &&
        Objects.equals(this.uvMaxTime, protectionResult.uvMaxTime) &&
        Objects.equals(this.uvTime, protectionResult.uvTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ozone, ozoneTime, uv, uvMax, uvMaxTime, uvTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProtectionResult {\n");
    sb.append("    ozone: ").append(toIndentedString(ozone)).append("\n");
    sb.append("    ozoneTime: ").append(toIndentedString(ozoneTime)).append("\n");
    sb.append("    uv: ").append(toIndentedString(uv)).append("\n");
    sb.append("    uvMax: ").append(toIndentedString(uvMax)).append("\n");
    sb.append("    uvMaxTime: ").append(toIndentedString(uvMaxTime)).append("\n");
    sb.append("    uvTime: ").append(toIndentedString(uvTime)).append("\n");
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
    openapiFields.add("ozone");
    openapiFields.add("ozone_time");
    openapiFields.add("uv");
    openapiFields.add("uv_max");
    openapiFields.add("uv_max_time");
    openapiFields.add("uv_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ozone");
    openapiRequiredFields.add("ozone_time");
    openapiRequiredFields.add("uv");
    openapiRequiredFields.add("uv_max");
    openapiRequiredFields.add("uv_max_time");
    openapiRequiredFields.add("uv_time");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProtectionResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProtectionResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProtectionResult is not found in the empty JSON string", ProtectionResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProtectionResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProtectionResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProtectionResult.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("ozone_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ozone_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ozone_time").toString()));
      }
      if (!jsonObj.get("uv_max_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uv_max_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uv_max_time").toString()));
      }
      if (!jsonObj.get("uv_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uv_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uv_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProtectionResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProtectionResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProtectionResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProtectionResult.class));

       return (TypeAdapter<T>) new TypeAdapter<ProtectionResult>() {
           @Override
           public void write(JsonWriter out, ProtectionResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProtectionResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProtectionResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProtectionResult
   * @throws IOException if the JSON string is invalid with respect to ProtectionResult
   */
  public static ProtectionResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProtectionResult.class);
  }

  /**
   * Convert an instance of ProtectionResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

