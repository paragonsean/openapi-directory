/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
import java.util.List;
import org.openapitools.client.model.SourceRef;

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
 * QueryFilters
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:37.231084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class QueryFilters {
  public static final String SERIALIZED_NAME_SERIES_TAG_IDS = "seriesTagIds";
  @SerializedName(SERIALIZED_NAME_SERIES_TAG_IDS)
  private List<Long> seriesTagIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERIES_TYPE_IDS = "seriesTypeIds";
  @SerializedName(SERIALIZED_NAME_SERIES_TYPE_IDS)
  private List<Long> seriesTypeIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOURCE_REFS = "sourceRefs";
  @SerializedName(SERIALIZED_NAME_SOURCE_REFS)
  private List<SourceRef> sourceRefs = new ArrayList<>();

  public QueryFilters() {
  }

  public QueryFilters seriesTagIds(List<Long> seriesTagIds) {
    this.seriesTagIds = seriesTagIds;
    return this;
  }

  public QueryFilters addSeriesTagIdsItem(Long seriesTagIdsItem) {
    if (this.seriesTagIds == null) {
      this.seriesTagIds = new ArrayList<>();
    }
    this.seriesTagIds.add(seriesTagIdsItem);
    return this;
  }

  /**
   * Get seriesTagIds
   * @return seriesTagIds
   */
  @javax.annotation.Nullable
  public List<Long> getSeriesTagIds() {
    return seriesTagIds;
  }

  public void setSeriesTagIds(List<Long> seriesTagIds) {
    this.seriesTagIds = seriesTagIds;
  }


  public QueryFilters seriesTypeIds(List<Long> seriesTypeIds) {
    this.seriesTypeIds = seriesTypeIds;
    return this;
  }

  public QueryFilters addSeriesTypeIdsItem(Long seriesTypeIdsItem) {
    if (this.seriesTypeIds == null) {
      this.seriesTypeIds = new ArrayList<>();
    }
    this.seriesTypeIds.add(seriesTypeIdsItem);
    return this;
  }

  /**
   * Get seriesTypeIds
   * @return seriesTypeIds
   */
  @javax.annotation.Nullable
  public List<Long> getSeriesTypeIds() {
    return seriesTypeIds;
  }

  public void setSeriesTypeIds(List<Long> seriesTypeIds) {
    this.seriesTypeIds = seriesTypeIds;
  }


  public QueryFilters sourceRefs(List<SourceRef> sourceRefs) {
    this.sourceRefs = sourceRefs;
    return this;
  }

  public QueryFilters addSourceRefsItem(SourceRef sourceRefsItem) {
    if (this.sourceRefs == null) {
      this.sourceRefs = new ArrayList<>();
    }
    this.sourceRefs.add(sourceRefsItem);
    return this;
  }

  /**
   * Get sourceRefs
   * @return sourceRefs
   */
  @javax.annotation.Nullable
  public List<SourceRef> getSourceRefs() {
    return sourceRefs;
  }

  public void setSourceRefs(List<SourceRef> sourceRefs) {
    this.sourceRefs = sourceRefs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    QueryFilters queryFilters = (QueryFilters) o;
    return Objects.equals(this.seriesTagIds, queryFilters.seriesTagIds) &&
        Objects.equals(this.seriesTypeIds, queryFilters.seriesTypeIds) &&
        Objects.equals(this.sourceRefs, queryFilters.sourceRefs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(seriesTagIds, seriesTypeIds, sourceRefs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class QueryFilters {\n");
    sb.append("    seriesTagIds: ").append(toIndentedString(seriesTagIds)).append("\n");
    sb.append("    seriesTypeIds: ").append(toIndentedString(seriesTypeIds)).append("\n");
    sb.append("    sourceRefs: ").append(toIndentedString(sourceRefs)).append("\n");
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
    openapiFields.add("seriesTagIds");
    openapiFields.add("seriesTypeIds");
    openapiFields.add("sourceRefs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to QueryFilters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!QueryFilters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in QueryFilters is not found in the empty JSON string", QueryFilters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!QueryFilters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `QueryFilters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("seriesTagIds") != null && !jsonObj.get("seriesTagIds").isJsonNull() && !jsonObj.get("seriesTagIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `seriesTagIds` to be an array in the JSON string but got `%s`", jsonObj.get("seriesTagIds").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("seriesTypeIds") != null && !jsonObj.get("seriesTypeIds").isJsonNull() && !jsonObj.get("seriesTypeIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `seriesTypeIds` to be an array in the JSON string but got `%s`", jsonObj.get("seriesTypeIds").toString()));
      }
      if (jsonObj.get("sourceRefs") != null && !jsonObj.get("sourceRefs").isJsonNull()) {
        JsonArray jsonArraysourceRefs = jsonObj.getAsJsonArray("sourceRefs");
        if (jsonArraysourceRefs != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sourceRefs").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sourceRefs` to be an array in the JSON string but got `%s`", jsonObj.get("sourceRefs").toString()));
          }

          // validate the optional field `sourceRefs` (array)
          for (int i = 0; i < jsonArraysourceRefs.size(); i++) {
            SourceRef.validateJsonElement(jsonArraysourceRefs.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!QueryFilters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'QueryFilters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<QueryFilters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(QueryFilters.class));

       return (TypeAdapter<T>) new TypeAdapter<QueryFilters>() {
           @Override
           public void write(JsonWriter out, QueryFilters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public QueryFilters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of QueryFilters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of QueryFilters
   * @throws IOException if the JSON string is invalid with respect to QueryFilters
   */
  public static QueryFilters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, QueryFilters.class);
  }

  /**
   * Convert an instance of QueryFilters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

