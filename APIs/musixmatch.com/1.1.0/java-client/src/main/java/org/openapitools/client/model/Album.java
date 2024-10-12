/*
 * Musixmatch API
 * Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.  Include millions of licensed lyrics on your website or in your application legally.  The fastest, most powerful and legal way to display lyrics on your website or in your application.  #### Read musixmatch API Terms & Conditions and the Privacy Policy: Before getting started, you must take a look at the [API Terms & Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.  #### Register for an API key: All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:  ```   https://api.musixmatch.com/ws/v1.1/track.get?apikey=YOUR_API_KEY ``` #### Integrate the musixmatch service with your web site or application In the most common scenario you only need to implement two API calls:  The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!  ## API Methods What does the musiXmatch API do?  The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.  To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.  The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/  Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.  Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).  ## Music meta data The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.  ## Track Inside the track object you can get the following extra information:  ### TRACK RATING  The track rating is a score 0-100 identifying how popular is a song in musixmatch.  You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.  ### INSTRUMENTAL AND EXPLICIT FLAGS  The instrumental flag identifies songs with music only, no lyrics.  The explicit flag identifies songs with explicit lyrics or explicit title. We're able to identify explicit words and set the flag for the most common languages.  ### FAVOURITES  How many users have this song in their list of favourites.  Can be used to sort tracks by num favourite to identify more popular tracks within a set.  ### MUSIC GENRE  The music genere of the song.  Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.  ### SONG TITLES TRANSLATIONS  The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:  LIES (Bigbang) becomes 在光化門 in chinese HALLELUJAH (Bigbang) becomes ハレルヤ in japanese   ## Artist Inside the artist object you can get the following nice extra information:  ### COMMENTS AND COUNTRY  An artist comment is a short snippet of text which can be mainly used for disambiguation.  The artist country is the born country of the artist/group  There are two perfect search result if you search by artist with the keyword \"U2\". Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.  Here's how you can made use of the artist comment in your search result page:  U2 (Irish rock band) U2 (あきやまうに) You can also show the artist country for even better disambiguation:  U2 (Irish rock band) from Ireland U2 (あきやまうに) from Japan ARTIST TRANSLATIONS  When you create a world wide music related service you have to take into consideration to display the artist name in the user's local language. These translation are also used as aliases to improve the search results.  Let's use PSY for this example.  Western people know him as PSY but korean want to see the original name 싸이.  Using the name translations provided by our api you can show to every user the writing they expect to see.  Furthermore, when you search for \"psy gangnam style\" or \"싸이 gangnam style\" with our search/match api you will still be able to find the song.  ### ARTIST RATING  The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.  You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.  ### ARTIST MUSIC GENRE  We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.    ## Album Inside the album object you can get the following nice extra information:  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM COPYRIGHT AND LABEL  For most of our albums we can provide extra information like for example:  Label: Universal-Island Records Ltd. Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment. ALBUM TYPE AND RELEASE DATE  The album official release date can be used to sort an artist's albums view starting by the most recent one.  Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.  ### ALBUM MUSIC GENRE  For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.  An example could be:  Primary genere: POP Secondary genre: K-POP or Mandopop 
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: info@musixmatch.com
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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.client.model.AlbumPrimaryGenres;
import org.openapitools.client.model.AlbumSecondaryGenres;

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
 * a album of songs in the Musixmatch database.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:43:43.628132-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Album {
  public static final String SERIALIZED_NAME_ALBUM_COPYRIGHT = "album_copyright";
  @SerializedName(SERIALIZED_NAME_ALBUM_COPYRIGHT)
  private String albumCopyright;

  public static final String SERIALIZED_NAME_ALBUM_COVERART100X100 = "album_coverart_100x100";
  @SerializedName(SERIALIZED_NAME_ALBUM_COVERART100X100)
  private String albumCoverart100x100;

  public static final String SERIALIZED_NAME_ALBUM_COVERART350X350 = "album_coverart_350x350";
  @SerializedName(SERIALIZED_NAME_ALBUM_COVERART350X350)
  private String albumCoverart350x350;

  public static final String SERIALIZED_NAME_ALBUM_COVERART500X500 = "album_coverart_500x500";
  @SerializedName(SERIALIZED_NAME_ALBUM_COVERART500X500)
  private String albumCoverart500x500;

  public static final String SERIALIZED_NAME_ALBUM_COVERART800X800 = "album_coverart_800x800";
  @SerializedName(SERIALIZED_NAME_ALBUM_COVERART800X800)
  private String albumCoverart800x800;

  public static final String SERIALIZED_NAME_ALBUM_EDIT_URL = "album_edit_url";
  @SerializedName(SERIALIZED_NAME_ALBUM_EDIT_URL)
  private String albumEditUrl;

  public static final String SERIALIZED_NAME_ALBUM_ID = "album_id";
  @SerializedName(SERIALIZED_NAME_ALBUM_ID)
  private BigDecimal albumId;

  public static final String SERIALIZED_NAME_ALBUM_LABEL = "album_label";
  @SerializedName(SERIALIZED_NAME_ALBUM_LABEL)
  private String albumLabel;

  public static final String SERIALIZED_NAME_ALBUM_MBID = "album_mbid";
  @SerializedName(SERIALIZED_NAME_ALBUM_MBID)
  private String albumMbid;

  public static final String SERIALIZED_NAME_ALBUM_NAME = "album_name";
  @SerializedName(SERIALIZED_NAME_ALBUM_NAME)
  private String albumName;

  public static final String SERIALIZED_NAME_ALBUM_PLINE = "album_pline";
  @SerializedName(SERIALIZED_NAME_ALBUM_PLINE)
  private String albumPline;

  public static final String SERIALIZED_NAME_ALBUM_RATING = "album_rating";
  @SerializedName(SERIALIZED_NAME_ALBUM_RATING)
  private BigDecimal albumRating;

  public static final String SERIALIZED_NAME_ALBUM_RELEASE_DATE = "album_release_date";
  @SerializedName(SERIALIZED_NAME_ALBUM_RELEASE_DATE)
  private String albumReleaseDate;

  public static final String SERIALIZED_NAME_ALBUM_RELEASE_TYPE = "album_release_type";
  @SerializedName(SERIALIZED_NAME_ALBUM_RELEASE_TYPE)
  private String albumReleaseType;

  public static final String SERIALIZED_NAME_ALBUM_TRACK_COUNT = "album_track_count";
  @SerializedName(SERIALIZED_NAME_ALBUM_TRACK_COUNT)
  private BigDecimal albumTrackCount;

  public static final String SERIALIZED_NAME_ALBUM_VANITY_ID = "album_vanity_id";
  @SerializedName(SERIALIZED_NAME_ALBUM_VANITY_ID)
  private String albumVanityId;

  public static final String SERIALIZED_NAME_ARTIST_ID = "artist_id";
  @SerializedName(SERIALIZED_NAME_ARTIST_ID)
  private BigDecimal artistId;

  public static final String SERIALIZED_NAME_ARTIST_NAME = "artist_name";
  @SerializedName(SERIALIZED_NAME_ARTIST_NAME)
  private String artistName;

  public static final String SERIALIZED_NAME_PRIMARY_GENRES = "primary_genres";
  @SerializedName(SERIALIZED_NAME_PRIMARY_GENRES)
  private AlbumPrimaryGenres primaryGenres;

  public static final String SERIALIZED_NAME_RESTRICTED = "restricted";
  @SerializedName(SERIALIZED_NAME_RESTRICTED)
  private BigDecimal restricted;

  public static final String SERIALIZED_NAME_SECONDARY_GENRES = "secondary_genres";
  @SerializedName(SERIALIZED_NAME_SECONDARY_GENRES)
  private AlbumSecondaryGenres secondaryGenres;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private String updatedTime;

  public Album() {
  }

  public Album albumCopyright(String albumCopyright) {
    this.albumCopyright = albumCopyright;
    return this;
  }

  /**
   * 
   * @return albumCopyright
   */
  @javax.annotation.Nullable
  public String getAlbumCopyright() {
    return albumCopyright;
  }

  public void setAlbumCopyright(String albumCopyright) {
    this.albumCopyright = albumCopyright;
  }


  public Album albumCoverart100x100(String albumCoverart100x100) {
    this.albumCoverart100x100 = albumCoverart100x100;
    return this;
  }

  /**
   * 
   * @return albumCoverart100x100
   */
  @javax.annotation.Nullable
  public String getAlbumCoverart100x100() {
    return albumCoverart100x100;
  }

  public void setAlbumCoverart100x100(String albumCoverart100x100) {
    this.albumCoverart100x100 = albumCoverart100x100;
  }


  public Album albumCoverart350x350(String albumCoverart350x350) {
    this.albumCoverart350x350 = albumCoverart350x350;
    return this;
  }

  /**
   * 
   * @return albumCoverart350x350
   */
  @javax.annotation.Nullable
  public String getAlbumCoverart350x350() {
    return albumCoverart350x350;
  }

  public void setAlbumCoverart350x350(String albumCoverart350x350) {
    this.albumCoverart350x350 = albumCoverart350x350;
  }


  public Album albumCoverart500x500(String albumCoverart500x500) {
    this.albumCoverart500x500 = albumCoverart500x500;
    return this;
  }

  /**
   * 
   * @return albumCoverart500x500
   */
  @javax.annotation.Nullable
  public String getAlbumCoverart500x500() {
    return albumCoverart500x500;
  }

  public void setAlbumCoverart500x500(String albumCoverart500x500) {
    this.albumCoverart500x500 = albumCoverart500x500;
  }


  public Album albumCoverart800x800(String albumCoverart800x800) {
    this.albumCoverart800x800 = albumCoverart800x800;
    return this;
  }

  /**
   * 
   * @return albumCoverart800x800
   */
  @javax.annotation.Nullable
  public String getAlbumCoverart800x800() {
    return albumCoverart800x800;
  }

  public void setAlbumCoverart800x800(String albumCoverart800x800) {
    this.albumCoverart800x800 = albumCoverart800x800;
  }


  public Album albumEditUrl(String albumEditUrl) {
    this.albumEditUrl = albumEditUrl;
    return this;
  }

  /**
   * 
   * @return albumEditUrl
   */
  @javax.annotation.Nullable
  public String getAlbumEditUrl() {
    return albumEditUrl;
  }

  public void setAlbumEditUrl(String albumEditUrl) {
    this.albumEditUrl = albumEditUrl;
  }


  public Album albumId(BigDecimal albumId) {
    this.albumId = albumId;
    return this;
  }

  /**
   * 
   * @return albumId
   */
  @javax.annotation.Nullable
  public BigDecimal getAlbumId() {
    return albumId;
  }

  public void setAlbumId(BigDecimal albumId) {
    this.albumId = albumId;
  }


  public Album albumLabel(String albumLabel) {
    this.albumLabel = albumLabel;
    return this;
  }

  /**
   * 
   * @return albumLabel
   */
  @javax.annotation.Nullable
  public String getAlbumLabel() {
    return albumLabel;
  }

  public void setAlbumLabel(String albumLabel) {
    this.albumLabel = albumLabel;
  }


  public Album albumMbid(String albumMbid) {
    this.albumMbid = albumMbid;
    return this;
  }

  /**
   * 
   * @return albumMbid
   */
  @javax.annotation.Nullable
  public String getAlbumMbid() {
    return albumMbid;
  }

  public void setAlbumMbid(String albumMbid) {
    this.albumMbid = albumMbid;
  }


  public Album albumName(String albumName) {
    this.albumName = albumName;
    return this;
  }

  /**
   * 
   * @return albumName
   */
  @javax.annotation.Nullable
  public String getAlbumName() {
    return albumName;
  }

  public void setAlbumName(String albumName) {
    this.albumName = albumName;
  }


  public Album albumPline(String albumPline) {
    this.albumPline = albumPline;
    return this;
  }

  /**
   * 
   * @return albumPline
   */
  @javax.annotation.Nullable
  public String getAlbumPline() {
    return albumPline;
  }

  public void setAlbumPline(String albumPline) {
    this.albumPline = albumPline;
  }


  public Album albumRating(BigDecimal albumRating) {
    this.albumRating = albumRating;
    return this;
  }

  /**
   * 
   * @return albumRating
   */
  @javax.annotation.Nullable
  public BigDecimal getAlbumRating() {
    return albumRating;
  }

  public void setAlbumRating(BigDecimal albumRating) {
    this.albumRating = albumRating;
  }


  public Album albumReleaseDate(String albumReleaseDate) {
    this.albumReleaseDate = albumReleaseDate;
    return this;
  }

  /**
   * 
   * @return albumReleaseDate
   */
  @javax.annotation.Nullable
  public String getAlbumReleaseDate() {
    return albumReleaseDate;
  }

  public void setAlbumReleaseDate(String albumReleaseDate) {
    this.albumReleaseDate = albumReleaseDate;
  }


  public Album albumReleaseType(String albumReleaseType) {
    this.albumReleaseType = albumReleaseType;
    return this;
  }

  /**
   * 
   * @return albumReleaseType
   */
  @javax.annotation.Nullable
  public String getAlbumReleaseType() {
    return albumReleaseType;
  }

  public void setAlbumReleaseType(String albumReleaseType) {
    this.albumReleaseType = albumReleaseType;
  }


  public Album albumTrackCount(BigDecimal albumTrackCount) {
    this.albumTrackCount = albumTrackCount;
    return this;
  }

  /**
   * 
   * @return albumTrackCount
   */
  @javax.annotation.Nullable
  public BigDecimal getAlbumTrackCount() {
    return albumTrackCount;
  }

  public void setAlbumTrackCount(BigDecimal albumTrackCount) {
    this.albumTrackCount = albumTrackCount;
  }


  public Album albumVanityId(String albumVanityId) {
    this.albumVanityId = albumVanityId;
    return this;
  }

  /**
   * 
   * @return albumVanityId
   */
  @javax.annotation.Nullable
  public String getAlbumVanityId() {
    return albumVanityId;
  }

  public void setAlbumVanityId(String albumVanityId) {
    this.albumVanityId = albumVanityId;
  }


  public Album artistId(BigDecimal artistId) {
    this.artistId = artistId;
    return this;
  }

  /**
   * 
   * @return artistId
   */
  @javax.annotation.Nullable
  public BigDecimal getArtistId() {
    return artistId;
  }

  public void setArtistId(BigDecimal artistId) {
    this.artistId = artistId;
  }


  public Album artistName(String artistName) {
    this.artistName = artistName;
    return this;
  }

  /**
   * 
   * @return artistName
   */
  @javax.annotation.Nullable
  public String getArtistName() {
    return artistName;
  }

  public void setArtistName(String artistName) {
    this.artistName = artistName;
  }


  public Album primaryGenres(AlbumPrimaryGenres primaryGenres) {
    this.primaryGenres = primaryGenres;
    return this;
  }

  /**
   * Get primaryGenres
   * @return primaryGenres
   */
  @javax.annotation.Nullable
  public AlbumPrimaryGenres getPrimaryGenres() {
    return primaryGenres;
  }

  public void setPrimaryGenres(AlbumPrimaryGenres primaryGenres) {
    this.primaryGenres = primaryGenres;
  }


  public Album restricted(BigDecimal restricted) {
    this.restricted = restricted;
    return this;
  }

  /**
   * 
   * @return restricted
   */
  @javax.annotation.Nullable
  public BigDecimal getRestricted() {
    return restricted;
  }

  public void setRestricted(BigDecimal restricted) {
    this.restricted = restricted;
  }


  public Album secondaryGenres(AlbumSecondaryGenres secondaryGenres) {
    this.secondaryGenres = secondaryGenres;
    return this;
  }

  /**
   * Get secondaryGenres
   * @return secondaryGenres
   */
  @javax.annotation.Nullable
  public AlbumSecondaryGenres getSecondaryGenres() {
    return secondaryGenres;
  }

  public void setSecondaryGenres(AlbumSecondaryGenres secondaryGenres) {
    this.secondaryGenres = secondaryGenres;
  }


  public Album updatedTime(String updatedTime) {
    this.updatedTime = updatedTime;
    return this;
  }

  /**
   * 
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public String getUpdatedTime() {
    return updatedTime;
  }

  public void setUpdatedTime(String updatedTime) {
    this.updatedTime = updatedTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Album album = (Album) o;
    return Objects.equals(this.albumCopyright, album.albumCopyright) &&
        Objects.equals(this.albumCoverart100x100, album.albumCoverart100x100) &&
        Objects.equals(this.albumCoverart350x350, album.albumCoverart350x350) &&
        Objects.equals(this.albumCoverart500x500, album.albumCoverart500x500) &&
        Objects.equals(this.albumCoverart800x800, album.albumCoverart800x800) &&
        Objects.equals(this.albumEditUrl, album.albumEditUrl) &&
        Objects.equals(this.albumId, album.albumId) &&
        Objects.equals(this.albumLabel, album.albumLabel) &&
        Objects.equals(this.albumMbid, album.albumMbid) &&
        Objects.equals(this.albumName, album.albumName) &&
        Objects.equals(this.albumPline, album.albumPline) &&
        Objects.equals(this.albumRating, album.albumRating) &&
        Objects.equals(this.albumReleaseDate, album.albumReleaseDate) &&
        Objects.equals(this.albumReleaseType, album.albumReleaseType) &&
        Objects.equals(this.albumTrackCount, album.albumTrackCount) &&
        Objects.equals(this.albumVanityId, album.albumVanityId) &&
        Objects.equals(this.artistId, album.artistId) &&
        Objects.equals(this.artistName, album.artistName) &&
        Objects.equals(this.primaryGenres, album.primaryGenres) &&
        Objects.equals(this.restricted, album.restricted) &&
        Objects.equals(this.secondaryGenres, album.secondaryGenres) &&
        Objects.equals(this.updatedTime, album.updatedTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(albumCopyright, albumCoverart100x100, albumCoverart350x350, albumCoverart500x500, albumCoverart800x800, albumEditUrl, albumId, albumLabel, albumMbid, albumName, albumPline, albumRating, albumReleaseDate, albumReleaseType, albumTrackCount, albumVanityId, artistId, artistName, primaryGenres, restricted, secondaryGenres, updatedTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Album {\n");
    sb.append("    albumCopyright: ").append(toIndentedString(albumCopyright)).append("\n");
    sb.append("    albumCoverart100x100: ").append(toIndentedString(albumCoverart100x100)).append("\n");
    sb.append("    albumCoverart350x350: ").append(toIndentedString(albumCoverart350x350)).append("\n");
    sb.append("    albumCoverart500x500: ").append(toIndentedString(albumCoverart500x500)).append("\n");
    sb.append("    albumCoverart800x800: ").append(toIndentedString(albumCoverart800x800)).append("\n");
    sb.append("    albumEditUrl: ").append(toIndentedString(albumEditUrl)).append("\n");
    sb.append("    albumId: ").append(toIndentedString(albumId)).append("\n");
    sb.append("    albumLabel: ").append(toIndentedString(albumLabel)).append("\n");
    sb.append("    albumMbid: ").append(toIndentedString(albumMbid)).append("\n");
    sb.append("    albumName: ").append(toIndentedString(albumName)).append("\n");
    sb.append("    albumPline: ").append(toIndentedString(albumPline)).append("\n");
    sb.append("    albumRating: ").append(toIndentedString(albumRating)).append("\n");
    sb.append("    albumReleaseDate: ").append(toIndentedString(albumReleaseDate)).append("\n");
    sb.append("    albumReleaseType: ").append(toIndentedString(albumReleaseType)).append("\n");
    sb.append("    albumTrackCount: ").append(toIndentedString(albumTrackCount)).append("\n");
    sb.append("    albumVanityId: ").append(toIndentedString(albumVanityId)).append("\n");
    sb.append("    artistId: ").append(toIndentedString(artistId)).append("\n");
    sb.append("    artistName: ").append(toIndentedString(artistName)).append("\n");
    sb.append("    primaryGenres: ").append(toIndentedString(primaryGenres)).append("\n");
    sb.append("    restricted: ").append(toIndentedString(restricted)).append("\n");
    sb.append("    secondaryGenres: ").append(toIndentedString(secondaryGenres)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
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
    openapiFields.add("album_copyright");
    openapiFields.add("album_coverart_100x100");
    openapiFields.add("album_coverart_350x350");
    openapiFields.add("album_coverart_500x500");
    openapiFields.add("album_coverart_800x800");
    openapiFields.add("album_edit_url");
    openapiFields.add("album_id");
    openapiFields.add("album_label");
    openapiFields.add("album_mbid");
    openapiFields.add("album_name");
    openapiFields.add("album_pline");
    openapiFields.add("album_rating");
    openapiFields.add("album_release_date");
    openapiFields.add("album_release_type");
    openapiFields.add("album_track_count");
    openapiFields.add("album_vanity_id");
    openapiFields.add("artist_id");
    openapiFields.add("artist_name");
    openapiFields.add("primary_genres");
    openapiFields.add("restricted");
    openapiFields.add("secondary_genres");
    openapiFields.add("updated_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Album
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Album.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Album is not found in the empty JSON string", Album.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Album.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Album` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("album_copyright") != null && !jsonObj.get("album_copyright").isJsonNull()) && !jsonObj.get("album_copyright").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_copyright` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_copyright").toString()));
      }
      if ((jsonObj.get("album_coverart_100x100") != null && !jsonObj.get("album_coverart_100x100").isJsonNull()) && !jsonObj.get("album_coverart_100x100").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_coverart_100x100` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_coverart_100x100").toString()));
      }
      if ((jsonObj.get("album_coverart_350x350") != null && !jsonObj.get("album_coverart_350x350").isJsonNull()) && !jsonObj.get("album_coverart_350x350").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_coverart_350x350` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_coverart_350x350").toString()));
      }
      if ((jsonObj.get("album_coverart_500x500") != null && !jsonObj.get("album_coverart_500x500").isJsonNull()) && !jsonObj.get("album_coverart_500x500").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_coverart_500x500` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_coverart_500x500").toString()));
      }
      if ((jsonObj.get("album_coverart_800x800") != null && !jsonObj.get("album_coverart_800x800").isJsonNull()) && !jsonObj.get("album_coverart_800x800").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_coverart_800x800` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_coverart_800x800").toString()));
      }
      if ((jsonObj.get("album_edit_url") != null && !jsonObj.get("album_edit_url").isJsonNull()) && !jsonObj.get("album_edit_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_edit_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_edit_url").toString()));
      }
      if ((jsonObj.get("album_label") != null && !jsonObj.get("album_label").isJsonNull()) && !jsonObj.get("album_label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_label").toString()));
      }
      if ((jsonObj.get("album_mbid") != null && !jsonObj.get("album_mbid").isJsonNull()) && !jsonObj.get("album_mbid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_mbid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_mbid").toString()));
      }
      if ((jsonObj.get("album_name") != null && !jsonObj.get("album_name").isJsonNull()) && !jsonObj.get("album_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_name").toString()));
      }
      if ((jsonObj.get("album_pline") != null && !jsonObj.get("album_pline").isJsonNull()) && !jsonObj.get("album_pline").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_pline` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_pline").toString()));
      }
      if ((jsonObj.get("album_release_date") != null && !jsonObj.get("album_release_date").isJsonNull()) && !jsonObj.get("album_release_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_release_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_release_date").toString()));
      }
      if ((jsonObj.get("album_release_type") != null && !jsonObj.get("album_release_type").isJsonNull()) && !jsonObj.get("album_release_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_release_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_release_type").toString()));
      }
      if ((jsonObj.get("album_vanity_id") != null && !jsonObj.get("album_vanity_id").isJsonNull()) && !jsonObj.get("album_vanity_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `album_vanity_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("album_vanity_id").toString()));
      }
      if ((jsonObj.get("artist_name") != null && !jsonObj.get("artist_name").isJsonNull()) && !jsonObj.get("artist_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `artist_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("artist_name").toString()));
      }
      // validate the optional field `primary_genres`
      if (jsonObj.get("primary_genres") != null && !jsonObj.get("primary_genres").isJsonNull()) {
        AlbumPrimaryGenres.validateJsonElement(jsonObj.get("primary_genres"));
      }
      // validate the optional field `secondary_genres`
      if (jsonObj.get("secondary_genres") != null && !jsonObj.get("secondary_genres").isJsonNull()) {
        AlbumSecondaryGenres.validateJsonElement(jsonObj.get("secondary_genres"));
      }
      if ((jsonObj.get("updated_time") != null && !jsonObj.get("updated_time").isJsonNull()) && !jsonObj.get("updated_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Album.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Album' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Album> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Album.class));

       return (TypeAdapter<T>) new TypeAdapter<Album>() {
           @Override
           public void write(JsonWriter out, Album value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Album read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Album given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Album
   * @throws IOException if the JSON string is invalid with respect to Album
   */
  public static Album fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Album.class);
  }

  /**
   * Convert an instance of Album to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

