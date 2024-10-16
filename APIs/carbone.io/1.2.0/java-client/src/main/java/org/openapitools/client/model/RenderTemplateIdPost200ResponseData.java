/*
 * Carbone API
 * Carbone Cloud/On-premise Open API reference.  For requesting: - Carbone Cloud API: find your API key on your [Carbone account](https://account.carbone.io). Home page > Copy the `production` or `testing` API key. - Carbone On-premise: Update the `Server URL` on the Open API specification.  Useful links: - [API Flow](https://carbone.io/api-reference.html#quickstart-api-flow) - [Integration / SDKs](https://carbone.io/api-reference.html#api-integration) - [Generated document storage](https://carbone.io/api-reference.html#report-storage) - [Request timeout](https://carbone.io/api-reference.html#api-timeout)
 *
 * The version of the OpenAPI document: 1.2.0
 * Contact: support@carbone.io
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
 * RenderTemplateIdPost200ResponseData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:40.293106-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RenderTemplateIdPost200ResponseData {
  public static final String SERIALIZED_NAME_RENDER_ID = "renderId";
  @SerializedName(SERIALIZED_NAME_RENDER_ID)
  private String renderId;

  public RenderTemplateIdPost200ResponseData() {
  }

  public RenderTemplateIdPost200ResponseData renderId(String renderId) {
    this.renderId = renderId;
    return this;
  }

  /**
   * Get renderId
   * @return renderId
   */
  @javax.annotation.Nullable
  public String getRenderId() {
    return renderId;
  }

  public void setRenderId(String renderId) {
    this.renderId = renderId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RenderTemplateIdPost200ResponseData renderTemplateIdPost200ResponseData = (RenderTemplateIdPost200ResponseData) o;
    return Objects.equals(this.renderId, renderTemplateIdPost200ResponseData.renderId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(renderId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RenderTemplateIdPost200ResponseData {\n");
    sb.append("    renderId: ").append(toIndentedString(renderId)).append("\n");
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
    openapiFields.add("renderId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RenderTemplateIdPost200ResponseData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RenderTemplateIdPost200ResponseData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RenderTemplateIdPost200ResponseData is not found in the empty JSON string", RenderTemplateIdPost200ResponseData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RenderTemplateIdPost200ResponseData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RenderTemplateIdPost200ResponseData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("renderId") != null && !jsonObj.get("renderId").isJsonNull()) && !jsonObj.get("renderId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `renderId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("renderId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RenderTemplateIdPost200ResponseData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RenderTemplateIdPost200ResponseData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RenderTemplateIdPost200ResponseData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RenderTemplateIdPost200ResponseData.class));

       return (TypeAdapter<T>) new TypeAdapter<RenderTemplateIdPost200ResponseData>() {
           @Override
           public void write(JsonWriter out, RenderTemplateIdPost200ResponseData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RenderTemplateIdPost200ResponseData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RenderTemplateIdPost200ResponseData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RenderTemplateIdPost200ResponseData
   * @throws IOException if the JSON string is invalid with respect to RenderTemplateIdPost200ResponseData
   */
  public static RenderTemplateIdPost200ResponseData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RenderTemplateIdPost200ResponseData.class);
  }

  /**
   * Convert an instance of RenderTemplateIdPost200ResponseData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

