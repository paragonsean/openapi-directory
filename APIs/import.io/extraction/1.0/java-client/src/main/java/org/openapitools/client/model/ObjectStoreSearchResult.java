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
import org.openapitools.client.model.ObjectStoreSearchResultHits;

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
 * ObjectStoreSearchResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:56.484539-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ObjectStoreSearchResult {
  public static final String SERIALIZED_NAME_HITS = "hits";
  @SerializedName(SERIALIZED_NAME_HITS)
  private ObjectStoreSearchResultHits hits;

  public static final String SERIALIZED_NAME_TIMED_OUT = "timed_out";
  @SerializedName(SERIALIZED_NAME_TIMED_OUT)
  private Boolean timedOut;

  public static final String SERIALIZED_NAME_TOOK = "took";
  @SerializedName(SERIALIZED_NAME_TOOK)
  private Integer took;

  public ObjectStoreSearchResult() {
  }

  public ObjectStoreSearchResult hits(ObjectStoreSearchResultHits hits) {
    this.hits = hits;
    return this;
  }

  /**
   * Get hits
   * @return hits
   */
  @javax.annotation.Nullable
  public ObjectStoreSearchResultHits getHits() {
    return hits;
  }

  public void setHits(ObjectStoreSearchResultHits hits) {
    this.hits = hits;
  }


  public ObjectStoreSearchResult timedOut(Boolean timedOut) {
    this.timedOut = timedOut;
    return this;
  }

  /**
   * Get timedOut
   * @return timedOut
   */
  @javax.annotation.Nullable
  public Boolean getTimedOut() {
    return timedOut;
  }

  public void setTimedOut(Boolean timedOut) {
    this.timedOut = timedOut;
  }


  public ObjectStoreSearchResult took(Integer took) {
    this.took = took;
    return this;
  }

  /**
   * Get took
   * @return took
   */
  @javax.annotation.Nullable
  public Integer getTook() {
    return took;
  }

  public void setTook(Integer took) {
    this.took = took;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ObjectStoreSearchResult objectStoreSearchResult = (ObjectStoreSearchResult) o;
    return Objects.equals(this.hits, objectStoreSearchResult.hits) &&
        Objects.equals(this.timedOut, objectStoreSearchResult.timedOut) &&
        Objects.equals(this.took, objectStoreSearchResult.took);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hits, timedOut, took);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ObjectStoreSearchResult {\n");
    sb.append("    hits: ").append(toIndentedString(hits)).append("\n");
    sb.append("    timedOut: ").append(toIndentedString(timedOut)).append("\n");
    sb.append("    took: ").append(toIndentedString(took)).append("\n");
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
    openapiFields.add("hits");
    openapiFields.add("timed_out");
    openapiFields.add("took");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ObjectStoreSearchResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ObjectStoreSearchResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ObjectStoreSearchResult is not found in the empty JSON string", ObjectStoreSearchResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ObjectStoreSearchResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ObjectStoreSearchResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `hits`
      if (jsonObj.get("hits") != null && !jsonObj.get("hits").isJsonNull()) {
        ObjectStoreSearchResultHits.validateJsonElement(jsonObj.get("hits"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ObjectStoreSearchResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ObjectStoreSearchResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ObjectStoreSearchResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ObjectStoreSearchResult.class));

       return (TypeAdapter<T>) new TypeAdapter<ObjectStoreSearchResult>() {
           @Override
           public void write(JsonWriter out, ObjectStoreSearchResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ObjectStoreSearchResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ObjectStoreSearchResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ObjectStoreSearchResult
   * @throws IOException if the JSON string is invalid with respect to ObjectStoreSearchResult
   */
  public static ObjectStoreSearchResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ObjectStoreSearchResult.class);
  }

  /**
   * Convert an instance of ObjectStoreSearchResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

