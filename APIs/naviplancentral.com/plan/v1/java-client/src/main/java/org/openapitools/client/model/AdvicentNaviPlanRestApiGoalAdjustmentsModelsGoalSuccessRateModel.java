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
 * AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_GOAL_ID = "goalId";
  @SerializedName(SERIALIZED_NAME_GOAL_ID)
  private Integer goalId;

  public static final String SERIALIZED_NAME_SUCCESS_RATE = "successRate";
  @SerializedName(SERIALIZED_NAME_SUCCESS_RATE)
  private Double successRate;

  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel() {
  }

  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel goalId(Integer goalId) {
    this.goalId = goalId;
    return this;
  }

  /**
   * Get goalId
   * @return goalId
   */
  @javax.annotation.Nullable
  public Integer getGoalId() {
    return goalId;
  }

  public void setGoalId(Integer goalId) {
    this.goalId = goalId;
  }


  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel successRate(Double successRate) {
    this.successRate = successRate;
    return this;
  }

  /**
   * Get successRate
   * @return successRate
   */
  @javax.annotation.Nullable
  public Double getSuccessRate() {
    return successRate;
  }

  public void setSuccessRate(Double successRate) {
    this.successRate = successRate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel advicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel = (AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel) o;
    return Objects.equals(this.description, advicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.description) &&
        Objects.equals(this.goalId, advicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.goalId) &&
        Objects.equals(this.successRate, advicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.successRate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, goalId, successRate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    goalId: ").append(toIndentedString(goalId)).append("\n");
    sb.append("    successRate: ").append(toIndentedString(successRate)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("goalId");
    openapiFields.add("successRate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel is not found in the empty JSON string", AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.class));

       return (TypeAdapter<T>) new TypeAdapter<AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel>() {
           @Override
           public void write(JsonWriter out, AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel
   * @throws IOException if the JSON string is invalid with respect to AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel
   */
  public static AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel.class);
  }

  /**
   * Convert an instance of AdvicentNaviPlanRestApiGoalAdjustmentsModelsGoalSuccessRateModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

