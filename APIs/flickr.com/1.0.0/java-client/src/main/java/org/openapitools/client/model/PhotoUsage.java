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
 * PhotoUsage
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:49.490227-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PhotoUsage {
  public static final String SERIALIZED_NAME_CANBLOG = "canblog";
  @SerializedName(SERIALIZED_NAME_CANBLOG)
  private Boolean canblog;

  public static final String SERIALIZED_NAME_CANDOWNLOAD = "candownload";
  @SerializedName(SERIALIZED_NAME_CANDOWNLOAD)
  private Boolean candownload;

  public static final String SERIALIZED_NAME_CANPRINT = "canprint";
  @SerializedName(SERIALIZED_NAME_CANPRINT)
  private Boolean canprint;

  public static final String SERIALIZED_NAME_CANSHARE = "canshare";
  @SerializedName(SERIALIZED_NAME_CANSHARE)
  private Boolean canshare;

  public PhotoUsage() {
  }

  public PhotoUsage canblog(Boolean canblog) {
    this.canblog = canblog;
    return this;
  }

  /**
   * Get canblog
   * @return canblog
   */
  @javax.annotation.Nullable
  public Boolean getCanblog() {
    return canblog;
  }

  public void setCanblog(Boolean canblog) {
    this.canblog = canblog;
  }


  public PhotoUsage candownload(Boolean candownload) {
    this.candownload = candownload;
    return this;
  }

  /**
   * Get candownload
   * @return candownload
   */
  @javax.annotation.Nullable
  public Boolean getCandownload() {
    return candownload;
  }

  public void setCandownload(Boolean candownload) {
    this.candownload = candownload;
  }


  public PhotoUsage canprint(Boolean canprint) {
    this.canprint = canprint;
    return this;
  }

  /**
   * Get canprint
   * @return canprint
   */
  @javax.annotation.Nullable
  public Boolean getCanprint() {
    return canprint;
  }

  public void setCanprint(Boolean canprint) {
    this.canprint = canprint;
  }


  public PhotoUsage canshare(Boolean canshare) {
    this.canshare = canshare;
    return this;
  }

  /**
   * Get canshare
   * @return canshare
   */
  @javax.annotation.Nullable
  public Boolean getCanshare() {
    return canshare;
  }

  public void setCanshare(Boolean canshare) {
    this.canshare = canshare;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PhotoUsage photoUsage = (PhotoUsage) o;
    return Objects.equals(this.canblog, photoUsage.canblog) &&
        Objects.equals(this.candownload, photoUsage.candownload) &&
        Objects.equals(this.canprint, photoUsage.canprint) &&
        Objects.equals(this.canshare, photoUsage.canshare);
  }

  @Override
  public int hashCode() {
    return Objects.hash(canblog, candownload, canprint, canshare);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PhotoUsage {\n");
    sb.append("    canblog: ").append(toIndentedString(canblog)).append("\n");
    sb.append("    candownload: ").append(toIndentedString(candownload)).append("\n");
    sb.append("    canprint: ").append(toIndentedString(canprint)).append("\n");
    sb.append("    canshare: ").append(toIndentedString(canshare)).append("\n");
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
    openapiFields.add("canblog");
    openapiFields.add("candownload");
    openapiFields.add("canprint");
    openapiFields.add("canshare");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PhotoUsage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PhotoUsage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PhotoUsage is not found in the empty JSON string", PhotoUsage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PhotoUsage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PhotoUsage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PhotoUsage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PhotoUsage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PhotoUsage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PhotoUsage.class));

       return (TypeAdapter<T>) new TypeAdapter<PhotoUsage>() {
           @Override
           public void write(JsonWriter out, PhotoUsage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PhotoUsage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PhotoUsage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PhotoUsage
   * @throws IOException if the JSON string is invalid with respect to PhotoUsage
   */
  public static PhotoUsage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PhotoUsage.class);
  }

  /**
   * Convert an instance of PhotoUsage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

