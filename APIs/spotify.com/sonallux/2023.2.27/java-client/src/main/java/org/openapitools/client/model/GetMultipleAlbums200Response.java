/*
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AlbumObject;

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
 * GetMultipleAlbums200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:56.088414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetMultipleAlbums200Response {
  public static final String SERIALIZED_NAME_ALBUMS = "albums";
  @SerializedName(SERIALIZED_NAME_ALBUMS)
  private List<AlbumObject> albums = new ArrayList<>();

  public GetMultipleAlbums200Response() {
  }

  public GetMultipleAlbums200Response albums(List<AlbumObject> albums) {
    this.albums = albums;
    return this;
  }

  public GetMultipleAlbums200Response addAlbumsItem(AlbumObject albumsItem) {
    if (this.albums == null) {
      this.albums = new ArrayList<>();
    }
    this.albums.add(albumsItem);
    return this;
  }

  /**
   * Get albums
   * @return albums
   */
  @javax.annotation.Nonnull
  public List<AlbumObject> getAlbums() {
    return albums;
  }

  public void setAlbums(List<AlbumObject> albums) {
    this.albums = albums;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetMultipleAlbums200Response getMultipleAlbums200Response = (GetMultipleAlbums200Response) o;
    return Objects.equals(this.albums, getMultipleAlbums200Response.albums);
  }

  @Override
  public int hashCode() {
    return Objects.hash(albums);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetMultipleAlbums200Response {\n");
    sb.append("    albums: ").append(toIndentedString(albums)).append("\n");
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
    openapiFields.add("albums");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("albums");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetMultipleAlbums200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetMultipleAlbums200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetMultipleAlbums200Response is not found in the empty JSON string", GetMultipleAlbums200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetMultipleAlbums200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetMultipleAlbums200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetMultipleAlbums200Response.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("albums").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `albums` to be an array in the JSON string but got `%s`", jsonObj.get("albums").toString()));
      }

      JsonArray jsonArrayalbums = jsonObj.getAsJsonArray("albums");
      // validate the required field `albums` (array)
      for (int i = 0; i < jsonArrayalbums.size(); i++) {
        AlbumObject.validateJsonElement(jsonArrayalbums.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetMultipleAlbums200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetMultipleAlbums200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetMultipleAlbums200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetMultipleAlbums200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetMultipleAlbums200Response>() {
           @Override
           public void write(JsonWriter out, GetMultipleAlbums200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetMultipleAlbums200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetMultipleAlbums200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetMultipleAlbums200Response
   * @throws IOException if the JSON string is invalid with respect to GetMultipleAlbums200Response
   */
  public static GetMultipleAlbums200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetMultipleAlbums200Response.class);
  }

  /**
   * Convert an instance of GetMultipleAlbums200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

