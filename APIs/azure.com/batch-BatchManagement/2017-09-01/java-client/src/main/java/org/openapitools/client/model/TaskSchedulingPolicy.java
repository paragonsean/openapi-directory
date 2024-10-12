/*
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
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
import java.util.Arrays;

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
 * TaskSchedulingPolicy
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TaskSchedulingPolicy {
  /**
   * Gets or Sets nodeFillType
   */
  @JsonAdapter(NodeFillTypeEnum.Adapter.class)
  public enum NodeFillTypeEnum {
    SPREAD("Spread"),
    
    PACK("Pack");

    private String value;

    NodeFillTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NodeFillTypeEnum fromValue(String value) {
      for (NodeFillTypeEnum b : NodeFillTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NodeFillTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NodeFillTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NodeFillTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NodeFillTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NodeFillTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NODE_FILL_TYPE = "nodeFillType";
  @SerializedName(SERIALIZED_NAME_NODE_FILL_TYPE)
  private NodeFillTypeEnum nodeFillType;

  public TaskSchedulingPolicy() {
  }

  public TaskSchedulingPolicy nodeFillType(NodeFillTypeEnum nodeFillType) {
    this.nodeFillType = nodeFillType;
    return this;
  }

  /**
   * Get nodeFillType
   * @return nodeFillType
   */
  @javax.annotation.Nonnull
  public NodeFillTypeEnum getNodeFillType() {
    return nodeFillType;
  }

  public void setNodeFillType(NodeFillTypeEnum nodeFillType) {
    this.nodeFillType = nodeFillType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaskSchedulingPolicy taskSchedulingPolicy = (TaskSchedulingPolicy) o;
    return Objects.equals(this.nodeFillType, taskSchedulingPolicy.nodeFillType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nodeFillType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaskSchedulingPolicy {\n");
    sb.append("    nodeFillType: ").append(toIndentedString(nodeFillType)).append("\n");
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
    openapiFields.add("nodeFillType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("nodeFillType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TaskSchedulingPolicy
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TaskSchedulingPolicy.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TaskSchedulingPolicy is not found in the empty JSON string", TaskSchedulingPolicy.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TaskSchedulingPolicy.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TaskSchedulingPolicy` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TaskSchedulingPolicy.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("nodeFillType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nodeFillType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nodeFillType").toString()));
      }
      // validate the required field `nodeFillType`
      NodeFillTypeEnum.validateJsonElement(jsonObj.get("nodeFillType"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TaskSchedulingPolicy.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TaskSchedulingPolicy' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TaskSchedulingPolicy> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TaskSchedulingPolicy.class));

       return (TypeAdapter<T>) new TypeAdapter<TaskSchedulingPolicy>() {
           @Override
           public void write(JsonWriter out, TaskSchedulingPolicy value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TaskSchedulingPolicy read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TaskSchedulingPolicy given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TaskSchedulingPolicy
   * @throws IOException if the JSON string is invalid with respect to TaskSchedulingPolicy
   */
  public static TaskSchedulingPolicy fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TaskSchedulingPolicy.class);
  }

  /**
   * Convert an instance of TaskSchedulingPolicy to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

