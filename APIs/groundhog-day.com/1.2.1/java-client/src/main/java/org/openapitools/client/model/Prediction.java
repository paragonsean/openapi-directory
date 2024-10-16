/*
 * Groundhog Day API
 * This API returns all of North America’s prognosticating animals and their yearly weather predictions.
 *
 * The version of the OpenAPI document: 1.2.1
 * Contact: hello@groundhog-day.com
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
import org.openapitools.client.model.Groundhog;

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
 * An annual prediction of an early spring or a longer winter.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:36.948560-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Prediction {
  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private String details;

  public static final String SERIALIZED_NAME_GROUNDHOG = "groundhog";
  @SerializedName(SERIALIZED_NAME_GROUNDHOG)
  private Groundhog groundhog;

  public static final String SERIALIZED_NAME_SHADOW = "shadow";
  @SerializedName(SERIALIZED_NAME_SHADOW)
  private Integer shadow;

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public Prediction() {
  }

  public Prediction details(String details) {
    this.details = details;
    return this;
  }

  /**
   * Get details
   * @return details
   */
  @javax.annotation.Nonnull
  public String getDetails() {
    return details;
  }

  public void setDetails(String details) {
    this.details = details;
  }


  public Prediction groundhog(Groundhog groundhog) {
    this.groundhog = groundhog;
    return this;
  }

  /**
   * Get groundhog
   * @return groundhog
   */
  @javax.annotation.Nullable
  public Groundhog getGroundhog() {
    return groundhog;
  }

  public void setGroundhog(Groundhog groundhog) {
    this.groundhog = groundhog;
  }


  public Prediction shadow(Integer shadow) {
    this.shadow = shadow;
    return this;
  }

  /**
   * Get shadow
   * minimum: 0
   * maximum: 1
   * @return shadow
   */
  @javax.annotation.Nullable
  public Integer getShadow() {
    return shadow;
  }

  public void setShadow(Integer shadow) {
    this.shadow = shadow;
  }


  public Prediction year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * Get year
   * minimum: 1886
   * @return year
   */
  @javax.annotation.Nonnull
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Prediction prediction = (Prediction) o;
    return Objects.equals(this.details, prediction.details) &&
        Objects.equals(this.groundhog, prediction.groundhog) &&
        Objects.equals(this.shadow, prediction.shadow) &&
        Objects.equals(this.year, prediction.year);
  }

  @Override
  public int hashCode() {
    return Objects.hash(details, groundhog, shadow, year);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Prediction {\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
    sb.append("    groundhog: ").append(toIndentedString(groundhog)).append("\n");
    sb.append("    shadow: ").append(toIndentedString(shadow)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("details");
    openapiFields.add("groundhog");
    openapiFields.add("shadow");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("details");
    openapiRequiredFields.add("shadow");
    openapiRequiredFields.add("year");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Prediction
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Prediction.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Prediction is not found in the empty JSON string", Prediction.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Prediction.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Prediction` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Prediction.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("details").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `details` to be a primitive type in the JSON string but got `%s`", jsonObj.get("details").toString()));
      }
      // validate the optional field `groundhog`
      if (jsonObj.get("groundhog") != null && !jsonObj.get("groundhog").isJsonNull()) {
        Groundhog.validateJsonElement(jsonObj.get("groundhog"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Prediction.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Prediction' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Prediction> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Prediction.class));

       return (TypeAdapter<T>) new TypeAdapter<Prediction>() {
           @Override
           public void write(JsonWriter out, Prediction value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Prediction read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Prediction given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Prediction
   * @throws IOException if the JSON string is invalid with respect to Prediction
   */
  public static Prediction fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Prediction.class);
  }

  /**
   * Convert an instance of Prediction to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

