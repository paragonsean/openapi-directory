/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
 * Statistics for a translation set
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GlobalResourcesSharedModelsTranslationSetStatistics {
  public static final String SERIALIZED_NAME_LANGUAGE_I_DS = "LanguageIDs";
  @SerializedName(SERIALIZED_NAME_LANGUAGE_I_DS)
  private List<Integer> languageIDs = new ArrayList<>();

  public static final String SERIALIZED_NAME_STRING_COUNT = "StringCount";
  @SerializedName(SERIALIZED_NAME_STRING_COUNT)
  private Integer stringCount;

  public GlobalResourcesSharedModelsTranslationSetStatistics() {
  }

  public GlobalResourcesSharedModelsTranslationSetStatistics languageIDs(List<Integer> languageIDs) {
    this.languageIDs = languageIDs;
    return this;
  }

  public GlobalResourcesSharedModelsTranslationSetStatistics addLanguageIDsItem(Integer languageIDsItem) {
    if (this.languageIDs == null) {
      this.languageIDs = new ArrayList<>();
    }
    this.languageIDs.add(languageIDsItem);
    return this;
  }

  /**
   * The IDs of languages for which translaions in this translation set have been requested
   * @return languageIDs
   */
  @javax.annotation.Nullable
  public List<Integer> getLanguageIDs() {
    return languageIDs;
  }

  public void setLanguageIDs(List<Integer> languageIDs) {
    this.languageIDs = languageIDs;
  }


  public GlobalResourcesSharedModelsTranslationSetStatistics stringCount(Integer stringCount) {
    this.stringCount = stringCount;
    return this;
  }

  /**
   * The count of unique string definitions contained in this translation set
   * @return stringCount
   */
  @javax.annotation.Nullable
  public Integer getStringCount() {
    return stringCount;
  }

  public void setStringCount(Integer stringCount) {
    this.stringCount = stringCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GlobalResourcesSharedModelsTranslationSetStatistics globalResourcesSharedModelsTranslationSetStatistics = (GlobalResourcesSharedModelsTranslationSetStatistics) o;
    return Objects.equals(this.languageIDs, globalResourcesSharedModelsTranslationSetStatistics.languageIDs) &&
        Objects.equals(this.stringCount, globalResourcesSharedModelsTranslationSetStatistics.stringCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(languageIDs, stringCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GlobalResourcesSharedModelsTranslationSetStatistics {\n");
    sb.append("    languageIDs: ").append(toIndentedString(languageIDs)).append("\n");
    sb.append("    stringCount: ").append(toIndentedString(stringCount)).append("\n");
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
    openapiFields.add("LanguageIDs");
    openapiFields.add("StringCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GlobalResourcesSharedModelsTranslationSetStatistics
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GlobalResourcesSharedModelsTranslationSetStatistics.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GlobalResourcesSharedModelsTranslationSetStatistics is not found in the empty JSON string", GlobalResourcesSharedModelsTranslationSetStatistics.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GlobalResourcesSharedModelsTranslationSetStatistics.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GlobalResourcesSharedModelsTranslationSetStatistics` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("LanguageIDs") != null && !jsonObj.get("LanguageIDs").isJsonNull() && !jsonObj.get("LanguageIDs").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `LanguageIDs` to be an array in the JSON string but got `%s`", jsonObj.get("LanguageIDs").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GlobalResourcesSharedModelsTranslationSetStatistics.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GlobalResourcesSharedModelsTranslationSetStatistics' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GlobalResourcesSharedModelsTranslationSetStatistics> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GlobalResourcesSharedModelsTranslationSetStatistics.class));

       return (TypeAdapter<T>) new TypeAdapter<GlobalResourcesSharedModelsTranslationSetStatistics>() {
           @Override
           public void write(JsonWriter out, GlobalResourcesSharedModelsTranslationSetStatistics value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GlobalResourcesSharedModelsTranslationSetStatistics read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GlobalResourcesSharedModelsTranslationSetStatistics given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GlobalResourcesSharedModelsTranslationSetStatistics
   * @throws IOException if the JSON string is invalid with respect to GlobalResourcesSharedModelsTranslationSetStatistics
   */
  public static GlobalResourcesSharedModelsTranslationSetStatistics fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GlobalResourcesSharedModelsTranslationSetStatistics.class);
  }

  /**
   * Convert an instance of GlobalResourcesSharedModelsTranslationSetStatistics to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

