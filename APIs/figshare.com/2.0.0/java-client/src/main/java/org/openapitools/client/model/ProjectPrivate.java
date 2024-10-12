/*
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
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
 * ProjectPrivate
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:45.951625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectPrivate {
  /**
   * Role inside this project
   */
  @JsonAdapter(RoleEnum.Adapter.class)
  public enum RoleEnum {
    OWNER("Owner"),
    
    COLLABORATOR("Collaborator"),
    
    VIEWER("Viewer");

    private String value;

    RoleEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RoleEnum fromValue(String value) {
      for (RoleEnum b : RoleEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RoleEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RoleEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RoleEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RoleEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RoleEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ROLE = "role";
  @SerializedName(SERIALIZED_NAME_ROLE)
  private RoleEnum role;

  /**
   * Project storage type
   */
  @JsonAdapter(StorageEnum.Adapter.class)
  public enum StorageEnum {
    INDIVIDUAL("individual"),
    
    GROUP("group");

    private String value;

    StorageEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StorageEnum fromValue(String value) {
      for (StorageEnum b : StorageEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StorageEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StorageEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StorageEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StorageEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StorageEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STORAGE = "storage";
  @SerializedName(SERIALIZED_NAME_STORAGE)
  private StorageEnum storage;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_PUBLISHED_DATE = "published_date";
  @SerializedName(SERIALIZED_NAME_PUBLISHED_DATE)
  private String publishedDate;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public ProjectPrivate() {
  }

  public ProjectPrivate role(RoleEnum role) {
    this.role = role;
    return this;
  }

  /**
   * Role inside this project
   * @return role
   */
  @javax.annotation.Nonnull
  public RoleEnum getRole() {
    return role;
  }

  public void setRole(RoleEnum role) {
    this.role = role;
  }


  public ProjectPrivate storage(StorageEnum storage) {
    this.storage = storage;
    return this;
  }

  /**
   * Project storage type
   * @return storage
   */
  @javax.annotation.Nonnull
  public StorageEnum getStorage() {
    return storage;
  }

  public void setStorage(StorageEnum storage) {
    this.storage = storage;
  }


  public ProjectPrivate id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Project id
   * @return id
   */
  @javax.annotation.Nonnull
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public ProjectPrivate publishedDate(String publishedDate) {
    this.publishedDate = publishedDate;
    return this;
  }

  /**
   * Date when project was published
   * @return publishedDate
   */
  @javax.annotation.Nullable
  public String getPublishedDate() {
    return publishedDate;
  }

  public void setPublishedDate(String publishedDate) {
    this.publishedDate = publishedDate;
  }


  public ProjectPrivate title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Project title
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public ProjectPrivate url(String url) {
    this.url = url;
    return this;
  }

  /**
   * Api endpoint
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectPrivate projectPrivate = (ProjectPrivate) o;
    return Objects.equals(this.role, projectPrivate.role) &&
        Objects.equals(this.storage, projectPrivate.storage) &&
        Objects.equals(this.id, projectPrivate.id) &&
        Objects.equals(this.publishedDate, projectPrivate.publishedDate) &&
        Objects.equals(this.title, projectPrivate.title) &&
        Objects.equals(this.url, projectPrivate.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(role, storage, id, publishedDate, title, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectPrivate {\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    storage: ").append(toIndentedString(storage)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    publishedDate: ").append(toIndentedString(publishedDate)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("published_date");
    openapiFields.add("title");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("role");
    openapiRequiredFields.add("storage");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("published_date");
    openapiRequiredFields.add("title");
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectPrivate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectPrivate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectPrivate is not found in the empty JSON string", ProjectPrivate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectPrivate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectPrivate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProjectPrivate.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("role").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `role` to be a primitive type in the JSON string but got `%s`", jsonObj.get("role").toString()));
      }
      // validate the required field `role`
      RoleEnum.validateJsonElement(jsonObj.get("role"));
      if (!jsonObj.get("storage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storage").toString()));
      }
      // validate the required field `storage`
      StorageEnum.validateJsonElement(jsonObj.get("storage"));
      if ((jsonObj.get("published_date") != null && !jsonObj.get("published_date").isJsonNull()) && !jsonObj.get("published_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `published_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("published_date").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectPrivate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectPrivate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectPrivate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectPrivate.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectPrivate>() {
           @Override
           public void write(JsonWriter out, ProjectPrivate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectPrivate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectPrivate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectPrivate
   * @throws IOException if the JSON string is invalid with respect to ProjectPrivate
   */
  public static ProjectPrivate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectPrivate.class);
  }

  /**
   * Convert an instance of ProjectPrivate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

