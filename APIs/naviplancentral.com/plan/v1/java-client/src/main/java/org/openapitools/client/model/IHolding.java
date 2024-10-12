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
import org.openapitools.client.model.IAssetMix;
import org.openapitools.client.model.IAssetValuation;
import org.openapitools.client.model.IPeriodRateOfReturnDetails;
import org.openapitools.client.model.PercentOrCurrency;

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
 * IHolding
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IHolding {
  public static final String SERIALIZED_NAME_ASSET_MIX = "assetMix";
  @SerializedName(SERIALIZED_NAME_ASSET_MIX)
  private IAssetMix assetMix;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_HOLD_AMOUNT = "holdAmount";
  @SerializedName(SERIALIZED_NAME_HOLD_AMOUNT)
  private PercentOrCurrency holdAmount;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_CLASSIFIED = "isClassified";
  @SerializedName(SERIALIZED_NAME_IS_CLASSIFIED)
  private Boolean isClassified;

  public static final String SERIALIZED_NAME_PRE_RETIREMENT_RETURN_RATES = "preRetirementReturnRates";
  @SerializedName(SERIALIZED_NAME_PRE_RETIREMENT_RETURN_RATES)
  private IPeriodRateOfReturnDetails preRetirementReturnRates;

  public static final String SERIALIZED_NAME_RETIREMENT_RETURN_RATES = "retirementReturnRates";
  @SerializedName(SERIALIZED_NAME_RETIREMENT_RETURN_RATES)
  private IPeriodRateOfReturnDetails retirementReturnRates;

  public static final String SERIALIZED_NAME_SYMBOL = "symbol";
  @SerializedName(SERIALIZED_NAME_SYMBOL)
  private String symbol;

  public static final String SERIALIZED_NAME_VALUATION = "valuation";
  @SerializedName(SERIALIZED_NAME_VALUATION)
  private IAssetValuation valuation;

  public IHolding() {
  }

  public IHolding(
     String description, 
     String id, 
     Boolean isClassified, 
     String symbol
  ) {
    this();
    this.description = description;
    this.id = id;
    this.isClassified = isClassified;
    this.symbol = symbol;
  }

  public IHolding assetMix(IAssetMix assetMix) {
    this.assetMix = assetMix;
    return this;
  }

  /**
   * Get assetMix
   * @return assetMix
   */
  @javax.annotation.Nullable
  public IAssetMix getAssetMix() {
    return assetMix;
  }

  public void setAssetMix(IAssetMix assetMix) {
    this.assetMix = assetMix;
  }


  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }



  public IHolding holdAmount(PercentOrCurrency holdAmount) {
    this.holdAmount = holdAmount;
    return this;
  }

  /**
   * Get holdAmount
   * @return holdAmount
   */
  @javax.annotation.Nullable
  public PercentOrCurrency getHoldAmount() {
    return holdAmount;
  }

  public void setHoldAmount(PercentOrCurrency holdAmount) {
    this.holdAmount = holdAmount;
  }


  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * Get isClassified
   * @return isClassified
   */
  @javax.annotation.Nullable
  public Boolean getIsClassified() {
    return isClassified;
  }



  public IHolding preRetirementReturnRates(IPeriodRateOfReturnDetails preRetirementReturnRates) {
    this.preRetirementReturnRates = preRetirementReturnRates;
    return this;
  }

  /**
   * Get preRetirementReturnRates
   * @return preRetirementReturnRates
   */
  @javax.annotation.Nullable
  public IPeriodRateOfReturnDetails getPreRetirementReturnRates() {
    return preRetirementReturnRates;
  }

  public void setPreRetirementReturnRates(IPeriodRateOfReturnDetails preRetirementReturnRates) {
    this.preRetirementReturnRates = preRetirementReturnRates;
  }


  public IHolding retirementReturnRates(IPeriodRateOfReturnDetails retirementReturnRates) {
    this.retirementReturnRates = retirementReturnRates;
    return this;
  }

  /**
   * Get retirementReturnRates
   * @return retirementReturnRates
   */
  @javax.annotation.Nullable
  public IPeriodRateOfReturnDetails getRetirementReturnRates() {
    return retirementReturnRates;
  }

  public void setRetirementReturnRates(IPeriodRateOfReturnDetails retirementReturnRates) {
    this.retirementReturnRates = retirementReturnRates;
  }


  /**
   * Get symbol
   * @return symbol
   */
  @javax.annotation.Nullable
  public String getSymbol() {
    return symbol;
  }



  public IHolding valuation(IAssetValuation valuation) {
    this.valuation = valuation;
    return this;
  }

  /**
   * Get valuation
   * @return valuation
   */
  @javax.annotation.Nullable
  public IAssetValuation getValuation() {
    return valuation;
  }

  public void setValuation(IAssetValuation valuation) {
    this.valuation = valuation;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IHolding iholding = (IHolding) o;
    return Objects.equals(this.assetMix, iholding.assetMix) &&
        Objects.equals(this.description, iholding.description) &&
        Objects.equals(this.holdAmount, iholding.holdAmount) &&
        Objects.equals(this.id, iholding.id) &&
        Objects.equals(this.isClassified, iholding.isClassified) &&
        Objects.equals(this.preRetirementReturnRates, iholding.preRetirementReturnRates) &&
        Objects.equals(this.retirementReturnRates, iholding.retirementReturnRates) &&
        Objects.equals(this.symbol, iholding.symbol) &&
        Objects.equals(this.valuation, iholding.valuation);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetMix, description, holdAmount, id, isClassified, preRetirementReturnRates, retirementReturnRates, symbol, valuation);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IHolding {\n");
    sb.append("    assetMix: ").append(toIndentedString(assetMix)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    holdAmount: ").append(toIndentedString(holdAmount)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isClassified: ").append(toIndentedString(isClassified)).append("\n");
    sb.append("    preRetirementReturnRates: ").append(toIndentedString(preRetirementReturnRates)).append("\n");
    sb.append("    retirementReturnRates: ").append(toIndentedString(retirementReturnRates)).append("\n");
    sb.append("    symbol: ").append(toIndentedString(symbol)).append("\n");
    sb.append("    valuation: ").append(toIndentedString(valuation)).append("\n");
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
    openapiFields.add("assetMix");
    openapiFields.add("description");
    openapiFields.add("holdAmount");
    openapiFields.add("id");
    openapiFields.add("isClassified");
    openapiFields.add("preRetirementReturnRates");
    openapiFields.add("retirementReturnRates");
    openapiFields.add("symbol");
    openapiFields.add("valuation");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IHolding
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IHolding.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IHolding is not found in the empty JSON string", IHolding.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IHolding.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IHolding` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `assetMix`
      if (jsonObj.get("assetMix") != null && !jsonObj.get("assetMix").isJsonNull()) {
        IAssetMix.validateJsonElement(jsonObj.get("assetMix"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `holdAmount`
      if (jsonObj.get("holdAmount") != null && !jsonObj.get("holdAmount").isJsonNull()) {
        PercentOrCurrency.validateJsonElement(jsonObj.get("holdAmount"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `preRetirementReturnRates`
      if (jsonObj.get("preRetirementReturnRates") != null && !jsonObj.get("preRetirementReturnRates").isJsonNull()) {
        IPeriodRateOfReturnDetails.validateJsonElement(jsonObj.get("preRetirementReturnRates"));
      }
      // validate the optional field `retirementReturnRates`
      if (jsonObj.get("retirementReturnRates") != null && !jsonObj.get("retirementReturnRates").isJsonNull()) {
        IPeriodRateOfReturnDetails.validateJsonElement(jsonObj.get("retirementReturnRates"));
      }
      if ((jsonObj.get("symbol") != null && !jsonObj.get("symbol").isJsonNull()) && !jsonObj.get("symbol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `symbol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("symbol").toString()));
      }
      // validate the optional field `valuation`
      if (jsonObj.get("valuation") != null && !jsonObj.get("valuation").isJsonNull()) {
        IAssetValuation.validateJsonElement(jsonObj.get("valuation"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IHolding.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IHolding' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IHolding> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IHolding.class));

       return (TypeAdapter<T>) new TypeAdapter<IHolding>() {
           @Override
           public void write(JsonWriter out, IHolding value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IHolding read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IHolding given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IHolding
   * @throws IOException if the JSON string is invalid with respect to IHolding
   */
  public static IHolding fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IHolding.class);
  }

  /**
   * Convert an instance of IHolding to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

