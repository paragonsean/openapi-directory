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
 * Build configuration when React Native, or other JavaScript tech, is part of the build steps
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class JavaScriptBranchConfigurationProperties {
  public static final String SERIALIZED_NAME_PACKAGE_JSON_PATH = "packageJsonPath";
  @SerializedName(SERIALIZED_NAME_PACKAGE_JSON_PATH)
  private String packageJsonPath;

  public static final String SERIALIZED_NAME_REACT_NATIVE_VERSION = "reactNativeVersion";
  @SerializedName(SERIALIZED_NAME_REACT_NATIVE_VERSION)
  private String reactNativeVersion;

  public static final String SERIALIZED_NAME_RUN_TESTS = "runTests";
  @SerializedName(SERIALIZED_NAME_RUN_TESTS)
  private Boolean runTests;

  public JavaScriptBranchConfigurationProperties() {
  }

  public JavaScriptBranchConfigurationProperties packageJsonPath(String packageJsonPath) {
    this.packageJsonPath = packageJsonPath;
    return this;
  }

  /**
   * Path to package.json file for the main project, e.g. \&quot;package.json\&quot; or \&quot;myapp/package.json\&quot;
   * @return packageJsonPath
   */
  @javax.annotation.Nullable
  public String getPackageJsonPath() {
    return packageJsonPath;
  }

  public void setPackageJsonPath(String packageJsonPath) {
    this.packageJsonPath = packageJsonPath;
  }


  public JavaScriptBranchConfigurationProperties reactNativeVersion(String reactNativeVersion) {
    this.reactNativeVersion = reactNativeVersion;
    return this;
  }

  /**
   * Version of React Native from package.json files
   * @return reactNativeVersion
   */
  @javax.annotation.Nullable
  public String getReactNativeVersion() {
    return reactNativeVersion;
  }

  public void setReactNativeVersion(String reactNativeVersion) {
    this.reactNativeVersion = reactNativeVersion;
  }


  public JavaScriptBranchConfigurationProperties runTests(Boolean runTests) {
    this.runTests = runTests;
    return this;
  }

  /**
   * Whether to run Jest unit tests, via npm test, during the build
   * @return runTests
   */
  @javax.annotation.Nullable
  public Boolean getRunTests() {
    return runTests;
  }

  public void setRunTests(Boolean runTests) {
    this.runTests = runTests;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    JavaScriptBranchConfigurationProperties javaScriptBranchConfigurationProperties = (JavaScriptBranchConfigurationProperties) o;
    return Objects.equals(this.packageJsonPath, javaScriptBranchConfigurationProperties.packageJsonPath) &&
        Objects.equals(this.reactNativeVersion, javaScriptBranchConfigurationProperties.reactNativeVersion) &&
        Objects.equals(this.runTests, javaScriptBranchConfigurationProperties.runTests);
  }

  @Override
  public int hashCode() {
    return Objects.hash(packageJsonPath, reactNativeVersion, runTests);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class JavaScriptBranchConfigurationProperties {\n");
    sb.append("    packageJsonPath: ").append(toIndentedString(packageJsonPath)).append("\n");
    sb.append("    reactNativeVersion: ").append(toIndentedString(reactNativeVersion)).append("\n");
    sb.append("    runTests: ").append(toIndentedString(runTests)).append("\n");
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
    openapiFields.add("packageJsonPath");
    openapiFields.add("reactNativeVersion");
    openapiFields.add("runTests");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to JavaScriptBranchConfigurationProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!JavaScriptBranchConfigurationProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in JavaScriptBranchConfigurationProperties is not found in the empty JSON string", JavaScriptBranchConfigurationProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!JavaScriptBranchConfigurationProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `JavaScriptBranchConfigurationProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("packageJsonPath") != null && !jsonObj.get("packageJsonPath").isJsonNull()) && !jsonObj.get("packageJsonPath").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `packageJsonPath` to be a primitive type in the JSON string but got `%s`", jsonObj.get("packageJsonPath").toString()));
      }
      if ((jsonObj.get("reactNativeVersion") != null && !jsonObj.get("reactNativeVersion").isJsonNull()) && !jsonObj.get("reactNativeVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reactNativeVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reactNativeVersion").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!JavaScriptBranchConfigurationProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'JavaScriptBranchConfigurationProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<JavaScriptBranchConfigurationProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(JavaScriptBranchConfigurationProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<JavaScriptBranchConfigurationProperties>() {
           @Override
           public void write(JsonWriter out, JavaScriptBranchConfigurationProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public JavaScriptBranchConfigurationProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of JavaScriptBranchConfigurationProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of JavaScriptBranchConfigurationProperties
   * @throws IOException if the JSON string is invalid with respect to JavaScriptBranchConfigurationProperties
   */
  public static JavaScriptBranchConfigurationProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, JavaScriptBranchConfigurationProperties.class);
  }

  /**
   * Convert an instance of JavaScriptBranchConfigurationProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

