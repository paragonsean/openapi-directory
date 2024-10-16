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
import java.util.Date;
import org.openapitools.client.model.GoalId;
import org.openapitools.client.model.IOptionalFieldCurrency;
import org.openapitools.client.model.IOptionalFieldGoalCoveragePercent;
import org.openapitools.client.model.IOptionalFieldYear;

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
 * IGoal
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IGoal {
  public static final String SERIALIZED_NAME_ASSETS_REMAINING_AFTER_FUNDING_GOAL = "assetsRemainingAfterFundingGoal";
  @SerializedName(SERIALIZED_NAME_ASSETS_REMAINING_AFTER_FUNDING_GOAL)
  private IOptionalFieldCurrency assetsRemainingAfterFundingGoal;

  public static final String SERIALIZED_NAME_COVERAGE = "coverage";
  @SerializedName(SERIALIZED_NAME_COVERAGE)
  private IOptionalFieldGoalCoveragePercent coverage;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private Date endDate;

  public static final String SERIALIZED_NAME_IDENTIFIER = "identifier";
  @SerializedName(SERIALIZED_NAME_IDENTIFIER)
  private GoalId identifier;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private Date startDate;

  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    RETIREMENT("Retirement"),
    
    SURVIVOR_INCOME("SurvivorIncome"),
    
    CRITICAL_ILLNESS("CriticalIllness"),
    
    LONG_TERM_CARE_INSURANCE("LongTermCareInsurance"),
    
    CASHFLOW("Cashflow"),
    
    DISABILITY_INCOME("DisabilityIncome"),
    
    EDUCATION("Education"),
    
    MAJOR_PURCHASE("MajorPurchase"),
    
    EMERGENCY_FUND("EmergencyFund"),
    
    UNDEFINED("Undefined"),
    
    NOT_SUPPORTED("NotSupported");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_YEAR_ASSETS_DEPLETED = "yearAssetsDepleted";
  @SerializedName(SERIALIZED_NAME_YEAR_ASSETS_DEPLETED)
  private IOptionalFieldYear yearAssetsDepleted;

  public IGoal() {
  }

  public IGoal(
     String description, 
     TypeEnum type
  ) {
    this();
    this.description = description;
    this.type = type;
  }

  public IGoal assetsRemainingAfterFundingGoal(IOptionalFieldCurrency assetsRemainingAfterFundingGoal) {
    this.assetsRemainingAfterFundingGoal = assetsRemainingAfterFundingGoal;
    return this;
  }

  /**
   * Get assetsRemainingAfterFundingGoal
   * @return assetsRemainingAfterFundingGoal
   */
  @javax.annotation.Nullable
  public IOptionalFieldCurrency getAssetsRemainingAfterFundingGoal() {
    return assetsRemainingAfterFundingGoal;
  }

  public void setAssetsRemainingAfterFundingGoal(IOptionalFieldCurrency assetsRemainingAfterFundingGoal) {
    this.assetsRemainingAfterFundingGoal = assetsRemainingAfterFundingGoal;
  }


  public IGoal coverage(IOptionalFieldGoalCoveragePercent coverage) {
    this.coverage = coverage;
    return this;
  }

  /**
   * Get coverage
   * @return coverage
   */
  @javax.annotation.Nullable
  public IOptionalFieldGoalCoveragePercent getCoverage() {
    return coverage;
  }

  public void setCoverage(IOptionalFieldGoalCoveragePercent coverage) {
    this.coverage = coverage;
  }


  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }



  public IGoal endDate(Date endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public Date getEndDate() {
    return endDate;
  }

  public void setEndDate(Date endDate) {
    this.endDate = endDate;
  }


  public IGoal identifier(GoalId identifier) {
    this.identifier = identifier;
    return this;
  }

  /**
   * Get identifier
   * @return identifier
   */
  @javax.annotation.Nullable
  public GoalId getIdentifier() {
    return identifier;
  }

  public void setIdentifier(GoalId identifier) {
    this.identifier = identifier;
  }


  public IGoal startDate(Date startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public Date getStartDate() {
    return startDate;
  }

  public void setStartDate(Date startDate) {
    this.startDate = startDate;
  }


  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }



  public IGoal yearAssetsDepleted(IOptionalFieldYear yearAssetsDepleted) {
    this.yearAssetsDepleted = yearAssetsDepleted;
    return this;
  }

  /**
   * Get yearAssetsDepleted
   * @return yearAssetsDepleted
   */
  @javax.annotation.Nullable
  public IOptionalFieldYear getYearAssetsDepleted() {
    return yearAssetsDepleted;
  }

  public void setYearAssetsDepleted(IOptionalFieldYear yearAssetsDepleted) {
    this.yearAssetsDepleted = yearAssetsDepleted;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IGoal igoal = (IGoal) o;
    return Objects.equals(this.assetsRemainingAfterFundingGoal, igoal.assetsRemainingAfterFundingGoal) &&
        Objects.equals(this.coverage, igoal.coverage) &&
        Objects.equals(this.description, igoal.description) &&
        Objects.equals(this.endDate, igoal.endDate) &&
        Objects.equals(this.identifier, igoal.identifier) &&
        Objects.equals(this.startDate, igoal.startDate) &&
        Objects.equals(this.type, igoal.type) &&
        Objects.equals(this.yearAssetsDepleted, igoal.yearAssetsDepleted);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetsRemainingAfterFundingGoal, coverage, description, endDate, identifier, startDate, type, yearAssetsDepleted);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IGoal {\n");
    sb.append("    assetsRemainingAfterFundingGoal: ").append(toIndentedString(assetsRemainingAfterFundingGoal)).append("\n");
    sb.append("    coverage: ").append(toIndentedString(coverage)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    identifier: ").append(toIndentedString(identifier)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    yearAssetsDepleted: ").append(toIndentedString(yearAssetsDepleted)).append("\n");
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
    openapiFields.add("assetsRemainingAfterFundingGoal");
    openapiFields.add("coverage");
    openapiFields.add("description");
    openapiFields.add("endDate");
    openapiFields.add("identifier");
    openapiFields.add("startDate");
    openapiFields.add("type");
    openapiFields.add("yearAssetsDepleted");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IGoal
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IGoal.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IGoal is not found in the empty JSON string", IGoal.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IGoal.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IGoal` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `assetsRemainingAfterFundingGoal`
      if (jsonObj.get("assetsRemainingAfterFundingGoal") != null && !jsonObj.get("assetsRemainingAfterFundingGoal").isJsonNull()) {
        IOptionalFieldCurrency.validateJsonElement(jsonObj.get("assetsRemainingAfterFundingGoal"));
      }
      // validate the optional field `coverage`
      if (jsonObj.get("coverage") != null && !jsonObj.get("coverage").isJsonNull()) {
        IOptionalFieldGoalCoveragePercent.validateJsonElement(jsonObj.get("coverage"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `endDate`
      if (jsonObj.get("endDate") != null && !jsonObj.get("endDate").isJsonNull()) {
        Date.validateJsonElement(jsonObj.get("endDate"));
      }
      // validate the optional field `identifier`
      if (jsonObj.get("identifier") != null && !jsonObj.get("identifier").isJsonNull()) {
        GoalId.validateJsonElement(jsonObj.get("identifier"));
      }
      // validate the optional field `startDate`
      if (jsonObj.get("startDate") != null && !jsonObj.get("startDate").isJsonNull()) {
        Date.validateJsonElement(jsonObj.get("startDate"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      // validate the optional field `yearAssetsDepleted`
      if (jsonObj.get("yearAssetsDepleted") != null && !jsonObj.get("yearAssetsDepleted").isJsonNull()) {
        IOptionalFieldYear.validateJsonElement(jsonObj.get("yearAssetsDepleted"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IGoal.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IGoal' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IGoal> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IGoal.class));

       return (TypeAdapter<T>) new TypeAdapter<IGoal>() {
           @Override
           public void write(JsonWriter out, IGoal value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IGoal read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IGoal given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IGoal
   * @throws IOException if the JSON string is invalid with respect to IGoal
   */
  public static IGoal fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IGoal.class);
  }

  /**
   * Convert an instance of IGoal to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

