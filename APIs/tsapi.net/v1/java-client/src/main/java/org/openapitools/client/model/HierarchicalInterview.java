/*
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
import org.openapitools.client.model.DataItem;
import org.openapitools.client.model.Level;
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
 * HierarchicalInterview
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:41.455821-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HierarchicalInterview {
  public static final String SERIALIZED_NAME_DATA_ITEMS = "dataItems";
  @SerializedName(SERIALIZED_NAME_DATA_ITEMS)
  private List<DataItem> dataItems;

  public static final String SERIALIZED_NAME_HIERARCHICAL_INTERVIEWS = "hierarchicalInterviews";
  @SerializedName(SERIALIZED_NAME_HIERARCHICAL_INTERVIEWS)
  private List<HierarchicalInterview> hierarchicalInterviews;

  public static final String SERIALIZED_NAME_IDENT = "ident";
  @SerializedName(SERIALIZED_NAME_IDENT)
  private String ident;

  public static final String SERIALIZED_NAME_LEVEL = "level";
  @SerializedName(SERIALIZED_NAME_LEVEL)
  private Level level;

  public HierarchicalInterview() {
  }

  public HierarchicalInterview dataItems(List<DataItem> dataItems) {
    this.dataItems = dataItems;
    return this;
  }

  public HierarchicalInterview addDataItemsItem(DataItem dataItemsItem) {
    if (this.dataItems == null) {
      this.dataItems = new ArrayList<>();
    }
    this.dataItems.add(dataItemsItem);
    return this;
  }

  /**
   * Get dataItems
   * @return dataItems
   */
  @javax.annotation.Nullable
  public List<DataItem> getDataItems() {
    return dataItems;
  }

  public void setDataItems(List<DataItem> dataItems) {
    this.dataItems = dataItems;
  }


  public HierarchicalInterview hierarchicalInterviews(List<HierarchicalInterview> hierarchicalInterviews) {
    this.hierarchicalInterviews = hierarchicalInterviews;
    return this;
  }

  public HierarchicalInterview addHierarchicalInterviewsItem(HierarchicalInterview hierarchicalInterviewsItem) {
    if (this.hierarchicalInterviews == null) {
      this.hierarchicalInterviews = new ArrayList<>();
    }
    this.hierarchicalInterviews.add(hierarchicalInterviewsItem);
    return this;
  }

  /**
   * Get hierarchicalInterviews
   * @return hierarchicalInterviews
   */
  @javax.annotation.Nullable
  public List<HierarchicalInterview> getHierarchicalInterviews() {
    return hierarchicalInterviews;
  }

  public void setHierarchicalInterviews(List<HierarchicalInterview> hierarchicalInterviews) {
    this.hierarchicalInterviews = hierarchicalInterviews;
  }


  public HierarchicalInterview ident(String ident) {
    this.ident = ident;
    return this;
  }

  /**
   * Get ident
   * @return ident
   */
  @javax.annotation.Nullable
  public String getIdent() {
    return ident;
  }

  public void setIdent(String ident) {
    this.ident = ident;
  }


  public HierarchicalInterview level(Level level) {
    this.level = level;
    return this;
  }

  /**
   * Get level
   * @return level
   */
  @javax.annotation.Nullable
  public Level getLevel() {
    return level;
  }

  public void setLevel(Level level) {
    this.level = level;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HierarchicalInterview hierarchicalInterview = (HierarchicalInterview) o;
    return Objects.equals(this.dataItems, hierarchicalInterview.dataItems) &&
        Objects.equals(this.hierarchicalInterviews, hierarchicalInterview.hierarchicalInterviews) &&
        Objects.equals(this.ident, hierarchicalInterview.ident) &&
        Objects.equals(this.level, hierarchicalInterview.level);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(dataItems, hierarchicalInterviews, ident, level);
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
    sb.append("class HierarchicalInterview {\n");
    sb.append("    dataItems: ").append(toIndentedString(dataItems)).append("\n");
    sb.append("    hierarchicalInterviews: ").append(toIndentedString(hierarchicalInterviews)).append("\n");
    sb.append("    ident: ").append(toIndentedString(ident)).append("\n");
    sb.append("    level: ").append(toIndentedString(level)).append("\n");
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
    openapiFields.add("dataItems");
    openapiFields.add("hierarchicalInterviews");
    openapiFields.add("ident");
    openapiFields.add("level");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HierarchicalInterview
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HierarchicalInterview.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HierarchicalInterview is not found in the empty JSON string", HierarchicalInterview.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HierarchicalInterview.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HierarchicalInterview` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("dataItems") != null && !jsonObj.get("dataItems").isJsonNull()) {
        JsonArray jsonArraydataItems = jsonObj.getAsJsonArray("dataItems");
        if (jsonArraydataItems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("dataItems").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `dataItems` to be an array in the JSON string but got `%s`", jsonObj.get("dataItems").toString()));
          }

          // validate the optional field `dataItems` (array)
          for (int i = 0; i < jsonArraydataItems.size(); i++) {
            DataItem.validateJsonElement(jsonArraydataItems.get(i));
          };
        }
      }
      if (jsonObj.get("hierarchicalInterviews") != null && !jsonObj.get("hierarchicalInterviews").isJsonNull()) {
        JsonArray jsonArrayhierarchicalInterviews = jsonObj.getAsJsonArray("hierarchicalInterviews");
        if (jsonArrayhierarchicalInterviews != null) {
          // ensure the json data is an array
          if (!jsonObj.get("hierarchicalInterviews").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `hierarchicalInterviews` to be an array in the JSON string but got `%s`", jsonObj.get("hierarchicalInterviews").toString()));
          }

          // validate the optional field `hierarchicalInterviews` (array)
          for (int i = 0; i < jsonArrayhierarchicalInterviews.size(); i++) {
            HierarchicalInterview.validateJsonElement(jsonArrayhierarchicalInterviews.get(i));
          };
        }
      }
      if ((jsonObj.get("ident") != null && !jsonObj.get("ident").isJsonNull()) && !jsonObj.get("ident").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ident` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ident").toString()));
      }
      // validate the optional field `level`
      if (jsonObj.get("level") != null && !jsonObj.get("level").isJsonNull()) {
        Level.validateJsonElement(jsonObj.get("level"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HierarchicalInterview.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HierarchicalInterview' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HierarchicalInterview> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HierarchicalInterview.class));

       return (TypeAdapter<T>) new TypeAdapter<HierarchicalInterview>() {
           @Override
           public void write(JsonWriter out, HierarchicalInterview value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HierarchicalInterview read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HierarchicalInterview given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HierarchicalInterview
   * @throws IOException if the JSON string is invalid with respect to HierarchicalInterview
   */
  public static HierarchicalInterview fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HierarchicalInterview.class);
  }

  /**
   * Convert an instance of HierarchicalInterview to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

