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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.OrderWorkgroupLevelSimpleVO;

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
 * Java type: com.noosh.nooshapi.vo.OrderWorkgroupLevelListVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderWorkgroupLevelListVO {
  public static final String SERIALIZED_NAME_RESULTS = "results";
  @SerializedName(SERIALIZED_NAME_RESULTS)
  private List<OrderWorkgroupLevelSimpleVO> results = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS_CODE = "status_code";
  @SerializedName(SERIALIZED_NAME_STATUS_CODE)
  private Integer statusCode;

  public static final String SERIALIZED_NAME_STATUS_REASON = "status_reason";
  @SerializedName(SERIALIZED_NAME_STATUS_REASON)
  private String statusReason;

  public OrderWorkgroupLevelListVO() {
  }

  public OrderWorkgroupLevelListVO results(List<OrderWorkgroupLevelSimpleVO> results) {
    this.results = results;
    return this;
  }

  public OrderWorkgroupLevelListVO addResultsItem(OrderWorkgroupLevelSimpleVO resultsItem) {
    if (this.results == null) {
      this.results = new ArrayList<>();
    }
    this.results.add(resultsItem);
    return this;
  }

  /**
   * 
   * @return results
   */
  @javax.annotation.Nullable
  public List<OrderWorkgroupLevelSimpleVO> getResults() {
    return results;
  }

  public void setResults(List<OrderWorkgroupLevelSimpleVO> results) {
    this.results = results;
  }


  public OrderWorkgroupLevelListVO statusCode(Integer statusCode) {
    this.statusCode = statusCode;
    return this;
  }

  /**
   * 
   * @return statusCode
   */
  @javax.annotation.Nullable
  public Integer getStatusCode() {
    return statusCode;
  }

  public void setStatusCode(Integer statusCode) {
    this.statusCode = statusCode;
  }


  public OrderWorkgroupLevelListVO statusReason(String statusReason) {
    this.statusReason = statusReason;
    return this;
  }

  /**
   * 
   * @return statusReason
   */
  @javax.annotation.Nullable
  public String getStatusReason() {
    return statusReason;
  }

  public void setStatusReason(String statusReason) {
    this.statusReason = statusReason;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderWorkgroupLevelListVO orderWorkgroupLevelListVO = (OrderWorkgroupLevelListVO) o;
    return Objects.equals(this.results, orderWorkgroupLevelListVO.results) &&
        Objects.equals(this.statusCode, orderWorkgroupLevelListVO.statusCode) &&
        Objects.equals(this.statusReason, orderWorkgroupLevelListVO.statusReason);
  }

  @Override
  public int hashCode() {
    return Objects.hash(results, statusCode, statusReason);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderWorkgroupLevelListVO {\n");
    sb.append("    results: ").append(toIndentedString(results)).append("\n");
    sb.append("    statusCode: ").append(toIndentedString(statusCode)).append("\n");
    sb.append("    statusReason: ").append(toIndentedString(statusReason)).append("\n");
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
    openapiFields.add("results");
    openapiFields.add("status_code");
    openapiFields.add("status_reason");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderWorkgroupLevelListVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderWorkgroupLevelListVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderWorkgroupLevelListVO is not found in the empty JSON string", OrderWorkgroupLevelListVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderWorkgroupLevelListVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderWorkgroupLevelListVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("results") != null && !jsonObj.get("results").isJsonNull()) {
        JsonArray jsonArrayresults = jsonObj.getAsJsonArray("results");
        if (jsonArrayresults != null) {
          // ensure the json data is an array
          if (!jsonObj.get("results").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `results` to be an array in the JSON string but got `%s`", jsonObj.get("results").toString()));
          }

          // validate the optional field `results` (array)
          for (int i = 0; i < jsonArrayresults.size(); i++) {
            OrderWorkgroupLevelSimpleVO.validateJsonElement(jsonArrayresults.get(i));
          };
        }
      }
      if ((jsonObj.get("status_reason") != null && !jsonObj.get("status_reason").isJsonNull()) && !jsonObj.get("status_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status_reason").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderWorkgroupLevelListVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderWorkgroupLevelListVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderWorkgroupLevelListVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderWorkgroupLevelListVO.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderWorkgroupLevelListVO>() {
           @Override
           public void write(JsonWriter out, OrderWorkgroupLevelListVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderWorkgroupLevelListVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderWorkgroupLevelListVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderWorkgroupLevelListVO
   * @throws IOException if the JSON string is invalid with respect to OrderWorkgroupLevelListVO
   */
  public static OrderWorkgroupLevelListVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderWorkgroupLevelListVO.class);
  }

  /**
   * Convert an instance of OrderWorkgroupLevelListVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

