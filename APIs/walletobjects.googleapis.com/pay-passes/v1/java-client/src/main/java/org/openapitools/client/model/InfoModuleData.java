/*
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import org.openapitools.client.model.LabelValueRow;

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
 * InfoModuleData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:07.622305-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InfoModuleData {
  public static final String SERIALIZED_NAME_LABEL_VALUE_ROWS = "labelValueRows";
  @SerializedName(SERIALIZED_NAME_LABEL_VALUE_ROWS)
  private List<LabelValueRow> labelValueRows = new ArrayList<>();

  public static final String SERIALIZED_NAME_SHOW_LAST_UPDATE_TIME = "showLastUpdateTime";
  @SerializedName(SERIALIZED_NAME_SHOW_LAST_UPDATE_TIME)
  private Boolean showLastUpdateTime;

  public InfoModuleData() {
  }

  public InfoModuleData labelValueRows(List<LabelValueRow> labelValueRows) {
    this.labelValueRows = labelValueRows;
    return this;
  }

  public InfoModuleData addLabelValueRowsItem(LabelValueRow labelValueRowsItem) {
    if (this.labelValueRows == null) {
      this.labelValueRows = new ArrayList<>();
    }
    this.labelValueRows.add(labelValueRowsItem);
    return this;
  }

  /**
   * A list of collections of labels and values. These will be displayed one after the other in a singular column.
   * @return labelValueRows
   */
  @javax.annotation.Nullable
  public List<LabelValueRow> getLabelValueRows() {
    return labelValueRows;
  }

  public void setLabelValueRows(List<LabelValueRow> labelValueRows) {
    this.labelValueRows = labelValueRows;
  }


  public InfoModuleData showLastUpdateTime(Boolean showLastUpdateTime) {
    this.showLastUpdateTime = showLastUpdateTime;
    return this;
  }

  /**
   * Get showLastUpdateTime
   * @return showLastUpdateTime
   */
  @javax.annotation.Nullable
  public Boolean getShowLastUpdateTime() {
    return showLastUpdateTime;
  }

  public void setShowLastUpdateTime(Boolean showLastUpdateTime) {
    this.showLastUpdateTime = showLastUpdateTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InfoModuleData infoModuleData = (InfoModuleData) o;
    return Objects.equals(this.labelValueRows, infoModuleData.labelValueRows) &&
        Objects.equals(this.showLastUpdateTime, infoModuleData.showLastUpdateTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(labelValueRows, showLastUpdateTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InfoModuleData {\n");
    sb.append("    labelValueRows: ").append(toIndentedString(labelValueRows)).append("\n");
    sb.append("    showLastUpdateTime: ").append(toIndentedString(showLastUpdateTime)).append("\n");
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
    openapiFields.add("labelValueRows");
    openapiFields.add("showLastUpdateTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InfoModuleData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InfoModuleData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InfoModuleData is not found in the empty JSON string", InfoModuleData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InfoModuleData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InfoModuleData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("labelValueRows") != null && !jsonObj.get("labelValueRows").isJsonNull()) {
        JsonArray jsonArraylabelValueRows = jsonObj.getAsJsonArray("labelValueRows");
        if (jsonArraylabelValueRows != null) {
          // ensure the json data is an array
          if (!jsonObj.get("labelValueRows").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `labelValueRows` to be an array in the JSON string but got `%s`", jsonObj.get("labelValueRows").toString()));
          }

          // validate the optional field `labelValueRows` (array)
          for (int i = 0; i < jsonArraylabelValueRows.size(); i++) {
            LabelValueRow.validateJsonElement(jsonArraylabelValueRows.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InfoModuleData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InfoModuleData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InfoModuleData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InfoModuleData.class));

       return (TypeAdapter<T>) new TypeAdapter<InfoModuleData>() {
           @Override
           public void write(JsonWriter out, InfoModuleData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InfoModuleData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InfoModuleData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InfoModuleData
   * @throws IOException if the JSON string is invalid with respect to InfoModuleData
   */
  public static InfoModuleData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InfoModuleData.class);
  }

  /**
   * Convert an instance of InfoModuleData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

