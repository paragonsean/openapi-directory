/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
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
 * Properties that describe a base image dependency.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:59.640634-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BaseImageDependency {
  public static final String SERIALIZED_NAME_DIGEST = "digest";
  @SerializedName(SERIALIZED_NAME_DIGEST)
  private String digest;

  public static final String SERIALIZED_NAME_REGISTRY = "registry";
  @SerializedName(SERIALIZED_NAME_REGISTRY)
  private String registry;

  public static final String SERIALIZED_NAME_REPOSITORY = "repository";
  @SerializedName(SERIALIZED_NAME_REPOSITORY)
  private String repository;

  public static final String SERIALIZED_NAME_TAG = "tag";
  @SerializedName(SERIALIZED_NAME_TAG)
  private String tag;

  /**
   * The type of the base image dependency.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    BUILD_TIME("BuildTime"),
    
    RUN_TIME("RunTime");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public BaseImageDependency() {
  }

  public BaseImageDependency digest(String digest) {
    this.digest = digest;
    return this;
  }

  /**
   * The sha256-based digest of the image manifest.
   * @return digest
   */
  @javax.annotation.Nullable
  public String getDigest() {
    return digest;
  }

  public void setDigest(String digest) {
    this.digest = digest;
  }


  public BaseImageDependency registry(String registry) {
    this.registry = registry;
    return this;
  }

  /**
   * The registry login server.
   * @return registry
   */
  @javax.annotation.Nullable
  public String getRegistry() {
    return registry;
  }

  public void setRegistry(String registry) {
    this.registry = registry;
  }


  public BaseImageDependency repository(String repository) {
    this.repository = repository;
    return this;
  }

  /**
   * The repository name.
   * @return repository
   */
  @javax.annotation.Nullable
  public String getRepository() {
    return repository;
  }

  public void setRepository(String repository) {
    this.repository = repository;
  }


  public BaseImageDependency tag(String tag) {
    this.tag = tag;
    return this;
  }

  /**
   * The tag name.
   * @return tag
   */
  @javax.annotation.Nullable
  public String getTag() {
    return tag;
  }

  public void setTag(String tag) {
    this.tag = tag;
  }


  public BaseImageDependency type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The type of the base image dependency.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BaseImageDependency baseImageDependency = (BaseImageDependency) o;
    return Objects.equals(this.digest, baseImageDependency.digest) &&
        Objects.equals(this.registry, baseImageDependency.registry) &&
        Objects.equals(this.repository, baseImageDependency.repository) &&
        Objects.equals(this.tag, baseImageDependency.tag) &&
        Objects.equals(this.type, baseImageDependency.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(digest, registry, repository, tag, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BaseImageDependency {\n");
    sb.append("    digest: ").append(toIndentedString(digest)).append("\n");
    sb.append("    registry: ").append(toIndentedString(registry)).append("\n");
    sb.append("    repository: ").append(toIndentedString(repository)).append("\n");
    sb.append("    tag: ").append(toIndentedString(tag)).append("\n");
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
    openapiFields.add("digest");
    openapiFields.add("registry");
    openapiFields.add("repository");
    openapiFields.add("tag");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BaseImageDependency
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BaseImageDependency.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BaseImageDependency is not found in the empty JSON string", BaseImageDependency.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BaseImageDependency.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BaseImageDependency` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("digest") != null && !jsonObj.get("digest").isJsonNull()) && !jsonObj.get("digest").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `digest` to be a primitive type in the JSON string but got `%s`", jsonObj.get("digest").toString()));
      }
      if ((jsonObj.get("registry") != null && !jsonObj.get("registry").isJsonNull()) && !jsonObj.get("registry").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `registry` to be a primitive type in the JSON string but got `%s`", jsonObj.get("registry").toString()));
      }
      if ((jsonObj.get("repository") != null && !jsonObj.get("repository").isJsonNull()) && !jsonObj.get("repository").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `repository` to be a primitive type in the JSON string but got `%s`", jsonObj.get("repository").toString()));
      }
      if ((jsonObj.get("tag") != null && !jsonObj.get("tag").isJsonNull()) && !jsonObj.get("tag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tag").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BaseImageDependency.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BaseImageDependency' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BaseImageDependency> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BaseImageDependency.class));

       return (TypeAdapter<T>) new TypeAdapter<BaseImageDependency>() {
           @Override
           public void write(JsonWriter out, BaseImageDependency value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BaseImageDependency read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BaseImageDependency given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BaseImageDependency
   * @throws IOException if the JSON string is invalid with respect to BaseImageDependency
   */
  public static BaseImageDependency fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BaseImageDependency.class);
  }

  /**
   * Convert an instance of BaseImageDependency to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

