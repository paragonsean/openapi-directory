/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
 * GroupMessageText
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:21.899808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GroupMessageText {
  public static final String SERIALIZED_NAME_PARSED = "parsed";
  @SerializedName(SERIALIZED_NAME_PARSED)
  private String parsed;

  public GroupMessageText() {
  }

  public GroupMessageText parsed(String parsed) {
    this.parsed = parsed;
    return this;
  }

  /**
   * Get parsed
   * @return parsed
   */
  @javax.annotation.Nullable
  public String getParsed() {
    return parsed;
  }

  public void setParsed(String parsed) {
    this.parsed = parsed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GroupMessageText groupMessageText = (GroupMessageText) o;
    return Objects.equals(this.parsed, groupMessageText.parsed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(parsed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GroupMessageText {\n");
    sb.append("    parsed: ").append(toIndentedString(parsed)).append("\n");
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
    openapiFields.add("parsed");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GroupMessageText
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GroupMessageText.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GroupMessageText is not found in the empty JSON string", GroupMessageText.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GroupMessageText.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GroupMessageText` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("parsed") != null && !jsonObj.get("parsed").isJsonNull()) && !jsonObj.get("parsed").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parsed` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parsed").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GroupMessageText.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GroupMessageText' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GroupMessageText> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GroupMessageText.class));

       return (TypeAdapter<T>) new TypeAdapter<GroupMessageText>() {
           @Override
           public void write(JsonWriter out, GroupMessageText value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GroupMessageText read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GroupMessageText given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GroupMessageText
   * @throws IOException if the JSON string is invalid with respect to GroupMessageText
   */
  public static GroupMessageText fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GroupMessageText.class);
  }

  /**
   * Convert an instance of GroupMessageText to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

