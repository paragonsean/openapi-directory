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
import org.openapitools.client.model.Currency;
import org.openapitools.client.model.GrowthRateValues;

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
 * ILumpSumDebtModStrategy
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ILumpSumDebtModStrategy {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Currency amount;

  public static final String SERIALIZED_NAME_DEBT_MODIFICATION_DATE = "debtModificationDate";
  @SerializedName(SERIALIZED_NAME_DEBT_MODIFICATION_DATE)
  private Date debtModificationDate;

  public static final String SERIALIZED_NAME_INDEX_RATE = "indexRate";
  @SerializedName(SERIALIZED_NAME_INDEX_RATE)
  private GrowthRateValues indexRate;

  public ILumpSumDebtModStrategy() {
  }

  public ILumpSumDebtModStrategy amount(Currency amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Get amount
   * @return amount
   */
  @javax.annotation.Nullable
  public Currency getAmount() {
    return amount;
  }

  public void setAmount(Currency amount) {
    this.amount = amount;
  }


  public ILumpSumDebtModStrategy debtModificationDate(Date debtModificationDate) {
    this.debtModificationDate = debtModificationDate;
    return this;
  }

  /**
   * Get debtModificationDate
   * @return debtModificationDate
   */
  @javax.annotation.Nullable
  public Date getDebtModificationDate() {
    return debtModificationDate;
  }

  public void setDebtModificationDate(Date debtModificationDate) {
    this.debtModificationDate = debtModificationDate;
  }


  public ILumpSumDebtModStrategy indexRate(GrowthRateValues indexRate) {
    this.indexRate = indexRate;
    return this;
  }

  /**
   * Get indexRate
   * @return indexRate
   */
  @javax.annotation.Nullable
  public GrowthRateValues getIndexRate() {
    return indexRate;
  }

  public void setIndexRate(GrowthRateValues indexRate) {
    this.indexRate = indexRate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ILumpSumDebtModStrategy ilumpSumDebtModStrategy = (ILumpSumDebtModStrategy) o;
    return Objects.equals(this.amount, ilumpSumDebtModStrategy.amount) &&
        Objects.equals(this.debtModificationDate, ilumpSumDebtModStrategy.debtModificationDate) &&
        Objects.equals(this.indexRate, ilumpSumDebtModStrategy.indexRate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, debtModificationDate, indexRate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ILumpSumDebtModStrategy {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    debtModificationDate: ").append(toIndentedString(debtModificationDate)).append("\n");
    sb.append("    indexRate: ").append(toIndentedString(indexRate)).append("\n");
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
    openapiFields.add("debtModificationDate");
    openapiFields.add("indexRate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ILumpSumDebtModStrategy
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ILumpSumDebtModStrategy.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ILumpSumDebtModStrategy is not found in the empty JSON string", ILumpSumDebtModStrategy.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ILumpSumDebtModStrategy.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ILumpSumDebtModStrategy` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `amount`
      if (jsonObj.get("amount") != null && !jsonObj.get("amount").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("amount"));
      }
      // validate the optional field `debtModificationDate`
      if (jsonObj.get("debtModificationDate") != null && !jsonObj.get("debtModificationDate").isJsonNull()) {
        Date.validateJsonElement(jsonObj.get("debtModificationDate"));
      }
      // validate the optional field `indexRate`
      if (jsonObj.get("indexRate") != null && !jsonObj.get("indexRate").isJsonNull()) {
        GrowthRateValues.validateJsonElement(jsonObj.get("indexRate"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ILumpSumDebtModStrategy.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ILumpSumDebtModStrategy' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ILumpSumDebtModStrategy> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ILumpSumDebtModStrategy.class));

       return (TypeAdapter<T>) new TypeAdapter<ILumpSumDebtModStrategy>() {
           @Override
           public void write(JsonWriter out, ILumpSumDebtModStrategy value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ILumpSumDebtModStrategy read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ILumpSumDebtModStrategy given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ILumpSumDebtModStrategy
   * @throws IOException if the JSON string is invalid with respect to ILumpSumDebtModStrategy
   */
  public static ILumpSumDebtModStrategy fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ILumpSumDebtModStrategy.class);
  }

  /**
   * Convert an instance of ILumpSumDebtModStrategy to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

