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
import org.openapitools.client.model.Label;
import org.openapitools.client.model.ParentType;
import org.openapitools.client.model.UseType;
import org.openapitools.client.model.VariableType;
import org.openapitools.client.model.VariableValues;
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
 * Variable
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:41.455821-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Variable {
  public static final String SERIALIZED_NAME_IDENT = "ident";
  @SerializedName(SERIALIZED_NAME_IDENT)
  private String ident;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private Label label;

  public static final String SERIALIZED_NAME_MAX_RESPONSES = "maxResponses";
  @SerializedName(SERIALIZED_NAME_MAX_RESPONSES)
  private Integer maxResponses;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PARENT_TYPE = "parentType";
  @SerializedName(SERIALIZED_NAME_PARENT_TYPE)
  private ParentType parentType;

  public static final String SERIALIZED_NAME_QUESTIONS = "questions";
  @SerializedName(SERIALIZED_NAME_QUESTIONS)
  private List<Variable> questions;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private VariableType type;

  public static final String SERIALIZED_NAME_USE = "use";
  @SerializedName(SERIALIZED_NAME_USE)
  private UseType use;

  public static final String SERIALIZED_NAME_VARIABLE_VALUES = "variableValues";
  @SerializedName(SERIALIZED_NAME_VARIABLE_VALUES)
  private VariableValues variableValues;

  public Variable() {
  }

  public Variable ident(String ident) {
    this.ident = ident;
    return this;
  }

  /**
   * Get ident
   * @return ident
   */
  @javax.annotation.Nullable
  public String getIdent() {
    return ident;
  }

  public void setIdent(String ident) {
    this.ident = ident;
  }


  public Variable label(Label label) {
    this.label = label;
    return this;
  }

  /**
   * Get label
   * @return label
   */
  @javax.annotation.Nullable
  public Label getLabel() {
    return label;
  }

  public void setLabel(Label label) {
    this.label = label;
  }


  public Variable maxResponses(Integer maxResponses) {
    this.maxResponses = maxResponses;
    return this;
  }

  /**
   * Get maxResponses
   * @return maxResponses
   */
  @javax.annotation.Nullable
  public Integer getMaxResponses() {
    return maxResponses;
  }

  public void setMaxResponses(Integer maxResponses) {
    this.maxResponses = maxResponses;
  }


  public Variable name(String name) {
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


  public Variable parentType(ParentType parentType) {
    this.parentType = parentType;
    return this;
  }

  /**
   * Get parentType
   * @return parentType
   */
  @javax.annotation.Nullable
  public ParentType getParentType() {
    return parentType;
  }

  public void setParentType(ParentType parentType) {
    this.parentType = parentType;
  }


  public Variable questions(List<Variable> questions) {
    this.questions = questions;
    return this;
  }

  public Variable addQuestionsItem(Variable questionsItem) {
    if (this.questions == null) {
      this.questions = new ArrayList<>();
    }
    this.questions.add(questionsItem);
    return this;
  }

  /**
   * Get questions
   * @return questions
   */
  @javax.annotation.Nullable
  public List<Variable> getQuestions() {
    return questions;
  }

  public void setQuestions(List<Variable> questions) {
    this.questions = questions;
  }


  public Variable type(VariableType type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public VariableType getType() {
    return type;
  }

  public void setType(VariableType type) {
    this.type = type;
  }


  public Variable use(UseType use) {
    this.use = use;
    return this;
  }

  /**
   * Get use
   * @return use
   */
  @javax.annotation.Nullable
  public UseType getUse() {
    return use;
  }

  public void setUse(UseType use) {
    this.use = use;
  }


  public Variable variableValues(VariableValues variableValues) {
    this.variableValues = variableValues;
    return this;
  }

  /**
   * Get variableValues
   * @return variableValues
   */
  @javax.annotation.Nullable
  public VariableValues getVariableValues() {
    return variableValues;
  }

  public void setVariableValues(VariableValues variableValues) {
    this.variableValues = variableValues;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Variable variable = (Variable) o;
    return Objects.equals(this.ident, variable.ident) &&
        Objects.equals(this.label, variable.label) &&
        Objects.equals(this.maxResponses, variable.maxResponses) &&
        Objects.equals(this.name, variable.name) &&
        Objects.equals(this.parentType, variable.parentType) &&
        Objects.equals(this.questions, variable.questions) &&
        Objects.equals(this.type, variable.type) &&
        Objects.equals(this.use, variable.use) &&
        Objects.equals(this.variableValues, variable.variableValues);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(ident, label, maxResponses, name, parentType, questions, type, use, variableValues);
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
    sb.append("class Variable {\n");
    sb.append("    ident: ").append(toIndentedString(ident)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    maxResponses: ").append(toIndentedString(maxResponses)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    parentType: ").append(toIndentedString(parentType)).append("\n");
    sb.append("    questions: ").append(toIndentedString(questions)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    use: ").append(toIndentedString(use)).append("\n");
    sb.append("    variableValues: ").append(toIndentedString(variableValues)).append("\n");
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
    openapiFields.add("ident");
    openapiFields.add("label");
    openapiFields.add("maxResponses");
    openapiFields.add("name");
    openapiFields.add("parentType");
    openapiFields.add("questions");
    openapiFields.add("type");
    openapiFields.add("use");
    openapiFields.add("variableValues");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Variable
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Variable.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Variable is not found in the empty JSON string", Variable.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Variable.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Variable` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ident") != null && !jsonObj.get("ident").isJsonNull()) && !jsonObj.get("ident").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ident` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ident").toString()));
      }
      // validate the optional field `label`
      if (jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) {
        Label.validateJsonElement(jsonObj.get("label"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `parentType`
      if (jsonObj.get("parentType") != null && !jsonObj.get("parentType").isJsonNull()) {
        ParentType.validateJsonElement(jsonObj.get("parentType"));
      }
      if (jsonObj.get("questions") != null && !jsonObj.get("questions").isJsonNull()) {
        JsonArray jsonArrayquestions = jsonObj.getAsJsonArray("questions");
        if (jsonArrayquestions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("questions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `questions` to be an array in the JSON string but got `%s`", jsonObj.get("questions").toString()));
          }

          // validate the optional field `questions` (array)
          for (int i = 0; i < jsonArrayquestions.size(); i++) {
            Variable.validateJsonElement(jsonArrayquestions.get(i));
          };
        }
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        VariableType.validateJsonElement(jsonObj.get("type"));
      }
      // validate the optional field `use`
      if (jsonObj.get("use") != null && !jsonObj.get("use").isJsonNull()) {
        UseType.validateJsonElement(jsonObj.get("use"));
      }
      // validate the optional field `variableValues`
      if (jsonObj.get("variableValues") != null && !jsonObj.get("variableValues").isJsonNull()) {
        VariableValues.validateJsonElement(jsonObj.get("variableValues"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Variable.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Variable' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Variable> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Variable.class));

       return (TypeAdapter<T>) new TypeAdapter<Variable>() {
           @Override
           public void write(JsonWriter out, Variable value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Variable read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Variable given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Variable
   * @throws IOException if the JSON string is invalid with respect to Variable
   */
  public static Variable fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Variable.class);
  }

  /**
   * Convert an instance of Variable to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

