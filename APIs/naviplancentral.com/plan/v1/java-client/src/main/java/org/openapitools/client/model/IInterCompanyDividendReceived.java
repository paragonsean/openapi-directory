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
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.FormattedEnumTypeInterCompanyDividendType;
import org.openapitools.client.model.IActivityData;

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
 * IInterCompanyDividendReceived
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IInterCompanyDividendReceived {
  public static final String SERIALIZED_NAME_ACTIVITY_DATA = "activityData";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_DATA)
  private IActivityData activityData;

  public static final String SERIALIZED_NAME_DIVIDEND_TYPE = "dividendType";
  @SerializedName(SERIALIZED_NAME_DIVIDEND_TYPE)
  private FormattedEnumTypeInterCompanyDividendType dividendType;

  public static final String SERIALIZED_NAME_GENERAL_RATE_OF_INCOME_POOL_AMOUNT = "generalRateOfIncomePoolAmount";
  @SerializedName(SERIALIZED_NAME_GENERAL_RATE_OF_INCOME_POOL_AMOUNT)
  private Currency generalRateOfIncomePoolAmount;

  public static final String SERIALIZED_NAME_RECEIVED_FROM = "receivedFrom";
  @SerializedName(SERIALIZED_NAME_RECEIVED_FROM)
  private String receivedFrom;

  public IInterCompanyDividendReceived() {
  }

  public IInterCompanyDividendReceived(
     String receivedFrom
  ) {
    this();
    this.receivedFrom = receivedFrom;
  }

  public IInterCompanyDividendReceived activityData(IActivityData activityData) {
    this.activityData = activityData;
    return this;
  }

  /**
   * Get activityData
   * @return activityData
   */
  @javax.annotation.Nullable
  public IActivityData getActivityData() {
    return activityData;
  }

  public void setActivityData(IActivityData activityData) {
    this.activityData = activityData;
  }


  public IInterCompanyDividendReceived dividendType(FormattedEnumTypeInterCompanyDividendType dividendType) {
    this.dividendType = dividendType;
    return this;
  }

  /**
   * Get dividendType
   * @return dividendType
   */
  @javax.annotation.Nullable
  public FormattedEnumTypeInterCompanyDividendType getDividendType() {
    return dividendType;
  }

  public void setDividendType(FormattedEnumTypeInterCompanyDividendType dividendType) {
    this.dividendType = dividendType;
  }


  public IInterCompanyDividendReceived generalRateOfIncomePoolAmount(Currency generalRateOfIncomePoolAmount) {
    this.generalRateOfIncomePoolAmount = generalRateOfIncomePoolAmount;
    return this;
  }

  /**
   * Get generalRateOfIncomePoolAmount
   * @return generalRateOfIncomePoolAmount
   */
  @javax.annotation.Nullable
  public Currency getGeneralRateOfIncomePoolAmount() {
    return generalRateOfIncomePoolAmount;
  }

  public void setGeneralRateOfIncomePoolAmount(Currency generalRateOfIncomePoolAmount) {
    this.generalRateOfIncomePoolAmount = generalRateOfIncomePoolAmount;
  }


  /**
   * Get receivedFrom
   * @return receivedFrom
   */
  @javax.annotation.Nullable
  public String getReceivedFrom() {
    return receivedFrom;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IInterCompanyDividendReceived iinterCompanyDividendReceived = (IInterCompanyDividendReceived) o;
    return Objects.equals(this.activityData, iinterCompanyDividendReceived.activityData) &&
        Objects.equals(this.dividendType, iinterCompanyDividendReceived.dividendType) &&
        Objects.equals(this.generalRateOfIncomePoolAmount, iinterCompanyDividendReceived.generalRateOfIncomePoolAmount) &&
        Objects.equals(this.receivedFrom, iinterCompanyDividendReceived.receivedFrom);
  }

  @Override
  public int hashCode() {
    return Objects.hash(activityData, dividendType, generalRateOfIncomePoolAmount, receivedFrom);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IInterCompanyDividendReceived {\n");
    sb.append("    activityData: ").append(toIndentedString(activityData)).append("\n");
    sb.append("    dividendType: ").append(toIndentedString(dividendType)).append("\n");
    sb.append("    generalRateOfIncomePoolAmount: ").append(toIndentedString(generalRateOfIncomePoolAmount)).append("\n");
    sb.append("    receivedFrom: ").append(toIndentedString(receivedFrom)).append("\n");
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
    openapiFields.add("activityData");
    openapiFields.add("dividendType");
    openapiFields.add("generalRateOfIncomePoolAmount");
    openapiFields.add("receivedFrom");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IInterCompanyDividendReceived
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IInterCompanyDividendReceived.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IInterCompanyDividendReceived is not found in the empty JSON string", IInterCompanyDividendReceived.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IInterCompanyDividendReceived.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IInterCompanyDividendReceived` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `activityData`
      if (jsonObj.get("activityData") != null && !jsonObj.get("activityData").isJsonNull()) {
        IActivityData.validateJsonElement(jsonObj.get("activityData"));
      }
      // validate the optional field `dividendType`
      if (jsonObj.get("dividendType") != null && !jsonObj.get("dividendType").isJsonNull()) {
        FormattedEnumTypeInterCompanyDividendType.validateJsonElement(jsonObj.get("dividendType"));
      }
      // validate the optional field `generalRateOfIncomePoolAmount`
      if (jsonObj.get("generalRateOfIncomePoolAmount") != null && !jsonObj.get("generalRateOfIncomePoolAmount").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("generalRateOfIncomePoolAmount"));
      }
      if ((jsonObj.get("receivedFrom") != null && !jsonObj.get("receivedFrom").isJsonNull()) && !jsonObj.get("receivedFrom").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `receivedFrom` to be a primitive type in the JSON string but got `%s`", jsonObj.get("receivedFrom").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IInterCompanyDividendReceived.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IInterCompanyDividendReceived' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IInterCompanyDividendReceived> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IInterCompanyDividendReceived.class));

       return (TypeAdapter<T>) new TypeAdapter<IInterCompanyDividendReceived>() {
           @Override
           public void write(JsonWriter out, IInterCompanyDividendReceived value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IInterCompanyDividendReceived read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IInterCompanyDividendReceived given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IInterCompanyDividendReceived
   * @throws IOException if the JSON string is invalid with respect to IInterCompanyDividendReceived
   */
  public static IInterCompanyDividendReceived fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IInterCompanyDividendReceived.class);
  }

  /**
   * Convert an instance of IInterCompanyDividendReceived to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

