/*
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2017-02-01
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
 * Specifies a range of IP addresses permitted to connect to the cache
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:23.393005-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RedisFirewallRuleProperties {
  public static final String SERIALIZED_NAME_END_I_P = "endIP";
  @SerializedName(SERIALIZED_NAME_END_I_P)
  private String endIP;

  public static final String SERIALIZED_NAME_START_I_P = "startIP";
  @SerializedName(SERIALIZED_NAME_START_I_P)
  private String startIP;

  public RedisFirewallRuleProperties() {
  }

  public RedisFirewallRuleProperties endIP(String endIP) {
    this.endIP = endIP;
    return this;
  }

  /**
   * highest IP address included in the range
   * @return endIP
   */
  @javax.annotation.Nonnull
  public String getEndIP() {
    return endIP;
  }

  public void setEndIP(String endIP) {
    this.endIP = endIP;
  }


  public RedisFirewallRuleProperties startIP(String startIP) {
    this.startIP = startIP;
    return this;
  }

  /**
   * lowest IP address included in the range
   * @return startIP
   */
  @javax.annotation.Nonnull
  public String getStartIP() {
    return startIP;
  }

  public void setStartIP(String startIP) {
    this.startIP = startIP;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RedisFirewallRuleProperties redisFirewallRuleProperties = (RedisFirewallRuleProperties) o;
    return Objects.equals(this.endIP, redisFirewallRuleProperties.endIP) &&
        Objects.equals(this.startIP, redisFirewallRuleProperties.startIP);
  }

  @Override
  public int hashCode() {
    return Objects.hash(endIP, startIP);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RedisFirewallRuleProperties {\n");
    sb.append("    endIP: ").append(toIndentedString(endIP)).append("\n");
    sb.append("    startIP: ").append(toIndentedString(startIP)).append("\n");
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
    openapiFields.add("endIP");
    openapiFields.add("startIP");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("endIP");
    openapiRequiredFields.add("startIP");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RedisFirewallRuleProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RedisFirewallRuleProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RedisFirewallRuleProperties is not found in the empty JSON string", RedisFirewallRuleProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RedisFirewallRuleProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RedisFirewallRuleProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : RedisFirewallRuleProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("endIP").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endIP` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endIP").toString()));
      }
      if (!jsonObj.get("startIP").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `startIP` to be a primitive type in the JSON string but got `%s`", jsonObj.get("startIP").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RedisFirewallRuleProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RedisFirewallRuleProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RedisFirewallRuleProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RedisFirewallRuleProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<RedisFirewallRuleProperties>() {
           @Override
           public void write(JsonWriter out, RedisFirewallRuleProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RedisFirewallRuleProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RedisFirewallRuleProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RedisFirewallRuleProperties
   * @throws IOException if the JSON string is invalid with respect to RedisFirewallRuleProperties
   */
  public static RedisFirewallRuleProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RedisFirewallRuleProperties.class);
  }

  /**
   * Convert an instance of RedisFirewallRuleProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

