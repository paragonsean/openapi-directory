/*
 * ResourceHealthMetadata API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ResourceHealthMetadataListDefaultResponseErrorDetailsInner;

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
 * Error model.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:44.028548-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ResourceHealthMetadataListDefaultResponseError {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private List<ResourceHealthMetadataListDefaultResponseErrorDetailsInner> details = new ArrayList<>();

  public static final String SERIALIZED_NAME_INNERERROR = "innererror";
  @SerializedName(SERIALIZED_NAME_INNERERROR)
  private String innererror;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public ResourceHealthMetadataListDefaultResponseError() {
  }

  public ResourceHealthMetadataListDefaultResponseError(
     String code, 
     String innererror, 
     String message, 
     String target
  ) {
    this();
    this.code = code;
    this.innererror = innererror;
    this.message = message;
    this.target = target;
  }

  /**
   * Standardized string to programmatically identify the error.
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }



  public ResourceHealthMetadataListDefaultResponseError details(List<ResourceHealthMetadataListDefaultResponseErrorDetailsInner> details) {
    this.details = details;
    return this;
  }

  public ResourceHealthMetadataListDefaultResponseError addDetailsItem(ResourceHealthMetadataListDefaultResponseErrorDetailsInner detailsItem) {
    if (this.details == null) {
      this.details = new ArrayList<>();
    }
    this.details.add(detailsItem);
    return this;
  }

  /**
   * Get details
   * @return details
   */
  @javax.annotation.Nullable
  public List<ResourceHealthMetadataListDefaultResponseErrorDetailsInner> getDetails() {
    return details;
  }

  public void setDetails(List<ResourceHealthMetadataListDefaultResponseErrorDetailsInner> details) {
    this.details = details;
  }


  /**
   * More information to debug error.
   * @return innererror
   */
  @javax.annotation.Nullable
  public String getInnererror() {
    return innererror;
  }



  /**
   * Detailed error description and debugging information.
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }



  /**
   * Detailed error description and debugging information.
   * @return target
   */
  @javax.annotation.Nullable
  public String getTarget() {
    return target;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ResourceHealthMetadataListDefaultResponseError resourceHealthMetadataListDefaultResponseError = (ResourceHealthMetadataListDefaultResponseError) o;
    return Objects.equals(this.code, resourceHealthMetadataListDefaultResponseError.code) &&
        Objects.equals(this.details, resourceHealthMetadataListDefaultResponseError.details) &&
        Objects.equals(this.innererror, resourceHealthMetadataListDefaultResponseError.innererror) &&
        Objects.equals(this.message, resourceHealthMetadataListDefaultResponseError.message) &&
        Objects.equals(this.target, resourceHealthMetadataListDefaultResponseError.target);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, details, innererror, message, target);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ResourceHealthMetadataListDefaultResponseError {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
    sb.append("    innererror: ").append(toIndentedString(innererror)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("details");
    openapiFields.add("innererror");
    openapiFields.add("message");
    openapiFields.add("target");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ResourceHealthMetadataListDefaultResponseError
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ResourceHealthMetadataListDefaultResponseError.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ResourceHealthMetadataListDefaultResponseError is not found in the empty JSON string", ResourceHealthMetadataListDefaultResponseError.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ResourceHealthMetadataListDefaultResponseError.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ResourceHealthMetadataListDefaultResponseError` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if (jsonObj.get("details") != null && !jsonObj.get("details").isJsonNull()) {
        JsonArray jsonArraydetails = jsonObj.getAsJsonArray("details");
        if (jsonArraydetails != null) {
          // ensure the json data is an array
          if (!jsonObj.get("details").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `details` to be an array in the JSON string but got `%s`", jsonObj.get("details").toString()));
          }

          // validate the optional field `details` (array)
          for (int i = 0; i < jsonArraydetails.size(); i++) {
            ResourceHealthMetadataListDefaultResponseErrorDetailsInner.validateJsonElement(jsonArraydetails.get(i));
          };
        }
      }
      if ((jsonObj.get("innererror") != null && !jsonObj.get("innererror").isJsonNull()) && !jsonObj.get("innererror").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `innererror` to be a primitive type in the JSON string but got `%s`", jsonObj.get("innererror").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("target") != null && !jsonObj.get("target").isJsonNull()) && !jsonObj.get("target").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `target` to be a primitive type in the JSON string but got `%s`", jsonObj.get("target").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ResourceHealthMetadataListDefaultResponseError.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ResourceHealthMetadataListDefaultResponseError' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ResourceHealthMetadataListDefaultResponseError> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ResourceHealthMetadataListDefaultResponseError.class));

       return (TypeAdapter<T>) new TypeAdapter<ResourceHealthMetadataListDefaultResponseError>() {
           @Override
           public void write(JsonWriter out, ResourceHealthMetadataListDefaultResponseError value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ResourceHealthMetadataListDefaultResponseError read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ResourceHealthMetadataListDefaultResponseError given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ResourceHealthMetadataListDefaultResponseError
   * @throws IOException if the JSON string is invalid with respect to ResourceHealthMetadataListDefaultResponseError
   */
  public static ResourceHealthMetadataListDefaultResponseError fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ResourceHealthMetadataListDefaultResponseError.class);
  }

  /**
   * Convert an instance of ResourceHealthMetadataListDefaultResponseError to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

