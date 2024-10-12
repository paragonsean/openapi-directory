/*
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
 * The filtering configuration block for a service of globally.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:27.562730-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IpFiltering {
  public static final String SERIALIZED_NAME_BLACKLIST = "blacklist";
  @SerializedName(SERIALIZED_NAME_BLACKLIST)
  private List<String> blacklist = new ArrayList<>();

  public static final String SERIALIZED_NAME_WHITELIST = "whitelist";
  @SerializedName(SERIALIZED_NAME_WHITELIST)
  private List<String> whitelist = new ArrayList<>();

  public IpFiltering() {
  }

  public IpFiltering blacklist(List<String> blacklist) {
    this.blacklist = blacklist;
    return this;
  }

  public IpFiltering addBlacklistItem(String blacklistItem) {
    if (this.blacklist == null) {
      this.blacklist = new ArrayList<>();
    }
    this.blacklist.add(blacklistItem);
    return this;
  }

  /**
   * Blacklisted IP addresses
   * @return blacklist
   */
  @javax.annotation.Nonnull
  public List<String> getBlacklist() {
    return blacklist;
  }

  public void setBlacklist(List<String> blacklist) {
    this.blacklist = blacklist;
  }


  public IpFiltering whitelist(List<String> whitelist) {
    this.whitelist = whitelist;
    return this;
  }

  public IpFiltering addWhitelistItem(String whitelistItem) {
    if (this.whitelist == null) {
      this.whitelist = new ArrayList<>();
    }
    this.whitelist.add(whitelistItem);
    return this;
  }

  /**
   * Whitelisted IP addresses
   * @return whitelist
   */
  @javax.annotation.Nonnull
  public List<String> getWhitelist() {
    return whitelist;
  }

  public void setWhitelist(List<String> whitelist) {
    this.whitelist = whitelist;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IpFiltering ipFiltering = (IpFiltering) o;
    return Objects.equals(this.blacklist, ipFiltering.blacklist) &&
        Objects.equals(this.whitelist, ipFiltering.whitelist);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blacklist, whitelist);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IpFiltering {\n");
    sb.append("    blacklist: ").append(toIndentedString(blacklist)).append("\n");
    sb.append("    whitelist: ").append(toIndentedString(whitelist)).append("\n");
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
    openapiFields.add("blacklist");
    openapiFields.add("whitelist");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("blacklist");
    openapiRequiredFields.add("whitelist");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IpFiltering
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IpFiltering.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IpFiltering is not found in the empty JSON string", IpFiltering.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IpFiltering.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IpFiltering` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : IpFiltering.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("blacklist") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("blacklist").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `blacklist` to be an array in the JSON string but got `%s`", jsonObj.get("blacklist").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("whitelist") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("whitelist").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `whitelist` to be an array in the JSON string but got `%s`", jsonObj.get("whitelist").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IpFiltering.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IpFiltering' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IpFiltering> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IpFiltering.class));

       return (TypeAdapter<T>) new TypeAdapter<IpFiltering>() {
           @Override
           public void write(JsonWriter out, IpFiltering value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IpFiltering read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IpFiltering given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IpFiltering
   * @throws IOException if the JSON string is invalid with respect to IpFiltering
   */
  public static IpFiltering fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IpFiltering.class);
  }

  /**
   * Convert an instance of IpFiltering to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

