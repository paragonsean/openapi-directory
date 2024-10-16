/*
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
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
 * GetRefundsIn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetRefundsIn {
  public static final String SERIALIZED_NAME_DATE_FROM = "date_from";
  @SerializedName(SERIALIZED_NAME_DATE_FROM)
  private String dateFrom;

  public static final String SERIALIZED_NAME_FORMAT = "format";
  @SerializedName(SERIALIZED_NAME_FORMAT)
  private String format;

  public static final String SERIALIZED_NAME_MOSS_COUNTRY_CODE = "moss_country_code";
  @SerializedName(SERIALIZED_NAME_MOSS_COUNTRY_CODE)
  private String mossCountryCode;

  public static final String SERIALIZED_NAME_TAX_REGION = "tax_region";
  @SerializedName(SERIALIZED_NAME_TAX_REGION)
  private String taxRegion;

  public GetRefundsIn() {
  }

  public GetRefundsIn dateFrom(String dateFrom) {
    this.dateFrom = dateFrom;
    return this;
  }

  /**
   * Take only refunds issued at or after the date. Format: yyyy-MM-dd
   * @return dateFrom
   */
  @javax.annotation.Nonnull
  public String getDateFrom() {
    return dateFrom;
  }

  public void setDateFrom(String dateFrom) {
    this.dateFrom = dateFrom;
  }


  public GetRefundsIn format(String format) {
    this.format = format;
    return this;
  }

  /**
   * Output format. &#39;csv&#39; value is accepted as well
   * @return format
   */
  @javax.annotation.Nullable
  public String getFormat() {
    return format;
  }

  public void setFormat(String format) {
    this.format = format;
  }


  public GetRefundsIn mossCountryCode(String mossCountryCode) {
    this.mossCountryCode = mossCountryCode;
    return this;
  }

  /**
   * MOSS country code, used to determine currency. If ommited, merchant default setting is used.
   * @return mossCountryCode
   */
  @javax.annotation.Nullable
  public String getMossCountryCode() {
    return mossCountryCode;
  }

  public void setMossCountryCode(String mossCountryCode) {
    this.mossCountryCode = mossCountryCode;
  }


  public GetRefundsIn taxRegion(String taxRegion) {
    this.taxRegion = taxRegion;
    return this;
  }

  /**
   * Tax region key, defaults to EU for backwards compatibility.
   * @return taxRegion
   */
  @javax.annotation.Nullable
  public String getTaxRegion() {
    return taxRegion;
  }

  public void setTaxRegion(String taxRegion) {
    this.taxRegion = taxRegion;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetRefundsIn getRefundsIn = (GetRefundsIn) o;
    return Objects.equals(this.dateFrom, getRefundsIn.dateFrom) &&
        Objects.equals(this.format, getRefundsIn.format) &&
        Objects.equals(this.mossCountryCode, getRefundsIn.mossCountryCode) &&
        Objects.equals(this.taxRegion, getRefundsIn.taxRegion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dateFrom, format, mossCountryCode, taxRegion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetRefundsIn {\n");
    sb.append("    dateFrom: ").append(toIndentedString(dateFrom)).append("\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
    sb.append("    mossCountryCode: ").append(toIndentedString(mossCountryCode)).append("\n");
    sb.append("    taxRegion: ").append(toIndentedString(taxRegion)).append("\n");
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
    openapiFields.add("date_from");
    openapiFields.add("format");
    openapiFields.add("moss_country_code");
    openapiFields.add("tax_region");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("date_from");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetRefundsIn
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetRefundsIn.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetRefundsIn is not found in the empty JSON string", GetRefundsIn.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetRefundsIn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetRefundsIn` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetRefundsIn.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("date_from").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_from` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_from").toString()));
      }
      if ((jsonObj.get("format") != null && !jsonObj.get("format").isJsonNull()) && !jsonObj.get("format").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `format` to be a primitive type in the JSON string but got `%s`", jsonObj.get("format").toString()));
      }
      if ((jsonObj.get("moss_country_code") != null && !jsonObj.get("moss_country_code").isJsonNull()) && !jsonObj.get("moss_country_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moss_country_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moss_country_code").toString()));
      }
      if ((jsonObj.get("tax_region") != null && !jsonObj.get("tax_region").isJsonNull()) && !jsonObj.get("tax_region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_region").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetRefundsIn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetRefundsIn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetRefundsIn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetRefundsIn.class));

       return (TypeAdapter<T>) new TypeAdapter<GetRefundsIn>() {
           @Override
           public void write(JsonWriter out, GetRefundsIn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetRefundsIn read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetRefundsIn given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetRefundsIn
   * @throws IOException if the JSON string is invalid with respect to GetRefundsIn
   */
  public static GetRefundsIn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetRefundsIn.class);
  }

  /**
   * Convert an instance of GetRefundsIn to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

