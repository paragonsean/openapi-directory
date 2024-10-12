/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
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
 * Error Field contract.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:18.645826-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IdentityProviderListByServiceDefaultResponseDetailsInner {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public IdentityProviderListByServiceDefaultResponseDetailsInner() {
  }

  public IdentityProviderListByServiceDefaultResponseDetailsInner code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Property level error code.
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public IdentityProviderListByServiceDefaultResponseDetailsInner message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Human-readable representation of property-level error.
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public IdentityProviderListByServiceDefaultResponseDetailsInner target(String target) {
    this.target = target;
    return this;
  }

  /**
   * Property name.
   * @return target
   */
  @javax.annotation.Nullable
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IdentityProviderListByServiceDefaultResponseDetailsInner identityProviderListByServiceDefaultResponseDetailsInner = (IdentityProviderListByServiceDefaultResponseDetailsInner) o;
    return Objects.equals(this.code, identityProviderListByServiceDefaultResponseDetailsInner.code) &&
        Objects.equals(this.message, identityProviderListByServiceDefaultResponseDetailsInner.message) &&
        Objects.equals(this.target, identityProviderListByServiceDefaultResponseDetailsInner.target);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, message, target);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IdentityProviderListByServiceDefaultResponseDetailsInner {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
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
    openapiFields.add("message");
    openapiFields.add("target");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IdentityProviderListByServiceDefaultResponseDetailsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IdentityProviderListByServiceDefaultResponseDetailsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IdentityProviderListByServiceDefaultResponseDetailsInner is not found in the empty JSON string", IdentityProviderListByServiceDefaultResponseDetailsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IdentityProviderListByServiceDefaultResponseDetailsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IdentityProviderListByServiceDefaultResponseDetailsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
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
       if (!IdentityProviderListByServiceDefaultResponseDetailsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IdentityProviderListByServiceDefaultResponseDetailsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IdentityProviderListByServiceDefaultResponseDetailsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IdentityProviderListByServiceDefaultResponseDetailsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<IdentityProviderListByServiceDefaultResponseDetailsInner>() {
           @Override
           public void write(JsonWriter out, IdentityProviderListByServiceDefaultResponseDetailsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IdentityProviderListByServiceDefaultResponseDetailsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IdentityProviderListByServiceDefaultResponseDetailsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IdentityProviderListByServiceDefaultResponseDetailsInner
   * @throws IOException if the JSON string is invalid with respect to IdentityProviderListByServiceDefaultResponseDetailsInner
   */
  public static IdentityProviderListByServiceDefaultResponseDetailsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IdentityProviderListByServiceDefaultResponseDetailsInner.class);
  }

  /**
   * Convert an instance of IdentityProviderListByServiceDefaultResponseDetailsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

