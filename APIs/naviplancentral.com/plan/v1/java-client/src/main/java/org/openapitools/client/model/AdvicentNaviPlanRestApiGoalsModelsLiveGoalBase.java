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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AdvicentNaviPlanRestApiModelsOwnerModel;

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
 * AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_COVERAGE_PERCENTAGE = "coveragePercentage";
  @SerializedName(SERIALIZED_NAME_COVERAGE_PERCENTAGE)
  private Double coveragePercentage;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private OffsetDateTime endDate;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INFLATION_RATE = "inflationRate";
  @SerializedName(SERIALIZED_NAME_INFLATION_RATE)
  private Double inflationRate;

  public static final String SERIALIZED_NAME_OWNERS = "owners";
  @SerializedName(SERIALIZED_NAME_OWNERS)
  private List<AdvicentNaviPlanRestApiModelsOwnerModel> owners = new ArrayList<>();

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase() {
  }

  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase coveragePercentage(Double coveragePercentage) {
    this.coveragePercentage = coveragePercentage;
    return this;
  }

  /**
   * Get coveragePercentage
   * @return coveragePercentage
   */
  @javax.annotation.Nullable
  public Double getCoveragePercentage() {
    return coveragePercentage;
  }

  public void setCoveragePercentage(Double coveragePercentage) {
    this.coveragePercentage = coveragePercentage;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase description(String description) {
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


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase endDate(OffsetDateTime endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEndDate() {
    return endDate;
  }

  public void setEndDate(OffsetDateTime endDate) {
    this.endDate = endDate;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase inflationRate(Double inflationRate) {
    this.inflationRate = inflationRate;
    return this;
  }

  /**
   * Get inflationRate
   * @return inflationRate
   */
  @javax.annotation.Nullable
  public Double getInflationRate() {
    return inflationRate;
  }

  public void setInflationRate(Double inflationRate) {
    this.inflationRate = inflationRate;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase owners(List<AdvicentNaviPlanRestApiModelsOwnerModel> owners) {
    this.owners = owners;
    return this;
  }

  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase addOwnersItem(AdvicentNaviPlanRestApiModelsOwnerModel ownersItem) {
    if (this.owners == null) {
      this.owners = new ArrayList<>();
    }
    this.owners.add(ownersItem);
    return this;
  }

  /**
   * Get owners
   * @return owners
   */
  @javax.annotation.Nullable
  public List<AdvicentNaviPlanRestApiModelsOwnerModel> getOwners() {
    return owners;
  }

  public void setOwners(List<AdvicentNaviPlanRestApiModelsOwnerModel> owners) {
    this.owners = owners;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase startDate(OffsetDateTime startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartDate() {
    return startDate;
  }

  public void setStartDate(OffsetDateTime startDate) {
    this.startDate = startDate;
  }


  public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase advicentNaviPlanRestApiGoalsModelsLiveGoalBase = (AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase) o;
    return Objects.equals(this.amount, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.amount) &&
        Objects.equals(this.coveragePercentage, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.coveragePercentage) &&
        Objects.equals(this.description, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.description) &&
        Objects.equals(this.endDate, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.endDate) &&
        Objects.equals(this.id, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.id) &&
        Objects.equals(this.inflationRate, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.inflationRate) &&
        Objects.equals(this.owners, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.owners) &&
        Objects.equals(this.startDate, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.startDate) &&
        Objects.equals(this.type, advicentNaviPlanRestApiGoalsModelsLiveGoalBase.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, coveragePercentage, description, endDate, id, inflationRate, owners, startDate, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    coveragePercentage: ").append(toIndentedString(coveragePercentage)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    inflationRate: ").append(toIndentedString(inflationRate)).append("\n");
    sb.append("    owners: ").append(toIndentedString(owners)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("coveragePercentage");
    openapiFields.add("description");
    openapiFields.add("endDate");
    openapiFields.add("id");
    openapiFields.add("inflationRate");
    openapiFields.add("owners");
    openapiFields.add("startDate");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase is not found in the empty JSON string", AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("owners") != null && !jsonObj.get("owners").isJsonNull()) {
        JsonArray jsonArrayowners = jsonObj.getAsJsonArray("owners");
        if (jsonArrayowners != null) {
          // ensure the json data is an array
          if (!jsonObj.get("owners").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `owners` to be an array in the JSON string but got `%s`", jsonObj.get("owners").toString()));
          }

          // validate the optional field `owners` (array)
          for (int i = 0; i < jsonArrayowners.size(); i++) {
            AdvicentNaviPlanRestApiModelsOwnerModel.validateJsonElement(jsonArrayowners.get(i));
          };
        }
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.class));

       return (TypeAdapter<T>) new TypeAdapter<AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase>() {
           @Override
           public void write(JsonWriter out, AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase
   * @throws IOException if the JSON string is invalid with respect to AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase
   */
  public static AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.class);
  }

  /**
   * Convert an instance of AdvicentNaviPlanRestApiGoalsModelsLiveGoalBase to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

