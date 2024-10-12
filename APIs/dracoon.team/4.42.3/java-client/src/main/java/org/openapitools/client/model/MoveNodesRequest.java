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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.MoveNode;

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
 * Request model for moving nodes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MoveNodesRequest {
  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<MoveNode> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_KEEP_SHARE_LINKS = "keepShareLinks";
  @SerializedName(SERIALIZED_NAME_KEEP_SHARE_LINKS)
  private Boolean keepShareLinks = false;

  public static final String SERIALIZED_NAME_NODE_IDS = "nodeIds";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_NODE_IDS)
  private List<Long> nodeIds = new ArrayList<>();

  /**
   * Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60;
   */
  @JsonAdapter(ResolutionStrategyEnum.Adapter.class)
  public enum ResolutionStrategyEnum {
    AUTORENAME("autorename"),
    
    OVERWRITE("overwrite"),
    
    FAIL("fail");

    private String value;

    ResolutionStrategyEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ResolutionStrategyEnum fromValue(String value) {
      for (ResolutionStrategyEnum b : ResolutionStrategyEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ResolutionStrategyEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ResolutionStrategyEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ResolutionStrategyEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ResolutionStrategyEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ResolutionStrategyEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RESOLUTION_STRATEGY = "resolutionStrategy";
  @SerializedName(SERIALIZED_NAME_RESOLUTION_STRATEGY)
  private ResolutionStrategyEnum resolutionStrategy = ResolutionStrategyEnum.AUTORENAME;

  public MoveNodesRequest() {
  }

  public MoveNodesRequest items(List<MoveNode> items) {
    this.items = items;
    return this;
  }

  public MoveNodesRequest addItemsItem(MoveNode itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * List of nodes to be moved
   * @return items
   */
  @javax.annotation.Nullable
  public List<MoveNode> getItems() {
    return items;
  }

  public void setItems(List<MoveNode> items) {
    this.items = items;
  }


  public MoveNodesRequest keepShareLinks(Boolean keepShareLinks) {
    this.keepShareLinks = keepShareLinks;
    return this;
  }

  /**
   * Preserve Download Share Links and point them to the new node.
   * @return keepShareLinks
   */
  @javax.annotation.Nullable
  public Boolean getKeepShareLinks() {
    return keepShareLinks;
  }

  public void setKeepShareLinks(Boolean keepShareLinks) {
    this.keepShareLinks = keepShareLinks;
  }


  @Deprecated
  public MoveNodesRequest nodeIds(List<Long> nodeIds) {
    this.nodeIds = nodeIds;
    return this;
  }

  public MoveNodesRequest addNodeIdsItem(Long nodeIdsItem) {
    if (this.nodeIds == null) {
      this.nodeIds = new ArrayList<>();
    }
    this.nodeIds.add(nodeIdsItem);
    return this;
  }

  /**
   * &amp;#128679; Deprecated since v4.5.0  Node IDs  Please use &#x60;items&#x60; instead.
   * @return nodeIds
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public List<Long> getNodeIds() {
    return nodeIds;
  }

  @Deprecated
  public void setNodeIds(List<Long> nodeIds) {
    this.nodeIds = nodeIds;
  }


  public MoveNodesRequest resolutionStrategy(ResolutionStrategyEnum resolutionStrategy) {
    this.resolutionStrategy = resolutionStrategy;
    return this;
  }

  /**
   * Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60;
   * @return resolutionStrategy
   */
  @javax.annotation.Nullable
  public ResolutionStrategyEnum getResolutionStrategy() {
    return resolutionStrategy;
  }

  public void setResolutionStrategy(ResolutionStrategyEnum resolutionStrategy) {
    this.resolutionStrategy = resolutionStrategy;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MoveNodesRequest moveNodesRequest = (MoveNodesRequest) o;
    return Objects.equals(this.items, moveNodesRequest.items) &&
        Objects.equals(this.keepShareLinks, moveNodesRequest.keepShareLinks) &&
        Objects.equals(this.nodeIds, moveNodesRequest.nodeIds) &&
        Objects.equals(this.resolutionStrategy, moveNodesRequest.resolutionStrategy);
  }

  @Override
  public int hashCode() {
    return Objects.hash(items, keepShareLinks, nodeIds, resolutionStrategy);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MoveNodesRequest {\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    keepShareLinks: ").append(toIndentedString(keepShareLinks)).append("\n");
    sb.append("    nodeIds: ").append(toIndentedString(nodeIds)).append("\n");
    sb.append("    resolutionStrategy: ").append(toIndentedString(resolutionStrategy)).append("\n");
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
    openapiFields.add("items");
    openapiFields.add("keepShareLinks");
    openapiFields.add("nodeIds");
    openapiFields.add("resolutionStrategy");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MoveNodesRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MoveNodesRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MoveNodesRequest is not found in the empty JSON string", MoveNodesRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MoveNodesRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MoveNodesRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            MoveNode.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("nodeIds") != null && !jsonObj.get("nodeIds").isJsonNull() && !jsonObj.get("nodeIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `nodeIds` to be an array in the JSON string but got `%s`", jsonObj.get("nodeIds").toString()));
      }
      if ((jsonObj.get("resolutionStrategy") != null && !jsonObj.get("resolutionStrategy").isJsonNull()) && !jsonObj.get("resolutionStrategy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resolutionStrategy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resolutionStrategy").toString()));
      }
      // validate the optional field `resolutionStrategy`
      if (jsonObj.get("resolutionStrategy") != null && !jsonObj.get("resolutionStrategy").isJsonNull()) {
        ResolutionStrategyEnum.validateJsonElement(jsonObj.get("resolutionStrategy"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MoveNodesRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MoveNodesRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MoveNodesRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MoveNodesRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<MoveNodesRequest>() {
           @Override
           public void write(JsonWriter out, MoveNodesRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MoveNodesRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MoveNodesRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MoveNodesRequest
   * @throws IOException if the JSON string is invalid with respect to MoveNodesRequest
   */
  public static MoveNodesRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MoveNodesRequest.class);
  }

  /**
   * Convert an instance of MoveNodesRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

