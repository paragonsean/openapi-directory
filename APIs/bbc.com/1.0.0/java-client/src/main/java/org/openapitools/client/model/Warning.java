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
 * Warning
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Warning {
  public static final String SERIALIZED_NAME_HASH_TEXT = "#text";
  @SerializedName(SERIALIZED_NAME_HASH_TEXT)
  private String hashText;

  public static final String SERIALIZED_NAME_SHORT_DESCRIPTION = "short_description";
  @SerializedName(SERIALIZED_NAME_SHORT_DESCRIPTION)
  private String shortDescription;

  public static final String SERIALIZED_NAME_WARNING_CODE = "warning_code";
  @SerializedName(SERIALIZED_NAME_WARNING_CODE)
  private String warningCode;

  public Warning() {
  }

  public Warning hashText(String hashText) {
    this.hashText = hashText;
    return this;
  }

  /**
   * Get hashText
   * @return hashText
   */
  @javax.annotation.Nullable
  public String getHashText() {
    return hashText;
  }

  public void setHashText(String hashText) {
    this.hashText = hashText;
  }


  public Warning shortDescription(String shortDescription) {
    this.shortDescription = shortDescription;
    return this;
  }

  /**
   * Get shortDescription
   * @return shortDescription
   */
  @javax.annotation.Nullable
  public String getShortDescription() {
    return shortDescription;
  }

  public void setShortDescription(String shortDescription) {
    this.shortDescription = shortDescription;
  }


  public Warning warningCode(String warningCode) {
    this.warningCode = warningCode;
    return this;
  }

  /**
   * Get warningCode
   * @return warningCode
   */
  @javax.annotation.Nullable
  public String getWarningCode() {
    return warningCode;
  }

  public void setWarningCode(String warningCode) {
    this.warningCode = warningCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Warning warning = (Warning) o;
    return Objects.equals(this.hashText, warning.hashText) &&
        Objects.equals(this.shortDescription, warning.shortDescription) &&
        Objects.equals(this.warningCode, warning.warningCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hashText, shortDescription, warningCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Warning {\n");
    sb.append("    hashText: ").append(toIndentedString(hashText)).append("\n");
    sb.append("    shortDescription: ").append(toIndentedString(shortDescription)).append("\n");
    sb.append("    warningCode: ").append(toIndentedString(warningCode)).append("\n");
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
    openapiFields.add("#text");
    openapiFields.add("short_description");
    openapiFields.add("warning_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Warning
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Warning.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Warning is not found in the empty JSON string", Warning.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Warning.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Warning` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("#text") != null && !jsonObj.get("#text").isJsonNull()) && !jsonObj.get("#text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `#text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("#text").toString()));
      }
      if ((jsonObj.get("short_description") != null && !jsonObj.get("short_description").isJsonNull()) && !jsonObj.get("short_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `short_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("short_description").toString()));
      }
      if ((jsonObj.get("warning_code") != null && !jsonObj.get("warning_code").isJsonNull()) && !jsonObj.get("warning_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `warning_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("warning_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Warning.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Warning' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Warning> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Warning.class));

       return (TypeAdapter<T>) new TypeAdapter<Warning>() {
           @Override
           public void write(JsonWriter out, Warning value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Warning read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Warning given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Warning
   * @throws IOException if the JSON string is invalid with respect to Warning
   */
  public static Warning fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Warning.class);
  }

  /**
   * Convert an instance of Warning to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

