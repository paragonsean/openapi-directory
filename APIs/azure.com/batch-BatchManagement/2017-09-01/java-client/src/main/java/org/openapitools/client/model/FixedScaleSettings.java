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
import org.openapitools.client.model.ComputeNodeDeallocationOption;

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
 * FixedScaleSettings
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FixedScaleSettings {
  public static final String SERIALIZED_NAME_NODE_DEALLOCATION_OPTION = "nodeDeallocationOption";
  @SerializedName(SERIALIZED_NAME_NODE_DEALLOCATION_OPTION)
  private ComputeNodeDeallocationOption nodeDeallocationOption;

  public static final String SERIALIZED_NAME_RESIZE_TIMEOUT = "resizeTimeout";
  @SerializedName(SERIALIZED_NAME_RESIZE_TIMEOUT)
  private String resizeTimeout;

  public static final String SERIALIZED_NAME_TARGET_DEDICATED_NODES = "targetDedicatedNodes";
  @SerializedName(SERIALIZED_NAME_TARGET_DEDICATED_NODES)
  private Integer targetDedicatedNodes;

  public static final String SERIALIZED_NAME_TARGET_LOW_PRIORITY_NODES = "targetLowPriorityNodes";
  @SerializedName(SERIALIZED_NAME_TARGET_LOW_PRIORITY_NODES)
  private Integer targetLowPriorityNodes;

  public FixedScaleSettings() {
  }

  public FixedScaleSettings nodeDeallocationOption(ComputeNodeDeallocationOption nodeDeallocationOption) {
    this.nodeDeallocationOption = nodeDeallocationOption;
    return this;
  }

  /**
   * Get nodeDeallocationOption
   * @return nodeDeallocationOption
   */
  @javax.annotation.Nullable
  public ComputeNodeDeallocationOption getNodeDeallocationOption() {
    return nodeDeallocationOption;
  }

  public void setNodeDeallocationOption(ComputeNodeDeallocationOption nodeDeallocationOption) {
    this.nodeDeallocationOption = nodeDeallocationOption;
  }


  public FixedScaleSettings resizeTimeout(String resizeTimeout) {
    this.resizeTimeout = resizeTimeout;
    return this;
  }

  /**
   * The default value is 15 minutes. Timeout values use ISO 8601 format. For example, use PT10M for 10 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service rejects the request with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request).
   * @return resizeTimeout
   */
  @javax.annotation.Nullable
  public String getResizeTimeout() {
    return resizeTimeout;
  }

  public void setResizeTimeout(String resizeTimeout) {
    this.resizeTimeout = resizeTimeout;
  }


  public FixedScaleSettings targetDedicatedNodes(Integer targetDedicatedNodes) {
    this.targetDedicatedNodes = targetDedicatedNodes;
    return this;
  }

  /**
   * At least one of targetDedicatedNodes, targetLowPriority nodes must be set.
   * @return targetDedicatedNodes
   */
  @javax.annotation.Nullable
  public Integer getTargetDedicatedNodes() {
    return targetDedicatedNodes;
  }

  public void setTargetDedicatedNodes(Integer targetDedicatedNodes) {
    this.targetDedicatedNodes = targetDedicatedNodes;
  }


  public FixedScaleSettings targetLowPriorityNodes(Integer targetLowPriorityNodes) {
    this.targetLowPriorityNodes = targetLowPriorityNodes;
    return this;
  }

  /**
   * At least one of targetDedicatedNodes, targetLowPriority nodes must be set.
   * @return targetLowPriorityNodes
   */
  @javax.annotation.Nullable
  public Integer getTargetLowPriorityNodes() {
    return targetLowPriorityNodes;
  }

  public void setTargetLowPriorityNodes(Integer targetLowPriorityNodes) {
    this.targetLowPriorityNodes = targetLowPriorityNodes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FixedScaleSettings fixedScaleSettings = (FixedScaleSettings) o;
    return Objects.equals(this.nodeDeallocationOption, fixedScaleSettings.nodeDeallocationOption) &&
        Objects.equals(this.resizeTimeout, fixedScaleSettings.resizeTimeout) &&
        Objects.equals(this.targetDedicatedNodes, fixedScaleSettings.targetDedicatedNodes) &&
        Objects.equals(this.targetLowPriorityNodes, fixedScaleSettings.targetLowPriorityNodes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nodeDeallocationOption, resizeTimeout, targetDedicatedNodes, targetLowPriorityNodes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FixedScaleSettings {\n");
    sb.append("    nodeDeallocationOption: ").append(toIndentedString(nodeDeallocationOption)).append("\n");
    sb.append("    resizeTimeout: ").append(toIndentedString(resizeTimeout)).append("\n");
    sb.append("    targetDedicatedNodes: ").append(toIndentedString(targetDedicatedNodes)).append("\n");
    sb.append("    targetLowPriorityNodes: ").append(toIndentedString(targetLowPriorityNodes)).append("\n");
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
    openapiFields.add("nodeDeallocationOption");
    openapiFields.add("resizeTimeout");
    openapiFields.add("targetDedicatedNodes");
    openapiFields.add("targetLowPriorityNodes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FixedScaleSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FixedScaleSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FixedScaleSettings is not found in the empty JSON string", FixedScaleSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FixedScaleSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FixedScaleSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `nodeDeallocationOption`
      if (jsonObj.get("nodeDeallocationOption") != null && !jsonObj.get("nodeDeallocationOption").isJsonNull()) {
        ComputeNodeDeallocationOption.validateJsonElement(jsonObj.get("nodeDeallocationOption"));
      }
      if ((jsonObj.get("resizeTimeout") != null && !jsonObj.get("resizeTimeout").isJsonNull()) && !jsonObj.get("resizeTimeout").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resizeTimeout` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resizeTimeout").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FixedScaleSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FixedScaleSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FixedScaleSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FixedScaleSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<FixedScaleSettings>() {
           @Override
           public void write(JsonWriter out, FixedScaleSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FixedScaleSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FixedScaleSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FixedScaleSettings
   * @throws IOException if the JSON string is invalid with respect to FixedScaleSettings
   */
  public static FixedScaleSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FixedScaleSettings.class);
  }

  /**
   * Convert an instance of FixedScaleSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

