/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.LegacyDeploymentResponseDeploymentValue;

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
 * LegacyDeploymentResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LegacyDeploymentResponse {
  public static final String SERIALIZED_NAME_DEPLOYMENT = "deployment";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT)
  private Map<String, LegacyDeploymentResponseDeploymentValue> deployment = new HashMap<>();

  public LegacyDeploymentResponse() {
  }

  public LegacyDeploymentResponse deployment(Map<String, LegacyDeploymentResponseDeploymentValue> deployment) {
    this.deployment = deployment;
    return this;
  }

  public LegacyDeploymentResponse putDeploymentItem(String key, LegacyDeploymentResponseDeploymentValue deploymentItem) {
    if (this.deployment == null) {
      this.deployment = new HashMap<>();
    }
    this.deployment.put(key, deploymentItem);
    return this;
  }

  /**
   * Get deployment
   * @return deployment
   */
  @javax.annotation.Nullable
  public Map<String, LegacyDeploymentResponseDeploymentValue> getDeployment() {
    return deployment;
  }

  public void setDeployment(Map<String, LegacyDeploymentResponseDeploymentValue> deployment) {
    this.deployment = deployment;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LegacyDeploymentResponse legacyDeploymentResponse = (LegacyDeploymentResponse) o;
    return Objects.equals(this.deployment, legacyDeploymentResponse.deployment);
  }

  @Override
  public int hashCode() {
    return Objects.hash(deployment);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LegacyDeploymentResponse {\n");
    sb.append("    deployment: ").append(toIndentedString(deployment)).append("\n");
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
    openapiFields.add("deployment");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LegacyDeploymentResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LegacyDeploymentResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LegacyDeploymentResponse is not found in the empty JSON string", LegacyDeploymentResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LegacyDeploymentResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LegacyDeploymentResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LegacyDeploymentResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LegacyDeploymentResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LegacyDeploymentResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LegacyDeploymentResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<LegacyDeploymentResponse>() {
           @Override
           public void write(JsonWriter out, LegacyDeploymentResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LegacyDeploymentResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LegacyDeploymentResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LegacyDeploymentResponse
   * @throws IOException if the JSON string is invalid with respect to LegacyDeploymentResponse
   */
  public static LegacyDeploymentResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LegacyDeploymentResponse.class);
  }

  /**
   * Convert an instance of LegacyDeploymentResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

