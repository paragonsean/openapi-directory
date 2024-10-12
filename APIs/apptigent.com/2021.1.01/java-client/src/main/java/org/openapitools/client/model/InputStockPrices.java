/*
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
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
 * InputStockPrices
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:11.265696-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InputStockPrices {
  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  /**
   * Stock exchange
   */
  @JsonAdapter(ExchangeEnum.Adapter.class)
  public enum ExchangeEnum {
    XNYS_NEW_YORK_STOCK_EXCHANGE_("XNYS (New York Stock Exchange)"),
    
    XNAS_NASDAQ_STOCK_EXCHANGE_("XNAS (NASDAQ Stock Exchange)"),
    
    XBRU_EURONEXT_BRUSSELS_("XBRU (Euronext Brussels)"),
    
    XTSE_TORONTO_STOCK_EXCHANGE_("XTSE (Toronto Stock Exchange)"),
    
    XCNQ_CANDADIAN_SECURITIES_EXCHANGE_("XCNQ (Candadian Securities Exchange)"),
    
    XSHG_SHANGHAI_STOCK_EXCHANGE_("XSHG (Shanghai Stock Exchange)"),
    
    XCSE_COPENHAGEN_STOCK_EXCHANGE_("XCSE (Copenhagen Stock Exchange)"),
    
    XPAR_EURONEXT_PARIS_("XPAR (Euronext Paris)"),
    
    XFRA_DEUTSCHE_BORSE_("XFRA (Deutsche Borse)"),
    
    XHKG_HONG_KONG_STOCK_EXCHANGE_("XHKG (Hong Kong Stock Exchange)"),
    
    XNSE_NATIONAL_STOCK_EXCHANGE_INDIA_("XNSE (National Stock Exchange India)"),
    
    XTAE_TEL_AVIV_STOCK_EXCHANGE_("XTAE (Tel Aviv Stock Exchange)"),
    
    XNGO_NAGOYA_STOCK_EXCHANGE_("XNGO (Nagoya Stock Exchange)"),
    
    XFKA_FUKUOKA_STOCK_EXCHANGE_("XFKA (Fukuoka Stock Exchange)"),
    
    XSAP_SAPPORO_STOCK_EXCHANGE_("XSAP (Sapporo Stock Exchange)"),
    
    XMEX_MEXICAN_STOCK_EXCHANGE_("XMEX (Mexican Stock Exchange)"),
    
    XNZE_NEW_ZEALAND_STOCK_EXCHANGE_("XNZE (New Zealand Stock Exchange)"),
    
    XLIS_EURONEXT_LISBON_("XLIS (Euronext Lisbon)"),
    
    MISX_MOSCOW_STOCK_EXCHANGE_("MISX (Moscow Stock Exchange)"),
    
    XSES_SINGAPORE_STOCK_EXCHANGE_("XSES (Singapore Stock Exchange)"),
    
    XLON_LONDON_STOCK_EXCHANGE_("XLON (London Stock Exchange)"),
    
    XASE_AMERICAN_STOCK_EXCHANGE_("XASE (American Stock Exchange)"),
    
    XASX_AUSTRALIA_STOCK_EXCHANGE_("XASX (Australia Stock Exchange)"),
    
    XDFM_DUBAI_FINANCIAL_MARKET_("XDFM (Dubai Financial Market)"),
    
    XBKK_STOCK_EXCHANGE_OF_THAILAND_("XBKK (Stock Exchange of Thailand)"),
    
    XSWX_SIX_SWISS_EXCHANGE_("XSWX (SIX Swiss Exchange)"),
    
    XSTO_STOCKHOLM_STOCK_EXCHANGE_("XSTO (Stockholm Stock Exchange)"),
    
    BMEX_BOLSAS_Y_MERCADOS_ESPA_OLES_("BMEX (Bolsas y Mercados Españoles)"),
    
    XJSE_JOHANNESBURG_STOCK_EXCHANGE_("XJSE (Johannesburg Stock Exchange)");

    private String value;

    ExchangeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ExchangeEnum fromValue(String value) {
      for (ExchangeEnum b : ExchangeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ExchangeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ExchangeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ExchangeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ExchangeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ExchangeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EXCHANGE = "exchange";
  @SerializedName(SERIALIZED_NAME_EXCHANGE)
  private ExchangeEnum exchange;

  public static final String SERIALIZED_NAME_SYMBOLS = "symbols";
  @SerializedName(SERIALIZED_NAME_SYMBOLS)
  private String symbols;

  public InputStockPrices() {
  }

  public InputStockPrices date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Date (yyyy-MM-dd, leave empty for latest)
   * @return date
   */
  @javax.annotation.Nullable
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }


  public InputStockPrices exchange(ExchangeEnum exchange) {
    this.exchange = exchange;
    return this;
  }

  /**
   * Stock exchange
   * @return exchange
   */
  @javax.annotation.Nullable
  public ExchangeEnum getExchange() {
    return exchange;
  }

  public void setExchange(ExchangeEnum exchange) {
    this.exchange = exchange;
  }


  public InputStockPrices symbols(String symbols) {
    this.symbols = symbols;
    return this;
  }

  /**
   * Stock ticker symbols (comma-separated, max 20)
   * @return symbols
   */
  @javax.annotation.Nonnull
  public String getSymbols() {
    return symbols;
  }

  public void setSymbols(String symbols) {
    this.symbols = symbols;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InputStockPrices inputStockPrices = (InputStockPrices) o;
    return Objects.equals(this.date, inputStockPrices.date) &&
        Objects.equals(this.exchange, inputStockPrices.exchange) &&
        Objects.equals(this.symbols, inputStockPrices.symbols);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date, exchange, symbols);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InputStockPrices {\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    exchange: ").append(toIndentedString(exchange)).append("\n");
    sb.append("    symbols: ").append(toIndentedString(symbols)).append("\n");
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
    openapiFields.add("date");
    openapiFields.add("exchange");
    openapiFields.add("symbols");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("symbols");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InputStockPrices
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InputStockPrices.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InputStockPrices is not found in the empty JSON string", InputStockPrices.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InputStockPrices.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InputStockPrices` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : InputStockPrices.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("date") != null && !jsonObj.get("date").isJsonNull()) && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if ((jsonObj.get("exchange") != null && !jsonObj.get("exchange").isJsonNull()) && !jsonObj.get("exchange").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exchange` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exchange").toString()));
      }
      // validate the optional field `exchange`
      if (jsonObj.get("exchange") != null && !jsonObj.get("exchange").isJsonNull()) {
        ExchangeEnum.validateJsonElement(jsonObj.get("exchange"));
      }
      if (!jsonObj.get("symbols").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `symbols` to be a primitive type in the JSON string but got `%s`", jsonObj.get("symbols").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InputStockPrices.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InputStockPrices' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InputStockPrices> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InputStockPrices.class));

       return (TypeAdapter<T>) new TypeAdapter<InputStockPrices>() {
           @Override
           public void write(JsonWriter out, InputStockPrices value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InputStockPrices read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InputStockPrices given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InputStockPrices
   * @throws IOException if the JSON string is invalid with respect to InputStockPrices
   */
  public static InputStockPrices fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InputStockPrices.class);
  }

  /**
   * Convert an instance of InputStockPrices to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

