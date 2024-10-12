/*
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-03-01
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
import java.util.HashMap;
import java.util.List;
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
 * The detector information. By default this is not populated, unless it&#39;s specified in expandDetector
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:41.372254-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Detector {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGE_PATHS = "imagePaths";
  @SerializedName(SERIALIZED_NAME_IMAGE_PATHS)
  private List<String> imagePaths = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PARAMETERS = "parameters";
  @SerializedName(SERIALIZED_NAME_PARAMETERS)
  private Map<String, Object> parameters = new HashMap<>();

  public static final String SERIALIZED_NAME_SUPPORTED_RESOURCE_TYPES = "supportedResourceTypes";
  @SerializedName(SERIALIZED_NAME_SUPPORTED_RESOURCE_TYPES)
  private List<String> supportedResourceTypes = new ArrayList<>();

  public Detector() {
  }

  public Detector description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The Smart Detector description. By default this is not populated, unless it&#39;s specified in expandDetector
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Detector id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The detector id.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Detector imagePaths(List<String> imagePaths) {
    this.imagePaths = imagePaths;
    return this;
  }

  public Detector addImagePathsItem(String imagePathsItem) {
    if (this.imagePaths == null) {
      this.imagePaths = new ArrayList<>();
    }
    this.imagePaths.add(imagePathsItem);
    return this;
  }

  /**
   * The Smart Detector image path. By default this is not populated, unless it&#39;s specified in expandDetector
   * @return imagePaths
   */
  @javax.annotation.Nullable
  public List<String> getImagePaths() {
    return imagePaths;
  }

  public void setImagePaths(List<String> imagePaths) {
    this.imagePaths = imagePaths;
  }


  public Detector name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The Smart Detector name. By default this is not populated, unless it&#39;s specified in expandDetector
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Detector parameters(Map<String, Object> parameters) {
    this.parameters = parameters;
    return this;
  }

  public Detector putParametersItem(String key, Object parametersItem) {
    if (this.parameters == null) {
      this.parameters = new HashMap<>();
    }
    this.parameters.put(key, parametersItem);
    return this;
  }

  /**
   * The detector&#39;s parameters.&#39;
   * @return parameters
   */
  @javax.annotation.Nullable
  public Map<String, Object> getParameters() {
    return parameters;
  }

  public void setParameters(Map<String, Object> parameters) {
    this.parameters = parameters;
  }


  public Detector supportedResourceTypes(List<String> supportedResourceTypes) {
    this.supportedResourceTypes = supportedResourceTypes;
    return this;
  }

  public Detector addSupportedResourceTypesItem(String supportedResourceTypesItem) {
    if (this.supportedResourceTypes == null) {
      this.supportedResourceTypes = new ArrayList<>();
    }
    this.supportedResourceTypes.add(supportedResourceTypesItem);
    return this;
  }

  /**
   * The Smart Detector supported resource types. By default this is not populated, unless it&#39;s specified in expandDetector
   * @return supportedResourceTypes
   */
  @javax.annotation.Nullable
  public List<String> getSupportedResourceTypes() {
    return supportedResourceTypes;
  }

  public void setSupportedResourceTypes(List<String> supportedResourceTypes) {
    this.supportedResourceTypes = supportedResourceTypes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Detector detector = (Detector) o;
    return Objects.equals(this.description, detector.description) &&
        Objects.equals(this.id, detector.id) &&
        Objects.equals(this.imagePaths, detector.imagePaths) &&
        Objects.equals(this.name, detector.name) &&
        Objects.equals(this.parameters, detector.parameters) &&
        Objects.equals(this.supportedResourceTypes, detector.supportedResourceTypes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, id, imagePaths, name, parameters, supportedResourceTypes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Detector {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    imagePaths: ").append(toIndentedString(imagePaths)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    parameters: ").append(toIndentedString(parameters)).append("\n");
    sb.append("    supportedResourceTypes: ").append(toIndentedString(supportedResourceTypes)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("imagePaths");
    openapiFields.add("name");
    openapiFields.add("parameters");
    openapiFields.add("supportedResourceTypes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Detector
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Detector.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Detector is not found in the empty JSON string", Detector.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Detector.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Detector` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Detector.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("imagePaths") != null && !jsonObj.get("imagePaths").isJsonNull() && !jsonObj.get("imagePaths").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `imagePaths` to be an array in the JSON string but got `%s`", jsonObj.get("imagePaths").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("supportedResourceTypes") != null && !jsonObj.get("supportedResourceTypes").isJsonNull() && !jsonObj.get("supportedResourceTypes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `supportedResourceTypes` to be an array in the JSON string but got `%s`", jsonObj.get("supportedResourceTypes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Detector.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Detector' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Detector> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Detector.class));

       return (TypeAdapter<T>) new TypeAdapter<Detector>() {
           @Override
           public void write(JsonWriter out, Detector value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Detector read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Detector given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Detector
   * @throws IOException if the JSON string is invalid with respect to Detector
   */
  public static Detector fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Detector.class);
  }

  /**
   * Convert an instance of Detector to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

