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
 * Id
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Id {
  public static final String SERIALIZED_NAME_HASH_TEXT = "#text";
  @SerializedName(SERIALIZED_NAME_HASH_TEXT)
  private String hashText;

  public static final String SERIALIZED_NAME_AUTHORITY = "authority";
  @SerializedName(SERIALIZED_NAME_AUTHORITY)
  private String authority;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Id() {
  }

  public Id hashText(String hashText) {
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


  public Id authority(String authority) {
    this.authority = authority;
    return this;
  }

  /**
   * Get authority
   * @return authority
   */
  @javax.annotation.Nullable
  public String getAuthority() {
    return authority;
  }

  public void setAuthority(String authority) {
    this.authority = authority;
  }


  public Id type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Id id = (Id) o;
    return Objects.equals(this.hashText, id.hashText) &&
        Objects.equals(this.authority, id.authority) &&
        Objects.equals(this.type, id.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hashText, authority, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Id {\n");
    sb.append("    hashText: ").append(toIndentedString(hashText)).append("\n");
    sb.append("    authority: ").append(toIndentedString(authority)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("authority");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Id
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Id.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Id is not found in the empty JSON string", Id.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Id.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Id` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("#text") != null && !jsonObj.get("#text").isJsonNull()) && !jsonObj.get("#text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `#text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("#text").toString()));
      }
      if ((jsonObj.get("authority") != null && !jsonObj.get("authority").isJsonNull()) && !jsonObj.get("authority").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authority` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authority").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Id.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Id' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Id> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Id.class));

       return (TypeAdapter<T>) new TypeAdapter<Id>() {
           @Override
           public void write(JsonWriter out, Id value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Id read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Id given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Id
   * @throws IOException if the JSON string is invalid with respect to Id
   */
  public static Id fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Id.class);
  }

  /**
   * Convert an instance of Id to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

