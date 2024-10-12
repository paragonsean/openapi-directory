/*
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
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
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

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
 * IotBaseModuleSettings
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:35:04.030214-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IotBaseModuleSettings {
  public static final String SERIALIZED_NAME_CREATE_OPTIONS = "createOptions";
  @SerializedName(SERIALIZED_NAME_CREATE_OPTIONS)
  private String createOptions;

  public static final String SERIALIZED_NAME_ENVIRONMENT_VARIABLES = "environmentVariables";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_VARIABLES)
  private Map<String, String> environmentVariables = new HashMap<>();

  public static final String SERIALIZED_NAME_MODULE_NAME = "moduleName";
  @SerializedName(SERIALIZED_NAME_MODULE_NAME)
  private String moduleName;

  public static final String SERIALIZED_NAME_PROPERTIES_DESIRED = "propertiesDesired";
  @SerializedName(SERIALIZED_NAME_PROPERTIES_DESIRED)
  private Map<String, String> propertiesDesired = new HashMap<>();

  public IotBaseModuleSettings() {
  }

  public IotBaseModuleSettings createOptions(String createOptions) {
    this.createOptions = createOptions;
    return this;
  }

  /**
   * Get createOptions
   * @return createOptions
   */
  @javax.annotation.Nullable
  public String getCreateOptions() {
    return createOptions;
  }

  public void setCreateOptions(String createOptions) {
    this.createOptions = createOptions;
  }


  public IotBaseModuleSettings environmentVariables(Map<String, String> environmentVariables) {
    this.environmentVariables = environmentVariables;
    return this;
  }

  public IotBaseModuleSettings putEnvironmentVariablesItem(String key, String environmentVariablesItem) {
    if (this.environmentVariables == null) {
      this.environmentVariables = new HashMap<>();
    }
    this.environmentVariables.put(key, environmentVariablesItem);
    return this;
  }

  /**
   * Get environmentVariables
   * @return environmentVariables
   */
  @javax.annotation.Nullable
  public Map<String, String> getEnvironmentVariables() {
    return environmentVariables;
  }

  public void setEnvironmentVariables(Map<String, String> environmentVariables) {
    this.environmentVariables = environmentVariables;
  }


  public IotBaseModuleSettings moduleName(String moduleName) {
    this.moduleName = moduleName;
    return this;
  }

  /**
   * Get moduleName
   * @return moduleName
   */
  @javax.annotation.Nullable
  public String getModuleName() {
    return moduleName;
  }

  public void setModuleName(String moduleName) {
    this.moduleName = moduleName;
  }


  public IotBaseModuleSettings propertiesDesired(Map<String, String> propertiesDesired) {
    this.propertiesDesired = propertiesDesired;
    return this;
  }

  public IotBaseModuleSettings putPropertiesDesiredItem(String key, String propertiesDesiredItem) {
    if (this.propertiesDesired == null) {
      this.propertiesDesired = new HashMap<>();
    }
    this.propertiesDesired.put(key, propertiesDesiredItem);
    return this;
  }

  /**
   * Get propertiesDesired
   * @return propertiesDesired
   */
  @javax.annotation.Nullable
  public Map<String, String> getPropertiesDesired() {
    return propertiesDesired;
  }

  public void setPropertiesDesired(Map<String, String> propertiesDesired) {
    this.propertiesDesired = propertiesDesired;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IotBaseModuleSettings iotBaseModuleSettings = (IotBaseModuleSettings) o;
    return Objects.equals(this.createOptions, iotBaseModuleSettings.createOptions) &&
        Objects.equals(this.environmentVariables, iotBaseModuleSettings.environmentVariables) &&
        Objects.equals(this.moduleName, iotBaseModuleSettings.moduleName) &&
        Objects.equals(this.propertiesDesired, iotBaseModuleSettings.propertiesDesired);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createOptions, environmentVariables, moduleName, propertiesDesired);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IotBaseModuleSettings {\n");
    sb.append("    createOptions: ").append(toIndentedString(createOptions)).append("\n");
    sb.append("    environmentVariables: ").append(toIndentedString(environmentVariables)).append("\n");
    sb.append("    moduleName: ").append(toIndentedString(moduleName)).append("\n");
    sb.append("    propertiesDesired: ").append(toIndentedString(propertiesDesired)).append("\n");
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
    openapiFields.add("createOptions");
    openapiFields.add("environmentVariables");
    openapiFields.add("moduleName");
    openapiFields.add("propertiesDesired");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IotBaseModuleSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IotBaseModuleSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IotBaseModuleSettings is not found in the empty JSON string", IotBaseModuleSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IotBaseModuleSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IotBaseModuleSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("createOptions") != null && !jsonObj.get("createOptions").isJsonNull()) && !jsonObj.get("createOptions").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `createOptions` to be a primitive type in the JSON string but got `%s`", jsonObj.get("createOptions").toString()));
      }
      if ((jsonObj.get("moduleName") != null && !jsonObj.get("moduleName").isJsonNull()) && !jsonObj.get("moduleName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moduleName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moduleName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IotBaseModuleSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IotBaseModuleSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IotBaseModuleSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IotBaseModuleSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<IotBaseModuleSettings>() {
           @Override
           public void write(JsonWriter out, IotBaseModuleSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IotBaseModuleSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IotBaseModuleSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IotBaseModuleSettings
   * @throws IOException if the JSON string is invalid with respect to IotBaseModuleSettings
   */
  public static IotBaseModuleSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IotBaseModuleSettings.class);
  }

  /**
   * Convert an instance of IotBaseModuleSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

