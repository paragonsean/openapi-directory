/*
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
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
import org.openapitools.client.model.ApplicationProperties;

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
 * The HDInsight cluster application
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:19:26.532369-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Application {
  public static final String SERIALIZED_NAME_ETAG = "etag";
  @SerializedName(SERIALIZED_NAME_ETAG)
  private String etag;

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private ApplicationProperties properties;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private Map<String, String> tags = new HashMap<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Application() {
  }

  public Application(
     String id, 
     String name, 
     String type
  ) {
    this();
    this.id = id;
    this.name = name;
    this.type = type;
  }

  public Application etag(String etag) {
    this.etag = etag;
    return this;
  }

  /**
   * The ETag for the application
   * @return etag
   */
  @javax.annotation.Nullable
  public String getEtag() {
    return etag;
  }

  public void setEtag(String etag) {
    this.etag = etag;
  }


  public Application properties(ApplicationProperties properties) {
    this.properties = properties;
    return this;
  }

  /**
   * Get properties
   * @return properties
   */
  @javax.annotation.Nullable
  public ApplicationProperties getProperties() {
    return properties;
  }

  public void setProperties(ApplicationProperties properties) {
    this.properties = properties;
  }


  public Application tags(Map<String, String> tags) {
    this.tags = tags;
    return this;
  }

  public Application putTagsItem(String key, String tagsItem) {
    if (this.tags == null) {
      this.tags = new HashMap<>();
    }
    this.tags.put(key, tagsItem);
    return this;
  }

  /**
   * The tags for the application.
   * @return tags
   */
  @javax.annotation.Nullable
  public Map<String, String> getTags() {
    return tags;
  }

  public void setTags(Map<String, String> tags) {
    this.tags = tags;
  }


  /**
   * Fully qualified resource Id for the resource.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * The name of the resource
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }



  /**
   * The type of the resource.
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Application application = (Application) o;
    return Objects.equals(this.etag, application.etag) &&
        Objects.equals(this.properties, application.properties) &&
        Objects.equals(this.tags, application.tags) &&
        Objects.equals(this.id, application.id) &&
        Objects.equals(this.name, application.name) &&
        Objects.equals(this.type, application.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(etag, properties, tags, id, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Application {\n");
    sb.append("    etag: ").append(toIndentedString(etag)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Application
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Application.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Application is not found in the empty JSON string", Application.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Application.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Application` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("etag") != null && !jsonObj.get("etag").isJsonNull()) && !jsonObj.get("etag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `etag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("etag").toString()));
      }
      // validate the optional field `properties`
      if (jsonObj.get("properties") != null && !jsonObj.get("properties").isJsonNull()) {
        ApplicationProperties.validateJsonElement(jsonObj.get("properties"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Application.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Application' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Application> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Application.class));

       return (TypeAdapter<T>) new TypeAdapter<Application>() {
           @Override
           public void write(JsonWriter out, Application value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Application read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Application given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Application
   * @throws IOException if the JSON string is invalid with respect to Application
   */
  public static Application fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Application.class);
  }

  /**
   * Convert an instance of Application to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

