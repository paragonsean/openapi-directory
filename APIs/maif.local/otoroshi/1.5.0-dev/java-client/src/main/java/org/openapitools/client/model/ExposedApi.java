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
import java.net.URI;
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
 * The Open API configuration for your service (if one)
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:27.562730-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExposedApi {
  public static final String SERIALIZED_NAME_EXPOSE_API = "exposeApi";
  @SerializedName(SERIALIZED_NAME_EXPOSE_API)
  private Boolean exposeApi;

  public static final String SERIALIZED_NAME_OPEN_API_DESCRIPTOR_URL = "openApiDescriptorUrl";
  @SerializedName(SERIALIZED_NAME_OPEN_API_DESCRIPTOR_URL)
  private URI openApiDescriptorUrl;

  public ExposedApi() {
  }

  public ExposedApi exposeApi(Boolean exposeApi) {
    this.exposeApi = exposeApi;
    return this;
  }

  /**
   * Whether or not the current service expose an API with an Open API descriptor
   * @return exposeApi
   */
  @javax.annotation.Nonnull
  public Boolean getExposeApi() {
    return exposeApi;
  }

  public void setExposeApi(Boolean exposeApi) {
    this.exposeApi = exposeApi;
  }


  public ExposedApi openApiDescriptorUrl(URI openApiDescriptorUrl) {
    this.openApiDescriptorUrl = openApiDescriptorUrl;
    return this;
  }

  /**
   * The URL of the Open API descriptor
   * @return openApiDescriptorUrl
   */
  @javax.annotation.Nullable
  public URI getOpenApiDescriptorUrl() {
    return openApiDescriptorUrl;
  }

  public void setOpenApiDescriptorUrl(URI openApiDescriptorUrl) {
    this.openApiDescriptorUrl = openApiDescriptorUrl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExposedApi exposedApi = (ExposedApi) o;
    return Objects.equals(this.exposeApi, exposedApi.exposeApi) &&
        Objects.equals(this.openApiDescriptorUrl, exposedApi.openApiDescriptorUrl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(exposeApi, openApiDescriptorUrl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExposedApi {\n");
    sb.append("    exposeApi: ").append(toIndentedString(exposeApi)).append("\n");
    sb.append("    openApiDescriptorUrl: ").append(toIndentedString(openApiDescriptorUrl)).append("\n");
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
    openapiFields.add("exposeApi");
    openapiFields.add("openApiDescriptorUrl");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("exposeApi");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExposedApi
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExposedApi.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExposedApi is not found in the empty JSON string", ExposedApi.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExposedApi.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExposedApi` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ExposedApi.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("openApiDescriptorUrl") != null && !jsonObj.get("openApiDescriptorUrl").isJsonNull()) && !jsonObj.get("openApiDescriptorUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `openApiDescriptorUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("openApiDescriptorUrl").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExposedApi.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExposedApi' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExposedApi> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExposedApi.class));

       return (TypeAdapter<T>) new TypeAdapter<ExposedApi>() {
           @Override
           public void write(JsonWriter out, ExposedApi value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExposedApi read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExposedApi given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExposedApi
   * @throws IOException if the JSON string is invalid with respect to ExposedApi
   */
  public static ExposedApi fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExposedApi.class);
  }

  /**
   * Convert an instance of ExposedApi to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

