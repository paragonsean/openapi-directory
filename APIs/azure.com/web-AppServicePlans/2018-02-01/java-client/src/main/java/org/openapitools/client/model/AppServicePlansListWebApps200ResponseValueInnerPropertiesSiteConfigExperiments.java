/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
import org.openapitools.client.model.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner;

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
 * Routing rules in production experiments.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:50.309367-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments {
  public static final String SERIALIZED_NAME_RAMP_UP_RULES = "rampUpRules";
  @SerializedName(SERIALIZED_NAME_RAMP_UP_RULES)
  private List<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner> rampUpRules = new ArrayList<>();

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments() {
  }

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments rampUpRules(List<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner> rampUpRules) {
    this.rampUpRules = rampUpRules;
    return this;
  }

  public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments addRampUpRulesItem(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner rampUpRulesItem) {
    if (this.rampUpRules == null) {
      this.rampUpRules = new ArrayList<>();
    }
    this.rampUpRules.add(rampUpRulesItem);
    return this;
  }

  /**
   * List of ramp-up rules.
   * @return rampUpRules
   */
  @javax.annotation.Nullable
  public List<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner> getRampUpRules() {
    return rampUpRules;
  }

  public void setRampUpRules(List<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner> rampUpRules) {
    this.rampUpRules = rampUpRules;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments = (AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments) o;
    return Objects.equals(this.rampUpRules, appServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.rampUpRules);
  }

  @Override
  public int hashCode() {
    return Objects.hash(rampUpRules);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments {\n");
    sb.append("    rampUpRules: ").append(toIndentedString(rampUpRules)).append("\n");
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
    openapiFields.add("rampUpRules");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments is not found in the empty JSON string", AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("rampUpRules") != null && !jsonObj.get("rampUpRules").isJsonNull()) {
        JsonArray jsonArrayrampUpRules = jsonObj.getAsJsonArray("rampUpRules");
        if (jsonArrayrampUpRules != null) {
          // ensure the json data is an array
          if (!jsonObj.get("rampUpRules").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `rampUpRules` to be an array in the JSON string but got `%s`", jsonObj.get("rampUpRules").toString()));
          }

          // validate the optional field `rampUpRules` (array)
          for (int i = 0; i < jsonArrayrampUpRules.size(); i++) {
            AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner.validateJsonElement(jsonArrayrampUpRules.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments>() {
           @Override
           public void write(JsonWriter out, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments
   */
  public static AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments.class);
  }

  /**
   * Convert an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

