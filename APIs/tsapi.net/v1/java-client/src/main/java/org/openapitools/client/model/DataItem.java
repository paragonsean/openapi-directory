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
import org.openapitools.client.model.ParentRef;
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
 * DataItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:41.455821-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DataItem {
  public static final String SERIALIZED_NAME_IDENT = "ident";
  @SerializedName(SERIALIZED_NAME_IDENT)
  private String ident;

  public static final String SERIALIZED_NAME_PARENT_IDENT = "parentIdent";
  @SerializedName(SERIALIZED_NAME_PARENT_IDENT)
  private ParentRef parentIdent;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<String> values;

  public DataItem() {
  }

  public DataItem ident(String ident) {
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


  public DataItem parentIdent(ParentRef parentIdent) {
    this.parentIdent = parentIdent;
    return this;
  }

  /**
   * Get parentIdent
   * @return parentIdent
   */
  @javax.annotation.Nullable
  public ParentRef getParentIdent() {
    return parentIdent;
  }

  public void setParentIdent(ParentRef parentIdent) {
    this.parentIdent = parentIdent;
  }


  public DataItem values(List<String> values) {
    this.values = values;
    return this;
  }

  public DataItem addValuesItem(String valuesItem) {
    if (this.values == null) {
      this.values = new ArrayList<>();
    }
    this.values.add(valuesItem);
    return this;
  }

  /**
   * Get values
   * @return values
   */
  @javax.annotation.Nullable
  public List<String> getValues() {
    return values;
  }

  public void setValues(List<String> values) {
    this.values = values;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DataItem dataItem = (DataItem) o;
    return Objects.equals(this.ident, dataItem.ident) &&
        Objects.equals(this.parentIdent, dataItem.parentIdent) &&
        Objects.equals(this.values, dataItem.values);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(ident, parentIdent, values);
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
    sb.append("class DataItem {\n");
    sb.append("    ident: ").append(toIndentedString(ident)).append("\n");
    sb.append("    parentIdent: ").append(toIndentedString(parentIdent)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
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
    openapiFields.add("ident");
    openapiFields.add("parentIdent");
    openapiFields.add("values");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DataItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DataItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DataItem is not found in the empty JSON string", DataItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DataItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DataItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ident") != null && !jsonObj.get("ident").isJsonNull()) && !jsonObj.get("ident").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ident` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ident").toString()));
      }
      // validate the optional field `parentIdent`
      if (jsonObj.get("parentIdent") != null && !jsonObj.get("parentIdent").isJsonNull()) {
        ParentRef.validateJsonElement(jsonObj.get("parentIdent"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("values") != null && !jsonObj.get("values").isJsonNull() && !jsonObj.get("values").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `values` to be an array in the JSON string but got `%s`", jsonObj.get("values").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DataItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DataItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DataItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DataItem.class));

       return (TypeAdapter<T>) new TypeAdapter<DataItem>() {
           @Override
           public void write(JsonWriter out, DataItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DataItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DataItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DataItem
   * @throws IOException if the JSON string is invalid with respect to DataItem
   */
  public static DataItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DataItem.class);
  }

  /**
   * Convert an instance of DataItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

