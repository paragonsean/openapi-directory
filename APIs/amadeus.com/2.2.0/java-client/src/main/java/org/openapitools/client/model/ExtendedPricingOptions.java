/*
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
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
 * fare filter options
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:36.621787-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExtendedPricingOptions {
  public static final String SERIALIZED_NAME_INCLUDED_CHECKED_BAGS_ONLY = "includedCheckedBagsOnly";
  @SerializedName(SERIALIZED_NAME_INCLUDED_CHECKED_BAGS_ONLY)
  private Boolean includedCheckedBagsOnly;

  public ExtendedPricingOptions() {
  }

  public ExtendedPricingOptions includedCheckedBagsOnly(Boolean includedCheckedBagsOnly) {
    this.includedCheckedBagsOnly = includedCheckedBagsOnly;
    return this;
  }

  /**
   * If true, returns the flight-offers with included checked bags only
   * @return includedCheckedBagsOnly
   */
  @javax.annotation.Nullable
  public Boolean getIncludedCheckedBagsOnly() {
    return includedCheckedBagsOnly;
  }

  public void setIncludedCheckedBagsOnly(Boolean includedCheckedBagsOnly) {
    this.includedCheckedBagsOnly = includedCheckedBagsOnly;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExtendedPricingOptions extendedPricingOptions = (ExtendedPricingOptions) o;
    return Objects.equals(this.includedCheckedBagsOnly, extendedPricingOptions.includedCheckedBagsOnly);
  }

  @Override
  public int hashCode() {
    return Objects.hash(includedCheckedBagsOnly);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExtendedPricingOptions {\n");
    sb.append("    includedCheckedBagsOnly: ").append(toIndentedString(includedCheckedBagsOnly)).append("\n");
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
    openapiFields.add("includedCheckedBagsOnly");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExtendedPricingOptions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExtendedPricingOptions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExtendedPricingOptions is not found in the empty JSON string", ExtendedPricingOptions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExtendedPricingOptions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExtendedPricingOptions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExtendedPricingOptions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExtendedPricingOptions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExtendedPricingOptions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExtendedPricingOptions.class));

       return (TypeAdapter<T>) new TypeAdapter<ExtendedPricingOptions>() {
           @Override
           public void write(JsonWriter out, ExtendedPricingOptions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExtendedPricingOptions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExtendedPricingOptions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExtendedPricingOptions
   * @throws IOException if the JSON string is invalid with respect to ExtendedPricingOptions
   */
  public static ExtendedPricingOptions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExtendedPricingOptions.class);
  }

  /**
   * Convert an instance of ExtendedPricingOptions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

