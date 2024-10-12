/*
 * Flight Cheapest Date Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Dictionaries;
import org.openapitools.client.model.FlightDate;
import org.openapitools.client.model.Issue;
import org.openapitools.client.model.Meta;

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
 * FlightDates
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:20.773098-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FlightDates {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private List<FlightDate> data = new ArrayList<>();

  public static final String SERIALIZED_NAME_DICTIONARIES = "dictionaries";
  @SerializedName(SERIALIZED_NAME_DICTIONARIES)
  private Dictionaries dictionaries;

  public static final String SERIALIZED_NAME_META = "meta";
  @SerializedName(SERIALIZED_NAME_META)
  private Meta meta;

  public static final String SERIALIZED_NAME_WARNINGS = "warnings";
  @SerializedName(SERIALIZED_NAME_WARNINGS)
  private List<Issue> warnings = new ArrayList<>();

  public FlightDates() {
  }

  public FlightDates data(List<FlightDate> data) {
    this.data = data;
    return this;
  }

  public FlightDates addDataItem(FlightDate dataItem) {
    if (this.data == null) {
      this.data = new ArrayList<>();
    }
    this.data.add(dataItem);
    return this;
  }

  /**
   * Get data
   * @return data
   */
  @javax.annotation.Nullable
  public List<FlightDate> getData() {
    return data;
  }

  public void setData(List<FlightDate> data) {
    this.data = data;
  }


  public FlightDates dictionaries(Dictionaries dictionaries) {
    this.dictionaries = dictionaries;
    return this;
  }

  /**
   * Get dictionaries
   * @return dictionaries
   */
  @javax.annotation.Nullable
  public Dictionaries getDictionaries() {
    return dictionaries;
  }

  public void setDictionaries(Dictionaries dictionaries) {
    this.dictionaries = dictionaries;
  }


  public FlightDates meta(Meta meta) {
    this.meta = meta;
    return this;
  }

  /**
   * Get meta
   * @return meta
   */
  @javax.annotation.Nullable
  public Meta getMeta() {
    return meta;
  }

  public void setMeta(Meta meta) {
    this.meta = meta;
  }


  public FlightDates warnings(List<Issue> warnings) {
    this.warnings = warnings;
    return this;
  }

  public FlightDates addWarningsItem(Issue warningsItem) {
    if (this.warnings == null) {
      this.warnings = new ArrayList<>();
    }
    this.warnings.add(warningsItem);
    return this;
  }

  /**
   * Get warnings
   * @return warnings
   */
  @javax.annotation.Nullable
  public List<Issue> getWarnings() {
    return warnings;
  }

  public void setWarnings(List<Issue> warnings) {
    this.warnings = warnings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlightDates flightDates = (FlightDates) o;
    return Objects.equals(this.data, flightDates.data) &&
        Objects.equals(this.dictionaries, flightDates.dictionaries) &&
        Objects.equals(this.meta, flightDates.meta) &&
        Objects.equals(this.warnings, flightDates.warnings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, dictionaries, meta, warnings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlightDates {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    dictionaries: ").append(toIndentedString(dictionaries)).append("\n");
    sb.append("    meta: ").append(toIndentedString(meta)).append("\n");
    sb.append("    warnings: ").append(toIndentedString(warnings)).append("\n");
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
    openapiFields.add("data");
    openapiFields.add("dictionaries");
    openapiFields.add("meta");
    openapiFields.add("warnings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FlightDates
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FlightDates.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FlightDates is not found in the empty JSON string", FlightDates.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FlightDates.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FlightDates` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("data") != null && !jsonObj.get("data").isJsonNull()) {
        JsonArray jsonArraydata = jsonObj.getAsJsonArray("data");
        if (jsonArraydata != null) {
          // ensure the json data is an array
          if (!jsonObj.get("data").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `data` to be an array in the JSON string but got `%s`", jsonObj.get("data").toString()));
          }

          // validate the optional field `data` (array)
          for (int i = 0; i < jsonArraydata.size(); i++) {
            FlightDate.validateJsonElement(jsonArraydata.get(i));
          };
        }
      }
      // validate the optional field `dictionaries`
      if (jsonObj.get("dictionaries") != null && !jsonObj.get("dictionaries").isJsonNull()) {
        Dictionaries.validateJsonElement(jsonObj.get("dictionaries"));
      }
      // validate the optional field `meta`
      if (jsonObj.get("meta") != null && !jsonObj.get("meta").isJsonNull()) {
        Meta.validateJsonElement(jsonObj.get("meta"));
      }
      if (jsonObj.get("warnings") != null && !jsonObj.get("warnings").isJsonNull()) {
        JsonArray jsonArraywarnings = jsonObj.getAsJsonArray("warnings");
        if (jsonArraywarnings != null) {
          // ensure the json data is an array
          if (!jsonObj.get("warnings").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `warnings` to be an array in the JSON string but got `%s`", jsonObj.get("warnings").toString()));
          }

          // validate the optional field `warnings` (array)
          for (int i = 0; i < jsonArraywarnings.size(); i++) {
            Issue.validateJsonElement(jsonArraywarnings.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FlightDates.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FlightDates' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FlightDates> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FlightDates.class));

       return (TypeAdapter<T>) new TypeAdapter<FlightDates>() {
           @Override
           public void write(JsonWriter out, FlightDates value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FlightDates read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FlightDates given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FlightDates
   * @throws IOException if the JSON string is invalid with respect to FlightDates
   */
  public static FlightDates fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FlightDates.class);
  }

  /**
   * Convert an instance of FlightDates to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

