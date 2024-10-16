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
 * Audience test result.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AudienceTestResult {
  /**
   * Gets or Sets inner
   */
  @JsonAdapter(InnerEnum.Adapter.class)
  public enum InnerEnum {
    STRING("string"),
    
    NUMBER("number"),
    
    BOOLEAN("boolean"),
    
    DATE_TIME("date_time");

    private String value;

    InnerEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static InnerEnum fromValue(String value) {
      for (InnerEnum b : InnerEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<InnerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final InnerEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public InnerEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return InnerEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      InnerEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CUSTOM_PROPERTIES = "custom_properties";
  @SerializedName(SERIALIZED_NAME_CUSTOM_PROPERTIES)
  private Map<String, InnerEnum> customProperties = new HashMap<>();

  public static final String SERIALIZED_NAME_DEFINITION = "definition";
  @SerializedName(SERIALIZED_NAME_DEFINITION)
  private String definition;

  public static final String SERIALIZED_NAME_ESTIMATED_COUNT = "estimated_count";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_COUNT)
  private Long estimatedCount;

  public static final String SERIALIZED_NAME_ESTIMATED_TOTAL_COUNT = "estimated_total_count";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_TOTAL_COUNT)
  private Long estimatedTotalCount;

  public AudienceTestResult() {
  }

  public AudienceTestResult customProperties(Map<String, InnerEnum> customProperties) {
    this.customProperties = customProperties;
    return this;
  }

  public AudienceTestResult putCustomPropertiesItem(String key, InnerEnum customPropertiesItem) {
    if (this.customProperties == null) {
      this.customProperties = new HashMap<>();
    }
    this.customProperties.put(key, customPropertiesItem);
    return this;
  }

  /**
   * Custom properties used in the definition.
   * @return customProperties
   */
  @javax.annotation.Nullable
  public Map<String, InnerEnum> getCustomProperties() {
    return customProperties;
  }

  public void setCustomProperties(Map<String, InnerEnum> customProperties) {
    this.customProperties = customProperties;
  }


  public AudienceTestResult definition(String definition) {
    this.definition = definition;
    return this;
  }

  /**
   * Audience definition in OData format.
   * @return definition
   */
  @javax.annotation.Nullable
  public String getDefinition() {
    return definition;
  }

  public void setDefinition(String definition) {
    this.definition = definition;
  }


  public AudienceTestResult estimatedCount(Long estimatedCount) {
    this.estimatedCount = estimatedCount;
    return this;
  }

  /**
   * Estimated audience size.
   * @return estimatedCount
   */
  @javax.annotation.Nullable
  public Long getEstimatedCount() {
    return estimatedCount;
  }

  public void setEstimatedCount(Long estimatedCount) {
    this.estimatedCount = estimatedCount;
  }


  public AudienceTestResult estimatedTotalCount(Long estimatedTotalCount) {
    this.estimatedTotalCount = estimatedTotalCount;
    return this;
  }

  /**
   * Estimated total audience size.
   * @return estimatedTotalCount
   */
  @javax.annotation.Nullable
  public Long getEstimatedTotalCount() {
    return estimatedTotalCount;
  }

  public void setEstimatedTotalCount(Long estimatedTotalCount) {
    this.estimatedTotalCount = estimatedTotalCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AudienceTestResult audienceTestResult = (AudienceTestResult) o;
    return Objects.equals(this.customProperties, audienceTestResult.customProperties) &&
        Objects.equals(this.definition, audienceTestResult.definition) &&
        Objects.equals(this.estimatedCount, audienceTestResult.estimatedCount) &&
        Objects.equals(this.estimatedTotalCount, audienceTestResult.estimatedTotalCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(customProperties, definition, estimatedCount, estimatedTotalCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AudienceTestResult {\n");
    sb.append("    customProperties: ").append(toIndentedString(customProperties)).append("\n");
    sb.append("    definition: ").append(toIndentedString(definition)).append("\n");
    sb.append("    estimatedCount: ").append(toIndentedString(estimatedCount)).append("\n");
    sb.append("    estimatedTotalCount: ").append(toIndentedString(estimatedTotalCount)).append("\n");
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
    openapiFields.add("custom_properties");
    openapiFields.add("definition");
    openapiFields.add("estimated_count");
    openapiFields.add("estimated_total_count");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AudienceTestResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AudienceTestResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AudienceTestResult is not found in the empty JSON string", AudienceTestResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AudienceTestResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AudienceTestResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("definition") != null && !jsonObj.get("definition").isJsonNull()) && !jsonObj.get("definition").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `definition` to be a primitive type in the JSON string but got `%s`", jsonObj.get("definition").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AudienceTestResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AudienceTestResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AudienceTestResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AudienceTestResult.class));

       return (TypeAdapter<T>) new TypeAdapter<AudienceTestResult>() {
           @Override
           public void write(JsonWriter out, AudienceTestResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AudienceTestResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AudienceTestResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AudienceTestResult
   * @throws IOException if the JSON string is invalid with respect to AudienceTestResult
   */
  public static AudienceTestResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AudienceTestResult.class);
  }

  /**
   * Convert an instance of AudienceTestResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

