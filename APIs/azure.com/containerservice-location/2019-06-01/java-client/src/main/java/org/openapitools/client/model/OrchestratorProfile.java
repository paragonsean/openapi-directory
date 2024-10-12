/*
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2019-06-01
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
 * Contains information about orchestrator.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:55.965123-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrchestratorProfile {
  public static final String SERIALIZED_NAME_IS_PREVIEW = "isPreview";
  @SerializedName(SERIALIZED_NAME_IS_PREVIEW)
  private Boolean isPreview;

  public static final String SERIALIZED_NAME_ORCHESTRATOR_TYPE = "orchestratorType";
  @SerializedName(SERIALIZED_NAME_ORCHESTRATOR_TYPE)
  private String orchestratorType;

  public static final String SERIALIZED_NAME_ORCHESTRATOR_VERSION = "orchestratorVersion";
  @SerializedName(SERIALIZED_NAME_ORCHESTRATOR_VERSION)
  private String orchestratorVersion;

  public OrchestratorProfile() {
  }

  public OrchestratorProfile isPreview(Boolean isPreview) {
    this.isPreview = isPreview;
    return this;
  }

  /**
   * Whether Kubernetes version is currently in preview.
   * @return isPreview
   */
  @javax.annotation.Nullable
  public Boolean getIsPreview() {
    return isPreview;
  }

  public void setIsPreview(Boolean isPreview) {
    this.isPreview = isPreview;
  }


  public OrchestratorProfile orchestratorType(String orchestratorType) {
    this.orchestratorType = orchestratorType;
    return this;
  }

  /**
   * Orchestrator type.
   * @return orchestratorType
   */
  @javax.annotation.Nullable
  public String getOrchestratorType() {
    return orchestratorType;
  }

  public void setOrchestratorType(String orchestratorType) {
    this.orchestratorType = orchestratorType;
  }


  public OrchestratorProfile orchestratorVersion(String orchestratorVersion) {
    this.orchestratorVersion = orchestratorVersion;
    return this;
  }

  /**
   * Orchestrator version (major, minor, patch).
   * @return orchestratorVersion
   */
  @javax.annotation.Nonnull
  public String getOrchestratorVersion() {
    return orchestratorVersion;
  }

  public void setOrchestratorVersion(String orchestratorVersion) {
    this.orchestratorVersion = orchestratorVersion;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrchestratorProfile orchestratorProfile = (OrchestratorProfile) o;
    return Objects.equals(this.isPreview, orchestratorProfile.isPreview) &&
        Objects.equals(this.orchestratorType, orchestratorProfile.orchestratorType) &&
        Objects.equals(this.orchestratorVersion, orchestratorProfile.orchestratorVersion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isPreview, orchestratorType, orchestratorVersion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrchestratorProfile {\n");
    sb.append("    isPreview: ").append(toIndentedString(isPreview)).append("\n");
    sb.append("    orchestratorType: ").append(toIndentedString(orchestratorType)).append("\n");
    sb.append("    orchestratorVersion: ").append(toIndentedString(orchestratorVersion)).append("\n");
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
    openapiFields.add("isPreview");
    openapiFields.add("orchestratorType");
    openapiFields.add("orchestratorVersion");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("orchestratorVersion");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrchestratorProfile
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrchestratorProfile.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrchestratorProfile is not found in the empty JSON string", OrchestratorProfile.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrchestratorProfile.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrchestratorProfile` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrchestratorProfile.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("orchestratorType") != null && !jsonObj.get("orchestratorType").isJsonNull()) && !jsonObj.get("orchestratorType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orchestratorType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orchestratorType").toString()));
      }
      if (!jsonObj.get("orchestratorVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `orchestratorVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("orchestratorVersion").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrchestratorProfile.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrchestratorProfile' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrchestratorProfile> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrchestratorProfile.class));

       return (TypeAdapter<T>) new TypeAdapter<OrchestratorProfile>() {
           @Override
           public void write(JsonWriter out, OrchestratorProfile value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrchestratorProfile read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrchestratorProfile given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrchestratorProfile
   * @throws IOException if the JSON string is invalid with respect to OrchestratorProfile
   */
  public static OrchestratorProfile fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrchestratorProfile.class);
  }

  /**
   * Convert an instance of OrchestratorProfile to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

