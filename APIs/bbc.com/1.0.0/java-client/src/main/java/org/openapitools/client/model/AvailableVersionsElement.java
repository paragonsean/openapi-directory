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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AvailableVersionsElementVersionInner;

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
 * AvailableVersionsElement
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AvailableVersionsElement {
  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private List<AvailableVersionsElementVersionInner> version = new ArrayList<>();

  public AvailableVersionsElement() {
  }

  public AvailableVersionsElement version(List<AvailableVersionsElementVersionInner> version) {
    this.version = version;
    return this;
  }

  public AvailableVersionsElement addVersionItem(AvailableVersionsElementVersionInner versionItem) {
    if (this.version == null) {
      this.version = new ArrayList<>();
    }
    this.version.add(versionItem);
    return this;
  }

  /**
   * Get version
   * @return version
   */
  @javax.annotation.Nullable
  public List<AvailableVersionsElementVersionInner> getVersion() {
    return version;
  }

  public void setVersion(List<AvailableVersionsElementVersionInner> version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AvailableVersionsElement availableVersionsElement = (AvailableVersionsElement) o;
    return Objects.equals(this.version, availableVersionsElement.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AvailableVersionsElement {\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AvailableVersionsElement
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AvailableVersionsElement.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AvailableVersionsElement is not found in the empty JSON string", AvailableVersionsElement.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AvailableVersionsElement.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AvailableVersionsElement` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) {
        JsonArray jsonArrayversion = jsonObj.getAsJsonArray("version");
        if (jsonArrayversion != null) {
          // ensure the json data is an array
          if (!jsonObj.get("version").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `version` to be an array in the JSON string but got `%s`", jsonObj.get("version").toString()));
          }

          // validate the optional field `version` (array)
          for (int i = 0; i < jsonArrayversion.size(); i++) {
            AvailableVersionsElementVersionInner.validateJsonElement(jsonArrayversion.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AvailableVersionsElement.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AvailableVersionsElement' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AvailableVersionsElement> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AvailableVersionsElement.class));

       return (TypeAdapter<T>) new TypeAdapter<AvailableVersionsElement>() {
           @Override
           public void write(JsonWriter out, AvailableVersionsElement value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AvailableVersionsElement read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AvailableVersionsElement given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AvailableVersionsElement
   * @throws IOException if the JSON string is invalid with respect to AvailableVersionsElement
   */
  public static AvailableVersionsElement fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AvailableVersionsElement.class);
  }

  /**
   * Convert an instance of AvailableVersionsElement to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

