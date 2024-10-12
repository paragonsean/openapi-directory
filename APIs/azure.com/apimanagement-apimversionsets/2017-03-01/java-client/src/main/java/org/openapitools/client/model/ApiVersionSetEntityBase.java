/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2017-03-01
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
 * ApiVersionSetEntityBase
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:19:20.690501-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiVersionSetEntityBase {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_VERSION_HEADER_NAME = "versionHeaderName";
  @SerializedName(SERIALIZED_NAME_VERSION_HEADER_NAME)
  private String versionHeaderName;

  public static final String SERIALIZED_NAME_VERSION_QUERY_NAME = "versionQueryName";
  @SerializedName(SERIALIZED_NAME_VERSION_QUERY_NAME)
  private String versionQueryName;

  public ApiVersionSetEntityBase() {
  }

  public ApiVersionSetEntityBase description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description of API Version Set.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ApiVersionSetEntityBase versionHeaderName(String versionHeaderName) {
    this.versionHeaderName = versionHeaderName;
    return this;
  }

  /**
   * Name of HTTP header parameter that indicates the API Version if versioningScheme is set to &#x60;header&#x60;.
   * @return versionHeaderName
   */
  @javax.annotation.Nullable
  public String getVersionHeaderName() {
    return versionHeaderName;
  }

  public void setVersionHeaderName(String versionHeaderName) {
    this.versionHeaderName = versionHeaderName;
  }


  public ApiVersionSetEntityBase versionQueryName(String versionQueryName) {
    this.versionQueryName = versionQueryName;
    return this;
  }

  /**
   * Name of query parameter that indicates the API Version if versioningScheme is set to &#x60;query&#x60;.
   * @return versionQueryName
   */
  @javax.annotation.Nullable
  public String getVersionQueryName() {
    return versionQueryName;
  }

  public void setVersionQueryName(String versionQueryName) {
    this.versionQueryName = versionQueryName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiVersionSetEntityBase apiVersionSetEntityBase = (ApiVersionSetEntityBase) o;
    return Objects.equals(this.description, apiVersionSetEntityBase.description) &&
        Objects.equals(this.versionHeaderName, apiVersionSetEntityBase.versionHeaderName) &&
        Objects.equals(this.versionQueryName, apiVersionSetEntityBase.versionQueryName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, versionHeaderName, versionQueryName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApiVersionSetEntityBase {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    versionHeaderName: ").append(toIndentedString(versionHeaderName)).append("\n");
    sb.append("    versionQueryName: ").append(toIndentedString(versionQueryName)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("versionHeaderName");
    openapiFields.add("versionQueryName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiVersionSetEntityBase
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiVersionSetEntityBase.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiVersionSetEntityBase is not found in the empty JSON string", ApiVersionSetEntityBase.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiVersionSetEntityBase.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiVersionSetEntityBase` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("versionHeaderName") != null && !jsonObj.get("versionHeaderName").isJsonNull()) && !jsonObj.get("versionHeaderName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `versionHeaderName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("versionHeaderName").toString()));
      }
      if ((jsonObj.get("versionQueryName") != null && !jsonObj.get("versionQueryName").isJsonNull()) && !jsonObj.get("versionQueryName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `versionQueryName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("versionQueryName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiVersionSetEntityBase.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiVersionSetEntityBase' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiVersionSetEntityBase> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiVersionSetEntityBase.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiVersionSetEntityBase>() {
           @Override
           public void write(JsonWriter out, ApiVersionSetEntityBase value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiVersionSetEntityBase read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiVersionSetEntityBase given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiVersionSetEntityBase
   * @throws IOException if the JSON string is invalid with respect to ApiVersionSetEntityBase
   */
  public static ApiVersionSetEntityBase fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiVersionSetEntityBase.class);
  }

  /**
   * Convert an instance of ApiVersionSetEntityBase to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

