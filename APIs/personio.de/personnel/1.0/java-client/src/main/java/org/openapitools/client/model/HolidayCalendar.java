/*
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
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
import java.math.BigDecimal;
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
 * HolidayCalendar
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:33.166267-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HolidayCalendar {
  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Object value;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public HolidayCalendar() {
  }

  public HolidayCalendar value(Object value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
   */
  @javax.annotation.Nullable
  public Object getValue() {
    return value;
  }

  public void setValue(Object value) {
    this.value = value;
  }


  public HolidayCalendar label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Get label
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HolidayCalendar holidayCalendar = (HolidayCalendar) o;
    return Objects.equals(this.value, holidayCalendar.value) &&
        Objects.equals(this.label, holidayCalendar.label);
  }

  @Override
  public int hashCode() {
    return Objects.hash(value, label);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HolidayCalendar {\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
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
    openapiFields.add("label");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("label");
    openapiRequiredFields.add("value");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HolidayCalendar
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HolidayCalendar.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HolidayCalendar is not found in the empty JSON string", HolidayCalendar.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HolidayCalendar.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HolidayCalendar` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HolidayCalendar.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `value`
      if (jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) {
        Object.validateJsonElement(jsonObj.get("value"));
      }
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HolidayCalendar.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HolidayCalendar' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HolidayCalendar> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HolidayCalendar.class));

       return (TypeAdapter<T>) new TypeAdapter<HolidayCalendar>() {
           @Override
           public void write(JsonWriter out, HolidayCalendar value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HolidayCalendar read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HolidayCalendar given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HolidayCalendar
   * @throws IOException if the JSON string is invalid with respect to HolidayCalendar
   */
  public static HolidayCalendar fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HolidayCalendar.class);
  }

  /**
   * Convert an instance of HolidayCalendar to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

