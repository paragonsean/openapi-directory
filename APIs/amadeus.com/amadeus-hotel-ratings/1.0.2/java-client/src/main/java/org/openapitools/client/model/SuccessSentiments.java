/*
 * Hotel Ratings
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, this API in test only offers 24 hotels; 10 in London and 14 in New-York. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.2
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
import org.openapitools.client.model.CollectionMeta;
import org.openapitools.client.model.HotelSentiment;
import org.openapitools.client.model.WarningNotFound;

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
 * SuccessSentiments
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:38.818955-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SuccessSentiments {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private List<HotelSentiment> data = new ArrayList<>();

  public static final String SERIALIZED_NAME_META = "meta";
  @SerializedName(SERIALIZED_NAME_META)
  private CollectionMeta meta;

  public static final String SERIALIZED_NAME_WARNINGS = "warnings";
  @SerializedName(SERIALIZED_NAME_WARNINGS)
  private List<WarningNotFound> warnings = new ArrayList<>();

  public SuccessSentiments() {
  }

  public SuccessSentiments data(List<HotelSentiment> data) {
    this.data = data;
    return this;
  }

  public SuccessSentiments addDataItem(HotelSentiment dataItem) {
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
  @javax.annotation.Nonnull
  public List<HotelSentiment> getData() {
    return data;
  }

  public void setData(List<HotelSentiment> data) {
    this.data = data;
  }


  public SuccessSentiments meta(CollectionMeta meta) {
    this.meta = meta;
    return this;
  }

  /**
   * Get meta
   * @return meta
   */
  @javax.annotation.Nullable
  public CollectionMeta getMeta() {
    return meta;
  }

  public void setMeta(CollectionMeta meta) {
    this.meta = meta;
  }


  public SuccessSentiments warnings(List<WarningNotFound> warnings) {
    this.warnings = warnings;
    return this;
  }

  public SuccessSentiments addWarningsItem(WarningNotFound warningsItem) {
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
  public List<WarningNotFound> getWarnings() {
    return warnings;
  }

  public void setWarnings(List<WarningNotFound> warnings) {
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
    SuccessSentiments successSentiments = (SuccessSentiments) o;
    return Objects.equals(this.data, successSentiments.data) &&
        Objects.equals(this.meta, successSentiments.meta) &&
        Objects.equals(this.warnings, successSentiments.warnings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, meta, warnings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SuccessSentiments {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
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
    openapiFields.add("meta");
    openapiFields.add("warnings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("data");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SuccessSentiments
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SuccessSentiments.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SuccessSentiments is not found in the empty JSON string", SuccessSentiments.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SuccessSentiments.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SuccessSentiments` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SuccessSentiments.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("data").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `data` to be an array in the JSON string but got `%s`", jsonObj.get("data").toString()));
      }

      JsonArray jsonArraydata = jsonObj.getAsJsonArray("data");
      // validate the required field `data` (array)
      for (int i = 0; i < jsonArraydata.size(); i++) {
        HotelSentiment.validateJsonElement(jsonArraydata.get(i));
      };
      // validate the optional field `meta`
      if (jsonObj.get("meta") != null && !jsonObj.get("meta").isJsonNull()) {
        CollectionMeta.validateJsonElement(jsonObj.get("meta"));
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
            WarningNotFound.validateJsonElement(jsonArraywarnings.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SuccessSentiments.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SuccessSentiments' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SuccessSentiments> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SuccessSentiments.class));

       return (TypeAdapter<T>) new TypeAdapter<SuccessSentiments>() {
           @Override
           public void write(JsonWriter out, SuccessSentiments value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SuccessSentiments read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SuccessSentiments given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SuccessSentiments
   * @throws IOException if the JSON string is invalid with respect to SuccessSentiments
   */
  public static SuccessSentiments fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SuccessSentiments.class);
  }

  /**
   * Convert an instance of SuccessSentiments to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

