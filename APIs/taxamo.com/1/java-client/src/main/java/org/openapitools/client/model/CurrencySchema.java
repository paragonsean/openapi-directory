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
 * CurrencySchema
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:16.755158-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CurrencySchema {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ISOCODE = "isocode";
  @SerializedName(SERIALIZED_NAME_ISOCODE)
  private String isocode;

  public static final String SERIALIZED_NAME_ISONUM = "isonum";
  @SerializedName(SERIALIZED_NAME_ISONUM)
  private Integer isonum;

  public static final String SERIALIZED_NAME_MINORUNITS = "minorunits";
  @SerializedName(SERIALIZED_NAME_MINORUNITS)
  private Integer minorunits;

  public CurrencySchema() {
  }

  public CurrencySchema code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Currency 3-letter ISO code.
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public CurrencySchema description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Currency description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public CurrencySchema isocode(String isocode) {
    this.isocode = isocode;
    return this;
  }

  /**
   * Currency 3-letter ISO code.
   * @return isocode
   */
  @javax.annotation.Nullable
  public String getIsocode() {
    return isocode;
  }

  public void setIsocode(String isocode) {
    this.isocode = isocode;
  }


  public CurrencySchema isonum(Integer isonum) {
    this.isonum = isonum;
    return this;
  }

  /**
   * Currency iso numeric code.
   * @return isonum
   */
  @javax.annotation.Nullable
  public Integer getIsonum() {
    return isonum;
  }

  public void setIsonum(Integer isonum) {
    this.isonum = isonum;
  }


  public CurrencySchema minorunits(Integer minorunits) {
    this.minorunits = minorunits;
    return this;
  }

  /**
   * Number of minor units for currency.
   * @return minorunits
   */
  @javax.annotation.Nullable
  public Integer getMinorunits() {
    return minorunits;
  }

  public void setMinorunits(Integer minorunits) {
    this.minorunits = minorunits;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CurrencySchema currencySchema = (CurrencySchema) o;
    return Objects.equals(this.code, currencySchema.code) &&
        Objects.equals(this.description, currencySchema.description) &&
        Objects.equals(this.isocode, currencySchema.isocode) &&
        Objects.equals(this.isonum, currencySchema.isonum) &&
        Objects.equals(this.minorunits, currencySchema.minorunits);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, description, isocode, isonum, minorunits);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CurrencySchema {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    isocode: ").append(toIndentedString(isocode)).append("\n");
    sb.append("    isonum: ").append(toIndentedString(isonum)).append("\n");
    sb.append("    minorunits: ").append(toIndentedString(minorunits)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("description");
    openapiFields.add("isocode");
    openapiFields.add("isonum");
    openapiFields.add("minorunits");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CurrencySchema
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CurrencySchema.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CurrencySchema is not found in the empty JSON string", CurrencySchema.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CurrencySchema.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CurrencySchema` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("isocode") != null && !jsonObj.get("isocode").isJsonNull()) && !jsonObj.get("isocode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `isocode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("isocode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CurrencySchema.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CurrencySchema' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CurrencySchema> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CurrencySchema.class));

       return (TypeAdapter<T>) new TypeAdapter<CurrencySchema>() {
           @Override
           public void write(JsonWriter out, CurrencySchema value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CurrencySchema read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CurrencySchema given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CurrencySchema
   * @throws IOException if the JSON string is invalid with respect to CurrencySchema
   */
  public static CurrencySchema fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CurrencySchema.class);
  }

  /**
   * Convert an instance of CurrencySchema to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

