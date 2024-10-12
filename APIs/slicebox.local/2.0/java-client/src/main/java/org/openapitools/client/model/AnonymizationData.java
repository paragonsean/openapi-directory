/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
import org.openapitools.client.model.AnonymizationProfile;
import org.openapitools.client.model.TagValue;

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
 * AnonymizationData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:37.231084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AnonymizationData {
  public static final String SERIALIZED_NAME_PROFILE = "profile";
  @SerializedName(SERIALIZED_NAME_PROFILE)
  private AnonymizationProfile profile;

  public static final String SERIALIZED_NAME_TAG_VALUES = "tagValues";
  @SerializedName(SERIALIZED_NAME_TAG_VALUES)
  private List<TagValue> tagValues = new ArrayList<>();

  public AnonymizationData() {
  }

  public AnonymizationData profile(AnonymizationProfile profile) {
    this.profile = profile;
    return this;
  }

  /**
   * Get profile
   * @return profile
   */
  @javax.annotation.Nullable
  public AnonymizationProfile getProfile() {
    return profile;
  }

  public void setProfile(AnonymizationProfile profile) {
    this.profile = profile;
  }


  public AnonymizationData tagValues(List<TagValue> tagValues) {
    this.tagValues = tagValues;
    return this;
  }

  public AnonymizationData addTagValuesItem(TagValue tagValuesItem) {
    if (this.tagValues == null) {
      this.tagValues = new ArrayList<>();
    }
    this.tagValues.add(tagValuesItem);
    return this;
  }

  /**
   * Get tagValues
   * @return tagValues
   */
  @javax.annotation.Nullable
  public List<TagValue> getTagValues() {
    return tagValues;
  }

  public void setTagValues(List<TagValue> tagValues) {
    this.tagValues = tagValues;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnonymizationData anonymizationData = (AnonymizationData) o;
    return Objects.equals(this.profile, anonymizationData.profile) &&
        Objects.equals(this.tagValues, anonymizationData.tagValues);
  }

  @Override
  public int hashCode() {
    return Objects.hash(profile, tagValues);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnonymizationData {\n");
    sb.append("    profile: ").append(toIndentedString(profile)).append("\n");
    sb.append("    tagValues: ").append(toIndentedString(tagValues)).append("\n");
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
    openapiFields.add("profile");
    openapiFields.add("tagValues");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AnonymizationData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AnonymizationData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AnonymizationData is not found in the empty JSON string", AnonymizationData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AnonymizationData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AnonymizationData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `profile`
      if (jsonObj.get("profile") != null && !jsonObj.get("profile").isJsonNull()) {
        AnonymizationProfile.validateJsonElement(jsonObj.get("profile"));
      }
      if (jsonObj.get("tagValues") != null && !jsonObj.get("tagValues").isJsonNull()) {
        JsonArray jsonArraytagValues = jsonObj.getAsJsonArray("tagValues");
        if (jsonArraytagValues != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tagValues").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tagValues` to be an array in the JSON string but got `%s`", jsonObj.get("tagValues").toString()));
          }

          // validate the optional field `tagValues` (array)
          for (int i = 0; i < jsonArraytagValues.size(); i++) {
            TagValue.validateJsonElement(jsonArraytagValues.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AnonymizationData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AnonymizationData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AnonymizationData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AnonymizationData.class));

       return (TypeAdapter<T>) new TypeAdapter<AnonymizationData>() {
           @Override
           public void write(JsonWriter out, AnonymizationData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AnonymizationData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AnonymizationData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AnonymizationData
   * @throws IOException if the JSON string is invalid with respect to AnonymizationData
   */
  public static AnonymizationData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AnonymizationData.class);
  }

  /**
   * Convert an instance of AnonymizationData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

