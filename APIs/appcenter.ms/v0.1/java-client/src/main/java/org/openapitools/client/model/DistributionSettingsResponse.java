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
 * DistributionSettingsResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DistributionSettingsResponse {
  public static final String SERIALIZED_NAME_DEFAULT_PUBLIC = "default_public";
  @SerializedName(SERIALIZED_NAME_DEFAULT_PUBLIC)
  private Boolean defaultPublic;

  public DistributionSettingsResponse() {
  }

  public DistributionSettingsResponse defaultPublic(Boolean defaultPublic) {
    this.defaultPublic = defaultPublic;
    return this;
  }

  /**
   * Is this app using the \&quot;Default to Public Distribution Groups\&quot; logic
   * @return defaultPublic
   */
  @javax.annotation.Nonnull
  public Boolean getDefaultPublic() {
    return defaultPublic;
  }

  public void setDefaultPublic(Boolean defaultPublic) {
    this.defaultPublic = defaultPublic;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DistributionSettingsResponse distributionSettingsResponse = (DistributionSettingsResponse) o;
    return Objects.equals(this.defaultPublic, distributionSettingsResponse.defaultPublic);
  }

  @Override
  public int hashCode() {
    return Objects.hash(defaultPublic);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DistributionSettingsResponse {\n");
    sb.append("    defaultPublic: ").append(toIndentedString(defaultPublic)).append("\n");
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
    openapiFields.add("default_public");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("default_public");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DistributionSettingsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DistributionSettingsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DistributionSettingsResponse is not found in the empty JSON string", DistributionSettingsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DistributionSettingsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DistributionSettingsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DistributionSettingsResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DistributionSettingsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DistributionSettingsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DistributionSettingsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DistributionSettingsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<DistributionSettingsResponse>() {
           @Override
           public void write(JsonWriter out, DistributionSettingsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DistributionSettingsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DistributionSettingsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DistributionSettingsResponse
   * @throws IOException if the JSON string is invalid with respect to DistributionSettingsResponse
   */
  public static DistributionSettingsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DistributionSettingsResponse.class);
  }

  /**
   * Convert an instance of DistributionSettingsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

