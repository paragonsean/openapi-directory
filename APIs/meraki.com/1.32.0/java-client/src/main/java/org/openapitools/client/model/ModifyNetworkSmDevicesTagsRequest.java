/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * ModifyNetworkSmDevicesTagsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ModifyNetworkSmDevicesTagsRequest {
  public static final String SERIALIZED_NAME_IDS = "ids";
  @SerializedName(SERIALIZED_NAME_IDS)
  private List<String> ids = new ArrayList<>();

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private List<String> scope = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERIALS = "serials";
  @SerializedName(SERIALIZED_NAME_SERIALS)
  private List<String> serials = new ArrayList<>();

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_UPDATE_ACTION = "updateAction";
  @SerializedName(SERIALIZED_NAME_UPDATE_ACTION)
  private String updateAction;

  public static final String SERIALIZED_NAME_WIFI_MACS = "wifiMacs";
  @SerializedName(SERIALIZED_NAME_WIFI_MACS)
  private List<String> wifiMacs = new ArrayList<>();

  public ModifyNetworkSmDevicesTagsRequest() {
  }

  public ModifyNetworkSmDevicesTagsRequest ids(List<String> ids) {
    this.ids = ids;
    return this;
  }

  public ModifyNetworkSmDevicesTagsRequest addIdsItem(String idsItem) {
    if (this.ids == null) {
      this.ids = new ArrayList<>();
    }
    this.ids.add(idsItem);
    return this;
  }

  /**
   * The ids of the devices to be modified.
   * @return ids
   */
  @javax.annotation.Nullable
  public List<String> getIds() {
    return ids;
  }

  public void setIds(List<String> ids) {
    this.ids = ids;
  }


  public ModifyNetworkSmDevicesTagsRequest scope(List<String> scope) {
    this.scope = scope;
    return this;
  }

  public ModifyNetworkSmDevicesTagsRequest addScopeItem(String scopeItem) {
    if (this.scope == null) {
      this.scope = new ArrayList<>();
    }
    this.scope.add(scopeItem);
    return this;
  }

  /**
   * The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified.
   * @return scope
   */
  @javax.annotation.Nullable
  public List<String> getScope() {
    return scope;
  }

  public void setScope(List<String> scope) {
    this.scope = scope;
  }


  public ModifyNetworkSmDevicesTagsRequest serials(List<String> serials) {
    this.serials = serials;
    return this;
  }

  public ModifyNetworkSmDevicesTagsRequest addSerialsItem(String serialsItem) {
    if (this.serials == null) {
      this.serials = new ArrayList<>();
    }
    this.serials.add(serialsItem);
    return this;
  }

  /**
   * The serials of the devices to be modified.
   * @return serials
   */
  @javax.annotation.Nullable
  public List<String> getSerials() {
    return serials;
  }

  public void setSerials(List<String> serials) {
    this.serials = serials;
  }


  public ModifyNetworkSmDevicesTagsRequest tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public ModifyNetworkSmDevicesTagsRequest addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * The tags to be added, deleted, or updated.
   * @return tags
   */
  @javax.annotation.Nonnull
  public List<String> getTags() {
    return tags;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }


  public ModifyNetworkSmDevicesTagsRequest updateAction(String updateAction) {
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


  public ModifyNetworkSmDevicesTagsRequest wifiMacs(List<String> wifiMacs) {
    this.wifiMacs = wifiMacs;
    return this;
  }

  public ModifyNetworkSmDevicesTagsRequest addWifiMacsItem(String wifiMacsItem) {
    if (this.wifiMacs == null) {
      this.wifiMacs = new ArrayList<>();
    }
    this.wifiMacs.add(wifiMacsItem);
    return this;
  }

  /**
   * The wifiMacs of the devices to be modified.
   * @return wifiMacs
   */
  @javax.annotation.Nullable
  public List<String> getWifiMacs() {
    return wifiMacs;
  }

  public void setWifiMacs(List<String> wifiMacs) {
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
    ModifyNetworkSmDevicesTagsRequest modifyNetworkSmDevicesTagsRequest = (ModifyNetworkSmDevicesTagsRequest) o;
    return Objects.equals(this.ids, modifyNetworkSmDevicesTagsRequest.ids) &&
        Objects.equals(this.scope, modifyNetworkSmDevicesTagsRequest.scope) &&
        Objects.equals(this.serials, modifyNetworkSmDevicesTagsRequest.serials) &&
        Objects.equals(this.tags, modifyNetworkSmDevicesTagsRequest.tags) &&
        Objects.equals(this.updateAction, modifyNetworkSmDevicesTagsRequest.updateAction) &&
        Objects.equals(this.wifiMacs, modifyNetworkSmDevicesTagsRequest.wifiMacs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ids, scope, serials, tags, updateAction, wifiMacs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ModifyNetworkSmDevicesTagsRequest {\n");
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
   * @throws IOException if the JSON Element is invalid with respect to ModifyNetworkSmDevicesTagsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ModifyNetworkSmDevicesTagsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ModifyNetworkSmDevicesTagsRequest is not found in the empty JSON string", ModifyNetworkSmDevicesTagsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ModifyNetworkSmDevicesTagsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ModifyNetworkSmDevicesTagsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ModifyNetworkSmDevicesTagsRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("ids") != null && !jsonObj.get("ids").isJsonNull() && !jsonObj.get("ids").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `ids` to be an array in the JSON string but got `%s`", jsonObj.get("ids").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonNull() && !jsonObj.get("scope").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be an array in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("serials") != null && !jsonObj.get("serials").isJsonNull() && !jsonObj.get("serials").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `serials` to be an array in the JSON string but got `%s`", jsonObj.get("serials").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("tags") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
      if (!jsonObj.get("updateAction").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updateAction` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updateAction").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("wifiMacs") != null && !jsonObj.get("wifiMacs").isJsonNull() && !jsonObj.get("wifiMacs").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `wifiMacs` to be an array in the JSON string but got `%s`", jsonObj.get("wifiMacs").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ModifyNetworkSmDevicesTagsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ModifyNetworkSmDevicesTagsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ModifyNetworkSmDevicesTagsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ModifyNetworkSmDevicesTagsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ModifyNetworkSmDevicesTagsRequest>() {
           @Override
           public void write(JsonWriter out, ModifyNetworkSmDevicesTagsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ModifyNetworkSmDevicesTagsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ModifyNetworkSmDevicesTagsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ModifyNetworkSmDevicesTagsRequest
   * @throws IOException if the JSON string is invalid with respect to ModifyNetworkSmDevicesTagsRequest
   */
  public static ModifyNetworkSmDevicesTagsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ModifyNetworkSmDevicesTagsRequest.class);
  }

  /**
   * Convert an instance of ModifyNetworkSmDevicesTagsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

