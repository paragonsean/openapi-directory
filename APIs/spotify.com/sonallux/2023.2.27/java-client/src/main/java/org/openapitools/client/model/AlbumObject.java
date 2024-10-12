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
import org.openapitools.client.model.CopyrightObject;
import org.openapitools.client.model.ExternalIdObject;
import org.openapitools.client.model.ExternalUrlObject;
import org.openapitools.client.model.ImageObject;
import org.openapitools.client.model.PagingSimplifiedTrackObject;
import org.openapitools.client.model.SimplifiedArtistObject;

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
 * AlbumObject
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:56.088414-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AlbumObject {
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

  public static final String SERIALIZED_NAME_ARTISTS = "artists";
  @SerializedName(SERIALIZED_NAME_ARTISTS)
  private List<SimplifiedArtistObject> artists = new ArrayList<>();

  public static final String SERIALIZED_NAME_COPYRIGHTS = "copyrights";
  @SerializedName(SERIALIZED_NAME_COPYRIGHTS)
  private List<CopyrightObject> copyrights = new ArrayList<>();

  public static final String SERIALIZED_NAME_EXTERNAL_IDS = "external_ids";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_IDS)
  private ExternalIdObject externalIds;

  public static final String SERIALIZED_NAME_GENRES = "genres";
  @SerializedName(SERIALIZED_NAME_GENRES)
  private List<String> genres = new ArrayList<>();

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_POPULARITY = "popularity";
  @SerializedName(SERIALIZED_NAME_POPULARITY)
  private Integer popularity;

  public static final String SERIALIZED_NAME_TRACKS = "tracks";
  @SerializedName(SERIALIZED_NAME_TRACKS)
  private PagingSimplifiedTrackObject tracks;

  public AlbumObject() {
  }

  public AlbumObject albumType(AlbumTypeEnum albumType) {
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


  public AlbumObject availableMarkets(List<String> availableMarkets) {
    this.availableMarkets = availableMarkets;
    return this;
  }

  public AlbumObject addAvailableMarketsItem(String availableMarketsItem) {
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


  public AlbumObject externalUrls(ExternalUrlObject externalUrls) {
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


  public AlbumObject href(String href) {
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


  public AlbumObject id(String id) {
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


  public AlbumObject images(List<ImageObject> images) {
    this.images = images;
    return this;
  }

  public AlbumObject addImagesItem(ImageObject imagesItem) {
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


  public AlbumObject name(String name) {
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


  public AlbumObject releaseDate(String releaseDate) {
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


  public AlbumObject releaseDatePrecision(ReleaseDatePrecisionEnum releaseDatePrecision) {
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


  public AlbumObject restrictions(AlbumRestrictionObject restrictions) {
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


  public AlbumObject totalTracks(Integer totalTracks) {
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


  public AlbumObject type(TypeEnum type) {
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


  public AlbumObject uri(String uri) {
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


  public AlbumObject artists(List<SimplifiedArtistObject> artists) {
    this.artists = artists;
    return this;
  }

  public AlbumObject addArtistsItem(SimplifiedArtistObject artistsItem) {
    if (this.artists == null) {
      this.artists = new ArrayList<>();
    }
    this.artists.add(artistsItem);
    return this;
  }

  /**
   * The artists of the album. Each artist object includes a link in &#x60;href&#x60; to more detailed information about the artist. 
   * @return artists
   */
  @javax.annotation.Nullable
  public List<SimplifiedArtistObject> getArtists() {
    return artists;
  }

  public void setArtists(List<SimplifiedArtistObject> artists) {
    this.artists = artists;
  }


  public AlbumObject copyrights(List<CopyrightObject> copyrights) {
    this.copyrights = copyrights;
    return this;
  }

  public AlbumObject addCopyrightsItem(CopyrightObject copyrightsItem) {
    if (this.copyrights == null) {
      this.copyrights = new ArrayList<>();
    }
    this.copyrights.add(copyrightsItem);
    return this;
  }

  /**
   * The copyright statements of the album.
   * @return copyrights
   */
  @javax.annotation.Nullable
  public List<CopyrightObject> getCopyrights() {
    return copyrights;
  }

  public void setCopyrights(List<CopyrightObject> copyrights) {
    this.copyrights = copyrights;
  }


  public AlbumObject externalIds(ExternalIdObject externalIds) {
    this.externalIds = externalIds;
    return this;
  }

  /**
   * Known external IDs for the album. 
   * @return externalIds
   */
  @javax.annotation.Nullable
  public ExternalIdObject getExternalIds() {
    return externalIds;
  }

  public void setExternalIds(ExternalIdObject externalIds) {
    this.externalIds = externalIds;
  }


  public AlbumObject genres(List<String> genres) {
    this.genres = genres;
    return this;
  }

  public AlbumObject addGenresItem(String genresItem) {
    if (this.genres == null) {
      this.genres = new ArrayList<>();
    }
    this.genres.add(genresItem);
    return this;
  }

  /**
   * A list of the genres used to classify the album. (If not yet classified, the array is empty.)
   * @return genres
   */
  @javax.annotation.Nullable
  public List<String> getGenres() {
    return genres;
  }

  public void setGenres(List<String> genres) {
    this.genres = genres;
  }


  public AlbumObject label(String label) {
    this.label = label;
    return this;
  }

  /**
   * The label for the album.
   * @return label
   */
  @javax.annotation.Nullable
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public AlbumObject popularity(Integer popularity) {
    this.popularity = popularity;
    return this;
  }

  /**
   * The popularity of the album, with 100 being the most popular. The popularity is calculated from the popularity of the album&#39;s individual tracks.
   * @return popularity
   */
  @javax.annotation.Nullable
  public Integer getPopularity() {
    return popularity;
  }

  public void setPopularity(Integer popularity) {
    this.popularity = popularity;
  }


  public AlbumObject tracks(PagingSimplifiedTrackObject tracks) {
    this.tracks = tracks;
    return this;
  }

  /**
   * The tracks of the album. 
   * @return tracks
   */
  @javax.annotation.Nullable
  public PagingSimplifiedTrackObject getTracks() {
    return tracks;
  }

  public void setTracks(PagingSimplifiedTrackObject tracks) {
    this.tracks = tracks;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AlbumObject albumObject = (AlbumObject) o;
    return Objects.equals(this.albumType, albumObject.albumType) &&
        Objects.equals(this.availableMarkets, albumObject.availableMarkets) &&
        Objects.equals(this.externalUrls, albumObject.externalUrls) &&
        Objects.equals(this.href, albumObject.href) &&
        Objects.equals(this.id, albumObject.id) &&
        Objects.equals(this.images, albumObject.images) &&
        Objects.equals(this.name, albumObject.name) &&
        Objects.equals(this.releaseDate, albumObject.releaseDate) &&
        Objects.equals(this.releaseDatePrecision, albumObject.releaseDatePrecision) &&
        Objects.equals(this.restrictions, albumObject.restrictions) &&
        Objects.equals(this.totalTracks, albumObject.totalTracks) &&
        Objects.equals(this.type, albumObject.type) &&
        Objects.equals(this.uri, albumObject.uri) &&
        Objects.equals(this.artists, albumObject.artists) &&
        Objects.equals(this.copyrights, albumObject.copyrights) &&
        Objects.equals(this.externalIds, albumObject.externalIds) &&
        Objects.equals(this.genres, albumObject.genres) &&
        Objects.equals(this.label, albumObject.label) &&
        Objects.equals(this.popularity, albumObject.popularity) &&
        Objects.equals(this.tracks, albumObject.tracks);
  }

  @Override
  public int hashCode() {
    return Objects.hash(albumType, availableMarkets, externalUrls, href, id, images, name, releaseDate, releaseDatePrecision, restrictions, totalTracks, type, uri, artists, copyrights, externalIds, genres, label, popularity, tracks);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AlbumObject {\n");
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
    sb.append("    artists: ").append(toIndentedString(artists)).append("\n");
    sb.append("    copyrights: ").append(toIndentedString(copyrights)).append("\n");
    sb.append("    externalIds: ").append(toIndentedString(externalIds)).append("\n");
    sb.append("    genres: ").append(toIndentedString(genres)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    popularity: ").append(toIndentedString(popularity)).append("\n");
    sb.append("    tracks: ").append(toIndentedString(tracks)).append("\n");
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
    openapiFields.add("artists");
    openapiFields.add("copyrights");
    openapiFields.add("external_ids");
    openapiFields.add("genres");
    openapiFields.add("label");
    openapiFields.add("popularity");
    openapiFields.add("tracks");

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
   * @throws IOException if the JSON Element is invalid with respect to AlbumObject
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AlbumObject.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AlbumObject is not found in the empty JSON string", AlbumObject.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AlbumObject.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AlbumObject` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AlbumObject.openapiRequiredFields) {
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
      if (jsonObj.get("artists") != null && !jsonObj.get("artists").isJsonNull()) {
        JsonArray jsonArrayartists = jsonObj.getAsJsonArray("artists");
        if (jsonArrayartists != null) {
          // ensure the json data is an array
          if (!jsonObj.get("artists").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `artists` to be an array in the JSON string but got `%s`", jsonObj.get("artists").toString()));
          }

          // validate the optional field `artists` (array)
          for (int i = 0; i < jsonArrayartists.size(); i++) {
            SimplifiedArtistObject.validateJsonElement(jsonArrayartists.get(i));
          };
        }
      }
      if (jsonObj.get("copyrights") != null && !jsonObj.get("copyrights").isJsonNull()) {
        JsonArray jsonArraycopyrights = jsonObj.getAsJsonArray("copyrights");
        if (jsonArraycopyrights != null) {
          // ensure the json data is an array
          if (!jsonObj.get("copyrights").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `copyrights` to be an array in the JSON string but got `%s`", jsonObj.get("copyrights").toString()));
          }

          // validate the optional field `copyrights` (array)
          for (int i = 0; i < jsonArraycopyrights.size(); i++) {
            CopyrightObject.validateJsonElement(jsonArraycopyrights.get(i));
          };
        }
      }
      // validate the optional field `external_ids`
      if (jsonObj.get("external_ids") != null && !jsonObj.get("external_ids").isJsonNull()) {
        ExternalIdObject.validateJsonElement(jsonObj.get("external_ids"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("genres") != null && !jsonObj.get("genres").isJsonNull() && !jsonObj.get("genres").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `genres` to be an array in the JSON string but got `%s`", jsonObj.get("genres").toString()));
      }
      if ((jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) && !jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      // validate the optional field `tracks`
      if (jsonObj.get("tracks") != null && !jsonObj.get("tracks").isJsonNull()) {
        PagingSimplifiedTrackObject.validateJsonElement(jsonObj.get("tracks"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AlbumObject.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AlbumObject' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AlbumObject> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AlbumObject.class));

       return (TypeAdapter<T>) new TypeAdapter<AlbumObject>() {
           @Override
           public void write(JsonWriter out, AlbumObject value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AlbumObject read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AlbumObject given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AlbumObject
   * @throws IOException if the JSON string is invalid with respect to AlbumObject
   */
  public static AlbumObject fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AlbumObject.class);
  }

  /**
   * Convert an instance of AlbumObject to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

