/*
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
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
import org.openapitools.client.model.EnvironmentSizeFragment;

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
 * Represents the size configuration under the lab account
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:25.069739-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SizeConfigurationPropertiesFragment {
  public static final String SERIALIZED_NAME_ENVIRONMENT_SIZES = "environmentSizes";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_SIZES)
  private List<EnvironmentSizeFragment> environmentSizes = new ArrayList<>();

  public SizeConfigurationPropertiesFragment() {
  }

  public SizeConfigurationPropertiesFragment environmentSizes(List<EnvironmentSizeFragment> environmentSizes) {
    this.environmentSizes = environmentSizes;
    return this;
  }

  public SizeConfigurationPropertiesFragment addEnvironmentSizesItem(EnvironmentSizeFragment environmentSizesItem) {
    if (this.environmentSizes == null) {
      this.environmentSizes = new ArrayList<>();
    }
    this.environmentSizes.add(environmentSizesItem);
    return this;
  }

  /**
   * Represents a list of size categories supported by this Lab Account (Small, Medium, Large)
   * @return environmentSizes
   */
  @javax.annotation.Nullable
  public List<EnvironmentSizeFragment> getEnvironmentSizes() {
    return environmentSizes;
  }

  public void setEnvironmentSizes(List<EnvironmentSizeFragment> environmentSizes) {
    this.environmentSizes = environmentSizes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SizeConfigurationPropertiesFragment sizeConfigurationPropertiesFragment = (SizeConfigurationPropertiesFragment) o;
    return Objects.equals(this.environmentSizes, sizeConfigurationPropertiesFragment.environmentSizes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(environmentSizes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SizeConfigurationPropertiesFragment {\n");
    sb.append("    environmentSizes: ").append(toIndentedString(environmentSizes)).append("\n");
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
    openapiFields.add("environmentSizes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SizeConfigurationPropertiesFragment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SizeConfigurationPropertiesFragment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SizeConfigurationPropertiesFragment is not found in the empty JSON string", SizeConfigurationPropertiesFragment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SizeConfigurationPropertiesFragment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SizeConfigurationPropertiesFragment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("environmentSizes") != null && !jsonObj.get("environmentSizes").isJsonNull()) {
        JsonArray jsonArrayenvironmentSizes = jsonObj.getAsJsonArray("environmentSizes");
        if (jsonArrayenvironmentSizes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("environmentSizes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `environmentSizes` to be an array in the JSON string but got `%s`", jsonObj.get("environmentSizes").toString()));
          }

          // validate the optional field `environmentSizes` (array)
          for (int i = 0; i < jsonArrayenvironmentSizes.size(); i++) {
            EnvironmentSizeFragment.validateJsonElement(jsonArrayenvironmentSizes.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SizeConfigurationPropertiesFragment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SizeConfigurationPropertiesFragment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SizeConfigurationPropertiesFragment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SizeConfigurationPropertiesFragment.class));

       return (TypeAdapter<T>) new TypeAdapter<SizeConfigurationPropertiesFragment>() {
           @Override
           public void write(JsonWriter out, SizeConfigurationPropertiesFragment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SizeConfigurationPropertiesFragment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SizeConfigurationPropertiesFragment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SizeConfigurationPropertiesFragment
   * @throws IOException if the JSON string is invalid with respect to SizeConfigurationPropertiesFragment
   */
  public static SizeConfigurationPropertiesFragment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SizeConfigurationPropertiesFragment.class);
  }

  /**
   * Convert an instance of SizeConfigurationPropertiesFragment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

