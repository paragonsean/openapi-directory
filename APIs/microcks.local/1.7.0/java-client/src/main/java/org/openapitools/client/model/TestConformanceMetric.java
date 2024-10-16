/*
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
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
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.Trend;

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
 * Represents the test conformance metrics (current score, history and evolution trend) of a Service
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:29.619783-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TestConformanceMetric {
  public static final String SERIALIZED_NAME_AGGREGATION_LABEL_VALUE = "aggregationLabelValue";
  @SerializedName(SERIALIZED_NAME_AGGREGATION_LABEL_VALUE)
  private String aggregationLabelValue;

  public static final String SERIALIZED_NAME_CURRENT_SCORE = "currentScore";
  @SerializedName(SERIALIZED_NAME_CURRENT_SCORE)
  private Double currentScore;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LAST_UPDATE_DAY = "lastUpdateDay";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_DAY)
  private String lastUpdateDay;

  public static final String SERIALIZED_NAME_LATEST_SCORES = "latestScores";
  @SerializedName(SERIALIZED_NAME_LATEST_SCORES)
  private Map<String, BigDecimal> latestScores = new HashMap<>();

  public static final String SERIALIZED_NAME_LATEST_TREND = "latestTrend";
  @SerializedName(SERIALIZED_NAME_LATEST_TREND)
  private Trend latestTrend;

  public static final String SERIALIZED_NAME_MAX_POSSIBLE_SCORE = "maxPossibleScore";
  @SerializedName(SERIALIZED_NAME_MAX_POSSIBLE_SCORE)
  private Double maxPossibleScore;

  public static final String SERIALIZED_NAME_SERVICE_ID = "serviceId";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  public TestConformanceMetric() {
  }

  public TestConformanceMetric aggregationLabelValue(String aggregationLabelValue) {
    this.aggregationLabelValue = aggregationLabelValue;
    return this;
  }

  /**
   * Value of the label used for metrics aggregation (if any)
   * @return aggregationLabelValue
   */
  @javax.annotation.Nullable
  public String getAggregationLabelValue() {
    return aggregationLabelValue;
  }

  public void setAggregationLabelValue(String aggregationLabelValue) {
    this.aggregationLabelValue = aggregationLabelValue;
  }


  public TestConformanceMetric currentScore(Double currentScore) {
    this.currentScore = currentScore;
    return this;
  }

  /**
   * Current test conformance score for the related Service
   * @return currentScore
   */
  @javax.annotation.Nonnull
  public Double getCurrentScore() {
    return currentScore;
  }

  public void setCurrentScore(Double currentScore) {
    this.currentScore = currentScore;
  }


  public TestConformanceMetric id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Unique identifier of coverage metric
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public TestConformanceMetric lastUpdateDay(String lastUpdateDay) {
    this.lastUpdateDay = lastUpdateDay;
    return this;
  }

  /**
   * The day of latest score update (in yyyyMMdd format)
   * @return lastUpdateDay
   */
  @javax.annotation.Nullable
  public String getLastUpdateDay() {
    return lastUpdateDay;
  }

  public void setLastUpdateDay(String lastUpdateDay) {
    this.lastUpdateDay = lastUpdateDay;
  }


  public TestConformanceMetric latestScores(Map<String, BigDecimal> latestScores) {
    this.latestScores = latestScores;
    return this;
  }

  public TestConformanceMetric putLatestScoresItem(String key, BigDecimal latestScoresItem) {
    if (this.latestScores == null) {
      this.latestScores = new HashMap<>();
    }
    this.latestScores.put(key, latestScoresItem);
    return this;
  }

  /**
   * History of latest scores (key is date with format yyyyMMdd, value is score as double)
   * @return latestScores
   */
  @javax.annotation.Nullable
  public Map<String, BigDecimal> getLatestScores() {
    return latestScores;
  }

  public void setLatestScores(Map<String, BigDecimal> latestScores) {
    this.latestScores = latestScores;
  }


  public TestConformanceMetric latestTrend(Trend latestTrend) {
    this.latestTrend = latestTrend;
    return this;
  }

  /**
   * Get latestTrend
   * @return latestTrend
   */
  @javax.annotation.Nullable
  public Trend getLatestTrend() {
    return latestTrend;
  }

  public void setLatestTrend(Trend latestTrend) {
    this.latestTrend = latestTrend;
  }


  public TestConformanceMetric maxPossibleScore(Double maxPossibleScore) {
    this.maxPossibleScore = maxPossibleScore;
    return this;
  }

  /**
   * Maximum conformance score that can be reached (depends on samples expresiveness)
   * @return maxPossibleScore
   */
  @javax.annotation.Nonnull
  public Double getMaxPossibleScore() {
    return maxPossibleScore;
  }

  public void setMaxPossibleScore(Double maxPossibleScore) {
    this.maxPossibleScore = maxPossibleScore;
  }


  public TestConformanceMetric serviceId(String serviceId) {
    this.serviceId = serviceId;
    return this;
  }

  /**
   * Unique identifier of the Service this metric is related to
   * @return serviceId
   */
  @javax.annotation.Nonnull
  public String getServiceId() {
    return serviceId;
  }

  public void setServiceId(String serviceId) {
    this.serviceId = serviceId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TestConformanceMetric testConformanceMetric = (TestConformanceMetric) o;
    return Objects.equals(this.aggregationLabelValue, testConformanceMetric.aggregationLabelValue) &&
        Objects.equals(this.currentScore, testConformanceMetric.currentScore) &&
        Objects.equals(this.id, testConformanceMetric.id) &&
        Objects.equals(this.lastUpdateDay, testConformanceMetric.lastUpdateDay) &&
        Objects.equals(this.latestScores, testConformanceMetric.latestScores) &&
        Objects.equals(this.latestTrend, testConformanceMetric.latestTrend) &&
        Objects.equals(this.maxPossibleScore, testConformanceMetric.maxPossibleScore) &&
        Objects.equals(this.serviceId, testConformanceMetric.serviceId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aggregationLabelValue, currentScore, id, lastUpdateDay, latestScores, latestTrend, maxPossibleScore, serviceId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TestConformanceMetric {\n");
    sb.append("    aggregationLabelValue: ").append(toIndentedString(aggregationLabelValue)).append("\n");
    sb.append("    currentScore: ").append(toIndentedString(currentScore)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastUpdateDay: ").append(toIndentedString(lastUpdateDay)).append("\n");
    sb.append("    latestScores: ").append(toIndentedString(latestScores)).append("\n");
    sb.append("    latestTrend: ").append(toIndentedString(latestTrend)).append("\n");
    sb.append("    maxPossibleScore: ").append(toIndentedString(maxPossibleScore)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
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
    openapiFields.add("aggregationLabelValue");
    openapiFields.add("currentScore");
    openapiFields.add("id");
    openapiFields.add("lastUpdateDay");
    openapiFields.add("latestScores");
    openapiFields.add("latestTrend");
    openapiFields.add("maxPossibleScore");
    openapiFields.add("serviceId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("currentScore");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("maxPossibleScore");
    openapiRequiredFields.add("serviceId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TestConformanceMetric
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TestConformanceMetric.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TestConformanceMetric is not found in the empty JSON string", TestConformanceMetric.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TestConformanceMetric.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TestConformanceMetric` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TestConformanceMetric.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("aggregationLabelValue") != null && !jsonObj.get("aggregationLabelValue").isJsonNull()) && !jsonObj.get("aggregationLabelValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `aggregationLabelValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("aggregationLabelValue").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("lastUpdateDay") != null && !jsonObj.get("lastUpdateDay").isJsonNull()) && !jsonObj.get("lastUpdateDay").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastUpdateDay` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastUpdateDay").toString()));
      }
      // validate the optional field `latestTrend`
      if (jsonObj.get("latestTrend") != null && !jsonObj.get("latestTrend").isJsonNull()) {
        Trend.validateJsonElement(jsonObj.get("latestTrend"));
      }
      if (!jsonObj.get("serviceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serviceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serviceId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TestConformanceMetric.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TestConformanceMetric' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TestConformanceMetric> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TestConformanceMetric.class));

       return (TypeAdapter<T>) new TypeAdapter<TestConformanceMetric>() {
           @Override
           public void write(JsonWriter out, TestConformanceMetric value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TestConformanceMetric read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TestConformanceMetric given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TestConformanceMetric
   * @throws IOException if the JSON string is invalid with respect to TestConformanceMetric
   */
  public static TestConformanceMetric fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TestConformanceMetric.class);
  }

  /**
   * Convert an instance of TestConformanceMetric to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

