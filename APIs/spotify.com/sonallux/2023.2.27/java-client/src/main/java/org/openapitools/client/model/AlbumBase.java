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
import org.openapitools.client.model.AlbumRestrictionObject;
import org.openapitools.client.model.ExternalUrlObject;
import org.openapitools.client.model.ImageObject;

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
 * AlbumBase
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:56.088414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AlbumBase {
  /**
   * The type of the album. 
   */
  @JsonAdapter(AlbumTypeEnum.Adapter.class)
  public enum AlbumTypeEnum {
    ALBUM("album"),
    
    SINGLE("single"),
    
    COMPILATION("compilation");

    private String value;

    AlbumTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AlbumTypeEnum fromValue(String value) {
      for (AlbumTypeEnum b : AlbumTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AlbumTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AlbumTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AlbumTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AlbumTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AlbumTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ALBUM_TYPE = "album_type";
  @SerializedName(SERIALIZED_NAME_ALBUM_TYPE)
  private AlbumTypeEnum albumType;

  public static final String SERIALIZED_NAME_AVAILABLE_MARKETS = "available_markets";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_MARKETS)
  private List<String> availableMarkets = new ArrayList<>();

  public static final String SERIALIZED_NAME_EXTERNAL_URLS = "external_urls";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_URLS)
  private ExternalUrlObject externalUrls;

  public static final String SERIALIZED_NAME_HREF = "href";
  @SerializedName(SERIALIZED_NAME_HREF)
  private String href;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IMAGES = "images";
  @SerializedName(SERIALIZED_NAME_IMAGES)
  private List<ImageObject> images = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_RELEASE_DATE = "release_date";
  @SerializedName(SERIALIZED_NAME_RELEASE_DATE)
  private String releaseDate;

  /**
   * The precision with which &#x60;release_date&#x60; value is known. 
   */
  @JsonAdapter(ReleaseDatePrecisionEnum.Adapter.class)
  public enum ReleaseDatePrecisionEnum {
    YEAR("year"),
    
    MONTH("month"),
    
    DAY("day");

    private String value;

    ReleaseDatePrecisionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ReleaseDatePrecisionEnum fromValue(String value) {
      for (ReleaseDatePrecisionEnum b : ReleaseDatePrecisionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ReleaseDatePrecisionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ReleaseDatePrecisionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ReleaseDatePrecisionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ReleaseDatePrecisionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ReleaseDatePrecisionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RELEASE_DATE_PRECISION = "release_date_precision";
  @SerializedName(SERIALIZED_NAME_RELEASE_DATE_PRECISION)
  private ReleaseDatePrecisionEnum releaseDatePrecision;

  public static final String SERIALIZED_NAME_RESTRICTIONS = "restrictions";
  @SerializedName(SERIALIZED_NAME_RESTRICTIONS)
  private AlbumRestrictionObject restrictions;

  public static final String SERIALIZED_NAME_TOTAL_TRACKS = "total_tracks";
  @SerializedName(SERIALIZED_NAME_TOTAL_TRACKS)
  private Integer totalTracks;

  /**
   * The object type. 
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    ALBUM("album");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_URI = "uri";
  @SerializedName(SERIALIZED_NAME_URI)
  private String uri;

  public AlbumBase() {
  }

  public AlbumBase albumType(AlbumTypeEnum albumType) {
    this.albumType = albumType;
    return this;
  }

  /**
   * The type of the album. 
   * @return albumType
   */
  @javax.annotation.Nonnull
  public AlbumTypeEnum getAlbumType() {
    return albumType;
  }

  public void setAlbumType(AlbumTypeEnum albumType) {
    this.albumType = albumType;
  }


  public AlbumBase availableMarkets(List<String> availableMarkets) {
    this.availableMarkets = availableMarkets;
    return this;
  }

  public AlbumBase addAvailableMarketsItem(String availableMarketsItem) {
    if (this.availableMarkets == null) {
      this.availableMarkets = new ArrayList<>();
    }
    this.availableMarkets.add(availableMarketsItem);
    return this;
  }

  /**
   * The markets in which the album is available: [ISO 3166-1 alpha-2 country codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). _**NOTE**: an album is considered available in a market when at least 1 of its tracks is available in that market._ 
   * @return availableMarkets
   */
  @javax.annotation.Nonnull
  public List<String> getAvailableMarkets() {
    return availableMarkets;
  }

  public void setAvailableMarkets(List<String> availableMarkets) {
    this.availableMarkets = availableMarkets;
  }


  public AlbumBase externalUrls(ExternalUrlObject externalUrls) {
    this.externalUrls = externalUrls;
    return this;
  }

  /**
   * Known external URLs for this album. 
   * @return externalUrls
   */
  @javax.annotation.Nonnull
  public ExternalUrlObject getExternalUrls() {
    return externalUrls;
  }

  public void setExternalUrls(ExternalUrlObject externalUrls) {
    this.externalUrls = externalUrls;
  }


  public AlbumBase href(String href) {
    this.href = href;
    return this;
  }

  /**
   * A link to the Web API endpoint providing full details of the album. 
   * @return href
   */
  @javax.annotation.Nonnull
  public String getHref() {
    return href;
  }

  public void setHref(String href) {
    this.href = href;
  }


  public AlbumBase id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the album. 
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public AlbumBase images(List<ImageObject> images) {
    this.images = images;
    return this;
  }

  public AlbumBase addImagesItem(ImageObject imagesItem) {
    if (this.images == null) {
      this.images = new ArrayList<>();
    }
    this.images.add(imagesItem);
    return this;
  }

  /**
   * The cover art for the album in various sizes, widest first. 
   * @return images
   */
  @javax.annotation.Nonnull
  public List<ImageObject> getImages() {
    return images;
  }

  public void setImages(List<ImageObject> images) {
    this.images = images;
  }


  public AlbumBase name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the album. In case of an album takedown, the value may be an empty string. 
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AlbumBase releaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
    return this;
  }

  /**
   * The date the album was first released. 
   * @return releaseDate
   */
  @javax.annotation.Nonnull
  public String getReleaseDate() {
    return releaseDate;
  }

  public void setReleaseDate(String releaseDate) {
    this.releaseDate = releaseDate;
  }


  public AlbumBase releaseDatePrecision(ReleaseDatePrecisionEnum releaseDatePrecision) {
    this.releaseDatePrecision = releaseDatePrecision;
    return this;
  }

  /**
   * The precision with which &#x60;release_date&#x60; value is known. 
   * @return releaseDatePrecision
   */
  @javax.annotation.Nonnull
  public ReleaseDatePrecisionEnum getReleaseDatePrecision() {
    return releaseDatePrecision;
  }

  public void setReleaseDatePrecision(ReleaseDatePrecisionEnum releaseDatePrecision) {
    this.releaseDatePrecision = releaseDatePrecision;
  }


  public AlbumBase restrictions(AlbumRestrictionObject restrictions) {
    this.restrictions = restrictions;
    return this;
  }

  /**
   * Included in the response when a content restriction is applied. 
   * @return restrictions
   */
  @javax.annotation.Nullable
  public AlbumRestrictionObject getRestrictions() {
    return restrictions;
  }

  public void setRestrictions(AlbumRestrictionObject restrictions) {
    this.restrictions = restrictions;
  }


  public AlbumBase totalTracks(Integer totalTracks) {
    this.totalTracks = totalTracks;
    return this;
  }

  /**
   * The number of tracks in the album.
   * @return totalTracks
   */
  @javax.annotation.Nonnull
  public Integer getTotalTracks() {
    return totalTracks;
  }

  public void setTotalTracks(Integer totalTracks) {
    this.totalTracks = totalTracks;
  }


  public AlbumBase type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The object type. 
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public AlbumBase uri(String uri) {
    this.uri = uri;
    return this;
  }

  /**
   * The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the album. 
   * @return uri
   */
  @javax.annotation.Nonnull
  public String getUri() {
    return uri;
  }

  public void setUri(String uri) {
    this.uri = uri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AlbumBase albumBase = (AlbumBase) o;
    return Objects.equals(this.albumType, albumBase.albumType) &&
        Objects.equals(this.availableMarkets, albumBase.availableMarkets) &&
        Objects.equals(this.externalUrls, albumBase.externalUrls) &&
        Objects.equals(this.href, albumBase.href) &&
        Objects.equals(this.id, albumBase.id) &&
        Objects.equals(this.images, albumBase.images) &&
        Objects.equals(this.name, albumBase.name) &&
        Objects.equals(this.releaseDate, albumBase.releaseDate) &&
        Objects.equals(this.releaseDatePrecision, albumBase.releaseDatePrecision) &&
        Objects.equals(this.restrictions, albumBase.restrictions) &&
        Objects.equals(this.totalTracks, albumBase.totalTracks) &&
        Objects.equals(this.type, albumBase.type) &&
        Objects.equals(this.uri, albumBase.uri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(albumType, availableMarkets, externalUrls, href, id, images, name, releaseDate, releaseDatePrecision, restrictions, totalTracks, type, uri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AlbumBase {\n");
    sb.append("    albumType: ").append(toIndentedString(albumType)).append("\n");
    sb.append("    availableMarkets: ").append(toIndentedString(availableMarkets)).append("\n");
    sb.append("    externalUrls: ").append(toIndentedString(externalUrls)).append("\n");
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    images: ").append(toIndentedString(images)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    releaseDate: ").append(toIndentedString(releaseDate)).append("\n");
    sb.append("    releaseDatePrecision: ").append(toIndentedString(releaseDatePrecision)).append("\n");
    sb.append("    restrictions: ").append(toIndentedString(restrictions)).append("\n");
    sb.append("    totalTracks: ").append(toIndentedString(totalTracks)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    uri: ").append(toIndentedString(uri)).append("\n");
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
    openapiFields.add("album_type");
    openapiFields.add("available_markets");
    openapiFields.add("external_urls");
    openapiFields.add("href");
    openapiFields.add("id");
    openapiFields.add("images");
    openapiFields.add("name");
    openapiFields.add("release_date");
    openapiFields.add("release_date_precision");
    openapiFields.add("restrictions");
    openapiFields.add("total_tracks");
    openapiFields.add("type");
    openapiFields.add("uri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("album_type");
    openapiRequiredFields.add("available_markets");
    openapiRequiredFields.add("external_urls");
    openapiRequiredFields.add("href");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("images");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("release_date");
    openapiRequiredFields.add("release_date_precision");
    openapiRequiredFields.add("total_tracks");
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("uri");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AlbumBase
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AlbumBase.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AlbumBase is not found in the empty JSON string", AlbumBase.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AlbumBase.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AlbumBase` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AlbumBase.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("album_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_type").toString()));
      }
      // validate the required field `album_type`
      AlbumTypeEnum.validateJsonElement(jsonObj.get("album_type"));
      // ensure the required json array is present
      if (jsonObj.get("available_markets") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("available_markets").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `available_markets` to be an array in the JSON string but got `%s`", jsonObj.get("available_markets").toString()));
      }
      // validate the required field `external_urls`
      ExternalUrlObject.validateJsonElement(jsonObj.get("external_urls"));
      if (!jsonObj.get("href").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `href` to be a primitive type in the JSON string but got `%s`", jsonObj.get("href").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("images").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `images` to be an array in the JSON string but got `%s`", jsonObj.get("images").toString()));
      }

      JsonArray jsonArrayimages = jsonObj.getAsJsonArray("images");
      // validate the required field `images` (array)
      for (int i = 0; i < jsonArrayimages.size(); i++) {
        ImageObject.validateJsonElement(jsonArrayimages.get(i));
      };
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("release_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_date").toString()));
      }
      if (!jsonObj.get("release_date_precision").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_date_precision` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_date_precision").toString()));
      }
      // validate the required field `release_date_precision`
      ReleaseDatePrecisionEnum.validateJsonElement(jsonObj.get("release_date_precision"));
      // validate the optional field `restrictions`
      if (jsonObj.get("restrictions") != null && !jsonObj.get("restrictions").isJsonNull()) {
        AlbumRestrictionObject.validateJsonElement(jsonObj.get("restrictions"));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if (!jsonObj.get("uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AlbumBase.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AlbumBase' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AlbumBase> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AlbumBase.class));

       return (TypeAdapter<T>) new TypeAdapter<AlbumBase>() {
           @Override
           public void write(JsonWriter out, AlbumBase value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AlbumBase read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AlbumBase given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AlbumBase
   * @throws IOException if the JSON string is invalid with respect to AlbumBase
   */
  public static AlbumBase fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AlbumBase.class);
  }

  /**
   * Convert an instance of AlbumBase to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

