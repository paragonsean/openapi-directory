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
import java.util.Arrays;
import org.openapitools.client.model.DescriptiveBoolean;
import org.openapitools.client.model.FormattedDateRange;

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
 * IRrspMaximizerStrategy
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IRrspMaximizerStrategy {
  public static final String SERIALIZED_NAME_APPLICABLE = "applicable";
  @SerializedName(SERIALIZED_NAME_APPLICABLE)
  private String applicable;

  public static final String SERIALIZED_NAME_APPLICABLE_RANGE = "applicableRange";
  @SerializedName(SERIALIZED_NAME_APPLICABLE_RANGE)
  private FormattedDateRange applicableRange;

  public static final String SERIALIZED_NAME_ASSET_NAME = "assetName";
  @SerializedName(SERIALIZED_NAME_ASSET_NAME)
  private String assetName;

  public static final String SERIALIZED_NAME_CONSTRAINED_BY_CASHFLOW = "constrainedByCashflow";
  @SerializedName(SERIALIZED_NAME_CONSTRAINED_BY_CASHFLOW)
  private DescriptiveBoolean constrainedByCashflow;

  public static final String SERIALIZED_NAME_MONTH = "month";
  @SerializedName(SERIALIZED_NAME_MONTH)
  private String month;

  public IRrspMaximizerStrategy() {
  }

  public IRrspMaximizerStrategy(
     String applicable, 
     String assetName, 
     String month
  ) {
    this();
    this.applicable = applicable;
    this.assetName = assetName;
    this.month = month;
  }

  /**
   * Get applicable
   * @return applicable
   */
  @javax.annotation.Nullable
  public String getApplicable() {
    return applicable;
  }



  public IRrspMaximizerStrategy applicableRange(FormattedDateRange applicableRange) {
    this.applicableRange = applicableRange;
    return this;
  }

  /**
   * Get applicableRange
   * @return applicableRange
   */
  @javax.annotation.Nullable
  public FormattedDateRange getApplicableRange() {
    return applicableRange;
  }

  public void setApplicableRange(FormattedDateRange applicableRange) {
    this.applicableRange = applicableRange;
  }


  /**
   * Get assetName
   * @return assetName
   */
  @javax.annotation.Nullable
  public String getAssetName() {
    return assetName;
  }



  public IRrspMaximizerStrategy constrainedByCashflow(DescriptiveBoolean constrainedByCashflow) {
    this.constrainedByCashflow = constrainedByCashflow;
    return this;
  }

  /**
   * Get constrainedByCashflow
   * @return constrainedByCashflow
   */
  @javax.annotation.Nullable
  public DescriptiveBoolean getConstrainedByCashflow() {
    return constrainedByCashflow;
  }

  public void setConstrainedByCashflow(DescriptiveBoolean constrainedByCashflow) {
    this.constrainedByCashflow = constrainedByCashflow;
  }


  /**
   * Get month
   * @return month
   */
  @javax.annotation.Nullable
  public String getMonth() {
    return month;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IRrspMaximizerStrategy irrspMaximizerStrategy = (IRrspMaximizerStrategy) o;
    return Objects.equals(this.applicable, irrspMaximizerStrategy.applicable) &&
        Objects.equals(this.applicableRange, irrspMaximizerStrategy.applicableRange) &&
        Objects.equals(this.assetName, irrspMaximizerStrategy.assetName) &&
        Objects.equals(this.constrainedByCashflow, irrspMaximizerStrategy.constrainedByCashflow) &&
        Objects.equals(this.month, irrspMaximizerStrategy.month);
  }

  @Override
  public int hashCode() {
    return Objects.hash(applicable, applicableRange, assetName, constrainedByCashflow, month);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IRrspMaximizerStrategy {\n");
    sb.append("    applicable: ").append(toIndentedString(applicable)).append("\n");
    sb.append("    applicableRange: ").append(toIndentedString(applicableRange)).append("\n");
    sb.append("    assetName: ").append(toIndentedString(assetName)).append("\n");
    sb.append("    constrainedByCashflow: ").append(toIndentedString(constrainedByCashflow)).append("\n");
    sb.append("    month: ").append(toIndentedString(month)).append("\n");
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
    openapiFields.add("applicable");
    openapiFields.add("applicableRange");
    openapiFields.add("assetName");
    openapiFields.add("constrainedByCashflow");
    openapiFields.add("month");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IRrspMaximizerStrategy
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IRrspMaximizerStrategy.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IRrspMaximizerStrategy is not found in the empty JSON string", IRrspMaximizerStrategy.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IRrspMaximizerStrategy.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IRrspMaximizerStrategy` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("applicable") != null && !jsonObj.get("applicable").isJsonNull()) && !jsonObj.get("applicable").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `applicable` to be a primitive type in the JSON string but got `%s`", jsonObj.get("applicable").toString()));
      }
      // validate the optional field `applicableRange`
      if (jsonObj.get("applicableRange") != null && !jsonObj.get("applicableRange").isJsonNull()) {
        FormattedDateRange.validateJsonElement(jsonObj.get("applicableRange"));
      }
      if ((jsonObj.get("assetName") != null && !jsonObj.get("assetName").isJsonNull()) && !jsonObj.get("assetName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetName").toString()));
      }
      // validate the optional field `constrainedByCashflow`
      if (jsonObj.get("constrainedByCashflow") != null && !jsonObj.get("constrainedByCashflow").isJsonNull()) {
        DescriptiveBoolean.validateJsonElement(jsonObj.get("constrainedByCashflow"));
      }
      if ((jsonObj.get("month") != null && !jsonObj.get("month").isJsonNull()) && !jsonObj.get("month").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `month` to be a primitive type in the JSON string but got `%s`", jsonObj.get("month").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IRrspMaximizerStrategy.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IRrspMaximizerStrategy' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IRrspMaximizerStrategy> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IRrspMaximizerStrategy.class));

       return (TypeAdapter<T>) new TypeAdapter<IRrspMaximizerStrategy>() {
           @Override
           public void write(JsonWriter out, IRrspMaximizerStrategy value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IRrspMaximizerStrategy read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IRrspMaximizerStrategy given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IRrspMaximizerStrategy
   * @throws IOException if the JSON string is invalid with respect to IRrspMaximizerStrategy
   */
  public static IRrspMaximizerStrategy fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IRrspMaximizerStrategy.class);
  }

  /**
   * Convert an instance of IRrspMaximizerStrategy to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

