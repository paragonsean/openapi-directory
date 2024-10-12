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
import org.openapitools.client.model.AvailableMediaSetsMediaSets;

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
 * AvailableMediaSets
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AvailableMediaSets {
  public static final String SERIALIZED_NAME_MEDIA_SETS = "media_sets";
  @SerializedName(SERIALIZED_NAME_MEDIA_SETS)
  private AvailableMediaSetsMediaSets mediaSets;

  public AvailableMediaSets() {
  }

  public AvailableMediaSets mediaSets(AvailableMediaSetsMediaSets mediaSets) {
    this.mediaSets = mediaSets;
    return this;
  }

  /**
   * Get mediaSets
   * @return mediaSets
   */
  @javax.annotation.Nullable
  public AvailableMediaSetsMediaSets getMediaSets() {
    return mediaSets;
  }

  public void setMediaSets(AvailableMediaSetsMediaSets mediaSets) {
    this.mediaSets = mediaSets;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AvailableMediaSets availableMediaSets = (AvailableMediaSets) o;
    return Objects.equals(this.mediaSets, availableMediaSets.mediaSets);
  }

  @Override
  public int hashCode() {
    return Objects.hash(mediaSets);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AvailableMediaSets {\n");
    sb.append("    mediaSets: ").append(toIndentedString(mediaSets)).append("\n");
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
    openapiFields.add("media_sets");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AvailableMediaSets
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AvailableMediaSets.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AvailableMediaSets is not found in the empty JSON string", AvailableMediaSets.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AvailableMediaSets.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AvailableMediaSets` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `media_sets`
      if (jsonObj.get("media_sets") != null && !jsonObj.get("media_sets").isJsonNull()) {
        AvailableMediaSetsMediaSets.validateJsonElement(jsonObj.get("media_sets"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AvailableMediaSets.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AvailableMediaSets' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AvailableMediaSets> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AvailableMediaSets.class));

       return (TypeAdapter<T>) new TypeAdapter<AvailableMediaSets>() {
           @Override
           public void write(JsonWriter out, AvailableMediaSets value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AvailableMediaSets read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AvailableMediaSets given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AvailableMediaSets
   * @throws IOException if the JSON string is invalid with respect to AvailableMediaSets
   */
  public static AvailableMediaSets fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AvailableMediaSets.class);
  }

  /**
   * Convert an instance of AvailableMediaSets to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

