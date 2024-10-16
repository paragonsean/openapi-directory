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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.AdvicentDomainLogicGoalWhatIfEducationGoalAdjustments;
import org.openapitools.client.model.AdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections;

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
 * AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel {
  public static final String SERIALIZED_NAME_ADJUSTED_VALUES = "adjustedValues";
  @SerializedName(SERIALIZED_NAME_ADJUSTED_VALUES)
  private AdvicentDomainLogicGoalWhatIfEducationGoalAdjustments adjustedValues;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_GOAL_ID = "goalId";
  @SerializedName(SERIALIZED_NAME_GOAL_ID)
  private Integer goalId;

  public static final String SERIALIZED_NAME_PROJECTED_RESULTS = "projectedResults";
  @SerializedName(SERIALIZED_NAME_PROJECTED_RESULTS)
  private AdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections projectedResults;

  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel() {
  }

  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel adjustedValues(AdvicentDomainLogicGoalWhatIfEducationGoalAdjustments adjustedValues) {
    this.adjustedValues = adjustedValues;
    return this;
  }

  /**
   * Get adjustedValues
   * @return adjustedValues
   */
  @javax.annotation.Nullable
  public AdvicentDomainLogicGoalWhatIfEducationGoalAdjustments getAdjustedValues() {
    return adjustedValues;
  }

  public void setAdjustedValues(AdvicentDomainLogicGoalWhatIfEducationGoalAdjustments adjustedValues) {
    this.adjustedValues = adjustedValues;
  }


  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel created(OffsetDateTime created) {
    this.created = created;
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }

  public void setCreated(OffsetDateTime created) {
    this.created = created;
  }


  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel goalId(Integer goalId) {
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


  public AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel projectedResults(AdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections projectedResults) {
    this.projectedResults = projectedResults;
    return this;
  }

  /**
   * Get projectedResults
   * @return projectedResults
   */
  @javax.annotation.Nullable
  public AdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections getProjectedResults() {
    return projectedResults;
  }

  public void setProjectedResults(AdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections projectedResults) {
    this.projectedResults = projectedResults;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel advicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel = (AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel) o;
    return Objects.equals(this.adjustedValues, advicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.adjustedValues) &&
        Objects.equals(this.created, advicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.created) &&
        Objects.equals(this.goalId, advicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.goalId) &&
        Objects.equals(this.projectedResults, advicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.projectedResults);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adjustedValues, created, goalId, projectedResults);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel {\n");
    sb.append("    adjustedValues: ").append(toIndentedString(adjustedValues)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    goalId: ").append(toIndentedString(goalId)).append("\n");
    sb.append("    projectedResults: ").append(toIndentedString(projectedResults)).append("\n");
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
    openapiFields.add("adjustedValues");
    openapiFields.add("created");
    openapiFields.add("goalId");
    openapiFields.add("projectedResults");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel is not found in the empty JSON string", AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `adjustedValues`
      if (jsonObj.get("adjustedValues") != null && !jsonObj.get("adjustedValues").isJsonNull()) {
        AdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.validateJsonElement(jsonObj.get("adjustedValues"));
      }
      // validate the optional field `projectedResults`
      if (jsonObj.get("projectedResults") != null && !jsonObj.get("projectedResults").isJsonNull()) {
        AdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections.validateJsonElement(jsonObj.get("projectedResults"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.class));

       return (TypeAdapter<T>) new TypeAdapter<AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel>() {
           @Override
           public void write(JsonWriter out, AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel
   * @throws IOException if the JSON string is invalid with respect to AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel
   */
  public static AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel.class);
  }

  /**
   * Convert an instance of AdvicentNaviPlanRestApiGoalAdjustmentsModelsEducationGoalAdjustmentsModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

