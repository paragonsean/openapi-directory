/*
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
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
 * Describes a script action on a running cluster.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:19:25.528717-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApplicationPropertiesInstallScriptActionsInner {
  public static final String SERIALIZED_NAME_APPLICATION_NAME = "applicationName";
  @SerializedName(SERIALIZED_NAME_APPLICATION_NAME)
  private String applicationName;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PARAMETERS = "parameters";
  @SerializedName(SERIALIZED_NAME_PARAMETERS)
  private String parameters;

  public static final String SERIALIZED_NAME_ROLES = "roles";
  @SerializedName(SERIALIZED_NAME_ROLES)
  private List<String> roles = new ArrayList<>();

  public static final String SERIALIZED_NAME_URI = "uri";
  @SerializedName(SERIALIZED_NAME_URI)
  private String uri;

  public ApplicationPropertiesInstallScriptActionsInner() {
  }

  public ApplicationPropertiesInstallScriptActionsInner(
     String applicationName
  ) {
    this();
    this.applicationName = applicationName;
  }

  /**
   * The application name of the script action, if any.
   * @return applicationName
   */
  @javax.annotation.Nullable
  public String getApplicationName() {
    return applicationName;
  }



  public ApplicationPropertiesInstallScriptActionsInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the script action.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ApplicationPropertiesInstallScriptActionsInner parameters(String parameters) {
    this.parameters = parameters;
    return this;
  }

  /**
   * The parameters for the script
   * @return parameters
   */
  @javax.annotation.Nullable
  public String getParameters() {
    return parameters;
  }

  public void setParameters(String parameters) {
    this.parameters = parameters;
  }


  public ApplicationPropertiesInstallScriptActionsInner roles(List<String> roles) {
    this.roles = roles;
    return this;
  }

  public ApplicationPropertiesInstallScriptActionsInner addRolesItem(String rolesItem) {
    if (this.roles == null) {
      this.roles = new ArrayList<>();
    }
    this.roles.add(rolesItem);
    return this;
  }

  /**
   * The list of roles where script will be executed.
   * @return roles
   */
  @javax.annotation.Nonnull
  public List<String> getRoles() {
    return roles;
  }

  public void setRoles(List<String> roles) {
    this.roles = roles;
  }


  public ApplicationPropertiesInstallScriptActionsInner uri(String uri) {
    this.uri = uri;
    return this;
  }

  /**
   * The URI to the script.
   * @return uri
   */
  @javax.annotation.Nonnull
  public String getUri() {
    return uri;
  }

  public void setUri(String uri) {
    this.uri = uri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApplicationPropertiesInstallScriptActionsInner applicationPropertiesInstallScriptActionsInner = (ApplicationPropertiesInstallScriptActionsInner) o;
    return Objects.equals(this.applicationName, applicationPropertiesInstallScriptActionsInner.applicationName) &&
        Objects.equals(this.name, applicationPropertiesInstallScriptActionsInner.name) &&
        Objects.equals(this.parameters, applicationPropertiesInstallScriptActionsInner.parameters) &&
        Objects.equals(this.roles, applicationPropertiesInstallScriptActionsInner.roles) &&
        Objects.equals(this.uri, applicationPropertiesInstallScriptActionsInner.uri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(applicationName, name, parameters, roles, uri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApplicationPropertiesInstallScriptActionsInner {\n");
    sb.append("    applicationName: ").append(toIndentedString(applicationName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    parameters: ").append(toIndentedString(parameters)).append("\n");
    sb.append("    roles: ").append(toIndentedString(roles)).append("\n");
    sb.append("    uri: ").append(toIndentedString(uri)).append("\n");
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
    openapiFields.add("applicationName");
    openapiFields.add("name");
    openapiFields.add("parameters");
    openapiFields.add("roles");
    openapiFields.add("uri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("roles");
    openapiRequiredFields.add("uri");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApplicationPropertiesInstallScriptActionsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApplicationPropertiesInstallScriptActionsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApplicationPropertiesInstallScriptActionsInner is not found in the empty JSON string", ApplicationPropertiesInstallScriptActionsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApplicationPropertiesInstallScriptActionsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApplicationPropertiesInstallScriptActionsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ApplicationPropertiesInstallScriptActionsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("applicationName") != null && !jsonObj.get("applicationName").isJsonNull()) && !jsonObj.get("applicationName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `applicationName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("applicationName").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("parameters") != null && !jsonObj.get("parameters").isJsonNull()) && !jsonObj.get("parameters").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parameters` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parameters").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("roles") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("roles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `roles` to be an array in the JSON string but got `%s`", jsonObj.get("roles").toString()));
      }
      if (!jsonObj.get("uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApplicationPropertiesInstallScriptActionsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApplicationPropertiesInstallScriptActionsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApplicationPropertiesInstallScriptActionsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApplicationPropertiesInstallScriptActionsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ApplicationPropertiesInstallScriptActionsInner>() {
           @Override
           public void write(JsonWriter out, ApplicationPropertiesInstallScriptActionsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApplicationPropertiesInstallScriptActionsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApplicationPropertiesInstallScriptActionsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApplicationPropertiesInstallScriptActionsInner
   * @throws IOException if the JSON string is invalid with respect to ApplicationPropertiesInstallScriptActionsInner
   */
  public static ApplicationPropertiesInstallScriptActionsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApplicationPropertiesInstallScriptActionsInner.class);
  }

  /**
   * Convert an instance of ApplicationPropertiesInstallScriptActionsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

