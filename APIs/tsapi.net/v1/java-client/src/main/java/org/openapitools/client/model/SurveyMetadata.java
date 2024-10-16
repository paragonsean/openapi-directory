/*
 * TSAPI
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
import org.openapitools.client.model.Hierarchy;
import org.openapitools.client.model.Language;
import org.openapitools.client.model.Variable;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * SurveyMetadata
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:41.455821-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SurveyMetadata {
  public static final String SERIALIZED_NAME_HIERARCHIES = "hierarchies";
  @SerializedName(SERIALIZED_NAME_HIERARCHIES)
  private List<Hierarchy> hierarchies;

  public static final String SERIALIZED_NAME_INTERVIEW_COUNT = "interviewCount";
  @SerializedName(SERIALIZED_NAME_INTERVIEW_COUNT)
  private Integer interviewCount;

  public static final String SERIALIZED_NAME_LANGUAGES = "languages";
  @SerializedName(SERIALIZED_NAME_LANGUAGES)
  private List<Language> languages;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_VARIABLES = "variables";
  @SerializedName(SERIALIZED_NAME_VARIABLES)
  private List<Variable> variables;

  public SurveyMetadata() {
  }

  public SurveyMetadata hierarchies(List<Hierarchy> hierarchies) {
    this.hierarchies = hierarchies;
    return this;
  }

  public SurveyMetadata addHierarchiesItem(Hierarchy hierarchiesItem) {
    if (this.hierarchies == null) {
      this.hierarchies = new ArrayList<>();
    }
    this.hierarchies.add(hierarchiesItem);
    return this;
  }

  /**
   * Get hierarchies
   * @return hierarchies
   */
  @javax.annotation.Nullable
  public List<Hierarchy> getHierarchies() {
    return hierarchies;
  }

  public void setHierarchies(List<Hierarchy> hierarchies) {
    this.hierarchies = hierarchies;
  }


  public SurveyMetadata interviewCount(Integer interviewCount) {
    this.interviewCount = interviewCount;
    return this;
  }

  /**
   * Get interviewCount
   * @return interviewCount
   */
  @javax.annotation.Nullable
  public Integer getInterviewCount() {
    return interviewCount;
  }

  public void setInterviewCount(Integer interviewCount) {
    this.interviewCount = interviewCount;
  }


  public SurveyMetadata languages(List<Language> languages) {
    this.languages = languages;
    return this;
  }

  public SurveyMetadata addLanguagesItem(Language languagesItem) {
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
  public List<Language> getLanguages() {
    return languages;
  }

  public void setLanguages(List<Language> languages) {
    this.languages = languages;
  }


  public SurveyMetadata name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SurveyMetadata title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public SurveyMetadata variables(List<Variable> variables) {
    this.variables = variables;
    return this;
  }

  public SurveyMetadata addVariablesItem(Variable variablesItem) {
    if (this.variables == null) {
      this.variables = new ArrayList<>();
    }
    this.variables.add(variablesItem);
    return this;
  }

  /**
   * Get variables
   * @return variables
   */
  @javax.annotation.Nullable
  public List<Variable> getVariables() {
    return variables;
  }

  public void setVariables(List<Variable> variables) {
    this.variables = variables;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SurveyMetadata surveyMetadata = (SurveyMetadata) o;
    return Objects.equals(this.hierarchies, surveyMetadata.hierarchies) &&
        Objects.equals(this.interviewCount, surveyMetadata.interviewCount) &&
        Objects.equals(this.languages, surveyMetadata.languages) &&
        Objects.equals(this.name, surveyMetadata.name) &&
        Objects.equals(this.title, surveyMetadata.title) &&
        Objects.equals(this.variables, surveyMetadata.variables);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(hierarchies, interviewCount, languages, name, title, variables);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SurveyMetadata {\n");
    sb.append("    hierarchies: ").append(toIndentedString(hierarchies)).append("\n");
    sb.append("    interviewCount: ").append(toIndentedString(interviewCount)).append("\n");
    sb.append("    languages: ").append(toIndentedString(languages)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    variables: ").append(toIndentedString(variables)).append("\n");
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
    openapiFields.add("hierarchies");
    openapiFields.add("interviewCount");
    openapiFields.add("languages");
    openapiFields.add("name");
    openapiFields.add("title");
    openapiFields.add("variables");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SurveyMetadata
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SurveyMetadata.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SurveyMetadata is not found in the empty JSON string", SurveyMetadata.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SurveyMetadata.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SurveyMetadata` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("hierarchies") != null && !jsonObj.get("hierarchies").isJsonNull()) {
        JsonArray jsonArrayhierarchies = jsonObj.getAsJsonArray("hierarchies");
        if (jsonArrayhierarchies != null) {
          // ensure the json data is an array
          if (!jsonObj.get("hierarchies").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `hierarchies` to be an array in the JSON string but got `%s`", jsonObj.get("hierarchies").toString()));
          }

          // validate the optional field `hierarchies` (array)
          for (int i = 0; i < jsonArrayhierarchies.size(); i++) {
            Hierarchy.validateJsonElement(jsonArrayhierarchies.get(i));
          };
        }
      }
      if (jsonObj.get("languages") != null && !jsonObj.get("languages").isJsonNull()) {
        JsonArray jsonArraylanguages = jsonObj.getAsJsonArray("languages");
        if (jsonArraylanguages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("languages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `languages` to be an array in the JSON string but got `%s`", jsonObj.get("languages").toString()));
          }

          // validate the optional field `languages` (array)
          for (int i = 0; i < jsonArraylanguages.size(); i++) {
            Language.validateJsonElement(jsonArraylanguages.get(i));
          };
        }
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if (jsonObj.get("variables") != null && !jsonObj.get("variables").isJsonNull()) {
        JsonArray jsonArrayvariables = jsonObj.getAsJsonArray("variables");
        if (jsonArrayvariables != null) {
          // ensure the json data is an array
          if (!jsonObj.get("variables").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `variables` to be an array in the JSON string but got `%s`", jsonObj.get("variables").toString()));
          }

          // validate the optional field `variables` (array)
          for (int i = 0; i < jsonArrayvariables.size(); i++) {
            Variable.validateJsonElement(jsonArrayvariables.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SurveyMetadata.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SurveyMetadata' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SurveyMetadata> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SurveyMetadata.class));

       return (TypeAdapter<T>) new TypeAdapter<SurveyMetadata>() {
           @Override
           public void write(JsonWriter out, SurveyMetadata value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SurveyMetadata read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SurveyMetadata given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SurveyMetadata
   * @throws IOException if the JSON string is invalid with respect to SurveyMetadata
   */
  public static SurveyMetadata fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SurveyMetadata.class);
  }

  /**
   * Convert an instance of SurveyMetadata to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

