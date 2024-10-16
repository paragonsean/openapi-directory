/*
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
 * Java type: com.noosh.domain.collaboration.vo.TagVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TagVO {
  public static final String SERIALIZED_NAME_IS_SPEC = "isSpec";
  @SerializedName(SERIALIZED_NAME_IS_SPEC)
  private Boolean isSpec;

  public static final String SERIALIZED_NAME_TAG_ID = "tagId";
  @SerializedName(SERIALIZED_NAME_TAG_ID)
  private Long tagId;

  public static final String SERIALIZED_NAME_TAG_NAME = "tagName";
  @SerializedName(SERIALIZED_NAME_TAG_NAME)
  private String tagName;

  public TagVO() {
  }

  public TagVO isSpec(Boolean isSpec) {
    this.isSpec = isSpec;
    return this;
  }

  /**
   * 
   * @return isSpec
   */
  @javax.annotation.Nullable
  public Boolean getIsSpec() {
    return isSpec;
  }

  public void setIsSpec(Boolean isSpec) {
    this.isSpec = isSpec;
  }


  public TagVO tagId(Long tagId) {
    this.tagId = tagId;
    return this;
  }

  /**
   * 
   * @return tagId
   */
  @javax.annotation.Nullable
  public Long getTagId() {
    return tagId;
  }

  public void setTagId(Long tagId) {
    this.tagId = tagId;
  }


  public TagVO tagName(String tagName) {
    this.tagName = tagName;
    return this;
  }

  /**
   * 
   * @return tagName
   */
  @javax.annotation.Nullable
  public String getTagName() {
    return tagName;
  }

  public void setTagName(String tagName) {
    this.tagName = tagName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TagVO tagVO = (TagVO) o;
    return Objects.equals(this.isSpec, tagVO.isSpec) &&
        Objects.equals(this.tagId, tagVO.tagId) &&
        Objects.equals(this.tagName, tagVO.tagName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isSpec, tagId, tagName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TagVO {\n");
    sb.append("    isSpec: ").append(toIndentedString(isSpec)).append("\n");
    sb.append("    tagId: ").append(toIndentedString(tagId)).append("\n");
    sb.append("    tagName: ").append(toIndentedString(tagName)).append("\n");
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
    openapiFields.add("isSpec");
    openapiFields.add("tagId");
    openapiFields.add("tagName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TagVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TagVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TagVO is not found in the empty JSON string", TagVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TagVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TagVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("tagName") != null && !jsonObj.get("tagName").isJsonNull()) && !jsonObj.get("tagName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tagName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tagName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TagVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TagVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TagVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TagVO.class));

       return (TypeAdapter<T>) new TypeAdapter<TagVO>() {
           @Override
           public void write(JsonWriter out, TagVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TagVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TagVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TagVO
   * @throws IOException if the JSON string is invalid with respect to TagVO
   */
  public static TagVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TagVO.class);
  }

  /**
   * Convert an instance of TagVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

