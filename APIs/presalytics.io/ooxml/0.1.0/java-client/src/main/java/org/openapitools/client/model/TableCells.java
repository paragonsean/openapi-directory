/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
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
import java.util.UUID;
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
 * TableCells
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TableCells {
  public static final String SERIALIZED_NAME_COLUMN_ID = "columnId";
  @SerializedName(SERIALIZED_NAME_COLUMN_ID)
  private UUID columnId;

  public static final String SERIALIZED_NAME_COLUMN_SPAN = "columnSpan";
  @SerializedName(SERIALIZED_NAME_COLUMN_SPAN)
  private Integer columnSpan;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_MERGED_HOROZONTAL = "isMergedHorozontal";
  @SerializedName(SERIALIZED_NAME_IS_MERGED_HOROZONTAL)
  private Boolean isMergedHorozontal;

  public static final String SERIALIZED_NAME_IS_MERGED_VERTICAL = "isMergedVertical";
  @SerializedName(SERIALIZED_NAME_IS_MERGED_VERTICAL)
  private Boolean isMergedVertical;

  public static final String SERIALIZED_NAME_ROW_ID = "rowId";
  @SerializedName(SERIALIZED_NAME_ROW_ID)
  private UUID rowId;

  public static final String SERIALIZED_NAME_ROW_SPAN = "rowSpan";
  @SerializedName(SERIALIZED_NAME_ROW_SPAN)
  private Integer rowSpan;

  public TableCells() {
  }

  public TableCells columnId(UUID columnId) {
    this.columnId = columnId;
    return this;
  }

  /**
   * Get columnId
   * @return columnId
   */
  @javax.annotation.Nullable
  public UUID getColumnId() {
    return columnId;
  }

  public void setColumnId(UUID columnId) {
    this.columnId = columnId;
  }


  public TableCells columnSpan(Integer columnSpan) {
    this.columnSpan = columnSpan;
    return this;
  }

  /**
   * Get columnSpan
   * @return columnSpan
   */
  @javax.annotation.Nullable
  public Integer getColumnSpan() {
    return columnSpan;
  }

  public void setColumnSpan(Integer columnSpan) {
    this.columnSpan = columnSpan;
  }


  public TableCells id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public TableCells isMergedHorozontal(Boolean isMergedHorozontal) {
    this.isMergedHorozontal = isMergedHorozontal;
    return this;
  }

  /**
   * Get isMergedHorozontal
   * @return isMergedHorozontal
   */
  @javax.annotation.Nullable
  public Boolean getIsMergedHorozontal() {
    return isMergedHorozontal;
  }

  public void setIsMergedHorozontal(Boolean isMergedHorozontal) {
    this.isMergedHorozontal = isMergedHorozontal;
  }


  public TableCells isMergedVertical(Boolean isMergedVertical) {
    this.isMergedVertical = isMergedVertical;
    return this;
  }

  /**
   * Get isMergedVertical
   * @return isMergedVertical
   */
  @javax.annotation.Nullable
  public Boolean getIsMergedVertical() {
    return isMergedVertical;
  }

  public void setIsMergedVertical(Boolean isMergedVertical) {
    this.isMergedVertical = isMergedVertical;
  }


  public TableCells rowId(UUID rowId) {
    this.rowId = rowId;
    return this;
  }

  /**
   * Get rowId
   * @return rowId
   */
  @javax.annotation.Nullable
  public UUID getRowId() {
    return rowId;
  }

  public void setRowId(UUID rowId) {
    this.rowId = rowId;
  }


  public TableCells rowSpan(Integer rowSpan) {
    this.rowSpan = rowSpan;
    return this;
  }

  /**
   * Get rowSpan
   * @return rowSpan
   */
  @javax.annotation.Nullable
  public Integer getRowSpan() {
    return rowSpan;
  }

  public void setRowSpan(Integer rowSpan) {
    this.rowSpan = rowSpan;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TableCells tableCells = (TableCells) o;
    return Objects.equals(this.columnId, tableCells.columnId) &&
        Objects.equals(this.columnSpan, tableCells.columnSpan) &&
        Objects.equals(this.id, tableCells.id) &&
        Objects.equals(this.isMergedHorozontal, tableCells.isMergedHorozontal) &&
        Objects.equals(this.isMergedVertical, tableCells.isMergedVertical) &&
        Objects.equals(this.rowId, tableCells.rowId) &&
        Objects.equals(this.rowSpan, tableCells.rowSpan);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(columnId, columnSpan, id, isMergedHorozontal, isMergedVertical, rowId, rowSpan);
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
    sb.append("class TableCells {\n");
    sb.append("    columnId: ").append(toIndentedString(columnId)).append("\n");
    sb.append("    columnSpan: ").append(toIndentedString(columnSpan)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isMergedHorozontal: ").append(toIndentedString(isMergedHorozontal)).append("\n");
    sb.append("    isMergedVertical: ").append(toIndentedString(isMergedVertical)).append("\n");
    sb.append("    rowId: ").append(toIndentedString(rowId)).append("\n");
    sb.append("    rowSpan: ").append(toIndentedString(rowSpan)).append("\n");
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
    openapiFields.add("columnId");
    openapiFields.add("columnSpan");
    openapiFields.add("id");
    openapiFields.add("isMergedHorozontal");
    openapiFields.add("isMergedVertical");
    openapiFields.add("rowId");
    openapiFields.add("rowSpan");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TableCells
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TableCells.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TableCells is not found in the empty JSON string", TableCells.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TableCells.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TableCells` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("columnId") != null && !jsonObj.get("columnId").isJsonNull()) && !jsonObj.get("columnId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `columnId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("columnId").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("rowId") != null && !jsonObj.get("rowId").isJsonNull()) && !jsonObj.get("rowId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rowId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rowId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TableCells.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TableCells' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TableCells> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TableCells.class));

       return (TypeAdapter<T>) new TypeAdapter<TableCells>() {
           @Override
           public void write(JsonWriter out, TableCells value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TableCells read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TableCells given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TableCells
   * @throws IOException if the JSON string is invalid with respect to TableCells
   */
  public static TableCells fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TableCells.class);
  }

  /**
   * Convert an instance of TableCells to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

