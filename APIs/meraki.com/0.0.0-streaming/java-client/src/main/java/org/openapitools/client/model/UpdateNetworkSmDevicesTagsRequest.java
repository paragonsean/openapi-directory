/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
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
 * UpdateNetworkSmDevicesTagsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:53.186925-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkSmDevicesTagsRequest {
  public static final String SERIALIZED_NAME_IDS = "ids";
  @SerializedName(SERIALIZED_NAME_IDS)
  private String ids;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public static final String SERIALIZED_NAME_SERIALS = "serials";
  @SerializedName(SERIALIZED_NAME_SERIALS)
  private String serials;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private String tags;

  public static final String SERIALIZED_NAME_UPDATE_ACTION = "updateAction";
  @SerializedName(SERIALIZED_NAME_UPDATE_ACTION)
  private String updateAction;

  public static final String SERIALIZED_NAME_WIFI_MACS = "wifiMacs";
  @SerializedName(SERIALIZED_NAME_WIFI_MACS)
  private String wifiMacs;

  public UpdateNetworkSmDevicesTagsRequest() {
  }

  public UpdateNetworkSmDevicesTagsRequest ids(String ids) {
    this.ids = ids;
    return this;
  }

  /**
   * The ids of the devices to be modified.
   * @return ids
   */
  @javax.annotation.Nullable
  public String getIds() {
    return ids;
  }

  public void setIds(String ids) {
    this.ids = ids;
  }


  public UpdateNetworkSmDevicesTagsRequest scope(String scope) {
    this.scope = scope;
    return this;
  }

  /**
   * The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified.
   * @return scope
   */
  @javax.annotation.Nullable
  public String getScope() {
    return scope;
  }

  public void setScope(String scope) {
    this.scope = scope;
  }


  public UpdateNetworkSmDevicesTagsRequest serials(String serials) {
    this.serials = serials;
    return this;
  }

  /**
   * The serials of the devices to be modified.
   * @return serials
   */
  @javax.annotation.Nullable
  public String getSerials() {
    return serials;
  }

  public void setSerials(String serials) {
    this.serials = serials;
  }


  public UpdateNetworkSmDevicesTagsRequest tags(String tags) {
    this.tags = tags;
    return this;
  }

  /**
   * The tags to be added, deleted, or updated.
   * @return tags
   */
  @javax.annotation.Nonnull
  public String getTags() {
    return tags;
  }

  public void setTags(String tags) {
    this.tags = tags;
  }


  public UpdateNetworkSmDevicesTagsRequest updateAction(String updateAction) {
    this.updateAction = updateAction;
    return this;
  }

  /**
   * One of add, delete, or update. Only devices that have been modified will be returned.
   * @return updateAction
   */
  @javax.annotation.Nonnull
  public String getUpdateAction() {
    return updateAction;
  }

  public void setUpdateAction(String updateAction) {
    this.updateAction = updateAction;
  }


  public UpdateNetworkSmDevicesTagsRequest wifiMacs(String wifiMacs) {
    this.wifiMacs = wifiMacs;
    return this;
  }

  /**
   * The wifiMacs of the devices to be modified.
   * @return wifiMacs
   */
  @javax.annotation.Nullable
  public String getWifiMacs() {
    return wifiMacs;
  }

  public void setWifiMacs(String wifiMacs) {
    this.wifiMacs = wifiMacs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkSmDevicesTagsRequest updateNetworkSmDevicesTagsRequest = (UpdateNetworkSmDevicesTagsRequest) o;
    return Objects.equals(this.ids, updateNetworkSmDevicesTagsRequest.ids) &&
        Objects.equals(this.scope, updateNetworkSmDevicesTagsRequest.scope) &&
        Objects.equals(this.serials, updateNetworkSmDevicesTagsRequest.serials) &&
        Objects.equals(this.tags, updateNetworkSmDevicesTagsRequest.tags) &&
        Objects.equals(this.updateAction, updateNetworkSmDevicesTagsRequest.updateAction) &&
        Objects.equals(this.wifiMacs, updateNetworkSmDevicesTagsRequest.wifiMacs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ids, scope, serials, tags, updateAction, wifiMacs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkSmDevicesTagsRequest {\n");
    sb.append("    ids: ").append(toIndentedString(ids)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    serials: ").append(toIndentedString(serials)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    updateAction: ").append(toIndentedString(updateAction)).append("\n");
    sb.append("    wifiMacs: ").append(toIndentedString(wifiMacs)).append("\n");
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
    openapiFields.add("ids");
    openapiFields.add("scope");
    openapiFields.add("serials");
    openapiFields.add("tags");
    openapiFields.add("updateAction");
    openapiFields.add("wifiMacs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("tags");
    openapiRequiredFields.add("updateAction");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkSmDevicesTagsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkSmDevicesTagsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkSmDevicesTagsRequest is not found in the empty JSON string", UpdateNetworkSmDevicesTagsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkSmDevicesTagsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkSmDevicesTagsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateNetworkSmDevicesTagsRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ids") != null && !jsonObj.get("ids").isJsonNull()) && !jsonObj.get("ids").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ids` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ids").toString()));
      }
      if ((jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonNull()) && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      if ((jsonObj.get("serials") != null && !jsonObj.get("serials").isJsonNull()) && !jsonObj.get("serials").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serials` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serials").toString()));
      }
      if (!jsonObj.get("tags").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if (!jsonObj.get("updateAction").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updateAction` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updateAction").toString()));
      }
      if ((jsonObj.get("wifiMacs") != null && !jsonObj.get("wifiMacs").isJsonNull()) && !jsonObj.get("wifiMacs").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `wifiMacs` to be a primitive type in the JSON string but got `%s`", jsonObj.get("wifiMacs").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkSmDevicesTagsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkSmDevicesTagsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkSmDevicesTagsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkSmDevicesTagsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkSmDevicesTagsRequest>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkSmDevicesTagsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkSmDevicesTagsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkSmDevicesTagsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkSmDevicesTagsRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkSmDevicesTagsRequest
   */
  public static UpdateNetworkSmDevicesTagsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkSmDevicesTagsRequest.class);
  }

  /**
   * Convert an instance of UpdateNetworkSmDevicesTagsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

