/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import org.openapitools.client.model.BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner;

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
 * BuildsListToolsetProjects200ResponseUwp
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BuildsListToolsetProjects200ResponseUwp {
  public static final String SERIALIZED_NAME_UWP_SOLUTIONS = "uwpSolutions";
  @SerializedName(SERIALIZED_NAME_UWP_SOLUTIONS)
  private List<BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner> uwpSolutions = new ArrayList<>();

  public BuildsListToolsetProjects200ResponseUwp() {
  }

  public BuildsListToolsetProjects200ResponseUwp uwpSolutions(List<BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner> uwpSolutions) {
    this.uwpSolutions = uwpSolutions;
    return this;
  }

  public BuildsListToolsetProjects200ResponseUwp addUwpSolutionsItem(BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner uwpSolutionsItem) {
    if (this.uwpSolutions == null) {
      this.uwpSolutions = new ArrayList<>();
    }
    this.uwpSolutions.add(uwpSolutionsItem);
    return this;
  }

  /**
   * The UWP solutions detected
   * @return uwpSolutions
   */
  @javax.annotation.Nonnull
  public List<BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner> getUwpSolutions() {
    return uwpSolutions;
  }

  public void setUwpSolutions(List<BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner> uwpSolutions) {
    this.uwpSolutions = uwpSolutions;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BuildsListToolsetProjects200ResponseUwp buildsListToolsetProjects200ResponseUwp = (BuildsListToolsetProjects200ResponseUwp) o;
    return Objects.equals(this.uwpSolutions, buildsListToolsetProjects200ResponseUwp.uwpSolutions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(uwpSolutions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BuildsListToolsetProjects200ResponseUwp {\n");
    sb.append("    uwpSolutions: ").append(toIndentedString(uwpSolutions)).append("\n");
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
    openapiFields.add("uwpSolutions");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("uwpSolutions");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BuildsListToolsetProjects200ResponseUwp
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BuildsListToolsetProjects200ResponseUwp.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BuildsListToolsetProjects200ResponseUwp is not found in the empty JSON string", BuildsListToolsetProjects200ResponseUwp.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BuildsListToolsetProjects200ResponseUwp.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BuildsListToolsetProjects200ResponseUwp` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BuildsListToolsetProjects200ResponseUwp.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("uwpSolutions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `uwpSolutions` to be an array in the JSON string but got `%s`", jsonObj.get("uwpSolutions").toString()));
      }

      JsonArray jsonArrayuwpSolutions = jsonObj.getAsJsonArray("uwpSolutions");
      // validate the required field `uwpSolutions` (array)
      for (int i = 0; i < jsonArrayuwpSolutions.size(); i++) {
        BuildsListToolsetProjects200ResponseUwpUwpSolutionsInner.validateJsonElement(jsonArrayuwpSolutions.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BuildsListToolsetProjects200ResponseUwp.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BuildsListToolsetProjects200ResponseUwp' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BuildsListToolsetProjects200ResponseUwp> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BuildsListToolsetProjects200ResponseUwp.class));

       return (TypeAdapter<T>) new TypeAdapter<BuildsListToolsetProjects200ResponseUwp>() {
           @Override
           public void write(JsonWriter out, BuildsListToolsetProjects200ResponseUwp value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BuildsListToolsetProjects200ResponseUwp read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BuildsListToolsetProjects200ResponseUwp given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BuildsListToolsetProjects200ResponseUwp
   * @throws IOException if the JSON string is invalid with respect to BuildsListToolsetProjects200ResponseUwp
   */
  public static BuildsListToolsetProjects200ResponseUwp fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BuildsListToolsetProjects200ResponseUwp.class);
  }

  /**
   * Convert an instance of BuildsListToolsetProjects200ResponseUwp to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

