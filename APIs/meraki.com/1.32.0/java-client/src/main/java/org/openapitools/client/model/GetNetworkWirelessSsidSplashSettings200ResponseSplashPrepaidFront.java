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
 * The prepaid front image used in the splash page.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront {
  public static final String SERIALIZED_NAME_EXTENSION = "extension";
  @SerializedName(SERIALIZED_NAME_EXTENSION)
  private String extension;

  public static final String SERIALIZED_NAME_MD5 = "md5";
  @SerializedName(SERIALIZED_NAME_MD5)
  private String md5;

  public GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront() {
  }

  public GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront extension(String extension) {
    this.extension = extension;
    return this;
  }

  /**
   * The extension of the prepaid front image file.
   * @return extension
   */
  @javax.annotation.Nullable
  public String getExtension() {
    return extension;
  }

  public void setExtension(String extension) {
    this.extension = extension;
  }


  public GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront md5(String md5) {
    this.md5 = md5;
    return this;
  }

  /**
   * The MD5 value of the prepaid front image file.
   * @return md5
   */
  @javax.annotation.Nullable
  public String getMd5() {
    return md5;
  }

  public void setMd5(String md5) {
    this.md5 = md5;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront getNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront = (GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront) o;
    return Objects.equals(this.extension, getNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.extension) &&
        Objects.equals(this.md5, getNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.md5);
  }

  @Override
  public int hashCode() {
    return Objects.hash(extension, md5);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront {\n");
    sb.append("    extension: ").append(toIndentedString(extension)).append("\n");
    sb.append("    md5: ").append(toIndentedString(md5)).append("\n");
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
    openapiFields.add("extension");
    openapiFields.add("md5");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront is not found in the empty JSON string", GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("extension") != null && !jsonObj.get("extension").isJsonNull()) && !jsonObj.get("extension").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `extension` to be a primitive type in the JSON string but got `%s`", jsonObj.get("extension").toString()));
      }
      if ((jsonObj.get("md5") != null && !jsonObj.get("md5").isJsonNull()) && !jsonObj.get("md5").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `md5` to be a primitive type in the JSON string but got `%s`", jsonObj.get("md5").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront>() {
           @Override
           public void write(JsonWriter out, GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront
   * @throws IOException if the JSON string is invalid with respect to GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront
   */
  public static GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.class);
  }

  /**
   * Convert an instance of GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

