/*
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import org.openapitools.client.model.CrawlRun;

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
 * ObjectStoreSearchResultHitsHitsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:59.898257-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ObjectStoreSearchResultHitsHitsInner {
  public static final String SERIALIZED_NAME_ID = "_id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_SCORE = "_score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Integer score;

  public static final String SERIALIZED_NAME_TYPE = "_type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_FIELDS = "fields";
  @SerializedName(SERIALIZED_NAME_FIELDS)
  private CrawlRun fields;

  public ObjectStoreSearchResultHitsHitsInner() {
  }

  public ObjectStoreSearchResultHitsHitsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public ObjectStoreSearchResultHitsHitsInner score(Integer score) {
    this.score = score;
    return this;
  }

  /**
   * Get score
   * @return score
   */
  @javax.annotation.Nullable
  public Integer getScore() {
    return score;
  }

  public void setScore(Integer score) {
    this.score = score;
  }


  public ObjectStoreSearchResultHitsHitsInner type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public ObjectStoreSearchResultHitsHitsInner fields(CrawlRun fields) {
    this.fields = fields;
    return this;
  }

  /**
   * Get fields
   * @return fields
   */
  @javax.annotation.Nullable
  public CrawlRun getFields() {
    return fields;
  }

  public void setFields(CrawlRun fields) {
    this.fields = fields;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ObjectStoreSearchResultHitsHitsInner objectStoreSearchResultHitsHitsInner = (ObjectStoreSearchResultHitsHitsInner) o;
    return Objects.equals(this.id, objectStoreSearchResultHitsHitsInner.id) &&
        Objects.equals(this.score, objectStoreSearchResultHitsHitsInner.score) &&
        Objects.equals(this.type, objectStoreSearchResultHitsHitsInner.type) &&
        Objects.equals(this.fields, objectStoreSearchResultHitsHitsInner.fields);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, score, type, fields);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ObjectStoreSearchResultHitsHitsInner {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    fields: ").append(toIndentedString(fields)).append("\n");
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
    openapiFields.add("_id");
    openapiFields.add("_score");
    openapiFields.add("_type");
    openapiFields.add("fields");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ObjectStoreSearchResultHitsHitsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ObjectStoreSearchResultHitsHitsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ObjectStoreSearchResultHitsHitsInner is not found in the empty JSON string", ObjectStoreSearchResultHitsHitsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ObjectStoreSearchResultHitsHitsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ObjectStoreSearchResultHitsHitsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("_id") != null && !jsonObj.get("_id").isJsonNull()) && !jsonObj.get("_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("_id").toString()));
      }
      if ((jsonObj.get("_type") != null && !jsonObj.get("_type").isJsonNull()) && !jsonObj.get("_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("_type").toString()));
      }
      // validate the optional field `fields`
      if (jsonObj.get("fields") != null && !jsonObj.get("fields").isJsonNull()) {
        CrawlRun.validateJsonElement(jsonObj.get("fields"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ObjectStoreSearchResultHitsHitsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ObjectStoreSearchResultHitsHitsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ObjectStoreSearchResultHitsHitsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ObjectStoreSearchResultHitsHitsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ObjectStoreSearchResultHitsHitsInner>() {
           @Override
           public void write(JsonWriter out, ObjectStoreSearchResultHitsHitsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ObjectStoreSearchResultHitsHitsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ObjectStoreSearchResultHitsHitsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ObjectStoreSearchResultHitsHitsInner
   * @throws IOException if the JSON string is invalid with respect to ObjectStoreSearchResultHitsHitsInner
   */
  public static ObjectStoreSearchResultHitsHitsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ObjectStoreSearchResultHitsHitsInner.class);
  }

  /**
   * Convert an instance of ObjectStoreSearchResultHitsHitsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

