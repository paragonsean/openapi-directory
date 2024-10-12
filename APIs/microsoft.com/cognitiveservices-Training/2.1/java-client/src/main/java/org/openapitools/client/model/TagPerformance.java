/*
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
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
import java.util.UUID;
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
 * Represents performance data for a particular tag in a trained iteration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:10.847797-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TagPerformance {
  public static final String SERIALIZED_NAME_AVERAGE_PRECISION = "averagePrecision";
  @SerializedName(SERIALIZED_NAME_AVERAGE_PRECISION)
  private Float averagePrecision;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

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

  public TagPerformance() {
  }

  public TagPerformance(
     Float averagePrecision, 
     UUID id, 
     String name, 
     Float precision, 
     Float precisionStdDeviation, 
     Float recall, 
     Float recallStdDeviation
  ) {
    this();
    this.averagePrecision = averagePrecision;
    this.id = id;
    this.name = name;
    this.precision = precision;
    this.precisionStdDeviation = precisionStdDeviation;
    this.recall = recall;
    this.recallStdDeviation = recallStdDeviation;
  }

  /**
   * Gets the average precision when applicable
   * @return averagePrecision
   */
  @javax.annotation.Nullable
  public Float getAveragePrecision() {
    return averagePrecision;
  }



  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }



  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }



  /**
   * Gets the precision
   * @return precision
   */
  @javax.annotation.Nullable
  public Float getPrecision() {
    return precision;
  }



  /**
   * Gets the standard deviation for the precision
   * @return precisionStdDeviation
   */
  @javax.annotation.Nullable
  public Float getPrecisionStdDeviation() {
    return precisionStdDeviation;
  }



  /**
   * Gets the recall
   * @return recall
   */
  @javax.annotation.Nullable
  public Float getRecall() {
    return recall;
  }



  /**
   * Gets the standard deviation for the recall
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
    TagPerformance tagPerformance = (TagPerformance) o;
    return Objects.equals(this.averagePrecision, tagPerformance.averagePrecision) &&
        Objects.equals(this.id, tagPerformance.id) &&
        Objects.equals(this.name, tagPerformance.name) &&
        Objects.equals(this.precision, tagPerformance.precision) &&
        Objects.equals(this.precisionStdDeviation, tagPerformance.precisionStdDeviation) &&
        Objects.equals(this.recall, tagPerformance.recall) &&
        Objects.equals(this.recallStdDeviation, tagPerformance.recallStdDeviation);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(averagePrecision, id, name, precision, precisionStdDeviation, recall, recallStdDeviation);
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
    sb.append("class TagPerformance {\n");
    sb.append("    averagePrecision: ").append(toIndentedString(averagePrecision)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("name");
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
   * @throws IOException if the JSON Element is invalid with respect to TagPerformance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TagPerformance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TagPerformance is not found in the empty JSON string", TagPerformance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TagPerformance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TagPerformance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TagPerformance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TagPerformance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TagPerformance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TagPerformance.class));

       return (TypeAdapter<T>) new TypeAdapter<TagPerformance>() {
           @Override
           public void write(JsonWriter out, TagPerformance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TagPerformance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TagPerformance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TagPerformance
   * @throws IOException if the JSON string is invalid with respect to TagPerformance
   */
  public static TagPerformance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TagPerformance.class);
  }

  /**
   * Convert an instance of TagPerformance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

