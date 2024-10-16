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
import org.openapitools.client.model.AnalyticsLanguageCounts200ResponseLanguagesInner;

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
 * Languages
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Languages {
  public static final String SERIALIZED_NAME_LANGUAGES = "languages";
  @SerializedName(SERIALIZED_NAME_LANGUAGES)
  private List<AnalyticsLanguageCounts200ResponseLanguagesInner> languages = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Long total;

  public Languages() {
  }

  public Languages languages(List<AnalyticsLanguageCounts200ResponseLanguagesInner> languages) {
    this.languages = languages;
    return this;
  }

  public Languages addLanguagesItem(AnalyticsLanguageCounts200ResponseLanguagesInner languagesItem) {
    if (this.languages == null) {
      this.languages = new ArrayList<>();
    }
    this.languages.add(languagesItem);
    return this;
  }

  /**
   * Get languages
   * @return languages
   */
  @javax.annotation.Nullable
  public List<AnalyticsLanguageCounts200ResponseLanguagesInner> getLanguages() {
    return languages;
  }

  public void setLanguages(List<AnalyticsLanguageCounts200ResponseLanguagesInner> languages) {
    this.languages = languages;
  }


  public Languages total(Long total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public Long getTotal() {
    return total;
  }

  public void setTotal(Long total) {
    this.total = total;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Languages languages = (Languages) o;
    return Objects.equals(this.languages, languages.languages) &&
        Objects.equals(this.total, languages.total);
  }

  @Override
  public int hashCode() {
    return Objects.hash(languages, total);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Languages {\n");
    sb.append("    languages: ").append(toIndentedString(languages)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("languages");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Languages
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Languages.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Languages is not found in the empty JSON string", Languages.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Languages.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Languages` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("languages") != null && !jsonObj.get("languages").isJsonNull()) {
        JsonArray jsonArraylanguages = jsonObj.getAsJsonArray("languages");
        if (jsonArraylanguages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("languages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `languages` to be an array in the JSON string but got `%s`", jsonObj.get("languages").toString()));
          }

          // validate the optional field `languages` (array)
          for (int i = 0; i < jsonArraylanguages.size(); i++) {
            AnalyticsLanguageCounts200ResponseLanguagesInner.validateJsonElement(jsonArraylanguages.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Languages.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Languages' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Languages> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Languages.class));

       return (TypeAdapter<T>) new TypeAdapter<Languages>() {
           @Override
           public void write(JsonWriter out, Languages value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Languages read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Languages given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Languages
   * @throws IOException if the JSON string is invalid with respect to Languages
   */
  public static Languages fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Languages.class);
  }

  /**
   * Convert an instance of Languages to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

