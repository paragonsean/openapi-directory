/*
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
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
 * EntryThumbForApiContract
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:40.974326-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EntryThumbForApiContract {
  public static final String SERIALIZED_NAME_MIME = "mime";
  @SerializedName(SERIALIZED_NAME_MIME)
  private String mime;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_URL_ORIGINAL = "urlOriginal";
  @SerializedName(SERIALIZED_NAME_URL_ORIGINAL)
  private String urlOriginal;

  public static final String SERIALIZED_NAME_URL_SMALL_THUMB = "urlSmallThumb";
  @SerializedName(SERIALIZED_NAME_URL_SMALL_THUMB)
  private String urlSmallThumb;

  public static final String SERIALIZED_NAME_URL_THUMB = "urlThumb";
  @SerializedName(SERIALIZED_NAME_URL_THUMB)
  private String urlThumb;

  public static final String SERIALIZED_NAME_URL_TINY_THUMB = "urlTinyThumb";
  @SerializedName(SERIALIZED_NAME_URL_TINY_THUMB)
  private String urlTinyThumb;

  public EntryThumbForApiContract() {
  }

  public EntryThumbForApiContract mime(String mime) {
    this.mime = mime;
    return this;
  }

  /**
   * Get mime
   * @return mime
   */
  @javax.annotation.Nullable
  public String getMime() {
    return mime;
  }

  public void setMime(String mime) {
    this.mime = mime;
  }


  public EntryThumbForApiContract name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public EntryThumbForApiContract urlOriginal(String urlOriginal) {
    this.urlOriginal = urlOriginal;
    return this;
  }

  /**
   * Get urlOriginal
   * @return urlOriginal
   */
  @javax.annotation.Nullable
  public String getUrlOriginal() {
    return urlOriginal;
  }

  public void setUrlOriginal(String urlOriginal) {
    this.urlOriginal = urlOriginal;
  }


  public EntryThumbForApiContract urlSmallThumb(String urlSmallThumb) {
    this.urlSmallThumb = urlSmallThumb;
    return this;
  }

  /**
   * Get urlSmallThumb
   * @return urlSmallThumb
   */
  @javax.annotation.Nullable
  public String getUrlSmallThumb() {
    return urlSmallThumb;
  }

  public void setUrlSmallThumb(String urlSmallThumb) {
    this.urlSmallThumb = urlSmallThumb;
  }


  public EntryThumbForApiContract urlThumb(String urlThumb) {
    this.urlThumb = urlThumb;
    return this;
  }

  /**
   * Get urlThumb
   * @return urlThumb
   */
  @javax.annotation.Nullable
  public String getUrlThumb() {
    return urlThumb;
  }

  public void setUrlThumb(String urlThumb) {
    this.urlThumb = urlThumb;
  }


  public EntryThumbForApiContract urlTinyThumb(String urlTinyThumb) {
    this.urlTinyThumb = urlTinyThumb;
    return this;
  }

  /**
   * Get urlTinyThumb
   * @return urlTinyThumb
   */
  @javax.annotation.Nullable
  public String getUrlTinyThumb() {
    return urlTinyThumb;
  }

  public void setUrlTinyThumb(String urlTinyThumb) {
    this.urlTinyThumb = urlTinyThumb;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EntryThumbForApiContract entryThumbForApiContract = (EntryThumbForApiContract) o;
    return Objects.equals(this.mime, entryThumbForApiContract.mime) &&
        Objects.equals(this.name, entryThumbForApiContract.name) &&
        Objects.equals(this.urlOriginal, entryThumbForApiContract.urlOriginal) &&
        Objects.equals(this.urlSmallThumb, entryThumbForApiContract.urlSmallThumb) &&
        Objects.equals(this.urlThumb, entryThumbForApiContract.urlThumb) &&
        Objects.equals(this.urlTinyThumb, entryThumbForApiContract.urlTinyThumb);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(mime, name, urlOriginal, urlSmallThumb, urlThumb, urlTinyThumb);
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
    sb.append("class EntryThumbForApiContract {\n");
    sb.append("    mime: ").append(toIndentedString(mime)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    urlOriginal: ").append(toIndentedString(urlOriginal)).append("\n");
    sb.append("    urlSmallThumb: ").append(toIndentedString(urlSmallThumb)).append("\n");
    sb.append("    urlThumb: ").append(toIndentedString(urlThumb)).append("\n");
    sb.append("    urlTinyThumb: ").append(toIndentedString(urlTinyThumb)).append("\n");
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
    openapiFields.add("mime");
    openapiFields.add("name");
    openapiFields.add("urlOriginal");
    openapiFields.add("urlSmallThumb");
    openapiFields.add("urlThumb");
    openapiFields.add("urlTinyThumb");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EntryThumbForApiContract
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EntryThumbForApiContract.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EntryThumbForApiContract is not found in the empty JSON string", EntryThumbForApiContract.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EntryThumbForApiContract.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EntryThumbForApiContract` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("mime") != null && !jsonObj.get("mime").isJsonNull()) && !jsonObj.get("mime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mime").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("urlOriginal") != null && !jsonObj.get("urlOriginal").isJsonNull()) && !jsonObj.get("urlOriginal").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlOriginal` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlOriginal").toString()));
      }
      if ((jsonObj.get("urlSmallThumb") != null && !jsonObj.get("urlSmallThumb").isJsonNull()) && !jsonObj.get("urlSmallThumb").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlSmallThumb` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlSmallThumb").toString()));
      }
      if ((jsonObj.get("urlThumb") != null && !jsonObj.get("urlThumb").isJsonNull()) && !jsonObj.get("urlThumb").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlThumb` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlThumb").toString()));
      }
      if ((jsonObj.get("urlTinyThumb") != null && !jsonObj.get("urlTinyThumb").isJsonNull()) && !jsonObj.get("urlTinyThumb").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlTinyThumb` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlTinyThumb").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EntryThumbForApiContract.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EntryThumbForApiContract' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EntryThumbForApiContract> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EntryThumbForApiContract.class));

       return (TypeAdapter<T>) new TypeAdapter<EntryThumbForApiContract>() {
           @Override
           public void write(JsonWriter out, EntryThumbForApiContract value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EntryThumbForApiContract read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EntryThumbForApiContract given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EntryThumbForApiContract
   * @throws IOException if the JSON string is invalid with respect to EntryThumbForApiContract
   */
  public static EntryThumbForApiContract fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EntryThumbForApiContract.class);
  }

  /**
   * Convert an instance of EntryThumbForApiContract to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

