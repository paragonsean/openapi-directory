/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
 * Audit node info
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AuditNodeInfo {
  public static final String SERIALIZED_NAME_COUNT_CHILDREN = "countChildren";
  @SerializedName(SERIALIZED_NAME_COUNT_CHILDREN)
  private Long countChildren;

  public static final String SERIALIZED_NAME_NODE_ID = "nodeId";
  @SerializedName(SERIALIZED_NAME_NODE_ID)
  private Long nodeId;

  public static final String SERIALIZED_NAME_NODE_IS_ENCRYPTED = "nodeIsEncrypted";
  @SerializedName(SERIALIZED_NAME_NODE_IS_ENCRYPTED)
  private Boolean nodeIsEncrypted;

  public static final String SERIALIZED_NAME_NODE_NAME = "nodeName";
  @SerializedName(SERIALIZED_NAME_NODE_NAME)
  private String nodeName;

  public static final String SERIALIZED_NAME_NODE_PARENT_ID = "nodeParentId";
  @SerializedName(SERIALIZED_NAME_NODE_PARENT_ID)
  private Long nodeParentId;

  public static final String SERIALIZED_NAME_NODE_PARENT_PATH = "nodeParentPath";
  @SerializedName(SERIALIZED_NAME_NODE_PARENT_PATH)
  private String nodeParentPath;

  public AuditNodeInfo() {
  }

  public AuditNodeInfo countChildren(Long countChildren) {
    this.countChildren = countChildren;
    return this;
  }

  /**
   * Number of direct children  (no recursion; for rooms only)
   * @return countChildren
   */
  @javax.annotation.Nullable
  public Long getCountChildren() {
    return countChildren;
  }

  public void setCountChildren(Long countChildren) {
    this.countChildren = countChildren;
  }


  public AuditNodeInfo nodeId(Long nodeId) {
    this.nodeId = nodeId;
    return this;
  }

  /**
   * Node ID
   * @return nodeId
   */
  @javax.annotation.Nonnull
  public Long getNodeId() {
    return nodeId;
  }

  public void setNodeId(Long nodeId) {
    this.nodeId = nodeId;
  }


  public AuditNodeInfo nodeIsEncrypted(Boolean nodeIsEncrypted) {
    this.nodeIsEncrypted = nodeIsEncrypted;
    return this;
  }

  /**
   * Encryption state
   * @return nodeIsEncrypted
   */
  @javax.annotation.Nullable
  public Boolean getNodeIsEncrypted() {
    return nodeIsEncrypted;
  }

  public void setNodeIsEncrypted(Boolean nodeIsEncrypted) {
    this.nodeIsEncrypted = nodeIsEncrypted;
  }


  public AuditNodeInfo nodeName(String nodeName) {
    this.nodeName = nodeName;
    return this;
  }

  /**
   * Node name
   * @return nodeName
   */
  @javax.annotation.Nonnull
  public String getNodeName() {
    return nodeName;
  }

  public void setNodeName(String nodeName) {
    this.nodeName = nodeName;
  }


  public AuditNodeInfo nodeParentId(Long nodeParentId) {
    this.nodeParentId = nodeParentId;
    return this;
  }

  /**
   * Parent room ID
   * @return nodeParentId
   */
  @javax.annotation.Nullable
  public Long getNodeParentId() {
    return nodeParentId;
  }

  public void setNodeParentId(Long nodeParentId) {
    this.nodeParentId = nodeParentId;
  }


  public AuditNodeInfo nodeParentPath(String nodeParentPath) {
    this.nodeParentPath = nodeParentPath;
    return this;
  }

  /**
   * Parent node path  &#x60;/&#x60; if node is a root node (room)
   * @return nodeParentPath
   */
  @javax.annotation.Nonnull
  public String getNodeParentPath() {
    return nodeParentPath;
  }

  public void setNodeParentPath(String nodeParentPath) {
    this.nodeParentPath = nodeParentPath;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuditNodeInfo auditNodeInfo = (AuditNodeInfo) o;
    return Objects.equals(this.countChildren, auditNodeInfo.countChildren) &&
        Objects.equals(this.nodeId, auditNodeInfo.nodeId) &&
        Objects.equals(this.nodeIsEncrypted, auditNodeInfo.nodeIsEncrypted) &&
        Objects.equals(this.nodeName, auditNodeInfo.nodeName) &&
        Objects.equals(this.nodeParentId, auditNodeInfo.nodeParentId) &&
        Objects.equals(this.nodeParentPath, auditNodeInfo.nodeParentPath);
  }

  @Override
  public int hashCode() {
    return Objects.hash(countChildren, nodeId, nodeIsEncrypted, nodeName, nodeParentId, nodeParentPath);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuditNodeInfo {\n");
    sb.append("    countChildren: ").append(toIndentedString(countChildren)).append("\n");
    sb.append("    nodeId: ").append(toIndentedString(nodeId)).append("\n");
    sb.append("    nodeIsEncrypted: ").append(toIndentedString(nodeIsEncrypted)).append("\n");
    sb.append("    nodeName: ").append(toIndentedString(nodeName)).append("\n");
    sb.append("    nodeParentId: ").append(toIndentedString(nodeParentId)).append("\n");
    sb.append("    nodeParentPath: ").append(toIndentedString(nodeParentPath)).append("\n");
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
    openapiFields.add("countChildren");
    openapiFields.add("nodeId");
    openapiFields.add("nodeIsEncrypted");
    openapiFields.add("nodeName");
    openapiFields.add("nodeParentId");
    openapiFields.add("nodeParentPath");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("nodeId");
    openapiRequiredFields.add("nodeName");
    openapiRequiredFields.add("nodeParentPath");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AuditNodeInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AuditNodeInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AuditNodeInfo is not found in the empty JSON string", AuditNodeInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AuditNodeInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AuditNodeInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AuditNodeInfo.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("nodeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nodeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nodeName").toString()));
      }
      if (!jsonObj.get("nodeParentPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nodeParentPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nodeParentPath").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AuditNodeInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AuditNodeInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AuditNodeInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AuditNodeInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<AuditNodeInfo>() {
           @Override
           public void write(JsonWriter out, AuditNodeInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AuditNodeInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AuditNodeInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AuditNodeInfo
   * @throws IOException if the JSON string is invalid with respect to AuditNodeInfo
   */
  public static AuditNodeInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AuditNodeInfo.class);
  }

  /**
   * Convert an instance of AuditNodeInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

