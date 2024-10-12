/*
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
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
 * PhotoURLs
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:49.490227-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PhotoURLs {
  public static final String SERIALIZED_NAME_H = "h";
  @SerializedName(SERIALIZED_NAME_H)
  private String h;

  public static final String SERIALIZED_NAME_L = "l";
  @SerializedName(SERIALIZED_NAME_L)
  private String l;

  public static final String SERIALIZED_NAME_S = "s";
  @SerializedName(SERIALIZED_NAME_S)
  private String s;

  public static final String SERIALIZED_NAME_T = "t";
  @SerializedName(SERIALIZED_NAME_T)
  private String t;

  public PhotoURLs() {
  }

  public PhotoURLs h(String h) {
    this.h = h;
    return this;
  }

  /**
   * Get h
   * @return h
   */
  @javax.annotation.Nullable
  public String getH() {
    return h;
  }

  public void setH(String h) {
    this.h = h;
  }


  public PhotoURLs l(String l) {
    this.l = l;
    return this;
  }

  /**
   * Get l
   * @return l
   */
  @javax.annotation.Nullable
  public String getL() {
    return l;
  }

  public void setL(String l) {
    this.l = l;
  }


  public PhotoURLs s(String s) {
    this.s = s;
    return this;
  }

  /**
   * Get s
   * @return s
   */
  @javax.annotation.Nullable
  public String getS() {
    return s;
  }

  public void setS(String s) {
    this.s = s;
  }


  public PhotoURLs t(String t) {
    this.t = t;
    return this;
  }

  /**
   * Get t
   * @return t
   */
  @javax.annotation.Nullable
  public String getT() {
    return t;
  }

  public void setT(String t) {
    this.t = t;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PhotoURLs photoURLs = (PhotoURLs) o;
    return Objects.equals(this.h, photoURLs.h) &&
        Objects.equals(this.l, photoURLs.l) &&
        Objects.equals(this.s, photoURLs.s) &&
        Objects.equals(this.t, photoURLs.t);
  }

  @Override
  public int hashCode() {
    return Objects.hash(h, l, s, t);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PhotoURLs {\n");
    sb.append("    h: ").append(toIndentedString(h)).append("\n");
    sb.append("    l: ").append(toIndentedString(l)).append("\n");
    sb.append("    s: ").append(toIndentedString(s)).append("\n");
    sb.append("    t: ").append(toIndentedString(t)).append("\n");
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
    openapiFields.add("h");
    openapiFields.add("l");
    openapiFields.add("s");
    openapiFields.add("t");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PhotoURLs
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PhotoURLs.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PhotoURLs is not found in the empty JSON string", PhotoURLs.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PhotoURLs.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PhotoURLs` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("h") != null && !jsonObj.get("h").isJsonNull()) && !jsonObj.get("h").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `h` to be a primitive type in the JSON string but got `%s`", jsonObj.get("h").toString()));
      }
      if ((jsonObj.get("l") != null && !jsonObj.get("l").isJsonNull()) && !jsonObj.get("l").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `l` to be a primitive type in the JSON string but got `%s`", jsonObj.get("l").toString()));
      }
      if ((jsonObj.get("s") != null && !jsonObj.get("s").isJsonNull()) && !jsonObj.get("s").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `s` to be a primitive type in the JSON string but got `%s`", jsonObj.get("s").toString()));
      }
      if ((jsonObj.get("t") != null && !jsonObj.get("t").isJsonNull()) && !jsonObj.get("t").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `t` to be a primitive type in the JSON string but got `%s`", jsonObj.get("t").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PhotoURLs.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PhotoURLs' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PhotoURLs> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PhotoURLs.class));

       return (TypeAdapter<T>) new TypeAdapter<PhotoURLs>() {
           @Override
           public void write(JsonWriter out, PhotoURLs value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PhotoURLs read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PhotoURLs given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PhotoURLs
   * @throws IOException if the JSON string is invalid with respect to PhotoURLs
   */
  public static PhotoURLs fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PhotoURLs.class);
  }

  /**
   * Convert an instance of PhotoURLs to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

