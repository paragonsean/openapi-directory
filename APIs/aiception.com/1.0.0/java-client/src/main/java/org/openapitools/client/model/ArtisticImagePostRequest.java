/*
 * AIception Interactive
 * Here you can play & test & prototype all the endpoints using just your browser! Go ahead!
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
 * ArtisticImagePostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:44.478268-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ArtisticImagePostRequest {
  public static final String SERIALIZED_NAME_ASYNC = "async";
  @SerializedName(SERIALIZED_NAME_ASYNC)
  private Boolean async = true;

  public static final String SERIALIZED_NAME_IMAGE_URL = "image_url";
  @SerializedName(SERIALIZED_NAME_IMAGE_URL)
  private String imageUrl;

  public static final String SERIALIZED_NAME_STYLE_URL = "style_url";
  @SerializedName(SERIALIZED_NAME_STYLE_URL)
  private String styleUrl;

  public ArtisticImagePostRequest() {
  }

  public ArtisticImagePostRequest async(Boolean async) {
    this.async = async;
    return this;
  }

  /**
   * Get async
   * @return async
   */
  @javax.annotation.Nullable
  public Boolean getAsync() {
    return async;
  }

  public void setAsync(Boolean async) {
    this.async = async;
  }


  public ArtisticImagePostRequest imageUrl(String imageUrl) {
    this.imageUrl = imageUrl;
    return this;
  }

  /**
   * Get imageUrl
   * @return imageUrl
   */
  @javax.annotation.Nonnull
  public String getImageUrl() {
    return imageUrl;
  }

  public void setImageUrl(String imageUrl) {
    this.imageUrl = imageUrl;
  }


  public ArtisticImagePostRequest styleUrl(String styleUrl) {
    this.styleUrl = styleUrl;
    return this;
  }

  /**
   * Get styleUrl
   * @return styleUrl
   */
  @javax.annotation.Nonnull
  public String getStyleUrl() {
    return styleUrl;
  }

  public void setStyleUrl(String styleUrl) {
    this.styleUrl = styleUrl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ArtisticImagePostRequest artisticImagePostRequest = (ArtisticImagePostRequest) o;
    return Objects.equals(this.async, artisticImagePostRequest.async) &&
        Objects.equals(this.imageUrl, artisticImagePostRequest.imageUrl) &&
        Objects.equals(this.styleUrl, artisticImagePostRequest.styleUrl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(async, imageUrl, styleUrl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ArtisticImagePostRequest {\n");
    sb.append("    async: ").append(toIndentedString(async)).append("\n");
    sb.append("    imageUrl: ").append(toIndentedString(imageUrl)).append("\n");
    sb.append("    styleUrl: ").append(toIndentedString(styleUrl)).append("\n");
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
    openapiFields.add("async");
    openapiFields.add("image_url");
    openapiFields.add("style_url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("image_url");
    openapiRequiredFields.add("style_url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ArtisticImagePostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ArtisticImagePostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ArtisticImagePostRequest is not found in the empty JSON string", ArtisticImagePostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ArtisticImagePostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ArtisticImagePostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ArtisticImagePostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("image_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image_url").toString()));
      }
      if (!jsonObj.get("style_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `style_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("style_url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ArtisticImagePostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ArtisticImagePostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ArtisticImagePostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ArtisticImagePostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ArtisticImagePostRequest>() {
           @Override
           public void write(JsonWriter out, ArtisticImagePostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ArtisticImagePostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ArtisticImagePostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ArtisticImagePostRequest
   * @throws IOException if the JSON string is invalid with respect to ArtisticImagePostRequest
   */
  public static ArtisticImagePostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ArtisticImagePostRequest.class);
  }

  /**
   * Convert an instance of ArtisticImagePostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

