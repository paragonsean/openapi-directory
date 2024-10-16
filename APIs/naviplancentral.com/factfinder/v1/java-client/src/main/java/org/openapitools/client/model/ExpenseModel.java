/*
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
 * ExpenseModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExpenseModel {
  public static final String SERIALIZED_NAME_ANNUAL_PERIOD = "annualPeriod";
  @SerializedName(SERIALIZED_NAME_ANNUAL_PERIOD)
  private Integer annualPeriod;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private OffsetDateTime endDate;

  public static final String SERIALIZED_NAME_EXPENSE_AMOUNT = "expenseAmount";
  @SerializedName(SERIALIZED_NAME_EXPENSE_AMOUNT)
  private Double expenseAmount;

  public static final String SERIALIZED_NAME_EXPENSE_TYPE_ID = "expenseTypeId";
  @SerializedName(SERIALIZED_NAME_EXPENSE_TYPE_ID)
  private Integer expenseTypeId;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private Integer frequency;

  /**
   * Gets or Sets member
   */
  @JsonAdapter(MemberEnum.Adapter.class)
  public enum MemberEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient"),
    
    JOINT("Joint");

    private String value;

    MemberEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MemberEnum fromValue(String value) {
      for (MemberEnum b : MemberEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MemberEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MemberEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MemberEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MemberEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MemberEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MEMBER = "member";
  @SerializedName(SERIALIZED_NAME_MEMBER)
  private MemberEnum member;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private OffsetDateTime startDate;

  public ExpenseModel() {
  }

  public ExpenseModel annualPeriod(Integer annualPeriod) {
    this.annualPeriod = annualPeriod;
    return this;
  }

  /**
   * Get annualPeriod
   * minimum: 1
   * maximum: 99
   * @return annualPeriod
   */
  @javax.annotation.Nullable
  public Integer getAnnualPeriod() {
    return annualPeriod;
  }

  public void setAnnualPeriod(Integer annualPeriod) {
    this.annualPeriod = annualPeriod;
  }


  public ExpenseModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ExpenseModel endDate(OffsetDateTime endDate) {
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


  public ExpenseModel expenseAmount(Double expenseAmount) {
    this.expenseAmount = expenseAmount;
    return this;
  }

  /**
   * Get expenseAmount
   * @return expenseAmount
   */
  @javax.annotation.Nullable
  public Double getExpenseAmount() {
    return expenseAmount;
  }

  public void setExpenseAmount(Double expenseAmount) {
    this.expenseAmount = expenseAmount;
  }


  public ExpenseModel expenseTypeId(Integer expenseTypeId) {
    this.expenseTypeId = expenseTypeId;
    return this;
  }

  /**
   * Get expenseTypeId
   * @return expenseTypeId
   */
  @javax.annotation.Nullable
  public Integer getExpenseTypeId() {
    return expenseTypeId;
  }

  public void setExpenseTypeId(Integer expenseTypeId) {
    this.expenseTypeId = expenseTypeId;
  }


  public ExpenseModel externalDestinationId(String externalDestinationId) {
    this.externalDestinationId = externalDestinationId;
    return this;
  }

  /**
   * Get externalDestinationId
   * @return externalDestinationId
   */
  @javax.annotation.Nullable
  public String getExternalDestinationId() {
    return externalDestinationId;
  }

  public void setExternalDestinationId(String externalDestinationId) {
    this.externalDestinationId = externalDestinationId;
  }


  public ExpenseModel factFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
    return this;
  }

  /**
   * Get factFinderId
   * @return factFinderId
   */
  @javax.annotation.Nonnull
  public Integer getFactFinderId() {
    return factFinderId;
  }

  public void setFactFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
  }


  public ExpenseModel frequency(Integer frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Get frequency
   * @return frequency
   */
  @javax.annotation.Nullable
  public Integer getFrequency() {
    return frequency;
  }

  public void setFrequency(Integer frequency) {
    this.frequency = frequency;
  }


  public ExpenseModel member(MemberEnum member) {
    this.member = member;
    return this;
  }

  /**
   * Get member
   * @return member
   */
  @javax.annotation.Nullable
  public MemberEnum getMember() {
    return member;
  }

  public void setMember(MemberEnum member) {
    this.member = member;
  }


  public ExpenseModel startDate(OffsetDateTime startDate) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExpenseModel expenseModel = (ExpenseModel) o;
    return Objects.equals(this.annualPeriod, expenseModel.annualPeriod) &&
        Objects.equals(this.description, expenseModel.description) &&
        Objects.equals(this.endDate, expenseModel.endDate) &&
        Objects.equals(this.expenseAmount, expenseModel.expenseAmount) &&
        Objects.equals(this.expenseTypeId, expenseModel.expenseTypeId) &&
        Objects.equals(this.externalDestinationId, expenseModel.externalDestinationId) &&
        Objects.equals(this.factFinderId, expenseModel.factFinderId) &&
        Objects.equals(this.frequency, expenseModel.frequency) &&
        Objects.equals(this.member, expenseModel.member) &&
        Objects.equals(this.startDate, expenseModel.startDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(annualPeriod, description, endDate, expenseAmount, expenseTypeId, externalDestinationId, factFinderId, frequency, member, startDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExpenseModel {\n");
    sb.append("    annualPeriod: ").append(toIndentedString(annualPeriod)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    expenseAmount: ").append(toIndentedString(expenseAmount)).append("\n");
    sb.append("    expenseTypeId: ").append(toIndentedString(expenseTypeId)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    member: ").append(toIndentedString(member)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
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
    openapiFields.add("annualPeriod");
    openapiFields.add("description");
    openapiFields.add("endDate");
    openapiFields.add("expenseAmount");
    openapiFields.add("expenseTypeId");
    openapiFields.add("externalDestinationId");
    openapiFields.add("factFinderId");
    openapiFields.add("frequency");
    openapiFields.add("member");
    openapiFields.add("startDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("factFinderId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExpenseModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExpenseModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExpenseModel is not found in the empty JSON string", ExpenseModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExpenseModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExpenseModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ExpenseModel.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("externalDestinationId") != null && !jsonObj.get("externalDestinationId").isJsonNull()) && !jsonObj.get("externalDestinationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalDestinationId").toString()));
      }
      if ((jsonObj.get("member") != null && !jsonObj.get("member").isJsonNull()) && !jsonObj.get("member").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `member` to be a primitive type in the JSON string but got `%s`", jsonObj.get("member").toString()));
      }
      // validate the optional field `member`
      if (jsonObj.get("member") != null && !jsonObj.get("member").isJsonNull()) {
        MemberEnum.validateJsonElement(jsonObj.get("member"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExpenseModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExpenseModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExpenseModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExpenseModel.class));

       return (TypeAdapter<T>) new TypeAdapter<ExpenseModel>() {
           @Override
           public void write(JsonWriter out, ExpenseModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExpenseModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExpenseModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExpenseModel
   * @throws IOException if the JSON string is invalid with respect to ExpenseModel
   */
  public static ExpenseModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExpenseModel.class);
  }

  /**
   * Convert an instance of ExpenseModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

