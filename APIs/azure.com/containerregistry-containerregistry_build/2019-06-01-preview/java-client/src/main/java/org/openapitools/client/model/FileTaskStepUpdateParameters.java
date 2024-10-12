/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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
import org.openapitools.client.model.SetValue;
import org.openapitools.client.model.TaskStepUpdateParameters;

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
 * The properties of updating a task step.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:55.681670-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FileTaskStepUpdateParameters extends TaskStepUpdateParameters {
  public static final String SERIALIZED_NAME_TASK_FILE_PATH = "taskFilePath";
  @SerializedName(SERIALIZED_NAME_TASK_FILE_PATH)
  private String taskFilePath;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<SetValue> values = new ArrayList<>();

  public static final String SERIALIZED_NAME_VALUES_FILE_PATH = "valuesFilePath";
  @SerializedName(SERIALIZED_NAME_VALUES_FILE_PATH)
  private String valuesFilePath;

  public FileTaskStepUpdateParameters() {
    this.type = this.getClass().getSimpleName();
  }

  public FileTaskStepUpdateParameters taskFilePath(String taskFilePath) {
    this.taskFilePath = taskFilePath;
    return this;
  }

  /**
   * The task template/definition file path relative to the source context.
   * @return taskFilePath
   */
  @javax.annotation.Nullable
  public String getTaskFilePath() {
    return taskFilePath;
  }

  public void setTaskFilePath(String taskFilePath) {
    this.taskFilePath = taskFilePath;
  }


  public FileTaskStepUpdateParameters values(List<SetValue> values) {
    this.values = values;
    return this;
  }

  public FileTaskStepUpdateParameters addValuesItem(SetValue valuesItem) {
    if (this.values == null) {
      this.values = new ArrayList<>();
    }
    this.values.add(valuesItem);
    return this;
  }

  /**
   * The collection of overridable values that can be passed when running a task.
   * @return values
   */
  @javax.annotation.Nullable
  public List<SetValue> getValues() {
    return values;
  }

  public void setValues(List<SetValue> values) {
    this.values = values;
  }


  public FileTaskStepUpdateParameters valuesFilePath(String valuesFilePath) {
    this.valuesFilePath = valuesFilePath;
    return this;
  }

  /**
   * The values/parameters file path relative to the source context.
   * @return valuesFilePath
   */
  @javax.annotation.Nullable
  public String getValuesFilePath() {
    return valuesFilePath;
  }

  public void setValuesFilePath(String valuesFilePath) {
    this.valuesFilePath = valuesFilePath;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FileTaskStepUpdateParameters fileTaskStepUpdateParameters = (FileTaskStepUpdateParameters) o;
    return Objects.equals(this.taskFilePath, fileTaskStepUpdateParameters.taskFilePath) &&
        Objects.equals(this.values, fileTaskStepUpdateParameters.values) &&
        Objects.equals(this.valuesFilePath, fileTaskStepUpdateParameters.valuesFilePath) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(taskFilePath, values, valuesFilePath, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FileTaskStepUpdateParameters {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    taskFilePath: ").append(toIndentedString(taskFilePath)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
    sb.append("    valuesFilePath: ").append(toIndentedString(valuesFilePath)).append("\n");
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
    openapiFields.add("contextAccessToken");
    openapiFields.add("contextPath");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FileTaskStepUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FileTaskStepUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FileTaskStepUpdateParameters is not found in the empty JSON string", FileTaskStepUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FileTaskStepUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FileTaskStepUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FileTaskStepUpdateParameters.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FileTaskStepUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FileTaskStepUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FileTaskStepUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FileTaskStepUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<FileTaskStepUpdateParameters>() {
           @Override
           public void write(JsonWriter out, FileTaskStepUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FileTaskStepUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FileTaskStepUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FileTaskStepUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to FileTaskStepUpdateParameters
   */
  public static FileTaskStepUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FileTaskStepUpdateParameters.class);
  }

  /**
   * Convert an instance of FileTaskStepUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

