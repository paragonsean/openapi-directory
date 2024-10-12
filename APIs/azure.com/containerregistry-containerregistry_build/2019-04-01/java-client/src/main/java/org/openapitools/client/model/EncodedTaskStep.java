/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
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
import org.openapitools.client.model.BaseImageDependency;
import org.openapitools.client.model.SetValue;
import org.openapitools.client.model.TaskStepProperties;

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
 * The properties of a encoded task step.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EncodedTaskStep extends TaskStepProperties {
  public static final String SERIALIZED_NAME_ENCODED_TASK_CONTENT = "encodedTaskContent";
  @SerializedName(SERIALIZED_NAME_ENCODED_TASK_CONTENT)
  private String encodedTaskContent;

  public static final String SERIALIZED_NAME_ENCODED_VALUES_CONTENT = "encodedValuesContent";
  @SerializedName(SERIALIZED_NAME_ENCODED_VALUES_CONTENT)
  private String encodedValuesContent;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<SetValue> values = new ArrayList<>();

  public EncodedTaskStep() {
    this.type = this.getClass().getSimpleName();
  }

  public EncodedTaskStep(
     List<BaseImageDependency> baseImageDependencies, 
     TypeEnum type
  ) {
    this();
    this.baseImageDependencies = baseImageDependencies;
    this.type = type;
  }

  public EncodedTaskStep encodedTaskContent(String encodedTaskContent) {
    this.encodedTaskContent = encodedTaskContent;
    return this;
  }

  /**
   * Base64 encoded value of the template/definition file content.
   * @return encodedTaskContent
   */
  @javax.annotation.Nonnull
  public String getEncodedTaskContent() {
    return encodedTaskContent;
  }

  public void setEncodedTaskContent(String encodedTaskContent) {
    this.encodedTaskContent = encodedTaskContent;
  }


  public EncodedTaskStep encodedValuesContent(String encodedValuesContent) {
    this.encodedValuesContent = encodedValuesContent;
    return this;
  }

  /**
   * Base64 encoded value of the parameters/values file content.
   * @return encodedValuesContent
   */
  @javax.annotation.Nullable
  public String getEncodedValuesContent() {
    return encodedValuesContent;
  }

  public void setEncodedValuesContent(String encodedValuesContent) {
    this.encodedValuesContent = encodedValuesContent;
  }


  public EncodedTaskStep values(List<SetValue> values) {
    this.values = values;
    return this;
  }

  public EncodedTaskStep addValuesItem(SetValue valuesItem) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EncodedTaskStep encodedTaskStep = (EncodedTaskStep) o;
    return Objects.equals(this.encodedTaskContent, encodedTaskStep.encodedTaskContent) &&
        Objects.equals(this.encodedValuesContent, encodedTaskStep.encodedValuesContent) &&
        Objects.equals(this.values, encodedTaskStep.values) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(encodedTaskContent, encodedValuesContent, values, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EncodedTaskStep {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    encodedTaskContent: ").append(toIndentedString(encodedTaskContent)).append("\n");
    sb.append("    encodedValuesContent: ").append(toIndentedString(encodedValuesContent)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
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
    openapiFields.add("baseImageDependencies");
    openapiFields.add("contextAccessToken");
    openapiFields.add("contextPath");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("encodedTaskContent");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EncodedTaskStep
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EncodedTaskStep.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EncodedTaskStep is not found in the empty JSON string", EncodedTaskStep.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EncodedTaskStep.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EncodedTaskStep` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EncodedTaskStep.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EncodedTaskStep.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EncodedTaskStep' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EncodedTaskStep> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EncodedTaskStep.class));

       return (TypeAdapter<T>) new TypeAdapter<EncodedTaskStep>() {
           @Override
           public void write(JsonWriter out, EncodedTaskStep value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EncodedTaskStep read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EncodedTaskStep given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EncodedTaskStep
   * @throws IOException if the JSON string is invalid with respect to EncodedTaskStep
   */
  public static EncodedTaskStep fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EncodedTaskStep.class);
  }

  /**
   * Convert an instance of EncodedTaskStep to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

