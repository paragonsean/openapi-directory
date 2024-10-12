/*
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
import org.openapitools.client.model.GuidanceWarningsWarningsWarnings;
import org.openapitools.client.model.WarningItems;
import org.openapitools.client.model.WarningTexts;

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
 * GuidanceWarningsWarnings
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GuidanceWarningsWarnings {
  public static final String SERIALIZED_NAME_WARNING_ITEMS = "warning_items";
  @SerializedName(SERIALIZED_NAME_WARNING_ITEMS)
  private WarningItems warningItems;

  public static final String SERIALIZED_NAME_WARNING_TEXTS = "warning_texts";
  @SerializedName(SERIALIZED_NAME_WARNING_TEXTS)
  private WarningTexts warningTexts;

  public static final String SERIALIZED_NAME_WARNINGS = "warnings";
  @SerializedName(SERIALIZED_NAME_WARNINGS)
  private GuidanceWarningsWarningsWarnings warnings;

  public GuidanceWarningsWarnings() {
  }

  public GuidanceWarningsWarnings warningItems(WarningItems warningItems) {
    this.warningItems = warningItems;
    return this;
  }

  /**
   * Get warningItems
   * @return warningItems
   */
  @javax.annotation.Nullable
  public WarningItems getWarningItems() {
    return warningItems;
  }

  public void setWarningItems(WarningItems warningItems) {
    this.warningItems = warningItems;
  }


  public GuidanceWarningsWarnings warningTexts(WarningTexts warningTexts) {
    this.warningTexts = warningTexts;
    return this;
  }

  /**
   * Get warningTexts
   * @return warningTexts
   */
  @javax.annotation.Nullable
  public WarningTexts getWarningTexts() {
    return warningTexts;
  }

  public void setWarningTexts(WarningTexts warningTexts) {
    this.warningTexts = warningTexts;
  }


  public GuidanceWarningsWarnings warnings(GuidanceWarningsWarningsWarnings warnings) {
    this.warnings = warnings;
    return this;
  }

  /**
   * Get warnings
   * @return warnings
   */
  @javax.annotation.Nullable
  public GuidanceWarningsWarningsWarnings getWarnings() {
    return warnings;
  }

  public void setWarnings(GuidanceWarningsWarningsWarnings warnings) {
    this.warnings = warnings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GuidanceWarningsWarnings guidanceWarningsWarnings = (GuidanceWarningsWarnings) o;
    return Objects.equals(this.warningItems, guidanceWarningsWarnings.warningItems) &&
        Objects.equals(this.warningTexts, guidanceWarningsWarnings.warningTexts) &&
        Objects.equals(this.warnings, guidanceWarningsWarnings.warnings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(warningItems, warningTexts, warnings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GuidanceWarningsWarnings {\n");
    sb.append("    warningItems: ").append(toIndentedString(warningItems)).append("\n");
    sb.append("    warningTexts: ").append(toIndentedString(warningTexts)).append("\n");
    sb.append("    warnings: ").append(toIndentedString(warnings)).append("\n");
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
    openapiFields.add("warning_items");
    openapiFields.add("warning_texts");
    openapiFields.add("warnings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GuidanceWarningsWarnings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GuidanceWarningsWarnings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GuidanceWarningsWarnings is not found in the empty JSON string", GuidanceWarningsWarnings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GuidanceWarningsWarnings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GuidanceWarningsWarnings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `warning_items`
      if (jsonObj.get("warning_items") != null && !jsonObj.get("warning_items").isJsonNull()) {
        WarningItems.validateJsonElement(jsonObj.get("warning_items"));
      }
      // validate the optional field `warning_texts`
      if (jsonObj.get("warning_texts") != null && !jsonObj.get("warning_texts").isJsonNull()) {
        WarningTexts.validateJsonElement(jsonObj.get("warning_texts"));
      }
      // validate the optional field `warnings`
      if (jsonObj.get("warnings") != null && !jsonObj.get("warnings").isJsonNull()) {
        GuidanceWarningsWarningsWarnings.validateJsonElement(jsonObj.get("warnings"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GuidanceWarningsWarnings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GuidanceWarningsWarnings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GuidanceWarningsWarnings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GuidanceWarningsWarnings.class));

       return (TypeAdapter<T>) new TypeAdapter<GuidanceWarningsWarnings>() {
           @Override
           public void write(JsonWriter out, GuidanceWarningsWarnings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GuidanceWarningsWarnings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GuidanceWarningsWarnings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GuidanceWarningsWarnings
   * @throws IOException if the JSON string is invalid with respect to GuidanceWarningsWarnings
   */
  public static GuidanceWarningsWarnings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GuidanceWarningsWarnings.class);
  }

  /**
   * Convert an instance of GuidanceWarningsWarnings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

