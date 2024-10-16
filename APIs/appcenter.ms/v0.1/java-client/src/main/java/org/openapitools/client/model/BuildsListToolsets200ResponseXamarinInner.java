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
 * The Xamarin SDK bundle
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BuildsListToolsets200ResponseXamarinInner {
  public static final String SERIALIZED_NAME_CURRENT = "current";
  @SerializedName(SERIALIZED_NAME_CURRENT)
  private Boolean current;

  public static final String SERIALIZED_NAME_MONO_VERSION = "monoVersion";
  @SerializedName(SERIALIZED_NAME_MONO_VERSION)
  private String monoVersion;

  public static final String SERIALIZED_NAME_SDK_BUNDLE = "sdkBundle";
  @SerializedName(SERIALIZED_NAME_SDK_BUNDLE)
  private String sdkBundle;

  public static final String SERIALIZED_NAME_STABLE = "stable";
  @SerializedName(SERIALIZED_NAME_STABLE)
  private Boolean stable;

  public static final String SERIALIZED_NAME_XCODE_VERSIONS = "xcodeVersions";
  @SerializedName(SERIALIZED_NAME_XCODE_VERSIONS)
  private List<String> xcodeVersions = new ArrayList<>();

  public BuildsListToolsets200ResponseXamarinInner() {
  }

  public BuildsListToolsets200ResponseXamarinInner current(Boolean current) {
    this.current = current;
    return this;
  }

  /**
   * If the SDK is latest stable
   * @return current
   */
  @javax.annotation.Nullable
  public Boolean getCurrent() {
    return current;
  }

  public void setCurrent(Boolean current) {
    this.current = current;
  }


  public BuildsListToolsets200ResponseXamarinInner monoVersion(String monoVersion) {
    this.monoVersion = monoVersion;
    return this;
  }

  /**
   * The Mono version
   * @return monoVersion
   */
  @javax.annotation.Nullable
  public String getMonoVersion() {
    return monoVersion;
  }

  public void setMonoVersion(String monoVersion) {
    this.monoVersion = monoVersion;
  }


  public BuildsListToolsets200ResponseXamarinInner sdkBundle(String sdkBundle) {
    this.sdkBundle = sdkBundle;
    return this;
  }

  /**
   * The Xamarin SDK version
   * @return sdkBundle
   */
  @javax.annotation.Nullable
  public String getSdkBundle() {
    return sdkBundle;
  }

  public void setSdkBundle(String sdkBundle) {
    this.sdkBundle = sdkBundle;
  }


  public BuildsListToolsets200ResponseXamarinInner stable(Boolean stable) {
    this.stable = stable;
    return this;
  }

  /**
   * If the SDK is stable
   * @return stable
   */
  @javax.annotation.Nullable
  public Boolean getStable() {
    return stable;
  }

  public void setStable(Boolean stable) {
    this.stable = stable;
  }


  public BuildsListToolsets200ResponseXamarinInner xcodeVersions(List<String> xcodeVersions) {
    this.xcodeVersions = xcodeVersions;
    return this;
  }

  public BuildsListToolsets200ResponseXamarinInner addXcodeVersionsItem(String xcodeVersionsItem) {
    if (this.xcodeVersions == null) {
      this.xcodeVersions = new ArrayList<>();
    }
    this.xcodeVersions.add(xcodeVersionsItem);
    return this;
  }

  /**
   * Specific for iOS SDK. A list of Xcode versions supported by current SDK version
   * @return xcodeVersions
   */
  @javax.annotation.Nullable
  public List<String> getXcodeVersions() {
    return xcodeVersions;
  }

  public void setXcodeVersions(List<String> xcodeVersions) {
    this.xcodeVersions = xcodeVersions;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BuildsListToolsets200ResponseXamarinInner buildsListToolsets200ResponseXamarinInner = (BuildsListToolsets200ResponseXamarinInner) o;
    return Objects.equals(this.current, buildsListToolsets200ResponseXamarinInner.current) &&
        Objects.equals(this.monoVersion, buildsListToolsets200ResponseXamarinInner.monoVersion) &&
        Objects.equals(this.sdkBundle, buildsListToolsets200ResponseXamarinInner.sdkBundle) &&
        Objects.equals(this.stable, buildsListToolsets200ResponseXamarinInner.stable) &&
        Objects.equals(this.xcodeVersions, buildsListToolsets200ResponseXamarinInner.xcodeVersions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(current, monoVersion, sdkBundle, stable, xcodeVersions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BuildsListToolsets200ResponseXamarinInner {\n");
    sb.append("    current: ").append(toIndentedString(current)).append("\n");
    sb.append("    monoVersion: ").append(toIndentedString(monoVersion)).append("\n");
    sb.append("    sdkBundle: ").append(toIndentedString(sdkBundle)).append("\n");
    sb.append("    stable: ").append(toIndentedString(stable)).append("\n");
    sb.append("    xcodeVersions: ").append(toIndentedString(xcodeVersions)).append("\n");
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
    openapiFields.add("current");
    openapiFields.add("monoVersion");
    openapiFields.add("sdkBundle");
    openapiFields.add("stable");
    openapiFields.add("xcodeVersions");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BuildsListToolsets200ResponseXamarinInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BuildsListToolsets200ResponseXamarinInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BuildsListToolsets200ResponseXamarinInner is not found in the empty JSON string", BuildsListToolsets200ResponseXamarinInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BuildsListToolsets200ResponseXamarinInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BuildsListToolsets200ResponseXamarinInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("monoVersion") != null && !jsonObj.get("monoVersion").isJsonNull()) && !jsonObj.get("monoVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `monoVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("monoVersion").toString()));
      }
      if ((jsonObj.get("sdkBundle") != null && !jsonObj.get("sdkBundle").isJsonNull()) && !jsonObj.get("sdkBundle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sdkBundle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sdkBundle").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("xcodeVersions") != null && !jsonObj.get("xcodeVersions").isJsonNull() && !jsonObj.get("xcodeVersions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `xcodeVersions` to be an array in the JSON string but got `%s`", jsonObj.get("xcodeVersions").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BuildsListToolsets200ResponseXamarinInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BuildsListToolsets200ResponseXamarinInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BuildsListToolsets200ResponseXamarinInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BuildsListToolsets200ResponseXamarinInner.class));

       return (TypeAdapter<T>) new TypeAdapter<BuildsListToolsets200ResponseXamarinInner>() {
           @Override
           public void write(JsonWriter out, BuildsListToolsets200ResponseXamarinInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BuildsListToolsets200ResponseXamarinInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BuildsListToolsets200ResponseXamarinInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BuildsListToolsets200ResponseXamarinInner
   * @throws IOException if the JSON string is invalid with respect to BuildsListToolsets200ResponseXamarinInner
   */
  public static BuildsListToolsets200ResponseXamarinInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BuildsListToolsets200ResponseXamarinInner.class);
  }

  /**
   * Convert an instance of BuildsListToolsets200ResponseXamarinInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

