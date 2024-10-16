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
import org.openapitools.client.model.AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner;

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
 * CrashGroupOperatingSystems
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CrashGroupOperatingSystems {
  public static final String SERIALIZED_NAME_CRASH_COUNT = "crash_count";
  @SerializedName(SERIALIZED_NAME_CRASH_COUNT)
  private Long crashCount;

  public static final String SERIALIZED_NAME_OPERATING_SYSTEMS = "operating_systems";
  @SerializedName(SERIALIZED_NAME_OPERATING_SYSTEMS)
  private List<AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner> operatingSystems = new ArrayList<>();

  public CrashGroupOperatingSystems() {
  }

  public CrashGroupOperatingSystems crashCount(Long crashCount) {
    this.crashCount = crashCount;
    return this;
  }

  /**
   * Get crashCount
   * @return crashCount
   */
  @javax.annotation.Nullable
  public Long getCrashCount() {
    return crashCount;
  }

  public void setCrashCount(Long crashCount) {
    this.crashCount = crashCount;
  }


  public CrashGroupOperatingSystems operatingSystems(List<AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner> operatingSystems) {
    this.operatingSystems = operatingSystems;
    return this;
  }

  public CrashGroupOperatingSystems addOperatingSystemsItem(AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner operatingSystemsItem) {
    if (this.operatingSystems == null) {
      this.operatingSystems = new ArrayList<>();
    }
    this.operatingSystems.add(operatingSystemsItem);
    return this;
  }

  /**
   * Get operatingSystems
   * @return operatingSystems
   */
  @javax.annotation.Nullable
  public List<AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner> getOperatingSystems() {
    return operatingSystems;
  }

  public void setOperatingSystems(List<AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner> operatingSystems) {
    this.operatingSystems = operatingSystems;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CrashGroupOperatingSystems crashGroupOperatingSystems = (CrashGroupOperatingSystems) o;
    return Objects.equals(this.crashCount, crashGroupOperatingSystems.crashCount) &&
        Objects.equals(this.operatingSystems, crashGroupOperatingSystems.operatingSystems);
  }

  @Override
  public int hashCode() {
    return Objects.hash(crashCount, operatingSystems);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CrashGroupOperatingSystems {\n");
    sb.append("    crashCount: ").append(toIndentedString(crashCount)).append("\n");
    sb.append("    operatingSystems: ").append(toIndentedString(operatingSystems)).append("\n");
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
    openapiFields.add("crash_count");
    openapiFields.add("operating_systems");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CrashGroupOperatingSystems
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CrashGroupOperatingSystems.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CrashGroupOperatingSystems is not found in the empty JSON string", CrashGroupOperatingSystems.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CrashGroupOperatingSystems.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CrashGroupOperatingSystems` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("operating_systems") != null && !jsonObj.get("operating_systems").isJsonNull()) {
        JsonArray jsonArrayoperatingSystems = jsonObj.getAsJsonArray("operating_systems");
        if (jsonArrayoperatingSystems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("operating_systems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `operating_systems` to be an array in the JSON string but got `%s`", jsonObj.get("operating_systems").toString()));
          }

          // validate the optional field `operating_systems` (array)
          for (int i = 0; i < jsonArrayoperatingSystems.size(); i++) {
            AnalyticsCrashGroupOperatingSystemCounts200ResponseOperatingSystemsInner.validateJsonElement(jsonArrayoperatingSystems.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CrashGroupOperatingSystems.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CrashGroupOperatingSystems' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CrashGroupOperatingSystems> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CrashGroupOperatingSystems.class));

       return (TypeAdapter<T>) new TypeAdapter<CrashGroupOperatingSystems>() {
           @Override
           public void write(JsonWriter out, CrashGroupOperatingSystems value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CrashGroupOperatingSystems read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CrashGroupOperatingSystems given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CrashGroupOperatingSystems
   * @throws IOException if the JSON string is invalid with respect to CrashGroupOperatingSystems
   */
  public static CrashGroupOperatingSystems fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CrashGroupOperatingSystems.class);
  }

  /**
   * Convert an instance of CrashGroupOperatingSystems to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

