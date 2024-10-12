/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
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
import java.util.UUID;
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
 * ThemeThemes
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ThemeThemes {
  public static final String SERIALIZED_NAME_BASE_ELEMENT_BLOB_URL = "baseElementBlobUrl";
  @SerializedName(SERIALIZED_NAME_BASE_ELEMENT_BLOB_URL)
  private String baseElementBlobUrl;

  public static final String SERIALIZED_NAME_CHANGED_BASE_ELEMENT_BLOB_URL = "changedBaseElementBlobUrl";
  @SerializedName(SERIALIZED_NAME_CHANGED_BASE_ELEMENT_BLOB_URL)
  private String changedBaseElementBlobUrl;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PACKAGE_URI = "packageUri";
  @SerializedName(SERIALIZED_NAME_PACKAGE_URI)
  private String packageUri;

  public static final String SERIALIZED_NAME_SLIDE_ID = "slideId";
  @SerializedName(SERIALIZED_NAME_SLIDE_ID)
  private UUID slideId;

  public ThemeThemes() {
  }

  public ThemeThemes baseElementBlobUrl(String baseElementBlobUrl) {
    this.baseElementBlobUrl = baseElementBlobUrl;
    return this;
  }

  /**
   * Get baseElementBlobUrl
   * @return baseElementBlobUrl
   */
  @javax.annotation.Nullable
  public String getBaseElementBlobUrl() {
    return baseElementBlobUrl;
  }

  public void setBaseElementBlobUrl(String baseElementBlobUrl) {
    this.baseElementBlobUrl = baseElementBlobUrl;
  }


  public ThemeThemes changedBaseElementBlobUrl(String changedBaseElementBlobUrl) {
    this.changedBaseElementBlobUrl = changedBaseElementBlobUrl;
    return this;
  }

  /**
   * Get changedBaseElementBlobUrl
   * @return changedBaseElementBlobUrl
   */
  @javax.annotation.Nullable
  public String getChangedBaseElementBlobUrl() {
    return changedBaseElementBlobUrl;
  }

  public void setChangedBaseElementBlobUrl(String changedBaseElementBlobUrl) {
    this.changedBaseElementBlobUrl = changedBaseElementBlobUrl;
  }


  public ThemeThemes id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public ThemeThemes name(String name) {
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


  public ThemeThemes packageUri(String packageUri) {
    this.packageUri = packageUri;
    return this;
  }

  /**
   * Get packageUri
   * @return packageUri
   */
  @javax.annotation.Nullable
  public String getPackageUri() {
    return packageUri;
  }

  public void setPackageUri(String packageUri) {
    this.packageUri = packageUri;
  }


  public ThemeThemes slideId(UUID slideId) {
    this.slideId = slideId;
    return this;
  }

  /**
   * Get slideId
   * @return slideId
   */
  @javax.annotation.Nullable
  public UUID getSlideId() {
    return slideId;
  }

  public void setSlideId(UUID slideId) {
    this.slideId = slideId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ThemeThemes themeThemes = (ThemeThemes) o;
    return Objects.equals(this.baseElementBlobUrl, themeThemes.baseElementBlobUrl) &&
        Objects.equals(this.changedBaseElementBlobUrl, themeThemes.changedBaseElementBlobUrl) &&
        Objects.equals(this.id, themeThemes.id) &&
        Objects.equals(this.name, themeThemes.name) &&
        Objects.equals(this.packageUri, themeThemes.packageUri) &&
        Objects.equals(this.slideId, themeThemes.slideId);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(baseElementBlobUrl, changedBaseElementBlobUrl, id, name, packageUri, slideId);
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
    sb.append("class ThemeThemes {\n");
    sb.append("    baseElementBlobUrl: ").append(toIndentedString(baseElementBlobUrl)).append("\n");
    sb.append("    changedBaseElementBlobUrl: ").append(toIndentedString(changedBaseElementBlobUrl)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    packageUri: ").append(toIndentedString(packageUri)).append("\n");
    sb.append("    slideId: ").append(toIndentedString(slideId)).append("\n");
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
    openapiFields.add("baseElementBlobUrl");
    openapiFields.add("changedBaseElementBlobUrl");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("packageUri");
    openapiFields.add("slideId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ThemeThemes
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ThemeThemes.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ThemeThemes is not found in the empty JSON string", ThemeThemes.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ThemeThemes.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ThemeThemes` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("baseElementBlobUrl") != null && !jsonObj.get("baseElementBlobUrl").isJsonNull()) && !jsonObj.get("baseElementBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `baseElementBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("baseElementBlobUrl").toString()));
      }
      if ((jsonObj.get("changedBaseElementBlobUrl") != null && !jsonObj.get("changedBaseElementBlobUrl").isJsonNull()) && !jsonObj.get("changedBaseElementBlobUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changedBaseElementBlobUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changedBaseElementBlobUrl").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("packageUri") != null && !jsonObj.get("packageUri").isJsonNull()) && !jsonObj.get("packageUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `packageUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("packageUri").toString()));
      }
      if ((jsonObj.get("slideId") != null && !jsonObj.get("slideId").isJsonNull()) && !jsonObj.get("slideId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `slideId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("slideId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ThemeThemes.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ThemeThemes' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ThemeThemes> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ThemeThemes.class));

       return (TypeAdapter<T>) new TypeAdapter<ThemeThemes>() {
           @Override
           public void write(JsonWriter out, ThemeThemes value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ThemeThemes read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ThemeThemes given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ThemeThemes
   * @throws IOException if the JSON string is invalid with respect to ThemeThemes
   */
  public static ThemeThemes fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ThemeThemes.class);
  }

  /**
   * Convert an instance of ThemeThemes to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

