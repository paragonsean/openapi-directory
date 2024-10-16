/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
import org.openapitools.client.model.AuthenticationExecutionExportRepresentation;

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
 * AuthenticationFlowRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AuthenticationFlowRepresentation {
  public static final String SERIALIZED_NAME_ALIAS = "alias";
  @SerializedName(SERIALIZED_NAME_ALIAS)
  private String alias;

  public static final String SERIALIZED_NAME_AUTHENTICATION_EXECUTIONS = "authenticationExecutions";
  @SerializedName(SERIALIZED_NAME_AUTHENTICATION_EXECUTIONS)
  private List<AuthenticationExecutionExportRepresentation> authenticationExecutions = new ArrayList<>();

  public static final String SERIALIZED_NAME_BUILT_IN = "builtIn";
  @SerializedName(SERIALIZED_NAME_BUILT_IN)
  private Boolean builtIn;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PROVIDER_ID = "providerId";
  @SerializedName(SERIALIZED_NAME_PROVIDER_ID)
  private String providerId;

  public static final String SERIALIZED_NAME_TOP_LEVEL = "topLevel";
  @SerializedName(SERIALIZED_NAME_TOP_LEVEL)
  private Boolean topLevel;

  public AuthenticationFlowRepresentation() {
  }

  public AuthenticationFlowRepresentation alias(String alias) {
    this.alias = alias;
    return this;
  }

  /**
   * Get alias
   * @return alias
   */
  @javax.annotation.Nullable
  public String getAlias() {
    return alias;
  }

  public void setAlias(String alias) {
    this.alias = alias;
  }


  public AuthenticationFlowRepresentation authenticationExecutions(List<AuthenticationExecutionExportRepresentation> authenticationExecutions) {
    this.authenticationExecutions = authenticationExecutions;
    return this;
  }

  public AuthenticationFlowRepresentation addAuthenticationExecutionsItem(AuthenticationExecutionExportRepresentation authenticationExecutionsItem) {
    if (this.authenticationExecutions == null) {
      this.authenticationExecutions = new ArrayList<>();
    }
    this.authenticationExecutions.add(authenticationExecutionsItem);
    return this;
  }

  /**
   * Get authenticationExecutions
   * @return authenticationExecutions
   */
  @javax.annotation.Nullable
  public List<AuthenticationExecutionExportRepresentation> getAuthenticationExecutions() {
    return authenticationExecutions;
  }

  public void setAuthenticationExecutions(List<AuthenticationExecutionExportRepresentation> authenticationExecutions) {
    this.authenticationExecutions = authenticationExecutions;
  }


  public AuthenticationFlowRepresentation builtIn(Boolean builtIn) {
    this.builtIn = builtIn;
    return this;
  }

  /**
   * Get builtIn
   * @return builtIn
   */
  @javax.annotation.Nullable
  public Boolean getBuiltIn() {
    return builtIn;
  }

  public void setBuiltIn(Boolean builtIn) {
    this.builtIn = builtIn;
  }


  public AuthenticationFlowRepresentation description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AuthenticationFlowRepresentation id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public AuthenticationFlowRepresentation providerId(String providerId) {
    this.providerId = providerId;
    return this;
  }

  /**
   * Get providerId
   * @return providerId
   */
  @javax.annotation.Nullable
  public String getProviderId() {
    return providerId;
  }

  public void setProviderId(String providerId) {
    this.providerId = providerId;
  }


  public AuthenticationFlowRepresentation topLevel(Boolean topLevel) {
    this.topLevel = topLevel;
    return this;
  }

  /**
   * Get topLevel
   * @return topLevel
   */
  @javax.annotation.Nullable
  public Boolean getTopLevel() {
    return topLevel;
  }

  public void setTopLevel(Boolean topLevel) {
    this.topLevel = topLevel;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuthenticationFlowRepresentation authenticationFlowRepresentation = (AuthenticationFlowRepresentation) o;
    return Objects.equals(this.alias, authenticationFlowRepresentation.alias) &&
        Objects.equals(this.authenticationExecutions, authenticationFlowRepresentation.authenticationExecutions) &&
        Objects.equals(this.builtIn, authenticationFlowRepresentation.builtIn) &&
        Objects.equals(this.description, authenticationFlowRepresentation.description) &&
        Objects.equals(this.id, authenticationFlowRepresentation.id) &&
        Objects.equals(this.providerId, authenticationFlowRepresentation.providerId) &&
        Objects.equals(this.topLevel, authenticationFlowRepresentation.topLevel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alias, authenticationExecutions, builtIn, description, id, providerId, topLevel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuthenticationFlowRepresentation {\n");
    sb.append("    alias: ").append(toIndentedString(alias)).append("\n");
    sb.append("    authenticationExecutions: ").append(toIndentedString(authenticationExecutions)).append("\n");
    sb.append("    builtIn: ").append(toIndentedString(builtIn)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    providerId: ").append(toIndentedString(providerId)).append("\n");
    sb.append("    topLevel: ").append(toIndentedString(topLevel)).append("\n");
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
    openapiFields.add("alias");
    openapiFields.add("authenticationExecutions");
    openapiFields.add("builtIn");
    openapiFields.add("description");
    openapiFields.add("id");
    openapiFields.add("providerId");
    openapiFields.add("topLevel");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AuthenticationFlowRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AuthenticationFlowRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AuthenticationFlowRepresentation is not found in the empty JSON string", AuthenticationFlowRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AuthenticationFlowRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AuthenticationFlowRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alias") != null && !jsonObj.get("alias").isJsonNull()) && !jsonObj.get("alias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alias").toString()));
      }
      if (jsonObj.get("authenticationExecutions") != null && !jsonObj.get("authenticationExecutions").isJsonNull()) {
        JsonArray jsonArrayauthenticationExecutions = jsonObj.getAsJsonArray("authenticationExecutions");
        if (jsonArrayauthenticationExecutions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("authenticationExecutions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `authenticationExecutions` to be an array in the JSON string but got `%s`", jsonObj.get("authenticationExecutions").toString()));
          }

          // validate the optional field `authenticationExecutions` (array)
          for (int i = 0; i < jsonArrayauthenticationExecutions.size(); i++) {
            AuthenticationExecutionExportRepresentation.validateJsonElement(jsonArrayauthenticationExecutions.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("providerId") != null && !jsonObj.get("providerId").isJsonNull()) && !jsonObj.get("providerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `providerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("providerId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AuthenticationFlowRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AuthenticationFlowRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AuthenticationFlowRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AuthenticationFlowRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<AuthenticationFlowRepresentation>() {
           @Override
           public void write(JsonWriter out, AuthenticationFlowRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AuthenticationFlowRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AuthenticationFlowRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AuthenticationFlowRepresentation
   * @throws IOException if the JSON string is invalid with respect to AuthenticationFlowRepresentation
   */
  public static AuthenticationFlowRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AuthenticationFlowRepresentation.class);
  }

  /**
   * Convert an instance of AuthenticationFlowRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

