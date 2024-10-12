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
 * InputMarketIndex
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:11.265696-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InputMarketIndex {
  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  /**
   * Market index
   */
  @JsonAdapter(SymbolEnum.Adapter.class)
  public enum SymbolEnum {
    DJA_INDX_DOW_JONES_COMPOSITE_AVERAGE_("DJA.INDX (Dow Jones Composite Average)"),
    
    DJI_INDX_DOW_JONES_INDUSTRIAL_AVERAGE_("DJI.INDX (Dow Jones Industrial Average)"),
    
    DJT_INDX_DOW_JONES_TRANSPORTATION_("DJT.INDX (Dow Jones Transportation)"),
    
    DJUS_INDX_DOW_JONES_US_("DJUS.INDX (Dow Jones US)"),
    
    DXY_INDX_US_DOLLAR_INDEX_("DXY.INDX (US Dollar Index)"),
    
    GDOW_INDX_GLOBAL_DOW_USD_("GDOW.INDX (Global Dow USD)"),
    
    NY_INDX_NYSE_US_100_INDEX_("NY.INDX (NYSE US 100 Index)"),
    
    NYA_INDX_NYSE_COMPOSITE_("NYA.INDX (NYSE Composite)"),
    
    IXIC_INDX_NASDAQ_COMPOSITE_("IXIC.INDX (NASDAQ Composite)"),
    
    NDX_INDX_NASDAQ_100_("NDX.INDX (NASDAQ 100)"),
    
    GSPC_INDX_S_P_500_("GSPC.INDX (S&P 500)"),
    
    ES_INDX_S_P_500_FUTURES_("ES.INDX (S&P 500 Futures)"),
    
    MID_INDX_S_P_MIDCAP_400_("MID.INDX (S&P Midcap 400)"),
    
    GPTSE_INDX_S_P_TSX_COMPOSITE_INDEX_CANADA_("GPTSE.INDX (S&P TSX Composite Index [Canada])"),
    
    FTSE_INDX_FTSE_100_INDEX_UK_("FTSE.INDX (FTSE 100 Index [UK])"),
    
    CDAXX_INDX_DAX_COMPOSITE_INDEX_GERMANY_("CDAXX.INDX (DAX Composite Index [Germany])"),
    
    GDAXI_INDX_DAX_INDEX_GERMANY_("GDAXI.INDX (DAX Index [Germany])"),
    
    HSCE_INDX_HANG_SENG_CHINA_ENTERPRISE_CEI_("HSCE.INDX (Hang Seng China Enterprise (CEI))"),
    
    HSI_INDX_HANG_SENG_INDEX_HONG_KONG_("HSI.INDX (Hang Seng Index [Hong Kong])"),
    
    N100_INDX_EURO_NEXT_100_("N100.INDX (EuroNext 100)"),
    
    N225_INDX_NIKKEI_225_INDEX_("N225.INDX (Nikkei 225 Index)"),
    
    RTSI_INDX_RTSI_INDEX_RUSSIA_("RTSI.INDX (RTSI Index [Russia])"),
    
    SSEC_INDX_SHANGHAI_COMPOSITE_("SSEC.INDX (Shanghai Composite)"),
    
    SSMI_INDX_SWISS_MARKET_INDEX_("SSMI.INDX (Swiss Market Index)");

    private String value;

    SymbolEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SymbolEnum fromValue(String value) {
      for (SymbolEnum b : SymbolEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SymbolEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SymbolEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SymbolEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SymbolEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SymbolEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SYMBOL = "symbol";
  @SerializedName(SERIALIZED_NAME_SYMBOL)
  private SymbolEnum symbol;

  public InputMarketIndex() {
  }

  public InputMarketIndex date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Date (yyyy-MM-dd, leave empty for last trading day)
   * @return date
   */
  @javax.annotation.Nullable
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }


  public InputMarketIndex symbol(SymbolEnum symbol) {
    this.symbol = symbol;
    return this;
  }

  /**
   * Market index
   * @return symbol
   */
  @javax.annotation.Nonnull
  public SymbolEnum getSymbol() {
    return symbol;
  }

  public void setSymbol(SymbolEnum symbol) {
    this.symbol = symbol;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InputMarketIndex inputMarketIndex = (InputMarketIndex) o;
    return Objects.equals(this.date, inputMarketIndex.date) &&
        Objects.equals(this.symbol, inputMarketIndex.symbol);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date, symbol);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InputMarketIndex {\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    symbol: ").append(toIndentedString(symbol)).append("\n");
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
    openapiFields.add("symbol");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("symbol");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InputMarketIndex
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InputMarketIndex.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InputMarketIndex is not found in the empty JSON string", InputMarketIndex.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InputMarketIndex.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InputMarketIndex` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : InputMarketIndex.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("date") != null && !jsonObj.get("date").isJsonNull()) && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if (!jsonObj.get("symbol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `symbol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("symbol").toString()));
      }
      // validate the required field `symbol`
      SymbolEnum.validateJsonElement(jsonObj.get("symbol"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InputMarketIndex.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InputMarketIndex' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InputMarketIndex> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InputMarketIndex.class));

       return (TypeAdapter<T>) new TypeAdapter<InputMarketIndex>() {
           @Override
           public void write(JsonWriter out, InputMarketIndex value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InputMarketIndex read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InputMarketIndex given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InputMarketIndex
   * @throws IOException if the JSON string is invalid with respect to InputMarketIndex
   */
  public static InputMarketIndex fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InputMarketIndex.class);
  }

  /**
   * Convert an instance of InputMarketIndex to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

