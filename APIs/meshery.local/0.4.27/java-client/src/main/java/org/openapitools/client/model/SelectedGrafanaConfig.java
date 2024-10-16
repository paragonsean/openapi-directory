/*
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
import org.openapitools.client.model.GrafanaBoard;
import org.openapitools.client.model.Panel;

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
 * SelectedGrafanaConfig represents the selected boards, panels, and template variables
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:51.881749-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SelectedGrafanaConfig {
  public static final String SERIALIZED_NAME_BOARD = "board";
  @SerializedName(SERIALIZED_NAME_BOARD)
  private GrafanaBoard board;

  public static final String SERIALIZED_NAME_PANELS = "panels";
  @SerializedName(SERIALIZED_NAME_PANELS)
  private List<Panel> panels = new ArrayList<>();

  public static final String SERIALIZED_NAME_TEMPLATE_VARS = "templateVars";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_VARS)
  private List<String> templateVars = new ArrayList<>();

  public SelectedGrafanaConfig() {
  }

  public SelectedGrafanaConfig board(GrafanaBoard board) {
    this.board = board;
    return this;
  }

  /**
   * Get board
   * @return board
   */
  @javax.annotation.Nullable
  public GrafanaBoard getBoard() {
    return board;
  }

  public void setBoard(GrafanaBoard board) {
    this.board = board;
  }


  public SelectedGrafanaConfig panels(List<Panel> panels) {
    this.panels = panels;
    return this;
  }

  public SelectedGrafanaConfig addPanelsItem(Panel panelsItem) {
    if (this.panels == null) {
      this.panels = new ArrayList<>();
    }
    this.panels.add(panelsItem);
    return this;
  }

  /**
   * Get panels
   * @return panels
   */
  @javax.annotation.Nullable
  public List<Panel> getPanels() {
    return panels;
  }

  public void setPanels(List<Panel> panels) {
    this.panels = panels;
  }


  public SelectedGrafanaConfig templateVars(List<String> templateVars) {
    this.templateVars = templateVars;
    return this;
  }

  public SelectedGrafanaConfig addTemplateVarsItem(String templateVarsItem) {
    if (this.templateVars == null) {
      this.templateVars = new ArrayList<>();
    }
    this.templateVars.add(templateVarsItem);
    return this;
  }

  /**
   * Get templateVars
   * @return templateVars
   */
  @javax.annotation.Nullable
  public List<String> getTemplateVars() {
    return templateVars;
  }

  public void setTemplateVars(List<String> templateVars) {
    this.templateVars = templateVars;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SelectedGrafanaConfig selectedGrafanaConfig = (SelectedGrafanaConfig) o;
    return Objects.equals(this.board, selectedGrafanaConfig.board) &&
        Objects.equals(this.panels, selectedGrafanaConfig.panels) &&
        Objects.equals(this.templateVars, selectedGrafanaConfig.templateVars);
  }

  @Override
  public int hashCode() {
    return Objects.hash(board, panels, templateVars);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SelectedGrafanaConfig {\n");
    sb.append("    board: ").append(toIndentedString(board)).append("\n");
    sb.append("    panels: ").append(toIndentedString(panels)).append("\n");
    sb.append("    templateVars: ").append(toIndentedString(templateVars)).append("\n");
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
    openapiFields.add("board");
    openapiFields.add("panels");
    openapiFields.add("templateVars");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SelectedGrafanaConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SelectedGrafanaConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SelectedGrafanaConfig is not found in the empty JSON string", SelectedGrafanaConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SelectedGrafanaConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SelectedGrafanaConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `board`
      if (jsonObj.get("board") != null && !jsonObj.get("board").isJsonNull()) {
        GrafanaBoard.validateJsonElement(jsonObj.get("board"));
      }
      if (jsonObj.get("panels") != null && !jsonObj.get("panels").isJsonNull()) {
        JsonArray jsonArraypanels = jsonObj.getAsJsonArray("panels");
        if (jsonArraypanels != null) {
          // ensure the json data is an array
          if (!jsonObj.get("panels").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `panels` to be an array in the JSON string but got `%s`", jsonObj.get("panels").toString()));
          }

          // validate the optional field `panels` (array)
          for (int i = 0; i < jsonArraypanels.size(); i++) {
            Panel.validateJsonElement(jsonArraypanels.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("templateVars") != null && !jsonObj.get("templateVars").isJsonNull() && !jsonObj.get("templateVars").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `templateVars` to be an array in the JSON string but got `%s`", jsonObj.get("templateVars").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SelectedGrafanaConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SelectedGrafanaConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SelectedGrafanaConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SelectedGrafanaConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<SelectedGrafanaConfig>() {
           @Override
           public void write(JsonWriter out, SelectedGrafanaConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SelectedGrafanaConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SelectedGrafanaConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SelectedGrafanaConfig
   * @throws IOException if the JSON string is invalid with respect to SelectedGrafanaConfig
   */
  public static SelectedGrafanaConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SelectedGrafanaConfig.class);
  }

  /**
   * Convert an instance of SelectedGrafanaConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

