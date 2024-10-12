/*
 * VocaDbWeb
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ReleaseEventSeriesForApiContract;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * ReleaseEventSeriesForApiContractPartialFindResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:40.974326-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReleaseEventSeriesForApiContractPartialFindResult {
  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<ReleaseEventSeriesForApiContract> items;

  public static final String SERIALIZED_NAME_TERM = "term";
  @SerializedName(SERIALIZED_NAME_TERM)
  private String term;

  public static final String SERIALIZED_NAME_TOTAL_COUNT = "totalCount";
  @SerializedName(SERIALIZED_NAME_TOTAL_COUNT)
  private Integer totalCount;

  public ReleaseEventSeriesForApiContractPartialFindResult() {
  }

  public ReleaseEventSeriesForApiContractPartialFindResult items(List<ReleaseEventSeriesForApiContract> items) {
    this.items = items;
    return this;
  }

  public ReleaseEventSeriesForApiContractPartialFindResult addItemsItem(ReleaseEventSeriesForApiContract itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Get items
   * @return items
   */
  @javax.annotation.Nullable
  public List<ReleaseEventSeriesForApiContract> getItems() {
    return items;
  }

  public void setItems(List<ReleaseEventSeriesForApiContract> items) {
    this.items = items;
  }


  public ReleaseEventSeriesForApiContractPartialFindResult term(String term) {
    this.term = term;
    return this;
  }

  /**
   * Get term
   * @return term
   */
  @javax.annotation.Nullable
  public String getTerm() {
    return term;
  }

  public void setTerm(String term) {
    this.term = term;
  }


  public ReleaseEventSeriesForApiContractPartialFindResult totalCount(Integer totalCount) {
    this.totalCount = totalCount;
    return this;
  }

  /**
   * Get totalCount
   * @return totalCount
   */
  @javax.annotation.Nullable
  public Integer getTotalCount() {
    return totalCount;
  }

  public void setTotalCount(Integer totalCount) {
    this.totalCount = totalCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReleaseEventSeriesForApiContractPartialFindResult releaseEventSeriesForApiContractPartialFindResult = (ReleaseEventSeriesForApiContractPartialFindResult) o;
    return Objects.equals(this.items, releaseEventSeriesForApiContractPartialFindResult.items) &&
        Objects.equals(this.term, releaseEventSeriesForApiContractPartialFindResult.term) &&
        Objects.equals(this.totalCount, releaseEventSeriesForApiContractPartialFindResult.totalCount);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(items, term, totalCount);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReleaseEventSeriesForApiContractPartialFindResult {\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    term: ").append(toIndentedString(term)).append("\n");
    sb.append("    totalCount: ").append(toIndentedString(totalCount)).append("\n");
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
    openapiFields.add("items");
    openapiFields.add("term");
    openapiFields.add("totalCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReleaseEventSeriesForApiContractPartialFindResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReleaseEventSeriesForApiContractPartialFindResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReleaseEventSeriesForApiContractPartialFindResult is not found in the empty JSON string", ReleaseEventSeriesForApiContractPartialFindResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReleaseEventSeriesForApiContractPartialFindResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReleaseEventSeriesForApiContractPartialFindResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            ReleaseEventSeriesForApiContract.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("term") != null && !jsonObj.get("term").isJsonNull()) && !jsonObj.get("term").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `term` to be a primitive type in the JSON string but got `%s`", jsonObj.get("term").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReleaseEventSeriesForApiContractPartialFindResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReleaseEventSeriesForApiContractPartialFindResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReleaseEventSeriesForApiContractPartialFindResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReleaseEventSeriesForApiContractPartialFindResult.class));

       return (TypeAdapter<T>) new TypeAdapter<ReleaseEventSeriesForApiContractPartialFindResult>() {
           @Override
           public void write(JsonWriter out, ReleaseEventSeriesForApiContractPartialFindResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReleaseEventSeriesForApiContractPartialFindResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReleaseEventSeriesForApiContractPartialFindResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReleaseEventSeriesForApiContractPartialFindResult
   * @throws IOException if the JSON string is invalid with respect to ReleaseEventSeriesForApiContractPartialFindResult
   */
  public static ReleaseEventSeriesForApiContractPartialFindResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReleaseEventSeriesForApiContractPartialFindResult.class);
  }

  /**
   * Convert an instance of ReleaseEventSeriesForApiContractPartialFindResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

