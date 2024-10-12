/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
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
import org.openapitools.client.model.TagPerformance;
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
 * Represents the detailed performance data for a trained iteration.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:14.859299-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IterationPerformance {
  public static final String SERIALIZED_NAME_AVERAGE_PRECISION = "averagePrecision";
  @SerializedName(SERIALIZED_NAME_AVERAGE_PRECISION)
  private Float averagePrecision;

  public static final String SERIALIZED_NAME_PER_TAG_PERFORMANCE = "perTagPerformance";
  @SerializedName(SERIALIZED_NAME_PER_TAG_PERFORMANCE)
  private List<TagPerformance> perTagPerformance = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRECISION = "precision";
  @SerializedName(SERIALIZED_NAME_PRECISION)
  private Float precision;

  public static final String SERIALIZED_NAME_PRECISION_STD_DEVIATION = "precisionStdDeviation";
  @SerializedName(SERIALIZED_NAME_PRECISION_STD_DEVIATION)
  private Float precisionStdDeviation;

  public static final String SERIALIZED_NAME_RECALL = "recall";
  @SerializedName(SERIALIZED_NAME_RECALL)
  private Float recall;

  public static final String SERIALIZED_NAME_RECALL_STD_DEVIATION = "recallStdDeviation";
  @SerializedName(SERIALIZED_NAME_RECALL_STD_DEVIATION)
  private Float recallStdDeviation;

  public IterationPerformance() {
  }

  public IterationPerformance(
     Float averagePrecision, 
     List<TagPerformance> perTagPerformance, 
     Float precision, 
     Float precisionStdDeviation, 
     Float recall, 
     Float recallStdDeviation
  ) {
    this();
    this.averagePrecision = averagePrecision;
    this.perTagPerformance = perTagPerformance;
    this.precision = precision;
    this.precisionStdDeviation = precisionStdDeviation;
    this.recall = recall;
    this.recallStdDeviation = recallStdDeviation;
  }

  /**
   * Gets the average precision when applicable.
   * @return averagePrecision
   */
  @javax.annotation.Nullable
  public Float getAveragePrecision() {
    return averagePrecision;
  }



  /**
   * Gets the per-tag performance details for this iteration.
   * @return perTagPerformance
   */
  @javax.annotation.Nullable
  public List<TagPerformance> getPerTagPerformance() {
    return perTagPerformance;
  }



  /**
   * Gets the precision.
   * @return precision
   */
  @javax.annotation.Nullable
  public Float getPrecision() {
    return precision;
  }



  /**
   * Gets the standard deviation for the precision.
   * @return precisionStdDeviation
   */
  @javax.annotation.Nullable
  public Float getPrecisionStdDeviation() {
    return precisionStdDeviation;
  }



  /**
   * Gets the recall.
   * @return recall
   */
  @javax.annotation.Nullable
  public Float getRecall() {
    return recall;
  }



  /**
   * Gets the standard deviation for the recall.
   * @return recallStdDeviation
   */
  @javax.annotation.Nullable
  public Float getRecallStdDeviation() {
    return recallStdDeviation;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IterationPerformance iterationPerformance = (IterationPerformance) o;
    return Objects.equals(this.averagePrecision, iterationPerformance.averagePrecision) &&
        Objects.equals(this.perTagPerformance, iterationPerformance.perTagPerformance) &&
        Objects.equals(this.precision, iterationPerformance.precision) &&
        Objects.equals(this.precisionStdDeviation, iterationPerformance.precisionStdDeviation) &&
        Objects.equals(this.recall, iterationPerformance.recall) &&
        Objects.equals(this.recallStdDeviation, iterationPerformance.recallStdDeviation);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(averagePrecision, perTagPerformance, precision, precisionStdDeviation, recall, recallStdDeviation);
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
    sb.append("class IterationPerformance {\n");
    sb.append("    averagePrecision: ").append(toIndentedString(averagePrecision)).append("\n");
    sb.append("    perTagPerformance: ").append(toIndentedString(perTagPerformance)).append("\n");
    sb.append("    precision: ").append(toIndentedString(precision)).append("\n");
    sb.append("    precisionStdDeviation: ").append(toIndentedString(precisionStdDeviation)).append("\n");
    sb.append("    recall: ").append(toIndentedString(recall)).append("\n");
    sb.append("    recallStdDeviation: ").append(toIndentedString(recallStdDeviation)).append("\n");
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
    openapiFields.add("averagePrecision");
    openapiFields.add("perTagPerformance");
    openapiFields.add("precision");
    openapiFields.add("precisionStdDeviation");
    openapiFields.add("recall");
    openapiFields.add("recallStdDeviation");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IterationPerformance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IterationPerformance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IterationPerformance is not found in the empty JSON string", IterationPerformance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IterationPerformance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IterationPerformance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("perTagPerformance") != null && !jsonObj.get("perTagPerformance").isJsonNull()) {
        JsonArray jsonArrayperTagPerformance = jsonObj.getAsJsonArray("perTagPerformance");
        if (jsonArrayperTagPerformance != null) {
          // ensure the json data is an array
          if (!jsonObj.get("perTagPerformance").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `perTagPerformance` to be an array in the JSON string but got `%s`", jsonObj.get("perTagPerformance").toString()));
          }

          // validate the optional field `perTagPerformance` (array)
          for (int i = 0; i < jsonArrayperTagPerformance.size(); i++) {
            TagPerformance.validateJsonElement(jsonArrayperTagPerformance.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IterationPerformance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IterationPerformance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IterationPerformance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IterationPerformance.class));

       return (TypeAdapter<T>) new TypeAdapter<IterationPerformance>() {
           @Override
           public void write(JsonWriter out, IterationPerformance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IterationPerformance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IterationPerformance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IterationPerformance
   * @throws IOException if the JSON string is invalid with respect to IterationPerformance
   */
  public static IterationPerformance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IterationPerformance.class);
  }

  /**
   * Convert an instance of IterationPerformance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

