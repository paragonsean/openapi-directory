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
import org.openapitools.client.model.ICashFlowIncomes;
import org.openapitools.client.model.ICashFlowOutflows;
import org.openapitools.client.model.ITaxes;

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
 * ICashFlow
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ICashFlow {
  public static final String SERIALIZED_NAME_INCOMES = "incomes";
  @SerializedName(SERIALIZED_NAME_INCOMES)
  private ICashFlowIncomes incomes;

  public static final String SERIALIZED_NAME_OUTFLOWS = "outflows";
  @SerializedName(SERIALIZED_NAME_OUTFLOWS)
  private ICashFlowOutflows outflows;

  public static final String SERIALIZED_NAME_SURPLUS_DEFICIT = "surplusDeficit";
  @SerializedName(SERIALIZED_NAME_SURPLUS_DEFICIT)
  private Currency surplusDeficit;

  public static final String SERIALIZED_NAME_TAXES = "taxes";
  @SerializedName(SERIALIZED_NAME_TAXES)
  private ITaxes taxes;

  public ICashFlow() {
  }

  public ICashFlow incomes(ICashFlowIncomes incomes) {
    this.incomes = incomes;
    return this;
  }

  /**
   * Get incomes
   * @return incomes
   */
  @javax.annotation.Nullable
  public ICashFlowIncomes getIncomes() {
    return incomes;
  }

  public void setIncomes(ICashFlowIncomes incomes) {
    this.incomes = incomes;
  }


  public ICashFlow outflows(ICashFlowOutflows outflows) {
    this.outflows = outflows;
    return this;
  }

  /**
   * Get outflows
   * @return outflows
   */
  @javax.annotation.Nullable
  public ICashFlowOutflows getOutflows() {
    return outflows;
  }

  public void setOutflows(ICashFlowOutflows outflows) {
    this.outflows = outflows;
  }


  public ICashFlow surplusDeficit(Currency surplusDeficit) {
    this.surplusDeficit = surplusDeficit;
    return this;
  }

  /**
   * Get surplusDeficit
   * @return surplusDeficit
   */
  @javax.annotation.Nullable
  public Currency getSurplusDeficit() {
    return surplusDeficit;
  }

  public void setSurplusDeficit(Currency surplusDeficit) {
    this.surplusDeficit = surplusDeficit;
  }


  public ICashFlow taxes(ITaxes taxes) {
    this.taxes = taxes;
    return this;
  }

  /**
   * Get taxes
   * @return taxes
   */
  @javax.annotation.Nullable
  public ITaxes getTaxes() {
    return taxes;
  }

  public void setTaxes(ITaxes taxes) {
    this.taxes = taxes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ICashFlow icashFlow = (ICashFlow) o;
    return Objects.equals(this.incomes, icashFlow.incomes) &&
        Objects.equals(this.outflows, icashFlow.outflows) &&
        Objects.equals(this.surplusDeficit, icashFlow.surplusDeficit) &&
        Objects.equals(this.taxes, icashFlow.taxes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(incomes, outflows, surplusDeficit, taxes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ICashFlow {\n");
    sb.append("    incomes: ").append(toIndentedString(incomes)).append("\n");
    sb.append("    outflows: ").append(toIndentedString(outflows)).append("\n");
    sb.append("    surplusDeficit: ").append(toIndentedString(surplusDeficit)).append("\n");
    sb.append("    taxes: ").append(toIndentedString(taxes)).append("\n");
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
    openapiFields.add("incomes");
    openapiFields.add("outflows");
    openapiFields.add("surplusDeficit");
    openapiFields.add("taxes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ICashFlow
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ICashFlow.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ICashFlow is not found in the empty JSON string", ICashFlow.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ICashFlow.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ICashFlow` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `incomes`
      if (jsonObj.get("incomes") != null && !jsonObj.get("incomes").isJsonNull()) {
        ICashFlowIncomes.validateJsonElement(jsonObj.get("incomes"));
      }
      // validate the optional field `outflows`
      if (jsonObj.get("outflows") != null && !jsonObj.get("outflows").isJsonNull()) {
        ICashFlowOutflows.validateJsonElement(jsonObj.get("outflows"));
      }
      // validate the optional field `surplusDeficit`
      if (jsonObj.get("surplusDeficit") != null && !jsonObj.get("surplusDeficit").isJsonNull()) {
        Currency.validateJsonElement(jsonObj.get("surplusDeficit"));
      }
      // validate the optional field `taxes`
      if (jsonObj.get("taxes") != null && !jsonObj.get("taxes").isJsonNull()) {
        ITaxes.validateJsonElement(jsonObj.get("taxes"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ICashFlow.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ICashFlow' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ICashFlow> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ICashFlow.class));

       return (TypeAdapter<T>) new TypeAdapter<ICashFlow>() {
           @Override
           public void write(JsonWriter out, ICashFlow value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ICashFlow read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ICashFlow given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ICashFlow
   * @throws IOException if the JSON string is invalid with respect to ICashFlow
   */
  public static ICashFlow fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ICashFlow.class);
  }

  /**
   * Convert an instance of ICashFlow to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

