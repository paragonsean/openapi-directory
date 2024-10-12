/*
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
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
 * The request for creating a profile.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:35:06.363531-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProfileRequestBase {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_INPUT_DATA = "inputData";
  @SerializedName(SERIALIZED_NAME_INPUT_DATA)
  private String inputData;

  public static final String SERIALIZED_NAME_KV_TAGS = "kvTags";
  @SerializedName(SERIALIZED_NAME_KV_TAGS)
  private Map<String, String> kvTags = new HashMap<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private Map<String, String> properties = new HashMap<>();

  public ProfileRequestBase() {
  }

  public ProfileRequestBase description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The profile description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ProfileRequestBase inputData(String inputData) {
    this.inputData = inputData;
    return this;
  }

  /**
   * The profile input data.
   * @return inputData
   */
  @javax.annotation.Nullable
  public String getInputData() {
    return inputData;
  }

  public void setInputData(String inputData) {
    this.inputData = inputData;
  }


  public ProfileRequestBase kvTags(Map<String, String> kvTags) {
    this.kvTags = kvTags;
    return this;
  }

  public ProfileRequestBase putKvTagsItem(String key, String kvTagsItem) {
    if (this.kvTags == null) {
      this.kvTags = new HashMap<>();
    }
    this.kvTags.put(key, kvTagsItem);
    return this;
  }

  /**
   * The tags dictionary.
   * @return kvTags
   */
  @javax.annotation.Nullable
  public Map<String, String> getKvTags() {
    return kvTags;
  }

  public void setKvTags(Map<String, String> kvTags) {
    this.kvTags = kvTags;
  }


  public ProfileRequestBase name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The profile name.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ProfileRequestBase properties(Map<String, String> properties) {
    this.properties = properties;
    return this;
  }

  public ProfileRequestBase putPropertiesItem(String key, String propertiesItem) {
    if (this.properties == null) {
      this.properties = new HashMap<>();
    }
    this.properties.put(key, propertiesItem);
    return this;
  }

  /**
   * The properties dictionary.
   * @return properties
   */
  @javax.annotation.Nullable
  public Map<String, String> getProperties() {
    return properties;
  }

  public void setProperties(Map<String, String> properties) {
    this.properties = properties;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProfileRequestBase profileRequestBase = (ProfileRequestBase) o;
    return Objects.equals(this.description, profileRequestBase.description) &&
        Objects.equals(this.inputData, profileRequestBase.inputData) &&
        Objects.equals(this.kvTags, profileRequestBase.kvTags) &&
        Objects.equals(this.name, profileRequestBase.name) &&
        Objects.equals(this.properties, profileRequestBase.properties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, inputData, kvTags, name, properties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProfileRequestBase {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    inputData: ").append(toIndentedString(inputData)).append("\n");
    sb.append("    kvTags: ").append(toIndentedString(kvTags)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("inputData");
    openapiFields.add("kvTags");
    openapiFields.add("name");
    openapiFields.add("properties");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProfileRequestBase
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProfileRequestBase.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProfileRequestBase is not found in the empty JSON string", ProfileRequestBase.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProfileRequestBase.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProfileRequestBase` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProfileRequestBase.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("inputData") != null && !jsonObj.get("inputData").isJsonNull()) && !jsonObj.get("inputData").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `inputData` to be a primitive type in the JSON string but got `%s`", jsonObj.get("inputData").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProfileRequestBase.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProfileRequestBase' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProfileRequestBase> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProfileRequestBase.class));

       return (TypeAdapter<T>) new TypeAdapter<ProfileRequestBase>() {
           @Override
           public void write(JsonWriter out, ProfileRequestBase value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProfileRequestBase read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProfileRequestBase given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProfileRequestBase
   * @throws IOException if the JSON string is invalid with respect to ProfileRequestBase
   */
  public static ProfileRequestBase fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProfileRequestBase.class);
  }

  /**
   * Convert an instance of ProfileRequestBase to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

