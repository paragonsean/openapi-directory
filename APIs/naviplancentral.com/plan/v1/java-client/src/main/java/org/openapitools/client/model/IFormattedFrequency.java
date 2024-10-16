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
 * IFormattedFrequency
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IFormattedFrequency {
  public static final String SERIALIZED_NAME_EVERY_N_PERIODS = "everyNPeriods";
  @SerializedName(SERIALIZED_NAME_EVERY_N_PERIODS)
  private Integer everyNPeriods;

  public static final String SERIALIZED_NAME_FORMATTED = "formatted";
  @SerializedName(SERIALIZED_NAME_FORMATTED)
  private String formatted;

  public static final String SERIALIZED_NAME_FORMATTED_ABBRV = "formattedAbbrv";
  @SerializedName(SERIALIZED_NAME_FORMATTED_ABBRV)
  private String formattedAbbrv;

  /**
   * Gets or Sets value
   */
  @JsonAdapter(ValueEnum.Adapter.class)
  public enum ValueEnum {
    ANNUAL("Annual"),
    
    SEMI_ANNUAL("SemiAnnual"),
    
    QUARTERLY("Quarterly"),
    
    BIMONTHLY("Bimonthly"),
    
    MONTHLY("Monthly"),
    
    TWICE_MONTHLY("TwiceMonthly"),
    
    BI_WEEKLY("BiWeekly"),
    
    WEEKLY("Weekly"),
    
    DAILY("Daily"),
    
    CONTINUOUSLY("Continuously"),
    
    ONETIME("Onetime"),
    
    EVERY_X_YEARS("EveryXYears");

    private String value;

    ValueEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ValueEnum fromValue(String value) {
      for (ValueEnum b : ValueEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ValueEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ValueEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ValueEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ValueEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ValueEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private ValueEnum value;

  public IFormattedFrequency() {
  }

  public IFormattedFrequency(
     Integer everyNPeriods, 
     String formatted, 
     String formattedAbbrv, 
     ValueEnum value
  ) {
    this();
    this.everyNPeriods = everyNPeriods;
    this.formatted = formatted;
    this.formattedAbbrv = formattedAbbrv;
    this.value = value;
  }

  /**
   * Get everyNPeriods
   * @return everyNPeriods
   */
  @javax.annotation.Nullable
  public Integer getEveryNPeriods() {
    return everyNPeriods;
  }



  /**
   * Get formatted
   * @return formatted
   */
  @javax.annotation.Nullable
  public String getFormatted() {
    return formatted;
  }



  /**
   * Get formattedAbbrv
   * @return formattedAbbrv
   */
  @javax.annotation.Nullable
  public String getFormattedAbbrv() {
    return formattedAbbrv;
  }



  /**
   * Get value
   * @return value
   */
  @javax.annotation.Nullable
  public ValueEnum getValue() {
    return value;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IFormattedFrequency iformattedFrequency = (IFormattedFrequency) o;
    return Objects.equals(this.everyNPeriods, iformattedFrequency.everyNPeriods) &&
        Objects.equals(this.formatted, iformattedFrequency.formatted) &&
        Objects.equals(this.formattedAbbrv, iformattedFrequency.formattedAbbrv) &&
        Objects.equals(this.value, iformattedFrequency.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(everyNPeriods, formatted, formattedAbbrv, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IFormattedFrequency {\n");
    sb.append("    everyNPeriods: ").append(toIndentedString(everyNPeriods)).append("\n");
    sb.append("    formatted: ").append(toIndentedString(formatted)).append("\n");
    sb.append("    formattedAbbrv: ").append(toIndentedString(formattedAbbrv)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("everyNPeriods");
    openapiFields.add("formatted");
    openapiFields.add("formattedAbbrv");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IFormattedFrequency
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IFormattedFrequency.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IFormattedFrequency is not found in the empty JSON string", IFormattedFrequency.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IFormattedFrequency.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IFormattedFrequency` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("formatted") != null && !jsonObj.get("formatted").isJsonNull()) && !jsonObj.get("formatted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formatted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formatted").toString()));
      }
      if ((jsonObj.get("formattedAbbrv") != null && !jsonObj.get("formattedAbbrv").isJsonNull()) && !jsonObj.get("formattedAbbrv").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formattedAbbrv` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formattedAbbrv").toString()));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
      // validate the optional field `value`
      if (jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) {
        ValueEnum.validateJsonElement(jsonObj.get("value"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IFormattedFrequency.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IFormattedFrequency' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IFormattedFrequency> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IFormattedFrequency.class));

       return (TypeAdapter<T>) new TypeAdapter<IFormattedFrequency>() {
           @Override
           public void write(JsonWriter out, IFormattedFrequency value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IFormattedFrequency read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IFormattedFrequency given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IFormattedFrequency
   * @throws IOException if the JSON string is invalid with respect to IFormattedFrequency
   */
  public static IFormattedFrequency fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IFormattedFrequency.class);
  }

  /**
   * Convert an instance of IFormattedFrequency to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

