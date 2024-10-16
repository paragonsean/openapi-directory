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
 * Audience definition.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AnalyticsListAudiences200ResponseValuesInner {
  public static final String SERIALIZED_NAME_DEFINITION = "definition";
  @SerializedName(SERIALIZED_NAME_DEFINITION)
  private String definition;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ESTIMATED_COUNT = "estimated_count";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_COUNT)
  private Long estimatedCount;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Audience state.
   */
  @JsonAdapter(StateEnum.Adapter.class)
  public enum StateEnum {
    CALCULATING("Calculating"),
    
    READY("Ready"),
    
    DISABLED("Disabled");

    private String value;

    StateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StateEnum fromValue(String value) {
      for (StateEnum b : StateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private StateEnum state;

  public AnalyticsListAudiences200ResponseValuesInner() {
  }

  public AnalyticsListAudiences200ResponseValuesInner definition(String definition) {
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


  public AnalyticsListAudiences200ResponseValuesInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Audience description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AnalyticsListAudiences200ResponseValuesInner estimatedCount(Long estimatedCount) {
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


  public AnalyticsListAudiences200ResponseValuesInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Audience name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AnalyticsListAudiences200ResponseValuesInner state(StateEnum state) {
    this.state = state;
    return this;
  }

  /**
   * Audience state.
   * @return state
   */
  @javax.annotation.Nullable
  public StateEnum getState() {
    return state;
  }

  public void setState(StateEnum state) {
    this.state = state;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalyticsListAudiences200ResponseValuesInner analyticsListAudiences200ResponseValuesInner = (AnalyticsListAudiences200ResponseValuesInner) o;
    return Objects.equals(this.definition, analyticsListAudiences200ResponseValuesInner.definition) &&
        Objects.equals(this.description, analyticsListAudiences200ResponseValuesInner.description) &&
        Objects.equals(this.estimatedCount, analyticsListAudiences200ResponseValuesInner.estimatedCount) &&
        Objects.equals(this.name, analyticsListAudiences200ResponseValuesInner.name) &&
        Objects.equals(this.state, analyticsListAudiences200ResponseValuesInner.state);
  }

  @Override
  public int hashCode() {
    return Objects.hash(definition, description, estimatedCount, name, state);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalyticsListAudiences200ResponseValuesInner {\n");
    sb.append("    definition: ").append(toIndentedString(definition)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    estimatedCount: ").append(toIndentedString(estimatedCount)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
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
    openapiFields.add("definition");
    openapiFields.add("description");
    openapiFields.add("estimated_count");
    openapiFields.add("name");
    openapiFields.add("state");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AnalyticsListAudiences200ResponseValuesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AnalyticsListAudiences200ResponseValuesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AnalyticsListAudiences200ResponseValuesInner is not found in the empty JSON string", AnalyticsListAudiences200ResponseValuesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AnalyticsListAudiences200ResponseValuesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AnalyticsListAudiences200ResponseValuesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("definition") != null && !jsonObj.get("definition").isJsonNull()) && !jsonObj.get("definition").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `definition` to be a primitive type in the JSON string but got `%s`", jsonObj.get("definition").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        StateEnum.validateJsonElement(jsonObj.get("state"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AnalyticsListAudiences200ResponseValuesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AnalyticsListAudiences200ResponseValuesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AnalyticsListAudiences200ResponseValuesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AnalyticsListAudiences200ResponseValuesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AnalyticsListAudiences200ResponseValuesInner>() {
           @Override
           public void write(JsonWriter out, AnalyticsListAudiences200ResponseValuesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AnalyticsListAudiences200ResponseValuesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AnalyticsListAudiences200ResponseValuesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AnalyticsListAudiences200ResponseValuesInner
   * @throws IOException if the JSON string is invalid with respect to AnalyticsListAudiences200ResponseValuesInner
   */
  public static AnalyticsListAudiences200ResponseValuesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AnalyticsListAudiences200ResponseValuesInner.class);
  }

  /**
   * Convert an instance of AnalyticsListAudiences200ResponseValuesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

