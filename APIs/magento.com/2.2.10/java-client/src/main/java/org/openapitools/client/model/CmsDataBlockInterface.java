/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
 * CMS block interface.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CmsDataBlockInterface {
  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_CONTENT = "content";
  @SerializedName(SERIALIZED_NAME_CONTENT)
  private String content;

  public static final String SERIALIZED_NAME_CREATION_TIME = "creation_time";
  @SerializedName(SERIALIZED_NAME_CREATION_TIME)
  private String creationTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IDENTIFIER = "identifier";
  @SerializedName(SERIALIZED_NAME_IDENTIFIER)
  private String identifier;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATE_TIME = "update_time";
  @SerializedName(SERIALIZED_NAME_UPDATE_TIME)
  private String updateTime;

  public CmsDataBlockInterface() {
  }

  public CmsDataBlockInterface active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * Active
   * @return active
   */
  @javax.annotation.Nullable
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  public CmsDataBlockInterface content(String content) {
    this.content = content;
    return this;
  }

  /**
   * Content
   * @return content
   */
  @javax.annotation.Nullable
  public String getContent() {
    return content;
  }

  public void setContent(String content) {
    this.content = content;
  }


  public CmsDataBlockInterface creationTime(String creationTime) {
    this.creationTime = creationTime;
    return this;
  }

  /**
   * Creation time
   * @return creationTime
   */
  @javax.annotation.Nullable
  public String getCreationTime() {
    return creationTime;
  }

  public void setCreationTime(String creationTime) {
    this.creationTime = creationTime;
  }


  public CmsDataBlockInterface id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * ID
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public CmsDataBlockInterface identifier(String identifier) {
    this.identifier = identifier;
    return this;
  }

  /**
   * Identifier
   * @return identifier
   */
  @javax.annotation.Nonnull
  public String getIdentifier() {
    return identifier;
  }

  public void setIdentifier(String identifier) {
    this.identifier = identifier;
  }


  public CmsDataBlockInterface title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public CmsDataBlockInterface updateTime(String updateTime) {
    this.updateTime = updateTime;
    return this;
  }

  /**
   * Update time
   * @return updateTime
   */
  @javax.annotation.Nullable
  public String getUpdateTime() {
    return updateTime;
  }

  public void setUpdateTime(String updateTime) {
    this.updateTime = updateTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CmsDataBlockInterface cmsDataBlockInterface = (CmsDataBlockInterface) o;
    return Objects.equals(this.active, cmsDataBlockInterface.active) &&
        Objects.equals(this.content, cmsDataBlockInterface.content) &&
        Objects.equals(this.creationTime, cmsDataBlockInterface.creationTime) &&
        Objects.equals(this.id, cmsDataBlockInterface.id) &&
        Objects.equals(this.identifier, cmsDataBlockInterface.identifier) &&
        Objects.equals(this.title, cmsDataBlockInterface.title) &&
        Objects.equals(this.updateTime, cmsDataBlockInterface.updateTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, content, creationTime, id, identifier, title, updateTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CmsDataBlockInterface {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    creationTime: ").append(toIndentedString(creationTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    identifier: ").append(toIndentedString(identifier)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updateTime: ").append(toIndentedString(updateTime)).append("\n");
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
    openapiFields.add("active");
    openapiFields.add("content");
    openapiFields.add("creation_time");
    openapiFields.add("id");
    openapiFields.add("identifier");
    openapiFields.add("title");
    openapiFields.add("update_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("identifier");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CmsDataBlockInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CmsDataBlockInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CmsDataBlockInterface is not found in the empty JSON string", CmsDataBlockInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CmsDataBlockInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CmsDataBlockInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CmsDataBlockInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("content") != null && !jsonObj.get("content").isJsonNull()) && !jsonObj.get("content").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content").toString()));
      }
      if ((jsonObj.get("creation_time") != null && !jsonObj.get("creation_time").isJsonNull()) && !jsonObj.get("creation_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creation_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creation_time").toString()));
      }
      if (!jsonObj.get("identifier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `identifier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("identifier").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("update_time") != null && !jsonObj.get("update_time").isJsonNull()) && !jsonObj.get("update_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `update_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("update_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CmsDataBlockInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CmsDataBlockInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CmsDataBlockInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CmsDataBlockInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<CmsDataBlockInterface>() {
           @Override
           public void write(JsonWriter out, CmsDataBlockInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CmsDataBlockInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CmsDataBlockInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CmsDataBlockInterface
   * @throws IOException if the JSON string is invalid with respect to CmsDataBlockInterface
   */
  public static CmsDataBlockInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CmsDataBlockInterface.class);
  }

  /**
   * Convert an instance of CmsDataBlockInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

