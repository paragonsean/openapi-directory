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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AbsencePeriodsResponseAllOfDataAttributes;

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
 * AbsencePeriodsResponseAllOfData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:33.166267-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AbsencePeriodsResponseAllOfData {
  public static final String SERIALIZED_NAME_ATTRIBUTES = "attributes";
  @SerializedName(SERIALIZED_NAME_ATTRIBUTES)
  private List<AbsencePeriodsResponseAllOfDataAttributes> attributes = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public AbsencePeriodsResponseAllOfData() {
  }

  public AbsencePeriodsResponseAllOfData attributes(List<AbsencePeriodsResponseAllOfDataAttributes> attributes) {
    this.attributes = attributes;
    return this;
  }

  public AbsencePeriodsResponseAllOfData addAttributesItem(AbsencePeriodsResponseAllOfDataAttributes attributesItem) {
    if (this.attributes == null) {
      this.attributes = new ArrayList<>();
    }
    this.attributes.add(attributesItem);
    return this;
  }

  /**
   * Get attributes
   * @return attributes
   */
  @javax.annotation.Nonnull
  public List<AbsencePeriodsResponseAllOfDataAttributes> getAttributes() {
    return attributes;
  }

  public void setAttributes(List<AbsencePeriodsResponseAllOfDataAttributes> attributes) {
    this.attributes = attributes;
  }


  public AbsencePeriodsResponseAllOfData type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AbsencePeriodsResponseAllOfData absencePeriodsResponseAllOfData = (AbsencePeriodsResponseAllOfData) o;
    return Objects.equals(this.attributes, absencePeriodsResponseAllOfData.attributes) &&
        Objects.equals(this.type, absencePeriodsResponseAllOfData.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(attributes, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AbsencePeriodsResponseAllOfData {\n");
    sb.append("    attributes: ").append(toIndentedString(attributes)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("attributes");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("attributes");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AbsencePeriodsResponseAllOfData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AbsencePeriodsResponseAllOfData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AbsencePeriodsResponseAllOfData is not found in the empty JSON string", AbsencePeriodsResponseAllOfData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AbsencePeriodsResponseAllOfData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AbsencePeriodsResponseAllOfData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AbsencePeriodsResponseAllOfData.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("attributes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `attributes` to be an array in the JSON string but got `%s`", jsonObj.get("attributes").toString()));
      }

      JsonArray jsonArrayattributes = jsonObj.getAsJsonArray("attributes");
      // validate the required field `attributes` (array)
      for (int i = 0; i < jsonArrayattributes.size(); i++) {
        AbsencePeriodsResponseAllOfDataAttributes.validateJsonElement(jsonArrayattributes.get(i));
      };
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AbsencePeriodsResponseAllOfData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AbsencePeriodsResponseAllOfData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AbsencePeriodsResponseAllOfData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AbsencePeriodsResponseAllOfData.class));

       return (TypeAdapter<T>) new TypeAdapter<AbsencePeriodsResponseAllOfData>() {
           @Override
           public void write(JsonWriter out, AbsencePeriodsResponseAllOfData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AbsencePeriodsResponseAllOfData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AbsencePeriodsResponseAllOfData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AbsencePeriodsResponseAllOfData
   * @throws IOException if the JSON string is invalid with respect to AbsencePeriodsResponseAllOfData
   */
  public static AbsencePeriodsResponseAllOfData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AbsencePeriodsResponseAllOfData.class);
  }

  /**
   * Convert an instance of AbsencePeriodsResponseAllOfData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

