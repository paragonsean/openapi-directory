/*
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
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
 * GetRawBlockV2200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:48.868561-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetRawBlockV2200Response {
  public static final String SERIALIZED_NAME_HEX = "hex";
  @SerializedName(SERIALIZED_NAME_HEX)
  private String hex;

  public GetRawBlockV2200Response() {
  }

  public GetRawBlockV2200Response hex(String hex) {
    this.hex = hex;
    return this;
  }

  /**
   * Get hex
   * @return hex
   */
  @javax.annotation.Nullable
  public String getHex() {
    return hex;
  }

  public void setHex(String hex) {
    this.hex = hex;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetRawBlockV2200Response getRawBlockV2200Response = (GetRawBlockV2200Response) o;
    return Objects.equals(this.hex, getRawBlockV2200Response.hex);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hex);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetRawBlockV2200Response {\n");
    sb.append("    hex: ").append(toIndentedString(hex)).append("\n");
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
    openapiFields.add("hex");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetRawBlockV2200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetRawBlockV2200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetRawBlockV2200Response is not found in the empty JSON string", GetRawBlockV2200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetRawBlockV2200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetRawBlockV2200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("hex") != null && !jsonObj.get("hex").isJsonNull()) && !jsonObj.get("hex").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hex` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hex").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetRawBlockV2200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetRawBlockV2200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetRawBlockV2200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetRawBlockV2200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetRawBlockV2200Response>() {
           @Override
           public void write(JsonWriter out, GetRawBlockV2200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetRawBlockV2200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetRawBlockV2200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetRawBlockV2200Response
   * @throws IOException if the JSON string is invalid with respect to GetRawBlockV2200Response
   */
  public static GetRawBlockV2200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetRawBlockV2200Response.class);
  }

  /**
   * Convert an instance of GetRawBlockV2200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

